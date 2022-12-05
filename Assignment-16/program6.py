"""6. Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)"""
tuple1=(100,200,300,400)
for i in tuple1:
    if i%100==0 or i%200==0 or i%300==0 or i%400==0 :
        print("yes it is divisible tuple")
        break
else:
    print("sorry it is not divisible")    
