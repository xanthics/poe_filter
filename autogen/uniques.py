#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 2016-06-10T23:46:15 PST from "Standard Uniques" data
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

desc = "Unique"

# Base type : settings pair
items = {
	"0 Golden Caligae": {"base": "Golden Caligae", "type": "unique very high"},
	"0 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique very high"},
	"0 Golden Bracers": {"base": "Golden Bracers", "type": "unique very high"},
	"0 Fishing Rod": {"base": "Fishing Rod", "type": "unique very high"},
	"0 Golden Wreath": {"base": "Golden Wreath", "type": "unique very high"},
	"0 Golden Obi": {"base": "Golden Obi", "type": "unique very high"},
	"0 Golden Mantle": {"base": "Golden Mantle", "type": "unique very high"},
	"0 Clutching Talisman": {"base": "Clutching Talisman", "type": "unique very high"},
	"0 Topaz Flask": {"base": "Topaz Flask", "type": "unique very high"},
	"0 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique very high"},
	"0 Golden Hoop": {"base": "Golden Hoop", "type": "unique very high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique very high"},
	"0 Golden Flame": {"base": "Golden Flame", "type": "unique very high"},
	"0 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique very high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique very high"},
	"0 Jet Amulet": {"base": "Jet Amulet", "type": "unique very high"},
	"0 Jasper Chopper": {"base": "Jasper Chopper", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Legion Gloves": {"base": "Legion Gloves", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique very high"},
	"0 Vaal Axe": {"base": "Vaal Axe", "type": "unique very high"},
	"0 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique very high"},
	"0 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"0 Silver Flask": {"base": "Silver Flask", "type": "unique very high"},
	"0 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique very high"},
	"0 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"0 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique very high"},
	"0 Midnight Blade": {"base": "Midnight Blade", "type": "unique very high"},
	"0 Royal Axe": {"base": "Royal Axe", "type": "unique very high"},
	"0 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique very high"},
	"0 Spine Bow": {"base": "Spine Bow", "type": "unique very high"},
	"0 Steelhead": {"base": "Steelhead", "type": "unique very high"},
	"0 Cedar Tower Shield": {"base": "Cedar Tower Shield", "type": "unique very high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique very high"},
	"0 Regicide Mask": {"base": "Regicide Mask", "type": "unique very high"},
	"0 Trapper Boots": {"base": "Trapper Boots", "type": "unique very high"},
	"0 Painted Tower Shield": {"base": "Painted Tower Shield", "type": "unique very high"},
	"0 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"0 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique very high"},
	"0 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique very high"},
	"0 Ancient Greaves": {"base": "Ancient Greaves", "type": "unique very high"},
	"0 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique very high"},
	"0 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique very high"},
	"0 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique very high"},
	"0 Despot Axe": {"base": "Despot Axe", "type": "unique very high"},
	"0 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique very high"},
	"0 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique very high"},
	"0 Gold Ring": {"base": "Gold Ring", "type": "unique very high"},
	"0 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique very high"},
	"0 Imperial Skean": {"base": "Imperial Skean", "type": "unique very high"},
	"0 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique very high"},
	"0 Judgement Staff": {"base": "Judgement Staff", "type": "unique very high"},
	"0 Paua Ring": {"base": "Paua Ring", "type": "unique very high"},
	"0 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique very high"},
	"0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique very high"},
	"0 Savant's Robe": {"base": "Savant's Robe", "type": "unique very high"},
	"0 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "unique very high"},
	"0 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique very high"},
	"0 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique very high"},
	"0 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique very high"},
	"0 Vaal Mask": {"base": "Vaal Mask", "type": "unique very high"},
	"0 Varnished Coat": {"base": "Varnished Coat", "type": "unique very high"},
	"0 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique very high"},
	"0 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique very high"},
	"1 Golden Plate": {"base": "Golden Plate", "type": "unique high"},
	"1 Unset Ring": {"base": "Unset Ring", "type": "unique high"},
	"1 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique high"},
	"1 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique high"},
	"1 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique high"},
	"1 Diamond Ring": {"base": "Diamond Ring", "type": "unique high"},
	"1 Crusader Plate": {"base": "Crusader Plate", "type": "unique high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"1 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique high"},
	"1 Reaver Sword": {"base": "Reaver Sword", "type": "unique high"},
	"1 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique high"},
	"1 Vaal Blade": {"base": "Vaal Blade", "type": "unique high"},
	"1 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique high"},
	"1 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique high"},
	"1 Enameled Buckler": {"base": "Enameled Buckler", "type": "unique high"},
	"1 Gladius": {"base": "Gladius", "type": "unique high"},
	"1 Heavy Quiver": {"base": "Heavy Quiver", "type": "unique high"},
	"1 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"1 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique high"},
	"1 Ranger Bow": {"base": "Ranger Bow", "type": "unique high"},
	"1 Raven Mask": {"base": "Raven Mask", "type": "unique high"},
	"1 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique high"},
	"1 Simple Robe": {"base": "Simple Robe", "type": "unique high"},
	"1 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique high"},
	"1 Imperial Bow": {"base": "Imperial Bow", "type": "unique high"},
	"1 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique high"},
	"1 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique high"},
	"1 Imperial Staff": {"base": "Imperial Staff", "type": "unique high"},
	"1 Vile Staff": {"base": "Vile Staff", "type": "unique high"},
	"1 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"1 Amethyst Ring": {"base": "Amethyst Ring", "type": "unique high"},
	"1 Goliath Gauntlets": {"base": "Goliath Gauntlets", "type": "unique high"},
	"1 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique high"},
	"1 Short Bow": {"base": "Short Bow", "type": "unique high"},
	"1 Terror Claw": {"base": "Terror Claw", "type": "unique high"},
	"1 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique high"},
	"1 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique high"},
	"1 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique high"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique high"},
	"1 Engraved Wand": {"base": "Engraved Wand", "type": "unique high"},
	"1 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique high"},
	"1 Opal Wand": {"base": "Opal Wand", "type": "unique high"},
	"1 Platinum Sceptre": {"base": "Platinum Sceptre", "type": "unique high"},
	"1 Reef Map": {"base": "Reef Map", "type": "unique high"},
	"1 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique high"},
	"1 Terror Maul": {"base": "Terror Maul", "type": "unique high"},
	"1 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique high"},
	"1 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique high"},
	"1 Elder Sword": {"base": "Elder Sword", "type": "unique high"},
	"1 Amber Amulet": {"base": "Amber Amulet", "type": "unique high"},
	"1 Astral Plate": {"base": "Astral Plate", "type": "unique high"},
	"1 Chain Belt": {"base": "Chain Belt", "type": "unique high"},
	"1 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique high"},
	"1 Demon's Horn": {"base": "Demon's Horn", "type": "unique high"},
	"1 Eternal Sword": {"base": "Eternal Sword", "type": "unique high"},
	"1 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique high"},
	"1 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"1 Heavy Belt": {"base": "Heavy Belt", "type": "unique high"},
	"1 Jagged Foil": {"base": "Jagged Foil", "type": "unique high"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"1 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique high"},
	"1 Legion Sword": {"base": "Legion Sword", "type": "unique high"},
	"1 Mind Cage": {"base": "Mind Cage", "type": "unique high"},
	"1 Murder Mitts": {"base": "Murder Mitts", "type": "unique high"},
	"1 Promenade Map": {"base": "Promenade Map", "type": "unique high"},
	"1 Ruby Flask": {"base": "Ruby Flask", "type": "unique high"},
	"1 Slink Boots": {"base": "Slink Boots", "type": "unique high"},
	"1 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique high"},
	"1 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"1 Vaal Hatchet": {"base": "Vaal Hatchet", "type": "unique high"},
	"1 Whalebone Rapier": {"base": "Whalebone Rapier", "type": "unique high"},
	"9 Other uniques": {"type": "unique normal"}
}
