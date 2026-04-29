from functools import wraps
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import User, B2BLead, Course
bp = Blueprint('admin', __name__)
def admin_required(f):
    @wraps(f)
    def w(*a, **k):
        if not current_user.is_authenticated or not current_user.is_admin: flash('Acesso negado.', 'error'); return redirect(url_for('main.index'))
        return f(*a, **k)
    return w
@bp.route('/')
@login_required
@admin_required
def index(): return render_template('admin/index.html', users=User.query.order_by(User.created_at.desc()).all(), leads=B2BLead.query.order_by(B2BLead.created_at.desc()).all(), courses=Course.query.all())
@bp.route('/usuario/<int:user_id>/toggle', methods=['POST'])
@login_required
@admin_required
def toggle(user_id):
    u=User.query.get_or_404(user_id)
    if u.id != current_user.id: u.is_active_user=not u.is_active_user; db.session.commit()
    return redirect(url_for('admin.index'))
@bp.route('/lead/<int:lead_id>/status', methods=['POST'])
@login_required
@admin_required
def lead_status(lead_id):
    l=B2BLead.query.get_or_404(lead_id); l.status=request.form.get('status','novo'); db.session.commit(); return redirect(url_for('admin.index'))
