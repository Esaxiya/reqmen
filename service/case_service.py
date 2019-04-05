from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import session
from config.models import Case
from config.models import System
from config.models import Api
from config.models import User
from config.models import Env
from config.exts import db


def case_show(sys_id):
    content = {
        'system': System.query.filter(System.id == sys_id).first(),
        'apis': Api.query.filter(Api.sys_id == sys_id).all(),
        "cases": Case.query.filter(Case.sys_id == sys_id).all(),
        "envs": Env.query.filter(Env.sys_id == sys_id).all()
    }
    return render_template('case.html', **content)


def case_add():
    user_id = session['user_id']
    name = request.form.get('name')
    sys_id = request.form.get('system')
    api_id = request.form.get('api_id')
    body = request.form.get('body')
    user = User.query.filter(User.id == user_id).first()
    api = Api.query.filter(Api.id == api_id).first()
    system = System.query.filter(System.id == sys_id).first()
    case = Case(name=name,
                api_name=api.name,
                method=api.method,
                api_id=api.id,
                path=api.path,
                contentType=api.contentType,
                header=api.header,
                system=api.system,
                sys_id=api.sys_id,
                user=user,
                user_id=user_id)
    case.body = body or api.body
    db.session.add(case)
    db.session.commit()
    return redirect(url_for('case', sys_id=sys_id))


def case_remove(case_id):
    case = Case.query.filter(Case.id == case_id).first()
    sys_id = case.sys_id
    db.session.delete(case)
    db.session.commit()
    return redirect(url_for('case', sys_id=sys_id))
