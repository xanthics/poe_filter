#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 06/28/2020(m/d/y) 00:57:02 UTC from "tmpstandard" data

desc = "Challenge Autogen"

# Base type : settings pair
items = {
	"10 Abyssal Delirium Orb": {"baseexact": "Abyssal Delirium Orb", 'other': ['CustomAlertSound "100_challenge11.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Amber Oil": {"baseexact": "Amber Oil", 'other': ['CustomAlertSound "75_challenge13.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Amber Oil": {"baseexact": "Amber Oil", 'other': ['StackSize >= 18', 'CustomAlertSound "100_challenge11.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Amorphous Delirium Orb": {"baseexact": "Amorphous Delirium Orb", 'other': ['CustomAlertSound "100_challenge11.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Armoursmith's Delirium Orb": {"baseexact": "Armoursmith's Delirium Orb", 'other': ['CustomAlertSound "100_challenge14.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Azure Oil": {"baseexact": "Azure Oil", 'other': ['CustomAlertSound "75_challenge14.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Azure Oil": {"baseexact": "Azure Oil", 'other': ['StackSize >= 18', 'CustomAlertSound "100_challenge14.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Black Oil": {"baseexact": "Black Oil", 'other': ['CustomAlertSound "75_challenge15.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Black Oil": {"baseexact": "Black Oil", 'other': ['StackSize >= 4', 'CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Blacksmith's Delirium Orb": {"baseexact": "Blacksmith's Delirium Orb", 'other': ['CustomAlertSound "100_challenge14.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Blighted Delirium Orb": {"baseexact": "Blighted Delirium Orb", 'other': ['CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Cartographer's Delirium Orb": {"baseexact": "Cartographer's Delirium Orb", 'other': ['CustomAlertSound "100_challenge11.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Clear Oil": {"baseexact": "Clear Oil", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Clear Oil": {"baseexact": "Clear Oil", 'other': ['StackSize >= 18', 'CustomAlertSound "100_challenge12.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Crimson Oil": {"baseexact": "Crimson Oil", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Crimson Oil": {"baseexact": "Crimson Oil", 'other': ['StackSize >= 5', 'CustomAlertSound "100_challenge13.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Decadent Delirium Orb": {"baseexact": "Decadent Delirium Orb", 'other': ['CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Diviner's Delirium Orb": {"baseexact": "Diviner's Delirium Orb", 'other': ['CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Fine Delirium Orb": {"baseexact": "Fine Delirium Orb", 'other': ['CustomAlertSound "100_challenge12.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Foreboding Delirium Orb": {"baseexact": "Foreboding Delirium Orb", 'other': ['CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Fossilised Delirium Orb": {"baseexact": "Fossilised Delirium Orb", 'other': ['CustomAlertSound "100_challenge11.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Fragmented Delirium Orb": {"baseexact": "Fragmented Delirium Orb", 'other': ['CustomAlertSound "100_challenge13.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Golden Oil": {"baseexact": "Golden Oil", 'other': ['CustomAlertSound "100_challenge11.wav"'], "class": "Currency", "type": "challenge very high"},
	"09 Golden Oil": {"baseexact": "Golden Oil", 'other': ['StackSize >= 2', 'CustomAlertSound "175_challenge12.wav"'], "class": "Currency", "type": "challenge extremely high"},
	"10 Imperial Delirium Orb": {"baseexact": "Imperial Delirium Orb", 'other': ['CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Indigo Oil": {"baseexact": "Indigo Oil", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Indigo Oil": {"baseexact": "Indigo Oil", 'other': ['StackSize >= 18', 'CustomAlertSound "100_challenge13.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Jeweller's Delirium Orb": {"baseexact": "Jeweller's Delirium Orb", 'other': ['CustomAlertSound "100_challenge13.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Obscured Delirium Orb": {"baseexact": "Obscured Delirium Orb", 'other': ['CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Opalescent Oil": {"baseexact": "Opalescent Oil", 'other': ['CustomAlertSound "75_challenge13.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Opalescent Oil": {"baseexact": "Opalescent Oil", 'other': ['StackSize >= 2', 'CustomAlertSound "100_challenge11.wav"'], "class": "Currency", "type": "challenge very high"},
	"08 Opalescent Oil": {"baseexact": "Opalescent Oil", 'other': ['StackSize >= 14', 'CustomAlertSound "175_challenge11.wav"'], "class": "Currency", "type": "challenge extremely high"},
	"10 Portentous Delirium Orb": {"baseexact": "Portentous Delirium Orb", 'other': ['CustomAlertSound "100_challenge13.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Primal Delirium Orb": {"baseexact": "Primal Delirium Orb", 'other': ['CustomAlertSound "100_challenge12.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Sepia Oil": {"baseexact": "Sepia Oil", 'other': ['CustomAlertSound "45_challenge6.wav"'], "class": "Currency", "type": "challenge normal"},
	"09 Sepia Oil": {"baseexact": "Sepia Oil", 'other': ['StackSize >= 2', 'CustomAlertSound "75_challenge14.wav"'], "class": "Currency", "type": "challenge high"},
	"08 Sepia Oil": {"baseexact": "Sepia Oil", 'other': ['StackSize >= 19', 'CustomAlertSound "100_challenge12.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Silver Oil": {"baseexact": "Silver Oil", 'other': ['CustomAlertSound "100_challenge12.wav"'], "class": "Currency", "type": "challenge very high"},
	"09 Silver Oil": {"baseexact": "Silver Oil", 'other': ['StackSize >= 5', 'CustomAlertSound "175_challenge13.wav"'], "class": "Currency", "type": "challenge extremely high"},
	"10 Singular Delirium Orb": {"baseexact": "Singular Delirium Orb", 'other': ['CustomAlertSound "100_challenge14.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Skittering Delirium Orb": {"baseexact": "Skittering Delirium Orb", 'other': ['CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Teal Oil": {"baseexact": "Teal Oil", 'other': ['CustomAlertSound "75_challenge12.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Teal Oil": {"baseexact": "Teal Oil", 'other': ['StackSize >= 18', 'CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Thaumaturge's Delirium Orb": {"baseexact": "Thaumaturge's Delirium Orb", 'other': ['CustomAlertSound "100_challenge14.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Timeless Delirium Orb": {"baseexact": "Timeless Delirium Orb", 'other': ['CustomAlertSound "100_challenge13.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Verdant Oil": {"baseexact": "Verdant Oil", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Verdant Oil": {"baseexact": "Verdant Oil", 'other': ['StackSize >= 18', 'CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Violet Oil": {"baseexact": "Violet Oil", 'other': ['CustomAlertSound "75_challenge11.wav"'], "class": "Currency", "type": "challenge high"},
	"09 Violet Oil": {"baseexact": "Violet Oil", 'other': ['StackSize >= 9', 'CustomAlertSound "100_challenge15.wav"'], "class": "Currency", "type": "challenge very high"},
	"10 Whispering Delirium Orb": {"baseexact": "Whispering Delirium Orb", 'other': ['CustomAlertSound "100_challenge12.wav"'], "class": "Currency", "type": "challenge very high"},
}
