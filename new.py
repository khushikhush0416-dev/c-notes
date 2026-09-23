# i=1
# while i<=10:
#     print(i)
#     i=i+1

# i=1
# while i>=10:
#     print(i)
#     i -=1

# for i in range (3):
#     for j in range (2):
#         print(i,j)







# for i in range (1,10):
#     if i == 5 :
#         break
#     print(i)

# for i in range (1,6):
#     if i==3 :
#         continue
#     print(i)

# class student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks

#     def display(self):
#         print("Name:",self.name)
#         print("Roll no:",self.rollno)
#         print("Marks:",self.marks)

#     def percentage(self):
#         total=sum(self.marks)
#         percentage=total/len(self.marks)

#     print("Percentage:",percntage)

# student1=student("khushi",11,[78,67,88])
# student1.display()
# student1.percentage()

class rectangle:
    def __init__(self, length , breadth ):
        self.length =length
        self.breadth= breadth
    def  area(self):
            print(self.length*self.breadth)
    def perimeter(self):
            print(2*(self.length+self.breadth))
s1 = rectangle(5,10)
print ( "area of rectangle:", s1.area())
print( " perimeter of rectangle:",s1.perimeter())




