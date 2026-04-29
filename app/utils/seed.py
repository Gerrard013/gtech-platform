import os
from app import db
from app.models import User, Course

def seed_admin_and_content():
    admin_email = os.getenv("ADMIN_EMAIL", "admin@gtech.com").lower().strip()
    admin_password = os.getenv("ADMIN_PASSWORD", "Admin@123456")
    admin = User.query.filter_by(email=admin_email).first()
    if not admin:
        admin = User(name="Administrador G Tech", email=admin_email, is_admin=True, plan="admin")
        admin.set_password(admin_password)
        db.session.add(admin)

    if Course.query.count() == 0:
        courses = [
            Course(title="Excel e Google Sheets para negócios", description="Do básico ao raciocínio analítico com filtros, PROCV/PROCX, tabelas e dashboards.", category="Dados", level="iniciante", duration="8h", is_free=True),
            Course(title="Power BI e indicadores executivos", description="Criação de dashboards, KPIs, storytelling de dados e visão para tomada de decisão.", category="BI", level="intermediário", duration="16h", is_free=False),
            Course(title="Python para análise de dados", description="Pandas, automação de planilhas, leitura de arquivos e geração de relatórios.", category="Python", level="intermediário", duration="20h", is_free=True),
            Course(title="RPA com Python para empresas", description="Automação de tarefas repetitivas, downloads, arquivos, PDFs, planilhas e sistemas web.", category="RPA", level="avançado", duration="24h", is_free=False),
        ]
        db.session.add_all(courses)
    db.session.commit()
