# -*- encoding: utf-8 -*-
__author__ = 'tang'


# 导入suds.client模块下的Client类
# 用于调用WebService接口
from suds.client import Client
from flask import jsonify
from utils import process_res_data


wsdl_url = 'http://XX.XXX.XXX.XX/IFWebService/XXXX.asmx?wsdl'


def get_product_api():
    # 创建一个webservice接口对象
    client = Client(wsdl_url)
    # 调用这个接口下的GetAllProducts方法
    client.service.GetAllProducts()
    # 保存请求报文，因为返回的是一个实例，所以要转为字符串
    # req = str(client.last_sent())
    # 保存返回报文，返回的也是一个实例
    response = str(client.last_received())
    resp = process_res_data(response)
    res = dict()
    res['response'] = resp
    # jsonify的处理对象必须是字典dict
    resp_json = jsonify(res)
    return resp_json


def get_batch_api():
    client = Client(wsdl_url)
    # 调用这个接口下的GetBatchList方法
    client.service.GetBatchList()
    response = str(client.last_received())
    resp = process_res_data(response)
    res = dict()
    res['response'] = resp
    resp_json = jsonify(res)
    return resp_json
