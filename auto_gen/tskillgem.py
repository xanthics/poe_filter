#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/15/2019(m/d/y) 05:21:44 UTC from "tmpstandard" data

desc = "Skill Gems Autogen"

# Base type : settings pair
items = {
	"00 True 1 Vaal Ancestral Warchief": {"baseexact": "Vaal Ancestral Warchief", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"00 True 1 Vaal Blade Vortex": {"baseexact": "Vaal Blade Vortex", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem extremely high"},
	"00 True 1 Vaal Double Strike": {"baseexact": "Vaal Double Strike", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"00 True 1 Vaal Flameblast": {"baseexact": "Vaal Flameblast", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"00 True 1 Vaal Ground Slam": {"baseexact": "Vaal Ground Slam", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"00 True 1 Vaal Ice Nova": {"baseexact": "Vaal Ice Nova", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"00 True 1 Vaal Power Siphon": {"baseexact": "Vaal Power Siphon", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"00 True 1 Vaal Reave": {"baseexact": "Vaal Reave", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"00 True 1 Vaal Spectral Throw": {"baseexact": "Vaal Spectral Throw", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"00 True 1 Vengeance": {"baseexact": "Vengeance", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 23", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Ancestral Protector": {"baseexact": "Ancestral Protector", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Ancestral Warchief": {"baseexact": "Ancestral Warchief", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Armageddon Brand": {"baseexact": "Armageddon Brand", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Artillery Ballista": {"baseexact": "Artillery Ballista", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Consecrated Path": {"baseexact": "Consecrated Path", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Conversion Trap": {"baseexact": "Conversion Trap", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Convocation": {"baseexact": "Convocation", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Detonate Dead": {"baseexact": "Detonate Dead", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Ethereal Knives": {"baseexact": "Ethereal Knives", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Explosive Arrow": {"baseexact": "Explosive Arrow", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Explosive Trap": {"baseexact": "Explosive Trap", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Fire Trap": {"baseexact": "Fire Trap", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Firestorm": {"baseexact": "Firestorm", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Frost Blades": {"baseexact": "Frost Blades", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Ground Slam": {"baseexact": "Ground Slam", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Ice Spear": {"baseexact": "Ice Spear", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Lancing Steel": {"baseexact": "Lancing Steel", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Lightning Arrow": {"baseexact": "Lightning Arrow", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Perforate": {"baseexact": "Perforate", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Purity of Fire": {"baseexact": "Purity of Fire", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Purity of Ice": {"baseexact": "Purity of Ice", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Rain of Arrows": {"baseexact": "Rain of Arrows", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Reckoning": {"baseexact": "Reckoning", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Righteous Fire": {"baseexact": "Righteous Fire", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Shattering Steel": {"baseexact": "Shattering Steel", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Siege Ballista": {"baseexact": "Siege Ballista", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Smite": {"baseexact": "Smite", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Summon Carrion Golem": {"baseexact": "Summon Carrion Golem", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Summon Flame Golem": {"baseexact": "Summon Flame Golem", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Summon Lightning Golem": {"baseexact": "Summon Lightning Golem", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Tempest Shield": {"baseexact": "Tempest Shield", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Temporal Chains": {"baseexact": "Temporal Chains", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Tornado Shot": {"baseexact": "Tornado Shot", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Vaal Ancestral Warchief": {"baseexact": "Vaal Ancestral Warchief", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Blade Vortex": {"baseexact": "Vaal Blade Vortex", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Blight": {"baseexact": "Vaal Blight", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Vaal Burning Arrow": {"baseexact": "Vaal Burning Arrow", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Cold Snap": {"baseexact": "Vaal Cold Snap", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Detonate Dead": {"baseexact": "Vaal Detonate Dead", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Discipline": {"baseexact": "Vaal Discipline", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem extremely high"},
	"01 True 1 Vaal Double Strike": {"baseexact": "Vaal Double Strike", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Earthquake": {"baseexact": "Vaal Earthquake", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Vaal Fireball": {"baseexact": "Vaal Fireball", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Flameblast": {"baseexact": "Vaal Flameblast", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Vaal Grace": {"baseexact": "Vaal Grace", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Ground Slam": {"baseexact": "Vaal Ground Slam", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Vaal Ice Nova": {"baseexact": "Vaal Ice Nova", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Impurity of Fire": {"baseexact": "Vaal Impurity of Fire", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Vaal Impurity of Ice": {"baseexact": "Vaal Impurity of Ice", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Lightning Strike": {"baseexact": "Vaal Lightning Strike", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Vaal Lightning Trap": {"baseexact": "Vaal Lightning Trap", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Molten Shell": {"baseexact": "Vaal Molten Shell", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Power Siphon": {"baseexact": "Vaal Power Siphon", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Rain of Arrows": {"baseexact": "Vaal Rain of Arrows", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Vaal Reave": {"baseexact": "Vaal Reave", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Vaal Righteous Fire": {"baseexact": "Vaal Righteous Fire", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vaal Spectral Throw": {"baseexact": "Vaal Spectral Throw", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Vaal Storm Call": {"baseexact": "Vaal Storm Call", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"01 True 1 Vaal Summon Skeletons": {"baseexact": "Vaal Summon Skeletons", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Vulnerability": {"baseexact": "Vulnerability", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"01 True 1 Winter Orb": {"baseexact": "Winter Orb", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem very high"},
	"01 True 1 Wither": {"baseexact": "Wither", "class": "Gems", "other": ["GemLevel >= 21", "Quality >= 0", "Corrupted True"], "type": "gem low"},
	"10 True 1 Arc": {"baseexact": "Arc", "class": "Gems", "other": ["GemLevel >= 20", "Quality >= 0", "Corrupted True"], "type": "gem high"},
	"20 False 1 Empower Support": {"baseexact": "Empower Support", "class": "Gems", "other": ["GemLevel >= 2", "Quality >= 0", "Corrupted False"], "type": "gem very high"},
	"20 False 1 Enhance Support": {"baseexact": "Enhance Support", "class": "Gems", "other": ["GemLevel >= 2", "Quality >= 0", "Corrupted False"], "type": "gem low"},
	"20 False 1 Enlighten Support": {"baseexact": "Enlighten Support", "class": "Gems", "other": ["GemLevel >= 2", "Quality >= 0", "Corrupted False"], "type": "gem very high"},
	"30 False 1 Arc": {"baseexact": "Arc", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Deathmark Support": {"baseexact": "Deathmark Support", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem very high"},
	"30 False 1 Explosive Arrow": {"baseexact": "Explosive Arrow", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Flicker Strike": {"baseexact": "Flicker Strike", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Freezing Pulse": {"baseexact": "Freezing Pulse", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Herald of Ice": {"baseexact": "Herald of Ice", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Ice Shot": {"baseexact": "Ice Shot", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Raise Spectre": {"baseexact": "Raise Spectre", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Raise Zombie": {"baseexact": "Raise Zombie", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Spell Cascade Support": {"baseexact": "Spell Cascade Support", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Spirit Offering": {"baseexact": "Spirit Offering", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Storm Brand": {"baseexact": "Storm Brand", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Trap Support": {"baseexact": "Trap Support", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Vicious Projectiles Support": {"baseexact": "Vicious Projectiles Support", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"30 False 1 Vulnerability": {"baseexact": "Vulnerability", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 20", "Corrupted False"], "type": "gem high"},
	"31 False 1 Empower Support": {"baseexact": "Empower Support", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 0", "Corrupted False"], "type": "gem high"},
	"31 False 1 Enlighten Support": {"baseexact": "Enlighten Support", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 0", "Corrupted False"], "type": "gem very high"},
	"31 False 1 Portal": {"baseexact": "Portal", "class": "Gems", "other": ["GemLevel >= 1", "Quality >= 0", "Corrupted False"], "type": "gem high"},
}
