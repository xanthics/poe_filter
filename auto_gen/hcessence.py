#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 03/06/2018(m/d/y) 07:42:55 UTC from "Hardcore" data

desc = "Essence Autogen"

# Base type : settings pair
items = {
	"0 Deafening Essence of Doubt": {"base": "Deafening Essence of Doubt", "class": "Currency", "type": "currency very high"},
	"0 Deafening Essence of Dread": {"base": "Deafening Essence of Dread", "class": "Currency", "type": "currency very high"},
	"0 Deafening Essence of Fear": {"base": "Deafening Essence of Fear", "class": "Currency", "type": "currency normal"},
	"0 Deafening Essence of Greed": {"base": "Deafening Essence of Greed", "class": "Currency", "type": "currency very high"},
	"0 Deafening Essence of Suffering": {"base": "Deafening Essence of Suffering", "class": "Currency", "type": "currency very high"},
	"0 Deafening Essence of Torment": {"base": "Deafening Essence of Torment", "class": "Currency", "type": "currency very high"},
	"0 Deafening Essence of Woe": {"base": "Deafening Essence of Woe", "class": "Currency", "type": "currency very high"},
	"0 Essence of Horror": {"base": "Essence of Horror", "class": "Currency", "type": "currency very high"},
	"0 Essence of Hysteria": {"base": "Essence of Hysteria", "class": "Currency", "type": "currency very high"},
	"0 Essence of Insanity": {"base": "Essence of Insanity", "class": "Currency", "type": "currency very high"},
	"0 Muttering Essence of Anger": {"base": "Muttering Essence of Anger", "class": "Currency", "type": "currency normal"},
	"0 Muttering Essence of Sorrow": {"base": "Muttering Essence of Sorrow", "class": "Currency", "type": "currency very high"},
	"0 Muttering Essence of Torment": {"base": "Muttering Essence of Torment", "class": "Currency", "type": "currency very high"},
	"0 Remnant of Corruption": {"base": "Remnant of Corruption", "class": "Currency", "type": "currency normal"},
	"0 Screaming Essence of Anger": {"base": "Screaming Essence of Anger", "class": "Currency", "type": "currency normal"},
	"0 Screaming Essence of Anguish": {"base": "Screaming Essence of Anguish", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Contempt": {"base": "Screaming Essence of Contempt", "class": "Currency", "type": "currency normal"},
	"0 Screaming Essence of Dread": {"base": "Screaming Essence of Dread", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Fear": {"base": "Screaming Essence of Fear", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Greed": {"base": "Screaming Essence of Greed", "class": "Currency", "type": "currency normal"},
	"0 Screaming Essence of Misery": {"base": "Screaming Essence of Misery", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Rage": {"base": "Screaming Essence of Rage", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Scorn": {"base": "Screaming Essence of Scorn", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Sorrow": {"base": "Screaming Essence of Sorrow", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Spite": {"base": "Screaming Essence of Spite", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Suffering": {"base": "Screaming Essence of Suffering", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Torment": {"base": "Screaming Essence of Torment", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Woe": {"base": "Screaming Essence of Woe", "class": "Currency", "type": "currency very high"},
	"0 Screaming Essence of Zeal": {"base": "Screaming Essence of Zeal", "class": "Currency", "type": "currency very high"},
	"0 Shrieking Essence of Misery": {"base": "Shrieking Essence of Misery", "class": "Currency", "type": "currency very high"},
	"0 Shrieking Essence of Spite": {"base": "Shrieking Essence of Spite", "class": "Currency", "type": "currency normal"},
	"0 Shrieking Essence of Wrath": {"base": "Shrieking Essence of Wrath", "class": "Currency", "type": "currency normal"},
	"0 Wailing Essence of Anguish": {"base": "Wailing Essence of Anguish", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Contempt": {"base": "Wailing Essence of Contempt", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Doubt": {"base": "Wailing Essence of Doubt", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Fear": {"base": "Wailing Essence of Fear", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Greed": {"base": "Wailing Essence of Greed", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Loathing": {"base": "Wailing Essence of Loathing", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Rage": {"base": "Wailing Essence of Rage", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Sorrow": {"base": "Wailing Essence of Sorrow", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Spite": {"base": "Wailing Essence of Spite", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Suffering": {"base": "Wailing Essence of Suffering", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Torment": {"base": "Wailing Essence of Torment", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Woe": {"base": "Wailing Essence of Woe", "class": "Currency", "type": "currency very high"},
	"0 Wailing Essence of Zeal": {"base": "Wailing Essence of Zeal", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Anger": {"base": "Weeping Essence of Anger", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Doubt": {"base": "Weeping Essence of Doubt", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Fear": {"base": "Weeping Essence of Fear", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Greed": {"base": "Weeping Essence of Greed", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Hatred": {"base": "Weeping Essence of Hatred", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Rage": {"base": "Weeping Essence of Rage", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Sorrow": {"base": "Weeping Essence of Sorrow", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Torment": {"base": "Weeping Essence of Torment", "class": "Currency", "type": "currency very high"},
	"0 Weeping Essence of Wrath": {"base": "Weeping Essence of Wrath", "class": "Currency", "type": "currency very high"},
	"7 Essence default": {"base": "Essence", "class": "Currency", "type": "currency low"}}
