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
	"Driftwood Maul": {"base": "Driftwood Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 8"], "type": "leveling low"},
	"Tribal Maul": {"base": "Tribal Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 13"], "type": "leveling low"},
	"Mallet": {"base": "Mallet", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Sledgehammer": {"base": "Sledgehammer", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 22"], "type": "leveling low"},
	"Jagged Maul": {"base": "Jagged Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 27"], "type": "leveling low"},
	"Brass Maul": {"base": "Brass Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 32"], "type": "leveling low"},
	"Fright Maul": {"base": "Fright Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 37"], "type": "leveling low"},
	"Morning Star": {"base": "Morning Star", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Totemic Maul": {"base": "Totemic Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 41"], "type": "leveling low"},
	"Great Mallet": {"base": "Great Mallet", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Steelhead": {"base": "Steelhead", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 49"], "type": "leveling low"},
	"Spiny Maul": {"base": "Spiny Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 53"], "type": "ignore"},
	"Plated Maul": {"base": "Plated Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 56"], "type": "ignore"},
	"Dread Maul": {"base": "Dread Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 59"], "type": "ignore"},
	"Solar Maul": {"base": "Solar Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Karui Maul": {"base": "Karui Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 62"], "type": "ignore"},
	"Colossus Mallet": {"base": "Colossus Mallet", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Piledriver": {"base": "Piledriver", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 66"], "type": "ignore"},
	"Meatgrinder": {"base": "Meatgrinder", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 68"], "type": "ignore"},
	"Imperial Maul": {"base": "Imperial Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Terror Maul": {"base": "Terror Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 72"], "type": "ignore"},
	"Coronal Maul": {"base": "Coronal Maul", "class": "Two Hand Mace", "other": ["Rarity <= Magic", "ItemLevel <= 74"], "type": "ignore"}
}