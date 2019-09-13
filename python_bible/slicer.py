#get user email address
email = input("What is your email address ? : ").strip()

#slice out user name
user = email[:email.index("@")]
#slice domain name
domain = email[email.index("@") + 1 :]
#format message
output = "your user name is {} and your domain is {}".format(user,domain)
#display output message
print(output)
