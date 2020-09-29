# -*- encoding: utf-8 -*-
__author__ = 'tang'


import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
# 前后端分离
# 在开发调试阶段，本地的flask测试服务器需要允许跨域访问
from flask_cors import CORS

from webservice import get_product_api
from webservice import get_batch_api


app = Flask(__name__)
# 初始化的时候加载配置
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = "hard to guess string"
app.config['UPLOAD_FOLDER'] = 'static\uploads'


@app.route('/api/product', methods=['POST', 'GET'])
def product_from_webservice():
    resp_json = get_product_api()
    # make_response封装数据并类型转换
    response = app.make_response(resp_json)
    # 设置头文件，允许跨域访问
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    return response


@app.route('/api/batch', methods=['POST', 'GET'])
def batch_from_webservice():
    resp_json = get_batch_api()
    response = app.make_response(resp_json)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    return response


@app.route('/api/files_from_frontend', methods=['POST'])
def get_files_from_frontend():
    if request.method == 'POST':
        print request.files
        try:
            if 'fileData' in request.files:
                blob_file = request.files['fileData']
                # secure_filename function returns a ASCII only string
                # 文件名中包含的非法字符【< > : " / \ | ? *】、中文字符会被抛弃
                # file_name = secure_filename(blob_file.filename)
                file_name = blob_file.filename
                print file_name
                blob_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], file_name))
                response = app.make_response(jsonify({'status': 'Uploaded file successfully :)'}))
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
                return response
        except Exception as e:
            print e
        return jsonify('Ops! Uploading failed :(')


if __name__ == '__main__':
    app.run(debug=True)
