#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Always show"

# Base type : settings pair
items = {
	"0 Leaguestone": {"class": "Leaguestone", "type": "challenge normal"},
	"01 Tabula Exception": {"base": "Simple Robe", "other": ["Rarity Unique", "SocketGroup WWWWWW"], "type": "unique high"},
	"02 6L": {"other": ["LinkedSockets 6"], "type": "show very high"},
	"03 6S": {"other": ["Sockets 6", 'CustomAlertSound "45_show.wav"'], "type": "show high"},
	"04 5L": {"other": ["Rarity < Unique", "LinkedSockets 5", 'CustomAlertSound "300_5link.wav"'], "type": "show high"},
	"04 Incursion Item": {"other": ['CustomAlertSound "45_show.wav"'], "class": "Incursion Item", "type": "show high"},
	"04 Timeworn Reliquary Key": {"base": "Timeworn Reliquary Key", "class": "Misc Map Items", "type": "map very good"},
	# High value atlas bases.  Show and make noise at any rarity
	"0 Fishing Rod": {"base": "Fishing Rod", "type": "show very high"},
	"0 Hideout Doodads": {"class": "Hideout Doodads", "type": "show low"},
	"0 Microtransactions": {"class": "Microtransactions", "type": "show low"},
	"0 Quest": {"class": "Quest", "type": "quest"},

	"9 Starter weapon": {"other": ["Class Dagger Wand \"One Hand\" Bow Stave \"Two Hand\" Sceptre Claws", "ItemLevel < 2"], "type": "show normal"},
}
