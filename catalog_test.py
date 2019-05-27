# -*- coding: utf-8 -*-
"""
Created on Mon May 27 00:48:02 2019

@author: Kenneth
"""
import unittest
import requests
import json        

url = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'
response = requests.get(url)
if (response.ok):
    jdata = json.loads(response.content)

def find_promotion(name, description):
    for p in jdata['Promotions']:
        if (p["Name"] == name and description in p["Description"] ):
            return p["Id"]
    return -1
    
class TestCatalog(unittest.TestCase):

    def test_category_name(self):
        self.assertEqual(jdata['Name'], 'Carbon credits')

    def test_can_relist(self):
        self.assertTrue(jdata['CanRelist'])        

    def test_promotion(self):
        self.assertGreater(find_promotion("Gallery", "2x larger image"), 0)

if __name__ == '__main__':
    unittest.main()