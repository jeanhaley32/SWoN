import functions
import sys


NULL = "\nNo information available for this subject."

######################Classes###############################################################
#Start Menu Class
class Menu():
	"""Class to store menus"""
	
	def __init__(self,description,menu):
		
		self.description = description
		self.menu = menu
	
	#prints out menu based on the "list_items()" function with information from self.menu.
	def info(self):

		while True:
			functions.clear_screen()
			functions.pyramid_logo()
			functions.greeting()
			selection_menu = functions.list_items(self.description,self.menu)
			
			answer = functions.prompt()
			
			if answer in selection_menu:
				selection_menu.get(answer).info()
			#check answer against the exit tuple and runs a shutdown sequence if true.
			if answer in functions.exit_tuple:
				functions.countdown("\nSHUTTING DOWN APPLICATION.\n","",4)
				sys.exit("\nUSER TERMINATED APPLICATION.\n")
			#checks answer for reboot sequence. 
			if answer == "reboot":
				functions.countdown("USER INITIALIZED REBOOT","REBOOTING",4)
				functions.greeting(.09)
			if answer == "return":
				break
			
			else:
				print("response invalid.")
				continue
    
#End Menu Class. 


 


#Start Region Class. 
class Governing_Body():
	"""Class to store informaiton about a region"""
	
	def __init__(
		self,
		sectors = {},
		title = NULL,
		name = NULL,
		synopsis = NULL,
		history = NULL,
		):
			
			
		"""Initialises initializes object for region"""
		self.title = title.title()
		self.name = name.title()
		self.synopsis = synopsis
		self.sectors = sectors
		self.history = history
	

						
	def info(self):
		while True:
			"""method to print info about the region."""
			functions.clear_screen()
			functions.pyramid_logo()
			#prints information from object. 
			print(
				"=" * 80
				+"\nGalactic power: \n"
				+ self.title
				+ "\n" + "=" * 80
				+"\n\n SYNOPSIS: \n\n"
				+ self.synopsis 
				+ "\n\n HISTORY: \n\n"
				+ self.history 
				+"\n\n"
				)
			if self.sectors:
				selection_menu = functions.list_items(str(self.name + " sectors"),self.sectors.items())
				answer = input("Select Index number for more information: ")
				if answer in selection_menu:
					selection_menu.get(answer).info()
					
				elif answer in functions.exit_tuple:
					functions.countdown("\nSHUTTING DOWN APPLICATION.\n","",4)
					sys.exit("\nUSER TERMINATED APPLICATION.\n")
				#checks answer for reboot sequence. 
				
				elif answer == "reboot":
					functions.countdown("USER INITIALIZED REBOOT","REBOOTING",4)
					functions.greeting(.09)
				else:
					return answer
			else:
				print("=" * 80 + "\n" + "This OBJECT contain \"NULL VALUE\"" + "\n" + "=" * 80 + "\n")
				answer = input("enter RETURN to go back: ")
								
				if answer in functions.exit_tuple:
					functions.countdown("\nSHUTTING DOWN APPLICATION.\n","",4)
					sys.exit("\nUSER TERMINATED APPLICATION.\n")
				#checks answer for reboot sequence. 
				
				elif answer == "reboot":
					functions.countdown("USER INITIALIZED REBOOT","REBOOTING",4)
					functions.greeting(.09)
				else:
					return answer
				

    		

    
#eng region class



#Begin System Class
class System():
	
	def __init__(
		self,
		name,
		region = {},
		s_hex = "", 
		atmo = "",
		temp = "", 
		biosphere = "", 
		population = "", 
		tech_level = "",
		overview = {},
		more = {}
		):
			
			self.name = name
			self.region = region
			self.s_hex = s_hex
			self.atmo = atmo
			self.temp = temp
			self.biosphere = biosphere
			self.population = population
			self.tech_level = tech_level
			self.overview = overview
			self.more = more
			
	def print_overview(self,line_cap = 82):
		functions.clear_screen()
		functions.pyramid_logo()
		'''method to print dictionary containing overview information'''
		while True:
			functions.clear_screen()
			functions.pyramid_logo()
			print("=" * 82)
			print(self.name.title() + " Overview: ")
			print("=" * 82)			
			for k, v in self.overview.items():
				print(k + v)
			
			answer = input("\npress enter to return\n")
			return answer 
	
	
	def print_more(self,line_cap = 82):

		'''method to print dictionary containing more information'''
		while True:
			index = 0
			functions.clear_screen()
			functions.pyramid_logo()
			print("=" * 82)
			print(self.name.title() + " resources")
			print("=" * 82)
			print("*" * 82)			
			for k, v in self.more.items():
				
				print(k + v)
				input("\nENTER>>\n")
					
			answer = input("\npress enter to return\n")
			return answer
			
			
				
	
	def info(self,line_cap = 82):
		"""method to print statistics on planet."""
		name = str(" Name: " + self.name)
		region = str(" Region: " + self.region + " ")
		s_hex = str(" System Hex: " + self.s_hex + " ")
		atmo = str(" Atmosphere: " + self.atmo + " ")
		temp = str(" Temperature: " + self.temp + " ")
		biosphere = str(" Biosphere: " + self.biosphere + " ")
		population = str(" Population: " + self.population + " ")
		tech_level = str(" Tech Level: " + self.tech_level + " ")
		title_bar = ("=" * line_cap)
		while True:
			functions.clear_screen()
			functions.pyramid_logo()
			#creates title bar
			print(title_bar)
			print(name + " " * (line_cap - (len(name) + len(region))) + region) 
			print(title_bar + "\n")
		
		
			#format information for atmo and system Hex.
		
			print(
				" " 
				+ "*" * (len(atmo) + 2) 
				+ " " * (line_cap - (len(atmo) + len(s_hex) + 3)) 
				+ "*" * (len(s_hex) + 2)
				)
			
			print(
				" *" 
				+ atmo
				+ "*" 
				+ " " * (line_cap - (len(atmo) + 3
				+ len(s_hex))) 
				+ "*" 
				+ s_hex
				+ "*"
				)
				
		
			print(
				" "
				+ "*" * (len(atmo) + 2)
				+ " " * (line_cap - (len(atmo) + len(s_hex) + 3))
				+ "*" * (len(s_hex) + 2)
				)
		
			print("\n")
		
			#formats Temperature and Biosphere information.
			
			print(" " + "*" * (len(temp) + 2)
			+ " " * (line_cap - (len(temp) + len(biosphere) + 3))
			+ "*" * (len(biosphere) + 2)
			)
		
			print(
				" *" 
				+ temp 
				+ "*" 
				+ " " * (line_cap - (len(temp) + 3 + len(biosphere))) 
				+ "*" 
				+ biosphere
				+ "*"
				)
			
			print(
				" "
				+ "*" * (len(temp) + 2)
				+ " " * (line_cap - (len(temp) + len(biosphere) + 3))
				+ "*" * (len(biosphere) + 2)
				)
					
			print("\n")	
		
			#format populaiton and Tech_level
			print(
				" " 
				+ "*" * (len(population) + 2) 
				+ " " * (line_cap - (len(population) + len(tech_level) + 3)) 
				+ "*" * (len(tech_level) + 2)
				)
		
			print(
				" *" 
				+ population
				+ "*" 
				+ " " * (line_cap - (len(population) + 3 + len(tech_level))) 
				+ "*" 
				+ tech_level
				+ "*"
				)
			
		
			print(
				" "
				+ "*" * (len(population) + 2)
				+ " " * (line_cap - (len(population) + len(tech_level) + 3))
				+ "*" * (len(tech_level) + 2)
				)
			
			print("\n") 
			
			print(
				"=" * line_cap 
				+ "\n" 
				+ "Enter Overview for more detailed information if available.\nEnter More for a list of available resources."
				+ "\n"
				+ "=" * line_cap
				)
			
			answer = functions.prompt("\n: ")
				
			#check answer against the exit tuple and runs a shutdown sequence if true.
			if answer in functions.exit_tuple:
				functions.countdown("\nSHUTTING DOWN APPLICATION.\n","",4)
				sys.exit("\nUSER TERMINATED APPLICATION.\n")
			#checks answer for reboot sequence. 
			if answer == "reboot":
				functions.countdown("USER INITIALIZED REBOOT","REBOOTING",4)
				functions.greeting(.09)
			if answer == "overview":
				self.print_overview()
			if answer == "more":
				self.print_more()
			if answer == "return":
				break
				
			else:
				print("response invalid.")
				continue
    
    

    
    
#end of system class