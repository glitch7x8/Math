import os
os.system("clear && figlet MATH")
print ("""
\033[0;35m1)\033[0;36m PGCD
\033[0;35m2)\033[0;36m PPCM
                                 By.Aymen & Rahim """)
input=int(input("\033[0;33m==> "))
if input == 1:
	os.system("python 0.py")
if input == 2:
	os.system("python 1.py")
if input <= 0 or input > 2 :
	print ("There Is Only 1 and 2")
