# Implicit inheritance
class Parent(object):
    # the base class
    
    def implicit(self):
        print("PARENT implicit()")
    
class Child(Parent):
    # subclass
    pass # empty block

dad = Parent()
son = Child()

dad.implicit()
son.implicit() # yet this call works

print()
print()
print()

# Override Explicitly
class Kingdom(object):
    
    def override(self):
        print("KINGDOM override()")

class Country(Kingdom):
    
    def override(self):
        print("COUNTRY override()")

UK = Kingdom()
England = Country()

UK.override()
England.override()

print()
print()
print()

# Alter Before or After
class Universe(object):
    
    def altered(self):
        print("UNIVERSE altered()")
        
class Planet(Universe):
    
    def altered(self):
        print("Planet, BEFORE Universe altered()")
        super(Planet, self).altered()
        print("Planet, AFTER Universe altered()")
        
class Continent(Planet):
    def altered(self):
        print("CONTINENT altered()...")
        print("Continent, BEFORE super1")
        print()
        super(Continent, self).altered()
        print()
        print("Continent, AFTER super1...")
        print("Continent, BEFORE super2")
        print()
        super(Planet, self).altered()
        print("Continent, AFTER super2")
        print("...CONTINENT altered()")

milkyway = Universe()
mother_earth = Planet()
africa = Continent()

milkyway.altered()
print()
mother_earth.altered()
print()
africa.altered()
