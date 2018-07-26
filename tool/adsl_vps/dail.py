# -*- coding=utf-8 -*-
# File Name: dail.py

import os
import re
import time
import envoy
import requests
from requests.exceptions import ConnectionError, ReadTimeout
from redis_service import RedisClient
import subprocess

ADSL_IFNAME = 'ppp0'
TEST_URL = 'http://www.baidu.com'
TEST_TIMEOUT = 20
ADSL_CYCLE = 100
ADSL_ERROR_CYCLE = 5
#ADSL_BASH = 'adsl-stop;adsl-start'
ADSL_BASH_START = '/usr/sbin/pppoe-start'
ADSL_BASH_STOP = '/usr/sbin/pppoe-stop'
PROXY_PORT = 8899
CLIENT_NAME = 'adsl1'

class Sender():
    def get_ip(self, ifname=ADSL_IFNAME):
        """
        :return:
        """
        (status, output) = subprocess.getstatusoutput('ifconfig')
        print(output)
        if status == 0:
            #pattern = re.compile(ifname + '.*?inet.*?(\d+\.\d+\.\d+\.\d+).*?netmask', re.S)
            pattern = re.compile('inet addr:(\d+\.\d+\.\d+\.\d+).*?P')
            result = re.search(pattern, output)
            if result:
                ip = result.group(1)
                return ip

    def test_proxy(self, proxy):
        """
        """
        try:
            response = requests.get(TEST_URL, proxies={
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }, timeout=TEST_TIMEOUT)
            if response.status_code == 200:
                return True
        except (ConnectionError, ReadTimeout):
            return False

    def remove_proxy(self):
        """
        :return: None
        """
        self.redis = RedisClient()
        self.redis.remove(CLIENT_NAME)
        print('Successfully Removed Proxy')

    def set_proxy(self, proxy):
        """
        :return: None
        """
        self.redis = RedisClient()
        if self.redis.set(CLIENT_NAME, proxy):
            print('Successfully Set Proxy', proxy)

    def adsl(self):
        """
        """

        env = {
            "PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games",
            "SHELL" : "/bin/bash",
            "USER" : "root",
            "PWD" : "/root/work/dail",
            "_" : "/usr/bin/env",
            "OLDPWD" : "/root/work",
            "XDG_RUNTIME_DIR" : "/run/user/0",
            "LESSOPEN" : "| /usr/bin/lesspipe %s",
            "SHLVL" : "1",
        }

        while True:
            print('ADSL Start, Remove Proxy, Please wait')
            self.remove_proxy()

            r = envoy.run(ADSL_BASH_STOP)
            if r.status_code == 0:
                print('stop success')
            else:
                print(r.std_out)
                print(r.std_err)
                time.sleep(ADSL_ERROR_CYCLE)
                continue 

            s = envoy.run(ADSL_BASH_START)
            if s.status_code == 0:
                print('start success')
            else:
                print(s.std_out)
                print(s.std_err)
                time.sleep(ADSL_ERROR_CYCLE)
                continue

            print('ADSL Successfully')

            ip = self.get_ip()
            if ip:
                print('Now IP', ip)
                print('Testing Proxy, Please Wait')
                proxy = '{ip}:{port}'.format(ip=ip, port=PROXY_PORT)
                if self.test_proxy(proxy):
                    print('Valid Proxy')
                    self.set_proxy(proxy)
                    print('Sleeping')
                    time.sleep(ADSL_CYCLE)
                else:
                    print('Invalid Proxy')
            else:
                print('Get IP Failed, Re Dialing')
                time.sleep(ADSL_ERROR_CYCLE)

def run():
    sender = Sender()
    sender.adsl()

if __name__ == "__main__":

    run()
