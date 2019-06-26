#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 06/26/2019(m/d/y) 01:03:57 UTC from "tmpstandard" data

desc = "Prophecy Autogen"

# Base type : settings pair
items = {
	"000 Thaumaturgical History III": {"prophecy": "Thaumaturgical History III", "class": "Currency", "type": "currency low"},
	"001 Thaumaturgical History IV": {"prophecy": "Thaumaturgical History IV", "class": "Currency", "type": "currency low"},
	"002 Thaumaturgical History II": {"prophecy": "Thaumaturgical History II", "class": "Currency", "type": "currency low"},
	"003 The Unbreathing Queen III": {"prophecy": "The Unbreathing Queen III", "class": "Currency", "type": "currency low"},
	"004 The Unbreathing Queen IV": {"prophecy": "The Unbreathing Queen IV", "class": "Currency", "type": "currency low"},
	"005 The Ambitious Bandit III": {"prophecy": "The Ambitious Bandit III", "class": "Currency", "type": "currency low"},
	"006 The Unbreathing Queen II": {"prophecy": "The Unbreathing Queen II", "class": "Currency", "type": "currency low"},
	"007 The Ambitious Bandit II": {"prophecy": "The Ambitious Bandit II", "class": "Currency", "type": "currency low"},
	"008 Unbearable Whispers III": {"prophecy": "Unbearable Whispers III", "class": "Currency", "type": "currency low"},
	"009 Unbearable Whispers IV": {"prophecy": "Unbearable Whispers IV", "class": "Currency", "type": "currency low"},
	"010 Unbearable Whispers II": {"prophecy": "Unbearable Whispers II", "class": "Currency", "type": "currency low"},
	"011 Day of Sacrifice III": {"prophecy": "Day of Sacrifice III", "class": "Currency", "type": "currency low"},
	"012 Day of Sacrifice IV": {"prophecy": "Day of Sacrifice IV", "class": "Currency", "type": "currency low"},
	"013 Day of Sacrifice II": {"prophecy": "Day of Sacrifice II", "class": "Currency", "type": "currency low"},
	"014 Deadly Rivalry III": {"prophecy": "Deadly Rivalry III", "class": "Currency", "type": "currency low"},
	"015 The Feral Lord III": {"prophecy": "The Feral Lord III", "class": "Currency", "type": "currency low"},
	"016 The Warmongers III": {"prophecy": "The Warmongers III", "class": "Currency", "type": "currency low"},
	"017 Anarchy's End III": {"prophecy": "Anarchy's End III", "class": "Currency", "type": "currency low"},
	"018 Deadly Rivalry II": {"prophecy": "Deadly Rivalry II", "class": "Currency", "type": "currency low"},
	"019 The Warmongers II": {"prophecy": "The Warmongers II", "class": "Currency", "type": "currency low"},
	"020 The Feral Lord IV": {"prophecy": "The Feral Lord IV", "class": "Currency", "type": "currency low"},
	"021 The Warmongers IV": {"prophecy": "The Warmongers IV", "class": "Currency", "type": "currency low"},
	"022 The Plaguemaw III": {"prophecy": "The Plaguemaw III", "class": "Currency", "type": "currency low"},
	"023 The Feral Lord II": {"prophecy": "The Feral Lord II", "class": "Currency", "type": "currency low"},
	"024 Deadly Rivalry IV": {"prophecy": "Deadly Rivalry IV", "class": "Currency", "type": "currency low"},
	"025 The Plaguemaw IV": {"prophecy": "The Plaguemaw IV", "class": "Currency", "type": "currency low"},
	"026 Beyond Sight III": {"prophecy": "Beyond Sight III", "class": "Currency", "type": "currency low"},
	"027 The Plaguemaw II": {"prophecy": "The Plaguemaw II", "class": "Currency", "type": "currency low"},
	"028 Anarchy's End IV": {"prophecy": "Anarchy's End IV", "class": "Currency", "type": "currency low"},
	"029 Anarchy's End II": {"prophecy": "Anarchy's End II", "class": "Currency", "type": "currency low"},
	"030 Beyond Sight II": {"prophecy": "Beyond Sight II", "class": "Currency", "type": "currency low"},
	"031 Beyond Sight IV": {"prophecy": "Beyond Sight IV", "class": "Currency", "type": "currency low"},
	"1 A Prodigious Hand": {"prophecy": "A Prodigious Hand", "class": "Currency", "type": "currency high"},
	"1 A Vision of Ice and Fire": {"prophecy": "A Vision of Ice and Fire", "class": "Currency", "type": "currency high"},
	"1 Ancient Doom": {"prophecy": "Ancient Doom", "class": "Currency", "type": "currency high"},
	"1 Battle Hardened": {"prophecy": "Battle Hardened", "class": "Currency", "type": "currency high"},
	"1 Blinding Light": {"prophecy": "Blinding Light", "class": "Currency", "type": "currency high"},
	"1 Bountiful Traps": {"prophecy": "Bountiful Traps", "class": "Currency", "type": "currency high"},
	"1 Cleanser of Sins": {"prophecy": "Cleanser of Sins", "class": "Currency", "type": "currency high"},
	"1 Fated Connections": {"prophecy": "Fated Connections", "class": "Currency", "type": "currency extremely high"},
	"1 Fire, Wood and Stone": {"prophecy": "Fire, Wood and Stone", "class": "Currency", "type": "currency high"},
	"1 Flesh of the Beast": {"prophecy": "Flesh of the Beast", "class": "Currency", "type": "currency high"},
	"1 Gilded Within": {"prophecy": "Gilded Within", "class": "Currency", "type": "currency very low"},
	"1 Ice from Above": {"prophecy": "Ice from Above", "class": "Currency", "type": "currency high"},
	"1 Kalandra's Craft": {"prophecy": "Kalandra's Craft", "class": "Currency", "type": "currency high"},
	"1 Lightning Falls": {"prophecy": "Lightning Falls", "class": "Currency", "type": "currency high"},
	"1 Lost in the Pages": {"prophecy": "Lost in the Pages", "class": "Currency", "type": "currency high"},
	"1 Monstrous Treasure": {"prophecy": "Monstrous Treasure", "class": "Currency", "type": "currency very high"},
	"1 Pleasure and Pain": {"prophecy": "Pleasure and Pain", "class": "Currency", "type": "currency very low"},
	"1 Reforged Bonds": {"prophecy": "Reforged Bonds", "class": "Currency", "type": "currency high"},
	"1 Severed Limbs": {"prophecy": "Severed Limbs", "class": "Currency", "type": "currency high"},
	"1 The Apex Predator": {"prophecy": "The Apex Predator", "class": "Currency", "type": "currency high"},
	"1 The Bowstring's Music": {"prophecy": "The Bowstring's Music", "class": "Currency", "type": "currency high"},
	"1 The Brothers of Necromancy": {"prophecy": "The Brothers of Necromancy", "class": "Currency", "type": "currency very low"},
	"1 The Feral Lord V": {"prophecy": "The Feral Lord V", "class": "Currency", "type": "currency high"},
	"1 The Great Leader of the North": {"prophecy": "The Great Leader of the North", "class": "Currency", "type": "currency very high"},
	"1 The Great Mind of the North": {"prophecy": "The Great Mind of the North", "class": "Currency", "type": "currency very high"},
	"1 The Jeweller's Touch": {"prophecy": "The Jeweller's Touch", "class": "Currency", "type": "currency very high"},
	"1 The Karui Rebellion": {"prophecy": "The Karui Rebellion", "class": "Currency", "type": "currency high"},
	"1 The Malevolent Witch": {"prophecy": "The Malevolent Witch", "class": "Currency", "type": "currency very high"},
	"1 The Nightmare Awakens": {"prophecy": "The Nightmare Awakens", "class": "Currency", "type": "currency high"},
	"1 The Plaguemaw V": {"prophecy": "The Plaguemaw V", "class": "Currency", "type": "currency high"},
	"1 The Queen's Sacrifice": {"prophecy": "The Queen's Sacrifice", "class": "Currency", "type": "currency extremely high"},
	"1 The Queen's Vaults": {"prophecy": "The Queen's Vaults", "class": "Currency", "type": "currency high"},
	"1 The Silverwood": {"prophecy": "The Silverwood", "class": "Currency", "type": "currency high"},
	"1 The Unbreathing Queen V": {"prophecy": "The Unbreathing Queen V", "class": "Currency", "type": "currency high"},
	"1 The Undead Storm": {"prophecy": "The Undead Storm", "class": "Currency", "type": "currency high"},
	"1 Trash to Treasure": {"prophecy": "Trash to Treasure", "class": "Currency", "type": "currency extremely high"},
	"1 Twice Enchanted": {"prophecy": "Twice Enchanted", "class": "Currency", "type": "currency high"},
	"1 Unbearable Whispers V": {"prophecy": "Unbearable Whispers V", "class": "Currency", "type": "currency high"},
	"1 Vaal Winds": {"prophecy": "Vaal Winds", "class": "Currency", "type": "currency high"},
	"1 Wind and Thunder": {"prophecy": "Wind and Thunder", "class": "Currency", "type": "currency very high"},
	"7 Prophecy default": {"Prophecy": "", "class": "Currency", "type": "currency low"}
}
