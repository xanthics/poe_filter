#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "formatting template for all files"

# Color values from http://pathofexile.gamepedia.com/Item_filter_guide
color = {
	"normal": "200 200 200",
	"magic": "136 136 255",
	"rare": "255 255 119",
	"unique": "175 96 37",
	"gem": "27 162 155",
	"currency": "170 158 130",
	"quest": "74 230 58",
	"divinationold": "170 230 230",
	"default": "127 127 127",
	"value": "255 255 255",
	"augmented": "136 136 255",
	"fire": "150 0 0",
	"cold": "54 100 146",
	"lightning": "255 215 0",
	"chaos": "208 32 144",
	"crafted": "184 218 242",
	"corrupted": "210 0 0",
	"supportpacknew": "180 96 0",
	"supporterpack": "163 141 109",
	"nemesis": "255 200 0",
	"nemesisoutline": "255 40 0",
	"bloodline": "210 0 220",
	"bloodlineoutline": "74 0 160",
	"torment": "50 230 100",
	"tormentoutline": "0 100 150",
	"title": "231 180 120",
	"favour": "170 158 120",
	"lpink": "255 192 203",
	"divinationnew": "30 144 255",
	"premiumbrown": "124 81 50",
	"premiumorange": "191 91 0",
	"premiumtan": "254 191 128",
	"premiumdpurple": "38 0 86",
	"premiumpurple": "88 0 179",
	"premiumlpurple": "192 128 254",
	"premiumdlime": "98 128 0",
	"premiumlime": "191 244 0",
	"premiumllime": "239 254 128",
	"premiumdred": "86 0 0",
	"premiumred": "191 0 0",
	"premiumlred": "254 128 128",
	"premiumdblue": "0 0 128",
	"premiumblue": "0 0 254",
	"premiumlblue": "128 179 254",
	"premiumdyellow": "254 170 0",
	"premiumyellow": "254 213 0",
	"premiumlyellow": "254 254 153",
	"premiumdlavender": "114 0 83",
	"premiumlavender": "204 0 154",
	"premiumllavender": "254 128 222",
	"premiumdgreen": "0 73 0",
	"premiumgreen": "0 191 0",
	"premiumlgreen": "128 254 128",
	"premiumdgrey": "42 42 42",
	"premiumgrey": "135 135 135",
	"premiumlgrey": "221 221 221",
	"black": "0 0 0",
	"prophecy": "128 0 200",
	"highlight": "51 58 75"
}

size = {
	"huge": "45",
	"vlarge": "44",
	"large": "39",
	"normal": "32",
	"small": "25",
	"minimum": "18",
}

# Volumes are controlled in wav_mixer
# mirror
# max
# high
# normal
# medium
# low

# initialize settings with all of the text color options
settings = {f"{k} text": [f"SetTextColor {color[k]}", "Continue"] for k in color}

# Text settings for various categories
# This is where you would define general settings for a category, such as PlayAlertSoundPositional.
# Each config should be its own array element.  Parsing will handle tabs/etc.
# ignore and hide have special meaning(see comment)
settings.update({
	# Special sound for anything worth at least 1/20th of a mirror
	"challenge mirror": ["SetBorderColor {}".format(color['currency']),
						 'MinimapIcon 0 Yellow UpsideDownHouse',
						 'PlayEffect Yellow',
						 "SetFontSize {}".format(size['huge']),
						 'CustomAlertSound "{}_challenge"'.format("mirror"),
						 "SetBackgroundColor {} 220".format(color['highlight'])],

	"challenge extremely high": ["SetBorderColor {}".format(color['premiumdlavender']),
								 'CustomAlertSound "{}_challenge"'.format('max'),
								 'MinimapIcon 0 Green Kite',
								 'PlayEffect Green',
								 "SetFontSize {}".format(size['huge']),
								 "SetBackgroundColor {} 220".format(color['highlight'])],
	"challenge very high": ["SetBorderColor {}".format(color['premiumdlavender']),
							'CustomAlertSound "{}_challenge"'.format('high'),
							'MinimapIcon 1 Blue Kite',
							'PlayEffect Green',
							"SetFontSize {}".format(size['vlarge']),
							"SetBackgroundColor {} 220".format(color['black'])],
	"challenge high": ["SetBorderColor {}".format(color['premiumdlavender']),
					   'CustomAlertSound "{}_challenge"'.format('normal'),
					   'MinimapIcon 1 Blue Kite',
					   "SetFontSize {}".format(size['large']),
					   "SetBackgroundColor {} 220".format(color['black'])],
	"challenge normal": ["SetBorderColor {}".format(color['premiumdlavender']),
						 'CustomAlertSound "{}_challenge"'.format('low'),
						 'MinimapIcon 2 Blue Kite',
						 "SetFontSize {}".format(size['normal']),
						 "SetBackgroundColor {} 220".format(color['black'])],
	"challenge show": ["SetBorderColor {} 150".format(color['premiumdlavender']),
					   'MinimapIcon 2 Blue Kite',
					   "SetFontSize {}".format(size['normal']),
					   "SetBackgroundColor {} 220".format(color['black'])],
	"challenge low": ['MinimapIcon 2 Blue Kite',
					  "SetFontSize {}".format(size['normal']),
					  "SetBackgroundColor {} 220".format(color['black'])],

	"animate melee b": ["SetFontSize {}".format(size['minimum']),
						"SetTextColor {}".format(color['premiumlred']),
						"SetBorderColor {} 150".format(color['premiumlred']),
						"SetBackgroundColor {} 0".format(color['black'])],
	"animate melee": ["SetFontSize {}".format(size['minimum']),
					  "SetTextColor {} 150".format(color['premiumlred']),
					  "SetBackgroundColor {} 0".format(color['black'])],
	"animate range b": ["SetFontSize {}".format(size['small']),
						"SetTextColor {}".format(color['premiumlred']),
						"SetBorderColor {} 200".format(color['premiumtan']),
						"SetBackgroundColor {} 150".format(color['premiumbrown'])],
	"animate range": ["SetFontSize {}".format(size['small']),
					  "SetTextColor {}".format(color['black']),
					  "SetBackgroundColor {} 150".format(color['premiumbrown'])],

	"quest": ["SetFontSize {}".format(size['normal']),
			  'MinimapIcon 2 Green Moon',
			  'PlayEffect Green',
			  "SetBorderColor {} 200".format(color['quest']),
			  "SetBackgroundColor {} 220".format(color['black'])],

	"chance": ["Rarity Normal",
	           'Corrupted False',
			   'Mirrored False',
			   "SetFontSize {}".format(size['large']),
			   "SetBorderColor {} 150".format(color['premiumorange']),
			   "SetBackgroundColor {} 220".format(color['premiumdpurple'])],

	"chance any": ['Corrupted False',
				   'Mirrored False',
				   "SetFontSize {}".format(size['large']),
				   "SetBorderColor {} 150".format(color['premiumorange']),
				   "SetBackgroundColor {} 220".format(color['premiumdpurple'])],

	# Special sound for anything worth at least 1/20th of a mirror
	"currency mirror": ["SetBorderColor {}".format(color['currency']),
			   'MinimapIcon 0 Yellow UpsideDownHouse',
			   'PlayEffect Yellow',
			   "SetFontSize {}".format(size['huge']),
			   'CustomAlertSound "{}_currency"'.format("mirror"),
			   "SetBackgroundColor {} 220".format(color['highlight'])],

	"currency extremely high": ["SetBorderColor {}".format(color['currency']),
								'MinimapIcon 0 Green Pentagon',
								'PlayEffect Green',
								"SetFontSize {}".format(size['huge']),
								'CustomAlertSound "{}_currency"'.format('max'),
								"SetBackgroundColor {} 220".format(color['highlight'])],
	"currency very high": ["SetBorderColor {}".format(color['currency']),
						   'MinimapIcon 1 Blue Pentagon',
						   'PlayEffect Blue',
						   "SetFontSize {}".format(size['vlarge']),
						   'CustomAlertSound "{}_currency"'.format('high'),
						   "SetBackgroundColor {} 220".format(color['black'])],
	"currency high": ["SetBorderColor {}".format(color['currency']),
					  'MinimapIcon 1 Blue Pentagon',
					  "SetFontSize {}".format(size['large']),
					  'CustomAlertSound "{}_currency"'.format('normal'),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"currency normal": ["SetBorderColor {}".format(color['currency']),
						'MinimapIcon 2 Brown Pentagon',
						"SetFontSize {}".format(size['normal']),
						'CustomAlertSound "{}_currency"'.format('low'),
						"SetBackgroundColor {} 220".format(color['black'])],
	"currency low": ["SetFontSize {}".format(size['small']),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"currency show": ["SetBorderColor {} 150".format(color['currency']),
					  'MinimapIcon 2 Grey Pentagon',
					  "SetFontSize {}".format(size['normal']),
					 "SetBackgroundColor {} 220".format(color['black'])],

	# Special sound for anything worth at least 1/20th of a mirror
	"divination mirror": ["SetBorderColor {}".format(color['divinationnew']),
						  'MinimapIcon 0 Yellow UpsideDownHouse',
						  'PlayEffect Yellow',
						  "SetFontSize {}".format(size['huge']),
						  'CustomAlertSound "{}_divination"'.format("mirror"),
						  "SetBackgroundColor {} 220".format(color['highlight'])],
	"divination extremely high": ["SetBorderColor {}".format(color['divinationnew']),
								  'MinimapIcon 0 Green Triangle',
								  'PlayEffect Green',
								  "SetFontSize {}".format(size['huge']),
								  'CustomAlertSound "{}_divination"'.format('max'),
								  "SetBackgroundColor {} 220".format(color['highlight'])],
	"divination very high": ["SetBorderColor {}".format(color['divinationnew']),
							 'MinimapIcon 1 Blue Triangle',
							 'PlayEffect Blue',
							 "SetFontSize {}".format(size['vlarge']),
							 'CustomAlertSound "{}_divination"'.format('high'),
							 "SetBackgroundColor {} 220".format(color['black'])],
	"divination high": ["SetBorderColor {}".format(color['divinationnew']),
						'MinimapIcon 1 Blue Triangle',
						'CustomAlertSound "{}_divination"'.format('normal'),
						"SetBackgroundColor {} 220".format(color['black']),
						"SetFontSize {}".format(size['normal'])],
	"divination normal": ['MinimapIcon 2 Red Triangle',
						  'CustomAlertSound "{}_divination"'.format('low'),
						  "SetBackgroundColor {} 220".format(color['black']),
						  "SetFontSize {}".format(size['normal'])],
	"divination show": ["SetBackgroundColor {} 220".format(color['black']),
						'MinimapIcon 2 Grey Triangle',
						"SetFontSize {}".format(size['normal'])],
	"divination low": ["SetBackgroundColor {} 220".format(color['black']),
					   "SetFontSize {}".format(size['small'])],

	# Special sound for anything worth at least 1/20th of a mirror
	"gem mirror": ["SetBorderColor {}".format(color['gem']),
				   'MinimapIcon 0 Yellow UpsideDownHouse',
				   'PlayEffect Yellow',
				   "SetFontSize {}".format(size['huge']),
				   'CustomAlertSound "{}_gem"'.format("mirror"),
				   "SetBackgroundColor {} 220".format(color['highlight'])],
	"gem extremely high": ["SetBorderColor {}".format(color['gem']),
						   'MinimapIcon 1 Green Hexagon',
						   'PlayEffect Green',
						   'CustomAlertSound "{}_gem"'.format('max'),
						   "SetFontSize {}".format(size['huge']),
						   "SetBackgroundColor {} 220".format(color['highlight'])],
	"gem very high": ["SetBorderColor {}".format(color['gem']),
					  'PlayEffect Blue',
					  'MinimapIcon 1 Blue Hexagon',
					  'CustomAlertSound "{}_gem"'.format('high'),
					  "SetFontSize {}".format(size['vlarge']),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"gem high": ["SetBorderColor {}".format(color['gem']),
				 'MinimapIcon 2 Blue Hexagon',
				 'CustomAlertSound "{}_gem"'.format('normal'),
				 "SetFontSize {}".format(size['normal']),
				 "SetBackgroundColor {} 220".format(color['black'])],
	"gem normal": ["SetBorderColor {} 220".format(color['gem']),
				   'MinimapIcon 2 Brown Hexagon',
				   "SetBackgroundColor {} 220".format(color['black']),
				   "SetFontSize {}".format(size['normal'])],
	"gem low": ["SetFontSize {}".format(size['small']),
				"SetBackgroundColor {} 220".format(color['black'])],

	# Special sound for anything worth at least 1/20th of a mirror
	"fragment mirror": ["SetBorderColor {}".format(color['premiumllavender']),
						"SetTextColor {}".format(color['premiumllavender']),
						'MinimapIcon 0 Yellow UpsideDownHouse',
						'PlayEffect Yellow',
						"SetFontSize {}".format(size['huge']),
						'CustomAlertSound "{}_currency"'.format("mirror"),
						"SetBackgroundColor {} 220".format(color['highlight'])],
	"fragment extremely high": ['MinimapIcon 0 Green Raindrop',
								"SetTextColor {}".format(color['premiumllavender']),
								'PlayEffect Green',
								"SetBorderColor {}".format(color['premiumllavender']),
								"SetFontSize {}".format(size['huge']),
								'CustomAlertSound "{}_currency"'.format('max'),
								"SetBackgroundColor {} 220".format(color['highlight'])],
	"fragment very high": ['MinimapIcon 1 Blue Raindrop',
						   "SetTextColor {}".format(color['premiumllavender']),
						   'PlayEffect Blue',
						   "SetBorderColor {}".format(color['premiumllavender']),
						   "SetFontSize {}".format(size['vlarge']),
						   'CustomAlertSound "{}_map_good"'.format('high'),
						   "SetBackgroundColor {} 220".format(color['black'])],
	"fragment high": ['MinimapIcon 1 Blue Raindrop',
					  "SetTextColor {}".format(color['premiumllavender']),
					  "SetFontSize {}".format(size['normal']),
					  "SetBorderColor {}".format(color['premiumllavender']),
					  'CustomAlertSound "{}_map_good"'.format('normal'),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"fragment normal": ["SetFontSize {}".format(size['normal']),
						"SetTextColor {}".format(color['premiumllavender']),
						"SetBorderColor {} 150".format(color['premiumllavender']),
						'MinimapIcon 2 Brown Raindrop',
						"SetBackgroundColor {} 220".format(color['black'])],
	"fragment low": ["SetFontSize {}".format(size['small']),
					 "SetTextColor {}".format(color['premiumllavender']),
					 "SetBorderColor {} 100".format(color['premiumllavender']),
					 "SetBackgroundColor {} 220".format(color['black'])],

	"map red": ["SetBorderColor {} 150".format(color['fire']),
				'MinimapIcon 1 Red Diamond',
				"SetFontSize {}".format(size['large']),
				'CustomAlertSound "{}_map_okay"'.format('normal'),
				"SetBackgroundColor {} 220".format(color['black'])],
	"map yellow": ["SetBorderColor {} 150".format(color['lightning']),
				   'MinimapIcon 2 Yellow Diamond',
				   "SetFontSize {}".format(size['normal']),
				   "SetBackgroundColor {} 220".format(color['black'])],
	"map white": ["SetBorderColor {} 150".format(color['normal']),
				  'MinimapIcon 2 White Diamond',
				  "SetFontSize {}".format(size['normal']),
				  "SetBackgroundColor {} 220".format(color['black'])],

	"map highlight": ["SetBorderColor {}".format(color['gem']),
					  'MinimapIcon 0 Blue Diamond',
					  'PlayEffect Blue',
					  "SetFontSize {}".format(size['vlarge']),
					  'CustomAlertSound "{}_map_good"'.format('high'),
					  "SetBackgroundColor {} 220".format(color['supporterpack'])],

	"map very good": ["SetBorderColor {}".format(color['fire']),
					 'MinimapIcon 0 Red Diamond',
					 'PlayEffect Red',
					 "SetFontSize {}".format(size['huge']),
					 'CustomAlertSound "{}_map_good"'.format('max'),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"map red good": ["SetBorderColor {}".format(color['fire']),
					 'MinimapIcon 0 Red Diamond',
					 'PlayEffect Red',
					 "SetFontSize {}".format(size['vlarge']),
					 'CustomAlertSound "{}_map_good"'.format('high'),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"map yellow good": ["SetBorderColor {}".format(color['lightning']),
						'MinimapIcon 1 Yellow Diamond',
						'PlayEffect Yellow',
						'CustomAlertSound "{}_map_good"'.format('medium'),
						"SetFontSize {}".format(size['large']),
						"SetBackgroundColor {} 220".format(color['black'])],
	"map white good": ["SetBorderColor {}".format(color['normal']),
					   'MinimapIcon 1 White Diamond',
					   'PlayEffect White',
					   "SetFontSize {}".format(size['normal']),
					   "SetBackgroundColor {} 220".format(color['black']),
					   'CustomAlertSound "{}_map_good"'.format('low')],

	"influenced map red": ["SetBorderColor {} 150".format(color['fire']),
				'MinimapIcon 1 Red Cross',
				"SetFontSize {}".format(size['large']),
				'CustomAlertSound "{}_map_okay"'.format('normal'),
				"SetBackgroundColor {} 220".format(color['black'])],
	"influenced map yellow": ["SetBorderColor {} 150".format(color['lightning']),
				   'MinimapIcon 2 Yellow Cross',
				   "SetFontSize {}".format(size['normal']),
				   "SetBackgroundColor {} 220".format(color['black'])],
	"influenced map white": ["SetBorderColor {} 150".format(color['normal']),
				  'MinimapIcon 2 White Cross',
				  "SetFontSize {}".format(size['normal']),
				  "SetBackgroundColor {} 220".format(color['black'])],

	"influenced map very good": ["SetBorderColor {}".format(color['fire']),
					 'MinimapIcon 0 Red Cross',
					 'PlayEffect Red',
					 "SetFontSize {}".format(size['huge']),
					 'CustomAlertSound "{}_map_good"'.format('max'),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"influenced map red good": ["SetBorderColor {}".format(color['fire']),
					 'MinimapIcon 0 Red Cross',
					 'PlayEffect Red',
					 "SetFontSize {}".format(size['vlarge']),
					 'CustomAlertSound "{}_map_good"'.format('high'),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"influenced map yellow good": ["SetBorderColor {}".format(color['lightning']),
						'MinimapIcon 1 Yellow Cross',
						'PlayEffect Yellow',
						'CustomAlertSound "{}_map_good"'.format('medium'),
						"SetFontSize {}".format(size['large']),
						"SetBackgroundColor {} 220".format(color['black'])],
	"influenced map white good": ["SetBorderColor {}".format(color['normal']),
					   'MinimapIcon 1 White Cross',
					   'PlayEffect White',
					   "SetFontSize {}".format(size['normal']),
					   "SetBackgroundColor {} 220".format(color['black']),
					   'CustomAlertSound "{}_map_good"'.format('low')],

	"leveling high": ["SetFontSize {}".format(size['normal']),
					  "SetBackgroundColor {} 150".format(color['black']),
					  "SetBorderColor {}".format(color['nemesisoutline'])],
	"leveling normal": ["SetFontSize {}".format(size['small']),
						"SetBackgroundColor {} 150".format(color['black']),
						"SetBorderColor {}".format(color['tormentoutline'])],
	"leveling low": ["SetFontSize {}".format(size['minimum']),
					 "SetBackgroundColor {} 150".format(color['black']),
					 "SetBorderColor {}".format(color['normal'])],

	"levelling rare high": ["Rarity Rare",
							"SetBorderColor {} 150".format(color['rare']),
							"SetFontSize {}".format(size['large']),
							"SetBackgroundColor {} 220".format(color['black'])],
	"rare highlight": ["Rarity Rare",
					   'MinimapIcon 2 Yellow Circle',
					   "SetFontSize {}".format(size['large']),
					   "SetBorderColor {} 150".format(color['premiumorange']),
					   "SetBackgroundColor {} 220".format(color['premiumdpurple'])],
	"rare high": ["Rarity Rare",
				  "SetBorderColor {}".format(color['rare']),
				  "SetFontSize {}".format(size['normal']),
				  "SetBackgroundColor {} 220".format(color['black'])],
	"levelling rare normal": ["Rarity Rare",
							  "SetBorderColor {} 150".format(color['rare']),
							  "SetFontSize {}".format(size['normal']),
							  "SetBackgroundColor {} 220".format(color['black'])],
	"rare normal": ["Rarity Rare",
					"SetFontSize {}".format(size['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],
	"rare low": ["Rarity Rare",
				 "SetFontSize {}".format(size['small']),
				 "SetBackgroundColor {} 220".format(color['black'])],
	"rare corrupted": ["Rarity Rare",
					   "SetFontSize {}".format(size['small']),
					   "SetBorderColor {} 100".format(color['premiumlred']),
					   "SetBackgroundColor {} 220".format(color['black'])],

	"chromatic": ["SocketGroup RGB",
				  "SetBorderColor {}".format(color['premiumgreen']),
				  "SetFontSize {}".format(size['normal']),
				  "SetBackgroundColor {} 220".format(color['black'])],
	"recipe item normal": ["SetBorderColor {}".format(color['premiumlavender']),
						   'MinimapIcon 2 Grey Square',
						   "SetFontSize {}".format(size['minimum']),
						   "SetBackgroundColor {} 220".format(color['black'])],
	"recipe item rare": ["SetBorderColor {}".format(color['premiumlavender']),
						 'MinimapIcon 2 Grey Square',
						 "SetFontSize {}".format(size['normal']),
						 "SetBackgroundColor {} 220".format(color['magic'])],
	"recipe item rare small": ["SetBorderColor {}".format(color['premiumlavender']),
							   'MinimapIcon 2 Grey Square',
							   "SetFontSize {}".format(size['small']),
						       "SetBackgroundColor {} 220".format(color['cold'])],

	"item mod": ["SetBorderColor {}".format(color['premiumlpurple']),
				 'MinimapIcon 2 Grey UpsideDownHouse',
				 "SetFontSize {}".format(size['normal']),
				 "SetBackgroundColor {} 220".format(color['black'])],

	# Special sound for anything worth at least 1/20th of a mirror
	"base mirror": ["SetBorderColor {}".format(color['premiumgreen']),
					"Rarity < Unique",
					'MinimapIcon 0 Yellow UpsideDownHouse',
					'PlayEffect Yellow',
					"SetFontSize {}".format(size['huge']),
					'CustomAlertSound "{}_base"'.format("mirror"),
					"SetBackgroundColor {} 220".format(color['highlight'])],
	"base extremely high": ["Rarity < Unique",
							'MinimapIcon 0 Green Circle',
							'PlayEffect Green',
							"SetBorderColor {}".format(color['premiumgreen']),
							"SetFontSize {}".format(size['huge']),
							'CustomAlertSound "{}_base"'.format('max'),
							"SetBackgroundColor {} 220".format(color['highlight'])],
	"base very high": ["Rarity < Unique",
					   'MinimapIcon 1 Blue Circle',
					   'PlayEffect Blue',
					   "SetBorderColor {}".format(color['premiumgreen']),
					   "SetFontSize {}".format(size['huge']),
					   'CustomAlertSound "{}_base"'.format('high'),
					   "SetBackgroundColor {} 220".format(color['black'])],

	# Special sound for anything worth at least 1/20th of a mirror
	"unique mirror": ["SetBorderColor {}".format(color['currency']),
					  "Rarity Unique",
					  'MinimapIcon 0 Yellow UpsideDownHouse',
					  'PlayEffect Yellow',
					  "SetFontSize {}".format(size['huge']),
					  'CustomAlertSound "{}_currency"'.format("mirror"),
					  "SetBackgroundColor {} 220".format(color['highlight'])],
	"unique extremely high": ["Rarity Unique",
							  'MinimapIcon 0 Green Star',
							  'PlayEffect Green',
							  "SetBorderColor {}".format(color['unique']),
							  "SetFontSize {}".format(size['huge']),
							  'CustomAlertSound "{}_unique"'.format('max'),
							  "SetBackgroundColor {} 220".format(color['highlight'])],
	"unique very high": ["Rarity Unique",
						 'MinimapIcon 1 Blue Star',
						 'PlayEffect Blue',
						 "SetBorderColor {}".format(color['unique']),
						 "SetFontSize {}".format(size['vlarge']),
						 'CustomAlertSound "{}_unique"'.format('high'),
						 "SetBackgroundColor {} 220".format(color['black'])],
	"unique high": ["Rarity Unique",
					'MinimapIcon 1 Blue Star',
					"SetFontSize {}".format(size['normal']),
					"SetBorderColor {}".format(color['unique']),
					'CustomAlertSound "{}_unique"'.format('normal'),
					"SetBackgroundColor {} 220".format(color['black'])],
	# Special class of unique that has a low average value but has some items that are quite valuable
	"unique special": ["Rarity Unique",
					   "SetFontSize {}".format(size['normal']),
					   'MinimapIcon 2 White Star',
					   "SetBorderColor {}".format(color['chaos']),
	                   'CustomAlertSound "{}_unique"'.format('medium'),
					   "SetBackgroundColor {} 220".format(color['black'])],
	# Special class of unique where only a restricted drop is valuable
	"unique limited": ["Rarity Unique",
					   "SetFontSize {}".format(size['normal']),
					   "SetBorderColor {}".format(color['premiumblue']),
					   'MinimapIcon 2 Cyan Star',
					   "SetBackgroundColor {} 220".format(color['black'])],
	"unique normal": ["Rarity Unique",
					  "SetFontSize {}".format(size['normal']),
					  'MinimapIcon 2 Brown Star',
					  "SetBackgroundColor {} 220".format(color['black'])],
	"unique low": ["Rarity Unique",
				   "SetFontSize {}".format(size['small']),
				   "SetBackgroundColor {} 220".format(color['black'])],

	# Special sound for anything worth at least 1/20th of a mirror
	"show mirror": ["SetBorderColor {}".format(color['premiumlpurple']),
					'MinimapIcon 0 Yellow UpsideDownHouse',
					'PlayEffect Yellow',
					"SetFontSize {}".format(size['huge']),
					'CustomAlertSound "{}_show"'.format("mirror"),
					"SetBackgroundColor {} 220".format(color['highlight'])],
	"show very high": ["SetBorderColor {}".format(color['premiumlpurple']),
					   'MinimapIcon 0 Green Square',
					   'PlayEffect Green',
					   "SetFontSize {}".format(size['huge']),
					   'CustomAlertSound "{}_show"'.format('high'),
					   "SetBackgroundColor {} 220".format(color['black'])],
	"show high": ["SetBorderColor {}".format(color['premiumlpurple']),
				  'MinimapIcon 1 Blue Square',
				  'PlayEffect Blue',
				  'CustomAlertSound "{}_show"'.format('normal'),
				  "SetFontSize {}".format(size['large']),
				  "SetBackgroundColor {} 220".format(color['black'])],
	"show normal": ["SetBorderColor {}".format(color['premiumlpurple']),
					'MinimapIcon 2 Grey Square',
					'CustomAlertSound "{}_show"'.format('low'),
					"SetFontSize {}".format(size['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],
	"show level": ["SetBorderColor {}".format(color['premiumdgrey']),
					"SetFontSize {}".format(size['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],
	"show low": ["SetFontSize {}".format(size['small']),
				 "SetBackgroundColor {} 220".format(color['black'])],
	"high": ["SetBorderColor {}".format(color['premiumdyellow']),
			 "SetFontSize {}".format(size['large']),
			 "SetBackgroundColor {} 220".format(color['black'])],
	"normal border": ["SetFontSize {}".format(size['normal']),
					  "SetBorderColor {}".format(color['normal']),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"normal": ["SetFontSize {}".format(size['normal']),
			   "SetBackgroundColor {} 220".format(color['black'])],
	"low": ["SetFontSize {}".format(size['minimum']),
			"SetBackgroundColor {} 150".format(color['black'])],

	"ignore": [""],  # will have no styling applied and will use the default set at the end
	"hide": [""]  # Will be explicitly hidden with applied styling
})
