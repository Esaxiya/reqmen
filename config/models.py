from datetime import datetime
from .exts import db


class User(db.Model):
    """
    用户模型
    __tablename__ = 'user'  数据库中表的名称
    这是SQLAlchemy所必需的;
    但是，如果模型定义了主键，Flask-SQLAlchemy将自动设置它。
    如果明确设置__table __或__tablename__，则将使用它。
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(11), nullable=False, )
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class System(db.Model):
    """
    项目模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('systems'))


class Api(db.Model):
    """
    http api 接口模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    path = db.Column(db.String(200), nullable=False)
    body = db.Column(db.String(200), nullable=True)
    header = db.Column(db.String(200), nullable=True)
    contentType = db.Column(db.String(200), nullable=False)
    # now() 服务器第一次运行的时间、now是每次创建模型的时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    sys_id = db.Column(db.Integer, db.ForeignKey('system.id'))
    system = db.relationship('System', backref=db.backref('apis'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('apis'))


class Case(db.Model):
    """
    http case 模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    api_name = db.Column(db.String(50), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    path = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=True)
    header = db.Column(db.Text, nullable=True)
    contentType = db.Column(db.String(500), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0, comment="执行状态:0未执行;1执行成功;2执行失败")
    # now() 服务器第一次运行的时间、now是每次创建模型的时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    sys_id = db.Column(db.Integer, db.ForeignKey('system.id'))
    system = db.relationship('System', backref=db.backref('cases'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('cases'))
    api_id = db.Column(db.Integer, db.ForeignKey('api.id'))
    api = db.relationship('Api', backref=db.backref('cases'))


class Suite(db.Model):
    """
    http suite 模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Env(db.Model):
    """
    测试环境
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    domain = db.Column(db.String(20), nullable=False)
    host = db.Column(db.String(20), nullable=False)
    port = db.Column(db.String(5), nullable=False)
    resp = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    sys_id = db.Column(db.Integer, db.ForeignKey('system.id'))
    system = db.relationship('System', backref=db.backref('envs'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('envs'))


class Question(db.Model):
    """
    问答模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Comment(db.Model):
    """
    评论模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
