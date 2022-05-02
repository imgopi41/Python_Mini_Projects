import datetime #importing datetime module

class User():   #defining a class as "User".
    def __init__(self,name,birthday):   #initializing init method defining name,birthday inside init method
        self.fullname = name    #assigning key 
        self.bday = birthday

        ans = name.split(" ")   #spliting a given name 
        self.fname= ans[0]  #reading first name
        self.lname=ans[1]   #reading last name

    def age(self):  #defining function called age

        today = datetime.date(2022,3,28)    #assigning today's date using datetime lib in variable called today
        year = int(self.bday[0:4])  
        month = int(self.bday[4:6])
        day = int(self.bday[6:8])
        dob = datetime.date(year,month,day)
        age_in_days = (today-dob).days
        age_in_year = age_in_days/365
        return int(age_in_year) #returning the calculated year

result = User("Rahul Dravid","19720111")    #defining our class
print(result.fname) #calling the key with object assigned to it
print(result.lname)
print(result.fullname)
print(result.age())
print(result.fullname,result.age(),result.bday)
