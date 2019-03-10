#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Magic items"

# Base type : settings pair
items = {
	"0 magic item": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "Rarity Magic", "SetBorderColor 208 32 144", "Identified True"], "type": "hide"},
}


# TODO: expand this section for better creation of mods/bases to look at
# "Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"
# , "Body Armour", "Boots", "Gloves", "Helmet", "Shield"
# , "Amulet", "Belt", "Ring"
# , "Jewel", "Abyss Jewel"
def itemmods():
	modtoitem = {'Entombing': ["Claw", "Dagger", "Sceptre", "Wand"],
				 'Cremating': ["Claw", "Dagger", "Sceptre", "Wand"],
				 'Electrocuting': ["Claw", "Dagger", "Sceptre", "Wand"],
				 'Malicious': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Dictator\'s': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Merciless': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 'Flaring': ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword", "Amulet"],
				 'Tul\'s': ["Sceptre", "Wand", "Stave"],
				 'Xoph\'s': ["Sceptre", "Wand", "Stave"],
				 'Esh\'s': ["Sceptre", "Wand", "Stave"],
				 'Runic': ["Sceptre", "Wand", "Stave"],
				 'of Unmaking': ["Sceptre", "Wand", "Stave"],

				 'Prime': ["Body Armour"],
				 'Athlete\'s': ["Boots", "Gloves", "Amulet"],
				 'Fecund': ["Helmet", "Belt"],
				 'Vigorous': ["Shield"],
				 'Virile': ["Ring"],
				 'of Bameth': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
				 'of Haast': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
				 'of Tzteosh': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
				 'of Ephij': ["Body Armour", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Belt", "Ring"],
				 'Hellion\'s': ["Boots"],
				 'Cheetah\'s': ["Boots"],
				 'Dragon\'s': ["Helmet"],
				 'of Excavation': ["Helmet", "Amulet", "Ring"],
				 'of the Span': ["Shield", "Amulet"],
				 'of the Rainbow': ["Shield", "Amulet"],
				 'Devastating': ["Amulet", "Belt"],
				 'Perandus\'': ["Amulet", "Ring"],
				 'of Expertise': ["Amulet"],
				 'of the Assassin': ["Amulet"],
				 'of the Infinite': ["Amulet"],
				 'of the Multiverse': ["Amulet"],
				 'of Overflowing': ["Belt"],
				 'of Sipping': ["Belt"],
				 'of Savouring': ["Belt"],
				 'of the Godslayer': ['Belt'],
				 'of Talent': ["Ring"],
				 'of Skill': ["Ring"],
				 'Flawless': ["Ring"],

				# Veiled mods so they can be eventually disabled when unlocked
				 "Veiled": [
					 "Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword",
					 "Wand",
					 "Bow",
					 "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword",
					 "Shield",
					 "Body Armour",
					 "Boots",
					 "Gloves",
					 "Helmet",
					 "Shield",
					 "Amulet",
					 "Belt",
					 "Ring"
				 ],
				 "Leo's Veiled": ["Ring", "Belt"],
				 "Catarina's Veiled": ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword", "Shield"],
				 "Elreon's Veiled": ["Amulet", "Ring"],
				 "Vorici's Veiled": ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 "Haku's Veiled": ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword", "Shield"],
				 "Tora's Veiled": ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword"],
				 "Vagan's Veiled": ["Gloves", "Amulet"],
				 "Guff's Veiled": ["Gloves"],
				 "It That Fled's Veiled": ["Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword", "Wand", "Bow", "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword", "Shield"],
				 "Gravicius' Veiled": ["Body Armour"],
				 "Korell's Veiled": ["Helmet"],
				 "Rin's Veiled": ["Boots"],

				 "of the Veil": [
					 "Claw", "Dagger", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Sceptre", "Thrusting One Hand Sword",
					 "Wand",
					 "Bow",
					 "Stave", "Two Hand Axe", "Two Hand Mace", "Two Hand Sword",
					 "Shield",
					 "Body Armour",
					 "Boots",
					 "Gloves",
					 "Helmet",
					 "Shield",
					 "Amulet",
					 "Belt",
					 "Ring"
				 ],
				 "of Janus' Veil": ["Helmet"],
				 "of Hillock's Veil": ["Body Armour"],
				 "of Jorgin's Veil": ["Amulet"],
				 "of Cameria's Veil": ["Ring"],
				 "of Aisling's Veil": ["Ring"],
				 "of Riker's Veil": ["Ring"],
				 }

	modanyitem = ['Eldritch', "The Shaper's", 'of the Elder', 'of Shaping',
				  "Subterranean", "of the Underground", "of Weaponcraft", "of Spellcraft", "of Crafting",
				  "Citaqualotl's", "Guatelitzi's", "Matatl's", "of Puhuarte", "of Tacati", "Tacati's", "Topotante's", "Xopec's",
				  "Brinerot", "Mutewind", "Redblade", "Betrayer\'s", "Deceiver\'s", "Turncoat\'s",
				  "of Farrul", "of Craiceann", "of Fenumus", "of Saqawal",
				 ]

	ret = {'0 Item Mod': {'other': ['HasExplicitMod "{}"'.format('" "'.join(modanyitem))], "type": "item mod"}}

	for mod in modtoitem:
		for item in modtoitem[mod]:
			keyval = "1 {}".format(item)
			if keyval in ret:
				ret[keyval]['other'][0] += ' "{}"'.format(mod)
			else:
				ret[keyval] = {"type": "item mod"}
				ret[keyval]['class'] = item
				ret[keyval]['other'] = ['HasExplicitMod "{}"'.format(mod)]


	return ret

if __name__ == '__main__':
	rets = itemmods()
	for i in rets:
		print(i, rets[i])