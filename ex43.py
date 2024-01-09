# Game Engine for the small adventure game: Gothons from Planet Percal #25

"""
Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below. The game will be more like a Zork or Adventure type game with text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes. Each room will print its own description when the player enters it and then tell the engine what room to run next out of the map.

* Map
 - next_scene
 - opening_scene
* Engine
 - play
* Scene
 - enter
 * Death
 * Central Corridor
 * Laser Weapon Armory
 * The Bridge
 * Escape Pod
"""

from sys import exit
from random import randint # Return random integer in range [a, b], including both end points.

class Scene(object):
    
    def enter(self):
        Print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Death(Scene):
    # This is when the player dies and should be something funny.
    
    deaths = [
        "No, Mr. Bond. I expect you to die.",
        "Uuurrghh",
        "1 million ways to die, choose one!",
        "Wasted!"
    ]
    
    def enter(self):
        print(Death.deaths[randint(0, len(self.deaths)-1)])
        exit(1)


class CentralCorridor(Scene):
    # This is the starting point and has a Gothon already standing there, which the player has to defeat with a joke before continuing.
    
    def enter(self):
        # print description
        print(
        """
        The Gothons of Planet Percal #25 have invaded your ship and destroyed
        your entire crew. You are the last surviving member and your last
        mission is to get the neutron destruct bomb from the Weapons Armory,
        put it in the bridge, and blow the ship up after getting into an
        escape pod.
        
        You're running down the central corridor to the Weapons Armory when
        a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
        flowing around his hate filled body. He's blocking the door to the
        Armory and about to pull a weapon to blast you.
        """)
        
        # tell engine what room to run next out of the map
        
        action = input("> ")
        
        if action == "shoot!":
            print(
            """
            Quick on the draw you yank out your blaster and fire it at the Gothon.
            His clown costume is flowing and moving around his body, which throws
            off your aim. Your laser hits his costume but misses him entirely. This
            completely ruins his brand new costume his mother bought him, which
            makes him fly into a rage and blast you repeatedly in the face until
            you are dead. Then he eats you.
            """)
            return 'death'
        
        elif action == "dodge!":
            print(
            """
            Like a world class boxer you dodge, weave, slip and slide right
            as the Gothon's blaster cranks a laser past your head.
            In the middle of your artful dodge your foot slips and you
            bang your head on the metal wall and pass out.
            You wake up shortly after only to die as the Gothon stomps on
            your head and eats you.
            """)
            return 'death'
        
        elif action == "tell a joke":
            print(
            """
            Lucky for you they made you learn Gothon insults in the academy.
            You tell the one Gothon joke you know:
            Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
            The Gothon stops, tries not to laugh, then busts out laughing and can't move.
            While he's laughing you run up and shoot him square in the head
            putting him down, then jump through the Weapon Armory door.
            """)
            return 'laser_weapon_armory'
        
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
        
#    def fight(self):
#       # fight is a verb - could translate into a function???
#        pass


class LaserWeaponArmory(Scene):
    # This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad he has to guess the number for.
    
    def enter(self):
        print(
        """
        You do a dive roll into the Weapon Armory, crouch and scan the room
        for more Gothons that might be hiding. It's dead quiet, too quiet.
        You stand up and run to the far side of the room and find the
        neutron bomb in its container. There's a keypad lock on the box
        and you need the code to get the bomb out. If you get the code
        wrong 10 times then the lock closes forever and you can't
        get the bomb. The code is 1 digit.
        """)
        # code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9)) # redicolously difficult code
        code = "%d" % randint(1,9) # 
        guess = input("[keypad]> ")
        guesses = -1 # fixed bug
        
        # tell engine what room to run next out of the map
        
        while guess != code and guesses < 3: # changed from 10 to 3
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")
            
        if guess == code:
            print(
            """
            The container clicks open and the seal breaks, letting gas out.
            You grab the neutron bomb and run as fast as you can to the
            bridge where you must place it in the right spot.
            """)
            return 'the_bridge'
            
        else:
            print(
            """
            The lock buzzes one last time and then you hear a sickening
            melting sound as the mechanism is fused together.
            You decide to sit there, and finally the Gothons blow up the
            ship from their ship and you die.
            """)
            return 'death'

class TheBridge(Scene):
    # Another battle scene with a Gothon where the hero places the bomb.
    
    def enter(self):
        print(
        """
        You burst onto the Bridge with the neutron destruct bomb
        under your arm and surprise 5 Gothons who are trying to
        take control of the ship. Each of them has an even uglier
        clown costume than the last. They haven't pulled their
        weapons out yet, as they see the active bomb under your
        arm and don't want to set it off.
        """)
        
        # tell engine what room to run next out of the map        
        action = input("> ")
        
        if action == "throw the bomb":
            print(
            """
            In a panic you throw the bomb at the group of Gothons
            and make a leap for the door. Right as you drop it a
            Gothon shoots you right in the back killing you.
            As you die you see another Gothon frantically try to disarm
            the bomb. You die knowing they will probably blow up when
            it goes off.
            """)
            return 'death'
        
        elif action == "slowly place the bomb":
            print(
            """
            You point your blaster at the bomb under your arm
            and the Gothons put their hands up and start to sweat.
            You inch backward to the door, open it, and then carefully
            place the bomb on the floor, pointing your blaster at it.
            You then jump back through the door, punch the close button
            and blast the lock so the Gothons can't get out.
            Now that the bomb is placed you run to the escape pod to
            get off this tin can.
            """)
            return 'escape_pod'
            
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

        
class EscapePod(Scene):
    # Where the hero escapes but only after guessing the right escape pod.

    def enter(self):
        print(
        """
        You rush through the ship desperately trying to make it to
        the escape pod before the whole ship explodes. It seems like
        hardly any Gothons are on the ship, so your run is clear of
        interference. You get to the chamber with the escape pods, and
        now need to pick one to take. Some of them could be damaged
        but you don't have time to look. There's 5 pods, which one
        do you take?
        """)

        # if it makes sense; tell engine what room to run next out of the map

        good_pod = randint(1,5)
        guess = input("[pod #]> ")
        
        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button. % guess")
            print("""
            The pod escapes out into the void of space, then
            implodes as the hull ruptures, crushing your body
            into jam jelly.
            """)
            return 'death'
            
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print(
            """
            The pod easily slides out into space heading to
            the planet below. As it flies to the planet, you look
            back and see your ship implode then explode like a
            bright star, taking out the Gothon ship at the same
            time. You won!
            """)
            return 'finished'


class Engine(object):
    # runs a map full of scenes
    
    def __init__(self, scene_map): # presumes an instance of Map() as its argument (see play()
        # assert scene_map.start_scene in scene_map.scenes # test whether returned scene name is in scene
            # else exit(1)
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene() # the opening_scene() method in the instance of map() is called.
        
        while True:
            print("\n--------")
            next_scene_name = current_scene.enter() # runs the enter() method in the instance of the scene class, which is at the outset must have been defined as an argument to map().
            current_scene = self.scene_map.next_scene(next_scene_name) # takes a scene name and returns an instance of the scene class corresponding to the scene name in the dict


class Map(object):
    
    scenes = { # changed square brackets [] for qurly brackets {} to make proper dict
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    } # a dict takes get()
    
    def __init__(self, start_scene):
        if start_scene not in self.scenes:
            raise ValueError(f"Invalid argument: {start_scene} must be central_corridor")
            
        self.start_scene = start_scene

    
    def next_scene(self, scene_name):
        assert scene_name in self.scenes, f"Invalid argument: {scene_name} must be real: {list(self.scenes.keys())}" # test whether returned scene name is in scene
        return Map.scenes.get(scene_name) # opens the scene name in scenes dict that has been provided as an argument to next_scene()
    
    def opening_scene(self):
        return self.next_scene(self.start_scene) # opening scene starts in __init__()
        
    # closing scene: EscapePod

class Gothon(object):
    # NEW: Gothon alien to fight the hero in scenes e.g. TheBridge
    # update: the solution does not require such class
    
    def __init__(self):
        pass




a_map = Map('central_corridor') # chooses start_scene
a_game = Engine(a_map) # a_game stores 
#a_game.play() # runs game engine i.e. opening scene to next scene


"""
How the program works

The game starts by passing 'central_corridor' to Map(). This creates an instance of the Map() class with that argument, defining the start_scene. The instance stores all the scenes and has the methods. Running the opening_scene() method runs the start_scene. The next_scene() methods takes the 'scene_name' as argument, which must be returned to it to provide the corresponding scene class instance. 



"""
