# Nicolas Campero
# 1856853

mypassword = input()

for i in mypassword:
    if i == 'i':
        mypassword = mypassword.replace('i', '!')
    elif i == 'a':
        mypassword = mypassword.replace('a', '@')
    elif i == 'm':
        mypassword = mypassword.replace('m', 'M')
    elif i == 'B':
        mypassword = mypassword.replace('B', '8')
    elif i == 'o':
        mypassword = mypassword.replace('o', '.')

mypassword += 'q*s'


print(mypassword)
