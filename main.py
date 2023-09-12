# coding=utf-8

import pymysql
import os
import threading
import time
import logging
import requests
from subprocess import call
# import socket
# import json
# import datetime
from urllib.error import HTTPError
import urllib.request

username = os.environ['MY_USER']  # root
password = os.environ['MY_PASS']  # 123456
dbhost = os.environ['DB_HOST']  # "192.168.100.20"
dbname = os.environ['DB_NAME']  # "test"
print("Running with user: %s" % username)


# Line Notify
def send_notify(token, msg, filepath=None, stickerPackageId=None, stickerId=None):
    payload = {'message': msg}
    headers = {
        "Authorization": "Bearer " + token
    }
    if stickerPackageId and stickerId:
        payload['stickerPackageId'] = stickerPackageId
        payload['stickerId'] = stickerId

    if filepath:
        attachment = {'imageFile': open(filepath, 'rb')}
        print(attachment)
        r = requests.post("https://notify-api.line.me/api/notify",
                          headers=headers, params=payload, files=attachment)
    else:
        print("attachment")
        r = requests.post("https://notify-api.line.me/api/notify",
                          headers=headers, params=payload)
    return r.status_code, r.text


def connectdb():
    print('連接mysql...')
    logging.debug('連接mysql...')
    db = pymysql.connect(host=dbhost, port=3306, user=username,
                         password=password, database=dbname)
    print('連上了!')
    logging.debug('連上了!')
    return db


def closedb(db):
    db.close()


# # 每隔10秒钟执行


# def t2():
#     while 1:
#         main()
#         time.sleep(10)

if __name__ == '__main__':
    token = "b5egoBtbAjpPs3mku154xWPZAjvlSJH2r31nYfoj5nJ"  # test
    try:
        db = connectdb()    # 连接MySQL数据库
        closedb(db)         # 关闭数据库
        send_notify(token=token, msg='test0...', filepath='')
    except:
        send_notify(token=token, msg='test1...', filepath='')
        print('連接mysql...失敗')

    os.exit()
