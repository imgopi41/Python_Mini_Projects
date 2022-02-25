import random

when = ["2011","2012","2013","2014","2015","2016"]
who = ["Dhoni","kohli","Sachin","Dravid","Rohit","Shreyas"]
what =["scored 91*","was Captain for Rcb","Retired","scored 69 versus england","played his first ODI WC","made his debut in DD"]
where = ["at Mumbai","at India","at Banglore","at Lords","at Australia","at Delhi"]
print(random.choice(when)+" "+random.choice(who)+" " +random.choice(what)+" "+random.choice(where))
