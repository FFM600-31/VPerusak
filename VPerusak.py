import os
import sys
import time

cyan='\033[0;36m'
purple='\033[0;35m'
brown='\033[0;33m'
lightgray='\033[0;37m'
darkgray='\033[1;30m'
lightblue='\033[1;34m'
lightgreen='\033[1;32m'
lightcyan='\033[1;36m'
yellow='\033[1;33m'
white='\033[37;1m'

os.system('clear')
print ('\033[1;32m')
menu = """
-----------Virus Perusak---------------
[+] Author By FFM600-31
[+] Youtube : FFM. YT
[+] Github : https://github.com/FFM600-31
---------------------------------------
"""
print menu
No = raw_input('\033[1;33m'"Masukan Nomor WA : ")
jml = int(input("Masukan Jumlah Virus : "))
nanya = raw_input("Memulai Serangan Y/N : ")
if nanya == 'Y' or nanya == 'y':
  time.sleep(1)
  for i in range(jml):
      print('\033[1;33m'"Mengirim Virus Ke"'\033[37;1m'),No
if nanya == 'N' or nanya == 'n':
   print("Selamat Tinggal")
   print ('\033[37;1m')
   time.sleep(1)
   os.system('clear')
   os.system('login')
