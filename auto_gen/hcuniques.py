#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 03/26/2017(m/d/y) 23:12:49 UTC from "Hardcore" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique very high"},
	"0 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique very high"},
	"0 Blinder": {"base": "Blinder", "type": "unique very high"},
	"0 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"0 Citadel Bow": {"base": "Citadel Bow", "type": "unique very high"},
	"0 Close Helmet": {"base": "Close Helmet", "type": "unique very high"},
	"0 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique very high"},
	"0 Cutlass": {"base": "Cutlass", "type": "unique very high"},
	"0 Decimation Bow": {"base": "Decimation Bow", "type": "unique very high"},
	"0 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique very high"},
	"0 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique very high"},
	"0 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique very high"},
	"0 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique very high"},
	"0 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Granite Flask": {"base": "Granite Flask", "type": "unique very high"},
	"0 Imperial Claw": {"base": "Imperial Claw", "type": "unique very high"},
	"0 Maelström Staff": {"base": "Maelström Staff", "type": "unique very high"},
	"0 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Royal Burgonet": {"base": "Royal Burgonet", "type": "unique very high"},
	"0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique very high"},
	"0 Savant's Robe": {"base": "Savant's Robe", "type": "unique very high"},
	"0 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique very high"},
	"0 Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "type": "unique very high"},
	"0 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique very high"},
	"0 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique very high"},
	"0 Spine Bow": {"base": "Spine Bow", "type": "unique very high"},
	"0 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique very high"},
	"0 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique very high"},
	"0 Topaz Flask": {"base": "Topaz Flask", "type": "unique very high"},
	"0 Trapper Boots": {"base": "Trapper Boots", "type": "unique very high"},
	"0 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique very high"},
	"0 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique very high"},
	"0 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique very high"},
	"0 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique very high"},
	"1 Amethyst Ring": {"base": "Amethyst Ring", "type": "unique high"},
	"1 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique high"},
	"1 Basket Rapier": {"base": "Basket Rapier", "type": "unique high"},
	"1 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique high"},
	"1 Chain Belt": {"base": "Chain Belt", "type": "unique high"},
	"1 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique high"},
	"1 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique high"},
	"1 Elder Sword": {"base": "Elder Sword", "type": "unique high"},
	"1 Estoc": {"base": "Estoc", "type": "unique high"},
	"1 Gavel": {"base": "Gavel", "type": "unique high"},
	"1 Golden Plate": {"base": "Golden Plate", "type": "unique high"},
	"1 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"1 Highland Blade": {"base": "Highland Blade", "type": "unique high"},
	"1 Imperial Staff": {"base": "Imperial Staff", "type": "unique high"},
	"1 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique high"},
	"1 Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "type": "unique high"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"1 Laminated Kite Shield": {"base": "Laminated Kite Shield", "type": "unique high"},
	"1 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique high"},
	"1 Lathi": {"base": "Lathi", "type": "unique high"},
	"1 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique high"},
	"1 Necropolis Map": {"base": "Necropolis Map", "type": "unique high"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique high"},
	"1 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique high"},
	"1 Quartz Wand": {"base": "Quartz Wand", "type": "unique high"},
	"1 Reaver Sword": {"base": "Reaver Sword", "type": "unique high"},
	"1 Reef Map": {"base": "Reef Map", "type": "unique high"},
	"1 Regicide Mask": {"base": "Regicide Mask", "type": "unique high"},
	"1 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique high"},
	"1 Reinforced Tower Shield": {"base": "Reinforced Tower Shield", "type": "unique high"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique high"},
	"1 Royal Bow": {"base": "Royal Bow", "type": "unique high"},
	"1 Royal Staff": {"base": "Royal Staff", "type": "unique high"},
	"1 Ruby Flask": {"base": "Ruby Flask", "type": "unique high"},
	"1 Saintly Chainmail": {"base": "Saintly Chainmail", "type": "unique high"},
	"1 Samite Helmet": {"base": "Samite Helmet", "type": "unique high"},
	"1 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique high"},
	"1 Shadow Axe": {"base": "Shadow Axe", "type": "unique high"},
	"1 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique high"},
	"1 Short Bow": {"base": "Short Bow", "type": "unique high"},
	"1 Slink Boots": {"base": "Slink Boots", "type": "unique high"},
	"1 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique high"},
	"1 Steelhead": {"base": "Steelhead", "type": "unique high"},
	"1 Strand Map": {"base": "Strand Map", "type": "unique high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"1 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique high"},
	"1 Tornado Wand": {"base": "Tornado Wand", "type": "unique high"},
	"1 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique high"},
	"1 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique high"},
	"1 Vile Staff": {"base": "Vile Staff", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Coral Amulet": {"base": "Coral Amulet", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Crude Bow": {"base": "Crude Bow", "type": "unique special"},
	"6 Death Bow": {"base": "Death Bow", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Iron Ring": {"base": "Iron Ring", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Long Bow": {"base": "Long Bow", "type": "unique special"},
	"6 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"6 Plate Vest": {"base": "Plate Vest", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Simple Robe": {"base": "Simple Robe", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"7 Demon's Horn": {"base": "Demon's Horn", "type": "unique low"},
	"7 Imperial Bow": {"base": "Imperial Bow", "type": "unique low"},
	"7 Iron Hat": {"base": "Iron Hat", "type": "unique low"},
	"7 Quartz Flask": {"base": "Quartz Flask", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
