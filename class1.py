class Calc():
    """ This is an calcultor program to perform add, mul, div, sub"""
    c = 0
    def __init__(self,a,b = None):
        self.x = a
        self.y = b
        Calc.c+=1
    def add(self):
        return print("Result = ",self.x+self.y)
    def mul(self,c):
        return print("Result = ",self.x*self.y*c)
    def sub(self):
        return print("Result = ",self.x-self.y)
    def div(self):
        if self.y == 0:
            print("Can't be return")  
        else: 
            print("Result = ",self.x/self.y)
    def call(self):
        print("No of copy = ",Calc.c)


def main():
    a = int(input("Enter value of a "))
    b = int(input("Enter value of b "))
    x = int(input("Enter value of x "))
    y = int(input("Enter value of y "))
    obj1 = Calc(a,b)
    obj2 = Calc(x,y)
    ch = int(input("Enter choice - \n1.add\n2.sub\n3.mul\n4.div"))
    if ch == 1:

        obj1.add()
        obj2.add()
    elif ch == 2:
        obj1.sub()
        obj2.sub()
    elif ch == 3:
        obj1.mul(int(input("Enter a value")))
        obj2.mul(int(input("Enter a value")))
    
if __name__ == '__main__':
    main()



