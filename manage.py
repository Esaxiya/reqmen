from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from config.exts import db

# 以下几个必须导入、即使不使用、初始化数据库时需要
from config.models import System
from config.models import Api
from config.models import Case
from config.models import Suite
from config.models import Env

# 用于处理一组命令的控制器类
manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manger中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
