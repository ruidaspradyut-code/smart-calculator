class Basic:

    def addition(self,a,b):
        return a+b
    
    def subtraction(self,a,b):
        return a-b
    
    def multiplication(self,a,b):
        return a*b
    
    def division(self,a,b):
        if b==0:
            print("Csn't be divided by zero!")
        else:
            return a/b
        
    def percentage(self,a,b):
        return (a/b)*100
    
