from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for

from config.models import System
from config.models import User
from config.exts import db


def system_show():
    content = {
        "systems": System.query.order_by('create_time').all()
    }
    return render_template('system.html', **content)


def system_add():
    name = request.form.get('name')
    description = request.form.get('description')
    system = System(name=name, description=description)
    # 获取当前登陆的用户的信息
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    system.user = user
    db.session.add(system)
    db.session.commit()
    return redirect(url_for('system'))


def system_remove(sys_id):
    system = System.query.filter(System.id == sys_id).first()
    db.session.delete(system)
    db.session.commit()
    return redirect(url_for('system'))
