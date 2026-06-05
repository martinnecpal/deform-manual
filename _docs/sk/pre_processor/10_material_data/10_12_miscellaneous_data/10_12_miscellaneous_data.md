---
lang: sk
title: "10.12. Rôzne údaje"
---

# 10.12. Rôzne údaje

10.12.1. Údaje o zlomoch (FRCMOD)
10.12.2. Mechanická práca na teplo (FRAE2H)
10.12.3. Sila na jednotku objemu alebo sila telesa (FPERV)
10.12.4. Odstredivá sila
10.12.5. Difúzna väzba
10.12.6. Model veľkosti (SIZESH a SIZEMD)
10.12.7. Model hnacej sily spekania

  * Jednoduchý elastický jednokrok

  * Skorohod

  * Kohúty

  * Šinagawa

  * Ashby

  * [Raj/Ashby](10_12_miscellaneous_data.htm#Raj/Ashby)

10.12.8. Požiadavky na údaje o materiáli

  
Na obr. 10.12.1 sú znázornené pokročilé vlastnosti materiálov, ktoré sú k dispozícii pre špeciálne aplikácie.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image001.jpg' | relative_url }})

Pokročilé okno vlastností materiálu

## Údaje o zlomoch (FRCMOD)

[FRCMOD](/docs/sk/keyword_documentation/f/frcmod/) určuje model poškodenia, ktorý sa má použiť na výpočet poškodenia. Na výber je desať rôznych modelov. Cockcroft & Latham je predvolený model poškodenia, ktorý sa používa na výpočet poškodenia v programe DEFORM. Je možné napísať aj užívateľský podprogram, ktorý sa môže použiť pre model poškodenia. Modely lomu nájdete v kapitole [10.12.1. Fracture Models](/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/)

## Mechanická práca na teplo (FRAE2H)

Mechanická práca na teplo ([FRAE2H](/docs/sk/keyword_documentation/f/frae2h/)) udáva podiel mechanickej práce premenenej na teplo. Podiel premeny je zvyčajne 0,9 až 0,95. Predvolená hodnota je 0,9 a pokiaľ používateľ nemá dobrý cit pre hodnotu, táto hodnota by sa nemala meniť.

## Sila na jednotku objemu alebo sila tela (FPERV)

Na výpočet sily telesa ([FPERV](/docs/sk/keyword_documentation/f/fperv/)) (napríklad gravitácie) pre porézne, plastické a elasto-plastické materiály sa používa nasledujúca rovnica:

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_1.jpg' | relative_url }}) |
---|---
  
  
Napríklad ak je hustota ocele v jednotkách SI 7850 Kg/m^3 a gravitačné zrýchlenie je 9,8 m/Sec^2, príkon sily bogy musí byť 0,00007693 t/(mm^2. Sec^2) alebo 0,00007693 N/mm^3.

## Odstredivá sila

Odstredivá sila môže pôsobiť priamo na objekt bez riadenia otáčavého pohybu. Ak je definovaná v údajoch o materiáli, predstavuje radiálnu silu telesa, ktorá je súčinom hustoty hmotnosti a štvorca rýchlosti otáčania v radiánoch/s. Napríklad v jednotkách SI, keď sa objekt otáča rýchlosťou 7000 ot/min, čo je 733,0382 rad/s. Ak predpokladáme, že materiál je oceľ, odstredivá sila je pri použití jednotných jednotiek 4,21816 N.

## Difúzna väzba

Čas difúzneho lepenia je čas potrebný na dosiahnutie 100 % spojenia za určitých podmienok, ako je teplota a tlak. Táto možnosť je k dispozícii len v prostredí MO.  
Vzťah medzi objektmi je potrebné definovať medzi objektmi väzby ako vzťah Master-Slave. Difúzne percento väzby sa vypočíta ako stavová premenná objektu Slave. Difúzne spájanie možno aktivovať začiarknutím políčka Turn on Diffusion bonding Calculations (Zapnúť výpočet difúzneho spájania) na karte properties (Vlastnosti) v Simulation Controls (Ovládacie prvky simulácie), ako je znázornené na nasledujúcom obr. 10.12.2.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image002.jpg' | relative_url }})

Okno s vlastnosťami zobrazujúce zaškrtávacie políčko Difúzne lepenie s červenou farbou

Vlastnosti difúzneho spájania možno definovať pre objekt slave na karte Material properties Advanced (Rozšírené vlastnosti materiálu), ako je znázornené na obr. 10.12.3.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image004.jpg' | relative_url }})

Okno Advanced Material zobrazujúce difúzne lepenie s červenou farbou

Ak teplota alebo tlak nie sú konštantné, efektívne akumulované percento spojenia sa vypočíta na základe definovaných údajov. Čas spájania pre 1 % a 99 % je potrebné určiť ako funkciu teploty a tlaku, ako je znázornené na obr. 10.12.4.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image005.jpg' | relative_url }})

Difúzna väzba Okno funkcie Definícia

## Model veľkosti (SIZESH a SIZEMD)

Tento model (pozri nižšie obr. 10.12.5.) môže zaznamenávať informácie týkajúce sa fáz nad rámec jednoduchej transformácie objemového podielu. Pred implementáciou veľkostného modelu bola jedinou dostupnou informáciou o fáze v materiáli zmesi jej objemový podiel v prvku (napríklad 80 % austenitu, 20 % martenzitu). To bolo dostatočné pre materiály, ako sú ocele (kde sa vlastnosti dajú odvodiť jednoduchým použitím zákona "pravidla zmesi"), ale nepostačovalo to pre materiály, ako sú superzliatiny na báze niklu alebo hliníkové zliatiny, pre ktoré majú malé objemové podiely zrazenín veľký vplyv.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image006.jpg' | relative_url }})

Okno výberu veľkosti modelu

  
[SIZESH](/docs/sk/keyword_documentation/s/sizesh/) uchováva informácie o veľkosti 2. fázy a jej tvare. Takto môže byť 2. fáza (napríklad častice delta fázy v superzliatine na báze niklu 718) opísaná ako tvoriaca 5 % objemového podielu každého prvku materiálu (definovaného v počiatočnom objemovom podiele prvkov, [VOLFC](/docs/sk/keyword_documentation/v/volfc/)); ale môže byť opísaná aj ako pozostávajúca z častíc, ktoré majú v priemere priemer ~ 10 mikrónov. V predvolenom nastavení kľúčového slova [SIZESH](/docs/sk/keyword_documentation/s/sizesh/) sa predpokladá, že častice majú guľový tvar (pozri vyššie obr. 10.12.5.). Zadaním modelu veľkosti častíc ([SIZEMD](/docs/sk/keyword_documentation/s/sizemd/)) možno definovať viac o vlastnostiach častíc opísaných v [SIZESH](/docs/sk/keyword_documentation/s/sizesh/).  
  
K dispozícii sú rôzne modely veľkosti častíc,

  1. Sférické: častice 2. fázy sú sférické
  2. Sekundárne alfa častice - všeobecne: častice 2. fázy sú sekundárne alfa častice v Ti
  3. Sekundárna lamela Alpha - rýchlosť chladenia:
  4. Alfa na hranici zrna: častice 2. fázy sú sekundárne alfa častice v Ti na hranici zrna
  5. Častice alfa bočnej dosky: častice 2. fázy sú častice alfa bočnej dosky v Ti
  6. Gama primárny nikel: častice 2. fázy sú častice, ktoré počas rastu a rekryštalizácie vyvolávajú pripínanie na hranici zŕn (ako napríklad delta v 718).
  7. Zrážky - veľkosť a počet:
  8. Model zrna JMAK:

Tento model je možné v budúcnosti ďalej rozšíriť, ak by sme chceli modelovať kubické častice (ako napríklad gama primárne častice v práškovej metalurgii zliatin na báze niklu) alebo častice podobné doskám, ihlám alebo diskom v iných zliatinách.

## Model hnacej sily spekania

Modely hnacej sily spekania simulujú deformačné správanie vyplývajúce z procesov spekania. Modely hnacej sily spekania sú použiteľné len pre porézne objekty, s výnimkou modelu "Jednoduchá pružná jednostupňová sila".

  * **Jednoduchý elastický jednokrok**

Ako už názov napovedá, tento model (pozri obr. 10.12.6.) sa používa na simuláciu zmrštenia v dôsledku procesu spekania pomocou jedného simulačného kroku a pružného obrobku. Pre dané relatívne rozloženie hustoty a elastické vlastnosti tento model vypočíta zmrštenie pri spekaní, keď diel po spekaní dosiahne takmer plnú úroveň hustoty.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image012.jpg' | relative_url }})

Jednoduchý elastický jednostupňový model spekania

Objemová deformácia je daná,

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_2.jpg' | relative_url }}) |
---|---
  
Napätie pri spekaní je dané,

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_3.jpg' | relative_url }}) |
---|---
  
  
Používateľ musí postupovať podľa nasledujúcich krokov, aby mohol vykonať zmrštenie pri spekaní pomocou tohto modelu,

  1. Odstráňte komponenty matrice
  2. Obnovenie rýchlostného poľa
  3. Vynulovanie poľa posunutia
  4. Vynulujte napätie
  5. Zmeňte objekt na elastický
  6. Definujte elastické vlastnosti
  7. Používanie Newtonových Raphsonových iterácií
  8. Aplikujte potrebné okrajové podmienky
  9. Generovanie DB a simulácia pre 1 krok

  
Poznámka:

  1. Pre modely 3D tet mesh použite zmiešané vzorce

  2. Jednoduchý pružný model s jedným krokom možno alternatívne aktivovať umiestnením prázdneho príznakového súboru DEF_SINTER.DAT do priečinka s problémami.

**Skorohod**

Vstupné okno Skorohodovej rovnice nájdete na obr. 10.12.7.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_4.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image008.jpg' | relative_url }})

Okno Skorohod Definícia

**Kohúty**

Okno pre zadávanie Cocksovej rovnice nájdete na obr. 10.12.8.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_5.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image009.jpg' | relative_url }})

Okno Cocks Definícia

**Shinagawa**

Vstupné okno rovnice Shinagawa nájdete na obr. 10.12.9.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_6.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image010.jpg' | relative_url }})

Okno Shinagawa Definícia

**Ashby**

Vstupné okno Ashbyho rovnice pozri na obr. 10.12.10.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_7.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image011.jpg' | relative_url }})

Okno Ashby Definícia

**Raj****/Ashby**

Pre vstupné okno rovnice Raj/Ashby pozri [Fig. 10.12.11.](10_12_miscellaneous_data.htm#Fig._10.12.11._Raj/Ashby__window_Definition)

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_8.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image007.jpg' | relative_url }})

Definícia okna Raj/Ashby

## Požiadavky na údaje o materiáli

**Pokyny**

  1. Problém izotermického tvárnenia s tuhými zápustkami a tuhým viskoplastickým obrobkom.

| **Práca** | **Zomiera**
---|---|---
Údaje o materiáli |
Prúdové napätie | X |
Youngov modul |
Pomer jedov | |
Tepelná rozťažnosť |
Tepelná kapacita |
Vodivosť |
Emisivita |
  
Usmernenia k údajom o materiáli pre izotermické tvárnenie

  1. Problém neizotermického tvárnenia s tuhými zápustkami a tuhým viskoplastickým obrobkom.

| **Práca** | **Zomiera**
---|---|---
Údaje o materiáli |
Prúdové napätie | X |
Youngov modul |
Pomer jedov | |
Tepelná rozťažnosť |
Tepelná kapacita | X | X
Vodivosť | X | X
Emisivita | X | X
  
Usmernenia k údajom o materiáli pre neizotermické tvárnenie

  1. Analýza prenosu tepla.

| **Práca** | **Zomiera**
---|---|---
Údaje o materiáli |
Stres pri prúdení |
Youngov modul |
Pomer jedov | |
Tepelná rozťažnosť |
Tepelná kapacita | X | X
Vodivosť | X | X
Emisivita | X | X
  
Usmernenia k údajom o materiáloch pre prenos tepla

  1. Spojená analýza neizotermická s tepelnou rozťažnosťou Pružné lisovacie formy a pružno-plastický obrobok.

| **Práca** | **Zomiera**
---|---|---
Údaje o materiáli |
Prúdové napätie | X |
Youngov modul | X | X
Pomer jedov | X | X
Tepelná rozťažnosť | X | X
Tepelná kapacita | X | X
Vodivosť | X | X
Emisivita | X | X
  
Usmernenia k údajom o materiáli pre neizotermickú analýzu s tepelnou rozťažnosťou

  1. Oddelená analýza napätia v zápustke izotermická.

| **Práca** | **Zomiera**
---|---|---
Údaje o materiáli |
Prúdové napätie | X |
Youngov modul | | X
Pomer jedov | | X
Tepelná rozťažnosť |
Tepelná kapacita |
Vodivosť |
Emisivita |
  
Usmernenia k údajom o materiáloch pre izotermickú analýzu napätia v zápustke

  1. Oddelená analýza napätia v zápustke, ktorá nie je izotermická.

| **Práca** | **Zomiera**
---|---|---
Údaje o materiáli |
Prúdové napätie | X |
Youngov modul | | X
Pomer jedov | | X
Tepelná rozťažnosť | | X
Tepelná kapacita | X | X
Vodivosť | X | X
Emisivita | X | X
  
Usmernenia k údajom o materiáli pre neizotermickú analýzu napätia v zápustke

Súvisiace témy:

[10.12.1. Fracture Models](/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/)

[Assigning Material to Object](../../../operation_templates/33_forming/33_1_2d_forming_setup.htm#Material)
[1.11. DEFORM Units](/docs/sk/about_deform/1_introduction_to_deform/1_9_units/)
[Material Editing](/docs/sk/labs/heat_treatment_labs/2d_ht_lab5_material_input/)
[Material Units Converter](../10_material_data.htm#Material_Data)
[Units Converter Next Gen Post](../../../post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options.htm#26_5_6_Unit_Conversion)
[Appendix IV: Determining 'R' coefficients for anisotropy models](/docs/sk/appendices/appendix_iv_determining_r_coefficientss/)
[Running an inertia weld simulation in DEFORM](/docs/sk/applications/55_applications/55_inertia_welding/2d_inertia_welding/)
[Running 2D creep simulations in DEFORM](/docs/sk/applications/55_applications/55_creep/2d_creep/)
[Appendix X: Meshing an object with multiple material groups](/docs/sk/appendices/appendix_x_meshing_an_object_with_multiple_material_group/)
[Setting up 2D induction heating in DEFORM](/docs/sk/applications/55_applications/55_4_induction_heating/setting_up_induction_heating_in_deform/)
[Fracture with Element Deletion and Damage Softening](/docs/sk/applications/55_applications/55_fracture/3d_fracture/)
[Setting up 2D fracture with element deletion with DEFORM](/docs/sk/applications/55_applications/55_fracture/2d_fracture/)
[A Theoretical Background to Resistance Heating Concepts](/docs/sk/applications/55_applications/55_resistance_heating_labs/a_theoretical_background_to_resistance_heating/)
[Setting up 3D machining models](/docs/sk/operation_templates/39_cutting/setting_up_3d_machining_models/)
