---
lang: sk
title: "43. Úvod do valcovania profilov"
---

# 43\. Úvod do valcovania profilov

Nastavenie šablóny operácie valcovania tvarov je určené na usmerňovanie používateľa pri nastavovaní rôznych typov procesov valcovania. Typické nastavenie valcovania tvarov pozostáva z obrobku, valcov (horný a spodný valec), posúvača a stola (pozri obr. 43.2). Pomocou tejto šablóny používateľ modeluje operáciu valcovania tvarov ako:

  1. Lagrangeov typ s valením

  2. Typ ALE v ustálenom stave

Proces tvarového valcovania je možné nastaviť ako kombináciu priechodov a stojov spolu s operáciami prenosu tepla medzi jednotlivými priechodmi. Používateľ má k dispozícii tabuľku priechodov a tabuľku stojov, v ktorých môže definovať údaje o procese v jednoduchom tabuľkovom formáte, ako je znázornené na obr. 43.1.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/image0001.jpg' | relative_url }})

Definovanie viacerých priechodov v tabuľke priechodov

Proces tvarového valcovania je možné nastaviť pomocou 2D prierezov obrobku a valca; toto 2D nastavenie možno použiť na simuláciu 2,5D procesu. Typické prierezy valcov sú k dispozícii ako primitívy na definovanie drážok valcov. 2D nastavenie je možné previesť do 3D pomocou možností 3D konverzie dostupných v šablóne. Používateľ môže vykonať potrebné úpravy 3D nastavenia na úrovni priechodu a definovať údaje, ako sú objekt posúvača, nastavenia siete, kritériá pregenerovania siete, inicializácia deformácie, boolovské operácie medzi priechodmi atď. Typické nastavenia valcovania pre Lagrangeovské a ALE valcovanie sú uvedené nižšie: 

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/image0002.jpg' | relative_url }})

Nastavenie typu Lagrangeovho valenia

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/image0003.jpg' | relative_url }})

Nastavenie typu ALE s valcovaním v ustálenom stave

**Súvisiace témy:**

[43.1. Shape Rolling Manual](/docs/en/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/)
