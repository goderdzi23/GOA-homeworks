age = int(input("enter your age:"))
if age >= 17:
    print("შენ შეგიძლია მანქანის მართვა")
else:
    print("შენ არ შეგიძლია მანქნის მართვა")


temperature = int(input("enter temperature:"))
if temperature >= 25:
    print("თბილა")
else:
    print("ცივა")


bread_mount = int(input("enter amount of bread:"))
if bread_mount >= 5:
    print("გვაქვს პურა")
else:
    print("პური საყიდელია")


money = int(input("enter money:"))
if money >= 200:
    print("შენ იყიდე მაიკა, მშვიდობაში:)")
else:
    print("ფასდაკლება 40%")


num = int(input("enter num:"))
if num % 2 == 0:
    print("ლუწი")
else:
    print("კენტი")