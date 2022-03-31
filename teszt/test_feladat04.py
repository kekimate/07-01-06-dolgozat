from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestJelesTanulok(TestCase):
    def test_feladat_ures(self):
        atlagok=[]
        tanulok=[]
        aktualis = feladatok.jeles_tanulok(atlagok,tanulok)
        elvart = []
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg a jeles tanulók listáját")
    def test_feladat_ures(self):
        atlagok=[4.6,3.5,5.0,3.5,3.1]
        tanulok=["Kis János", "Nagy Imre", "Arany Piri", "Péter János", "Vég Antal"]
        aktualis = feladatok.jeles_tanulok(atlagok,tanulok)
        elvart = ["Kis János","Arany Piri"]
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg a jeles tanulók listáját")

