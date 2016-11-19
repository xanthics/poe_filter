#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 11/19/2016(m/d/y) 07:56:03 UTC from "Hardcore" data
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

desc = "Divination Card"

# Base type : settings pair
items = {
	"000 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination very high"},
	"001 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"002 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination high"},
	"003 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination normal"},
	"1 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"1 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination very high"},
	"1 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination very high"},
	"1 Coveted Possession": {"base": "Coveted Possession", "class": "Divination Card", "type": "divination very high"},
	"1 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination very high"},
	"1 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"1 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination very high"},
	"1 Hunter's Resolve": {"base": "Hunter's Resolve", "class": "Divination Card", "type": "divination very high"},
	"1 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination very high"},
	"1 Lucky Connections": {"base": "Lucky Connections", "class": "Divination Card", "type": "divination very high"},
	"1 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"1 The Aesthete": {"base": "The Aesthete", "class": "Divination Card", "type": "divination very high"},
	"1 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination very high"},
	"1 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination very high"},
	"1 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"1 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"1 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination very high"},
	"1 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination very high"},
	"1 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination very high"},
	"1 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"1 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination very high"},
	"1 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination very high"},
	"1 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination very high"},
	"1 The Fox": {"base": "The Fox", "class": "Divination Card", "type": "divination very high"},
	"1 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination very high"},
	"1 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"1 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination very high"},
	"1 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"1 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"1 The Lion": {"base": "The Lion", "class": "Divination Card", "type": "divination very high"},
	"1 The Lover": {"base": "The Lover", "class": "Divination Card", "type": "divination very high"},
	"1 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination very high"},
	"1 The One With All": {"base": "The One With All", "class": "Divination Card", "type": "divination very high"},
	"1 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"1 The Scarred Meadow": {"base": "The Scarred Meadow", "class": "Divination Card", "type": "divination very high"},
	"1 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "divination very high"},
	"1 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination very high"},
	"1 The Union": {"base": "The Union", "class": "Divination Card", "type": "divination very high"},
	"1 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination very high"},
	"1 The Wrath": {"base": "The Wrath", "class": "Divination Card", "type": "divination very high"},
	"1 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination very high"},
	"1 Tranquillity": {"base": "Tranquillity", "class": "Divination Card", "type": "divination very high"},
	"1 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"2 Assassin's Favour": {"base": "Assassin's Favour", "class": "Divination Card", "type": "divination high"},
	"2 Dying Anguish": {"base": "Dying Anguish", "class": "Divination Card", "type": "divination high"},
	"2 Hope": {"base": "Hope", "class": "Divination Card", "type": "divination high"},
	"2 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"2 Lost Worlds": {"base": "Lost Worlds", "class": "Divination Card", "type": "divination high"},
	"2 The Calling": {"base": "The Calling", "class": "Divination Card", "type": "divination high"},
	"2 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"2 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"2 The Demoness": {"base": "The Demoness", "class": "Divination Card", "type": "divination high"},
	"2 The Encroaching Darkness": {"base": "The Encroaching Darkness", "class": "Divination Card", "type": "divination high"},
	"2 The Endurance": {"base": "The Endurance", "class": "Divination Card", "type": "divination high"},
	"2 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"2 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination high"},
	"2 The Inventor": {"base": "The Inventor", "class": "Divination Card", "type": "divination high"},
	"2 The Siren": {"base": "The Siren", "class": "Divination Card", "type": "divination high"},
	"2 The Spoiled Prince": {"base": "The Spoiled Prince", "class": "Divination Card", "type": "divination high"},
	"2 The Summoner": {"base": "The Summoner", "class": "Divination Card", "type": "divination high"},
	"2 The Throne": {"base": "The Throne", "class": "Divination Card", "type": "divination high"},
	"2 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination high"},
	"2 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination high"},
	"2 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination high"},
	"3 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination low"},
	"3 Prosperity": {"base": "Prosperity", "class": "Divination Card", "type": "divination low"},
	"3 Scholar of the Seas": {"base": "Scholar of the Seas", "class": "Divination Card", "type": "divination low"},
	"3 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination low"},
	"3 The Flora's Gift": {"base": "The Flora's Gift", "class": "Divination Card", "type": "divination low"},
	"3 The Hermit": {"base": "The Hermit", "class": "Divination Card", "type": "divination low"},
	"3 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "divination low"},
	"3 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"3 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "divination low"},
	"3 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "divination low"},
	"3 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
