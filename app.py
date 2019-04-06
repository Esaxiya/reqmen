from flask import Flask
from flask import session
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from config import config
from config.exts import db

# 导入模型中原型
from config.models import System
from config.models import User

# 导入service层相关业务处理逻辑控制
from service.base_service import login_service
from service.base_service import register_service
from service.system_service import system_show
from service.system_service import system_add
from service.system_service import system_remove
from service.api_service import api_show
from service.api_service import api_add
from service.api_service import api_remove
from service.case_service import case_show
from service.case_service import case_add
from service.case_service import case_remove
from service.env_service import env_show
from service.env_service import env_add
from service.env_service import env_remove
from service.question_service import question_service
from service.question_service import detail_service
from service.question_service import add_comment_service
from service.question_service import content_show
from service.suite_service import suite_add
from service.suite_service import suite_remove
from service.suite_service import suite_show
from service.suite_service import suite_update

# 访问限制、必须登陆才可以、必须放到路由装饰器的下面、否则不起作用
from config.decorator import required_login

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

"""
    本模块主要用是--路由转发、
    业务逻辑实际通过service层来实现
    Flask默认request对象、已经收集了前端传入的特定数据
    除非特殊传递参数、如path位置、否则只想使用位置导入request即可获取数据
"""


@app.context_processor
def my_context_process():
    """
    上下文处理、添加到这里返回的、在每个页面都可以接收到哦
    """
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


@app.route("/")
@required_login
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
        登陆功能
    """
    return login_service()


@app.route('/logout')
def logout():
    """
        退出登陆
        session.pop('user_id') 或 del session['user_id'] 或 session.clear()
    """
    session.clear()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    注册功能
    """
    return register_service()


# ============================================


@app.route("/system", methods=['GET'])
@required_login
def system():
    """
        显示项目列表
    """
    return system_show()


@app.route("/system/new", methods=['GET', 'POST'])
@required_login
def system_new():
    """
    POST、新增项目
    """
    return system_add()


@app.route("/system/delete/<sys_id>")
@required_login
def system_delete(sys_id):
    """
        删除特定的项目、及其管理内容
    """
    return system_remove(sys_id)


@app.route("/system/update")
@required_login
def system_update():
    """
    项目更新信息
    """


# ============================================

@app.route("/api/<sys_id>", methods=['GET'])
@required_login
def api(sys_id):
    """
    指定项目的接口数据
    GET、  展示接口数据列表
    """
    return api_show(sys_id)


@app.route("/api/new", methods=['GET', 'POST'])
@required_login
def api_new():
    """
        POST、添加指定项目接口数据
    """
    return api_add()


@app.route("/api/delete/<api_id>")
@required_login
def api_delete(api_id):
    """
    删除指定接口数据、
    重定向到当前项目的接口列表显示页面
    """
    return api_remove(api_id)


@app.route("/api/update")
@required_login
def api_update():
    """
    更新接口信息
    """


# ============================================

@app.route("/case/<sys_id>", methods=['GET'])
@required_login
def case(sys_id):
    """
    GET、获取指定项目的测试用例
    """
    return case_show(sys_id)


@app.route("/case/new", methods=['GET', 'POST'])
@required_login
def case_new():
    """
    POST、新增指定项目的测试用例、依据接口信息
    """
    return case_add()


@app.route("/case/delete/<case_id>", methods=['GET'])
@required_login
def case_delete(case_id):
    """
    删除指定的测试用例
    """
    return case_remove(case_id)


@app.route("/case/update")
@required_login
def case_update():
    """
    更新指定项目的测试用例
    """


# ============================================
@app.route("/suite/<sys_id>", methods=['GET', 'POST'])
@required_login
def suite(sys_id):
    """
    获取测试用例集列表
    """
    return suite_show(sys_id)


@app.route("/suite/new", methods=['GET', 'POST'])
@required_login
def suite_new():
    """
    新增测试集
    """
    return suite_add()


@app.route("/suite/delete/<suite_id>", methods=['GET', 'POST'])
def suite_delete(suite_id):
    """
    删除测试集
    """
    return suite_remove(suite_id)


@app.route("/suite/update", methods=['GET', 'POST'])
@required_login
def suite_update():
    """
    更新测试集
    """
    return suite_update


# ============================================
@app.route("/env/<sys_id>", methods=['GET'])
@required_login
def env(sys_id):
    """
    测试环境展示
    """
    return env_show(sys_id)


@app.route("/env/new", methods=['POST'])
@required_login
def env_new():
    """
    测试环境添加
    """
    return env_add()


@app.route("/env/delete/<env_id>", methods=['GET', 'POST'])
@required_login
def env_delete(env_id):
    """
    删除测试环境
    """
    return env_remove(env_id)


@app.route("/env/update", methods=['GET', 'POST'])
@required_login
def env_update():
    """
    更新测试环境
    """


# ============================================

@app.route('/content', methods=['GET'])
@required_login
def content():
    """
    问答内容列表展示页面
    """
    return content_show()


@app.route('/add/question', methods=['GET', 'POST'])
@required_login
def question_new():
    """
    问答添加页面
    """
    return question_service()


@app.route('/detail/<question_id>')
@required_login
def detail(question_id):
    """
    问答详情页面
    """
    return detail_service(question_id)


@app.route('/add/comment', methods=["POST"])
@required_login
def add_comment():
    """
    添加评论
    """
    return add_comment_service()


# ============================================


if __name__ == '__main__':
    app.run(debug=True)
