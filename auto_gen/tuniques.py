#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/13/2018(m/d/y) 19:54:56 UTC from "tmpstandard" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Callous Mask": {"base": "Callous Mask", "type": "unique very high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique very high"},
	"0 Royal Axe": {"base": "Royal Axe", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"1 Ambush Mitts": {"base": "Ambush Mitts", "type": "unique high"},
	"1 Ancient Spirit Shield": {"base": "Ancient Spirit Shield", "type": "unique high"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique high"},
	"1 Assassin's Boots": {"base": "Assassin's Boots", "type": "unique high"},
	"1 Bismuth Flask": {"base": "Bismuth Flask", "type": "unique high"},
	"1 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique high"},
	"1 Blood Raiment": {"base": "Blood Raiment", "type": "unique high"},
	"1 Blunt Arrow Quiver Piece": {"base": "Blunt Arrow Quiver Piece", "type": "unique high"},
	"1 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique high"},
	"1 Carnal Boots": {"base": "Carnal Boots", "type": "unique high"},
	"1 Cloth Belt Piece": {"base": "Cloth Belt Piece", "type": "unique high"},
	"1 Clutching Talisman": {"base": "Clutching Talisman", "type": "unique high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique high"},
	"1 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique high"},
	"1 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique high"},
	"1 Harbinger Map": {"base": "Harbinger Map", "type": "unique high"},
	"1 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique high"},
	"1 Hydrascale Boots": {"base": "Hydrascale Boots", "type": "unique high"},
	"1 Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "type": "unique high"},
	"1 Legion Gloves": {"base": "Legion Gloves", "type": "unique high"},
	"1 Maze Map": {"base": "Maze Map", "type": "unique high"},
	"1 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique high"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique high"},
	"1 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique high"},
	"1 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique high"},
	"1 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique high"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique high"},
	"1 Riveted Gloves": {"base": "Riveted Gloves", "type": "unique high"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique high"},
	"1 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique high"},
	"1 Shackled Boots": {"base": "Shackled Boots", "type": "unique high"},
	"1 Shore Map": {"base": "Shore Map", "type": "unique high"},
	"1 Siege Axe": {"base": "Siege Axe", "type": "unique high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"1 Variscite Blade": {"base": "Variscite Blade", "type": "unique high"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Ancient Greaves": {"base": "Ancient Greaves", "type": "unique special"},
	"6 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique special"},
	"6 Archon Kite Shield Piece": {"base": "Archon Kite Shield Piece", "type": "unique special"},
	"6 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique special"},
	"6 Bone Bow": {"base": "Bone Bow", "type": "unique special"},
	"6 Carnal Armour": {"base": "Carnal Armour", "type": "unique special"},
	"6 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"6 Citadel Bow": {"base": "Citadel Bow", "type": "unique special"},
	"6 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique special"},
	"6 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Coronal Leather": {"base": "Coronal Leather", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Cutlass": {"base": "Cutlass", "type": "unique special"},
	"6 Despot Axe": {"base": "Despot Axe", "type": "unique special"},
	"6 Diamond Ring": {"base": "Diamond Ring", "type": "unique special"},
	"6 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"6 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique special"},
	"6 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique special"},
	"6 Gavel": {"base": "Gavel", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Golden Plate": {"base": "Golden Plate", "type": "unique special"},
	"6 Goliath Greaves": {"base": "Goliath Greaves", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Great Mallet": {"base": "Great Mallet", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique special"},
	"6 Imperial Bow": {"base": "Imperial Bow", "type": "unique special"},
	"6 Imperial Claw": {"base": "Imperial Claw", "type": "unique special"},
	"6 Imperial Staff": {"base": "Imperial Staff", "type": "unique special"},
	"6 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"6 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Labrys": {"base": "Labrys", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Maelström Staff": {"base": "Maelström Staff", "type": "unique special"},
	"6 Midnight Blade": {"base": "Midnight Blade", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Murder Boots": {"base": "Murder Boots", "type": "unique special"},
	"6 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique special"},
	"6 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"6 Opal Ring": {"base": "Opal Ring", "type": "unique special"},
	"6 Painted Tower Shield": {"base": "Painted Tower Shield", "type": "unique special"},
	"6 Paua Amulet": {"base": "Paua Amulet", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Quartz Flask": {"base": "Quartz Flask", "type": "unique special"},
	"6 Ruby Flask": {"base": "Ruby Flask", "type": "unique special"},
	"6 Ruby Ring": {"base": "Ruby Ring", "type": "unique special"},
	"6 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"6 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique special"},
	"6 Sadist Garb": {"base": "Sadist Garb", "type": "unique special"},
	"6 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique special"},
	"6 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique special"},
	"6 Silken Hood": {"base": "Silken Hood", "type": "unique special"},
	"6 Simple Robe": {"base": "Simple Robe", "type": "unique special"},
	"6 Slink Boots": {"base": "Slink Boots", "type": "unique special"},
	"6 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique special"},
	"6 Spine Bow": {"base": "Spine Bow", "type": "unique special"},
	"6 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique special"},
	"6 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique special"},
	"6 Stygian Vise": {"base": "Stygian Vise", "type": "unique special"},
	"6 Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "type": "unique special"},
	"6 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique special"},
	"6 Titan Greaves": {"base": "Titan Greaves", "type": "unique special"},
	"6 Topaz Ring": {"base": "Topaz Ring", "type": "unique special"},
	"6 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Axe": {"base": "Vaal Axe", "type": "unique special"},
	"6 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"6 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique special"},
	"6 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique special"},
	"6 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique special"},
	"6 Zealot Gloves": {"base": "Zealot Gloves", "type": "unique special"},
	"6 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique special"},
	"7 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique low"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Boot Blade": {"base": "Boot Blade", "type": "unique low"},
	"7 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"7 Bronze Gauntlets": {"base": "Bronze Gauntlets", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Coral Amulet": {"base": "Coral Amulet", "type": "unique low"},
	"7 Death Bow": {"base": "Death Bow", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Iron Staff": {"base": "Iron Staff", "type": "unique low"},
	"7 Long Staff": {"base": "Long Staff", "type": "unique low"},
	"7 Plate Vest": {"base": "Plate Vest", "type": "unique low"},
	"7 Plated Greaves": {"base": "Plated Greaves", "type": "unique low"},
	"7 Platinum Kris": {"base": "Platinum Kris", "type": "unique low"},
	"7 Prophet Crown": {"base": "Prophet Crown", "type": "unique low"},
	"7 Recurve Bow": {"base": "Recurve Bow", "type": "unique low"},
	"7 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique low"},
	"7 Shagreen Boots": {"base": "Shagreen Boots", "type": "unique low"},
	"7 Skinning Knife": {"base": "Skinning Knife", "type": "unique low"},
	"7 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"7 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique low"},
	"7 Stiletto": {"base": "Stiletto", "type": "unique low"},
	"7 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique low"},
	"7 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique low"},
	"7 Vine Circlet": {"base": "Vine Circlet", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
