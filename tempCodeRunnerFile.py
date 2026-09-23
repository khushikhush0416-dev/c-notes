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