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





class mailnesia(object):
    email = None
    inbox = None
    def isOpen(self):
        return True if self.inbox is not None else False
    def novo(self):
        retorno = False
        inbox = random_char(14, u=False, n=False)
        email = '%s@mailnesia.com' % (inbox)
        url = 'https://m.mailnesia.com/api/mailbox/%s' % (inbox)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'Referer': 'https://m.mailnesia.com/'
        }
        r = requests.get(url, headers=headers, verify=False)
        if r.status_code == 200:
            self.email = email
            self.inbox = inbox
            retorno = True
        return retorno
    def getMessages(self):
        retorno = False
        if self.inbox is not None:
            url = 'https://m.mailnesia.com/api/mailbox/%s' % (self.inbox)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                'Referer': 'https://m.mailnesia.com/'
            }
            r = requests.get(url, headers=headers, verify=False)
            if r.status_code == 200:
                retorno = json.loads(r.text)
        return retorno
    def getMessage(self, id):
        retorno = False
        if self.inbox is not None:
            url = 'http://m.mailnesia.com/api/mailbox/%s/%s' % (self.inbox, id)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                'Referer': 'https://m.mailnesia.com/'
            }
            r = requests.get(url, headers=headers, verify=False)
            if r.status_code == 200:
                retorno = r.text
        return retorno


# class mailnesia(object):
#     inbox = None
#     def __init__(self, inbox):
#         self.inbox = inbox
#         self.abrir()
#     def abrir(self):
#         retorno = None
#         url = 'https://m.mailnesia.com/api/mailbox/%s' % (self.inbox)
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
#             'Referer': 'https://m.mailnesia.com/'
#         }
#         r = None
#         try:
#             r = requests.get(url, headers=headers, verify=False)
#         except Exception as e:
#             print('abrir email EXP %s' % (str(e)))
#         if r:
#             if r.status_code == 200:
#                 j_data = json.loads(r.text)
#                 retorno = j_data
#         return retorno
#     def procuraEmail(self, titulo):
#         retorno = None
#         temp = self.abrir()
#         if temp is not None:
#             try:
#                 if len(temp)>0:
#                     for i in temp:
#                         if titulo in i['subject']:
#                             retorno = i['id']
#                             break
#             except Exception as e:
#                 print('EXP ... %s' % (str(e)))
#         return retorno
#     def lerEmail(self, codigo):
#         retorno = None
#         url = 'http://m.mailnesia.com/api/mailbox/%s/%s' % (self.inbox, codigo)
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
#             'Referer': 'https://m.mailnesia.com/'
#         }
#         r2 = None
#         try:
#             r2 = requests.get(url, headers=headers, verify=False)
#         except Exception as e:
#             print('exp LER EMAIL %s' % (str(e)))
#         if r2:    
#             if r2.status_code == 200:
#                 retorno = r2.text
#         return retorno
