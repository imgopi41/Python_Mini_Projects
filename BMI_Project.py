



name = input("Enter the name: ")    #user name   
feet = float(input("Enter your height in feet: "))    #user height 
Con_meter = feet/3.281  #converting height feet to meters
weight = float(input("Enter your weight: "))    #user weight
Bmi = weight / (Con_meter ** 2) #BMI formula used to notify user is under weight or over weight.

if Bmi <=25: # checking BMI is below or equal to '25'.
    print("Congratulations {} your are under weight by {} is your body mass index".format(name,Bmi))   #under-weight message
else:
    print("oops..!{} your are over weight by {} is your body mass index".format(name,Bmi))  #over-weight message





