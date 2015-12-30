"""
* Copyright (c) 2015 Jeremy Parks. All rights reserved.
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

desc = "gems"

# Text settings for various categories
settings = {
    "very high": ["Class \"Gems\"",
                  "SetBorderColor 27 162 155",
                  "SetFontSize 35"],
    "high": ["Class \"Gems\"",
             "SetBorderColor 27 162 155",
             "SetFontSize 30"],
    "normal": ["Class \"Gems\"",
               "SetBorderColor 27 162 155"],
    "low": ["Class \"Gems\"",
            "SetFontSize 24",
            "SetBackgroundColor 0 0 0 200"],
    "ignore": [""],
    "hide": ["Class \"Gems\""]
}

# Base type : settings pair
items = {
    "01 Quality Gem High": {"other": ["Quality >= 10"], "type": "very high"},
    "02 Quality Gem": {"other": ["Quality >= 1"], "type": "high"},
    "1 Portal": {"base": "Portal", "type": "normal"},
    "1 Detonate Mines": {"base": "Detonate Mines", "type": "ignore"},
    "1 Empower": {"base": "Empower", "type": "normal"},
    "1 Enhance": {"base": "Enhance", "type": "normal"},
    "1 Enlighten": {"base": "Enlighten", "type": "normal"},
    "1 Added Chaos Damage": {"base": "Added Chaos Damage", "type": "normal"},
    "1 Vaal Gems": {"base":"Vaal", "type": "normal"},
    "9 Other Gems": {"type": "low"}
}