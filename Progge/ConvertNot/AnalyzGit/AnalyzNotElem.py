# listes pour la recherche du programme de conversion de notes

PAP = 'Les mots particuliers et les accords plus étendus sont disponibles sur demande aux soins de https://www.scoreexchange.com/scores/189858.html'
#en_harmonique = {'do': 'si&sharp', 'do&sharp': 'r&eacute&flat', 'r&eacute&flat': 'do&sharp','r&eacute&sharp': 'mi&flat', 'mi&flat': 'r&eacute&sharp',
#	'mi' : 'fa&flat', 'fa&flat': 'mi', 'fa': 'mi&sharp', 'mi&sharp': 'fa', 'fa&sharp': 'sol&flat', 'sol&flat': 'fa&sharp',
#	'sol&sharp': 'la&flat', 'la&flat': 'sol&sharp', 'la&sharp': 'si&flat', 'si&flat': 'la&sharp', 'si' : 'do&flat'} #revoir key/result ou remplacer par en_harmoniq_plus
#&& 'ré': 'mi&#119083', 'ré': 'do&#119082'
en_harmoniq_plusAndNum = {'do': 'ré&#119083', 'do&sharp': 'ré&flat', 'do&#119082': 'r?eacute', 'r&eacute': 'mi&#119083', 'ré&sharp': 'mi&flat', 'ré&#119082': 'mi',
	'mi': 'fa&flat', 'mi&harp': 'fa', 'mi&#119082': 'fa&#119082', 'fa': 'sol&#119083', 'fa#': 'sol&flat', 'fa&#119082': 'sol', 'sol': 'la&#119083',
	'sol#': 'lab', 'solx':'la','la': 'sibb','la#': 'sib','lax':'si', 'si' : 'dob', 'si#':'do', 'six':'do#'}
#à revérifier
en_harmoniq_plus = {'dob': 'si', 'do': 'rébb', 'do dièze': 'réb', 'do double dièze': 'ré',
	'réb': 'do dièze', 'ré': 'mibb', 'ré dièze': 'mib', 'ré double dièze': 'mi',
	'mib': 'ré dièze', 'mi': 'fab', 'mi dièze': 'fa', 'mi double dièze': 'fa dièze',
	'fab': 'mi', 'fa': 'solbb', 'fa dièze': 'solb', 'fa double dièze': 'sol',
	'solb': 'fa dièze', 'sol': 'labb', 'sol dièze': 'lab', 'sol double dièze': 'la',
	'lab': 'sol dièze','la': 'sibb', 'la dièze': 'sib', 'la double dièze': 'si',
	'sib' : 'la dièze', 'si': 'dob', 'si dièze': 'do', 'si double dièze': 'do dièze'}

nottAndNum = ["do", "r&eacute&flat", "r&eacute", "mi&flat", "mi", "fa", "sol&flat", "sol", "la&flat", "la", "si&flat", "si"]
nott = ["do", "réb", "ré", "mib", "mi", "fa", "solb", "sol", "lab", "la", "sib", "si"]
not_t = nott + nott

not_diatoniqAndNum = ['do', 'r&aecute', 'mi', 'fa', 'sol', 'la', 'si']
not_diatoniq = ['do', 'ré', 'mi', 'fa', 'sol', 'la', 'si']
not_diat_t = not_diatoniq + not_diatoniq

nom_in_tervalle = ["unisson ou octave", "seconde mineure", "seconde majeure",
               "tierce mineure", "tierce majeure", "quarte juste",
               "quinte diminuée", "quinte juste", "sixte mineure",
                "sixte majeure", "septi&egraveme mineure", "septi&egraveme majeure" ]
n_in_tervalle = nom_in_tervalle + nom_in_tervalle
intervall_diat = ["unisson ou octave", "seconde", "tierce", "quarte", "quinte", "sixte", "septi&egraveme"]

note_reg = (r'^[dflmrs][aeéio]l?b?$')	#&ecute ?
list_accor = ('accor_trois_sons_dim', 'accor_trois_sons_min', 'accor_trois_sons_maj',
	'accor_trois_sons_augm',  'accor_quatre_sons_septieme_dim', 'accor_quatre_sons_septieme_min',
	'accor_quatre_sons_septieme_min', 'accor_quatre_sons_septieme_domin',
	'accor_quatre_sons_septieme_maj', 'accor_quatre_sons_quinte_augm_septieme_maj' )
gammaj = [0, 2, 4, 5, 7, 9, 11 ]
gamminh = [0, 2, 3, 5, 7, 8, 11]
gamminnat = [0, 2, 3, 5, 7, 8, 10]
gamminmelasc = [0, 2, 3, 5, 7, 9, 11]
accor_trois_sons_dim = [0, 3, 6]
accor_trois_sons_min = [0, 3, 7]
accor_trois_sons_maj = [0, 4, 7]
accor_trois_sons_augm = [0, 4, 8]
accor_quatre_sons_septieme_dim = [0, 3, 6, 9]
#ajouter # accor_quatre_sons_septieme_min_quinte_diminuee = [0, 3, 6, 10]
accor_quatre_sons_septieme_min = [0, 3, 7, 10]
accor_quatre_sons_septieme_domin = [0, 4, 7, 10]
accor_quatre_sons_septieme_maj = [0, 4, 7, 11]
accor_quatre_sons_quinte_augm_septieme_maj = [0, 4, 8, 11]
# et compléter selon recherches

#gam_sept_sons = {'gamme majeure' : [0, 2, 4, 5, 7, 9, 11 ], 'gamme mineure harmonique' : [0, 2, 3, 5, 7, 8, 11], 'gamme mineure naturelle' : [0, 2, 3, 5, 7, 8, 10], 'gamme mineure mélodique ascendante' : [0, 2, 3, 5, 7, 9, 11]}
#accor_trois_sons = {'dim': [0, 3, 6], 'min': [0, 3, 7], 'maj': [0, 4, 7],  'augm': [0, 4, 8]}
#accor_quatre_sons = {'septieme_dim': [0, 3, 6, 9],'septieme_min': [0, 3, 10], 'septieme_domin': [0, 4, 7, 10], 'septieme_maj': [0, 4, 7, 11], 'quinte_augm_septieme_maj': [0, 4, 8, 11]}

#&&
##nom_in_terv_diat = ["unisson ou octave", "seconde", "tierce", "quarte", "quinte", "sixte", "septième"]
#nottes = "do, ré bémol, ré, mi bémol, mi, fa, sol bémol, sol la bémol, la, si bémol, si"
