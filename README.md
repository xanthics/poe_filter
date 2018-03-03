# poe_filter

This is a script to generate a filter file for Path of Exile using the included config files.

[GGG Forum thread](https://www.pathofexile.com/forum/view-thread/1721195) with more information about the filter.

**HIDE**
* [Download Bestiary](xan.t.hide.filter?raw=true)
* [Download Bestiary Hardcore](xan.thc.hide.filter?raw=true)
* [Download Standard](xan.st.hide.filter?raw=true)
* [Download Hardcore](xan.hc.hide.filter?raw=true)

**SHOW**
* [Download Bestiary](xan.t.show.filter?raw=true)
* [Download Bestiary Hardcore](xan.thc.show.filter?raw=true)
* [Download Standard](xan.s.show.filter?raw=true)
* [Download Hardcore](xan.hc.show.filter?raw=true)

Usage
=====
Run Create_filter with necessary config files to generate xan.filter.  Note that this will automatically put xan.show.filter and xan.hide.filter in <relative path>\Documents\My Games\Path of Exile

(Optional) Run pricetool to update currency, divination, and unique tiers.  
The poe ninja version should finish very quickly  
~~The ggg-api version may take some time depending on how much data is pending in ggg stash river.  Requires a running MongoDB instance.~~

Config
======
See item_config.template.py and theme_config.minimal.py

Hide all
========
![Hide unspecified items](https://i.imgur.com/7Y8tzsz.jpg "Hide")

Show all
========
![Show all items](https://i.imgur.com/HP8IT0p.jpg "Show")

Thanks
======
This script is heavily inspired by "One Filter to rule them all" that can be found at https://www.pathofexile.com/forum/view-thread/1259059
