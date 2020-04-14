#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 此项目主要参考链接【http://cuiqingcai.com/1076.html，感谢作者的分享

__author__ = 'JustFantasy'

import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import re

# 模拟登录淘宝类
# 登录淘宝流程
# 1、请求地址https://login.taobao.com/member/login.jhtml获取到token
# 2、请求地址https://passport.alibaba.com/mini_apply_st.js?site=0&token=1L1nkdyfEDIA44Hw1FSDcnA&callback=callback 通过token换取st
# 3、请求地址https://login.taobao.com/member/vst.htm?st={st}实现登录
class Taobao: # 定义类

    # 初始化方法
    def __init__(self): # 定义方法
        # 登录的URL，获取token
        self.request_url = 'https://login.taobao.com/member/login.jhtml'
        # 通过st实现登录的URL
        self.st_url = 'https://login.taobao.com/member/vst.htm?st={st}'
        # 用户中心地址
        self.user_url = 'https://i.taobao.com/my_taobao.htm'
        # 代理IP地址，防止自己的IP被封禁
        self.proxy_ip = 'http://120.193.146.97:843'
        # 登录POST数据时发送的头部信息
        self.request_headers =  {
            'Host':'login.taobao.com',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer' : 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive'
        }
        # 用户名
        self.username = 'longyi280132947'
        # ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua = '110#kYckAUkfkxYwDt4+rK5VMuy2gMLnaPOW48RoN9SUcPyIkKgksUkU4uf28MLY0U28MKkkNvBksPyukKYIQGkkPuykEeUe3JTWPKgXbVKkk32Wkk6tDwkkw4yvk1ZwUTK9+xsxgwcxhedyygskYmHhjM5OmUkoAiQI8Amn/UjphouyaObk2t5SoFwMmArgVRi/83snFw6wROUt5OJfDhQq5EN8Gvq9eadfrLBf/aIQhDIw8NDbtDVRn/NLq/cd8LvwsTvsa5R8J3ciskT47TmwjbBq44W3sQvJjTHzKvsAJAbfsWmmGLaqjTcwkk2sbOMws9bXMcoDyA3OynkkGLswVT/Au8dwmATHI9Q2kc+XkEWGJByMcN4YO7WcLB54ipEaB4lvy2mOveiT6qcAUlOsIvrGMqKGrAxRI30uWpYLCHhauQqHeGfF6tm0BDhlnP5J5gntEBWCTkXv/Op7Zo48Dt43a4g6kIk0LX2rMfm64zfMh6s8Cx/oaXNWNJVDVOLZOjWE+qq2p21aqQZXCAZ9rQasnfMvdKxey5epmMEsuzdAHctCC/jePQGKX6y/Yni9zVvOsaWJWO34VpO+exe74HMTESd+Gsj2E/0BPTAldrkKezejxsBTtMaBTTkDP5FR0/xNDOqCAs6HPgTzdiuKiotv19AXCQktQrTEwnLTBsPzAz3MyE0gGZ3CDkm3amrHsfiStmlC0wTm1LjDltKNCbtH+xPc+kJ7nEBgukmEXmxeeyFJFZOmTFrj9l5Nrvk1XP7Q/1TM7nvjWSkLYSRhzTK1/Fo4oVHYvRAZztv8i+yfJiCP4mkiAwgSb2WRXUdXqTQTWUdGm7zW347arX70y/vf9G9ztUNBFBIlO7a6E0vkG6yqGzBJote4qHtkwXHJLlukw5V2/2gHvCCDhDQ1/V+wtObAbwnPi3sIMVnoxL7LtQZfUU=='
        # 密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2 = '1466aa32e64211b5f4c4f2d1dac2263cd7fc07f08fa298cfcb88b3a66bc6c6d57c8bd40df5bc0966558d2dd5dbaabcf426458a5f5edd9a0e68124ec87d9370e68e45456d9c1cf506727bbc60199a89a2e12b3784e29627677d595b827dd7996ecf499cc27a3f4a3332cf0a30c57f96d15d007b9f4c20bea15ef80a868f59cf50'
        self.post = {
            'ua': self.ua,
            'TPL_checkcode': '',
            'CtrlVersion': '1,0,0,7',
            'TPL_password': '',
            'TPL_redirect_url': 'http://i.taobao.com/my_taobao.htm',
            'TPL_username': self.username,
            'loginsite': '0',
            'newlogin': '0',
            'from': 'tb',
            'fc': 'default',
            'style': 'default',
            'css_style': '',
            'tid': 'XOR_1_000000000000000000000000000000_625C4720470A0A050976770A',
            'support': '000001',
            'loginType': '4',
            'minititle': '',
            'minipara': '',
            'umto': 'NaN',
            'pstrong': '3',
            'llnick': '',
            'sign': '',
            'need_sign': '',
            'isIgnore': '',
            'full_redirect': '',
            'popid': '',
            'callback': '',
            'guf': '',
            'not_duplite_str': '',
            'need_user_id': '',
            'poy': '',
            'gvfdcname': '10',
            'gvfdcre': '',
            'from_encoding ': '',
            'sub': '',
            'TPL_password_2': self.password2,
            'loginASR': '1',
            'loginASRSuc': '1',
            'allp': '',
            'oslanguage': 'zh-CN',
            'sr': '1366*768',
            'osVer': 'windows|6.1',
            'naviVer': 'firefox|35'
        }
        # 将POST的数据进行编码转换
        self.post_data = urllib.parse.urlencode(self.post).encode(encoding='GBK') # 淘宝的编码为GBK
        # 设置代理
        self.proxy = urllib.request.ProxyHandler({'http': self.proxy_ip})
        # 设置cookie
        self.cookie = http.cookiejar.LWPCookieJar()
        # 设置cookie处理器
        self.cookieHandler = urllib.request.HTTPCookieProcessor(self.cookie)
        # 设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib.request.build_opener(self.cookieHandler, self.proxy, urllib.request.HTTPHandler)
        # 赋值J_HToken
        self.J_HToken = ''
        # 登录成功时，需要的Cookie
        self.newCookie = http.cookiejar.CookieJar()
        # 登陆成功时，需要的一个新的opener
        self.newOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.newCookie))

    # 利用st码进行登录
    # 这一步我是参考的崔庆才的个人博客的教程，因为抓包的时候并没有抓取到这个url
    # 但是如果不走这一步，登录又无法成功
    # 区别是并不需要传递user_name字段，只需要st就可以了
    def login_by_st(self, st):
        st_url = self.st_url.format(st=st)
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Host':'login.taobao.com',
            'Connection' : 'Keep-Alive'
        }
        request = urllib.request.Request(st_url, headers=headers)
        response = self.newOpener.open(request)
        content =  response.read().decode('gbk')

        #检测结果，看是否登录成功
        pattern = re.compile('top.location.href = "(.*?)"', re.S)
        match = re.search(pattern, content)
        print(match)
        if match:
            print(u'登录网址成功')
            return True
        else:
            print(u'登录失败')
            return False


    # 程序运行主干
    def main(self):
        try:
            # 请求登录地址， 此时返回的页面中有两个js的引入
            # 位置是页面的前两个JS的引入，其中都带有token参数
            request = urllib.request.Request(self.request_url, self.post_data, self.request_headers)
            response = self.opener.open(request)
            content = response.read().decode('gbk')

            # 抓取页面中的两个获取st的js
            pattern = re.compile('<script src=\"(.*)\"><\/script>')
            match = pattern.findall(content)

            # [
            # 'https://passport.alibaba.com/mini_apply_st.js?site=0&token=1f2f3ePAx5b-G8YbNIlDCFQ&callback=callback',
            # 'https://passport.alipay.com/mini_apply_st.js?site=0&token=1tbpdXJo6W1E4bgPCfOEiGw&callback=callback',
            # 'https://g.alicdn.com/kissy/k/1.4.2/seed-min.js',
            # 'https://g.alicdn.com/vip/login/0.5.43/js/login/miser-reg.js?t=20160617'
            # ]
            # 其中第一个是我们需要请求的JS，它会返回我们需要的st
            #print(match)


            # 如果匹配到了则去获取st
            if match:
                # 此时可以看到有两个st， 一个alibaba的，一个alipay的，我们用alibaba的去实现登录
                request = urllib.request.Request(match[0])
                response = urllib.request.urlopen(request)
                content = response.read().decode('gbk')

                # {"code":200,"data":{"st":"1lmuSWeWh1zGQn-t7cfAwvw"} 这段JS正常的话会包含这一段，我们需要的就是st
                #print(content)

                # 正则匹配st
                pattern = re.compile('{"st":"(.*?)"}')
                match = pattern.findall(content)

                # 利用st进行登录
                if match:
                    self.login_by_st(match[0])
                else:
                    print(u'无法获取到st，请检查')
                    return

                # 请求用户中心，查看打印出来的内容，可以看到用户中心的相关信息
                response = self.newOpener.open(self.user_url)
                page = response.read().decode('utf-8')
                print(page)

        except urllib.error.HTTPError as e:
            print(u'请求失败，错误信息：', e.msg)



taobao = Taobao()
taobao.main()