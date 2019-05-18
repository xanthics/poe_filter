#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 05/18/2019(m/d/y) 19:18:18 UTC from "tmpstandard" data

desc = "Helm Enchant Autogen"

# Base type : settings pair
items = {
	"000 Enchantment Flame Surge Vs Burning Enemies 1": {"enchant": "Enchantment Flame Surge Vs Burning Enemies 1", "type": "ignore"},
	"1 10% increased Incinerate Damage for each stage": {"enchant": "Enchantment Incinerate Damage Per Stage 3", "type": "currency very high"},
	"1 12% increased Reave Radius": {"enchant": "Enchantment Reave Area Of Effect 2", "type": "currency very high"},
	"1 15% increased Elemental Hit Attack Speed": {"enchant": "Enchantment Elemental Hit Attack Speed 2", "type": "currency very high"},
	"1 150% increased Effect of the Buff granted by your Stone Golems": {"enchant": "Enchantment Stone Golem Granted Buff Effect 2", "type": "currency very high"},
	"1 20% reduced Storm Call Duration": {"enchant": "Enchantment Storm Call Duration 1", "type": "currency very high"},
	"1 25% increased Searing Bond Damage": {"enchant": "Enchantment Searing Bond Damage 1", "type": "currency very high"},
	"1 30% chance for Discharge to deal Damage without removing Charges": {"enchant": "Enchantment Discharge Consume Charges 2", "type": "currency very high"},
	"1 30% increased Blade Vortex Duration": {"enchant": "Enchantment Blade Vortex Duration 2", "type": "currency very high"},
	"1 30% increased Despair Curse Effect": {"enchant": "Enchantment Despair Effect 2", "type": "currency very high"},
	"1 30% increased Ethereal Knives Projectile Speed": {"enchant": "Enchantment Ethereal Knives Projectile Speed 2", "type": "currency very high"},
	"1 30% increased Spark Projectile Speed": {"enchant": "Enchantment Spark Projectile Speed 2", "type": "currency very high"},
	"1 30% increased Temporal Chains Curse Effect": {"enchant": "Enchantment Temporal Chains Curse Effect 2", "type": "currency very high"},
	"1 30% increased Vortex Duration": {"enchant": "Enchantment Vortex Duration 2", "type": "currency very high"},
	"1 30% reduced Earthquake Duration": {"enchant": "Enchantment Earthquake Duration 2", "type": "currency very high"},
	"1 30% reduced Lightning Warp Duration": {"enchant": "Enchantment Lightning Warp Duration 2", "type": "currency very high"},
	"1 30% reduced Spectral Throw Projectile Deceleration": {"enchant": "Enchantment Spectral Throw Projectile Deceleration 2", "type": "currency very high"},
	"1 30% reduced Storm Call Duration": {"enchant": "Enchantment Storm Call Duration 2", "type": "currency very high"},
	"1 40% increased Arctic Breath Damage": {"enchant": "Enchantment Arctic Breath Damage 2", "type": "currency very high"},
	"1 40% increased Blade Flurry Damage": {"enchant": "Enchantment Blade Flurry Damage 2", "type": "currency very high"},
	"1 40% increased Caustic Arrow Damage": {"enchant": "Enchantment Caustic Arrow Damage 2", "type": "currency very high"},
	"1 40% increased Cyclone Damage": {"enchant": "Enchantment Cyclone Damage 2", "type": "currency very high"},
	"1 40% increased Essence Drain Damage": {"enchant": "Enchantment Essence Drain Damage 2", "type": "currency very high"},
	"1 40% increased Fireball Damage": {"enchant": "Enchantment Fireball Damage 2", "type": "currency very high"},
	"1 40% increased Flicker Strike Damage": {"enchant": "Enchantment Flicker Strike Damage 2", "type": "currency very high"},
	"1 40% increased Freezing Pulse Damage": {"enchant": "Enchantment Freezing Pulse Damage 2", "type": "currency very high"},
	"1 40% increased Frost Blades Damage": {"enchant": "Enchantment Frost Blades Damage 2", "type": "currency very high"},
	"1 40% increased Glacial Cascade Damage": {"enchant": "Enchantment Glacial Cascade Damage 2", "type": "currency very high"},
	"1 40% increased Ice Nova Damage": {"enchant": "Enchantment Ice Nova Damage 2", "type": "currency very high"},
	"1 40% increased Righteous Fire Damage": {"enchant": "Enchantment Righteous Fire Damage 2", "type": "currency very high"},
	"1 40% increased Spark Damage": {"enchant": "Enchantment Spark Damage 2", "type": "currency very high"},
	"1 40% increased Tectonic Slam Damage": {"enchant": "Enchantment Tectonic Slam Damage 2", "type": "currency very high"},
	"1 40% of Glacial Cascade Physical Damage Converted to Cold Damage": {"enchant": "Enchantment Glacial Cascade Physical Damage Percent To Convert To Cold 2", "type": "currency very high"},
	"1 45% increased Vigilant Strike Fortify Duration": {"enchant": "Enchantment Vigilant Strike Fortify Duration 2", "type": "currency very high"},
	"1 9% increased Flicker Strike Damage per Frenzy Charge": {"enchant": "Enchantment Flicker Strike Damage Per Frenzy Charge 2", "type": "currency very high"},
	"1 Arc Chains an additional time": {"enchant": "Enchantment Arc Num Of Additional Projectiles In Chain 1", "type": "currency very high"},
	"1 Bane deals 40% increased Damage": {"enchant": "Enchantment Bane Damage 2", "type": "currency very high"},
	"1 Barrage fires an additional Projectile": {"enchant": "Enchantment Barrage Num Of Additional Projectiles 1", "type": "currency very high"},
	"1 Consecrated Path deals 40% increased Damage": {"enchant": "Enchantment Consecrated Path Damage 2", "type": "currency very high"},
	"1 Discipline has 20% reduced Mana Reservation": {"enchant": "Enchantment Discipline Mana Reservation 2", "type": "currency very high"},
	"1 Divine Ire Damages 2 additional nearby Enemies when gaining Stages": {"enchant": "Enchantment Divine Ire Number Of Additional Nearby Enemies To Zap 2", "type": "currency very high"},
	"1 Divine Ire deals 40% increased Damage": {"enchant": "Enchantment Divine Ire Damage 2", "type": "currency very high"},
	"1 Double Strike has a 15% chance to deal Double Damage to Bleeding Enemies": {"enchant": "Enchantment Double Strike Double Damage Vs Bleeding 2", "type": "currency very high"},
	"1 Dread Banner has 40% increased Aura Effect": {"enchant": "Enchantment Dread Banner Effect 2", "type": "currency very high"},
	"1 Elemental Hit deals 40% increased Damage": {"enchant": "Enchantment Elemental Hit Damage 2", "type": "currency very high"},
	"1 Herald of Agony has 20% reduced Mana Reservation": {"enchant": "Enchantment Herald Of Agony Mana Reservation 1", "type": "currency very high"},
	"1 Herald of Agony has 30% reduced Mana Reservation": {"enchant": "Enchantment Herald Of Agony Mana Reservation 2", "type": "currency extremely high"},
	"1 Holy Flame Totem deals 40% increased Damage": {"enchant": "Enchantment Flame Totem Damage 2", "type": "currency very high"},
	"1 Holy Flame Totem fires 2 additional Projectiles": {"enchant": "Enchantment Flame Totem Num Of Additional Projectiles 2", "type": "currency very high"},
	"1 Holy Flame Totem has 30% increased Projectile Speed": {"enchant": "Enchantment Flame Totem Projectile Speed 2", "type": "currency very high"},
	"1 Ice Golems deal 40% increased Damage": {"enchant": "Enchantment Summon Ice Golem Damage 2", "type": "currency very high"},
	"1 Ice Spear fires an additional Projectile": {"enchant": "Enchantment Ice Spear Additional Projectile 1", "type": "currency very high"},
	"1 Ice Trap Damage Penetrates 10% Cold Resistance": {"enchant": "Enchantment Ice Trap Cold Penetration 2", "type": "currency very high"},
	"1 Incinerate has +2 to maximum stages": {"enchant": "Enchantment Incinerate Maximum Stages 2", "type": "currency very high"},
	"1 Kinetic Blast has a 75% chance for an additional explosion": {"enchant": "Enchantment Kinetic Blast Explosions 2", "type": "currency very high"},
	"1 Lightning Trap Damage Penetrates 10% Lightning Resistance": {"enchant": "Enchantment Lightning Trap Penetration 2", "type": "currency very high"},
	"1 Magma Orb Chains an additional 2 times": {"enchant": "Enchantment Magma Orb Num Of Additional Projectiles In Chain 2", "type": "currency very high"},
	"1 Malevolence has 15% reduced Mana Reservation": {"enchant": "Enchantment Malevolence Mana Reservation 2", "type": "currency very high"},
	"1 Molten Strike fires 2 additional Projectiles": {"enchant": "Enchantment Molten Strike Num Of Additional Projectiles 2", "type": "currency extremely high"},
	"1 Molten Strike fires an additional Projectile": {"enchant": "Enchantment Molten Strike Num Of Additional Projectiles 1", "type": "currency very high"},
	"1 Purity of Ice has 20% reduced Mana Reservation": {"enchant": "Enchantment Purity Of Ice Mana Reservation 2", "type": "currency very high"},
	"1 Scourge Arrow creates an additional spore pod at Maximum Stages": {"enchant": "Enchantment Scourge Arrow Additional Spore 1", "type": "currency very high"},
	"1 Shock Nova ring deals 60% increased Damage": {"enchant": "Enchantment Shock Nova Larger Ring Damage 2", "type": "currency very high"},
	"1 Soulrend deals 40% increased Damage": {"enchant": "Enchantment Soulrend Damage 2", "type": "currency very high"},
	"1 Soulrend fires an additional Projectile": {"enchant": "Enchantment Soulrend Number Of Additional Projectiles 1", "type": "currency very high"},
	"1 Spark fires 3 additional Projectiles": {"enchant": "Enchantment Spark Num Of Additional Projectiles 2", "type": "currency very high"},
	"1 Storm Brand Damage Penetrates 12% of Branded Enemy's Lightning Resistance": {"enchant": "Storm Brand Attached Target Lightning Penetration 2", "type": "currency very high"},
	"1 Storm Brand deals 40% increased Damage": {"enchant": "Enchantment Storm Brand Damage 2", "type": "currency very high"},
	"1 Storm Burst has a 15% chance to create an additional Orb": {"enchant": "Enchantment Storm Burst Additional Object Chance 2", "type": "currency very high"},
	"1 Summoned Agony Crawler fires 2 additional Projectiles": {"enchant": "Enchantment Herald Of Agony Num Of Secondary Projectiles 1", "type": "currency very high"},
	"1 Tectonic Slam has 20% chance to create a Charged Slam": {"enchant": "Enchantment Tectonic Slam Chance To Charged Slam 2", "type": "currency very high"},
	"1 Tornado Shot fires 2 additional secondary Projectiles": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 2", "type": "currency extremely high"},
	"1 Tornado Shot fires an additional secondary Projectile": {"enchant": "Enchantment Tornado Shot Num Of Secondary Projectiles 1", "type": "currency very high"},
	"1 Toxic Rain deals 40% increased Damage": {"enchant": "Enchantment Toxic Rain Damage 2", "type": "currency very high"},
	"1 Toxic Rain fires 1 additional Arrow": {"enchant": "Enchantment Toxic Rain Num Of Additional Projectiles 1", "type": "currency very high"},
	"1 Wild Strike Chains an additional 6 times": {"enchant": "Enchantment Wild Strike Num Of Additional Projectiles In Chain 2", "type": "currency very high"},
	"1 Winter Orb deals 25% increased Damage": {"enchant": "Enchantment Winter Orb Damage 1", "type": "currency very high"},
	"1 Winter Orb deals 40% increased Damage": {"enchant": "Enchantment Winter Orb Damage 2", "type": "currency extremely high"},
	"1 Winter Orb has +2 Maximum Stages": {"enchant": "Enchantment Frost Fury Additional Max Number Of Stages 1", "type": "currency extremely high"},
	"1 Winter Orb has 3% increased Area of Effect per Stage": {"enchant": "Enchantment Frost Fury Area Of Effect Per Stage 2", "type": "currency very high"},
	"1 Zealotry has 15% reduced Mana Reservation": {"enchant": "Enchantment Zealotry Mana Reservation 2", "type": "currency very high"},
}
