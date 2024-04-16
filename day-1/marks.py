marks = int(input("Enter your marks: "))

if marks < 40:
    print("Fail")
elif 40 <= marks < 55:
    print("Pass")
elif 55 <= marks < 70:
    print("Second Class")
elif 70 <= marks < 85:
    print("First Class")
else:
    print("OutStanding")
