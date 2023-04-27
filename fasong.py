# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core import mail
from django.conf import settings
from django.shortcuts import HttpResponse
from django.contrib import messages
from bmi.models import User
from django.db.models import F
from random import choice
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import os
import re
import time
import base64
import ddddocr
import requests
from interval import Interval
import datetime
import random


def youjian(request):
    while True:
      list_d="false"
      while list_d=="false":
        yzm = random.randint(1, 99)
        yzm1 = str(yzm)
        yzmid = '305091027159415831064757851596' + yzm1
        ph = random.randint(1, 30)
        photo = str(ph)
        guanliList=[[2103529,"Cxy525.."],[2103533,"LWiuei294"],[2103504,"Myq2022320"],[2003668,"Awoaiganlu1"],[2103491,"Xx2103491"],[2204516,"040214Yjg"],[2204517,"wF20040519"],[2204520,"Zz2152363195"]]
        
        heards11 = [["Mozilla/5.0 (Linux; Android 12; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36"],["Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1"]]
        guanliLst1=choice(guanliList)
        heards112=choice(heards11)
        username = guanliLst1[0]
        passw = guanliLst1[1]
        passw = ''.join(str(i) for i in passw)
        print("----------------开发密码:" + passw + "正在访问-----------------------")
        pwd = passw.encode()
        key = b'1234123412ABCDEF'
        iv = b'ABCDEF1234123412'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(pwd, AES.block_size))
        passwd = encrypted.hex()
        
        url_1 = "http://szxy.cqtbi.edu.cn/cqdddt/bsdt!createVertifyCode.action?checkId=" + yzmid
        url = 'http://szxy.cqtbi.edu.cn/cqdddt/bsdt!loginCheck.action'
        headers = {
            
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': heards112[0],
        }
        headers_1 = {
            
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': heards112[0],
        }
        c = requests.get(url=url_1, headers=headers_1,verify=False).content
        with open("daka" + photo + ".png", "wb") as fb:
            fb.write(c)
            ocr = ddddocr.DdddOcr()
        with open('daka'+ photo + '.png', 'rb') as f:
            img_bytes = f.read()
            res = ocr.classification(img_bytes)
            print("验证码:" + res)
            
        data = {
            'des': '1',
            'user_code': username,
            'pwd': passwd,
            'checkId': yzmid,
            'checkcode': res,
        }
        r = requests.post(url=url,headers=headers,data=data,verify=False).text
        success=re.findall('success.*?(\w+)', r)
        list_d = ''.join(str(i) for i in success)
        print(list_d) 
      ticket=re.findall('ticket.*?(\w+)', r)
      tick = ''.join(str(i) for i in ticket)
      print(tick)
      print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time()))))
      headers_ssid = {
          'Host': '2class.cqtbi.edu.cn',
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/4G Language/zh_CN',
      }
      res_ssid = requests.get(url='https://2class.cqtbi.edu.cn/Admin/Index/cqtbiSSO?PORTAL_TICKET=' + tick + '',
                              headers=headers_ssid)
      list1 = [res_ssid.request.headers]
      list2 = [str(i) for i in list1]
      list3 = ''.join(list2)
      s = re.findall('SSID=.*\w+', list3)
      for cookies in s:
          cookie = cookies
      url_p = 'https://2class.cqtbi.edu.cn/Student/Activity/getActivityCanApply.html'
      headers_p = {
          "Host": "2class.cqtbi.edu.cn",
          "Cookie": cookies
      }
  
      a = requests.post(url=url_p, headers=headers_p).text
      s = a.encode('utf-8').decode('unicode_escape')
      hdid = re.findall(r"activityID\":\"(.*?)\",\"activityName\"", s)
      hdname = re.findall(r"activityName\":\"(.*?)\",\"applyStartDate\"", s)
      start = re.findall(r"applyStartDate\":\"(.*?)\",\"applyEndDate\"", s)
      print("等待活动数据更新")
      time.sleep(120)
      print("开始二轮查询")
      headers_ssid = {
          'Host': '2class.cqtbi.edu.cn',
          'User-Agent': heards112[0],
      }
      res_ssid = requests.get(url='https://2class.cqtbi.edu.cn/Admin/Index/cqtbiSSO?PORTAL_TICKET=' + tick + '',
                              headers=headers_ssid)
      list1 = [res_ssid.request.headers]
      list2 = [str(i) for i in list1]
      list3 = ''.join(list2)
      s = re.findall('SSID=.*\w+', list3)
      for cookies in s:
          cookie = cookies
      url_p = 'https://2class.cqtbi.edu.cn/Student/Activity/getActivityCanApply.html'
      headers_p = {
          "Host": "2class.cqtbi.edu.cn",
          "Cookie": cookies
      }
      a = requests.post(url=url_p, headers=headers_p).text
      s = a.encode('utf-8').decode('unicode_escape')
      # print(hdid2)
      hdid2=re.findall(r"activityID\":\"(.*?)\",\"activityName\"", s)
      print(hdid)
      print(hdid2)
      c = [x for x in hdid if x in hdid2]
      d = [y for y in hdid2 if y not in c]

      result_set = d
      if result_set == [] :
        print("暂时没有发布新活动")
      persons = User.objects.filter(tixing="1")
      maillist = []
      for person in persons:
        email = person.email
        maillist.append(email)
      print(maillist)
      for i in result_set:
        qb = re.findall('(?<=activityID":"'+str(i)+').*?(?=moduleID)', s)
        mingcheng = re.findall('(?<=activityName":").*?(?=")', str(qb))
        mingcheng = ''.join(str(i) for i in mingcheng)
        leibie = re.findall('(?<=typeID":").*?(?=")', str(qb))
        leibie = ''.join(str(i) for i in leibie)
        if leibie == "5":
          leibie = "讲座"
        elif leibie == "324":
          leibie = "劳动教育"
        elif leibie == "38":
          leibie = "文艺美育"
        elif leibie == "34":
          leibie = "志愿活动"
        else:
          leibie = "其他活动"
        shijian = re.findall('(?<=applyStartDate":").*?(?=")', str(qb))
        shijian = ''.join(str(i) for i in shijian)
        shijian = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(shijian)))
        check = re.findall('(?<=checkAfterApply":").*?(?=")', str(qb))
        check = ''.join(str(i) for i in check)
        print(mingcheng)
        soure = re.findall('(?<=score":").*?(?=")', str(qb))
        soure = ''.join(str(i) for i in soure)
        if result_set != [] :
            if check=="0":
              wsgilog=""
              with open("/var/log/uwsgi.log", "w") as log:
                log.write(wsgilog)
              print("日志已清除")
              time.sleep(1)
              shenhe="非审核制"
              mail.send_mail(
                subject = '有新的第二课堂发布',
                message = "名称:"+mingcheng+"\n时间:"+shijian+"\n分数:"+soure+"\n类别:"+leibie+"\n"+shenhe+"\n请准时登录官网报名\n或使用网站http://39.101.79.171/快速报名\n学校发错活动会立刻取消,可能出现第二课堂没有该活动的情况",
                from_email = '重庆工商职业学院<3034098798@qq.com>',
                recipient_list = maillist
              )
              print("邮件已发送")

            if check=="1":
              shenhe="审核制"
              mail.send_mail(
                subject = '有新的第二课堂发布',
                message = "名称:"+mingcheng+"\n时间:"+shijian+"\n分数:"+soure+"\n类别:"+leibie+"\n"+shenhe+"\n请准时登录官网报名\n或使用网站http://39.101.79.171/快速报名\n学校发错活动会立刻取消,可能出现第二课堂没有该活动的情况",
                from_email = '重庆工商职业学院<3034098798@qq.com>',
                recipient_list = maillist
              )
              print("审核制活动邮件已发送")
        else:
          print("没有发送邮件")      
    time.sleep(1)