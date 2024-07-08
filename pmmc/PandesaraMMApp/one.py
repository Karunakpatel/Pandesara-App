
import datetime

def age_calculator(birthdate):
   today = datetime.date.today()
   age = (today - birthdate) // datetime.timedelta(days=365.2425)
   return age
birthdate = datetime.date(1991, 5, 14)
age = age_calculator(birthdate)

print("your age",age)