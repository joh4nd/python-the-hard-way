
"""
note: the author's tests seem more like integration tests than like unittests. Each function is not tested independently. E.g. see the names of test_'some_function': room_paths() and map() are not functions in ex47_game.py.

- https://softwareengineering.stackexchange.com/questions/221766/how-to-structure-tests-where-one-test-is-another-tests-setup
- https://softwareengineering.stackexchange.com/questions/423253/how-do-you-unit-test-functions-split-in-smaller-functions
- https://softwareengineering.stackexchange.com/questions/225323/how-should-i-test-the-functionality-of-a-function-that-uses-other-functions-in-i
- https://stackoverflow.com/questions/58788214/how-to-properly-unit-test-code-inside-of-a-python-function
- https://stackoverflow.com/questions/30283767/how-should-i-unit-test-functions-with-many-subfunctions

"""

from ex47_game import Room
# nose.tools import * # I refactored the script to pytest instead. terminal: pytest ex47_test.py

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert gold.name == "GoldRoom"
    assert gold.paths == {} # changed to dict in ex47_game.py

def test_room_paths(): # there is not room_paths() function
    center = Room("Center", "Test room in the center")
    north = Room("North", "Test room in the north")
    south = Room("South", "Test room in the south")
    
    center.add_paths({'north': north, 'south': south}) # dict, not list
    assert center.go('north') == north
    assert center.go('south') == south
    
def test_map(): # there is no map() function
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    
    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start
