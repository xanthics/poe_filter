#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/10/2018(m/d/y) 22:08:11 UTC from "Standard" data

desc = "Unique"

# Base type : settings pair
items = {
	"000 Archon Kite Shield Piece": {"base": "Archon Kite Shield Piece", "type": "unique high"},
	"001 Blunt Arrow Quiver Piece": {"base": "Blunt Arrow Quiver Piece", "type": "unique special"},
	"002 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique very high"},
	"003 Cloth Belt Piece": {"base": "Cloth Belt Piece", "type": "unique special"},
	"004 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique normal"},
	"005 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique very high"},
	"1 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique high"},
	"1 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"1 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"1 Ambush Mitts": {"base": "Ambush Mitts", "type": "unique extremely high"},
	"1 Ambusher": {"base": "Ambusher", "type": "unique low"},
	"1 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique high"},
	"1 Ancient Spirit Shield": {"base": "Ancient Spirit Shield", "type": "unique high"},
	"1 Antique Rapier": {"base": "Antique Rapier", "type": "unique low"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique very high"},
	"1 Arcanist Slippers": {"base": "Arcanist Slippers", "type": "unique very high"},
	"1 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique special"},
	"1 Assassin Bow": {"base": "Assassin Bow", "type": "unique special"},
	"1 Assassin's Boots": {"base": "Assassin's Boots", "type": "unique extremely high"},
	"1 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique low"},
	"1 Astral Plate": {"base": "Astral Plate", "type": "unique high"},
	"1 Aventail Helmet": {"base": "Aventail Helmet", "type": "unique low"},
	"1 Awl": {"base": "Awl", "type": "unique low"},
	"1 Baroque Round Shield": {"base": "Baroque Round Shield", "type": "unique low"},
	"1 Basket Rapier": {"base": "Basket Rapier", "type": "unique low"},
	"1 Bastard Sword": {"base": "Bastard Sword", "type": "unique low"},
	"1 Bismuth Flask": {"base": "Bismuth Flask", "type": "unique high"},
	"1 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique high"},
	"1 Blood Raiment": {"base": "Blood Raiment", "type": "unique very high"},
	"1 Blood Sceptre": {"base": "Blood Sceptre", "type": "unique very high"},
	"1 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique special"},
	"1 Bone Armour": {"base": "Bone Armour", "type": "unique high"},
	"1 Bone Circlet": {"base": "Bone Circlet", "type": "unique low"},
	"1 Bone Crypt Map": {"base": "Bone Crypt Map", "type": "unique high"},
	"1 Boot Blade": {"base": "Boot Blade", "type": "unique low"},
	"1 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"1 Brass Maul": {"base": "Brass Maul", "type": "unique low"},
	"1 Bronze Gauntlets": {"base": "Bronze Gauntlets", "type": "unique low"},
	"1 Bronze Sceptre": {"base": "Bronze Sceptre", "type": "unique low"},
	"1 Bronzescale Boots": {"base": "Bronzescale Boots", "type": "unique low"},
	"1 Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "type": "unique low"},
	"1 Buckskin Tunic": {"base": "Buckskin Tunic", "type": "unique low"},
	"1 Burnished Spiked Shield": {"base": "Burnished Spiked Shield", "type": "unique low"},
	"1 Callous Mask": {"base": "Callous Mask", "type": "unique extremely high"},
	"1 Cardinal Round Shield": {"base": "Cardinal Round Shield", "type": "unique high"},
	"1 Carnal Armour": {"base": "Carnal Armour", "type": "unique special"},
	"1 Carnal Boots": {"base": "Carnal Boots", "type": "unique extremely high"},
	"1 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique special"},
	"1 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"1 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"1 Cedar Tower Shield": {"base": "Cedar Tower Shield", "type": "unique high"},
	"1 Cemetery Map": {"base": "Cemetery Map", "type": "unique high"},
	"1 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"1 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"1 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique high"},
	"1 Chateau Map": {"base": "Chateau Map", "type": "unique extremely high"},
	"1 Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "type": "unique low"},
	"1 Citadel Bow": {"base": "Citadel Bow", "type": "unique high"},
	"1 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique special"},
	"1 Clasped Boots": {"base": "Clasped Boots", "type": "unique low"},
	"1 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"1 Cleaver": {"base": "Cleaver", "type": "unique low"},
	"1 Close Helmet": {"base": "Close Helmet", "type": "unique high"},
	"1 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"1 Clutching Talisman": {"base": "Clutching Talisman", "type": "unique very high"},
	"1 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"1 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"1 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique high"},
	"1 Conquest Chainmail": {"base": "Conquest Chainmail", "type": "unique low"},
	"1 Copper Plate": {"base": "Copper Plate", "type": "unique low"},
	"1 Coral Amulet": {"base": "Coral Amulet", "type": "unique special"},
	"1 Corsair Sword": {"base": "Corsair Sword", "type": "unique high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"1 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"1 Crude Bow": {"base": "Crude Bow", "type": "unique low"},
	"1 Crusader Boots": {"base": "Crusader Boots", "type": "unique extremely high"},
	"1 Crusader Chainmail": {"base": "Crusader Chainmail", "type": "unique low"},
	"1 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique special"},
	"1 Crusader Helmet": {"base": "Crusader Helmet", "type": "unique high"},
	"1 Crystal Belt": {"base": "Crystal Belt", "type": "unique high"},
	"1 Crystal Sceptre": {"base": "Crystal Sceptre", "type": "unique low"},
	"1 Crystal Wand": {"base": "Crystal Wand", "type": "unique low"},
	"1 Cured Quiver": {"base": "Cured Quiver", "type": "unique very high"},
	"1 Cursed Crypt Map": {"base": "Cursed Crypt Map", "type": "unique high"},
	"1 Cutlass": {"base": "Cutlass", "type": "unique special"},
	"1 Death Bow": {"base": "Death Bow", "type": "unique low"},
	"1 Decimation Bow": {"base": "Decimation Bow", "type": "unique low"},
	"1 Decorative Axe": {"base": "Decorative Axe", "type": "unique low"},
	"1 Deerskin Boots": {"base": "Deerskin Boots", "type": "unique low"},
	"1 Deicide Mask": {"base": "Deicide Mask", "type": "unique high"},
	"1 Demon's Horn": {"base": "Demon's Horn", "type": "unique low"},
	"1 Despot Axe": {"base": "Despot Axe", "type": "unique special"},
	"1 Destiny Leather": {"base": "Destiny Leather", "type": "unique high"},
	"1 Destroyer Regalia": {"base": "Destroyer Regalia", "type": "unique high"},
	"1 Dragonscale Boots": {"base": "Dragonscale Boots", "type": "unique low"},
	"1 Dragonscale Gauntlets": {"base": "Dragonscale Gauntlets", "type": "unique special"},
	"1 Dread Maul": {"base": "Dread Maul", "type": "unique low"},
	"1 Dream Mace": {"base": "Dream Mace", "type": "unique low"},
	"1 Dunes Map": {"base": "Dunes Map", "type": "unique high"},
	"1 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"1 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique special"},
	"1 Elegant Sword": {"base": "Elegant Sword", "type": "unique special"},
	"1 Enameled Buckler": {"base": "Enameled Buckler", "type": "unique low"},
	"1 Estoc": {"base": "Estoc", "type": "unique low"},
	"1 Eternal Sword": {"base": "Eternal Sword", "type": "unique special"},
	"1 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique high"},
	"1 Ezomyte Axe": {"base": "Ezomyte Axe", "type": "unique low"},
	"1 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique low"},
	"1 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique high"},
	"1 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique special"},
	"1 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique very high"},
	"1 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique low"},
	"1 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique low"},
	"1 Flaying Knife": {"base": "Flaying Knife", "type": "unique low"},
	"1 Fright Claw": {"base": "Fright Claw", "type": "unique low"},
	"1 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique high"},
	"1 Gavel": {"base": "Gavel", "type": "unique special"},
	"1 Gemstone Sword": {"base": "Gemstone Sword", "type": "unique very high"},
	"1 Gilded Sallet": {"base": "Gilded Sallet", "type": "unique low"},
	"1 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique high"},
	"1 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"1 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"1 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"1 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"1 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"1 Gold Ring": {"base": "Gold Ring", "type": "unique high"},
	"1 Golden Bracers": {"base": "Golden Bracers", "type": "unique extremely high"},
	"1 Golden Buckler": {"base": "Golden Buckler", "type": "unique low"},
	"1 Golden Hoop": {"base": "Golden Hoop", "type": "unique extremely high"},
	"1 Golden Mantle": {"base": "Golden Mantle", "type": "unique extremely high"},
	"1 Golden Mask": {"base": "Golden Mask", "type": "unique low"},
	"1 Golden Obi": {"base": "Golden Obi", "type": "unique extremely high"},
	"1 Golden Plate": {"base": "Golden Plate", "type": "unique special"},
	"1 Golden Wreath": {"base": "Golden Wreath", "type": "unique extremely high"},
	"1 Goliath Greaves": {"base": "Goliath Greaves", "type": "unique special"},
	"1 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique very high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique special"},
	"1 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"1 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"1 Great Mallet": {"base": "Great Mallet", "type": "unique low"},
	"1 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique low"},
	"1 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique extremely high"},
	"1 Grinning Fetish": {"base": "Grinning Fetish", "type": "unique low"},
	"1 Gut Ripper": {"base": "Gut Ripper", "type": "unique low"},
	"1 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"1 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique low"},
	"1 Harbinger Map": {"base": "Harbinger Map", "type": "unique very high"},
	"1 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique extremely high"},
	"1 Headsman Axe": {"base": "Headsman Axe", "type": "unique low"},
	"1 Heavy Belt": {"base": "Heavy Belt", "type": "unique low"},
	"1 Heavy Quiver": {"base": "Heavy Quiver", "type": "unique extremely high"},
	"1 Hellion's Paw": {"base": "Hellion's Paw", "type": "unique high"},
	"1 Highborn Staff": {"base": "Highborn Staff", "type": "unique high"},
	"1 Highland Blade": {"base": "Highland Blade", "type": "unique low"},
	"1 Holy Chainmail": {"base": "Holy Chainmail", "type": "unique low"},
	"1 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique special"},
	"1 Hydrascale Boots": {"base": "Hydrascale Boots", "type": "unique very high"},
	"1 Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "type": "unique extremely high"},
	"1 Imbued Wand": {"base": "Imbued Wand", "type": "unique low"},
	"1 Imperial Bow": {"base": "Imperial Bow", "type": "unique special"},
	"1 Imperial Maul": {"base": "Imperial Maul", "type": "unique very high"},
	"1 Imperial Skean": {"base": "Imperial Skean", "type": "unique low"},
	"1 Imperial Staff": {"base": "Imperial Staff", "type": "unique high"},
	"1 Infernal Axe": {"base": "Infernal Axe", "type": "unique low"},
	"1 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"1 Iron Circlet": {"base": "Iron Circlet", "type": "unique low"},
	"1 Iron Hat": {"base": "Iron Hat", "type": "unique low"},
	"1 Iron Mask": {"base": "Iron Mask", "type": "unique low"},
	"1 Iron Staff": {"base": "Iron Staff", "type": "unique low"},
	"1 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"1 Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "type": "unique low"},
	"1 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"1 Jade Hatchet": {"base": "Jade Hatchet", "type": "unique low"},
	"1 Jagged Foil": {"base": "Jagged Foil", "type": "unique low"},
	"1 Jagged Maul": {"base": "Jagged Maul", "type": "unique low"},
	"1 Jasper Chopper": {"base": "Jasper Chopper", "type": "unique high"},
	"1 Jet Amulet": {"base": "Jet Amulet", "type": "unique extremely high"},
	"1 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"1 Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "type": "unique high"},
	"1 Judgement Staff": {"base": "Judgement Staff", "type": "unique special"},
	"1 Karui Chopper": {"base": "Karui Chopper", "type": "unique low"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique low"},
	"1 Labrys": {"base": "Labrys", "type": "unique high"},
	"1 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique special"},
	"1 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"1 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique special"},
	"1 Lathi": {"base": "Lathi", "type": "unique low"},
	"1 Latticed Ringmail": {"base": "Latticed Ringmail", "type": "unique low"},
	"1 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"1 Leather Hood": {"base": "Leather Hood", "type": "unique low"},
	"1 Leatherscale Boots": {"base": "Leatherscale Boots", "type": "unique high"},
	"1 Legion Boots": {"base": "Legion Boots", "type": "unique low"},
	"1 Legion Gloves": {"base": "Legion Gloves", "type": "unique extremely high"},
	"1 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"1 Lion Pelt": {"base": "Lion Pelt", "type": "unique high"},
	"1 Long Bow": {"base": "Long Bow", "type": "unique low"},
	"1 Long Staff": {"base": "Long Staff", "type": "unique low"},
	"1 Lunaris Circlet": {"base": "Lunaris Circlet", "type": "unique low"},
	"1 Maelström Staff": {"base": "Maelström Staff", "type": "unique special"},
	"1 Magistrate Crown": {"base": "Magistrate Crown", "type": "unique very high"},
	"1 Maze Map": {"base": "Maze Map", "type": "unique extremely high"},
	"1 Mesh Boots": {"base": "Mesh Boots", "type": "unique low"},
	"1 Midnight Blade": {"base": "Midnight Blade", "type": "unique special"},
	"1 Military Staff": {"base": "Military Staff", "type": "unique low"},
	"1 Mind Cage": {"base": "Mind Cage", "type": "unique low"},
	"1 Mirrored Spiked Shield": {"base": "Mirrored Spiked Shield", "type": "unique low"},
	"1 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"1 Murder Boots": {"base": "Murder Boots", "type": "unique special"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique very high"},
	"1 Nailed Fist": {"base": "Nailed Fist", "type": "unique low"},
	"1 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique special"},
	"1 Necropolis Map": {"base": "Necropolis Map", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Nightmare Mace": {"base": "Nightmare Mace", "type": "unique very high"},
	"1 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique high"},
	"1 Nubuck Gloves": {"base": "Nubuck Gloves", "type": "unique very high"},
	"1 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique special"},
	"1 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"1 Opal Ring": {"base": "Opal Ring", "type": "unique special"},
	"1 Ornate Mace": {"base": "Ornate Mace", "type": "unique low"},
	"1 Ornate Ringmail": {"base": "Ornate Ringmail", "type": "unique low"},
	"1 Ornate Sword": {"base": "Ornate Sword", "type": "unique low"},
	"1 Overgrown Shrine Map": {"base": "Overgrown Shrine Map", "type": "unique high"},
	"1 Painted Buckler": {"base": "Painted Buckler", "type": "unique low"},
	"1 Paua Amulet": {"base": "Paua Amulet", "type": "unique special"},
	"1 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique special"},
	"1 Pine Buckler": {"base": "Pine Buckler", "type": "unique low"},
	"1 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique special"},
	"1 Plague Mask": {"base": "Plague Mask", "type": "unique low"},
	"1 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique low"},
	"1 Plate Vest": {"base": "Plate Vest", "type": "unique low"},
	"1 Plated Greaves": {"base": "Plated Greaves", "type": "unique low"},
	"1 Platinum Kris": {"base": "Platinum Kris", "type": "unique low"},
	"1 Poleaxe": {"base": "Poleaxe", "type": "unique low"},
	"1 Praetor Crown": {"base": "Praetor Crown", "type": "unique low"},
	"1 Primordial Staff": {"base": "Primordial Staff", "type": "unique low"},
	"1 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique extremely high"},
	"1 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"1 Promenade Map": {"base": "Promenade Map", "type": "unique high"},
	"1 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique extremely high"},
	"1 Prophet Crown": {"base": "Prophet Crown", "type": "unique low"},
	"1 Quartz Flask": {"base": "Quartz Flask", "type": "unique special"},
	"1 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"1 Quicksilver Flask": {"base": "Quicksilver Flask", "type": "unique low"},
	"1 Raven Mask": {"base": "Raven Mask", "type": "unique high"},
	"1 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique extremely high"},
	"1 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique very high"},
	"1 Reaver Sword": {"base": "Reaver Sword", "type": "unique low"},
	"1 Recurve Bow": {"base": "Recurve Bow", "type": "unique low"},
	"1 Regicide Mask": {"base": "Regicide Mask", "type": "unique low"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique very high"},
	"1 Riveted Boots": {"base": "Riveted Boots", "type": "unique low"},
	"1 Riveted Gloves": {"base": "Riveted Gloves", "type": "unique extremely high"},
	"1 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique extremely high"},
	"1 Rotted Round Shield": {"base": "Rotted Round Shield", "type": "unique low"},
	"1 Royal Axe": {"base": "Royal Axe", "type": "unique extremely high"},
	"1 Royal Bow": {"base": "Royal Bow", "type": "unique low"},
	"1 Royal Burgonet": {"base": "Royal Burgonet", "type": "unique high"},
	"1 Royal Skean": {"base": "Royal Skean", "type": "unique low"},
	"1 Royal Staff": {"base": "Royal Staff", "type": "unique low"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique very high"},
	"1 Ruby Flask": {"base": "Ruby Flask", "type": "unique special"},
	"1 Ruby Ring": {"base": "Ruby Ring", "type": "unique special"},
	"1 Rusted Sword": {"base": "Rusted Sword", "type": "unique low"},
	"1 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"1 Sabre": {"base": "Sabre", "type": "unique low"},
	"1 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique special"},
	"1 Sadist Garb": {"base": "Sadist Garb", "type": "unique special"},
	"1 Sage Wand": {"base": "Sage Wand", "type": "unique special"},
	"1 Sage's Robe": {"base": "Sage's Robe", "type": "unique low"},
	"1 Samite Gloves": {"base": "Samite Gloves", "type": "unique low"},
	"1 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique very high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique very high"},
	"1 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"1 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique special"},
	"1 Satin Gloves": {"base": "Satin Gloves", "type": "unique high"},
	"1 Savant's Robe": {"base": "Savant's Robe", "type": "unique high"},
	"1 Scholar Boots": {"base": "Scholar Boots", "type": "unique low"},
	"1 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique low"},
	"1 Secutor Helm": {"base": "Secutor Helm", "type": "unique low"},
	"1 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique low"},
	"1 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "unique low"},
	"1 Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "type": "unique high"},
	"1 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"1 Shackled Boots": {"base": "Shackled Boots", "type": "unique high"},
	"1 Shadow Axe": {"base": "Shadow Axe", "type": "unique low"},
	"1 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique low"},
	"1 Shagreen Boots": {"base": "Shagreen Boots", "type": "unique low"},
	"1 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique high"},
	"1 Sharktooth Arrow Quiver": {"base": "Sharktooth Arrow Quiver", "type": "unique low"},
	"1 Shore Map": {"base": "Shore Map", "type": "unique high"},
	"1 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"1 Silk Gloves": {"base": "Silk Gloves", "type": "unique low"},
	"1 Silk Slippers": {"base": "Silk Slippers", "type": "unique low"},
	"1 Silken Hood": {"base": "Silken Hood", "type": "unique special"},
	"1 Simple Robe": {"base": "Simple Robe", "type": "unique low"},
	"1 Skinning Knife": {"base": "Skinning Knife", "type": "unique low"},
	"1 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique low"},
	"1 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"1 Slink Boots": {"base": "Slink Boots", "type": "unique special"},
	"1 Solaris Circlet": {"base": "Solaris Circlet", "type": "unique very high"},
	"1 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique special"},
	"1 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique low"},
	"1 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique special"},
	"1 Sorcerer Gloves": {"base": "Sorcerer Gloves", "type": "unique high"},
	"1 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique low"},
	"1 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique low"},
	"1 Spiked Club": {"base": "Spiked Club", "type": "unique low"},
	"1 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique low"},
	"1 Stealth Boots": {"base": "Stealth Boots", "type": "unique special"},
	"1 Steel Ring": {"base": "Steel Ring", "type": "unique high"},
	"1 Steelhead": {"base": "Steelhead", "type": "unique high"},
	"1 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique special"},
	"1 Steelwood Bow": {"base": "Steelwood Bow", "type": "unique high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique special"},
	"1 Stiletto": {"base": "Stiletto", "type": "unique low"},
	"1 Strand Map": {"base": "Strand Map", "type": "unique high"},
	"1 Strapped Boots": {"base": "Strapped Boots", "type": "unique low"},
	"1 Strapped Leather": {"base": "Strapped Leather", "type": "unique low"},
	"1 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique low"},
	"1 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique low"},
	"1 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique low"},
	"1 Sundering Axe": {"base": "Sundering Axe", "type": "unique low"},
	"1 Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "type": "unique low"},
	"1 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique low"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique very high"},
	"1 Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "type": "unique high"},
	"1 Thresher Claw": {"base": "Thresher Claw", "type": "unique low"},
	"1 Timeworn Claw": {"base": "Timeworn Claw", "type": "unique low"},
	"1 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique special"},
	"1 Titan Greaves": {"base": "Titan Greaves", "type": "unique special"},
	"1 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique high"},
	"1 Tomahawk": {"base": "Tomahawk", "type": "unique low"},
	"1 Topaz Flask": {"base": "Topaz Flask", "type": "unique special"},
	"1 Topaz Ring": {"base": "Topaz Ring", "type": "unique special"},
	"1 Tornado Wand": {"base": "Tornado Wand", "type": "unique special"},
	"1 Tribal Circlet": {"base": "Tribal Circlet", "type": "unique low"},
	"1 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"1 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique special"},
	"1 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique low"},
	"1 Twilight Blade": {"base": "Twilight Blade", "type": "unique low"},
	"1 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"1 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique special"},
	"1 Underground River Map": {"base": "Underground River Map", "type": "unique high"},
	"1 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"1 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique high"},
	"1 Vaal Axe": {"base": "Vaal Axe", "type": "unique special"},
	"1 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"1 Vaal Buckler": {"base": "Vaal Buckler", "type": "unique low"},
	"1 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique special"},
	"1 Vaal Mask": {"base": "Vaal Mask", "type": "unique very high"},
	"1 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique high"},
	"1 Vaal Rapier": {"base": "Vaal Rapier", "type": "unique very high"},
	"1 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique special"},
	"1 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique special"},
	"1 Vanguard Belt": {"base": "Vanguard Belt", "type": "unique high"},
	"1 Variscite Blade": {"base": "Variscite Blade", "type": "unique high"},
	"1 Velvet Gloves": {"base": "Velvet Gloves", "type": "unique low"},
	"1 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique low"},
	"1 Vile Staff": {"base": "Vile Staff", "type": "unique low"},
	"1 Vine Circlet": {"base": "Vine Circlet", "type": "unique low"},
	"1 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"1 Visored Sallet": {"base": "Visored Sallet", "type": "unique low"},
	"1 Void Axe": {"base": "Void Axe", "type": "unique very high"},
	"1 Void Sceptre": {"base": "Void Sceptre", "type": "unique low"},
	"1 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"1 War Hammer": {"base": "War Hammer", "type": "unique low"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique very high"},
	"1 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique special"},
	"1 Wild Leather": {"base": "Wild Leather", "type": "unique low"},
	"1 Woodsplitter": {"base": "Woodsplitter", "type": "unique low"},
	"1 Wool Gloves": {"base": "Wool Gloves", "type": "unique low"},
	"1 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"1 Wyrmscale Doublet": {"base": "Wyrmscale Doublet", "type": "unique very high"},
	"1 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique low"},
	"1 Zealot Gloves": {"base": "Zealot Gloves", "type": "unique very high"},
	"1 Zealot Helmet": {"base": "Zealot Helmet", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
