from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import session

from config.models import User
from config.models import Env
from config.models import System
from config.exts import db


def env_show(sys_id):
    content = {
        "envs": Env.query.filter(Env.sys_id == sys_id).all(),
        'sys_id': sys_id
    }
    return render_template('env.html', **content)


def env_add():
    # 获取当前登陆的用户的信息
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    sys_id = request.form.get("system")
    name = request.form.get('name')
    domain = request.form.get('domain')
    host = request.form.get('host')
    port = request.form.get('port')
    resp = request.form.get('resp')

    env = Env(name=name, domain=domain, host=host, port=port, resp=resp)
    env.user = user
    env.user_id = user_id
    env.sys_id = sys_id
    env.system = System.query.filter(System.id == sys_id).first()
    db.session.add(env)
    db.session.commit()
    return redirect(url_for('env', sys_id=sys_id))
