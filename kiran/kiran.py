a = 4
b = 1
while(a > 0):
    try:
        c = a/b
        print "c value :",str(c)
        break
    except:
        print "a cannot be divided by zero"
        break
