from flask import request
from flask import session
from flask import url_for
from flask import redirect
from flask import render_template
from config.models import User
from config.exts import db


def login_service():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone = request.form.get('phone')
        password = request.form.get('password')
        user = User.query.filter(User.phone == phone).first()
        if not user:
            return '手机未注册、请先进行注册'
        else:
            if password == user.password:
                session['user_id'] = user.id  # 添加session 保持登陆状态
                session.permanent = True  # 如果向在31天内无需在登陆、设置如下
                return redirect(url_for('index'))
            else:
                return "手机号、或密码错误、请重新输入"


def register_service():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        phone = request.form.get('phone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # 手机号码验证、如果注册过就不能注册
        user = User.query.filter(User.phone == phone).first()
        if user:
            return '该手机号吗已经被注册、请检查'
        else:
            # 检查两次密码输入是否相同、相同才可以注册
            if password1 != password2:
                return "两次密码输入不一致、请重新输入"
            else:
                user = User(phone=phone, username=username, password=password1, )
                db.session.add(user)
                db.session.commit()
                # 注册成功、页面跳转到登陆页面
                return redirect(url_for('login'))
