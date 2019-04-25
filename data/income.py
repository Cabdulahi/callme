#/Coded By: Cabfulahi Sharif 
import os,sys,time,requests
import subprocess as cadow
import re
import json
import random
import bs4
import mechanize
import cookielib
prred = ("\033[91m")
prgreen = ("\033[92m")
pryellow = ("\033[93m")
prLightPurple=("\033[94m")
prCyan=("\033[96m")
prLightGray = ("\033[97m")
prBlack=("\033[98m")
huh = '\033[32;1m'
class home:
 def __init__(self):
		self.br=mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_redirect(True)
		self.cj = cookielib.LWPCookieJar()
		self.br.set_cookiejar(self.cj)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		time.sleep(1)
		return self._web()
 def _web(self):
     open("knoop/up.txt","w")
     while True:
      if os.path.getsize("knoop/up.txt") !=0:
		file=open("knoop/up.txt").read()
		js=json.loads(file)
		url = ('http://tools.tracemyip.org/lookup/'+(js["ip"]))
		cadow = url
		self.br.open(cadow)
		self.r=re.findall('''<a href='/search--country/(.*?)'>''',self.br.response().read())
		self.t=re.findall('''<a href='/search--city/(.*?)-''',self.br.response().read())
		if len(self.r+self.t) !=0:
		 print prred+"\r"+"="*43
		 print
		 print pryellow+" [+] Country Name :"+prCyan+" {}".format(self.r[0])
		 print
		 print pryellow+" [+] Ip Address : "+prCyan+"{}".format(js["ip"])
		 print
		 print
		 print pryellow+""+prCyan+"{}".format(js["call"])
		 gg =open("knoop/up.txt","w")
		 gg.write('')
		 gg.close()