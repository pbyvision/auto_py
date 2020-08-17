import re

text = "박보렬 8809041148544 sdfhlsd 김민석 9102051548554 주민번호아닌것 1515148472454 8835112457894"

tmp = text.split(" ")

for data in tmp:
    if data.isdigit():
        birth_month = data[2:4]
        birth_day = data[4:6]
        sex = data[7]
        if int(birth_day) < 32 and int(birth_month) < 13:
            print(data)




'''
    if int(data):
        birth_year = data[0:2]
        birth_month = data[2:4]
        birth_day = data[4:6]
        if int(birth_month) < 13:
            print(data)
    
    
    if len(data) == 13 && :birth_month < 13 
        print(data, len(data))

        sex = data[7]
 '''
