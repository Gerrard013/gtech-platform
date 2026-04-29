import os
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
bp = Blueprint('pricing', __name__)
@bp.route('/')
def index(): return render_template('pricing/index.html')
@bp.route('/checkout/<plan>', methods=['POST'])
@login_required
def checkout(plan):
    prices={'pro':29.90,'b2b':249.90}
    if plan not in prices: flash('Plano inválido.', 'error'); return redirect(url_for('pricing.index'))
    token=os.getenv('MERCADO_PAGO_ACCESS_TOKEN')
    if not token: flash('Pagamento ainda não configurado. Use o contato/orçamento por enquanto.', 'info'); return redirect(url_for('pricing.index'))
    import mercadopago
    sdk=mercadopago.SDK(token); pref={"items":[{"title":f"G Tech {plan.upper()}","quantity":1,"unit_price":prices[plan],"currency_id":"BRL"}],"payer":{"email":current_user.email,"name":current_user.name},"back_urls":{"success":url_for('pricing.success', plan=plan, _external=True),"failure":url_for('pricing.index', _external=True),"pending":url_for('pricing.index', _external=True)}}
    return redirect(sdk.preference().create(pref)['response']['init_point'])
@bp.route('/sucesso/<plan>')
@login_required
def success(plan): current_user.plan=plan; db.session.commit(); flash('Plano ativado com sucesso.', 'success'); return redirect(url_for('dashboard.index'))
