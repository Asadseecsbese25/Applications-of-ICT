marks= int(input("Enter your marks (0-100):" ))
if marks >=90 and marks <= 100:
    print("grade= A")
elif marks >= 75 and marks < 90:
    print("grade = B")
elif marks >= 60 and marks < 75:
    print("grade = C")
elif marks >= 50 and marks < 60:
    print("grade = D")
elif marks >= 40 and marks < 50: 
    print("grade = E")
elif marks < 40:
    print("grade = F")
else:
    print("invalid output")