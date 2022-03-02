email = input("Enter the Email-Id : ")  
username = email[:email.index('@')] 
domain = email[email.index('@')+1:] 
result = "your username = {}\nyour domain = {}".format(username,domain)
print(result)


