import re

sac_email_condition = "^[a-z]+(2[3-9]|[3-9][0-9])+[@]+(my.sevkoleji.k12.tr)"
koc_email_condition = "^[a-z]+(202[3-9]|20[3-9][0-9])+[@]+(stu.koc.k12.tr)"
usn = input()
if(re.search(pattern=sac_email_condition, string=usn)):
    print('Correct sac email')

elif(re.search(koc_email_condition, usn)):
    print('connrect koc email')
else:
    print('wrong both email')

    