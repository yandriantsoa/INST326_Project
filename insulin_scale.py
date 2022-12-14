class Sugar:
    def __init__(self, level: int):
        self._level = level
    """
    This is a property attribute of Sugar that get the sugar level
    and determines insulin intake
    """
       
    @property
    def sugar_level(self):
        print("Accessing sugar level")
        if self._level < 70:
            print ("Inititate Hypoglycemia Protocol")
        elif self._level >=70 and self._level <= 130:
            print ("Take 0 units")
        elif self._level >=131 and self._level <= 180:
            print ("Take 2 units")
        elif self._level >=181 and self._level <= 240:
            print ("Take 4 units")
        elif self._level >=241 and self._level <= 300:
            print ("Take 6 units")
        elif self._level >=301 and self._level <= 350:
            print ("Take 8 units")
        elif self._level >=351 and self._level <= 400:
            print ("Take 10 units")
        elif self._level > 400:
            print ("Take 12 units and CALL the doctor office for further instructions.")
        else: 
            print ("Please try again. Enter your current blood sugar level.")
        return self._level
          
    @sugar_level.setter
    def sugar_level(self,value):
        print(f'Sugar level is now {value}')
        self._level = value
        
    @sugar_level.deleter
    def sugar_level(self):
        print('Sugar level was deleted')      



''' defining main menu of app'''
def main():
    print ('\n---------------------------------------------------------------')
    print ("Moderate Dose Insulin Sliding Scale")
    print ("\nSuggested starting point for average patient")


   
if __name__== '__main__':
    sugar = Sugar(130)
    print(f'The sugar level is {sugar.sugar_level}')