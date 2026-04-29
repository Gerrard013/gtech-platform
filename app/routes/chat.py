import os
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app import db, csrf, limiter
from app.models import ChatMessage
bp = Blueprint('chat', __name__)

def answer(text):
    key = text.lower()
    if os.getenv('OPENAI_API_KEY'):
        try:
            from openai import OpenAI
            c=OpenAI(); r=c.chat.completions.create(model='gpt-4o-mini', messages=[{'role':'system','content':'Você é o mentor IA da G Tech. Ajude com educação, BI, Python, Excel, RPA e negócios. Seja claro, prático e profissional.'},{'role':'user','content':text}], max_tokens=500)
            return r.choices[0].message.content
        except Exception: pass
    if 'rpa' in key or 'automat' in key: return 'RPA é automação de processos repetitivos. Na G Tech, o caminho prático é mapear a tarefa, padronizar entradas, automatizar com Python e medir horas economizadas.'
    if 'bi' in key or 'dashboard' in key: return 'BI transforma dados em decisão. Comece definindo KPIs, fonte dos dados, limpeza, modelo e visual executivo.'
    if 'python' in key: return 'Python é excelente para dados e automação. Foque em pandas, openpyxl, requests e organização de scripts em funções.'
    return 'Sou o assistente IA da G Tech. Posso ajudar com BI, Python, Excel, RPA, carreira e soluções para empresas.'

@bp.route('/')
@login_required
def index(): return render_template('chat/index.html', messages=ChatMessage.query.filter_by(user_id=current_user.id).order_by(ChatMessage.created_at.asc()).limit(80).all())

@bp.route('/send', methods=['POST'])
@login_required
@csrf.exempt
@limiter.limit('20 per minute')
def send():
    data=request.get_json() or {}; text=(data.get('message') or '').strip()
    if not text: return jsonify({'error':'Mensagem vazia'}),400
    db.session.add(ChatMessage(user_id=current_user.id, role='user', content=text)); resp=answer(text)
    db.session.add(ChatMessage(user_id=current_user.id, role='assistant', content=resp)); db.session.commit()
    return jsonify({'response':resp})
