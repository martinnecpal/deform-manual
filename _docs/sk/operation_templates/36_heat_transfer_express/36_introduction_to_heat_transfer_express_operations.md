---
lang: sk
title: "36. Úvod do operácií programu Heat Transfer Express"
---

# 36\. Úvod do funkcií programu Heat Transfer Express

Prenos tepla je pohyb energie spôsobený teplotným rozdielom. Kedykoľvek existuje teplotný rozdiel v prostredí alebo medzi prostrediami, musí dochádzať k prenosu tepla. Mechanizmy prenosu tepla možno rozdeliť do 3 širokých kategórií:

**Vedenie**: Prenos tepla cez pevný materiál prostredníctvom kontaktu medzi jednotlivými molekulami. Teplo prúdi z oblasti s vyššou teplotou do oblasti s nižšou teplotou. 

  
**Konvekcia**: Proces prenosu tepla, pri ktorom dochádza k pohybu tekutiny (napríklad vzduchu) v dôsledku rozdielu v hustote tekutiny a pôsobenia gravitácie.

  
**Žiarenie**: Prenos tepla vo forme elektromagnetických vĺn z jedného samostatného povrchu na druhý. Vyžiarená energia sa buď prenáša, absorbuje, odráža, alebo ide o kombináciu všetkých troch javov.

  
V režime „Viacnásobné operácie – Prenos tepla – Expresné operácie“ sa bude simulovať iba prenos tepla prostredníctvom vedenia a konvekcie.

  
Operácie programu Heat Transfer Express sú prispôsobené tak, aby nastavovali výlučne procesy prenosu tepla počas kovania, ako je ohrev obrobku, presun obrobku z pece do lisu, odpočinok obrobku na matrici (pred tvarovaním) a zotrvanie obrobku na matrici po tvarovaní. Pomocou týchto operácií môže používateľ nastaviť viacero operácií tak, aby v jednom kroku napodobil skutočný proces horúceho alebo teplého kovania. Vhodný výber typu prenosu tepla (ohrev, prenos, odpočinok alebo zotrvanie) pridá príslušné okná nastavení a navedie používateľa k rýchlemu nastaveniu operácií prenosu tepla počas operácií horúceho/teplého kovania výlučne v režime s návodom.

V režime Heat Transfer Express sú v 2D aj 3D k dispozícii štyri typy ohrevu alebo operácií prenosu tepla, a to (pozri [Fig. 36.1]().),

  1. Kúrenie

  2. Prevod

  3. Položte na formu a

  4. Zostať na hrane

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/image001.jpg' | relative_url }})

Okno nastavení 2D a 3D procesov

  
**Kúrenie**: Pri prevádzke v režime kúrenia alebo v tepelnej peci sa modeluje ohrev sochory v peci. Pre túto operáciu je povolený len jeden objekt, ktorý sa pridá automaticky. Pridajú sa predvolené nastavenia procesu vhodné pre operáciu ohrevu (pozri tabuľku 36.1.), pričom pri definovaní konkrétnej operácie je možné vykonať zmeny v predvolených nastaveniach.

**Prenos tepla**: Pri operácii prenosu tepla sa modeluje prenos tepla alebo únik tepla do okolia pred umiestnením obrobku/polotovaru na lisovú formu. V predvolenom nastavení sa do stromu projektu pre túto operáciu pridá jeden objekt – obrobok. Predvolené nastavenia procesu pre prenos tepla sú uvedené v tabuľke 36.1.

**Odpočinok na matrici**: Pri operácii tepelného odpočinku sa modeluje tepelné odpočinutie na matrici pred deformáciou. Štandardne sa do stromu projektu pridajú objekty obrobku, hornej a spodnej matrice. Štandardné nastavenia procesu pre operáciu tepelného odpočinku sú uvedené v tabuľke 36.1.

**Doba odpočívania v matrici**: Pri operácii s tepelným odpočinom sa v tejto operácii modeluje prenos tepla po deformácii (po tom, čo sa matrice stiahnu z obrobku). Do stromu projektu sa štandardne pridajú objekty obrobku, hornej a spodnej matrice. Štandardné nastavenia procesu pre operáciu s tepelným odpočinom sú uvedené v tabuľke 36.1.

**Typ ohrevu** |  **Teplota obrobku** **(°C alebo °F)** |  **Teplota foriem** **(°C alebo °F)** |  **Doba spracovania** **(s)** |  **Teplota okolia** **(°C alebo °F)** |  **Konvekčný koeficient** **(N/s/mm/°C alebo Btu/s/in²/°F)**  
---|---|---|---|---|---  
Kúrenie |  1200 °C alebo 2250 °F |  neuvádza sa |  3600 |  1200 °C alebo 2250 °F |  0,0226611 N/s/mm/°C alebo 7,7e-6 Btu/s/palec²/°F  
Prenos |  1200 °C alebo 2250 °F | N/A |  15 |  20 °C alebo 68 °F |  0,0226611 N/s/mm/°C alebo 7,7e-6 Btu/s/in²/°F  
V kľude |  1200 °C alebo 2250 °F |  150 °C alebo 300 °F |  4 |  20 °C alebo 68 °F |  0,0226611 N/s/mm/°C alebo 7,7e-6 Btu/s/in²/°F  
Bývanie |  1200 °C alebo 2250 °F |  150 °C alebo 300 °F |  4 |  20 °C alebo 68 °F |  0,0226611 N/s/mm/°C alebo 7,7e-6 Btu/s/in²/°F  
  
Predvolené nastavenia procesu (tepelné podmienky) a teploty objektov pre rôzne typy ohrevu

Predvolené nastavenia procesu (tepelné podmienky) a teploty objektov pre rôzne typy ohrevu

  
Ďalšie informácie o nastavení všetkých štyroch procesov prenosu tepla nájdete v dokumentácii k modelom [2D Heat Transfer Express Operation](/docs/en/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/) a [3D Heat Transfer Express Operation](/docs/en/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/).

**Súvisiace témy:**

[36.1. 2D Heat Transfer Express Operation](/docs/en/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/)

[36.2. 3D Heat Transfer Express Operation](/docs/en/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/)
