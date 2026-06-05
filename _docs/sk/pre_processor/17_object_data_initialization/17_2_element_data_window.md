---
lang: sk
title: "17.2. Okno s údajmi o prvku"
---

# 17.2. Okno s údajmi o prvku ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }})

17.2.1. Funkcie okna zobrazenia zahŕňajú v okne Element Data

17.2.2. Inicializácia údajov prvkov

17.2.3. Karta Deformácia

  * Karta Všeobecné

  * Stresové komponenty Tab

  * Karta Komponenty stresu späť

  * Karta Komponenty kmeňa

  * Záložka pre rýchlosť kmeňa

  * Mat. Uhlová záložka

17.2.4. Karta tvrdosti

  * Tvrdosť

  * Čas chladenia

17.2.5. Karta Elektrické vykurovanie

  * Intenzita elektrického poľa R

  * Intenzita elektrického poľa I

17.2.6. Karta Mikroštruktúra

  * Karta Obilniny

  * Karta Fáza

17.2.7. Karta Veľkosť

17.2.8. Karta Textúra

17.2.9. Záložka Používateľ

17.2.10. Termomechanická karta

17.2.11. Karta Aditívna výroba

**[2D, 3D]** : V dialógovom okne s údajmi o prvkoch môže používateľ preskúmať kompletný súbor údajov o prvkoch, ktoré sa vzťahujú na daný model (pozri obr. 17.2.1 a obr. 17.2.2). Tieto údaje zahŕňajú, napätie, deformáciu, rýchlosť deformácie, materiálovú os, tvrdosť, údaje o transformácii, údaje o ohreve, údaje o zrnách a používateľom definované prvkové premenné.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image001.jpg' | relative_url }})

Deformácia prvkov Okno všeobecných údajov pre 2D

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image002.jpg' | relative_url }})

Deformácia prvkov Okno všeobecných údajov pre 3D

V okne prvkov sa zobrazia všetky dostupné informácie o prvkoch. Všetky informácie možno upravovať a mnohé premenné možno vykresliť.

## Funkcie zobrazovacieho okna patria do okna Element Data

**Element** :

Číslo prvku, pre ktorý sa zobrazujú informácie. Prvok možno vybrať buď zadaním hodnoty kľúčom, alebo pomocou ikony výberu a kliknutím myšou na prvok.

**Elemental Connectivity** (ELMCON):

Spojitosť prvku ([ELMCON](/docs/sk/keyword_documentation/e/elmcon/)) určuje čísla 4 alebo 8 uzlov, ktoré definujú rohy prvku.

**Zvýrazňujúci prvok** : Zvýraznenie vybraného prvku na grafickom displeji.

**Inicializácia hodnôt** : Ikona ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) inicializuje zadanú hodnotu premennej na Element v objekte pre,

  * konkrétny prvok

  * Rozsah prvku

  * Výber prvku pomocou nástrojov na výber (pozri obr. 17.2.3 a obr. 17.2.4)

  * Metóda interpolácie

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image003.jpg' | relative_url }})

Výber nástrojov na výber prvku pre 2D

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image004.jpg' | relative_url }})

Výber nástrojov na výber prvku pre 3D

**Premenná na grafe:**

![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) Vykresľuje vybranú stavovú premennú prvku v tieňovanom obryse.

Typ grafu možno zmeniť kliknutím pravým tlačidlom myši na obrysový pruh v okne zobrazenia.

## Inicializácia údajov prvku

Dáta môžeme inicializovať pomocou dvoch metód, metódy Priradenie a Interpolácia.

Máme ďalšie dve možnosti:

**Rozsah** : Pomocou možnosti Range môže používateľ definovať číslo počiatočného prvku a číslo koncového prvku a hodnotu premennej. Po definovaní parametrov, keď používateľ klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), sa údaje inicializujú na vybrané uzly.

**Vyberanie** : Pomocou možnosti výberu môže používateľ vybrať prvky na inicializáciu hodnoty.

V súvislosti s možnosťami výberu pozri 14. Hraničné podmienky [Picking options for 2D](../14_boundary_conditions/14_boundary_conditions.htm#Picking_option_for_2D) a [Picking options for 3D](../14_boundary_conditions/14_boundary_conditions.htm#Picking_option_for_3D).

## Karta Deformácia **[2D, 3D]**

**Všeobecná karta**

  * **Materiál (MTLGRP)** : [MTLGRP](/docs/sk/keyword_documentation/m/mtlgrp/) udáva číslo materiálu priradené ku každému prvku.

  * **Hustota (DENSTY)** : [DENSTY](/docs/sk/keyword_documentation/d/densty/) udáva relatívnu hustotu materiálu v každom prvku. [DENSTY](/docs/sk/keyword_documentation/d/densty/)sa používa, keď sa simuluje porézny materiál s relatívnou hustotou menšou ako 1,0. Ak nie je pre hustotu zadaná žiadna hodnota, predpokladá sa, že je 1,0. Napätie pri prúdení poréznych objektov by sa malo špecifikovať pre úplne hustý materiál.

  * **Eff. Napätie** **(STRAIN)** : [STRAIN](/docs/sk/keyword_documentation/s/strain/) udáva hodnotu celkovej efektívnej deformácie v strede každého prvku. Deformácie prvkov sa interpolujú medzi sieťami počas postupov remeshingu. Keď používateľ vyberie "Integračný" typ výstupu Element/Nodal pre Strain v rámci Simulation controls![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Advanced options ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) [Advanced output](../9_simulation_controls/9_7_advanced_options.htm#9.7.4._Output_Control), pre objekt Brick mesh môžeme pozorovať 8 hodnôt integračných výstupov pre každý prvok, ako je znázornené na obr. 17.2.5. Používateľ môže tiež inititizovať hodnoty pre jednotlivé integračné body. Dokonca aj pre varianty stavu poškodenia a napätia je k dispozícii možnosť výstupu typu "Integrácia" Element/Nodal.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image005.jpg' | relative_url }})

Eff.Strain Zobrazenie integračného bodu v okne údajov o prvku

  * **Poškodenie (DAMAGE) :**[DAMAGE](/docs/sk/keyword_documentation/d/damage/) určuje faktor poškodenia v každom prvku na základe modelu vybraného v dialógovom okne materiálu. Faktor poškodenia možno použiť na predpovedanie lomu pri operáciách tvárnenia za studena. Faktor poškodenia sa zvyšuje s deformáciou materiálu. Lom nastane, keď faktor poškodenia dosiahne svoju kritickú hodnotu.

**Záložka komponentov stresu (STRESS)**
**[2D, 3D]**[STRESS](/docs/sk/keyword_documentation/s/stress/) definuje tenzory napätia každého prvku objektu. (Pozri obr. 17.2.6.)

V 2Dplošnom modeli deformácie sú zobrazené hodnoty X/R hodnota ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_x.png' | relative_url }}) , Y/Z je ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_y.png' | relative_url }}), Z/Theta je ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_z.png' | relative_url }}) a XY/RZ je ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/tou_xy.png' | relative_url }}).

V 2D osovo symetrickom modeli sú zobrazené hodnoty X/R hodnotou ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_r.png' | relative_url }}), Y/Z je ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_z.png' | relative_url }}), Z/Theta je ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_theta.png' | relative_url }}) a XY/RZ je ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/tou_rz.png' | relative_url }}).

V 3D sa zobrazujú hodnoty napätia ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_x.png' | relative_url }}),![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_y.png' | relative_url }}) , ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_z.png' | relative_url }}),![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_xy.png' | relative_url }}) , ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_yz.png' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_zx.png' | relative_url }}).

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image006.jpg' | relative_url }})

Komponent napätia v okne údajov o prvku pre 3D

**Záložka Komponenty záťaže (YLDS)**
**[2D, 3D]**[YLDS](/docs/sk/keyword_documentation/y/ylds/) určuje translačný tenzor povrchu klzu pre kinematické spevnenie. V prípade izotropného spevnenia zostávajú všetky tieto hodnoty nulové. (Pozri obr. 17.2.7.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image007.jpg' | relative_url }})

Spätné napätie v dátovom okne prvku pre 3D

**Záložka Komponenty ťahu**
**[2D, 3D]** Určuje tenzor deformácie každého prvku objektu (pozri obr. 17.2.8).

Ak chceme aktivovať výstup deformačnej zložky, musíme vybrať zaškrtávacie políčko Typ výstupu deformačnej zložky ako Plastická, Pružná, Creepová, Transformačná a tepelná volumetrická a Transformačná volumetrická v záložke Simulation control [Advanced output](../9_simulation_controls/9_7_advanced_options.htm#9.7.4._Output_Control).

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image008.jpg' | relative_url }})

Komponent deformácie v okne Element data pre 3D

**Tabuľka rýchlosti ťahu**
Určuje tenzory miery deformácie každého prvku objektu.

V 2D sa hodnoty pre X/R, Y/Z, Z/Theta, XY/RZ zadávajú kliknutím na tlačidlo inicializovať, aby sa vypočítalo maximálne hlavné napätie a minimálne hlavné napätie pre konkrétny prvok. Toto je užitočnejšie po dokončení simulácie, takže hlavné napätie možno skontrolovať pre každý prvok buď výberom čísla prvku, alebo len kliknutím na konkrétny prvok objektu.

**Mat. Uhlová karta (MATAXI)**
Uhol materiálu ([MATAXI](/docs/sk/keyword_documentation/m/mataxi/)) meria veľkosť a smer otáčania okolo osi Z (kolmej na rovinu obrazovky). Smer sa riadi pravidlom pravej ruky, kde proti smeru hodinových ručičiek je kladný a v smere hodinových ručičiek je záporný. Jednotky uhla sú v radiánoch.

## Tabuľka tvrdosti

**[2D, 3D]** Dialóg s údajmi o tvrdosti prvkov pozri na obr. 17.2.9.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image009.jpg' | relative_url }})

Okno s údajmi o tvrdosti prvkov

  * **Hardness****(HDNOBJ1)** : Tvrdosť ([HDNOBJ1](/docs/sk/keyword_documentation/h/hdnobj/)) udáva hodnotu tvrdosti pre každý prvok.

  * **Čas chladenia (HDNOBJ2)** : Čas chladenia ([HDNOBJ2](/docs/sk/keyword_documentation/h/hdnobj/)) určuje čas chladenia z vysokej teploty na nízku teplotu pre každý prvok. Tento údaj sa môže použiť v spojení s údajmi Jominyho na určenie hodnoty tvrdosti.

## Elektrická vykurovacia karta

**[2D, 3D]** Dialógové okno s údajmi o prvkoch elektrického vykurovania pozri na obr. 17.2.10.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image010.jpg' | relative_url }})

Okno s údajmi o elektrickom ohreve Elemental pre indukčný ohrev Typ

**Intenzita elektrického poľa R :** je skutočná hodnota intenzity elektrického poľa každého prvku.

**Intenzita elektrického poľa I :** je imaginárna hodnota intenzity elektrického poľa každého prvku.

## **Záložka mikroštruktúry**

**Zrnková tabuľka**
**[2D, 3D]** Toto sú hodnoty prvkov pre všetky rôzne premenné stavu zrna. (Pozri obr. 17.2.11.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image011.jpg' | relative_url }})

Okno s údajmi o premennej Elemental Grain

Karta **Fáza (transformácia)**
Dialóg s údajmi o fázovej transformácii elementárnej mikroštruktúry je uvedený na obr. 17.2.12.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image012.jpg' | relative_url }})

Okno s údajmi o premennej Transformácia fázy prvkov

  * **Aktuálny objemový podiel (VOLFC):**[VOLFC](/docs/sk/keyword_documentation/v/volfc/) určuje počiatočný objemový podiel fázy (materiálu) v prvku na začiatku simulácie. Okrem toho sa počas celej simulácie v [VOLFC](/docs/sk/keyword_documentation/v/volfc/) ukladá objemový podiel všetkých fáz v každom prvku v každom kroku. Objemový podiel sa určuje z kľúčového slova [TTTD](/docs/sk/keyword_documentation/t/tttd/), ktoré špecifikuje model alebo údaje použité pri výpočte objemového podielu každej fázy. Je dôležité, aby používateľ zadal potrebné vstupné údaje pre kľúčové slovo [TTTD](/docs/sk/keyword_documentation/t/tttd/), inak sa objemový zlomok ([VOLFC](/docs/sk/keyword_documentation/v/volfc/) ) pre objekt nevypočíta. Používateľ musí zadať typ difúzneho modelu a aspoň dve časovo-teplotné krivky, začiatok transformácie a koniec transformácie.

  * **Východiskový objemový zlomok (VOLFS) :**[VOLFS](/docs/sk/keyword_documentation/v/volfs/) určuje hranicu objemového zlomku fázy v prvku objektu. [VOLFS](/docs/sk/keyword_documentation/v/volfs/) sa do databázy ukladá len na začiatku novej fázovej premeny, napr. austenit![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) perlit alebo austenit ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) martenzit. Zámerom [VOLFC](/docs/sk/keyword_documentation/v/volfc/) je zabezpečiť, aby množstvo objemového zlomku transformovaného z austenitu ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) perlitu neprekročilo objemový zlomok austenitu pred transformáciou. Treba poznamenať, že [VOLFC](/docs/sk/keyword_documentation/v/volfc/) sa líši od [VOLFS](/docs/sk/keyword_documentation/v/volfs/) v tom, že [VOLFC](/docs/sk/keyword_documentation/v/volfc/) ukladá objemový podiel fáz v každom kroku. Zvyčajne sa používateľ bude zaoberať zadávaním objemových podielov pre [VOLFS](/docs/sk/keyword_documentation/v/volfs/) len na začiatku simulácie.

  * **Zmena objemového podielu (DVOLF) :**[DVOLF](/docs/sk/keyword_documentation/d/dvolf/) udáva zmenu objemového podielu všetkých rôznych fáz, ktoré sú výsledkom transformácie počas každého časového kroku. [DVOLF](/docs/sk/keyword_documentation/d/dvolf/) každej fázy je pri simulácii na začiatku nastavená na nulu. [DVOLF](/docs/sk/keyword_documentation/d/dvolf/) sa určuje pre každý krok, kde f je objemový podiel konkrétnej fázy. [DVOLF](/docs/sk/keyword_documentation/d/dvolf/) sa používa pri výpočte latentného tepla v dôsledku transformácie a zmeny objemu objektu. [DVOLF](/docs/sk/keyword_documentation/d/dvolf/) môže byť neoceniteľný pri určovaní priebehu transformácie a pomôcť používateľovi pri rozhodovaní, či zvýšiť alebo znížiť časový krok pre konkrétnu transformáciu.

  * **Inkubačný čas (TICF):**[TICF](/docs/sk/keyword_documentation/t/ticf/) (spotreba inkubačného času) udáva časový úsek, ktorý uplynul, kým sa začala transformácia. Vypočíta sa pre difúzny typ transformácie takto: [TICF](/docs/sk/keyword_documentation/t/ticf/) = kde je prírastok času a je inkubačný čas pri teplote. Premenná celkom závisí od teploty. Ak sa dosiahne [TICF](/docs/sk/keyword_documentation/t/ticf/), transformácia sa začne. Tento inkubačný čas nie je vstupným údajom, ale vypočíta ho MKP.

## Veľkosť karty

## Karta Textúra

## Karta používateľa

**[2D,3D]** Tu sa môžu inicializovať, definovať alebo skúmať údaje pre premenné používateľských prvkov ([USRELM](/docs/sk/keyword_documentation/u/usrelm/)).

Hodnoty premenných užívateľských prvkov možno definovať pomocou podprogramov jazyka FORTRAN. [Refer chapter 56 section USRUPD subroutines.](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_3_User_defined_node_and_element_value_\(USRUPD\)) Každá hodnota prvku môže akceptovať názov aj hodnotu. (Pozri obr. 17.2.13.) Takisto možno definovať nekonečný počet premenných. Štandardne sa definujú minimálne 2 premenné používateľských prvkov, používateľ ich však môže zvýšiť na ľubovoľne veľký počet. Používateľ musí byť opatrný, že veľký počet definovaných premenných môže viesť k veľkému databázovému súboru.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image013.jpg' | relative_url }})

Okno s údajmi o používateľských premenných Elemental

## Termomechanická karta

**[2D, 3D]** V časti Simulation controls - [Thermomechanical](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/) variable page (Ovládacie prvky simulácie - stránka s premennými [Thermomechanical](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)) sa pridané premenné súvisiace s údajmi prvku zobrazia v záložke Thermomechanical variable (Termomechanická premenná) ( [ERECID](/docs/sk/keyword_documentation/e/erecid/)) v okne Element data (Údaje prvku), ako je znázornené na obr. 17.2.14. Hodnota termomechanickej premennej sa tu môže inicializovať alebo preskúmať.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image014.jpg' | relative_url }})

Okno s údajmi o termomechanických premenných prvkov

## Karta aditívnej výroby

**[3D]** V záložke Aditívna výroba ([LAYRID](/docs/sk/keyword_documentation/l/layrid/)) môže používateľ definovať ID vrstvy pre narezané vrstvy objektu, ktoré sa používajú pre proces aditívnej výroby (pozri obr. 17.2.15.). Aj po vykonaní [Slice Layers](../18_object_manipulation_tools/18_1_boolean.htm#Fig_18_1_8_Slice_layers_page) na stránke [Boolean](/docs/sk/pre_processor/18_object_manipulation_tools/18_1_boolean/) môže používateľ priradiť Layer ID (ID vrstvy) pre jednotlivé nakrájané vrstvy na stránke 3D Geometry Examine (Preskúmanie 3D geometrie).

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image015.jpg' | relative_url }})

Aditívna výroba Okno s premennými údajmi o prvkoch

**Súvisiace témy:**

[17\. Object Data Initialize](/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[17.1. Node Data Window](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/)

[17.3. Data Interpolation Window](/docs/sk/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/)
