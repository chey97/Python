#For this task, you must first generate a google app password for your Gmail account.

import os, random, smtplib

def automatic_email():
    user = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    
#create the email msg
    message = (f"Dear {user}, Welcome to Pyhton Programming")
    
#The code creates a string variable called "message" and assigns it the value of a string that uses f-string formatting. The f-string includes a placeholder, {user}, which is a variable that should be defined before the code is executed and will be replaced by its value in the final string.
#The final string would be "Dear [user], Welcome to Thecleverprogrammer"

#send the email
    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login("chethiya.research@gmail.com", "pllwldgtpoxgzjjh")
    server.sendmail('&&&&&&&&&&&&&',email, message)
    server.quit()
    print("Email Sent!")
    
automatic_email()