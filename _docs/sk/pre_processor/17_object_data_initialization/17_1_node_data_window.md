---
lang: sk
title: "17.1. Okno s údajmi o uzle"
---

# 17.1. Okno s údajmi o uzle ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }})

17.1.1. Funkcie zobrazovacieho okna v okne Node Data zahŕňajú

17.1.2. Inicializácia uzlových údajov

17.1.3. Karta Deformácia

  * Karta Všeobecné

  * Premiestnenie

  * Rýchlosť

  * Sila

  * Tlak

  * Deformácia BCC

  * Funkcia BCC

  * Kmeň (uzol)

  * Poškodenie(Nodal)

  * Stres(Nodal) Tab

17.1.4. Tepelná karta

  * Teplota uzla

  * Teplo

  * Tepelný tok

  * Tepelné BCC

  * Funkcia hraničných podmienok

  * Difúzna väzba

17.1.5. Karta Difúzia

  * Percentuálny podiel atómov

  * Difúzny tok

  * Difúzia BCC

17.1.6. Karta Elektrické vykurovanie

  * Intenzita elektrického poľa

  * Odolnosť BCC

  * Prúdový tok

17.1.7. Karta Používateľ

17.1.8. Termomechanická premenná Tab

17.1.9. Karta Aditívna výroba

[**2D,3D**]: Okno s údajmi o uzloch zobrazuje všetky dostupné informácie o uzloch. Všetky informácie možno upravovať a mnohé z premenných možno vykresliť, ako je znázornené na obr. 17.1.1. a obr. 17.1.2.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image001.jpg' | relative_url }})

2D deformácia uzlov - okno všeobecných údajov

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image002.jpg' | relative_url }})

Deformácia 3D uzla - okno všeobecných údajov

## Funkcie zobrazovacieho okna sú zahrnuté v okne Node Data

**Číslo uzla** : Číslo uzla, pre ktorý sa zobrazujú informácie. Uzol možno vybrať buď zadaním hodnoty kľúčom, alebo použitím ikony výberu a kliknutím myšou na uzol.

**Zvýraznenie uzla** : Zvýraznenie vybraného uzla na grafickom displeji.

**Inicializácia hodnôt** :![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) ikona inicializuje zadanú hodnotu premennej v uzloch objektu pre,

  * konkrétny uzol
  * rozsah uzlov
  * Výber uzlov pomocou nástrojov na výber (pozri obr. 17.1.3 a obr. 17.1.4)
  * metóda interpolácie

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image003.jpg' | relative_url }})

Nástroje na výber uzla pre 2D

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image004.jpg' | relative_url }})

Nástroje na výber uzla pre 3D

**Premenná na grafe** :

![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) Vykreslí stavovú premennú vybraného uzla v tieňovanom obryse.

![]({{ '/assets/icons/pre_icons/mo_plot_vector_icon.jpg' | relative_url }}) Vykreslí stavovú premennú vybraného uzla Vektorový graf.

Typ grafu možno zmeniť kliknutím pravým tlačidlom myši na obrysový pruh v okne zobrazenia.

**Súradnica uzla** :

Súradnice uzla sa zobrazia vedľa čísla uzla. Hodnoty možno upraviť, aby sa mierne upravila poloha uzlov, v ktorých neboli správne uplatnené okrajové podmienky. Toto by sa malo robiť s VYŠŠOU opatrnosťou. V prípade funkcií, ako je extrakcia hraníc a generovanie siete, sa musí databáza uložiť a novo uložený krok načítať do predprocesora predtým, ako sa môžu použiť upravené súradnice.

## Inicializácia uzlových údajov

Dáta môžeme inicializovať pomocou dvoch metód, metódy Priradenie a Interpolácia.

Máme ďalšie dve možnosti:

**Rozsah** : Pomocou možnosti Rozsah môže používateľ definovať číslo počiatočného uzla a číslo koncového uzla a hodnotu premennej. Po definovaní parametrov, keď používateľ klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), údaje sa inicializujú na vybrané uzly.

**Vyberanie** : Pomocou možnosti výberu môže používateľ vybrať uzly na inicializáciu hodnoty.

V súvislosti s možnosťami výberu pozri 14. Hraničné podmienky [Picking options for 2D](../14_boundary_conditions/14_boundary_conditions.htm#Picking_option_for_2D) a [Picking options for 3D](../14_boundary_conditions/14_boundary_conditions.htm#Picking_option_for_3D).

**Priradenie metódy** : ****

**Interpolačná metóda:**

## Deformačná karta [2D, 3D]

**Všeobecná karta**

  * **Posun (DRZ) :** Posun ([DRZ](/docs/sk/keyword_documentation/d/drz/)) uchováva posun každého uzla od posledného remesingu. V prípade pružných objektov sa môže určiť posunutie pre interferenčné uloženia. Pružné zotavenie objektu spôsobí, že sa vyvinú príslušné hodnoty napätia.

  * **Rýchlosť (URZ) :**[URZ](/docs/sk/keyword_documentation/u/urz/) sú zložky rýchlosti každého uzla.

  * **Sila (FRZ) :**[FRZ](/docs/sk/keyword_documentation/f/frz/) určuje hodnotu konštantnej uzlovej sily v jednotlivých uzloch.

  * **Tlak (PRZ) :**[PRZ](/docs/sk/keyword_documentation/p/prz/) udržiava zadaný normálový tlak alebo šmykovú ťahovú silu na povrchu prvkov ležiacich medzi vybranými hraničnými uzlami.

  * **Deformácia BCC (BCCDEF) :**[BCCDEF](/docs/sk/keyword_documentation/b/bccdef/) určuje okrajovú podmienku deformácie v smeroch X a Y.

Hodnoty kódu sú:

**0** Zadaná sila uzla

**1** X, Y alebo Z zložka rýchlosti uzla obmedzená, zodpovedajúca X, Y alebo Z zložke [BCCDEF](/docs/sk/keyword_documentation/b/bccdef/)

**2** Obmedzené ťahy uzlov určené PRZ

**3** Definované riadenie pohybu uzlov

**-n** Uzol je v kontakte s objektom číslo N.

**Poznámka** : Súčiastka kontaktu X, Y alebo Z nemá žiadny význam. Hodnoty kontaktov sa ukladajú do prvej voľnej zložky, začínajúc Z, potom Y, potom X.

  * **Funkcia BCC (BCCDFN)** : [BCCDFN](/docs/sk/keyword_documentation/b/bccdfn/) určuje, či sa má hodnota deformačného hraničného obmedzenia (uzlovej rýchlosti, sily alebo trakcie) spojená s konkrétnym uzlom špecifikovať ako konštanta alebo ako súbor údajov o časovej/uzlovej hodnote.

  * **Náťah(uzol)** : Strain (nodal) určuje hodnotu Strain v jednotlivých uzloch.

  * **Poškodenie(uzol)** : Deformácia (nodálna) udáva hodnotu Deformácie v jednotlivých uzloch.

**Poznámka** :

Ak chceme aktivovať údaje o deformácii (uzol), poškodení (uzol) a napätí (uzol), musíme aktivovať rádiové tlačidlo Damage Element+Node output, rádiové tlačidlo Strain Element+Node output a rádiové tlačidlo Stress Element+Node output na karte Simulation control [Advanced output](../9_simulation_controls/9_7_advanced_options.htm#9.7.4._Output_Control).

  
******Stress(Nodal) Tab**
Stres uchováva napätie pre každý uzol od posledného remeshingu. Hodnoty napätia sa tu môžu inicializovať pre konkrétny uzol alebo sadu uzlov. Hodnoty pre X/R, Y/Z, Z/Theta, XY/RZ sa zadávajú kliknutím na tlačidlo inicializovať, aby sa vypočítalo Max. hlavné napätie a Min. hlavné napätie pre konkrétny uzol. Toto je užitočnejšie po dokončení simulácie, takže hlavné napätie možno skontrolovať pre každý uzol buď výberom čísla uzla, alebo len kliknutím na konkrétny uzol objektu, ako je znázornené na obr. 17.1.5. a obr. 17.1.6.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image005.jpg' | relative_url }})

Okno s údajmi o uzlovej deformácii a napätí pre 2D

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image006.jpg' | relative_url }})

Okno s údajmi o uzlovej deformácii a napätí pre 3D

## Tepelná karta

**[2D, 3D]** : V tomto dialógovom okne je možné preskúmať, definovať alebo inicializovať všetky tepelné údaje uzlov modelu. (Pozri obr. 17.1.7.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image007.jpg' | relative_url }})

2D okno s uzlovými tepelnými údajmi

  * **Teplota uzla (NDTMP) :**[NDTMP](/docs/sk/keyword_documentation/n/ndtmp/) určuje teplotu uzla, ktorá sa má aplikovať na jednotlivé uzly.

  * **Heat (NDHEAT) :**[NDHEAT](/docs/sk/keyword_documentation/n/ndheat/) určuje uzlové teplo, ktoré sa má aplikovať na jednotlivé uzly.

  * **Tepelný tok (NDFLUX) :**[NDFLUX](/docs/sk/keyword_documentation/n/ndflux/) určuje distribuovaný uzlový tepelný tok, ktorý sa má aplikovať na jednotlivé uzly. Obmedzenie tepelného toku sa uplatní na plochy prvku ležiace medzi vybranými hraničnými uzlami.

  * **Termický BCC (BCCTMP) :**[BCCTMP](/docs/sk/keyword_documentation/b/bcctmp/) určuje kód obmedzenia hranice prestupu tepla pre jednotlivé uzly.

  1. Zadaná je konštantná uzlová teplota
  2. Prenos tepla s okrajovou podmienkou prostredia
  3. Špecifikovaný uzlový tepelný tok

  * **Funkcia hraničných podmienok (BCCTFN) :** [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/) sa používa na zadanie dvojíc časových/uzlových hodnôt pre uzlové hraničné obmedzenia. Typy uzlových okrajových obmedzení, ktoré možno špecifikovať ako dvojice čas/uzolová hodnota, zahŕňajú rýchlosť, silu, trakciu, teplotu, teplo a distribuovaný tepelný tok. [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/) možno použiť len vtedy, keď bol typ funkcie hraničného obmedzenia uzla, [BCCDFN](/docs/sk/keyword_documentation/b/bccdfn/) alebo [BCCTFN](/docs/sk/keyword_documentation/b/bcctfn/), špecifikovaný ako typ časová/uzlová hodnota.

  * **Difúzna väzba :**

## Difúzna karta

**[2D, 3D]** Pre všetky modely so zapnutou difúziou v ovládacích prvkoch simulácie možno v tomto dialógovom okne preskúmať, definovať alebo inicializovať uzlové difúzne údaje pre objekt. (Pozri obr. 17.1.8. a obr. 17.1.9.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image008.jpg' | relative_url }})

Okno s údajmi o uzlovej difúzii pre 2D

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image009.jpg' | relative_url }})

Okno s údajmi o uzlovej difúzii pre 2D

  * **Podiel atómov (DATOM) :**[DATOM](/docs/sk/keyword_documentation/d/datom/) určuje obsah atómov v uzle.

  * **Difúzny tok (CRBFLX)** : [CRBFLX](/docs/sk/keyword_documentation/c/crbflx/) určuje "uhlíkový tok" alebo atómový tok pre povrch obrobku.

  * **Difúzia BCC (BCCCRB)** : [BCCCRB](/docs/sk/keyword_documentation/b/bcccrb/) určuje kód obmedzenia hranice prenosu atómov pre jednotlivé uzly.

## Elektrická vykurovacia karta

**[2D, 3D]** Dialógové okno Elektrický ohrev Uzlové údaje je zobrazené na obr. 17.1.10.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image010.jpg' | relative_url }})

Dátové okno elektrického vykurovania Nodal

  * **Intenzita elektrického poľa** **(VOTAGE)** : Intenzita elektrického poľa ([VOTAGE](/docs/sk/keyword_documentation/v/votage/)) udáva veľkosť napätia dodávaného na ohrev objektu.

  * **Odolnosť BCC** **(BCCRHT)** : Resistance BCC ([BCCRHT](/docs/sk/keyword_documentation/b/bccrht/)) určuje, či sa má hodnota hraničného obmedzenia odporu (uzlovej rýchlosti, sily alebo trakcie) spojená s konkrétnym uzlom špecifikovať ako konštanta alebo ako súbor údajov o časovej/uzlovej hodnote.

  * **Prúdový tok (RHTFLX)** :**** Rýchlosť toku prúdu ([RHTFLX](/docs/sk/keyword_documentation/r/rhtflx/)) dodávaného na ohrev objektu.

## Karta používateľa

**[2D,3D]** Tu sa môžu inicializovať, definovať alebo skúmať údaje pre premenné uzla User ([USRNOD](/docs/sk/keyword_documentation/u/usrnod/)).

Hodnoty premenných užívateľských uzlov možno definovať pomocou podprogramov jazyka FORTRAN. Pozri [Chapter 56 section USRUPD subroutines](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_3_User_defined_node_and_element_value_\(USRUPD\)). Každá hodnota uzla môže akceptovať názov aj hodnotu (pozri obr. 17.1.11.). Taktiež je možné definovať nekonečný počet premenných. Štandardne sa definujú minimálne 2 používateľské premenné uzla, používateľ ich však môže zvýšiť na ľubovoľne veľký počet. Používateľ musí byť opatrný, že veľký počet definovaných premenných môže viesť k veľkému databázovému súboru.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image011.jpg' | relative_url }})

Okno s údajmi o uzlových premenných používateľa

## Termomechanická premenná Tab

**[2D, 3D]** V časti Simulation controls - [Thermomechanical](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/) variable page (Ovládacie prvky simulácie - stránka s premennými [Thermomechanical](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)) sa pridané premenné týkajúce sa uzlových údajov uvedú v záložke Thermomechanical variable (Termomechanická premenná) ( [NRECID](/docs/sk/keyword_documentation/n/nrecid/)) v okne Node data (Údaje uzla), ako je znázornené na obr. 17.1.12. Hodnota termomechanickej premennej sa tu môže inicializovať alebo preskúmať.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image012.jpg' | relative_url }})

Okno s údajmi o uzlových termomechanických premenných

## Karta aditívnej výroby

**[3D]** V záložke Aditívna výroba ([NODDEN](/docs/sk/keyword_documentation/n/nodden/)) môže používateľ definovať hodnotu hustoty uzlov objektu použitého pre proces aditívnej výroby. (Pozri obr. 17.1.13.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image013.jpg' | relative_url }})

3D Nodal okno s údajmi o premenných aditívnej výroby

**Súvisiace témy:**

[17\. Object Data Initialize](/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[17.2. Element Data Window](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/)

[17.3. Data Interpolation Window](/docs/sk/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/)
