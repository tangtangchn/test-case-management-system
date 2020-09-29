# -*- encoding: utf-8 -*-
__author__ = 'tang'


import re


def process_res_data(resp):
    resp_list = []
    resp = resp.split('\n')
    for item in resp:
        extract = re.findall("<string>.*</string>", item)
        for el in extract:
            el = el.replace('<string>', '')
            el = el.replace('</string>', '')
            resp_list.append(el)
    return resp_list
