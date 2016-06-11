#!/usr/bin/python
# -*- coding: utf-8 -*-
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
Purpose: Create price lists for uniques and divination cards from exiletools api data
         This file creates updated priority lists for uniques and divination cards
Note: Requires Python 3.4.x
"""

import requests
from codecs import open
from api_key import user, password
from datetime import datetime

header = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: {} PST from "{}" data
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
'''


def gen_lists():
	league1 = "Prophecy"
	league2 = "Hardcore Prophecy"
	league3 = "Standard"
	league4 = "Hardcore"

	league1queryunique = '''{{"query":{{"bool":{{"must":[{{"term":{{"attributes.league":{{"value":"{0}"}}}}}},{{"term":{{"attributes.rarity":{{"value":"Unique"}}}}}},{{"term":{{"shop.hasPrice":{{"value":"true"}}}}}}]}}}},"aggs":{{"{0} Uniques":{{"terms":{{"field":"info.typeLine","size":1000,"order":{{"avgPrice[50.0]":"desc"}}}},"aggs":{{"avgPrice":{{"percentiles":{{"field":"shop.chaosEquiv","percents":[50]}}}}}}}}}},size:0}}'''.format(league1)
	league1querycard = '''{{"query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{0}"}}}}}},{{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},{{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}]}}}},"aggs": {{"{0} Cards": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},"aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}}},size:0}}'''.format(league1)

	league2queryunique = '''{{"query":{{"bool":{{"must":[{{"term":{{"attributes.league":{{"value":"{0}"}}}}}},{{"term":{{"attributes.rarity":{{"value":"Unique"}}}}}},{{"term":{{"shop.hasPrice":{{"value":"true"}}}}}}]}}}},"aggs":{{"{0} Uniques":{{"terms":{{"field":"info.typeLine","size":1000,"order":{{"avgPrice[50.0]":"desc"}}}},"aggs":{{"avgPrice":{{"percentiles":{{"field":"shop.chaosEquiv","percents":[50]}}}}}}}}}},size:0}}'''.format(league2)
	league2querycard = '''{{"query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{0}"}}}}}},{{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},{{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}]}}}},"aggs": {{"{0} Cards": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},"aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}}},size:0}}'''.format(league2)

	league3queryunique = '''{{"query":{{"bool":{{"must":[{{"term":{{"attributes.league":{{"value":"{0}"}}}}}},{{"term":{{"attributes.rarity":{{"value":"Unique"}}}}}},{{"term":{{"shop.hasPrice":{{"value":"true"}}}}}}]}}}},"aggs":{{"{0} Uniques":{{"terms":{{"field":"info.typeLine","size":1000,"order":{{"avgPrice[50.0]":"desc"}}}},"aggs":{{"avgPrice":{{"percentiles":{{"field":"shop.chaosEquiv","percents":[50]}}}}}}}}}},size:0}}'''.format(league3)
	league3querycard = '''{{"query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{0}"}}}}}},{{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},{{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}]}}}},"aggs": {{"{0} Cards": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},"aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}}},size:0}}'''.format(league3)

	league4queryunique = '''{{"query":{{"bool":{{"must":[{{"term":{{"attributes.league":{{"value":"{0}"}}}}}},{{"term":{{"attributes.rarity":{{"value":"Unique"}}}}}},{{"term":{{"shop.hasPrice":{{"value":"true"}}}}}}]}}}},"aggs":{{"{0} Uniques":{{"terms":{{"field":"info.typeLine","size":1000,"order":{{"avgPrice[50.0]":"desc"}}}},"aggs":{{"avgPrice":{{"percentiles":{{"field":"shop.chaosEquiv","percents":[50]}}}}}}}}}},size:0}}'''.format(league4)
	league4querycard = '''{{"query": {{"bool": {{"must": [{{"term": {{"attributes.league": {{"value": "{0}"}}}}}},{{"term": {{"attributes.baseItemType": {{"value": "Card"}}}}}},{{"term": {{"shop.hasPrice": {{"value": "true"}}}}}}]}}}},"aggs": {{"{0} Cards": {{"terms": {{"field": "info.typeLine","size": 1000,"order" : {{"avgPrice[50.0]" : "desc"}}}},"aggs": {{"avgPrice": {{"percentiles": {{"field": "shop.chaosEquiv","percents": [50]}}}}}}}}}},size:0}}'''.format(league4)

	url = 'http://api.exiletools.com/index/_msearch?pretty'

	req = requests.get(url, data="{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n{{}}\n{}\n".format(league1queryunique, league1querycard, league2queryunique, league2querycard, league3queryunique, league3querycard, league4queryunique, league4querycard), auth=(user, password))

	data = req.json(encoding='utf-8')

	badcards = ["A Mother's Parting Gift",
				"The Carrion Crow",
				"The Rabid Rhoa",
				"The King's Blade",
				"The Inoculated",
				"Turn the Other Cheek"]

	lowcards = ["Thunderous Skies",
				"The Scholar"]

	if 'responses' in data:
		for l in data['responses']:
			curkey = list(l['aggregations'].keys())[0]
			if "Uniques" in curkey:
				name = ""
				if curkey == "{} Uniques".format(league1):
					name = "p"
				elif curkey == "{} Uniques".format(league2):
					name = "phc"
				elif curkey == "{} Uniques".format(league3):
					name = ""
				elif curkey == "{} Uniques".format(league4):
					name = "hc"
				items = {'very high': [], 'high': []}

				for i in l['aggregations'][curkey]['buckets']:
					if i['avgPrice']['values']['50.0'] >= 50:
						items['very high'].append(i[u'key'])
					elif i['avgPrice']['values']['50.0'] >= 10:
						items['high'].append(i[u'key'])

				with open('autogen\\{}uniques.py'.format(name), 'w', 'utf-8') as f:
					f.write(u'''{}\ndesc = "Unique"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.now().strftime('%Y-%m-%dT%H:%M:%S'), curkey)))
					for ii in items['very high']:
						f.write(u'\t"0 {0}": {{"base": "{0}", "type": "unique very high"}},\n'.format(ii))
					for ii in items['high']:
						f.write(u'\t"1 {0}": {{"base": "{0}", "type": "unique high"}},\n'.format(ii))
					f.write(u'\t"9 Other uniques": {"type": "unique normal"}\n}\n')

			elif "Cards" in curkey:
				name = ""
				if curkey == "{} Cards".format(league1):
					name = "p"
				elif curkey == "{} Cards".format(league2):
					name = "phc"
				elif curkey == "{} Cards".format(league3):
					name = ""
				elif curkey == "{} Cards".format(league4):
					name = "hc"
				items = {'high': [], 'normal': [], 'low': []}

				for i in l['aggregations'][curkey]['buckets']:
					if i['key'] in badcards or i['key'] in lowcards:
						pass
					elif i['avgPrice']['values']['50.0'] >= 6:
						items['high'].append(i[u'key'])
					elif i['avgPrice']['values']['50.0'] >= 1:
						items['normal'].append(i[u'key'])

				with open('autogen\\{}divination.py'.format(name), 'w', 'utf-8') as f:
					f.write(u'''{}\ndesc = "Divination Card"\n\n# Base type : settings pair\nitems = {{\n'''.format(header.format(datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),curkey)))
					for ii in items['high']:
						f.write(u'\t"0 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination very high"}},\n'.format(ii))
					for ii in items['normal']:
						f.write(u'\t"1 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination high"}},\n'.format(ii))
					for ii in lowcards:
						f.write(u'\t"2 {0}": {{"base": "{0}", "class": "Divination Card", "type": "divination low"}},\n'.format(ii))
					for ii in badcards:
						f.write(u'\t"7 {0}": {{"base": "{0}", "class": "Divination Card", "type": "hide"}},\n'.format(ii))
					f.write(u'\t"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}\n}\n')


if __name__ == '__main__':

	gen_lists()
