---
lang: sk
title: "35. Úvod do procesov prenosu tepla"
---

# 35\. Úvod do procesov prenosu tepla

Funkcia „Prenos tepla“ pomôže používateľovi simulovať rôzne operácie ohrevu/chladenia v procese tvárnenia, ktoré zahŕňajú zmenu teploty a deformáciu. Tieto operácie sú prispôsobené tak, aby sa počas tvárnenia nastavoval iba proces prenosu tepla, ako je ohrev obrobku, presun obrobku z pece do lisu, odpočinok obrobku na matrici (pred tvárnením) a výdrž po tvárnení. Vhodný výber typu prenosu tepla (ohrev, prenos, odpočinok alebo zotrvanie) pridá príslušné okná nastavení a navedie používateľa k rýchlemu nastaveniu operácií prenosu tepla počas operácií horúceho/teplého kovania.

V 2D aj 3D sú k dispozícii štyri typy operácií prenosu tepla,

  1. Zahrievanie v peci

  2. Preprava leteckou dopravou

  3. Položte na formu a

  4. Zostať na hrane

**Ohrev v peci:** Pri prevádzke v režime kúrenia alebo ohrevu sa modeluje ohrev sochory v peci. Budú pridané predvolené nastavenia procesu vhodné pre prevádzku ohrevu (pozri [Table. 35.1.](35_introduction_to_heat_transfer_operations.htm#Table_35_1_Default_process_settings_\(heat_condition\)_and_object_temperatures_for_different_heating_types)), pri definovaní konkrétnej operácie je možné vykonať zmeny predvolených nastavení.

**Prenos vzduchom:** Pri operácii „Prenos vzduchom“ sa modeluje prenos tepla alebo tepelné straty do okolia počas presunu obrobku/polotovaru do formy. V predvolenom nastavení sa do stromu projektu pre túto operáciu pridá jeden objekt – obrobok. Predvolené nastavenia procesu pre prevod cez vzduch sú uvedené v [Table. 35.1.](35_introduction_to_heat_transfer_operations.htm#Table_35_1_Default_process_settings_\(heat_condition\)_and_object_temperatures_for_different_heating_types)

**Odpočinok na forme:** Pri operácii „Odpočinok na forme“ sa modeluje prenos tepla alebo únik tepla do okolia a do formy zo sústruženého dielu/polotovaru počas odpočinku na forme predtým, ako horná forma príde do kontaktu so sústruženým dielom/polotovarom. Predvolene sa do stromu projektu pridajú objekty sústruženého dielu, hornej a spodnej formy. Predvolené nastavenia procesu pre operáciu „Odpočinok na matrici“ sú uvedené v [Table. 35.1.](35_introduction_to_heat_transfer_operations.htm#Table_35_1_Default_process_settings_\(heat_condition\)_and_object_temperatures_for_different_heating_types)

**Dwell on die:** V tejto operácii sa modeluje prenos tepla alebo únik tepla do okolia a do formy z obrobku/polotovaru po deformácii (po tom, čo sa formy stiahnu z obrobku). Štandardne sa do stromu projektu pridajú objekty obrobku, hornej a spodnej formy. Predvolené nastavenia procesu pre operáciu „Dwell on Die“ sú uvedené v [Table. 35.1.](35_introduction_to_heat_transfer_operations.htm#Table_35_1_Default_process_settings_\(heat_condition\)_and_object_temperatures_for_different_heating_types)

**Typ ohrevu** |  **Teplota obrobku** **(°C alebo °F)** |  **Teplota foriem** **(°C alebo °F)** |  **Doba spracovania** **(s)** |  **Teplota okolia** **(°C alebo °F)** |  **Konvekčný koeficient** **(N/s/mm/°C alebo Btu/s/in²/°F)**  
---|---|---|---|---|---  
Teplo v peci |  1232 °C alebo 2250 °F |  neuvádza sa |  3600 |  1200 °C alebo 2250 °F |  0,02 N/s/mm/°C alebo 7,7e-6 Btu/s/in²/°F  
Prenos vzduchom |  1232 °C alebo 2250 °F | NA |  15 |  20 °C alebo 68 °F |  0,02 N/s/mm/°C alebo 7,7e-6 Btu/s/in²/°F  
Odpočinok |  1232 °C alebo 2250 °F |  20 °C alebo 68 °F |  4 |  20 °C alebo 68 °F |  0,02 N/s/mm/°C alebo  
7,7e-6 Btu/s/in²/F  
Bývanie |  1232 °C alebo 2250 °F |  20 °C alebo 68 °F |  4 |  20 °C alebo 68 °F |  0,02 N/s/mm/°C alebo 7,7e-6 Btu/s/in²/°F  
  
Predvolené nastavenia procesu (tepelné podmienky) a teploty objektov pre rôzne typy ohrevu

Ďalšie informácie o nastavení všetkých štyroch procesov prenosu tepla nájdete v dokumentoch [35.1. 2D Heat Transfer Operation]() a [35.2. 3D Heat Transfer Operation]().
