from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestLegnagyobbSorszama(TestCase):
    def test_feladat_ures(self):
        adatok=""
        aktualis = feladatok.maxhely(adatok)
        elvart = None
        print(adatok)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg a legnagyobb elem sorszámát")
    def test_feladat_elso(self):
        adatok="7,3; 5,4; 2,0; 1,9; 4,22; 3,7"
        aktualis = feladatok.maxhely(adatok)
        elvart = 1
        print(adatok)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg a legnagyobb elem sorszámát")
    def test_feladat_utolso(self):
        adatok="5,3; 5,4; 2,0; 1,9; 4,22; 9,7"
        aktualis = feladatok.maxhely(adatok)
        elvart = 6
        print(adatok)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg a legnagyobb elem sorszámát")
    def test_feladat_kozbe(self):
        adatok="5,3; 5,4; 10,0; 1,9; 4,22; 0,7"
        aktualis = feladatok.maxhely(adatok)
        elvart = 3
        print(adatok)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg a legnagyobb elem sorszámát")