---
lang: sk
title: "9.6. Prevádzkové podmienky"
---

# 9.6. Prevádzkové podmienky ![]({{ '/assets/icons/pre_icons/mo_process_conditions.jpg' | relative_url }})

9.6.1. Prenos tepla

  * Teplota okolia (ENVTMP)

  * Konvekčný koeficient (CNVCOF)

  * Výpočet koeficientu výhľadu

  * Zapnúť výpočet difúzneho spájania

9.6.2. Difúzia

  * Obsah atómov v prostredí (ENVATM)

  * Koeficient rýchlosti reakcie (ACVCOF)

  * Atom (ATOMID)

9.6.3. Indukcia

  * Magnetická permeabilita (ENVMPR)

  * Magnetická permitivita (ENVMPT)

  * Pomerný pomer zdrojovej energie (EHRATE)

  * Zaškrtnite políčko „Prekrývajúca sa vzdušná sieťovina“

  * Definovať okná pre indukčné ohrev

  * Použiť redukovanú 3D BEM maticu

9.6.4. Konštanty 

  * Konštanta penalizácie rozhrania (PENINF)

  * Premena mechanickej energie na tepelnú (UNTE2H)

  * Faktor časovej integrácie (TINTGF)

  * Boltzmannova konštanta (BLZMAN)

  * Faktor zníženia tepla vznikajúceho trením (UNTE2H)

  * Faktor vyhladenia tepelnej vodivosti (TCONSF)

9.6.5. Aditívna výroba

9.6.6. Zdroj tepla

Ponuka „Podmienky spracovania“ obsahuje informácie o prostredí spracovania a konštantách súvisiacich so všeobecným správaním riešenia.

## Prenos tepla [2D, 3D]

Definície podmienok procesu prenosu tepla majú vplyv na proces iba vtedy, ak je zaškrtnuté políčko „Prenos tepla“ na karte „Hlavné“ v okne „Ovládacie prvky simulácie“ a ak sú definované príslušné BCC prostredia. (Pozri obr. 9.6.1.) 

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image001.jpg' | relative_url }})

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image002.jpg' | relative_url }})

b)

Podmienky spracovania s využitím prenosu tepla; (a) pre 2D (b) pre 3D

  * **Teplota okolia (ENVTMP)**

Teplota okolia ([ENVTMP](/docs/sk/keyword_documentation/e/envtmp/)) sa používa pri výpočtoch prenosu tepla sálaním a konvekciou a predstavuje teplotu priestoru, v ktorom prebieha modelovaný proces. Teplotu okolia je možné zadať ako konštantu alebo ako funkciu času. Predpokladá sa, že k prenosu tepla na túto teplotu dochádza z akýchkoľvek uzlov, ktoré nie sú v kontakte s iným objektom. (Pokiaľ sa nepoužívajú okná na výmenu tepla).

  * **Koeficient konvekcie (CNVCOF)**

Koeficient konvekcie ([CNVCOF](/docs/sk/keyword_documentation/c/cnvcof/)) je potrebný na výpočty konvekčného prenosu tepla. Koeficient konvekcie možno zadať ako konštantu alebo ako funkciu teploty.

  * **Výpočet koeficientu výhľadu**

Žiarenie sa v simulácii vypočíta, ak zaškrtneme políčko „Vypočítať koeficient zviditeľnenia“, pričom môžeme vybrať aj objekty, pre ktoré sa má koeficient zviditeľnenia vypočítať (možnosť výberu objektov je k dispozícii len v 3D režime, ako je znázornené na obr. 9.6.2.).

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image003.jpg' | relative_url }})

Vyberte okno objektu na výpočet koeficientu zobrazenia (v 3D)

### Zapnúť výpočet difúzneho spájania

Bude sa v simulácii počítať difúzne spájanie, ak zaškrtneme políčko „Zapnúť výpočet difúzneho spájania“?

## Difúzia [2D, 3D]

Nastavenia podmienok difúzneho procesu majú vplyv na priebeh procesu iba vtedy, ak je zaškrtnuté políčko „Difúzia“ na karte „Hlavné“ v okne „Ovládacie prvky simulácie“ a ak je definovaný príslušný BCC prostredia. (Pozri obr. 9.6.3.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image004.jpg' | relative_url }})

Podmienky difúzneho spracovania

  * **Obsah atómov v prostredí (ENVATM)**

Percentuálny podiel atómov ([ENVATM](/docs/sk/keyword_documentation/e/envatm/)) dominantného atómu (zvyčajne uhlíka) v prostredí pre výpočty difúzie.

  * **Koeficient rýchlosti reakcie (ACVCOF)**

Rýchlosť povrchovej reakcie ([ACVCOF](/docs/sk/keyword_documentation/a/acvcof/)) s obsahom atómov v atmosfére pre výpočty difúzie.  
  
Od verzie DEFORM-v12 môže používateľ definovať viacero typov atómov pre difúziu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), ako je znázornené na obr. 9.6.4.

  
Poznámka: V súčasnosti je možné použiť maximálne 2 rôzne typy atómov.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image004.jpg' | relative_url }})

Nová podmienka difúzneho procesu 

  * **Atom ([ATOMID](/docs/sk/keyword_documentation/a/atomid/))**

V poli „Atóm“ môže používateľ zmeniť názov každého typu atómu a aktivovať alebo deaktivovať difúziu zaškrtnutím alebo odškrtnutím príslušného políčka.  
Keď do tabuľky difúzie pridáme dva rôzne typy atómov, môžeme vidieť, že pod položkou „Koeficient rýchlosti reakcie“ sa objaví nové pole f(teplota, atóm1, atóm2), ako je znázornené na obr. 9.6.5.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image005.jpg' | relative_url }})

Možnosti koeficientov rýchlosti reakcie

V časti „Vlastnosti materiálu“ v zozname typov „Tepelná vodivosť“ a „Tepelná kapacita“ môžeme vidieť, že bude pridané nové pole f(Teplota, Aom1, Atom2).  
Aj na stránke „Vlastnosti materiálu – Difúzia“ môžeme vidieť, že viaceré atómy definované na stránke „Ovládacie prvky simulácie – Difúzia“ sa zobrazujú v zozname atómov, takže vlastnosti každého atómu je možné definovať nezávisle, ako je znázornené na obr. 9.6.6.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image006.jpg' | relative_url }})

Stránka „Difúzia materiálových vlastností“

Aj na stránke BCC (pozri obr. 9.6.7.) môžeme pri všetkých možnostiach difúzie BCC vidieť, že sú k dispozícii oba typy atómov definované na stránke Difúzia v nastaveniach simulácie, a môžeme nastaviť BCC pre každý typ atómu samostatne.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image007.jpg' | relative_url }})

Stránka BCC – možnosť „Multiple Atom“ na stránke „Diffusion with Environment“

## Indukcia [2D, 3D]

Kartu „Indukcia“ (pozri obr. 9.6.8.) aktivujete zaškrtnutím políčka „Kúrenie“ v časti „Ovládacie prvky simulácie“ > karta „Hlavná“.

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image009.jpg' | relative_url }})

b)

Konštanty indukčného spracovania; (a) pre 2D, (b) pre 3D.

  * **Magnetická permeabilita (ENVMPR)**

Permeabilita ([ENVMPR](/docs/sk/keyword_documentation/e/envmpr/)) je vlastnosť materiálu, ktorá sa rovná hustote magnetického toku B vytvoreného v materiáli magnetizujúcim poľom, vydelená intenzitou magnetického poľa H tohto magnetizujúceho poľa.

Priepustnosť vákua (ENVMPR) sa nastavuje v ponuke „Simulation Controls > Process Conditions“. Pre orientačné účely uvádzame nižšie typickú hodnotu.

1,26 × 10⁻⁹ H/mm (SI)  
3,20 × 10⁻⁸ H/palec (anglický systém)

  * **Magnetická permitivita (ENVMPT)**

Permitivita ([ENVMPT](/docs/sk/keyword_documentation/e/envmpt/)) je veličina, ktorá opisuje, ako magnetické pole pôsobí na dielektrické prostredie a ako je ním ovplyvňované. Určuje ju schopnosť materiálu polarizovať sa v reakcii na pole a tým znížiť celkové elektrické pole vo vnútri materiálu. Permitivita sa teda týka schopnosti materiálu prenášať (alebo „povoľovať“) magnetické pole.

Dieliča elektrickej priepustnosti vákua (ENVMPT) sa nastavuje v ponuke „Simulation Controls > Process Conditions“. Pre orientačné účely uvádzame nižšie typickú hodnotu.

8,85 × 10⁻¹⁵ F/mm (SI)   
2,25 × 10⁻¹³ F/palec (anglický systém)

  * **Pomer zdrojovej energie (EHRATE)**

„Koeficient premeny energie“ ([EHRATE](/docs/sk/keyword_documentation/e/ehrate/)) je koeficient premeny elektrickej energie na teplo.  
Ak je zadaná hodnota „0“ alebo „1000“, znamená to, že 100 % elektrickej energie sa premieňa na teplo. Ak je zadaná hodnota „500“, znamená to 50 % účinnosť.

  * **Zaškrtnite políčko „Prekrývajúca sa vzdušná sieťovina“ [2D]**

  * **Definovanie okien pre indukčné ohrev [3D]**

  * **Použiť redukovanú 3D BEM maticu [3D]**

## Konštanty [2D, 3D]

Nastavenia konštánt procesných podmienok nájdete na obr. 9.6.9.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image010.jpg' | relative_url }})

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image011.jpg' | relative_url }})

b)

Pokročilé procesné konštanty; (a) pre 2D, (b) pre 3D.

  * **Konštanta penalizácie rozhrania (PENINF)**

Veľké kladné číslo, ktoré sa používa na penalizáciu rýchlosti prenikania ([PENINF](/docs/sk/keyword_documentation/p/peninf/)) uzla cez hlavnú plochu. Predvolená hodnota je pre väčšinu simulácií postačujúca. Mala by byť aspoň o dva až tri rády vyššia ako konštanta objemovej penalizácie ([PENVOL](/docs/sk/keyword_documentation/p/penvol/)).  
V prípade veľmi malých objektov (napr. spojovacích prvkov) sa odporúča znížiť tento počet o jeden alebo dva rády, aby sa zlepšila konvergencia. K zlepšeniu konvergencie to prispeje len v prípade, ak sa používa riešiteľ pre riedke matice. Túto konštantu je možné upravovať len v režime pre pokročilých používateľov.

  * **Premena mechanickej energie na tepelnú (UNTE2H)**

Konštanta slúžiaca na prepojenie jednotiek tepelnej energie (napr. BTU) s jednotkami mechanickej energie (napr. klb-in). Pre anglické a jednotky SI sa automaticky nastavia príslušné hodnoty konštanty. Túto konštantu je možné upravovať iba v režime pre pokročilých používateľov. ([UNTE2H](/docs/sk/keyword_documentation/u/unte2h/))

  * **Faktor časovej integrácie (TINTGF)**

Faktor časovej integrácie ([TINTGF](/docs/sk/keyword_documentation/t/tintgf/)) je koeficient doprednej integrácie pre integráciu teploty v čase. Jeho hodnota by sa mala pohybovať v rozmedzí od 0,0 do 1,0. Pre väčšinu simulácií je vhodná hodnota 0,75. Túto konštantu je možné upravovať iba v režime pre pokročilých používateľov.

  * **Boltzmannova konštanta (BLZMAN)**

Boltzmannova konštanta ([BLZMN](/docs/sk/keyword_documentation/b/blzman/)) je potrebná na výpočty prenosu tepla žiarením. Predvolené hodnoty pre anglické a SI jednotky sa nastavujú automaticky. Pri výpočtoch tepelného vyžarovania sa teplota uzla automaticky prepočíta na absolútnu teplotu (Rankin, Kelvin) na základe zvolených anglických alebo SI jednotiek. Túto konštantu je možné upravovať iba v režime Pokročilý používateľ.

  * **Koeficient zníženia tepla vznikajúceho trením (UNTE2H)**

  * **Faktor vyhladenia tepelnej vodivosti (TCONSF) [3D]**

## Aditívna výroba [3D]

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image012.jpg' | relative_url }})

Podmienky procesu aditívnej výroby

## Zdroj tepla [3D]

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image013.jpg' | relative_url }})

Prevádzkové podmienky zdroja tepla

Súvisiace témy:

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)   
[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)
