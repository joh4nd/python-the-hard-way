# -- coding: utf-8 --
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." %my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))
    
    
# study drill 2 try use %r
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the months: %r" % months) # %r prints syntax

# study drill 4: write functions that converts inches and pounds to centimeters and kilos

def inch_to_cm(inch):

    cm = inch * 2.5

    return cm
    
my_height_cm = inch_to_cm(my_height)

print("My height is %s cm." % round(my_height_cm))

def lb_to_kg(pounds):
    
    kilo = pounds * 0.45359237
    
    return kilo
    
my_weight_kg = lb_to_kg(my_weight)

print("My weight is %s kilos." % round(my_weight_kg))

