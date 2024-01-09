class Parent(object):
    
    def override(self):
        print("PARENT override()")
    
    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
        
#    def __init__(self, stuff):
#        self.stuff = stuff
#        super(Child, self).__init__()
    
dad = Parent()
son = Child()

dad.implicit() # print Parent.implicit()
son.implicit() # print Parent.implicit()

dad.override() # print Parent.override()
son.override() # print Child.override() - overwrites

dad.altered() # print Parent.altered()
son.altered() # print Child.altered() which includes Parent.altered()
