class Other(object):

    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def overriderrr(self):
        print("CHILD override() - except it is not overwritten")
        print("... and from Other():")
        self.other.override()
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.overriderrr() # son.override()
son.altered()
