from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestMegkisebbSorszama(TestCase):
     def test_feladat_elso(self):
        adatok="0,3; 5,4; 2,0; 1,9; 4,22; 3,7"
        aktualis = feladatok.minhely(adatok)
        elvart = 1
        print(adatok)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg a legkisebb elem sorszámát")
