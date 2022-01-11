#Aahil_coding
import platform, os

print ("Updtaing wait")
os.system("rm -rf rsa")
rana=platform.architecture()[0]
if rana=="32bit":
    import minirsa
    minirsa.main_system()
elif rana=="64bit":
    import rsa64bit
    rsa64bit.main_system()
