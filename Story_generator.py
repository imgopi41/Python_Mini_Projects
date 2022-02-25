import random #importing Random Library

when = ["2011","2012","2013","2014","2015","2016"]  #stories storing in "when" variable
who = ["Dhoni","kohli","Sachin","Dravid","Rohit","Shreyas"] #stories storing in "who" variable 
what =["scored 91*","was Captain for Rcb","Retired","scored 69 versus england","played his first ODI WC","made his debut in DD"]  #stories storing in "what" variable
where = ["at Mumbai","at India","at Banglore","at Lords","at Australia","at Delhi"] #stories storing in "where" variable
print(random.choice(when)+" "+random.choice(who)+" " +random.choice(what)+" "+random.choice(where)) #printing initialized variable inside random.choice
