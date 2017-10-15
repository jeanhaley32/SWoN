import classes
import regions








#start planets/systems

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


#Start Sys Chauvin
chauvin = classes.System(
    "Chauvin",
    {"confederated Dominion": regions.confederated_dominion},
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
	{"Confederated Dominon" : regions.confederated_dominion},
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
	{"confederated Dominion" : regions.confederated_dominion},
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
	{"confederated Dominion" : regions.confederated_dominion},
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
	{"confederated Dominion" : regions.confederated_dominion},
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
	{"confederated Dominion" : regions.confederated_dominion},
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
	{"confederated Dominion" : regions.confederated_dominion},
	"0508",
	atmosphere[2],
	temperature[0],
	biosphere[0],
	population[1],
	"3"
	)
#end Sys zion

#start sys valdosta
valdosta = classes.System(
	"valdosta",
	{"Independent Frontier Stars" : regions.independent_frontier},
	"0000",
	atmosphere[2],
	temperature[3],
	biosphere[0],
	population[1],
	"3"
	)
#end sys valdosta

#start sys holtx
holtz = classes.System(
	"holtz",
	{"Independent Frontier Stars" : regions.independent_frontier},
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
	{"Independent Frontier Stars" : regions.independent_frontier},
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
	{"Independent Frontier Stars" : regions.independent_frontier},
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
	{"Independent Frontier Stars" : regions.independent_frontier},
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
	{"Independent Frontier Stars" : regions.independent_frontier},
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
	{"Independent Frontier Stars" : regions.independent_frontier},
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
	{"Independent Frontier Stars" : regions.independent_frontier},
	"0301",
	atmosphere[2],
	temperature[0],
	biosphere[2],
	population[2],
	"5"
	)
#end sys zamyatin

#start sys Kenosha
kenosha = classes.System(
	"kenosha",
	{"United Stellar Federation" : regions.stellar_federation},
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
	{"United Stellar Federation" : regions.stellar_federation},
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
	{"United Stellar Federation" : regions.stellar_federation},
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
	{"United Stellar Federation" : regions.stellar_federation},
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
	{"United Stellar Federation" : regions.stellar_federation},
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
	{"United Stellar Federation" : regions.stellar_federation},
	"0308",
	atmosphere[2],
	temperature[1],
	biosphere[0],
	population[2],
	"4"
	)
#end sys taranus

#start sys acadia
acadia = classes.System(
	"acadia",
	{"United Stellar Federation" : regions.stellar_federation},
	"0104",
	atmosphere[3],
	temperature[0],
	biosphere[0],
	population[1],
	"4"
	)

#end planets/systems






#sector list
confederated_domion_sector_list = {
	"0406" : chauvin,
	"0607" : vale,
	"0608" : kogami,
	"0706" : sinai,
	"0707" : congaree,
	"0708" : kurzweil,
	"0508" : zion
	}

independent_frontier_sector_list = {
	"0000" : valdosta,
	"0001" : holtz,
	"0102" : acoma,
	"0500" : ayahos,
	"0503" : ziriaba,
	"0604" : azalis,
	"0702" : trementina,
	"0301" : zamyatin
}


stellar_federation_sector_list = {
	"0006" : kenosha,
	"0009" : kahje,
	"0106" : nibiru,
	"0107" : caelum,
	"0206" : aldous,
	"0308" : taranis,
	"0104" : acadia
}

#end sector list