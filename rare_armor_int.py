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

desc = "Nonrare item for leveling or crafting"

# Text settings for various categories
# This is where you would define general settings for a category, such as PlayAlertSound.
# Each config should be its own array element.  Parsing will handle tabs/etc.
# ignore and hide have special meaning(see comment) everything else is local to file
settings = {
	"very high": ["SetFontSize 28",
				  "SetBackgroundColor 0 0 0 100",
				  "SetBorderColor 255 40 0"],
	"high": ["Rarity Rare",
             "SetBorderColor 255 255 119",
             "SetFontSize 34"],
	"normal": ["Rarity Rare",
             "SetBorderColor 255 255 119"],
	"low": [""],
	"ignore": [""],  # will have no styling applied and will use the default set at the end
	"hide": [""]  # Will be explicitly hidden with applied styling
}

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Simple Robe": {"base": "Simple Robe", "other": ["ItemLevel <= 8"], "type": "normal"},
	"Silken Vest": {"base": "Silken Vest", "other": ["ItemLevel <= 16"], "type": "normal"},
	"Scholar's Robe": {"base": "Scholar's Robe", "other": ["ItemLevel <= 23"], "type": "normal"},
	"Silken Garb": {"base": "Silken Garb", "other": ["ItemLevel <= 30"], "type": "normal"},
	"Mage's Vestment": {"base": "Mage's Vestment", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Silk Robe": {"base": "Silk Robe", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Cabalist Regalia": {"base": "Cabalist Regalia", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Sage's Robe": {"base": "Sage's Robe", "other": ["ItemLevel <= 42"], "type": "normal"},
	"Silken Wrap": {"base": "Silken Wrap", "other": ["ItemLevel <= 46"], "type": "normal"},
	"Conjurer's Vestment": {"base": "Conjurer's Vestment", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Spidersilk Robe": {"base": "Spidersilk Robe", "other": ["ItemLevel <= 54"], "type": "normal"},
	"Destroyer Regalia": {"base": "Destroyer Regalia", "other": ["ItemLevel <= 58"], "type": "normal"},
	"Savant's Robe": {"base": "Savant's Robe", "other": ["ItemLevel <= 61"], "type": "normal"},
	"Necromancer Silks": {"base": "Necromancer Silks", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Occultist's Vestment": {"base": "Occultist's Vestment", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Widowsilk Robe": {"base": "Widowsilk Robe", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Vaal Regalia": {"base": "Vaal Regalia", "other": ["ItemLevel <= 73"], "type": "normal"},
	"Wool Shoes": {"base": "Wool Shoes", "other": ["ItemLevel <= 8"], "type": "normal"},
	"Velvet Slippers": {"base": "Velvet Slippers", "other": ["ItemLevel <= 14"], "type": "normal"},
	"Silk Slippers": {"base": "Silk Slippers", "other": ["ItemLevel <= 27"], "type": "normal"},
	"Scholar Boots": {"base": "Scholar Boots", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Satin Slippers": {"base": "Satin Slippers", "other": ["ItemLevel <= 43"], "type": "normal"},
	"Samite Slippers": {"base": "Samite Slippers", "other": ["ItemLevel <= 49"], "type": "normal"},
	"Conjurer Boots": {"base": "Conjurer Boots", "other": ["ItemLevel <= 58"], "type": "normal"},
	"Arcanist Slippers": {"base": "Arcanist Slippers", "other": ["ItemLevel <= 66"], "type": "normal"},
	"Sorcerer Boots": {"base": "Sorcerer Boots", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Wool Gloves": {"base": "Wool Gloves", "other": ["ItemLevel <= 8"], "type": "normal"},
	"Velvet Gloves": {"base": "Velvet Gloves", "other": ["ItemLevel <= 17"], "type": "normal"},
	"Silk Gloves": {"base": "Silk Gloves", "other": ["ItemLevel <= 30"], "type": "normal"},
	"Embroidered Gloves": {"base": "Embroidered Gloves", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Satin Gloves": {"base": "Satin Gloves", "other": ["ItemLevel <= 46"], "type": "normal"},
	"Samite Gloves": {"base": "Samite Gloves", "other": ["ItemLevel <= 52"], "type": "normal"},
	"Conjurer Gloves": {"base": "Conjurer Gloves", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Arcanist Gloves": {"base": "Arcanist Gloves", "other": ["ItemLevel <= 65"], "type": "normal"},
	"Sorcerer Gloves": {"base": "Sorcerer Gloves", "other": ["ItemLevel <= 74"], "type": "normal"},
	"Vine Circlet": {"base": "Vine Circlet", "other": ["ItemLevel <= 8"], "type": "normal"},
	"Iron Circlet": {"base": "Iron Circlet", "other": ["ItemLevel <= 13"], "type": "normal"},
	"Torture Cage": {"base": "Torture Cage", "other": ["ItemLevel <= 22"], "type": "normal"},
	"Tribal Circlet": {"base": "Tribal Circlet", "other": ["ItemLevel <= 31"], "type": "normal"},
	"Bone Circlet": {"base": "Bone Circlet", "other": ["ItemLevel <= 39"], "type": "normal"},
	"Lunaris Circlet": {"base": "Lunaris Circlet", "other": ["ItemLevel <= 44"], "type": "normal"},
	"Steel Circlet": {"base": "Steel Circlet", "other": ["ItemLevel <= 53"], "type": "normal"},
	"Necromancer Circlet": {"base": "Necromancer Circlet", "other": ["ItemLevel <= 59"], "type": "normal"},
	"Solaris Circlet": {"base": "Solaris Circlet", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Mind Cage": {"base": "Mind Cage", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Hubris Circlet": {"base": "Hubris Circlet", "other": ["ItemLevel <= 74"], "type": "normal"},
	"Twig Spirit Shield": {"base": "Twig Spirit Shield", "other": ["ItemLevel <= 8"], "type": "normal"},
	"Yew Spirit Shield": {"base": "Yew Spirit Shield", "other": ["ItemLevel <= 14"], "type": "normal"},
	"Bone Spirit Shield": {"base": "Bone Spirit Shield", "other": ["ItemLevel <= 20"], "type": "normal"},
	"Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "other": ["ItemLevel <= 28"], "type": "normal"},
	"Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Brass Spirit Shield": {"base": "Brass Spirit Shield", "other": ["ItemLevel <= 38"], "type": "normal"},
	"Walnut Spirit Shield": {"base": "Walnut Spirit Shield", "other": ["ItemLevel <= 42"], "type": "normal"},
	"Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "other": ["ItemLevel <= 46"], "type": "normal"},
	"Ancient Spirit Shield": {"base": "Ancient Spirit Shield", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "other": ["ItemLevel <= 54"], "type": "normal"},
	"Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "other": ["ItemLevel <= 58"], "type": "normal"},
	"Lacewood Spirit Shield": {"base": "Lacewood Spirit Shield", "other": ["ItemLevel <= 61"], "type": "normal"},
	"Fossilised Spirit Shield": {"base": "Fossilised Spirit Shield", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "other": ["ItemLevel <= 73"], "type": "normal"}
}
