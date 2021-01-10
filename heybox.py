# -*- coding: UTF-8 -*-

"""

 * @author  zfj

 * @date  2020/9/26 15:39

"""

import sys
import time
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
try:
    if len(sys.argv)==4 or len(sys.argv)==5:
        app_id = sys.argv[1]
        Authorization = sys.argv[2]
        Energy_code = sys.argv[3]
    else:
        print("缺少必要参数！！！")
except Exception as e:
    print(e)

sign_path = ''

def apiRequest_get(url,cookie,params):
    params_get = params
    headers_get = {
        'Cache-Control': 'Cache-Control:public,no-cache',
        'Referer': 'http://api.maxjia.com/'
        'Accept-Encoding': 'gzip',
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 ApiMaxJia/1.0'
        'Connection': 'Keep-Alive',
        'Host': 'api.xiaoheihe.cn'
        'Cookie': cookie
    }
    
    try:
        with requests.get(url, headers=headers_get, params=params_get, verify=False, timeout=300) as resp:
            res = resp.json()
            return res
    except Exception as ex:
        print(ex)

def mimikko(cookie):
    sign_data = apiRequest_get(sign_path,cookie,"")
    if sign_data:
        if sign_data.get('status')=="ok":
            sign_result_post = '签到成功：' + sign_data['msg']
        else:
            sign_result_post = '签到失败，今日已签到'
    else:
        sign_result_post = '签到请求失败'

print(sign_result_post)
try:
    if len(sys.argv)==5:
        SCKEY = sys.argv[4]
        # print("有SCKEY")
        print("正在推送到微信")
        post_info = "?text=小黑盒每日签到&desp=<p>" + sign_result_post
        post_data = requests.get(server_api + SCKEY + '.send' + post_info)
        print(post_data)
    else:
        print("没有SCKEY")
except Exception as e:
    print(e)
