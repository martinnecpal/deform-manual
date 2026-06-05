---
lang: sk
title: "9.7. Pokročilé nastavenia"
---

# 9.7. Pokročilé nastavenia ![]({{ '/assets/icons/pre_icons/mo_advanced_options.jpg' | relative_url }})

9.7.1. Premenné

  * [Current Global Time/Current Local Time (TNOW)](9_7_advanced_options.htm#Current_Global_Time/Current_Local_Time_\(TNOW\))

  * Primárny obrobok (PDIE)

  * Použiť pravidlo pôvodnej adície pre kinetiku transformácie (TRANS)

9.7.2. Tolerancia chýb

  * Spôsob uvoľnenia kontaktu (CNTERR)

  * Geometrická chyba (GEOERR)

9.7.3. Premenné definované používateľom (USRDEF)

9.7.4. Kontakt

  * Trest

  * Prispôsobivá spojka

  * Rozšírený Lagrangeov funkcionál

  * Metóda viacnásobnej deformácie (MULDEF)

Plne prepojené

Voľne prepojené 

Geometria nebola aktualizovaná

  * Výpočet deformácie

  * Tepelný výpočet

9.7.5. Frekvencia

9.7.6. Kmitanie uzlov (OSCTRL)

  * Kútové kmitania

  * [Repeated touching / separating](9_7_advanced_options.htm#Repeated_touching_/_separating)

9.7.7. Kopírovanie objektu

Nastavenia pokročilých premenných pre riadenie simulácie nájdete na obr. 9.7.1.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image001.jpg' | relative_url }})

Okno pokročilých premenných

## Premenné [2D, 3D]

### **Aktuálny svetový čas/aktuálny miestny čas (TNOW)**

Tento parameter ([TNOW](/docs/sk/keyword_documentation/t/tnow/)) určuje hodnoty globálneho a lokálneho času procesu. (Pozri obr. 9.7.1.) Globálny čas predstavuje čas od začiatku riešenia úlohy a nemal by sa nikdy vynulovať. Lokálny čas je parameter, ktorý môže používateľ vynulovať. Globálny čas by sa nemal počas simulácie vynulovať, pretože postprocesor tento čas používa pre mnohé operácie postprocesingu. Pod definíciami lokálneho a globálneho času sa nachádza výberové pole, ktoré určuje, ktorý čas sa má použiť pre funkcie závislé od času, ako sú napríklad ovládacie prvky pohybu. Predvoleným nastavením je globálny čas, avšak funkcie závislé od času môžu byť nastavené aj na lokálny čas.

### **Hlavný obrobok (PDIE)**

Tento parameter ([PDIE](/docs/sk/keyword_documentation/p/pdie/)) umožňuje používateľovi určiť obrobok ako objekt, ktorý sa nesmie pohybovať ako tuhé teleso. (Pozri obr. 9.7.1.) Ak sa teleso nedeformuje, simulácia sa zastaví. Jedným z účelov tejto funkcie je zabrániť tomu, aby simulácia valcovania pokračovala za valcovanú dĺžku materiálu.

### **Použiť pravidlo pôvodnej aditívnosti pre kinetiku transformácie (TRANS)**

Vylepšili sme pravidlo pre kinetiku transformácie ([TRANS](/docs/sk/keyword_documentation/t/trans/)) z verzie 6.0. V novej verzii môže pri danom materiáli dochádzať k viacerým transformáciám súčasne a pri rovnakej teplote. Ak používateľ nechce používať toto nové pravidlo a chce používať predchádzajúce, zaškrtnutím tohto políčka to môže urobiť. (Pozri obr. 9.7.1.)

##  Tolerancie chýb [2D, 3D]

  * **Spôsob uvoľnenia pri kontakte (CNTERR) [2D]:**

V niektorých prípadoch súčasný algoritmus detekcie kontaktu neuvoľní uzly, ktoré sa počas časového kroku dotýkajú hlavnej plochy. Táto voľba [CNTERR](/docs/sk/keyword_documentation/c/cnterr/) umožňuje uvoľniť kontaktnú podmienku pre podriadený uzol, ak sa vzdiali od hlavnej hranice o predpísanú vzdialenosť. Táto hodnota sa môže použiť ako alternatíva k chybe posuvu ([SLDERR](/docs/sk/keyword_documentation/s/slderr/)). (Pozri obr. 9.7.2.)

  * **Chyba geometrie (GEOERR) [2D, 3D]**

Hodnota [GEOERR](/docs/sk/keyword_documentation/g/geoerr/) predstavuje odhad chyby medzi diskretizovanými objektmi. Predvolená hodnota je pre väčšinu bežných aplikácií postačujúca. (Pozri obr. 9.7.2.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image002.jpg' | relative_url }})

Okno „Pokročilé nastavenia tolerancie chýb“

##  Používateľom definované premenné (USRDEF) [2D, 3D]

Premenné definované používateľom ([USRDEF](/docs/sk/keyword_documentation/u/usrdef/)) sú reťazcové premenné s dĺžkou 80 znakov, ktoré sa odovzdávajú do podprogramov definovaných používateľom. Ďalšie informácie o používaní týchto premenných nájdete v kapitole [56\. User Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_user_routines_in_deform/). (Pozri obr. 9.7.3.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image003.jpg' | relative_url }})

Hodnoty definované používateľom

## Kontakt [3D]

V DEFORM-V12 bola na stránke „Pokročilé“ pridaná záložka „Kontakt“ a položka „Spôsob kontaktu“ ([CNTMTH](/docs/sk/keyword_documentation/c/cntmth/)), ktorá bola doteraz k dispozícii pre 3D objekty na stránke „Vzťahy medzi objektmi“, bola presunutá na túto stránku. Teraz máme k dispozícii 3 typy spôsobov kontaktu:

  * Trest
  * Prispôsobivá spojka
  * Rozšírený Lagrangeov funkcionál 

  * **Trest**

Metóda penalizácie (obr. 9.7.4.) je hlavným prístupom k spracovaniu kontaktu pre všetky deformovateľné objekty pri riešení kontaktu s lisovacou formou. Pre tuhé plastové modely s viacerými deformovateľnými objektmi v kontakte alebo v samokontakte je však k dispozícii aj konformné prepojenie.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image004.jpg' | relative_url }})

Trest – spôsob kontaktu

  * **Zhodná spojka**

Konformné prepojenie v podstate rieši kontakt tak, že najskôr automaticky vytvorí kontaktné prvky medzi systémami kontaktných sietí. Pri modeloch s rotačnou symetriou sa konformné prepojenie používa štandardne.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image005.jpg' | relative_url }})

Zhodná spojka – kontaktná metóda

  * **Rozšírený Lagrangeov funkcionál**

Od verzie v12 bola zavedená nová metóda rozšíreného Lagrangeovho kontaktu (ALC), ktorá umožňuje rýchlejšie výpočty pre modely zahŕňajúce viacero deformujúcich sa objektov, ako sú napríklad kombinované napätia v lisovacích formách (pružné lisovacie formy – tuhý plastický obrobok, pružné lisovacie formy – elastoplastický obrobok). Metóda ALC nie je citlivá na penalizačné číslo a funguje dobre s iteratívnym riešiteľom CG. Metóda ALC sa dá použiť s metódami Newton-Raphson aj Direct, ale modely zahŕňajúce elasto-plastické objekty vyžadujú metódu Newton-Raphson. ALC funguje lepšie s riešiteľom CG a pre veľké modely zahŕňajúce viacero deformujúcich sa objektov alebo elastické formy.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image006.jpg' | relative_url }})

Rozšírený Lagrangeov funkcionál – kontaktná metóda

  * **Metóda viacerých deformácií ([MULDEF](/docs/sk/keyword_documentation/m/muldef/))**

V starších verziách bolo na simuláciu analýzy napätia v prepojených čipoch potrebné vytvoriť súbor DEF_LCDSTS.DAT; v programe DEFORM-V12 je teraz možné tieto nastavenia definovať priamo v grafickom rozhraní, ako je znázornené na obr. 9.7.7.

  * Plne prepojené
  * Voľne prepojené 
  * Žiadna aktualizácia geometrie

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image007.jpg' | relative_url }})![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image007.jpg' | relative_url }})

Rôzne metódy deformácie

  * **Plne prepojené:** Plné prepojenie znamená, že deformácia nástroja sa premieta do deformácie obrobku v aktuálnom kroku. Vo všeobecnosti je plné prepojenie najpresnejšie, ale zároveň najnáročnejšie na výpočtový výkon. Možnosť bez aktualizácie geometrie je najmenej náročná na výpočtový výkon a ponúka najväčšie zjednodušenie procesu.

  * **Voľné prepojenie**: Ak je táto možnosť zvolená, napätia sa vypočítajú v nástroji, avšak aktualizovaná geometria formy sa v deformácii obrobku prejaví až v nasledujúcom kroku. Voľné prepojenie je numericky efektívnejšie ako úplné prepojenie, ale môže spôsobiť určité nezrovnalosti v polohe povrchu obrobku (a tým aj v objeme obrobku), ak je zmena tvaru formy podstatná.

  * **Bez aktualizácie geometrie:** Pri voľbe „Bez aktualizácie geometrie“ sa v matrici počíta iba napätie, geometria matrice sa však nikdy neaktualizuje. Ak sa používateľ zaujíma iba o napätie v nástroji, voľba „Bez aktualizácie geometrie“ je spravidla postačujúca. Ak je dôležité vychýlenie nástroja, je potrebné zvoliť voľbu „Plne prepojené“ alebo „Voľne prepojené“.

  * **Výpočet deformácie**

Používateľ môže pomocou možnosti „Užívateľsky definované“ nastaviť interval krokov pre výpočet deformácie nástroja. Predvolene je zvolená možnosť „Automatický krok“, takže výpočty deformácie sa vykonávajú pri každom kroku.

  * **Tepelný výpočet**

Používateľ môže pomocou možnosti „Užívateľsky definované“ nastaviť interval krokov pre tepelné výpočty nástroja. Predvolene je zvolená možnosť „Automatický krok“, takže tepelné výpočty sa vykonávajú pri každom kroku.

## Frekvencia [2D, 3D]

V časti „Frekvencia“ (pozri obr. 9.7.8.) môže používateľ nastaviť riadiacu hodnotu pre výpočet v rámci explicitného riešiteľa, riešenie Maxwellových rovníc, výpočet koeficientu priepustnosti a výpočet povrchu výnosu.

Aj pri simulácii ustáleného stavu metódou ALE môže používateľ definovať spôsob aktualizácie deformácie a spôsob aktualizácie teploty.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image008.jpg' | relative_url }})

3D frekvenčné okno

## Kmitanie uzlov [2D]

  
Nastavenia simulácie riadenia pokročilých uzlových kmitov ([OSCTRL](/docs/sk/keyword_documentation/o/osctrl/)) sú uvedené na obr. 9.7.9.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image009.jpg' | relative_url }})

Okno 2D uzlových kmitov

  * **Kmitanie v rohoch**

Ovládacie prvky pre osciláciu v rohu slúžia na riadenie oscilácie uzla medzi susednými úsečkami povrchu. Ak počet oscilácií prekročí limit, uzol sa na určitý počet čiastkových krokov zablokuje.

  * **Opakované spájanie a oddeľovanie**

Keď sa podriadené uzly dotknú hlavnej plochy a od nej oddelia, po dvoch osciláciách sa uzly opäť dotknú na účely vykonania čiastkového kroku. Funkciu riadenia dotyku/oddelenia možno použiť na to, aby sa uzol oddelil od plochy na účely vykonania čiastkového kroku po zadanom počte oscilácií.

## Kopírovanie objektu [3D]

Na nahradenie súboru DEF_VIEWSYM.DAT bola v rámci ovládacích prvkov simulácie vytvorená možnosť „Kópia objektu“ ([OBJCPY](/docs/sk/keyword_documentation/o/objcpy/)) (pozri obr. 9.7.10.). Používateľ si môže vybrať spôsob usporiadania objektu (posunutím alebo zrkadlením). 

**Pri preklade:** V metóde Translatinn musí používateľ určiť hodnotu vektora vzdialenosti, aby sa objekt skopíroval.

**Metódou zrkadlenia:** Pri metóde zrkadlenia musí používateľ definovať referenčný bod a hodnotu vektora.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_7_advanced_options/9_7_image010.jpg' | relative_url }})

Okno kopírovania objektu

**Súvisiace témy:**

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.6. Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)   
[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)

[9.10. Output controls](/docs/sk/pre_processor/9_simulation_controls/9_10_output_controls/)
