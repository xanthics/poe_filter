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
	"Plate Vest": {"base": "Plate Vest", "other": ["ItemLevel <= 6"], "type": "normal"},
	"Chestplate": {"base": "Chestplate", "other": ["ItemLevel <= 11"], "type": "normal"},
	"Copper Plate": {"base": "Copper Plate", "other": ["ItemLevel <= 22"], "type": "normal"},
	"War Plate": {"base": "War Plate", "other": ["ItemLevel <= 26"], "type": "normal"},
	"Full Plate": {"base": "Full Plate", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Arena Plate": {"base": "Arena Plate", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Lordly Plate": {"base": "Lordly Plate", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Bronze Plate": {"base": "Bronze Plate", "other": ["ItemLevel <= 42"], "type": "normal"},
	"Battle Plate": {"base": "Battle Plate", "other": ["ItemLevel <= 46"], "type": "normal"},
	"Sun Plate": {"base": "Sun Plate", "other": ["ItemLevel <= 50"], "type": "normal"},
	"Colosseum Plate": {"base": "Colosseum Plate", "other": ["ItemLevel <= 54"], "type": "normal"},
	"Majestic Plate": {"base": "Majestic Plate", "other": ["ItemLevel <= 58"], "type": "normal"},
	"Golden Plate": {"base": "Golden Plate", "other": ["ItemLevel <= 61"], "type": "normal"},
	"Crusader Plate": {"base": "Crusader Plate", "other": ["ItemLevel <= 64"], "type": "normal"},
	"Astral Plate": {"base": "Astral Plate", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Gladiator Plate": {"base": "Gladiator Plate", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Glorious Plate": {"base": "Glorious Plate", "other": ["ItemLevel <= 73"], "type": "normal"},
	"Iron Greaves": {"base": "Iron Greaves", "other": ["ItemLevel <= 6"], "type": "normal"},
	"Steel Greaves": {"base": "Steel Greaves", "other": ["ItemLevel <= 14"], "type": "normal"},
	"Plated Greaves": {"base": "Plated Greaves", "other": ["ItemLevel <= 28"], "type": "normal"},
	"Reinforced Greaves": {"base": "Reinforced Greaves", "other": ["ItemLevel <= 38"], "type": "normal"},
	"Antique Greaves": {"base": "Antique Greaves", "other": ["ItemLevel <= 42"], "type": "normal"},
	"Ancient Greaves": {"base": "Ancient Greaves", "other": ["ItemLevel <= 51"], "type": "normal"},
	"Goliath Greaves": {"base": "Goliath Greaves", "other": ["ItemLevel <= 59"], "type": "normal"},
	"Vaal Greaves": {"base": "Vaal Greaves", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Titan Greaves": {"base": "Titan Greaves", "other": ["ItemLevel <= 73"], "type": "normal"},
	"Iron Gauntlets": {"base": "Iron Gauntlets", "other": ["ItemLevel <= 6"], "type": "normal"},
	"Plated Gauntlets": {"base": "Plated Gauntlets", "other": ["ItemLevel <= 16"], "type": "normal"},
	"Bronze Gauntlets": {"base": "Bronze Gauntlets", "other": ["ItemLevel <= 28"], "type": "normal"},
	"Steel Gauntlets": {"base": "Steel Gauntlets", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Antique Gauntlets": {"base": "Antique Gauntlets", "other": ["ItemLevel <= 44"], "type": "normal"},
	"Ancient Gauntlets": {"base": "Ancient Gauntlets", "other": ["ItemLevel <= 52"], "type": "normal"},
	"Goliath Gauntlets": {"base": "Goliath Gauntlets", "other": ["ItemLevel <= 58"], "type": "normal"},
	"Vaal Gauntlets": {"base": "Vaal Gauntlets", "other": ["ItemLevel <= 68"], "type": "normal"},
	"Titan Gauntlets": {"base": "Titan Gauntlets", "other": ["ItemLevel <= 74"], "type": "normal"},
	"Iron Hat": {"base": "Iron Hat", "other": ["ItemLevel <= 6"], "type": "normal"},
	"Cone Helmet": {"base": "Cone Helmet", "other": ["ItemLevel <= 12"], "type": "normal"},
	"Barbute Helmet": {"base": "Barbute Helmet", "other": ["ItemLevel <= 23"], "type": "normal"},
	"Close Helmet": {"base": "Close Helmet", "other": ["ItemLevel <= 31"], "type": "normal"},
	"Gladiator Helmet": {"base": "Gladiator Helmet", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Reaver Helmet": {"base": "Reaver Helmet", "other": ["ItemLevel <= 45"], "type": "normal"},
	"Siege Helmet": {"base": "Siege Helmet", "other": ["ItemLevel <= 53"], "type": "normal"},
	"Samite Helmet": {"base": "Samite Helmet", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "other": ["ItemLevel <= 65"], "type": "normal"},
	"Royal Burgonet": {"base": "Royal Burgonet", "other": ["ItemLevel <= 70"], "type": "normal"},
	"Eternal Burgonet": {"base": "Eternal Burgonet", "other": ["ItemLevel <= 74"], "type": "normal"},
	"Splintered Tower Shield": {"base": "Splintered Tower Shield", "other": ["ItemLevel <= 6"], "type": "normal"},
	"Corroded Tower Shield": {"base": "Corroded Tower Shield", "other": ["ItemLevel <= 10"], "type": "normal"},
	"Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "other": ["ItemLevel <= 16"], "type": "normal"},
	"Cedar Tower Shield": {"base": "Cedar Tower Shield", "other": ["ItemLevel <= 22"], "type": "normal"},
	"Copper Tower Shield": {"base": "Copper Tower Shield", "other": ["ItemLevel <= 29"], "type": "normal"},
	"Reinforced Tower Shield": {"base": "Reinforced Tower Shield", "other": ["ItemLevel <= 35"], "type": "normal"},
	"Painted Tower Shield": {"base": "Painted Tower Shield", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Buckskin Tower Shield": {"base": "Buckskin Tower Shield", "other": ["ItemLevel <= 44"], "type": "normal"},
	"Mahogany Tower Shield": {"base": "Mahogany Tower Shield", "other": ["ItemLevel <= 48"], "type": "normal"},
	"Bronze Tower Shield": {"base": "Bronze Tower Shield", "other": ["ItemLevel <= 52"], "type": "normal"},
	"Girded Tower Shield": {"base": "Girded Tower Shield", "other": ["ItemLevel <= 56"], "type": "normal"},
	"Crested Tower Shield": {"base": "Crested Tower Shield", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Shagreen Tower Shield": {"base": "Shagreen Tower Shield", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Ebony Tower Shield": {"base": "Ebony Tower Shield", "other": ["ItemLevel <= 66"], "type": "normal"},
	"Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "other": ["ItemLevel <= 69"], "type": "normal"},
	"Colossal Tower Shield": {"base": "Colossal Tower Shield", "other": ["ItemLevel <= 72"], "type": "normal"},
	"Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "other": ["ItemLevel <= 75"], "type": "normal"}
}
