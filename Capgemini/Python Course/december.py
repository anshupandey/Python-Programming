"""
this modules helps in doing ABC
thanks
bye

"""



class employee:
    # class arguments
    age = 25
    city = ""
    
    def __init__(self,name):
        self.name = name
        print(f"Employee object created with name {self.name}")
            
    def onboarding(self):
        print(f"Employee {self.name} got onboarded")
        print("Age is ",self.age)
        
    def get_salary(self,exp,multi):
        return exp*multi
    
    
def myfunction():
    print("hello from python")
    return None

def spectrum(a,b=6):
    c = a+b
    return c