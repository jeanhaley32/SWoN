import classes
import functions
#import systems
		



atmosphere = (
	"airless, or thin",
	"inert gas",
	"breathable Mix",
	"Thicke Breathable(mask)"
	)
	
temperature = (
	"cold",
	"termperate",
	"warm"
	)

biosphere = (
	"No Native Bioshpere",
	"Microbial Life",
	"human-miscibal",
	"immiscible Biosphere",
	)
	
population = (
	"Tens of Thousands",
	"Hundreds of Thousands",
	"Millions",
	"Billions")






#Begin of Anarchic Frontier Region Object. 
af_sector_list = {}

af_synopsis = functions.format_string(
"The Remote and Anarchic Sector Fronier:  \
or as it's known by the local population 'The Anarchic Frontier' \
is a loose cluster of governing bodies that, although each self-governing \
work together under the Common-Accord.")


af_history = functions.format_string(
"The Anarchic-Frontier began in the early days of space \
exploration, when large corporations and self funded entrepaneurs \
could invest in the building of large Frontier-Class Frigates to \
ferry union men out to the limits of the galaxy, in order to tame and \
exploit the plentiful resource of the as yet then untouch rim worlds. \
Over the years many of the corporations have moved away from \
what they precieve to be the limiting influence of their government and have \
taken their newly found and partly tamed frontier as their staging grounds.")
		

anarchic_frontier = classes.Governing_Body(
    af_sector_list,
    'The remote and anarchic sector frontier',
    af_synopsis,
    af_history
    )
    
#End of Anarchic Frontier Region Object.     



#Beginning of Condeferated Dominion of the stars.


#Start Sys Chauvin
chauvin = classes.System(
    "Chauvin",
    "confederated Dominion",
    "0406",
    atmosphere[2],
    temperature[2],
    biosphere[0],
    population[2],
    "3")
#End sys chauvin

#start sys vale

vale = classes.System(
	"vale",
	"Confederated Dominon",
	"0607",
	atmosphere[2],
	temperature[0],
	biosphere[1],
	population[1],
	"3"
	)
#end sys vale

#start sys kogami
kogami = classes.System(
	"kogami",
	"confederated Dominion",
	"0608",
	atmosphere[2],
	temperature[0],
	biosphere[0],
	population[1],
	"3"
	)
#end sys kogami

#start sys Sinai
sinai = classes.System(
	"sinai",
	"confederated Dominion",
	"0706",
	atmosphere[1],
	temperature[2],
	biosphere[2],
	population[2],
	"4"
	)
#end sys sinai

#start sys congaree
congaree = classes.System(
	"congaree",
	"confederated Dominion",
	"0707",
	atmosphere[2],
	temperature[1],
	biosphere[2],
	population[0],
	"4"
	)
#end sys kurzweil
kurzweil = classes.System(
	"klurzweil",
	"confederated Dominion",
	"0708",
	atmosphere[0],
	temperature[2],
	biosphere[3],
	population[1],
	"4"
	)
#end sys kurzweil

#start sys zio
zion = classes.System(
	"zion",
	"confederated Dominion",
	"0508",
	atmosphere[2],
	temperature[0],
	biosphere[0],
	population[1],
	"3"
	)
#end Sys zion



#sector list
confederated_domion_sector_list = {
	str("0406: " + chauvin.name) : chauvin,
	str("0607: " + vale.name) : vale,
	str("0608: " + kogami.name) : kogami,
	str("0706: " + sinai.name) : sinai,
	str("0707: " + congaree.name) : congaree,
	str("0708: " + kurzweil.name) : kurzweil,
	str("0508: " + zion.name) : zion
	}


confederated_dominion = classes.Governing_Body(
    confederated_domion_sector_list,
    "The Backward Confederated Dominion of Stars",
    "Confederated Dominion",
    classes.NULL,
    classes.NULL,
    )
    
#End of Confederated Dominion of the stars.







#begin stellar federation


#start sys Kenosha
kenosha = classes.System(
	"kenosha",
	"United Stellar Federation",
	"0006",
	atmosphere[2],
	temperature[0],
	biosphere[3],
	population[2],
	"3"
	)
#end sys kenosha

#start sys kahje
kahje = classes.System(
	"kahje",
	"United Stellar Federation",
	"0009",
	atmosphere[2],
	temperature[2],
	biosphere[2],
	population[2],
	"4"
	)
#end sys kahje

#start sys nibiru
nibiru = classes.System(
	"nibiru",
	"United Stellar Federation",
	"0106",
	atmosphere[2],
	temperature[1],
	biosphere[2],
	population[2],
	"4+(Some Pre)"
	)
#end sys nibiru

#start sys caelum
caelum = classes.System(
	"caelum",
	"United Stellar Federation",
	"0107",
	atmosphere[2],
	temperature[0],
	biosphere[2],
	population[1],
	"1"
	)
#end sys caelum

#start sys aldous
aldous = classes.System(
	"aldous",
	"United Stellar Federation",
	"0206",
	atmosphere[0],
	temperature[2],
	biosphere[0],
	population[1],
	"4"
	)
#end sys aldous

#start sys taranus
taranis = classes.System(
	"taranis",
	"United Stellar Federation",
	"0308",
	atmosphere[2],
	temperature[1],
	biosphere[0],
	population[2],
	"4"
	)
#end sys taranus

#start sys acadia

#acadia overview beginning. 
acadia_overview_object ="""

**************************************************************************************
*Population: 5,681,786,125                                                           *
*                                                                                    *
**************************************************************************************
*Climate: Urban Expanse universal. Cold upper atmosphere causing snowfall througout  *
*         Megalopolis on upper tower layers. Heat from energy sources in lower lev-  *
*         lead to rain and fog.                                                      *
*                                                                                    *
**************************************************************************************
*Capital Region: The Pentarchic Spires of the Old Town.                              *
*                                                                                    * 
**************************************************************************************
*Head of States: Prime Minister Aubert. He and his pary, predominantly consisting of *
*                upper-level corporate executives and members of the elite of Acadia *
*                , ran on a platform of economic equality and tolerange in the face  *
*                of recent hostilities toward his party's agenda.                    *
*                                                                                    *
**************************************************************************************
*Government: Parliamentary democracy consisting of elected officials from all megal- *
*            opolis districts and levels. All members of the central parliament rem- *
*            ains for terms of no more than eight years, and cannot run for Parliam- *
*            office again in their lifetime.                                         *
*                                                                                    *
**************************************************************************************


"""

acadia_overview = {
	"" : acadia_overview_object
	}
#acadia overview End.


#acadia more information

#formationg laws and policies
laws_and_policies = """
Sidhuri CLAIM Implant - CLAIM implants are mandatory for access to Acadia.
These implants are combination communications devices, identification chips, and
passports for all systems within the United Stellar Federation. If you have not been
provided yours, please contact the Bureau of Federation Security through SecNet
to receive yours.

Personal Firearms - Small arms are permitted universally on Acadia and
surrounding orbitals within the star system. Please note that concealed carry is
permitted in all cases. Open carry is punishable by a fine of no less than 500 CR
and no more than 1500 CR. Violation of small arms law will result in arrest and
litigation. All firearms owned by travelers must be registered with customs prior to
entry of atmosphere.

Personal Armor - Civilian-grade protective suits permitted universally on Acadia.
Military-grade armors and exosuits are expressly forbidden on Acadia due to both
security and aesthetic restrictions.

Drugs and Alcohol - No restrictions apply. Use responsibly. Intoxication is an 
aggravating charge if found to have been related or causal in other legal infractions.

Prostitution and Gambling - Permitted only if you have registered with the
respective bureaus. Illegal prostitution and gambling are strictly forbidden. Legal
restrictions are in place to protect all parties involved in these operations.

"""

#formationg laws and politics
	
#creating and formation fashions and culture
fashions_and_culture = """
Acadia is home to many ancient customs and traditions. The elegance and
propriety of the founders has been passed on for generations, and has become a 
core symbol of the Elegant Star of Stars that the USF strives to be for all people of 
the sector. Fashions center widely around what was known in ancient history as
"The Roaring Twenties" of Earth-That-Once-Was. The art and clothing of this
sophisticated era has followed a culture that celebrates life and good company,
making Acadia a central destination for relaxation, recreational intoxication, and
fun. Above all else, our musicians have taken ancient musics of this era and given
them a modern flair that will leave your foot tapping and your heart pumping. Join
us in celebration!

"""

#finished formation fasions and culture. 


#creating and formation key attractions.
key_attractions = """
The Pentarchic Spires - These five old towers have been the core of sector
politics since the early days of the founders. Still standing, gilt in the sparkling gold
filigree of the Golden Age before the Scream, these towers are a testament to the
enduring unity of the USF.

The Sidhuri Collective Systems Golden Monolith - Acadia is home to the
Software and Computing powerhouse that is Sidhuri Collective Systems, makers of
the USF's CLAIM system. This elegant structure can be found within view of the
Pentarchic Spires of the Old Town, and is a testament to its creator's vision of
lending aid to making the USF a beacon of light to all who can see its splendor.

"""

#finished creating and formation key attracitons. 

#creating and formating job listings  

job_listings = """
All contracts are handled through core SecNet listings. For more information,
connect to core SecNet register using your unique CLAIM identifier. Please submit
all complaints to the Bureau of Labor Management using form 15683-12C. 

"""

acadia_more = {
	"Laws and Policies:\n" : laws_and_policies,
	"Fashions and Culture:\n" : fashions_and_culture,
	"Key Attractions:\n" : key_attractions,
	"job listings:\n" : job_listings
}


acadia = classes.System(
	"acadia",
	"United Stellar Federation",
	"0104",
	atmosphere[3],
	temperature[0],
	biosphere[0],
	population[1],
	"4",
	acadia_overview,
	acadia_more
	)
#end sys Acadia



stellar_federation_sector_list = {
	str("0006: " + kenosha.name) : kenosha,
	str("0009: " + kahje.name) : kahje,
	str("0106: " + nibiru.name) : nibiru,
	str("0107: " + caelum.name) : caelum,
	str("0206: " + aldous.name) : aldous,
	str("0308: " + taranis.name) : taranis,
	str("0104: " + acadia.name) : acadia
}


stellar_federation = classes.Governing_Body(
    stellar_federation_sector_list,
    "United Stellar Federation",
    "Stellar Federation"
    )

#end stellar federation





#Start of Independent Frontier of Stars. 

#start sys valdosta
valdosta = classes.System(
	"valdosta",
	"Independent Frontier Stars",
	"0000",
	atmosphere[2],
	temperature[2],
	biosphere[0],
	population[1],
	"3"
	)
#end sys valdosta

#start sys holtx
holtz = classes.System(
	"holtz",
	"Independent Frontier Stars",
	"0001",
	atmosphere[3],
	temperature[1],
	biosphere[2],
	population[2],
	"4"
	)
#end sys holtz

#start sys acoma
acoma = classes.System(
	"acoma",
	"Independent Frontier Stars",
	"0102",
	atmosphere[2],
	temperature[1],
	biosphere[2],
	population[1],
	"4"
	)

#start sys ayahos
ayahos = classes.System(
	"ayahos",
	"Independent Frontier Stars",
	"0102",
	atmosphere[2],
	temperature[1],
	biosphere[2],
	population[1],
	"4"
	)
#end sys ayahos

#start sys ziriaba
ziriaba = classes.System(
	"ziriaba",
	"Independent Frontier Stars",
	"0503",
	atmosphere[2],
	temperature[1],
	biosphere[2],
	population[2],
	"4"
	)
#end sys ziriaba

#start sys azalis
azalis = classes.System(
	"azalis",
	"Independent Frontier Stars",
	"0604",
	atmosphere[1],
	temperature[1],
	biosphere[0],
	population[0],
	"3"
	)
#end sys azalis

#start sys trementina
trementina = classes.System(
	"trementina",
	"Independent Frontier Stars",
	"0702",
	atmosphere[2],
	temperature[1],
	biosphere[2],
	population[3],
	"4"
	)
#end sys trementia

#start sys zamyatin
zamyatin = classes.System(
	"zamyatin",
	"Independent Frontier Stars",
	"0301",
	atmosphere[2],
	temperature[0],
	biosphere[2],
	population[2],
	"5"
	)
#end sys zamyatin


#end planets/systems


independent_frontier_sector_list = {
	str("0000: " + valdosta.name) : valdosta,
	str("0001: " + holtz.name) : holtz,
	str("0102: " + acoma.name) : acoma,
	str("0500: " + ayahos.name): ayahos,
	str("0503: " + ziriaba.name) : ziriaba,
	str("0604: " + azalis.name) : azalis,
	str("0702: " + trementina.name) : trementina,
	str("0301: " + zamyatin.name) : zamyatin
	}


independent_frontier = classes.Governing_Body(
    independent_frontier_sector_list,
    "independent frontier of stars",
    "independent frontier"
    )


#End of Independent Frontier of Stars. 


#Start of locations menu. 

#Dictionary of Regions. 
unknown_regions_list = {
    "anarchic frontier" : anarchic_frontier
    }
unknown_regions = classes.Menu("Unknown Regions", unknown_regions_list.items())

#End of Locations Menu.



#being Occidens Indus Alpha

occidens_indus_alpha_list = {
    "Confederated Dominion of stars" : confederated_dominion,  
    "Independent Frontier stars" : independent_frontier,
    "United Stellar Federation" : stellar_federation
    }
occidens_indus_alpha = classes.Menu("Regional Powers", occidens_indus_alpha_list.items())

#end Occidens Indus Alpha




#beginning sectors_list

government_list = {
    "unknown regions" : unknown_regions,
    "Occidens Indus Alpha" : occidens_indus_alpha
    }

governments = classes.Menu("SECTOR", government_list.items())