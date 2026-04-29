from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Course
bp = Blueprint('education', __name__)
@bp.route('/')
@login_required
def index(): return render_template('education/index.html', courses=Course.query.order_by(Course.created_at.desc()).all())
