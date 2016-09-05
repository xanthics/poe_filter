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

desc = "Chance Base"

# Base type : settings pair
items = {
	"0 Aegis Aurora": {"base": "Champion Kite Shield", "type": "ignore"},
	"0 Heretic's Veil": {"base": "Deicide Mask", "type": "ignore"},
	"0 Taste of Hate": {"base": "Sapphire Flask", "type": "ignore"},
	"0 Lightning Coil": {"base": "Desert Brigandine", "type": "ignore"},
	"0 Cospri's Will": {"base": "Assassin's Garb", "type": "ignore"},
	"0 Rathpith Globe": {"base": "Titanium Spirit Shield", "type": "ignore"},
	"0 Carcass Jack": {"base": "Varnished Coat", "type": "ignore"},

	"0 Shavronne's Wrappings": {"base": "Occultist's Vestment", "type": "ignore"},
	"0 Kaom's Heart": {"base": "Glorious Plate", "type": "ignore"},
	"0 Void Battery": {"base": "Prophecy Wand", "type": "ignore"},
	"0 Soul Taker": {"base": "Siege Axe", "type": "ignore"},
	"0 Skyforth": {"base": "Sorcerer Boots", "type": "chance"},
	"0 Headhunter": {"base": "Leather Belt", "other": ["ItemLevel >= 74"], "type": "ignore"}
}
