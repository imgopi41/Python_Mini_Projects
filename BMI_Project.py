print("lets check our body mass")   #welcome message

print("HI There...\n")  #welcome message
name = input("Enter your name: ")   
weight = float(input("Enter your weight: "))    
height = float(input("Enter your height: "))    #User must give his/her height in meters
BMI = weight / (height ** 2)    #BMI formula

if BMI <= 25:   #if condition is less than or equal to '25'.
    print("Congratulations {} you are under weight by {} body mass index".format(name,BMI)) #your are under weight
else:   #if not 
    print("{} your over weight by {} body mass index".format(name,BMI)) #your are over weight.




