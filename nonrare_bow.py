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
	"high": ["SetFontSize 24",
			 "SetBackgroundColor 0 0 0 100",
			 "SetBorderColor 0 100 150"],
	"normal": ["SetFontSize 18",
			   "SetBackgroundColor 0 0 0 100",
			   "SetBorderColor 100 100 100"],
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
	"Crude Bow": {"base": "Crude Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "normal"},
	"Short Bow": {"base": "Short Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 10"], "type": "normal"},
	"Long Bow": {"base": "Long Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 14"], "type": "normal"},
	"Composite Bow": {"base": "Composite Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 19"], "type": "normal"},
	"Recurve Bow": {"base": "Recurve Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "normal"},
	"Bone Bow": {"base": "Bone Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 28"], "type": "normal"},
	"Royal Bow": {"base": "Royal Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 33"], "type": "normal"},
	"Death Bow": {"base": "Death Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "high"},
	"Grove Bow": {"base": "Grove Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "normal"},
	"Reflex Bow": {"base": "Reflex Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "normal"},
	"Decurve Bow": {"base": "Decurve Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 43"], "type": "normal"},
	"Compound Bow": {"base": "Compound Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 46"], "type": "normal"},
	"Sniper Bow": {"base": "Sniper Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "normal"},
	"Ivory Bow": {"base": "Ivory Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 52"], "type": "normal"},
	"Highborn Bow": {"base": "Highborn Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 55"], "type": "normal"},
	"Decimation Bow": {"base": "Decimation Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "high"},
	"Thicket Bow": {"base": "Thicket Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "normal"},
	"Steelwood Bow": {"base": "Steelwood Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "normal"},
	"Citadel Bow": {"base": "Citadel Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 63"], "type": "normal"},
	"Ranger Bow": {"base": "Ranger Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 65"], "type": "normal"},
	"Assassin Bow": {"base": "Assassin Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "normal"},
	"Spine Bow": {"base": "Spine Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 69"], "type": "normal"},
	"Imperial Bow": {"base": "Imperial Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 71"], "type": "normal"},
	"Harbinger Bow": {"base": "Harbinger Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "high"},
	"Maraketh Bow": {"base": "Maraketh Bow", "class": "Bow", "other": ["Rarity <= Magic", "ItemLevel <= 76"], "type": "normal"}
}
