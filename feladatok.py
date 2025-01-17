# feladat.py

# 1. feladat
# Készítsen függvényt megtalalhato néven!
# A függvény egyik bemeneti paramétere egy lista megyeszékhelyek neveivel. Pl. megyek = ["Budapest","Miskolc","Pécs","Szeged","Szekszárd","Szolnok"].
# A másik bemenő paraméter egy keresett megyeszékhely neve.
# A függvény határozza meg, hogy a keresett megyeszékhely szerepel-e a listában!

def megtalalhato(megyeszekhelyek:list, keresett:str) -> bool:
    if len(megyeszekhelyek) == 0:
        return False

    for i in megyeszekhelyek:
        if i == keresett:
            return True
    return False
# 2. feladat
# Készítsen függvényt jeles néven!
# A függvény bemenete egy jegyekből álló karakterlánc: "4, 2, 4, 3, 2, 3, 1"!
# A függvény számolja meg, hogy hány tantárgyból ért el jeles (5) eredményt a diák!
def jeles(jegy:str) -> int:
    db = 0
    seged = jegy.split(", ")
    for i in seged:
        if i == "5":
            db += 1
    return db

# 3. feladat
# Készítsen függfényt minhely néven!
# A függvény bemenete egy számokból álló karakterlánc: 2,3; 5,4; 2,0; 1,9; 4,22; 3,7!
# Határozza meg a legkisebb szám sorszámát (az első számot egytől sorszámozzuk)!
# Ha nincsenek számok térjen vissza None értékkel!

def minhely(szamok:str) -> int:
    seged = szamok.replace(',','.')
    seged2 = seged.split("; ")
    min = seged2[0]
    db = 1
    if szamok == "":
        return None
    for i in seged2:
        if i < min:
            min = i
    for j in seged2:
        if j != min:
            db += 1
        else:
            break
    return db

# 4. feladat
# A feladat csak akkor csinálja meg, ha minden feladattal végzett!
# A feladat megoldása csak egy pontot ér, a célja a dolgozat írás alatti hasznos időtöltés annak aki gyorsan végzett a feladatokkal!
# Készítsen függvényt jeles_tanulók néven
# A függvény bemeneti paramétere két lista. Az egyik tartalmazza a matematika dolgozat eredményeit. A másik lista a diákok nevét!
# Az első lista n. jegyéhez a másik lista n. diákja tartozik.
# A függvény visszatérési értéke legyen egy lista a jeles dolgozati eredményt elért tanulók neveivel! A jeles dolgozatírók tanulók akik ötöst dologozatot írtak.

def jeles_tanulok(metek:list, tanulok:list)->list:
    eredmey = []
    return eredmey