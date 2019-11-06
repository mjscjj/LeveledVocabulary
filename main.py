#!/usr/bin/env python3
# encoding: utf-8
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-07 11:11

from flask_script import Manager
from app import create_app

app = create_app('production')

manager = Manager(app)

# @app.route('/')
# def index():
#     return 'Index Page'
#
#
# @app.route('/hello')
# def hello():
#     return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True, port=80,host='0.0.0.0')  # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
