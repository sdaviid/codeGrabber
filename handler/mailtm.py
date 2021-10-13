import requests
import json
import random


def random_char(y, l=True, u=True, n=True):
    ls = 'abcdefghijklmnopqrstuvwxyz'
    us = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ns = '0123456789'
    t = ''
    if l is True:
        t += ls
    if u is True:
        t += us
    if n is True:
        t += ns
    return ''.join(random.choice(t) for x in range(y))





class mailTm(object):
    req = None
    email = None
    senha = None
    token = None
    def isOpen(self):
        return True if self.token is not None else False
    def getDomain(self):
        retorno = False
        url = 'https://api.mail.tm/domains'
        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        r = requests.get(url, headers=headers, verify=False)
        return r.json()
    def novo(self):
        retorno = False
        url = 'https://api.mail.tm/accounts'
        dominios = self.getDomain()
        if dominios:
            if len(dominios)>0:
                d = dominios[0]
                host = d['domain']
                inbox = random_char(14, u=False, n=False)
                email = '%s@%s' % (inbox, host)
                senha = random_char(8)
                headers = {
                    'accept': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
                }
                payload = {
                    "address": email,
                    "password": senha
                }
                r = requests.post(url, json=payload, headers=headers, verify=False)
                if r.status_code in (200, 201):
                    self.email = email
                    self.senha = senha
                    if self.token() is True:
                        retorno = True
        return retorno
    def token(self):
        retorno = False
        if self.email is not None and self.senha is not None:
            url = 'https://api.mail.tm/token'
            headers = {
                'accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
                'content-type': 'application/json;charset=UTF-8'
            }
            payload = {
                "address": self.email,
                "password": self.senha
            }
            r = requests.post(url, json=payload, headers=headers, verify=False)
            if r.status_code == 200:
                j = r.json()
                if 'token' in j:
                    self.token = j['token']
                    retorno = True
        return retorno
    def getMessages(self):
        retorno = False
        if self.token is not None:
            url = 'https://api.mail.tm/messages'
            headers = {
                'accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
                'Authorization': 'Bearer %s' % (self.token)
            }
            r = requests.get(url, headers=headers, verify=False)
            if r.status_code == 200:
                retorno = r.json()
        return retorno
    def getMessage(self, id):
        retorno = False
        if self.token is not None:
            url = 'https://api.mail.tm/messages/%s' % (id)
            headers = {
                'accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
                'Authorization': 'Bearer %s' % (self.token)
            }
            r = requests.get(url, headers=headers, verify=False)
            if r.status_code == 200:
                retorno = r.json()
        return retorno
