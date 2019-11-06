#!/usr/bin/env python3
# encoding: utf-8
# @File: __init__.py
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-07 12:52
from flask import Flask
from config import config
from flask_mail import Mail
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy

mail = Mail()
bootstrap = Bootstrap()
# db = SQLAlchemy()


def create_app(config_name):
    """程序工厂函数"""

    # app = Flask(__name__, static_folder='/Users/chujiejie/workspace/framework/word_classification/app/static')
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@Ab323637@127.0.0.1:3306/locdata'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 进行app配置 把自己的config设定导入到app中

    mail.init_app(app)
    bootstrap.init_app(app)
    # with app.app_context():
    #     db.init_app(app)

    # from_object会把参数的所有的大写名属性导入到app的config中
    app.config.from_object(config[config_name])
    # 初始化app配置
    config[config_name].init_app(app)

    # 设置session设置的过期时间 也就是关闭浏览器5分钟内不用重新登录
    # app.permanent_session_lifetime = timedelta(minutes=30)

    # 在程序中注册蓝本
    from app.controller import controller
    from app.runner import error
    app.register_blueprint(error)
    app.register_blueprint(controller)


    # 启动log
    # with app.app_context():
    from app.log import logs
    logs.init_log('./log/app', app.logger)  # 初始化app.logger

    return app
