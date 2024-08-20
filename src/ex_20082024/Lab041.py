#Grade calculator
score=int(input("Enter score"))

if score>=90 and score <=100:
    print("You are Pass and grade is","A")
elif score>=80 and score <=89:
    print("You are pass and grade is ","B")
elif score>=70 and score <=79:
    print("You are pass and grade is ","C")
elif score>=60 and score <=69:
    print("You are pass and grade is ","D")
elif score>=50 and score <=59:
    print("You are pass and grade is ","E")
else:
    print("You are fail")
