from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestMegkisebbSorszama(TestCase):
    def test_feladat_ures(self):
        adatok=""
        aktualis = feladatok.minhely(adatok)
        elvart = None
        print(adatok)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg a legkisebb elem sorszámát")
