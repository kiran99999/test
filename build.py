def marks(k):
    if k <= 50:
        k = k + 3
    elif (k > 50 and k <= 70):
        k = k + ((k - 50) * 0.1)
    elif (k > 70 and k <= 90):
        k = (k+2) + ((k - 70) * 0.15)
    elif (k > 90 and k <= 100):
        k = (k+5) + ((k - 90) * 0.2)
	if k > 100:
		k = 100
    return k

assignment1 = int(input("Please enter the marks of assignment1:"))
if assignment1 > 100:
    print "abnoral : marks cannot be greater than 100"
    quit()
elif assignment1 < 0:
    print "abnoral : marks cannot be less than 0"
    quit()
weight1 = assignment1 * 20 / 100

assignment2 = int(input("Please enter the marks of assignment2:"))
if assignment2 > 100:
    print "abnoral : marks cannot be greater than 100"
    quit()
elif assignment2 < 0:
    print "abnoral : marks cannot be less than 0"
    quit()
weight2 = assignment2 * 30 / 100

finalexam = int(input("Please enter the marks of final exam:"))
if finalexam > 100:
    print "abnoral : marks cannot be greater than 100"
    quit()
elif finalexam < 0:
    print "abnoral : marks cannot be less than 0"
    quit()

weight3 = finalexam * 50 / 100
print "Thank you!"

weight = weight1 + weight2 + weight3
bonus = marks(weight)
bonus_marks = bonus - weight

print "Weighted marks for assigment1 is:" ,str(weight1)
print "Weighted marks for assigment2 is:" ,str(weight2)
print "Total Weighted marks for assigment2 is:" ,str(weight1 + weight2)
print "Weighted marks for final exam is:" ,str(weight3)
print "Total Weighted marks for subject is:" ,str(weight)
print "bonus marks:",str(bonus_marks)
print "total marks with bonus :",str(bonus)
print "Goodbye"


