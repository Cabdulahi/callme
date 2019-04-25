#!/usr/bin/python
# coding=utf-8
#///.coded by cabdulahi sharif
import time
import os,sys
from data import see


def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

green = '\033[32;1m'

gta = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
  #//Colors 
white = '\033[1;37m' # White 
prred = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan
green = ("\033[92m")
pryellow = ("\033[93m")
prlight=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")
class cadowx:
  def __init__(self):
      self.cade=(pryellow+'[ðŸ’¡]Cabdulahi)=>:  ')
      print prred+"\r"+"="*43
      
      print pryellow+"""
      
  ___ __ _| | |  _ __ ___
 / __/ _` | | | | '_ ` _ \
| (_| (_| | | | 
 \___\__,_|_|_| |_| |_| |_|
 
"""+C+p+"""
   [🚩]Youtube Channel: """+pryellow+"""Somali 4You"""+C+p+"""
   [🚩]facebook : """+pryellow+"""cabdulahi.sharif.100"""+C+p+"""
   [🚩]github: """+pryellow+"""https://github.com/Cabdulahi"""+C+p+"""
   [🚩]developer: """+pryellow+"""Cabdulahi Sharif Gsm
   """
      print prred+"\r"+"="*43
      print
      time.sleep(1)
      return self.mee()
     
  def mee(self):
      try:
          see.home()
      except Exception as g:
          print g
      
       
if __name__ == "__main__":
	cadowx()