#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Rare item for leveling or crafting"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Nailed Fist": {"base": "Nailed Fist", "class": "Claw", "other": ["ItemLevel <= 8"], "type": "levelling rare normal"},
	"Sharktooth Claw": {"base": "Sharktooth Claw", "class": "Claw", "other": ["ItemLevel <= 12"], "type": "levelling rare normal"},
	"Awl": {"base": "Awl", "class": "Claw", "other": ["ItemLevel <= 17"], "type": "levelling rare normal"},
	"Cat's Paw": {"base": "Cat's Paw", "class": "Claw", "other": ["ItemLevel <= 22"], "type": "levelling rare normal"},
	"Blinder": {"base": "Blinder", "class": "Claw", "other": ["ItemLevel <= 27"], "type": "levelling rare normal"},
	"Timeworn Claw": {"base": "Timeworn Claw", "class": "Claw", "other": ["ItemLevel <= 31"], "type": "levelling rare normal"},
	"Sparkling Claw": {"base": "Sparkling Claw", "class": "Claw", "other": ["ItemLevel <= 35"], "type": "levelling rare normal"},
	"Fright Claw": {"base": "Fright Claw", "class": "Claw", "other": ["ItemLevel <= 39"], "type": "levelling rare normal"},
	"Double Claw": {"base": "Double Claw", "class": "Claw", "other": ["ItemLevel <= 41"], "type": "levelling rare normal"},
	"Thresher Claw": {"base": "Thresher Claw", "class": "Claw", "other": ["ItemLevel <= 42"], "type": "levelling rare normal"},
	"Gouger": {"base": "Gouger", "class": "Claw", "other": ["ItemLevel <= 45"], "type": "levelling rare normal"},
	"Tiger's Paw": {"base": "Tiger's Paw", "class": "Claw", "other": ["ItemLevel <= 48"], "type": "levelling rare normal"},
	"Gut Ripper": {"base": "Gut Ripper", "class": "Claw", "other": ["ItemLevel <= 51"], "type": "levelling rare normal"},
	"Prehistoric Claw": {"base": "Prehistoric Claw", "class": "Claw", "other": ["ItemLevel <= 54"], "type": "levelling rare normal"},
	"Noble Claw": {"base": "Noble Claw", "class": "Claw", "other": ["ItemLevel <= 57"], "type": "levelling rare normal"},
	"Eagle Claw": {"base": "Eagle Claw", "class": "Claw", "other": ["ItemLevel <= 60"], "type": "levelling rare normal"},
	"Twin Claw": {"base": "Twin Claw", "class": "Claw", "other": ["ItemLevel <= 62"], "type": "levelling rare normal"},
	"Great White Claw": {"base": "Great White Claw", "class": "Claw", "other": ["ItemLevel <= 63"], "type": "levelling rare normal"},
	"Throat Stabber": {"base": "Throat Stabber", "class": "Claw", "other": ["ItemLevel <= 65"], "type": "levelling rare normal"},
	"Hellion's Paw": {"base": "Hellion's Paw", "class": "Claw", "other": ["ItemLevel <= 67"], "type": "levelling rare normal"},
	"Eye Gouger": {"base": "Eye Gouger", "class": "Claw", "other": ["ItemLevel <= 69"], "type": "ignore"},
	"Vaal Claw": {"base": "Vaal Claw", "class": "Claw", "other": ["ItemLevel <= 71"], "type": "ignore"},
	"Imperial Claw": {"base": "Imperial Claw", "class": "Claw", "other": ["ItemLevel <= 73"], "type": "ignore"},
	"Terror Claw": {"base": "Terror Claw", "class": "Claw", "other": ["ItemLevel <= 75"], "type": "ignore"},
	"Gemini Claw": {"base": "Gemini Claw", "class": "Claw", "other": ["ItemLevel <= 77"], "type": "ignore"}
}
