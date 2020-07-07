#**CODE BY AEVHAKAN****#
#SELAM
##INSTAGRAM : aevhakan


import random
import time
pass_generator = 'abcdefghijklmnopqrstuvwxyz12345678910#%&*)$($+$838282(2+$;$!$))'

number = input("Sayi Adeti: ")
number = int(number)

lenght = input("Kac Hane: ")
lenght = int(lenght)

for x in range(number):
  password= ''
  for g in range(lenght):
     password += random.choice(pass_generator)
     
print("Olusturuluyor...")
time.sleep(2)
print("%50")
print("")
print("")
time.sleep(1)
print"@aevhakan follow me pls"
print("")
print("")
time.sleep(1.5)
print"%100"
print("")
print("")
time.sleep(1.3)
print("Your Password ", password )
