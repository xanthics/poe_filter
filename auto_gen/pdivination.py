#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 11/20/2016(m/d/y) 00:45:22 UTC from "Essence" data
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
	"000 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination low"},
	"001 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"002 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination very high"},
	"003 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination normal"},
	"1 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"1 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination very high"},
	"1 Dialla's Subjugation": {"base": "Dialla's Subjugation", "class": "Divination Card", "type": "divination very high"},
	"1 Earth Drinker": {"base": "Earth Drinker", "class": "Divination Card", "type": "divination very high"},
	"1 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"1 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination very high"},
	"1 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination very high"},
	"1 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "divination very high"},
	"1 Mawr Blaidd": {"base": "Mawr Blaidd", "class": "Divination Card", "type": "divination very high"},
	"1 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"1 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination very high"},
	"1 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"1 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"1 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"1 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination very high"},
	"1 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination very high"},
	"1 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination very high"},
	"1 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination very high"},
	"1 The Fox": {"base": "The Fox", "class": "Divination Card", "type": "divination very high"},
	"1 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination very high"},
	"1 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"1 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination very high"},
	"1 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"1 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"1 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination very high"},
	"1 The Penitent": {"base": "The Penitent", "class": "Divination Card", "type": "divination very high"},
	"1 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"1 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination very high"},
	"1 The Stormcaller": {"base": "The Stormcaller", "class": "Divination Card", "type": "divination very high"},
	"1 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "divination very high"},
	"1 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination very high"},
	"1 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination very high"},
	"1 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination very high"},
	"1 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination very high"},
	"1 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination very high"},
	"1 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination very high"},
	"1 Treasure Hunter": {"base": "Treasure Hunter", "class": "Divination Card", "type": "divination very high"},
	"1 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"2 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination high"},
	"2 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination high"},
	"2 Hope": {"base": "Hope", "class": "Divination Card", "type": "divination high"},
	"2 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"2 Jack in the Box": {"base": "Jack in the Box", "class": "Divination Card", "type": "divination high"},
	"2 Lost Worlds": {"base": "Lost Worlds", "class": "Divination Card", "type": "divination high"},
	"2 Lysah's Respite": {"base": "Lysah's Respite", "class": "Divination Card", "type": "divination high"},
	"2 Merciless Armament": {"base": "Merciless Armament", "class": "Divination Card", "type": "divination high"},
	"2 Scholar of the Seas": {"base": "Scholar of the Seas", "class": "Divination Card", "type": "divination high"},
	"2 The Aesthete": {"base": "The Aesthete", "class": "Divination Card", "type": "divination high"},
	"2 The Calling": {"base": "The Calling", "class": "Divination Card", "type": "divination high"},
	"2 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"2 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"2 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination high"},
	"2 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination high"},
	"2 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination high"},
	"2 The Encroaching Darkness": {"base": "The Encroaching Darkness", "class": "Divination Card", "type": "divination high"},
	"2 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination high"},
	"2 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"2 The Inventor": {"base": "The Inventor", "class": "Divination Card", "type": "divination high"},
	"2 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"2 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination high"},
	"2 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination high"},
	"2 The Wrath": {"base": "The Wrath", "class": "Divination Card", "type": "divination high"},
	"2 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination high"},
	"2 Vinia's Token": {"base": "Vinia's Token", "class": "Divination Card", "type": "divination high"},
	"3 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "class": "Divination Card", "type": "divination low"},
	"3 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination low"},
	"3 Assassin's Favour": {"base": "Assassin's Favour", "class": "Divination Card", "type": "divination low"},
	"3 Audacity": {"base": "Audacity", "class": "Divination Card", "type": "divination low"},
	"3 Birth of the Three": {"base": "Birth of the Three", "class": "Divination Card", "type": "divination low"},
	"3 Cartographer's Delight": {"base": "Cartographer's Delight", "class": "Divination Card", "type": "divination low"},
	"3 Coveted Possession": {"base": "Coveted Possession", "class": "Divination Card", "type": "divination low"},
	"3 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination low"},
	"3 Doedre's Madness": {"base": "Doedre's Madness", "class": "Divination Card", "type": "divination low"},
	"3 Dying Anguish": {"base": "Dying Anguish", "class": "Divination Card", "type": "divination low"},
	"3 Gift of the Gemling Queen": {"base": "Gift of the Gemling Queen", "class": "Divination Card", "type": "divination low"},
	"3 Her Mask": {"base": "Her Mask", "class": "Divination Card", "type": "divination low"},
	"3 Lantador's Lost Love": {"base": "Lantador's Lost Love", "class": "Divination Card", "type": "divination low"},
	"3 Light and Truth": {"base": "Light and Truth", "class": "Divination Card", "type": "divination low"},
	"3 Loyalty": {"base": "Loyalty", "class": "Divination Card", "type": "divination low"},
	"3 Prosperity": {"base": "Prosperity", "class": "Divination Card", "type": "divination low"},
	"3 Rain Tempter": {"base": "Rain Tempter", "class": "Divination Card", "type": "divination low"},
	"3 Rain of Chaos": {"base": "Rain of Chaos", "class": "Divination Card", "type": "divination low"},
	"3 Shard of Fate": {"base": "Shard of Fate", "class": "Divination Card", "type": "divination low"},
	"3 The Catalyst": {"base": "The Catalyst", "class": "Divination Card", "type": "divination low"},
	"3 The Dragon": {"base": "The Dragon", "class": "Divination Card", "type": "divination low"},
	"3 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "class": "Divination Card", "type": "divination low"},
	"3 The Endurance": {"base": "The Endurance", "class": "Divination Card", "type": "divination low"},
	"3 The Explorer": {"base": "The Explorer", "class": "Divination Card", "type": "divination low"},
	"3 The Feast": {"base": "The Feast", "class": "Divination Card", "type": "divination low"},
	"3 The Flora's Gift": {"base": "The Flora's Gift", "class": "Divination Card", "type": "divination low"},
	"3 The Gambler": {"base": "The Gambler", "class": "Divination Card", "type": "divination low"},
	"3 The Gemcutter": {"base": "The Gemcutter", "class": "Divination Card", "type": "divination low"},
	"3 The Hermit": {"base": "The Hermit", "class": "Divination Card", "type": "divination low"},
	"3 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination low"},
	"3 The Lich": {"base": "The Lich", "class": "Divination Card", "type": "divination low"},
	"3 The Lion": {"base": "The Lion", "class": "Divination Card", "type": "divination low"},
	"3 The Lord in Black": {"base": "The Lord in Black", "class": "Divination Card", "type": "divination low"},
	"3 The Lover": {"base": "The Lover", "class": "Divination Card", "type": "divination low"},
	"3 The Lunaris Priestess": {"base": "The Lunaris Priestess", "class": "Divination Card", "type": "divination low"},
	"3 The Mercenary": {"base": "The Mercenary", "class": "Divination Card", "type": "divination low"},
	"3 The Metalsmith's Gift": {"base": "The Metalsmith's Gift", "class": "Divination Card", "type": "divination low"},
	"3 The Oath": {"base": "The Oath", "class": "Divination Card", "type": "divination low"},
	"3 The One With All": {"base": "The One With All", "class": "Divination Card", "type": "divination low"},
	"3 The Pack Leader": {"base": "The Pack Leader", "class": "Divination Card", "type": "divination low"},
	"3 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "divination low"},
	"3 The Scarred Meadow": {"base": "The Scarred Meadow", "class": "Divination Card", "type": "divination low"},
	"3 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"3 The Sigil": {"base": "The Sigil", "class": "Divination Card", "type": "divination low"},
	"3 The Siren": {"base": "The Siren", "class": "Divination Card", "type": "divination low"},
	"3 The Summoner": {"base": "The Summoner", "class": "Divination Card", "type": "divination low"},
	"3 The Sun": {"base": "The Sun", "class": "Divination Card", "type": "divination low"},
	"3 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "divination low"},
	"3 The Throne": {"base": "The Throne", "class": "Divination Card", "type": "divination low"},
	"3 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "divination low"},
	"3 The Visionary": {"base": "The Visionary", "class": "Divination Card", "type": "divination low"},
	"3 The Warden": {"base": "The Warden", "class": "Divination Card", "type": "divination low"},
	"3 The Watcher": {"base": "The Watcher", "class": "Divination Card", "type": "divination low"},
	"3 The Web": {"base": "The Web", "class": "Divination Card", "type": "divination low"},
	"3 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"3 Volatile Power": {"base": "Volatile Power", "class": "Divination Card", "type": "divination low"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
