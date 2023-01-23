import getpass

database = {"Amal":"5678", "Kamal":"1234"}
username = input("Enter the Username: ")

password = getpass.getpass("Enter the Password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again : ")
        break
print("verified")