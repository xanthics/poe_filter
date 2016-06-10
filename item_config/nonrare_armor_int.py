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

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Simple Robe": {"base": "Simple Robe", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Silken Vest": {"base": "Silken Vest", "other": ["Rarity <= Magic", "ItemLevel <= 16"], "type": "leveling low"},
	"Scholar's Robe": {"base": "Scholar's Robe", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "leveling low"},
	"Silken Garb": {"base": "Silken Garb", "other": ["Rarity <= Magic", "ItemLevel <= 30"], "type": "leveling low"},
	"Mage's Vestment": {"base": "Mage's Vestment", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Silk Robe": {"base": "Silk Robe", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Cabalist Regalia": {"base": "Cabalist Regalia", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Sage's Robe": {"base": "Sage's Robe", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Silken Wrap": {"base": "Silken Wrap", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Conjurer's Vestment": {"base": "Conjurer's Vestment", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Spidersilk Robe": {"base": "Spidersilk Robe", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Destroyer Regalia": {"base": "Destroyer Regalia", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Savant's Robe": {"base": "Savant's Robe", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Necromancer Silks": {"base": "Necromancer Silks", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Occultist's Vestment": {"base": "Occultist's Vestment", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Widowsilk Robe": {"base": "Widowsilk Robe", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Vaal Regalia": {"base": "Vaal Regalia", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Wool Shoes": {"base": "Wool Shoes", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Velvet Slippers": {"base": "Velvet Slippers", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "leveling low"},
	"Silk Slippers": {"base": "Silk Slippers", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "leveling low"},
	"Scholar Boots": {"base": "Scholar Boots", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Satin Slippers": {"base": "Satin Slippers", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "leveling low"},
	"Samite Slippers": {"base": "Samite Slippers", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Conjurer Boots": {"base": "Conjurer Boots", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Arcanist Slippers": {"base": "Arcanist Slippers", "other": ["Rarity <= Magic", "ItemLevel <= 66"], "type": "ignore"},
	"Sorcerer Boots": {"base": "Sorcerer Boots", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Wool Gloves": {"base": "Wool Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Velvet Gloves": {"base": "Velvet Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Silk Gloves": {"base": "Silk Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 30"], "type": "leveling low"},
	"Embroidered Gloves": {"base": "Embroidered Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Satin Gloves": {"base": "Satin Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Samite Gloves": {"base": "Samite Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "ignore"},
	"Conjurer Gloves": {"base": "Conjurer Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Arcanist Gloves": {"base": "Arcanist Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "ignore"},
	"Sorcerer Gloves": {"base": "Sorcerer Gloves", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Vine Circlet": {"base": "Vine Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Iron Circlet": {"base": "Iron Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "leveling low"},
	"Torture Cage": {"base": "Torture Cage", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Tribal Circlet": {"base": "Tribal Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 31"], "type": "leveling low"},
	"Bone Circlet": {"base": "Bone Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Lunaris Circlet": {"base": "Lunaris Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 44"], "type": "leveling low"},
	"Steel Circlet": {"base": "Steel Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 53"], "type": "ignore"},
	"Necromancer Circlet": {"base": "Necromancer Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Solaris Circlet": {"base": "Solaris Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Mind Cage": {"base": "Mind Cage", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Hubris Circlet": {"base": "Hubris Circlet", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"},
	"Twig Spirit Shield": {"base": "Twig Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Yew Spirit Shield": {"base": "Yew Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "leveling low"},
	"Bone Spirit Shield": {"base": "Bone Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 20"], "type": "leveling low"},
	"Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "leveling low"},
	"Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "leveling low"},
	"Brass Spirit Shield": {"base": "Brass Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 38"], "type": "leveling low"},
	"Walnut Spirit Shield": {"base": "Walnut Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 42"], "type": "leveling low"},
	"Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "leveling low"},
	"Ancient Spirit Shield": {"base": "Ancient Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Lacewood Spirit Shield": {"base": "Lacewood Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Fossilised Spirit Shield": {"base": "Fossilised Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"}
}
