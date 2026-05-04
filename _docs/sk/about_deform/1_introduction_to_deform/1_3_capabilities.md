---
lang: sk
title: "1.3. Schopnosti"
---

# 1.3. Schopnosti

1.3.1. Deformácia

1.3.2. Tepelné spracovanie

## Deformácia

  * Spájané modelovanie deformácie a prenosu tepla na simuláciu procesov kovania za studena, za tepla alebo za tepla (všetky výrobky).

  * Rozsiahla [material database](/docs/sk/pre_processor/10_material_data/10_material_data/) pre mnohé bežné zliatiny vrátane ocelí, hliníka, titánu a superzliatin. (všetky výrobky).

  * Zadanie údajov o materiáli definovaných používateľom pre akýkoľvek materiál, ktorý nie je zahrnutý v [material database](/docs/sk/pre_processor/10_material_data/10_material_data/). (všetky výrobky).

  * Informácie o toku materiálu, plnení zápustky, zaťažení výkovku, napätí v zápustke, toku zŕn, tvorbe defektov a tvárnom lome (všetky výrobky).

  * Tuhé, pružné a termo-viskoplastické modely materiálov, ktoré sú ideálne na modelovanie veľkých deformácií (všetky produkty).

  * Elasticko-plastický materiálový model pre problémy zvyškového napätia a spätnej pružiny. (2D, 3D).

  * Model porézneho materiálu na modelovanie tvarovania výrobkov práškovej metalurgie (2D, 3D).

  * Integrované modely tvárniacich zariadení pre hydraulické lisy, kladivá, skrutkové lisy a mechanické lisy (všetky výrobky).

  * [User defined subroutines](/docs/sk/user_routines/56_user_routines_in_deform/56_1_introduction_to_user_routines/) na modelovanie materiálov, modelovanie lisov, lomové kritériá a ďalšie funkcie (2D, 3D).

  * Vstavaná funkcia Flownet je možnosť, pomocou ktorej môže používateľ pred simuláciou databázového súboru definovať hodnotu flownet na vizualizáciu prípadných nepravidelností v štruktúre zrna alebo na zobrazenie potenciálnych povrchových defektov.

  * FLOWNET (2D, 3D) a sledovanie bodov (všetky produkty) pre dôležité informácie o toku materiálu.

  * Oblasť záujmu (ROI), ľubovoľný tvar (2d alebo 3d), ktorý definuje oblasť, z ktorej sa zhromažďujú informácie o objekte. Tieto oblasti možno použiť na získanie min/max hodnôt stavových premenných z konkrétnej časti na objekte (2D, 3D).

  * Kupóny Extrakcia údajov na vyhodnotenie mikroštruktúry a mechanických vlastností konkrétnej rezanej časti (2D, 3D).

  * Postprocesor bol rozšírený o výstupy simulácie vo formáte .pdf (3D) a .ppt. To umožňuje používateľovi väčšiu flexibilitu pre [report generation](/docs/sk/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/) (2D, 3D).

  * Obrysové grafy teploty, deformácie, napätia, poškodenia a ďalších kľúčových premenných zjednodušujú následné spracovanie (všetky produkty).

  * Podmienka vlastného kontaktu s robustným remeshingom umožňuje pokračovať v simulácii až do konca aj po vytvorení oblúka alebo záhybu (2D, 3D).

  * Možnosť viacnásobnej deformácie telesa umožňuje analýzu viacnásobne deformujúcich sa obrobkov alebo spojenú analýzu napätia v zápustke. (2D, 3D).

  * Modely iniciácie a šírenia trhlín založené na dobre známych faktoroch poškodenia umožňujú modelovanie strihania, zasekávania, prepichovania a obrábania (2D, 3D).

## Tepelné spracovanie

Simulujte normalizáciu, žíhanie, kalenie, popúšťanie a nauhličovanie.

**Normalizácia (zatiaľ nie je k dispozícii)**

Zahriatie zliatiny železa na vhodnú teplotu nad rozsahom premeny a ochladenie na vzduchu na teplotu podstatne nižšiu ako rozsah premeny.

**Žíhanie**

Všeobecný pojem označujúci úpravu pozostávajúcu zo zahriatia na vhodnú teplotu a jej udržiavania, po ktorej nasleduje ochladzovanie vhodnou rýchlosťou, používanú predovšetkým na zmäkčenie kovových materiálov. V prípade železných zliatin sa žíhanie zvyčajne vykonáva nad hornou kritickou teplotou, ale časovo-teplotné cykly sa značne líšia tak v maximálnej dosiahnutej teplote, ako aj v použitej rýchlosti chladenia.

**Temperovanie**

Popúšťanie martenzitu je difúzny proces a možno ho modelovať pomocou modelov časovej teplotnej transformácie s martenzitom ako materskou fázou a popúšťaným martenzitom (alebo inými produktmi podľa potreby) ako podriadenou fázou (fázami).

**Zmiernenie stresu**

Zahriatie na vhodnú teplotu, dostatočne dlhé udržiavanie na zníženie zvyškových napätí a potom dostatočne pomalé ochladzovanie, aby sa minimalizoval vznik nových zvyškových napätí.

**Zdravenie**

Rýchle chladenie, ktorého účelom je kontrola mikroštruktúry a fázových produktov.

  * Predpovedať tvrdosť, objemový podiel kovovej štruktúry, deformáciu a obsah uhlíka.

  * Špecializované modely materiálov pre tečenie, fázovú transformáciu, tvrdosť a difúziu.

  * Na predpovedanie rozloženia tvrdosti konečného výrobku možno použiť údaje Jominy.

  * Modelovanie viacerých materiálových fáz, z ktorých každá má vlastné elastické, plastické, tepelné a tvrdostné vlastnosti. Výsledné vlastnosti materiálu zmesi závisia od percentuálneho podielu každej fázy prítomnej v ktoromkoľvek kroku simulácie tepelného spracovania.

DEFORM modeluje komplexnú interakciu medzi deformáciou, teplotou a v prípade tepelného spracovania aj transformáciou a difúziou. Medzi celým javom existuje väzba, ako je znázornené na obr. 1.3.1. nižšie. Ak sú licencované a aktivované príslušné moduly, tieto väzbové efekty zahŕňajú ohrev v dôsledku deformačnej práce, tepelné zmäkčenie, teplotne riadenú transformáciu, latentné teplo transformácie, transformačnú plasticitu, transformačné napätia, vplyv napätia na transformáciu a vplyv obsahu uhlíka na všetky vlastnosti materiálu.

[DEFORM HT](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/) umožňuje nastavenie operácií tepelného spracovania v cykloch za sebou a ich postupnú simuláciu.

![]({{ '/assets/images/about_deform/1_3_capabilities/1_3_image001.jpg' | relative_url }})

Vzťah medzi rôznymi modulmi DEFORM

**Súvisiace témy:**

[PRE-PROCESSOR](/docs/sk/pre_processor/7_introduction_to_pre-processor/)

[POST-PROCESSOR](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[INV. HEAT TRANSFER](/docs/sk/inverse_heat/51_introduction_to_inverse_heat/)

[HEAT TREATMENT](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/)

[Integrated Manufacturing Process](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/) (MO)

[HT FURNACE](/docs/sk/operation_templates/38_furnace_heating/38_introduction_to_3d_ht_furnace/)
