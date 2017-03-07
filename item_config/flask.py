#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Flasks"

# Base type : settings pair
items = {
    "01 Qual Flask": {"base": "Flask", "other": ["Quality = 20", "Rarity Normal"], "type": "high"},
    "02 Qual Flask": {"base": "Flask", "other": ["Quality >= 10"], "type": "show normal"},
    "03 Qual Flask": {"base": "Flask", "other": ["Quality >= 1"], "type": "ignore"},
    "1 Diamond Flask": {"base": "Diamond Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Granite Flask": {"base": "Granite Flask", "other": ["Rarity Normal"], "type": "ignore"},
    "1 Jade Flask": {"base": "Jade Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Topaz Flask": {"base": "Topaz Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Sapphire Flask": {"base": "Sapphire Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Ruby Flask": {"base": "Ruby Flask", "other": ["Rarity Normal"], "type": "normal"},
    "11 Quicksilver Flask <= 25": {"base": "Quicksilver Flask", "other": ["ItemLevel <= 25"], "type": "normal"},
    "12 Quicksilver Flask": {"base": "Quicksilver Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Amethyst Flask": {"base": "Amethyst Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Basalt Flask": {"base": "Basalt Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Aquamarine Flask": {"base": "Aquamarine Flask", "other": ["Rarity Normal"], "type": "ignore"},
    "1 Stibnite Flask": {"base": "Stibnite Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Sulphur Flask": {"base": "Sulphur Flask", "other": ["Rarity Normal"], "type": "ignore"},
    "1 Silver Flask": {"base": "Silver Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Quartz Flask": {"base": "Quartz Flask", "other": ["Rarity Normal"], "type": "normal"},
    "1 Bismuth Flask": {"base": "Bismuth Flask", "other": ["Rarity Normal"], "type": "ignore"},

    "1 Small Flasks": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 0", "ItemLevel <= 3"], "type": "normal"},
    "1 Medium Flasks": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 3", "ItemLevel <= 6"], "type": "normal"},
    "1 Large Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 6", "ItemLevel <= 12"], "type": "normal"},
    "1 Greater Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 12", "ItemLevel <= 18"], "type": "normal"},
    "1 Grand Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 18", "ItemLevel <= 24"], "type": "normal"},
    "1 Giant Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 24", "ItemLevel <= 30"], "type": "normal"},
    "1 Colossal Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 30", "ItemLevel <= 36"], "type": "normal"},
    "1 Sacred Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 36", "ItemLevel <= 42"], "type": "normal"},
    "1 Hallowed Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 42", "ItemLevel <= 60"], "type": "normal"},
    "1 Sanctified Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 50", "ItemLevel <= 60"], "type": "ignore"},
    "1 Divine Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 60", "ItemLevel <= 65"], "type": "ignore"},
    "1 Eternal Flask": {"class": "Life Flasks\" \"Mana Flasks", "other": ["DropLevel = 65", "ItemLevel <= 70"], "type": "ignore"},

    "2 Small Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 10", "ItemLevel <= 20"], "type": "ignore"},
    "2 medium Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 20", "ItemLevel <= 30"], "type": "ignore"},
    "2 large Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 30", "ItemLevel <= 40"], "type": "ignore"},
    "2 Colossal Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 40", "ItemLevel <= 50"], "type": "ignore"},
    "2 Sacred Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 50", "ItemLevel <= 60"], "type": "ignore"},
    "2 Hallowed Flask": {"class": "Hybrid Flask", "other": ["DropLevel = 60", "ItemLevel <= 70"], "type": "ignore"},

    "9 Other Flasks": {"base": "Flask", "type": "ignore"}
}