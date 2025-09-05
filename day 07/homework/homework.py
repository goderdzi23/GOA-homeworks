number1 = int(input("enter number 1:"))
number2 = int(input("enter number 2:"))
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 ** number2)
print(number1 % number2)
print(number1 / number2)
print(number1 // number2)


number = int(input("enter number:"))
if number % 2 == 0:
    print("number is even!")
else: 
    print("number is odd!")


score = int(input("enter score:"))
if score >= 90 and score <= 100:
    print("შესანიშნავია!")
if score >= 80 and score <= 89:
    print("კარგი!")    
if score >= 70 and score <= 79:
    print("საშუალო")
if score >= 60 and score <= 69:
    print("ცუდია")
if score >= 0 and score <= 59:
    print("ძალიან ცუდი")


age = int(input("enter age:"))
if age >= 10:
    print("შენ შეგიძლია ატარო ზილი")
if age >= 25:
    print("შენ შეგიძლია ატარო იკარუსი")
if age <= 9:
    print("შენ არ შეგიზლია მართო არც ზილი არც იკარუსი")    


temperature = int(input("enter temperature:"))
if temperature >= 25:
    print("მოკლე შარვალი და მაისური")
if temperature <= 10:
    print("ქურთუკი და ქოლგა")
if temperature >= 11 and temperature <= 24:
    print("ჩვეულებრივი ტანსაცმელი")


# boss level
print(8 * " " + "*")
print(7 * " " + 3 * "*")
print(6 * " " + 5 * "*")
print(5 * " " + 7 * "*")
print(4 * " " + 9 * "*")
print(3 * " " + 11 * "*")
print(2 * " " + 13 * "*")
print(1 * " " + 15 * "*")