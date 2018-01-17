f=open("cal.txt","r")
t=f.readlines()
for x in t:
    if '+' in x:
        num1,num2 =x.split('+')
        print(int(num1)+int(num2))
    if '*' in x:
        num1,num2 =x.split('*')
        print(int(num1)*int(num2))
    if '-' in x:
        num1,num2 =x.split('-')
        print(int(num1)-int(num2))
    if '/' in x:
        num1,num2 =x.split('/')
        print(int(num1)/int(num2))
    if '%' in x:
        num1,num2 =x.split('%')
        print(int(num1)%int(num2))
f.close()
