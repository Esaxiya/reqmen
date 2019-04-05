from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from config.models import Api
from config.models import System
from config.models import User
from config.exts import db


def api_show(sys_id):
    """
        前台页面需要使用到
        system项目信息、
        api接口信息
    """
    content = {
        'system': System.query.filter(System.id == sys_id).first(),
        'apis': Api.query.filter(Api.sys_id == sys_id).all()
    }
    print(content)
    return render_template('api.html', **content)


def api_add():
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    sys_id = request.form.get('system')
    system = System.query.filter(System.id == sys_id).first()
    name = request.form.get('name')
    method = request.form.get('method')
    path = request.form.get('path')
    contentType = request.form.get('contentType')
    body = request.form.get('body').replace("\r", "").replace("\n", '')
    header = request.form.get('body').replace("\r", "").replace("\n", '')
    api = Api(name=name, method=method, path=path, contentType=contentType,
              body=body, header=header, system=system)
    api.user = user
    api.user_id = user_id
    db.session.add(api)
    db.session.commit()
    return redirect(url_for('api', sys_id=sys_id))


def api_remove(api_id):
    api = Api.query.filter(Api.id == api_id).first()
    sys_id = api.sys_id
    db.session.delete(api)
    db.session.commit()
    return redirect(url_for('api', sys_id=sys_id))
