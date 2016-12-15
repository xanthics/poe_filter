"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
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

desc = "Always show"

# Base type : settings pair
items = {
    "01 Tabula Exception": {"base": "Simple Robe", "other": ["Rarity Unique", "SocketGroup WWWWWW"], "type": "unique high"},
    "02 6L": {"other": ["LinkedSockets 6"], "type": "show very high"},
    "03 5L": {"other": ["LinkedSockets 5", "PlayAlertSound 2 75"], "type": "show high"},
    "04 6S": {"other": ["Sockets 6", "PlayAlertSound 2 50"], "type": "show high"},
    # High value atlas bases.  Show and make noise at any rarity
    "04 Steel Ring": {"base": "Steel Ring", "type": "show high"},
    "04 Crystal Belt": {"base": "Crystal Belt", "type": "show high"},
    "04 Opal Ring": {"base": "Opal Ring", "type": "show high"},
    "10 Talisman": {'other': ["Rarity >= Rare", "ItemLevel >= 70"], "base": "Talisman", "type": "show high"},
    "11 Talisman": {'other': ["ItemLevel >= 70"], "base": "Talisman", "type": "show high"},
    "12 Talisman": {"base": "Talisman", "type": "show low"},
    "0 Fishing Rod": {"base": "Fishing Rod", "type": "show very high"},
    "0 Hideout Doodads": {"class": "Hideout Doodads", "type": "show low"},
    "0 Microtransactions": {"class": "Microtransactions", "type": "show low"},
    "0 Quest": {"class": "Quest", "type": "quest"},
    "0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "show high"},
    "0 Jewel": {"class": "Jewel", "other": ["Rarity <= Magic"], "type": "show normal"},

    "9 Starter weapon": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "ItemLevel < 2"], "type": "low"},

    # Rare highlighting for currency recipes.  change 'ignore' to 'high' or back as needed
    "0 Rare Two Hand": {"class": "Two Hand\" \"Staves\" \"Bow", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
    "0 Rare Helm": {"class": "Helmets", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
    "0 Rare Body": {"class": "Body Armours", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
    "0 Rare Glove": {"class": "Gloves", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
    "0 Rare Boot": {"class": "Boots", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},

	"02 60+ amulet": {"class": "Amulets", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
	"02 60+ ring": {"class": "Rings", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},
	"02 60+ belt": {"class": "Belts", "other": ["Rarity Rare", "ItemLevel >= 60"], "type": "ignore"},

}