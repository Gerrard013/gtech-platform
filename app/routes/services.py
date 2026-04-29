from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from app import db
from app.models import B2BLead
bp = Blueprint('services', __name__)
@bp.route('/')
def index(): return render_template('services/index.html')
@bp.route('/solicitar', methods=['POST'])
def solicitar():
    vals={k:request.form.get(k,'').strip() for k in ['name','email','company','service','description']}
    if not all(vals.values()): flash('Preencha todos os campos.', 'error'); return redirect(url_for('services.index')+'#orcamento')
    db.session.add(B2BLead(**vals, user_id=current_user.id if current_user.is_authenticated else None)); db.session.commit(); flash('Solicitação enviada. A G Tech vai analisar seu caso.', 'success')
    return redirect(url_for('services.index')+'#orcamento')
