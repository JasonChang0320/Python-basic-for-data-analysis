#if else eilf:
grade=80

# if (grade>=60 and grade<100):
if grade>=60:
    print("pass")
elif grade<60:
    print("fail")
elif grade==100:
    print("good job")
else:
    print("ok")

#for loop
fruits=["watermelon","guava","strawberry"]

for fruit in fruits:
    print(fruit)

for index in range(len(fruits)):
    print(fruits[index])

for fruit in fruits:
    if fruit!="guava":
        print(fruit)
    else:
        print("I hate guava !")

for i in ["A","B","C"]:
    print(i)
    for j in [1,2,3]:
        print(j)

#單行for迴圈 
number_list=[num for num in [1,4,9,16,25,36]]
number_square=[num**(1/2) for num in [1,4,9,16,25,36]]


#while loop
index=0
while index<20:
    index+=1
    print(index)

index=0
while index<20:
    index-=1
    print(index)

#pass, continue, break

for number in range(20):
    if number<10:
        pass
        print("ok")
    elif number<15:
        continue
    elif number >18:
        break
    print(f"原本數字:{number} | 數字平方:{number**2}")


