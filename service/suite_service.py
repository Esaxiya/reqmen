from flask import render_template
from flask import url_for
from flask import session
from flask import request
from flask import redirect

from config.models import Suite
from config.models import Env
from config.models import System
from config.models import User

from config.exts import db


def suite_show(sys_id):
    content = {
        'system': System.query.filter(System.id == sys_id).first(),
        "envs": Env.query.filter(Env.sys_id == sys_id).all(),
        "suites": Suite.query.filter(Suite.sys_id == sys_id).all()
    }
    return render_template('suite.html', **content)


def suite_add():
    user_id = session['user_id']
    name = request.form.get('name')
    sys_id = request.form.get('system')
    user = User.query.filter(User.id == user_id).first()
    system = System.query.filter(System.id == sys_id).first()
    desp = request.form.get('desp')
    suite = Suite(name=name, desp=desp)
    suite.sys_id = sys_id
    suite.system = system
    suite.user = user
    suite.user_id = user_id
    db.session.add(suite)
    db.session.commit()
    return redirect(url_for('suite', sys_id=sys_id))


def suite_remove(suite_id):
    pass


def suite_update():
    pass
