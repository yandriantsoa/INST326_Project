# Insulin sliding scale application
# Patricia, Michael, Yannrick, Kedrala

''' defining main menu of app'''
def main():
    print ('\n---------------------------------------------------------------')
    print ("Moderate Dose Insulin Sliding Scale")
    print ("\nSuggested starting point for average patient")
    print ('-----------------------------------------------------------------')
    sugar_level()
    insulin_intake(sugar_level)



''' defining insulin intake in units according to user's input'''
def insulin_intake(sugar_no):    
    ''' ask user to input blood sugar value'''
    sugar_no = int(input("Please enter your Blood Sugar(mg/dL) value from your glucometer:\n"))
    return sugar_no

'''declaring the conditions'''
if sugar_no < 70:
   print ("Inititate Hypoglycemia Protocol")
elif sugar_no >=70 and sugar_no <= 130:
   print ("Take 0 units")
elif sugar_no >=131 and sugar_no <= 180:
   print ("Take 2 units")
elif sugar_no >=181 and sugar_no <= 240:
   print ("Take 4 units")
elif sugar_no >=241 and sugar_no <= 300:
   print ("Take 6 units")
elif sugar_no >=301 and sugar_no <= 350:
   print ("Take 8 units")
elif sugar_no >=351 and sugar_no <= 400:
   print ("Take 10 units")
elif sugar_no > 400:
   print ("Take 12 units and CALL the doctor office for further instructions.")
else: 
    print ("Please try again. Enter your current blood sugar level.")