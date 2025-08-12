# Testausdokumentti

## Testaus

Unittestit voi käydä läpi "src"-directoryssä komennolla "python -m unittest".
Unittesteillä on testattu algoritmien toiminta vertaamalla generoitujen verkkojen läpikäynnin tuloksia
itserakennetulla algoritmilla vs NetworkX:n tarjoamalla algoritmillä. Testit tarkastavat, saavatko algoritmit samat tulokset samassa verkossa. Näin ollen oman algoritmin täytyy toimia oikein, sillä suurissa verkoissa oikeaa tulosta ei saa sattumanvaraisesti.

## Kattavuusraportti

Coverage report:

![Covreport](https://i.imgur.com/8E9sIIm.jpg)

Eli testauscoverage 90% paikkeilla, netxfuncs sisältää lähinnä parametrien asettamista NetworkX:n metodeihin

Coveragen voi testata itse asentamalla Coveragen esim. pipillä, ja runnaamalla testit

 > python -m coverage run -m unittest

 Ja sen jälkeen tekemällä niistä coverage-kansioon html-tiedoston komennolla 

 > python -m coverage html

 Komennot voivat hieman vaihdella käytetyn järjestelmän mukaan.