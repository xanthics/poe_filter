"""
* Copyright (c) 2015 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create an item filter based on config files
Note: Requires Python 3.4.x
"""

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
	"prophecy": "128 0 200"
}

size = {
	"huge": "45",
	"vlarge": "40",
	"large": "35",
	"normal": "30",
	"small": "25",
	"minimum": "18",
}

# Text settings for various categories
# This is where you would define general settings for a category, such as PlayAlertSound.
# Each config should be its own array element.  Parsing will handle tabs/etc.
# ignore and hide have special meaning(see comment)
settings = {
	"challenge": ["SetBorderColor {}".format(color['prophecy']),
				  "SetFontSize {}".format(size['huge']),
				  "PlayAlertSound 4 175",
				  "SetBackgroundColor {} 220".format(color['black'])],

	"animate melee b": ["Rarity Normal",
					  "SetFontSize {}".format(size['large']),
					  "SetTextColor {}".format(color['black']),
					  "SetBorderColor {} 200".format(color['premiumlgreen']),
					  "SetBackgroundColor {} 150".format(color['premiumdgreen'])],
	"animate melee": ["Rarity Normal",
					  "SetFontSize {}".format(size['large']),
					  "SetTextColor {}".format(color['black']),
					  "SetBackgroundColor {} 150".format(color['premiumdgreen'])],

	"quest": ["SetFontSize {}".format(size['normal']),
			  "SetBorderColor {} 200".format(color['quest']),
			   "SetBackgroundColor {} 220".format(color['black'])],

	"animate range b": ["Rarity Normal",
					  "SetFontSize {}".format(size['large']),
					  "SetTextColor {}".format(color['black']),
					  "SetBorderColor {} 200".format(color['premiumtan']),
					  "SetBackgroundColor {} 150".format(color['premiumbrown'])],

	"animate range": ["Rarity Normal",
					  "SetFontSize {}".format(size['large']),
					  "SetTextColor {}".format(color['black']),
					  "SetBackgroundColor {} 150".format(color['premiumbrown'])],

	"chance": ["Rarity Normal",
			   "SetFontSize {}".format(size['small']),
			   "SetBorderColor {} 150".format(color['premiumorange']),
			   "SetBackgroundColor {} 220".format(color['black'])],

	"chromatic": ["SocketGroup RGB",
				  "SetBorderColor {}".format(color['premiumgreen']), 
				  "SetFontSize {}".format(size['normal']),
				  "SetBackgroundColor {} 220".format(color['black'])],

	"t1 ilvl83/84 crafting": ["Rarity <= Magic", 
							  "SetBackgroundColor {} 220".format(color['black'])],

	"currency very high": ["SetBorderColor {}".format(color['currency']), 
						   "SetFontSize {}".format(size['huge']),
						   "PlayAlertSound 5 300", 
						   "SetBackgroundColor {} 220".format(color['black'])],
	"currency high": ["SetBorderColor {}".format(color['currency']), 
					  "SetFontSize {}".format(size['large']),
					  "PlayAlertSound 5 75", 
					  "SetBackgroundColor {} 220".format(color['black'])],
	"currency normal": ["SetBorderColor {}".format(color['currency']), 
						"PlayAlertSound 5 25", 
						"SetBackgroundColor {} 220".format(color['black'])],
	"currency low": ["SetBorderColor {}".format(color['currency']), 
					 "SetFontSize {}".format(size['normal']),
					 "SetBackgroundColor {} 220".format(color['black'])],

	"divination high": ["SetBorderColor {}".format(color['divinationnew']),
						"SetFontSize {}".format(size['vlarge']),
						"PlayAlertSound 6 175", 
						"SetBackgroundColor {} 220".format(color['black'])],
	"divination normal": ["SetBorderColor {}".format(color['divinationnew']),
						  "PlayAlertSound 6 50", 
						  "SetBackgroundColor {} 220".format(color['black'])],
	"divination low": ["SetBorderColor {}".format(color['divinationnew']),
					   "SetBackgroundColor {} 220".format(color['black'])],

	"gem very high": ["SetBorderColor {}".format(color['gem']),
					  "SetFontSize {}".format(size['large']),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"gem high": ["SetBorderColor {}".format(color['gem']), 
				 "SetFontSize {}".format(size['normal']),
				 "SetBackgroundColor {} 220".format(color['black'])],
	"gem normal": ["SetBorderColor {}".format(color['gem']), 
				   "SetBackgroundColor {} 220".format(color['black'])],
	"gem low": ["SetFontSize {}".format(size['small']),
				"SetBackgroundColor {} 220".format(color['black'])],

	"leveling high": ["SetFontSize {}".format(size['normal']),
					  "SetBackgroundColor {} 100".format(color['black']),
					  "SetBorderColor {}".format(color['nemesisoutline'])],
	"leveling normal": ["SetFontSize {}".format(size['small']),
						"SetBackgroundColor {} 100".format(color['black']),
						"SetBorderColor {}".format(color['tormentoutline'])],
	"leveling low": ["SetFontSize {}".format(size['minimum']),
					 "Sockets > 2", 
					 "SetBackgroundColor {} 100".format(color['black']),
					 "SetBorderColor {}".format(color['normal'])],

	"map red": ["SetBorderColor {} 150".format(color['fire']),
				"SetFontSize {}".format(size['huge']),
				"PlayAlertSound 8 125",
				"SetBackgroundColor {} 220".format(color['black'])],
	"map yellow": ["SetBorderColor {} 150".format(color['lightning']),
				   "PlayAlertSound 8 75",
				   "SetFontSize {}".format(size['large']),
				   "SetBackgroundColor {} 220".format(color['black'])],
	"map white": ["SetBorderColor {} 150".format(color['normal']),
				  "SetBackgroundColor {} 220".format(color['black'])],

	"map red good": ["SetBorderColor {}".format(color['fire']),
					  "SetFontSize {}".format(size['huge']),
					  "PlayAlertSound 7 125",
					  "SetBackgroundColor {} 220".format(color['black'])],
	"map yellow good": ["SetBorderColor {}".format(color['lightning']),
				   		"PlayAlertSound 7 75",
				   		"SetFontSize {}".format(size['large']),
				   		"SetBackgroundColor {} 220".format(color['black'])],
	"map white good": ["SetBorderColor {}".format(color['normal']),
					   "SetBackgroundColor {} 220".format(color['black']),
					   "PlayAlertSound 7 25"],

	"levelling rare high": ["Rarity Rare", 
							"SetBorderColor {} 150".format(color['rare']), 
							"SetFontSize {}".format(size['large']),
							"SetBackgroundColor {} 220".format(color['black'])],
	"rare high": ["Rarity Rare", 
				  "SetBorderColor {}".format(color['rare']), 
				  "SetFontSize {}".format(size['large']),
				  "SetBackgroundColor {} 220".format(color['black'])],
	"levelling rare normal": ["Rarity Rare", 
							  "SetBorderColor {} 150".format(color['rare']),
							  "SetFontSize {}".format(size['normal']),
							  "SetBackgroundColor {} 220".format(color['black'])],
	"rare normal": ["Rarity Rare", 
					"SetBorderColor {}".format(color['rare']),
					"SetFontSize {}".format(size['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],
	"rare low": ["Rarity Rare", 
				 "SetFontSize {}".format(size['small']),
				 "SetBackgroundColor {} 220".format(color['black'])],

	"recipe item normal": ["SetBorderColor {}".format(color['premiumlavender']), 
						   "SetFontSize {}".format(size['normal']),
						   "SetBackgroundColor {} 220".format(color['black'])],

	"show very high": ["SetBorderColor {}".format(color['premiumlpurple']),
					   "SetFontSize {}".format(size['huge']),
					   "PlayAlertSound 1 175", 
					   "SetBackgroundColor {} 220".format(color['black'])],
	"show high": ["SetBorderColor {}".format(color['premiumlpurple']),
				  "SetFontSize {}".format(size['large']),
				  "SetBackgroundColor {} 220".format(color['black'])],
	"show normal": ["SetBorderColor {}".format(color['premiumlpurple']),
					"SetFontSize {}".format(size['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],
	"show low": ["SetFontSize {}".format(size['small']),
				 "SetBackgroundColor {} 220".format(color['black'])],

	"t1 83/84 rare high": ["Rarity Rare", 
						   "SetBorderColor {}".format(color['nemesisoutline']), 
						   "SetFontSize {}".format(size['large']),
						   "SetBackgroundColor {} 220".format(color['black'])],

	"unique very high": ["Rarity Unique", 
						 "SetBorderColor {}".format(color['unique']), 
						 "SetFontSize {}".format(size['huge']),
						 "PlayAlertSound 3 300", 
						 "SetBackgroundColor {} 220".format(color['black'])],
	"unique high": ["Rarity Unique", 
					"SetFontSize {}".format(size['vlarge']),
					"SetBorderColor {}".format(color['unique']), 
					"PlayAlertSound 3 75", 
					"SetBackgroundColor {} 220".format(color['black'])],
	"unique normal": ["Rarity Unique", 
					  "PlayAlertSound 3 50", 
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
			"SetBackgroundColor {} 100".format(color['black']),
			"SetBorderColor {}".format(color['premiumgrey'])],

	"ignore": [""],  # will have no styling applied and will use the default set at the end
	"hide": [""]  # Will be explicitly hidden with applied styling
}
