import datetime

def ageCalculator(y, m, d):
    today = datetime.datetime.now().date()
    DOB = datetime.date(y, m, d)
    age = int((today-DOB).days / 365.25)
    print("Age :", age)
    
ageCalculator(1998,12,30)
