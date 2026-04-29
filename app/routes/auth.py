import os, re
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from flask_login import login_user, logout_user, login_required, current_user
from authlib.integrations.flask_client import OAuth
from app import db, limiter
from app.models import User

bp = Blueprint('auth', __name__)
oauth = OAuth()
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

def google_client():
    oauth.init_app(current_app)
    if 'google' not in oauth._clients:
        oauth.register(
            name='google', client_id=current_app.config.get('GOOGLE_CLIENT_ID'), client_secret=current_app.config.get('GOOGLE_CLIENT_SECRET'),
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration', client_kwargs={'scope':'openid email profile'}
        )
    return oauth.google

@bp.route('/login', methods=['GET','POST'])
@limiter.limit('10 per minute')
def login():
    if current_user.is_authenticated: return redirect(url_for('dashboard.index'))
    if request.method == 'POST':
        email = request.form.get('email','').lower().strip(); password = request.form.get('password','')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password) and user.is_active:
            user.last_login = datetime.utcnow(); db.session.commit(); login_user(user, remember=bool(request.form.get('remember')))
            return redirect(request.args.get('next') or url_for('dashboard.index'))
        flash('E-mail ou senha inválidos.', 'error')
    return render_template('auth/login.html')

@bp.route('/cadastro', methods=['GET','POST'])
@limiter.limit('8 per minute')
def register():
    if current_user.is_authenticated: return redirect(url_for('dashboard.index'))
    if request.method == 'POST':
        name = request.form.get('name','').strip(); email = request.form.get('email','').lower().strip(); password = request.form.get('password','')
        if len(name) < 2 or not EMAIL_RE.match(email) or len(password) < 8:
            flash('Confira nome, e-mail e senha com mínimo de 8 caracteres.', 'error'); return render_template('auth/register.html')
        if User.query.filter_by(email=email).first(): flash('Este e-mail já está cadastrado.', 'error'); return render_template('auth/register.html')
        user = User(name=name, email=email); user.set_password(password); db.session.add(user); db.session.commit(); login_user(user)
        return redirect(url_for('dashboard.index'))
    return render_template('auth/register.html')

@bp.route('/google')
def google_login():
    if not current_app.config.get('GOOGLE_CLIENT_ID') or not current_app.config.get('GOOGLE_CLIENT_SECRET'):
        flash('Login Google ainda não configurado nas variáveis.', 'info'); return redirect(url_for('auth.login'))
    return google_client().authorize_redirect(url_for('auth.google_callback', _external=True))

@bp.route('/google/callback')
def google_callback():
    token = google_client().authorize_access_token(); info = token.get('userinfo')
    if not info: info = google_client().parse_id_token(token)
    email = info['email'].lower(); user = User.query.filter_by(email=email).first()
    if not user:
        user = User(name=info.get('name','Usuário G Tech'), email=email, google_id=info.get('sub')); db.session.add(user)
    user.google_id = info.get('sub'); user.last_login = datetime.utcnow(); db.session.commit(); login_user(user)
    return redirect(url_for('dashboard.index'))

@bp.route('/logout')
@login_required
def logout(): logout_user(); return redirect(url_for('main.index'))
