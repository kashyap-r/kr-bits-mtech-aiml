# Toteutusdokumentti

Ohjelman tarkoitus on komentoriviltä suoritettavalla käyttöliittymällä generoida verkkoja, joita visualisoidaan NetworkX-moduulin avulla, ja selvittää niissä lyhimpiä reittejä Dijkstran algoritmin sekä IDA*-algoritmin avulla.

Dijkstra toimii aikavaativuudella O(n + m log n) sekä tilavaativuudella O(n + m).
IDA*:n aikavaativuus taas on ekponentiaalinen (O(n^m)), sillä se voi huonossa tapauksessa (esim. suurissa verkoissa) etsiä samoja reittejä todella monta kertaa, sillä se ei hyödynnä dynaamista ohjelmointia reittien pitämiseen välimuistissa.Tämän takia sen tilavaativuus on tosin huomattavasti A*:ia parempi, joka niin tekee.


Mahdollisia puutteita tai parannettavaa projektissa:

- Melko vähäinen unittestien määrä, mutta tätä kompensoi se, että nämä testit epäsuorasti testaavat käytännössä kaiken ydintoiminnan ja varmistavat todenmukaiset vastaukset.
- Ei kovin optimaalinen IDA*:n testaamiseen, mutta hyvin tiheissä verkoissa toimii IDA*:n kanssa riittävän hyvin.
- UI:n kanssa hieman bugeja, mutta eivät estä pääasiallista toiminnallisuutta.

Lähteet:

[Tietorakenteet ja algoritmit, Antti Laaksonen](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)
Wikipedia: [Dijkstran algoritmi](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) sekä [IDA*](https://en.wikipedia.org/wiki/Iterative_deepening_A*), myös [täältä](https://www.algorithms-and-technologies.com/iterative_deepening_a_star/python) haettu tietoa.
