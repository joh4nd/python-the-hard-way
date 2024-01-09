

# Python code to illustrate how mangling works  
# With method overriding 
  
class Map:  

    def __init__(self):  
        self.__geek() # during instantiation, calls __geek() i.e. _Map__geek. Requires that this is defined!
        self.__dumdum() # kræver """__dumdum = dumdum  """
        self.geek = geek()
        self.geekz = "geeeeky"
        print(self.geekz)
          
    def geek(self):  
        print("In parent class")  
    
    def dumdum(self):
        print("en ting til")
    
    # private copy of original geek() method  
    # __geek = geek
    # print(__geek) # <function Map.geek at 0x7fe4b1d1ba60>
    
    # eller en lokal kopi af dumdum funktionen:
    __geek = dumdum # prints en ting til
    
    # self.__dumdum
    __dumdum = geek # prints In parent class



class geek:
    def __init__(self):
        print("geekz")
        self.geek()
        
    def geek (self):
        print("geekzer")

    
class MapSubclass(Map):  
        
    # provides new signature for geek() but  
    # does not break __init__()  
    def geek(self):          
        print("In Child class") 
          
# Driver's code 
obj2 = Map()
print()
print()
obj2._Map__geek.__call__() # prints Map.geek()
obj2._Map__dumdum.__call__() # prints Map.dumdum()
# print()
# obj = MapSubclass() # instantiates a Map class and in doing so prints In parent class
# obj._Map__geek
# obj.geek() # prints In Child class



