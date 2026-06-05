---
lang: sk
title: "10.2. Elastické údaje"
---

# 10.2. Elastické údaje

10.2.1. Youngov modul

10.2.2. Poissonov pomer

10.2.3. Tepelná rozťažnosť

10.2.4. Referenčná teplota materiálu

[10.2.5. Hyperelastic](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_5_hyperelastic/)

Na analýzu deformácie elastických a elastoplastických materiálov sú potrebné elastické údaje. Na opis vlastností pre elastickú deformáciu sa používajú tri premenné: Youngov modul, Poissonov pomer, tepelná rozťažnosť a hyperelastickosť, ako je znázornené na obr. 10.2.1.

![]({{ '/assets/images/pre-processor/10_material_data/10_2_elastic_data/10_2_image001.jpg' | relative_url }})

Okno s údajmi o elastickom materiáli

  
  
Poznámka:
Ak chcete aktivovať možnosť referenčnej teploty, musí byť koeficient tepelnej rozťažnosti funkciou teploty.

## Youngov modul

Youngov modul ([YOUNG](/docs/sk/keyword_documentation/y/young/)) sa používa pre elastické materiály a elastoplastické materiály pod hranicou klzu. Môže byť definovaný ako konštanta alebo ako funkcia teploty, hustoty (pre práškové kovy), dominantného obsahu atómov (napríklad obsahu uhlíka) alebo ako funkcia teploty a obsahu atómov.

## Poissonov pomer

Poissonov pomer ([POISON](/docs/sk/keyword_documentation/p/poison/)) je pomer medzi osovými a priečnymi deformáciami. Vyžaduje sa pre pružné a elasto-plastické materiály. Môže byť definovaný ako konštanta alebo ako funkcia teploty, hustoty (v prípade práškových kovov), dominantného obsahu atómov (napríklad obsahu uhlíka) alebo ako funkcia teploty a obsahu atómov.

## Tepelná rozťažnosť

Koeficient tepelnej rozťažnosti ([EXPAND](/docs/sk/keyword_documentation/e/expand/)) definuje objemovú deformáciu spôsobenú zmenami teploty. Môže byť definovaný ako konštanta alebo ako funkcia teploty.  
Pre pružné telesá je zmena teploty definovaná ako rozdiel medzi uzlovými teplotami a zadanou referenčnou teplotou ([REFTMP](/docs/sk/keyword_documentation/r/reftmp/)):

![]({{ '/assets/equations/pre_processor/10_material_data/10_2_elastic_data/eq_10_2_3_1.jpg' | relative_url }}) |
---|---
  
  
V prípade elasto-plastických telies je vstupom tepelnej rozťažnosti v predprocesore priemerná hodnota tepelnej rozťažnosti a MKP vypočíta okamžitú (tangenciálnu) hodnotu z priemernej hodnoty.

![]({{ '/assets/equations/pre_processor/10_material_data/10_2_elastic_data/eq_10_2_3_2.jpg' | relative_url }}) |
---|---
  
  
K dispozícii sú experimentálne údaje o tepelnej rozťažnosti a konverzné nástroje.  
Používateľské rozhranie teraz umožňuje buď priame zadanie koeficientu tepelnej rozťažnosti tangensu ako funkcie teploty, alebo môže používateľ importovať aj okamžité hodnoty, ak sú k dispozícii z experimentálnych údajov. (Pozri obr. 10.2.2.) Pri importovaní okamžitých hodnôt musí používateľ uviesť, či sú záznamy založené na skúškach ohrevu alebo chladenia, a referenčnú teplotu. Tieto okamžité údaje o tepelnej rozťažnosti možno previesť na priemerné údaje. (Nazýva sa aj sekantný, čo je požiadavka na údaje z hľadiska modelu). V každom okamihu môže používateľ vidieť buď pôvodné údaje ako importované, alebo konvertované údaje, alebo oboje. Tieto údaje možno tiež importovať a exportovať ako textové súbory. Tieto tabuľkové údaje možno tiež vystrihnúť a vložiť z a do tabuľky údajov programu Excel (v systémoch PC).

![]({{ '/assets/images/pre-processor/10_material_data/10_2_elastic_data/10_2_3_image001.jpg' | relative_url }})

Zariadenia na konverziu údajov pre údaje o funkcii tepelnej rozťažnosti

## Referenčná teplota materiálu

Referenčná teplota ([REFTMP](/docs/sk/keyword_documentation/r/reftmp/)) platí len pre výpočet tepelnej rozťažnosti plastových objektov Elastic a Elasto, táto hodnota sa používa ako referenčná teplota pre výpočet tepelnej rozťažnosti. Pre modely alebo objekty Elasto-Plastic sa (počnúc verziou DEFORM v11) vždy používa referenčná teplota definovaná v dialógovom okne s údajmi o materiáli. Pre elastické modely alebo objekty, ak je tepelná rozťažnosť objektu konštantná, použije sa referenčná teplota objektu (pozri Referenčná teplota vlastností objektu). Pre elastické modely alebo objekty, ak je tepelná rozťažnosť funkciou teploty, použije sa referenčná teplota definovaná v dialógovom okne s údajmi o materiáli.

[10.2.5. Hyperelastic](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_5_hyperelastic/)
