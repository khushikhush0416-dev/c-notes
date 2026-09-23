#creating a class named book
class book:
#it run automatically when object is created
    def __init__ (self, title , author , price , quantity):
        #store in the object
        self.title= title
        self.author =author
        self.price= price
        self.quantity= quantity
        #display the details
    def display(self):
          print("author:",self.author)
          print("price:",self.price)
          print("quantity:",self.quantity)

#function
    def totalvalue(self):
        print(self.price*self.quantity)
b1= book("c","ansii",100,3)    

    #calling function
b1.display()
s2=b1.totalvalue
    
     #printing the value and author   
print("total value of book",s2.totalvalue)
print("author name and value of book", b1.author(),s2)
      


class employee:
    def __init__ (self, name, department , salary, performance_score):
        self.name= name
        self.department = department
        self.slary= salary
        self. performance_score= performance_score
    def (self):
        print()
    def (self):
        print(self.value)
    print("",())
    print("", ())


 #creating class
class electricitybill:
    def __init__(self,customer_name,units,rate_per_unit):
        self.customer_name=customer_name
        self.units=units
        self.rate_per_unit=rate_per_unit

    def calculate_bill(self):
        bill = self.units* self.rate_per_unit

        if bill >2000:

          bill = bill+(bill *5/100)
        return bill
    def display(self):
       print("customer name", self.customer_name)
       print("rate per unit", self.rate_per_unit)
       print("final bill",self.alculate_bill)
       print()

customer1 =electricitybill("khushi",160,12)
customer2 =electricitybill("rajiv",220,11)
customer3 =electricitybill("mohani",100,18)
print("electricitybill details")

customer1.display
customer2.display
customer3.display

total_bill = (
   customer1.calculate_bill()
   +customer2.calculate_bill()
   +customer3.calculate_bill()
   
)
average_bill = total_bill/3
print("average electricitybill",average_bill)