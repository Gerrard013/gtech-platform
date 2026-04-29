from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Course, ChatMessage, B2BLead
bp = Blueprint('dashboard', __name__)
@bp.route('/')
@login_required
def index():
    return render_template('dashboard/index.html', courses=Course.query.limit(4).all(), messages=ChatMessage.query.filter_by(user_id=current_user.id).count(), leads=B2BLead.query.filter_by(user_id=current_user.id).count())
