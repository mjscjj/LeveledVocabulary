#!/usr/bin/env python3
# encoding: utf-8
# @File: config.py
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-07 11:52

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """基础配置，导入所有配置中"""
    # 密匙
    SECRET_KEY = os.environ.get('SECRET_KEY') or "SecretKey"

    # 数据库自动提交数据
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

    # 查询耗时过长的时间
    SLOW_DB_QUERY_TIME = 0.5

    # 发送邮件时使用TLS安全协议 默认为False
    MAIL_USE_TLS = False

    # 发送邮件时使用SSL安全协议 默认为False
    MAIL_USE_SSL = True

    # 发送邮件所用的邮箱用户名以及密码
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '你的邮箱@test.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '你的邮箱密码'

    # 管理员邮箱
    ADMIN_MAIL = os.environ.get('ADMIN_EMAIL') or '你的邮箱@test.com'
    # 管理员账号 默认为admin 可修改 第一次运行时会自动注册
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    # 管理员密码 默认为admin 可修改 第一次运行时会自动注册
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'admin'
    # SSL安全协议开关 False会打开
    SSL_DISABLE = True

    # 禁止转换asc码
    JSON_AS_ASCII = False

    # 存储图片的位置
    UPLOAD_FOLDER = 'app//static//image'

    # 分页设置 每页显示数量
    POSTS_PER_PAGE = 15

    # 配置类可以定义 init_app() 类方法，其参数是程序实例。
    # 在这个方法中，可以执行对当前 环境的配置初始化。
    # 现在，基类 Config 中的 init_app() 方法为空。
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发配置 以及开发时使用的数据库地址"""
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@Ab323637@127.0.0.1:3306/locdata'


class ProductionConfig(Config):
    """正常使用时的配置 以及数据库地址 发生错误时自动发送邮件"""
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@Ab323637@127.0.0.1:3306/locdata'
    # @classmethod
    # def init_app(cls, app):
    #     Config.init_app(app)
    #
    #     # 发生错误时自动发送错误日志到管理员邮箱
    #     import logging
    #     from logging.handlers import SMTPHandler
    #
    #     credentials = None  # 凭证
    #     secure = None  # 安全保护
    #
    #     if getattr(cls, 'MAIL_USERNAME', None) is not None:
    #         credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
    #         if getattr(cls, 'MAIL_USE_TLS', None):
    #             secure = ()
    #     # 邮件处理设置
    #     mail_handler = SMTPHandler(
    #         mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
    #         fromaddr=cls.MAIL_SENDER,
    #         toaddrs=[cls.ADMIN_MAIL],
    #         subject=cls.MAIL_SUBJECT_PREFIX + "网站发生错误",
    #         credentials=credentials,
    #         secure=secure)
    #     # 设置此处理程序的日志级别
    #     mail_handler.setLevel(logging.ERROR)
    #     # 给app添加错误处理程序
    #     app.logger.addHandler(mail_handler)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
