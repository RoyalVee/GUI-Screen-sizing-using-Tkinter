from tkinter import *

"""this class is used to get a fullscreen by default when the constructor is called and root passed into it 
 
 or you can create yours

screenlength_x is for the screen length along x-axis
screenlength_y is for the screen length along y-axis

position_x is the space to create from the left of the screen before your created screen is placed
position_y is the space to create from the top of the screen before your created screen is placed

"""
class ScreenSize:
    def __init__(self, master):
        self.master = master
        self.screenWidth = master.winfo_screenwidth()               ##set the screen width to the window width of the computer
        self.screenHeight = master.winfo_screenheight()             ##set the screen height to the window height of the computer
        self.dist_Left_of_Screen = 0                                ##distance to give from the left side of the window
        self.dist_top_of_screen = 0                                 ##distance to give from the top side of the window
        master.geometry('{}x{}+{}+{}'.format(self.screenWidth, self.screenHeight, self.dist_Left_of_Screen, self.dist_top_of_screen))

    def makescreen(self, screenlength_x, screenlength_y, position_x = 0, position_y = 0,):
        self.master.geometry('{}x{}+{}+{}'.format(screenlength_x, screenlength_y, position_x, position_y))

