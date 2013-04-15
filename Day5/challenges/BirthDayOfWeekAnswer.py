'''
Created on Apr 7, 2013

@author: Kiks
'''

from datetime import date

userBDay = raw_input("Please tell me your birthday in 'YYYY-MM-DD' format")
bData = userBDay.split("-")

bYear = int(bData[0])
bMonth = int(bData[1])
bDay = int(bData[2])

birthday = date(bYear, bMonth, bDay)

print("You were born on a " + birthday.strftime("%A") + "!")
