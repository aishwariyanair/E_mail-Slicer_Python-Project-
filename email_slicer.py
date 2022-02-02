# Email slicer


email_id=input("Enter your email address: ")

# slicing email & domain name

username=email_id[:email_id.index("@")]
domain=email_id[email_id.index("@")+1:]
print(f"Your username is  {username} and domain name is {domain}")