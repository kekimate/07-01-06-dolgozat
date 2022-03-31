from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestMegtatlahtoMegyeSzekhely01(TestCase):
    def test_feladat_megye_ures(self):
        megyek=[]
        keresett="Miskolc"
        aktualis = feladatok.megtalalhato(megyek,keresett)
        elvart = False
        print(megyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy "+ keresett+" megyeszékhely megtalálható-e a a listába.")
