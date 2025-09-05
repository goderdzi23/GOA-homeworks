# for loop ები სხვადასხვა ელემენტებზე მისასვლელად და თითოეულ ელემენტებძე მოქმედების შესასრულებლად გამოიყენება.


num = int(input("შეიყვანე რიცხვი:"))
if num > 0:
    print("დადებითია")
elif num < 0:
    print("უარყოფითი")
else:
    print("ნულია")


num = int(input("შეიყვანე რიცხვი:"))
if num % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")


score = int(input("შეიყვანეთ შენი გამოცდის ქულა: "))
if score == 100:
    print("მალადეც")
elif score < 50:
    print("ჩაიჭერი")
else:
    print("საშუალო ქულა") 