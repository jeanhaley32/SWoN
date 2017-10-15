import functions
import classes
import sys
import time
import classes
import regions


#start of start_menu
start_menu_list = {
    "Governing Bodies" : regions.governments
    }
start_menu = classes.Menu("selection", start_menu_list.items())
#end of start_menu 


first_start = True

while True:
    #initializes greeting. 
    if first_start:
        functions.greeting(.09)
        first_start = False
    else:
        functions.greeting()
    
    #starts first menu.    
    start_menu.info()
