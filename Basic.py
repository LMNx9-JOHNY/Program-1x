###############################
#       DARK TEAM LMNx9       #
###############################
import os 
import time 
os.system("pkg install espeak")
os.system("termux-open https/www.facebook.com/LJ.LMNx9")

time.sleep(2)
os.system("espeak -a 500 \" welcome to LMNx9 Basic Tool\"")

logo = ("""
<\><\>DARK TEAM LMNx9<\><\>
[1] All Basic Update
[2] All Update ?/?
""")

os.system("clear")
print(logo)
limon = input("Choose : ")

if limon in ["01","1"]:
    print("=============================")
print("Updating Termux -")
print("=============================")
print(logo)
print("=============================")
#	os.system('pkg update & upgrade')
os.system("espeak -a 500 \"Your Terminal Is Being Updating\"")
os.system("apt update && upgrade")
#time.sleep(1)
os.system("clear")

print("=============================")
print("Pkg Installing Python -")
print("=============================")
print(logo)
print("=============================")
os.system("espeak -a 500 \"Your Python is being Installing\"")
os.system("pkg install python")
#time.sleep(1)
os.system("clear")

print("=============================")
print("Pkg Installing Python2")
print("=============================")
print(logo)
print("=============================")
os.system("espeak -a 500\"Your Python 2 is being installing\"")

os.system("pkg install python2")
os.system("clear")

print("=============================")
print("Pkg Installing Python3")
print("=============================")
print(logo)
print("=============================")
os.system("espeak -a 500\"Your Python 3 is being installing\"")
os.system("pkg install python3")
os.system("clear")

print("=============================")
print("Pkg Installing Git")
print("=============================")
print(logo)
print("=============================")
os.system("espeak -a 500\"Your Git Is being Installing\"")
os.system("pkg install git")
#time.sleep(1)
os.system("clear")

print("=============================")
print("Pkg Installing PHP -")
print("=============================")
print(logo)
print("=============================")
os.system("espeak -a 500\"Your Php is being Installing\"")
os.system("pkg install php")
#time.sleep(1)
os.system("clear")

print("Basic Finish")
print("=============================")
print(logo)
print("=============================")
print("Run Again LMNx9 Tool ?? y/n")
run = input("Choose :")
if run in ["y"]:
    os.system("python Basic.py")

elif run in ["n"]:
	os.system("exit")
	
#####################DARK LMNx9
elif limon in ["02","2"]:
	print(logo)
	print("Installing All Pkg")
os.system("espeak -a 500 \"Please wait Proccess is being start soon\"")
    
#time.sleep(2)

print("Installing Full pkg - please wait")
os.system("pkg install nmap")
    
#time.sleep(1)
    
print(logo)
os.system("python Basic.py")
