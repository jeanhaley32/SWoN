import string
import textwrap


	
	
	
'''	
	
	#formats string to properly fit in display. mostly just word wraps based on line length defined by "length"
def format_string(text,length = 92):
   index = 0
    endstring = ''
    wasNL = False
    wasAlpha = False
    while index < len(text):
        if wasNL:
            if text[index].isalpha():
                if wasAlpha:
                    endstring += text[index]
                    index += 1
                    wasNL = False
                    wasAlpha = False
                    continue
                else:
                    endstring += text[index]
                    index += 1
                    wasNL = False
                    continue
                
            if text[index] == " " or text[index == "\\"]:
                index += 1 
                wasNL = False
                continue
        if index % length == 0 and index != 0:
            if text[index].isalpha():
                endstring += text[index]
                endstring += "-"
                endstring += "\n "
                wasAlpha = True
                wasNL = True
                index += 1
                continue
            
            if text[index] == " ":
                endstring += "\n "
                wasNL = True
                index += 1
        else:
            endstring += text[index]
            index += 1
            
    return endstring
#End Format_string    




#Begin Format_String


def format_string(string,max_length = 52):
    
	#defines a tuple for vowels and consonant's to be used as comparison 
	#points when figuring out where the hypher should go when splitting
	#a word between lines. 
	
	vowel_tuple = ("a","e","i","o","u","y")

	consonant_tuple = ("b","c","d","f","g","h","i","j","k","l","m","n","o"
	,"p","q","r","s","t","v","w","x","z")

	string_list = []

	formated_string = ""
    
	string_list = string.split(" ")


	while True:
		
        #loops through string_list while it contains data, moving all
		#portions of data to the final "formated_string"
		while string_list:
			
			container_string = ""
			container_list = []
			index = 0
			
			for word in string_list:
				
				while len(container_string) <= max_length:
					if string_list:
						container_string += string_list.pop(0) + " "
					else:
						break

			print("-----" + container_string + "-----" + "\n\n")
					
			if len(container_string) > max_length:
				container_list = container_string.split(" ")
				final_word = container_list[-1]
				
				for word in container_list:
					if word == final_word:
						if len(word) <= 4:
							formated_string += word + "\n" + " "
						else:
							ishyphen = False
							index = 0
							for letter in word:
								if index <= 3:
									formated_string += letter
									index += 1
									
								if index > 3 and letter not in vowel_tuple:
									formated_string += letter + "-" + "\n"
									ishyphen = True
									
								if ishyphen == True:
									formated_string += letter
							formated_string += " "
							
					else:
					    formated_string += word + " "
			else:
				
				new_line = False
				
				while container_string:
					while len(container_string) > max_length:
						formated_string += container_string[0] + " "
						container_string.remov[0]
					
					if container_string:
						for word in container_string:
							if new_line == False:
								formated_string += "/n" + word
								new_line = True
						
							if new_line == True:
								formated_string += word + " "
					
				
				
			            
                        
		formated_string = " " + formated_string
		return formated_string	






string_to_print = format_string("Hello, this is a test string. It should have several line and should be fairly long.\
Hopefully if this works properly i'll be able to print this out and have it work properly.")

print(string_to_print)


'''

str = "Hello, this is a test string. It should have several line and should be fairly long.\
 Hopefully if this works properly i'll be able to print this out and have it work properly."

#final_output = textwrap.fill(str)

final_output = str.ljust(1)


print (final_output)