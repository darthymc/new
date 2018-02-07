class holidays:
    "common holiday for all"
    count=0
    def __init__(self,date,name):
        self.date=date
        self.name=name
        holidays.count+=1
    def displaycount(self):
        print"no of holidays are:",holidays.count
    def displayholiday(self):
        print self.date,"-->",self.name
holiday1=holidays('1-1-18','new year')
holiday2=holidays('15-1-18','sankaranthi')
holiday3=holidays('26-1-18','republic day')
holiday4=holidays('30-3-18','good friday')
holiday5=holidays('1-5-18','labor day')
holiday6=holidays('15-8-18','Independence day')
holiday7=holidays('13-9-18','Ganesh chathurthi')
holiday8=holidays('2-10-18','Gandhi jayanthi')
holiday9=holidays('07-11-18','Diwali')
holiday10=holidays('25-12-18','christmas')
holiday1.displayholiday()
holiday2.displayholiday()
holiday3.displayholiday()
holiday4.displayholiday()
holiday5.displayholiday()
holiday6.displayholiday()
holiday7.displayholiday()
holiday8.displayholiday()
holiday9.displayholiday()
holiday10.displayholiday()
print"no of holidays are:",holidays.count
print "holidays.doc:",holidays.__doc__
print"holidays.name:",holidays.__name__
print"holidays.module:",holidays.__module__
print"holidays.bases:",holidays.__bases__
print"holidays.dict:",holidays.__dict__





