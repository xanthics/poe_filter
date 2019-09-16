#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/16/2019(m/d/y) 18:58:33 UTC from "tmpstandard" data

desc = "Helm Enchant Autogen"

# Base type : settings pair
items = {
	"000 Enchantment Flame Surge Vs Burning Enemies 1": {"enchant": "Enchantment Flame Surge Vs Burning Enemies 1", "type": "ignore"},
	"1 15% increased Cyclone Attack Speed": {"enchant": "Enchantment Cyclone Attack Speed 2", "type": "base very high"},
	"1 15% increased Frostbolt Cast Speed": {"enchant": "Enchantment Frost Bolt Cast Speed 2", "type": "base very high"},
	"1 30% increased Blade Vortex Duration": {"enchant": "Enchantment Blade Vortex Duration 2", "type": "base very high"},
	"1 30% increased Freezing Pulse Projectile Speed": {"enchant": "Enchantment Freezing Pulse Projectile Speed 2", "type": "base very high"},
	"1 30% increased Temporal Chains Curse Effect": {"enchant": "Enchantment Temporal Chains Curse Effect 2", "type": "base very high"},
	"1 30% reduced Earthquake Duration": {"enchant": "Enchantment Earthquake Duration 2", "type": "base very high"},
	"1 30% reduced Storm Call Duration": {"enchant": "Enchantment Storm Call Duration 2", "type": "base very high"},
	"1 40% increased Arc Damage": {"enchant": "Enchantment Arc Damage 2", "type": "base very high"},
	"1 40% increased Ball Lightning Damage": {"enchant": "Enchantment Ball Lightning Damage 2", "type": "base very high"},
	"1 40% increased Cyclone Damage": {"enchant": "Enchantment Cyclone Damage 2", "type": "base very high"},
	"1 40% increased Essence Drain Damage": {"enchant": "Enchantment Essence Drain Damage 2", "type": "base very high"},
	"1 40% increased Freezing Pulse Damage": {"enchant": "Enchantment Freezing Pulse Damage 2", "type": "base very high"},
	"1 40% increased Frost Blades Damage": {"enchant": "Enchantment Frost Blades Damage 2", "type": "base very high"},
	"1 40% increased Frostbolt Damage": {"enchant": "Enchantment Frost Bolt Damage 2", "type": "base very high"},
	"1 40% increased Glacial Cascade Damage": {"enchant": "Enchantment Glacial Cascade Damage 2", "type": "base very high"},
	"1 40% increased Ice Nova Damage": {"enchant": "Enchantment Ice Nova Damage 2", "type": "base very high"},
	"1 40% increased Ice Shot Damage": {"enchant": "Enchantment Ice Shot Damage 2", "type": "base very high"},
	"1 Arc Chains an additional time": {"enchant": "Enchantment Arc Num Of Additional Projectiles In Chain 1", "type": "base very high"},
	"1 Ball Lightning fires an additional Projectile": {"enchant": "Enchantment Ball Lightning Additional Projectiles 1", "type": "base very high"},
	"1 Barrage fires an additional Projectile": {"enchant": "Enchantment Barrage Num Of Additional Projectiles 1", "type": "base very high"},
	"1 Blood Rage grants additional 12% increased Attack Speed": {"enchant": "Enchantment Blood Rage Attack Speed 2", "type": "base very high"},
	"1 Divine Ire deals 40% increased Damage": {"enchant": "Enchantment Divine Ire Damage 2", "type": "base very high"},
	"1 Flamethrower Trap has 2 additional Flames": {"enchant": "Enchantment Flamethrower Additional Flamethrowers 2", "type": "base very high"},
	"1 Hatred has 15% reduced Mana Reservation": {"enchant": "Enchantment Hatred Mana Reservation 2", "type": "base very high"},
	"1 Herald of Agony has 30% reduced Mana Reservation": {"enchant": "Enchantment Herald Of Agony Mana Reservation 2", "type": "base very high"},
	"1 Holy Flame Totem deals 40% increased Damage": {"enchant": "Enchantment Flame Totem Damage 2", "type": "base very high"},
	"1 Holy Flame Totem fires 2 additional Projectiles": {"enchant": "Enchantment Flame Totem Num Of Additional Projectiles 2", "type": "base very high"},
	"1 Ice Spear fires an additional Projectile": {"enchant": "Enchantment Ice Spear Additional Projectile 1", "type": "base very high"},
	"1 Incinerate has +2 to maximum stages": {"enchant": "Enchantment Incinerate Maximum Stages 2", "type": "base very high"},
	"1 Lightning Arrow hits 2 additional Enemies": {"enchant": "Enchantment Lightning Arrow Extra Targets 2", "type": "base very high"},
	"1 Lightning Trap Damage Penetrates 10% Lightning Resistance": {"enchant": "Enchantment Lightning Trap Penetration 2", "type": "base very high"},
	"1 Magma Orb Chains an additional 2 times": {"enchant": "Enchantment Magma Orb Num Of Additional Projectiles In Chain 2", "type": "base very high"},
	"1 Malevolence has 15% reduced Mana Reservation": {"enchant": "Enchantment Malevolence Mana Reservation 2", "type": "base very high"},
	"1 Molten Strike fires 2 additional Projectiles": {"enchant": "Enchantment Molten Strike Num Of Additional Projectiles 2", "type": "base very high"},
	"1 Orb of Storms has 30% increased Cast Speed": {"enchant": "Enchantment Orb Of Storms Cast Speed 2", "type": "base very high"},
	"1 Scourge Arrow creates an additional spore pod at Maximum Stages": {"enchant": "Enchantment Scourge Arrow Additional Spore 1", "type": "base extremely high"},
	"1 Storm Brand Damage Penetrates 12% of Branded Enemy's Lightning Resistance": {"enchant": "Storm Brand Attached Target Lightning Penetration 2", "type": "base very high"},
	"1 Storm Brand deals 40% increased Damage": {"enchant": "Enchantment Storm Brand Damage 2", "type": "base very high"},
	"1 Storm Burst has a 15% chance to create an additional Orb": {"enchant": "Enchantment Storm Burst Additional Object Chance 2", "type": "base very high"},
	"1 Summon Raging Spirit has 18% chance to summon an extra Minion": {"enchant": "Enchantment Summoned Raging Spirit Additional 2", "type": "base very high"},
	"1 Summoned Agony Crawler fires 2 additional Projectiles": {"enchant": "Enchantment Herald Of Agony Num Of Secondary Projectiles 1", "type": "base very high"},
	"1 Tectonic Slam has 20% chance to create a Charged Slam": {"enchant": "Enchantment Tectonic Slam Chance To Charged Slam 2", "type": "base very high"},
	"1 Tornado Shot fires 2 additional secondary Projectiles": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 2", "type": "base extremely high"},
	"1 Tornado Shot fires an additional secondary Projectile": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 1", "type": "base extremely high"},
	"1 Toxic Rain deals 40% increased Damage": {"enchant": "Enchantment Toxic Rain Damage 2", "type": "base very high"},
	"1 Toxic Rain fires 1 additional Arrow": {"enchant": "Enchantment Toxic Rain Num Of Additional Projectiles 1", "type": "base extremely high"},
	"1 0 Volatile Dead destroys up to 1 additional Corpse": {"enchant": "Enchantment Volatile Dead Orbs 1", "type": "base very high"},
	"1 1 Volatile Dead destroys up to 1 additional Corpse": {"enchant": "Enchantment Volatile Dead Orbs 2", "type": "base very high"},
	"1 2 Volatile Dead destroys up to 1 additional Corpse": {"enchant": "Enchantment Volatile Dead Orbs 3", "type": "base very high"},
	"1 Wild Strike Chains an additional 6 times": {"enchant": "Enchantment Wild Strike Num Of Additional Projectiles In Chain 2", "type": "base very high"},
	"1 Winter Orb has +2 Maximum Stages": {"enchant": "Enchantment Frost Fury Additional Max Number Of Stages 1", "type": "base very high"},
	"7 enchant default": {"class": "Helmet", "other": ["AnyEnchantment True"], "type": "item mod"}
}
