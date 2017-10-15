from functions import *

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
			self.description = "No further information available. "
			self.overview = overview
			self.more = more
			
	def print_overview(self,line_cap = 82):
		'''method to print dictionary containing overview information'''
		while true:
			for k, v in self.overview.items():
				print(k + ": " + v)
			
			answer = functions.prompt("press enter to return")
			break

	
	
	def print_more(self,line_cap = 82):
		'''method to print dictionary containing more information'''
		while true:
			for k, v in self.more.items():
				print(k + ": " + v)
			
			answer = functions.prompt("press enter to return")
			break
			
			
				
	
	def info(self,line_cap = 82):
		functions.clear_screen()
		functions.pyramid_logo()
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
				+ self.description
				+ "\n"
				+ "=" * line_cap
				)
			
			answer = functions.prompt("Type in \"overview\" for a more Detailed overview of this system, type in \"more\" for further information.")
				
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
		tech_level = ""):
			
			self.name = name
			self.region = region
			self.s_hex = s_hex
			self.atmo = atmo
			self.temp = temp
			self.biosphere = biosphere
			self.population = population
			self.tech_level = tech_level
			self.description = "No further information available. "
			
	
	def info(self,line_cap = 90):
		functions.clear_screen()
		functions.pyramid_logo()
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
				+ self.description
				+ "\n"
				+ "=" * line_cap
				)
			
			answer = functions.prompt()
				
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
    		
#end of system class




