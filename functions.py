import time
import string
import textwrap
import sys

#Tuple with Exit values. 
exit_tuple =(
    "quit",
    "exit",
    "q",
    "e",
    "break",
    "shutdown",
    "shut down"
    )

sector_tuple = (
    "SECTOR",
    "sector",
    "sec",
    "s",
    "S"
    )


#Simple Prompt.
def prompt(answer = "Please Enter SELECTION: "):
    answer = input(answer)
    return answer
    
#clears screen
def clear_screen():
    print("\n" * 90)


#Displays a pyramid Logo. fairly adjustable. 
def pyramid_logo(sleep = 00, p_width = 35,modify_point =.00, pudge = 2):
    pos = 0
    for line in range(0,p_width,pudge):
        time.sleep(sleep)
        if line <= int(p_width * modify_point): 
            print(
                "  " 
                + " " * (p_width - line) 
                + ("%" * line) 
                + ("*" * line) 
                + ("" * (p_width- line))
                )
            
        else:
            pos = pos + 1
            print(
                "  " 
                + " " * (p_width - line) 
                + ("%" * int(line + pos)) 
                + ("*" * int(line - pos) + ("" * (p_width - line)))
                ) 
    
    
#Begin Format_String

def format_string(string,max_length = 78):
	
	final_output = textwrap.fill(string,initial_indent = " ",subsequent_indent = " ")
	
	return final_output
	
#end string format. 
    


#starts ship greeting."sleep" is used to modify the scrolling time of the intial start screen.  
def greeting(sleep = 00):
    clear_screen()
    pyramid_logo(sleep)
    time.sleep(sleep)
    print("\nHello User. ")
    time.sleep(sleep)
    print("=" * 81) 
    time.sleep(sleep)
    print("You are currently logged into a Mark V InfoGen NODE under the DREAMCATCHER alias.")
    time.sleep(sleep)
    print("=" * 81)
    time.sleep(sleep)
    print("\n\nPlease select menu option for more infomation. Type 'quit' to exit.\nTo restart type 'reboot'\n\n")
    time.sleep(sleep)
            

#function to create an expanding list with borders. 
def list_items(
    description,menu = {0 :"NULL VALUE"},
    frame_type ="*",
    border = int(83),
    frame = 30,
    first_row = 8
    ):
        
        
    #start menu creation
    
    selection_menu = {}
    
    #greeting()
    
    preamble = int(border / frame)
    size_k = first_row
    n = 1
    index = str(n)
    
    print ( 
    " " * (int((border / 2) - 1) - int(len("Index")+1)) \
    + "Index" 
    + " | "
    + description
    + " " * (int((border - 6) / 2) - int(len(description)+1))
    )
    
    print(frame_type * border)
    #creates a new dictionary based on the index and object title of the list contents. 
    for k, v in sorted(menu):
        selection_menu[index] = v
        front_space = int(size_k - len("000" + index))
        back_space =  border - ((preamble * 2) + 5 + 3 + len(k)) 
        
        print(
            frame_type * preamble 
            + " " * int(front_space) 
            + index 
            + " | " 
            + k
            + " " * back_space 
            + frame_type * preamble
            )
        
        n += 1
        
        index = str(n)
    
    print(frame_type * border)
    
    print("\n\n")
    
    #returns the new dictionary to be used to derive the function of each selection. 
    return selection_menu
    #finish Menu creation
    
    
    
    
    
def countdown(
    first_message = "LOADING",
    second_message = "COMPLETE",
    timer = 10,
    wait_time = .4
    ):
    
    print(first_message)
    time.sleep(wait_time)
    
    for n in range(timer):
        time.sleep(wait_time)
        sys.stdout.write(str(timer - n) + " ")
        sys.stdout.flush()
        
    print("\n" + second_message)
    time.sleep(wait_time)
    
    
















