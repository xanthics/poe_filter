#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
from datetime import datetime
from os import path
from io import open

from auto_gen import divination
from auto_gen import hcdivination
from auto_gen import pdivination
from auto_gen import phcdivination
from auto_gen import uniques
from auto_gen import hcuniques
from auto_gen import puniques
from auto_gen import phcuniques
from auto_gen import currency as stcurrency
from auto_gen import hccurrency
from auto_gen import pcurrency
from auto_gen import phccurrency

from item_config import animate_weapon
from item_config import challenges
from item_config import chance
from item_config import chroma
from item_config import crafting_bases
from item_config import currency
from item_config import essences
from item_config import flask
from item_config import gems
from item_config import general_levelling
from item_config import hide
from item_config import labyrinth
from item_config import maps
from item_config import nonrare_armor_dex
from item_config import nonrare_armor_dex_int
from item_config import nonrare_armor_int
from item_config import nonrare_armor_str
from item_config import nonrare_armor_str_dex
from item_config import nonrare_armor_str_int
from item_config import nonrare_bow
from item_config import nonrare_claw
from item_config import nonrare_dagger
from item_config import nonrare_jewelry
from item_config import nonrare_one_hand_axe
from item_config import nonrare_one_hand_mace
from item_config import nonrare_one_hand_sword
from item_config import nonrare_sceptre
from item_config import nonrare_staff
from item_config import nonrare_thrusting_one_hand_sword
from item_config import nonrare_two_hand_axe
from item_config import nonrare_two_hand_mace
from item_config import nonrare_two_hand_sword
from item_config import nonrare_wand
from item_config import rare_armor_dex
from item_config import rare_armor_dex_int
from item_config import rare_armor_int
from item_config import rare_armor_str
from item_config import rare_armor_str_dex
from item_config import rare_armor_str_int
from item_config import rare_bow
from item_config import rare_claw
from item_config import rare_dagger
from item_config import rare_highlight
from item_config import rare_one_hand_axe
from item_config import rare_one_hand_mace
from item_config import rare_one_hand_sword
from item_config import rare_sceptre
from item_config import rare_staff
from item_config import rare_thrusting_one_hand_sword
from item_config import rare_two_hand_axe
from item_config import rare_two_hand_mace
from item_config import rare_two_hand_sword
from item_config import rare_wand
from item_config import rares
from item_config import recipe_item
from item_config import show
from item_config import t1_rares
from item_config import warbands

from theme_config import formatting


def gen_list(obj):
#	print("Starting {}".format(obj))
	b = ""

	# gen our string
	for i in sorted(obj.items):
		s = obj.items[i]
		if s['type'] != "ignore":
			b += "#{} - {}\n".format(i, obj.desc)
			if s['type'] == "hide":
				b += "Hide"
			else:
				b += "Show"
			if 'base' in s:
				b += "\n\tBaseType \"{}\"".format(s['base'])
			if 'class' in s:
				b += "\n\tClass \"{}\"".format(s['class'])
			if 'other' in s:
				b += "\n\t{}".format("\n\t".join(s['other']))
			if formatting.settings[s['type']]:
				b += "\n\t{}".format("\n\t".join(formatting.settings[s['type']]))
			else:
				print("Missing type field {} ** {}".format(obj, i))
			b += "\n\n"

	return b


# main function for creating a filter
def main():
	leagues = [("st", "Standard", uniques, divination, stcurrency),
			   ("hc", "Hardcore", hcuniques, hcdivination, hccurrency),
			   ("l", "Legacy", puniques, pdivination, pcurrency),
			   ("lhc", "Hardcore Legacy", phcuniques, phcdivination, phccurrency)]

	leveling = True  # toggle to show leveling items

	for i in leagues:

		buffer = """#**************************************************************
# Welcome to xan.filter, a Python generated loot filter for PoE
# This filter was generated for {} on {} UTC
# The most current version of code can always be found at https://github.com/xanthics/poe_filter
#**************************************************************

""".format(i[1], datetime.utcnow().strftime('%m/%d/%Y(m/d/y) %H:%M:%S'))

		buffer += gen_list(show)  # Always show these items
		buffer += gen_list(hide)  # Always hide these items
		if i[0] not in ['st', 'hc']:
			buffer += gen_list(challenges)
		buffer += gen_list(labyrinth)
		buffer += gen_list(i[4])  # Autogen currency values
		buffer += gen_list(essences)  # Essences
		buffer += gen_list(currency)  # Currency
		buffer += gen_list(gems)  # Gems
		buffer += gen_list(i[2])  # uniques
		buffer += gen_list(recipe_item)  # Items for vendor recipe
		buffer += gen_list(maps)  # maps
		buffer += gen_list(i[3])  # divination cards
		buffer += gen_list(flask)  # Flasks
		buffer += gen_list(t1_rares)
		if leveling:
			for rareitemleveling in [rare_armor_dex, rare_armor_dex_int, rare_armor_str_dex, rare_armor_str, rare_armor_int, rare_armor_str_int, rare_bow, rare_claw, rare_dagger, rare_one_hand_sword,
									 rare_one_hand_mace, rare_one_hand_axe, rare_sceptre, rare_staff, rare_thrusting_one_hand_sword, rare_two_hand_sword, rare_two_hand_mace, rare_two_hand_axe, rare_wand]:
				buffer += gen_list(rareitemleveling)

		buffer += gen_list(rare_highlight)  # rares highlighting + jewelry
		buffer += gen_list(rares)  # rares catchall
		buffer += gen_list(chroma)  # chrome vendor items
		if leveling:
			buffer += gen_list(general_levelling)
		buffer += gen_list(chance)  # Chance bases
		buffer += gen_list(crafting_bases)  # Crafting bases
		#buffer += gen_list(animate_weapon)  # Animate Weapon bases

		if leveling:
			for nonrareitemleveling in [nonrare_armor_dex, nonrare_armor_dex_int, nonrare_armor_str_dex, nonrare_armor_str, nonrare_armor_int, nonrare_armor_str_int, nonrare_bow, nonrare_claw, nonrare_dagger,
										nonrare_jewelry, nonrare_one_hand_sword, nonrare_one_hand_mace, nonrare_one_hand_axe, nonrare_sceptre, nonrare_staff,
										nonrare_thrusting_one_hand_sword, nonrare_two_hand_sword, nonrare_two_hand_mace, nonrare_two_hand_axe, nonrare_wand]:
				buffer += gen_list(nonrareitemleveling)

		buffer += gen_list(warbands)  # Warband base type highlighting

		print("Writing files to {}".format(path.expanduser("~\\my game\\Path of Exile\\")))

		with open("xan.{}.show.filter".format(i[0]), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Show\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
		with open(path.expanduser(r"~\Documents\my games\Path of Exile\xan.{}.show.filter".format(i[0])), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Show\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")

		with open("xan.{}.hide.filter".format(i[0]), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Hide\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")
		with open(path.expanduser(r"~\Documents\my games\Path of Exile\xan.{}.hide.filter".format(i[0])), "w", encoding='utf-8') as f:
			f.write(buffer)
			# Default for all other items
			f.write("Hide\n\tSetFontSize 18\n\tSetBackgroundColor 0 0 0 100\n\tSetBorderColor 100 100 100")


if __name__ == "__main__":
	main()
