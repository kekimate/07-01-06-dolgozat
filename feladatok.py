# feladat.py

# 1. feladat
# Készítsen függvényt megatalható-e néven!
# A függvény egyik bemeneti paramétere egy lista megyék neveivel. Pl. megyek = ["Bács-Kiskun","Csongrád-Csanád","Fejér","Nógrád","Pest","Tolna"].
# A másik bemenő paraméter egy keresett megye neve.
# A függvény határozza meg, hogy a keresett megye szerepel-e a listában!

def megtalalhato(megyek:list, keresett:str) -> bool:
    return False

# 2. feladat
# Készítsen függvényt kezepes néven!
# A függvény bemenete egy jegyekből álló karakterlánc: "4, 2, 4, 3, 2, 3, 1"!
# A függvény számolja meg, hogy hány tantárgyból ért el közepes eredményt a diák!

# 3. feladat
# Készítsen függfényt maxhely néven!
# A függvény bemenete egy számokból álló karakterlánc: 2,3; 5,4; 2,0; 1,9; 4,22; 3,7!
# Határozza meg a legnagyobb szám sorszámát (az első számot egytől sorszámozzuk)!
# Ha nincsenek számok térjen vissza None értékkel!

# 4. feladat
# A feladat csak akkor csinálja meg, ha minden feladattal végzett!
# A feladat megoldása csak egy pontot ér, a célja a dolgozat írás alatti hasznos időtöltés annak aki gyorsan végzett a feladatokkal!
# Készítsen függvényt jeles_tanulók néven
# A függvény bemeneti paramétere két lista. Az egyik tartalmazza a diákok átlagát. A másik lista a diákok nevét!
# Az első lista n. átlagához a másik lista n. diákja tartozik.
# A függvény visszatérési értéke legyen egy lista a jeles tanulók neveivel! A jeles tanulók azok, akik átlaga 4.5-nél jobbak.

def jeles_tanulok(atlagok:list, tanulok:list)->list:
    eredmey = []
    return eredmey