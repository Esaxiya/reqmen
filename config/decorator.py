from functools import wraps
from flask import session
from flask import redirect
from flask import url_for


# 登陆状态验证装饰器
def required_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
