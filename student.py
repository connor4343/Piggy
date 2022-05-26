#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 75
        self.RIGHT_DEFAULT = 75 
        self.MIDPOINT = 1475  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "v": ("Varmecky", self.varmecky),
                "m": ("MW", self.move_to_wall),
                "t": ("WT", self.wall_turn),
                "b": ("MTB", self.move_to_box),
                "sc": ("Scan", self.scan)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''
    def varmecky(self):
      for side in range(4):
        self.fwd()
        time.sleep(2)
        self.right()
        time.sleep(.875)
      self.stop()
        
    def safe_to_dance(self):
      self.read_distance()
      self.servo(1000)
      if self.read_distance() > 700:
        self.servo(2000)
        self.read_distance()
        if self.read_distance() > 700:
          self.servo(1000)
          self.read_distance()
          self.right(primary=90, counter=-90)
          time.sleep(2.5)
          if self.read_distance() > 700:
            return True
          if self.read_distance() < 700:
            return False
            self.stop()
        
       
        if self.read_distance() < 700:
            return False
            self.stop()
      if self.read_distance() < 700:
        return False
        self.stop()
        
      self.stop()
         
    def move_to_wall(self):
      while self.read_distance() > 700:
        self.fwd()
      self.stop()
        
          

    def wall_turn(self):
      while True:
        self.fwd()
        self.read_distance()
        if self.read_distance() <= 600:
          self.right(primary = 90, counter = -90)
          time.sleep(.85)
          
   
  
    def move_to_box(self):
      self.servo(1475)
      while self.read_distance() > 200:
        self.fwd()
      self.stop()
      self.servo(1050)
      time.sleep(1)
      right = self.read_distance()
      self.servo(1950)
      time.sleep(1)
      left = self.read_distance()
      print("123")
      if right > left:
        print("first one read")
        self.right(primary=90, counter=-90)
        time.sleep(.45)
        self.fwd()
        self.servo(2000)
        while self.read_distance() < 2000:
          self.fwd()
          self.servo(2250)
          print("second one read")
        self.fwd()
        time.sleep(.75)
        self.left(primary=90, counter=-90)
        time.sleep(.4)
        self.fwd()

      else:
        print("it reached the else")
        self.servo(2000)
        print("it reached the else2")
        while self.read_distance() > 1000:
          print("it reached the else3")
          self.left(primary=90, counter=-90)
          time.sleep(.45)
          self.fwd()
          self.servo(1000)
          while self.read_distance() < 2000:
            self.fwd()
            self.servo(750)
          self.fwd()
          time.sleep(.75)
          self.right(primary=90, counter=-90)
          time.sleep(.4)
          self.fwd()
          print("it reached the else4")
          
        
    def scan(self):
      while True:
        self.fwd(30,30)
        time.sleep(.25)
        self.servo(1475)
        time.sleep(.2)
        center = self.read_distance()
        print("1")
        
        self.servo(1900)
        time.sleep(.2)
        left = self.read_distance()
        
        self.servo(1100)
        time.sleep(.2)
        right = self.read_distance()
       
        
        if center < 600 and left < 600:
          
          if right > center and right > left:
            self.stop()
            print("it reached the else2")

            self.right(primary=90, counter=-90)
            time.sleep(.45)
            self.fwd()
            self.servo(2000)
            while self.read_distance() < 2000:
              self.fwd()
              self.servo(2250)
            self.fwd()
            time.sleep(.75)
            self.left(primary=90, counter=-90)
            time.sleep(.4)
            self.fwd()
        elif left < 600:
          
            self.stop()
            self.right(primary=90, counter=20)
            time.sleep(.4)
            self.fwd()
            time.sleep(.4)
            self.left(primary=90, counter=20)
            time.sleep(.4)
            self.fwd()
          
        
        if center < 600 and right < 600:
          
          if left > center and left > right:
            self.stop()
            print("first one read")
            self.servo(1000)
            self.left(primary=90, counter=-90)
            time.sleep(.45)
            self.fwd()
            self.servo(1000)
            while self.read_distance() < 2000:
              self.fwd()
              self.servo(750)
              print("second one read")
            self.fwd()
            time.sleep(.75)
            self.right(primary=90, counter=-90)
            time.sleep(.4)
            self.fwd() 
        elif right < 600:
          
    
            self.stop()
            self.left(primary=90, counter=20)
            time.sleep(.4)
            self.fwd()
            time.sleep(.4)
            self.right(primary=90, counter=20)
            time.sleep(.4)
            self.fwd()
            
    
      
      


      
    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        # TODO: check to see if it's safe before dancing
        
        if self.safe_to_dance() == True:
          # lower-ordered example...
          self.right(primary=90, counter=-90)
          time.sleep(1.75)
          self.fwd()
          time.sleep(1)
          self.back()
          time.sleep(2)
          for shake in range(5):
            self.left(primary=90, counter=-45)
            time.sleep(.1)
            self.right(primary=90, counter=-45)
            time.sleep(.1)
        else:
          print("you don't have enough room to dance")
        self.stop()
        
        

    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left



    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
