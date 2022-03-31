from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKozepesJegy(TestCase):
    def test_feladat_ures(self):
        jegyek=""
        aktualis = feladatok.kozepes(jegyek)
        elvart = 0
        print(jegyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány közpes jegy van a jegyek között!")
    def test_feladat_elso_egy(self):
        jegyek="3, 2, 5, 5, 4"
        aktualis = feladatok.kozepes(jegyek)
        elvart = 1
        print(jegyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány közpes jegy van a jegyek között!")
    def test_feladat_kozbe_tobb(self):
        jegyek="4, 2, 3, 5, 3, 2, 3, 5, 3, 2"
        aktualis = feladatok.kozepes(jegyek)
        elvart = 4
        print(jegyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány közpes jegy van a jegyek között!")
    def test_feladat_egyse(self):
        jegyek="4, 2, 2, 5, 4, 2, 4, 5, 4, 2"
        aktualis = feladatok.kozepes(jegyek)
        elvart = 0
        print(jegyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány közpes jegy van a jegyek között!")