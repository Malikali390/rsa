


#                     #Aahil-coding



import os, platform
os.system("cd $HOME/")
try:
    import bs4
except ImportError:
    os.system("pip install bs4")
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import mechanize
except ImportError:
    os.system("pip install mechanize")
    
rana=platform.architecture()[0]
if rana=="32bit":
    import minirsa
    minirsa.main_system()
elif rana=="64bit":
    import rsa.cpython64
    rsa.cpython64.sec()
