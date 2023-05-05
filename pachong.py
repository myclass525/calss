# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.core import mail
from django.conf import settings
from django.shortcuts import HttpResponse
from django.contrib import messages
from bmi.models import User
from django.db.models import F
from django_redis import get_redis_connection
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


# 接收请求数据
def web(request):
  ID = request.GET['ID']
  mycookie = request.COOKIES.get('tick','1')
  xuehao = request.COOKIES.get('xuehao','1')
  if mycookie == '1':
    return HttpResponseRedirect("http://39.101.79.171/")
  Time = request.GET['huodongtime']
  Dtime = int(time.time())
  sytime = int(Time) - Dtime
  sytime = sytime - 50
  return render(request, "free.html",{'ID': ID,'mycookie': mycookie,'Time': Time,'Dtime': Dtime,'sytime': sytime,'xuehao': xuehao})

def web2(request):
  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
  name_2 = random.choices(chars, k=10)
  name_2 = "".join(name_2)
  ID = request.GET['ID']
  mycookie = request.COOKIES.get('tick','1')
  if mycookie == '1':
    return HttpResponseRedirect("http://39.101.79.171/")
  xuehao = request.COOKIES.get('xuehao','1')
  name = request.COOKIES['username']
  person = User.objects.get(username=name)
  studentmima = person.mima
  if person.jifen <= 0 and person.shenfen == "putong":
    messages.success(request, '积分为0时禁止使用服务，可联系管理增加1积分后重试')
    return render(request, "bmi.html",{'xuehao': xuehao,'mima': studentmima})
  else:
    headers_ssid = {
        'Host': '2class.cqtbi.edu.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/4G Language/zh_CN',
    }
    res_ssid = requests.get(url='https://2class.cqtbi.edu.cn/Admin/Index/cqtbiSSO?PORTAL_TICKET=' + mycookie + '',
                            headers=headers_ssid)
    list1 = [res_ssid.request.headers]
    list2 = [str(i) for i in list1]
    list3 = ''.join(list2)
    s = re.findall('SSID=.*\w+', list3)
    for cookies in s:
        mycookie = cookies
  
    headers = {
        "Host": "2class.cqtbi.edu.cn",
        "Connection": "keep-alive",
        "Content-Length": "84",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/4G Language/zh_CN',
        "Origin": "https://2class.cqtbi.edu.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://2class.cqtbi.edu.cn/Student/Activity/apply.html?activityID=" + ID + "&retUrl=JTJGU3R1ZGVudCUyRkFjdGl2aXR5JTJGaW5kZXguaHRtbA==",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": mycookie
    }
  
    # 获取验证码
    headers_1 = {
        "Host": "2class.cqtbi.edu.cn",
        "Connection": "keep-alive",
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/4G Language/zh_CN',
        "Accept": "image/avif,image/webp,imagepic,imageg,image/apng,image/*,*/*;q=0.8",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "image",
        "Referer": "http://2class.cqtbi.edu.cn/Student/Activity/apply.html?activityID=" + ID + "&retUrl=JTJGU3R1ZGVudCUyRkFjdGl2aXR5JTJGaW5kZXguaHRtbA==",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": mycookie
    }
  
    # 获取s1&s2
    headers_2 = {
        "Host": "2class.cqtbi.edu.cn",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/4G Language/zh_CN',
        "Accept": "textcml,application/xhtml+xml,application/xml;q=0.9,image/avif,imagepic,imageg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://2class.cqtbi.edu.cn/Student/Activity/index.html",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": mycookie
    }
  
    url_1 = "https://2class.cqtbi.edu.cn/Student/Activity/verifycode.html"  # 报名验证码
    url_2 = "https://2class.cqtbi.edu.cn/Student/Activity/apply.html?activityID=" + ID + "&retUrl=JTJGU3R1ZGVudCUyRkFjdGl2aXR5JTJGaW5kZXguaHRtbA=="  # 活动密钥获取
    url = "https://2class.cqtbi.edu.cn/Student/Activity/applyGo.html"  # 活动报名
    
    url_p = 'https://2class.cqtbi.edu.cn/Student/Activity/getActivityCanApply.html'
    headers_p = {
          "Host": "2class.cqtbi.edu.cn",
          "Cookie": mycookie
    }
    a = requests.post(url=url_p, headers=headers_p).text
    s = a.encode('utf-8').decode('unicode_escape')
    hdidd = re.findall(r"activityID\":\"(.*?)\",\"activityName\"",s)
    hdnamed = re.findall(r"activityName\":\"(.*?)\",\"applyStartDate\"",s)
    start = re.findall(r"applyStartDate\":\"(.*?)\",\"applyEndDate\"",s)
    img = re.findall(r"img\":\"(.*?)\",\"status\"",s)
    heji=zip(hdnamed,hdidd,start,img)
    list_c = person.name
    
    qb = re.findall('(?<=activityID":"'+str(ID)+').*?(?=moduleID)', s)
    leibie = re.findall('(?<=typeID":").*?(?=")', str(qb))
    leibie = ''.join(str(i) for i in leibie)
    start = re.findall(r"applyStartDate\":\"(.*?)\",\"applyEndDate\"",str(qb))
    start = ''.join(str(i) for i in start)
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
    soure = re.findall('(?<=score":").*?(?=")', str(qb))
    soure = ''.join(str(i) for i in soure)
    if int(start) < (int(time.time())-1800):
      hdpass = "pass"
    else:
      hdpass = "nopass"
    if (leibie != "其他活动" and soure == "0.2" and person.jifen < 2) and hdpass != "pass":
      messages.success(request, '您的账号积分不足')
      return render(request, "chenggong.html", {'heji': heji,'data2': list_c})
    if (leibie != "其他活动" and (soure == "0.4" or soure == "0.5") and person.jifen < 3) and hdpass != "pass":
      messages.success(request, '您的账号积分不足')
      return render(request, "chenggong.html", {'heji': heji,'data2': list_c})
    if (leibie == "其他活动" and (soure == "0.4" or soure == "0.5") and person.jifen < 2) and hdpass != "pass":
      messages.success(request, '您的账号积分不足')
      return render(request, "chenggong.html", {'heji': heji,'data2': list_c})
    if (person.jifen <= 0 and person.shenfen == "putong") and hdpass != "pass":
      messages.success(request, '您的账号积分不足')
      return render(request, "chenggong.html", {'heji': heji,'data2': list_c})
    print(leibie)
    print(soure)
    panduan_1 = 0
    redis_conn = get_redis_connection("default")
    redis_conn.set(xuehao, panduan_1)
    while panduan_1 < 51:
        
        c = requests.get(url=url_1, headers=headers_1).content
        with open(name_2+".png", "wb") as fb:
            fb.write(c)
            ocr = ddddocr.DdddOcr()
        with open(name_2+".png", 'rb') as f:
  
            img_bytes = f.read()
            res = ocr.classification(img_bytes)
        os.remove(name_2 + '.png')
  
        flag = True  # 正确验证码
        if res:
            for ch in res:
                if ch >= '0' and ch <= '9':
                    continue
                else:
                    flag = False
                    print('验证码识别有误！！')
                    break
        if flag == True:
                panduan_1 = int(panduan_1)+1
                s1_s2 = requests.get(url=url_2, headers=headers_2, allow_redirects=False).text
                sult_1 = re.findall('s1:.*?(\w+)', s1_s2)
                sult_2 = re.findall('s2:.*?(\w+)', s1_s2)
                print("key_1:" + sult_1[0])
                print("key_2:" + sult_2[0])
                s1 = str(sult_1[0])
                s2 = str(sult_2[0])
                data = "activityID=" + ID + "&activityApplyRand=" + res + "&s1=" + s1 + "&s2=" + s2
                data = data.encode()
                session = requests.Session()
                activity_post = session.post(url=url, headers=headers, data=data)
                panduan = activity_post.content.decode('utf-8')
                d = str.isascii(panduan)
                
                redis_conn.set(xuehao, panduan_1)
                if d:
                    panduan = (panduan.encode('ascii').decode('unicode_escape'))
                    panduan = panduan.lstrip('"')
                    panduan = panduan.rstrip('"')
                    print("^^^^^^^^^^^^^" + panduan + "^^^^^^^^^^^^^^^^")
                    return_1 = "2"
                    return_2 = "-2"
                    return_3 = "请勿重复报名"
                    return_4 = "1"
                    return_5 = "报名失败！很遗憾，报名时间已过或者活动已被取消！"
                    return_1 = return_1.strip()
                    return_2 = return_2.strip()
                    return_3 = return_3.strip()
                    return_4 = return_4.strip()
                    return_5 = return_5.strip()
                    if panduan == return_4:
                        panduan_1 = 51
                        print("******************报名成功!!!***********************")
                        if person.shenfen == "putong" and hdpass != "pass":
                          if soure == "0.2":
                            if leibie == "其他活动":
                              person.jifen = F('jifen') - 1
                              person.save()
                              panduan_1 = 50
                              redis_conn.set(xuehao, panduan_1)
                              return JsonResponse({"status": '报名成功,消耗1积分'})
                            if person.jifen >= 2 and leibie != "其他活动":
                              person.jifen = F('jifen') - 2
                              person.save()
                              panduan_1 = 50
                              redis_conn.set(xuehao, panduan_1)
                              return JsonResponse({"status": '报名成功,必修活动消耗2积分'})
                            else:
                              return JsonResponse({"status": '报名失败,积分不足'})
                          if soure == "0.4" or soure == "0.5":
                            if leibie == "其他活动" and person.jifen >= 2:
                              person.jifen = F('jifen') - 2
                              person.save()
                              panduan_1 = 50
                              redis_conn.set(xuehao, panduan_1)
                              return JsonResponse({"status": '报名成功,高分活动消耗2积分'})
                            if leibie != "其他活动" and person.jifen >= 3:
                              person.jifen = F('jifen') - 3
                              person.save()
                              panduan_1 = 50
                              redis_conn.set(xuehao, panduan_1)
                              return JsonResponse({"status": '报名成功,高分必修活动消耗3积分'})
                            else:
                              return JsonResponse({"status": '报名失败,积分不足'})
                          else:
                            person.jifen = F('jifen') - 1
                            person.save()
                            panduan_1 = 50
                            redis_conn.set(xuehao, panduan_1)
                            return JsonResponse({"status": '报名成功,消耗1积分'})
                        if hdpass == "pass":
                          panduan_1 = 50
                          redis_conn.set(xuehao, panduan_1)
                          return JsonResponse({"status": '报名成功,此活动报名时间已经过去很久了,不消耗积分'})
                        panduan_1 = 50
                        redis_conn.set(xuehao, panduan_1)
                        return JsonResponse({"status": '报名成功,此账号不消耗积分'})
                    if panduan == return_1:
                        panduan_1 = 51
                        print("******************报名成功!!!***********************")
                        if person.shenfen == "putong" and hdpass != "pass":
                          if soure == "0.2":
                            if leibie == "其他活动":
                              person.jifen = F('jifen') - 1
                              person.save()
                              panduan_1 = 50
                              redis_conn.set(xuehao, panduan_1)
                              return JsonResponse({"status": '报名成功,消耗1积分'})
                            if person.jifen >= 2 and leibie != "其他活动":
                              person.jifen = F('jifen') - 2
                              person.save()
                              panduan_1 = 50
                              redis_conn.set(xuehao, panduan_1)
                              return JsonResponse({"status": '报名成功,必修活动消耗2积分'})
                            else:
                              return JsonResponse({"status": '报名失败,积分不足'})
                          if soure == "0.4" or soure == "0.5":
                            if leibie == "其他活动" and person.jifen >= 2:
                              person.jifen = F('jifen') - 2
                              person.save()
                              panduan_1 = 50
                              redis_conn.set(xuehao, panduan_1)
                              return JsonResponse({"status": '报名成功,高分活动消耗2积分'})
                            if leibie != "其他活动" and person.jifen >= 3:
                              person.jifen = F('jifen') - 3
                              person.save()
                              panduan_1 = 50
                              redis_conn.set(xuehao, panduan_1)
                              return JsonResponse({"status": '报名成功,高分必修活动消耗3积分'})
                            else:
                              return JsonResponse({"status": '报名失败,积分不足'})
                          else:
                            person.jifen = F('jifen') - 1
                            person.save()
                            panduan_1 = 50
                            redis_conn.set(xuehao, panduan_1)
                            return JsonResponse({"status": '报名成功,消耗1积分'})
                        if hdpass == "pass":
                          panduan_1 = 50
                          redis_conn.set(xuehao, panduan_1)
                          return JsonResponse({"status": '报名成功,此活动报名时间已经过去很久了,不消耗积分'})
                        panduan_1 = 50
                        redis_conn.set(xuehao, panduan_1)
                        return JsonResponse({"status": '报名成功,此账号不消耗积分'})
                    if panduan == return_2:
                        panduan_1 = 51
                        redis_conn.set(xuehao, panduan_1)
                        print("*******************很抱歉，名额已尽!!!************************")
                        return JsonResponse({"status": '名额已满'})
                    if panduan == return_3:
                        panduan_1 = 51
                        print("*******************请勿重复报名!!!************************")
                        redis_conn.set(xuehao, panduan_1)
                        return JsonResponse({"status": '请勿重复报名'})
                    if panduan_1 >= 50:
                        panduan_1 = 51
                        redis_conn.set(xuehao, panduan_1)
                        print("*******************报名失败!!!************************")
                        return JsonResponse({"status": '报名:50次,失败:50次,请检查活动开始时间'})
                else:
                    print("网页出错啦！")
                    print("学校网站崩了，请五分钟后再试试........")
                    panduan_1 = 0
                    
def jdt(request):
  xuehao = request.COOKIES.get('xuehao','1')
  redis_conn = get_redis_connection("default")
  z = redis_conn.get(xuehao)
  z = int(z.decode('utf-8'))
  connection_pool = redis_conn.connection_pool
  return JsonResponse({"jindu": z})
