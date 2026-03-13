class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
        return(self.width*self.height)

    def perimeter(self):
        return((self.width+self.height)*2)
    def is_square(self):
        a="True" if self.width==self.height else "False"
        return a
rect = Rectangle(5, 10)
print(rect.area())       
print(rect.perimeter())   
print(rect.is_square())