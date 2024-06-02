weight=float(input("enter your weight in kg:"))
height= float(input("enter your height in meters :"))
bmi=weight/(height**2)
print ("your bmi is=",bmi)
if bmi<18.5:
    print("under weight")
elif 18.5<=bmi<25:
    print("heatlthy weight")
else:
    print("over  weight")