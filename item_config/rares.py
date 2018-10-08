#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "General Rares"

# Base type : settings pair
items = {
	# 'rare low' after this
	"7 5": {"other": ["DropLevel <= 5", "ItemLevel >= 15", "Rarity Rare"], "type": "rare low"},
	"7 10": {"other": ["DropLevel <= 10", "ItemLevel >= 20", "Rarity Rare"], "type": "rare low"},
	"7 15": {"other": ["DropLevel <= 15", "ItemLevel >= 25", "Rarity Rare"], "type": "rare low"},
	"7 20": {"other": ["DropLevel <= 20", "ItemLevel >= 30", "Rarity Rare"], "type": "rare low"},
	"7 25": {"other": ["DropLevel <= 25", "ItemLevel >= 35", "Rarity Rare"], "type": "rare low"},
	"7 30": {"other": ["DropLevel <= 30", "ItemLevel >= 40", "Rarity Rare"], "type": "rare low"},
	"7 35": {"other": ["DropLevel <= 35", "ItemLevel >= 45", "Rarity Rare"], "type": "rare low"},
	"7 40": {"other": ["DropLevel <= 40", "ItemLevel >= 50", "Rarity Rare"], "type": "rare low"},
	"7 45": {"other": ["DropLevel <= 45", "ItemLevel >= 55", "Rarity Rare"], "type": "rare low"},
	"7 50": {"other": ["DropLevel <= 50", "ItemLevel >= 60", "Rarity Rare"], "type": "rare low"},
	"7 55": {"other": ["DropLevel <= 55", "ItemLevel >= 65", "Rarity Rare"], "type": "rare low"},

	"8 Other rares": {"type": "rare normal"},
	"9 identified rares": {"other": ["Identified True", "Rarity Rare"], "type": "low"},

	# last items in the list because of their special icon that will show if any previous rare highlighting is chosen
	"8 Elder Item": {'other': ["ElderItem True"], "type": "rare low"},
	"8 Shaper Item": {'other': ["ShaperItem True"], "type": "rare low"}
}