from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestMegtatlahtoMegye(TestCase):
    def test_feladat_ures(self):
        megyek=[]
        keresett="Baranya"
        aktualis = feladatok.megtalalhato(megyek,keresett)
        elvart = False
        print(megyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy "+ keresett+" megye megtalálható-e a a listába.")
    def test_feladat_elso(self):
        megyek=["Bács-Kiskun","Csongrád-Csanád","Fejér","Nógrád","Pest","Tolna"]
        keresett="Bács-Kiskun"
        aktualis = feladatok.megtalalhato(megyek,keresett)
        elvart = True
        print(megyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy "+ keresett+" megye megtalálható-e a a listába.")
    def test_feladat_utolso(self):
        megyek=["Bács-Kiskun","Csongrád-Csanád","Fejér","Nógrád","Pest","Tolna"]
        keresett="Tolna"
        aktualis = feladatok.megtalalhato(megyek,keresett)
        elvart = True
        print(megyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy "+ keresett+" megye megtalálható-e a a listába.")
    def test_feladat_kozepe(self):
        megyek=["Bács-Kiskun","Csongrád-Csanád","Fejér","Nógrád","Pest","Tolna"]
        keresett="Nógrád"
        aktualis = feladatok.megtalalhato(megyek,keresett)
        elvart = True
        print(megyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy "+ keresett+" megye megtalálható-e a a listába.")
    def test_feladat_nincs(self):
        megyek=["Bács-Kiskun","Csongrád-Csanád","Fejér","Nógrád","Pest","Tolna"]
        keresett="Vas"
        aktualis = feladatok.megtalalhato(megyek,keresett)
        elvart = False
        print(megyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy "+ keresett+" megye megtalálható-e a a listába.")