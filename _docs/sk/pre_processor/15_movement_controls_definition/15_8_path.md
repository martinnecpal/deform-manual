---
lang: sk
title: "15.8. Cesta"
---

# 15.8. Cesta

15.8.1. Miestne a globálne súradnice

15.8.2. Zarovnanie stredu rotácie na stred objektu

15.8.3. Synchronizácia s definovanými údajmi o ceste

**[2D, 3D]** : Pohyb po dráhe možno definovať jedným z dvoch spôsobov, ako funkciu času alebo ako profil + rýchlosť podávania.

Ak je poloha funkciou času, pohyb sa lineárne interpoluje medzi jednotlivými definovanými polohami.

Ak je poloha funkciou rýchlosti posuvu, každá zadaná rýchlosť posuvu [FeedRate(i)] definuje, ako rýchlo sa objekt presunie z príslušnej polohy [Position(i)] do nasledujúcej polohy [Position(i+1)]. Rýchlosť posuvu posledného páru údajov sa automaticky nastaví na nulu, pretože nemá praktický význam.

Programy G-Code zvyčajne definujú dráhy pomocou polohy ako funkcie rýchlosti posuvu. Je potrebné poznamenať, že vzťah medzi rýchlosťou posuvu a polohou je mierne odlišný od vzťahu používaného v programe DEFORM. V G-Code každá zadaná rýchlosť posuvu [FeedRate(i)] definuje, ako rýchlo sa objekt posunie do príslušnej polohy [Position(i)] z predchádzajúcej polohy [Position(i-1)].

Rozdiel vo formátoch posuvu sa musí zohľadniť pri importovaní dráh G-kódu na použitie ako dráhy DEFORM. Konverziu možno vykonať posunutím rýchlosti posuvu o jednu pozíciu dopredu v tabuľke dráh. Inými slovami, každá rýchlosť posuvu (i) sa musí posunúť na predchádzajúcu dvojicu údajov o pozícii (i-1).

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image001.jpg' | relative_url }})

Pohyb po ceste a po ceste so zarovnaním

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image002.jpg' | relative_url }})

Smerovosť vektorov osi a rýchlosti vzhľadom na referenčný bod na objekte

V prvom kroku definovania údajov o pohybe cesty používateľ vstúpi do dialógového okna kontroly pohybu cesty. (Pozri obr. 15.8.3. a obr. 15.8.4.)

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image003.jpg' | relative_url }})

2D používateľské rozhranie na zadanie definície pohybu cesty

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image004.jpg' | relative_url }})

3D používateľské rozhranie na zadanie definície pohybu cesty

**[2D]** : 2D Pohyb po ceste môže byť definovaný pomocou pozícií X a Y bez ohľadu na typ použitej funkcie.

## Lokálne a globálne súradnice [3D]

V**Globálne súradnice** sa používajú, keď sa má objekt pohybovať v smeroch X, Y a Z definovaním hodnôt polohy pozdĺž týchto troch smerov ako funkcie času alebo funkcie rýchlosti posuvu.

Ak je translačný pohyb rotujúceho valca obmedzený na rovinu, jeho pohyb možno v tejto rovine opísať v **lokálnom súradnicovom** systéme. Ak možno lokálnu rovinu definovať pomocou dvoch vektorov (U,V), pohyb v jej lokálnej rovine možno ľahko definovať. Nasledujúci obrázok (Pozri obr. 15.8.5.) to znázorňuje v aplikácii prietokového tvárnenia, kde sa valce pohybujú radiálne a axiálne len v rovine prechádzajúcej stredom valca a osou obrobku.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image005.jpg' | relative_url }})

Základné pojmy miestnej roviny s ilustráciou

Je potrebné definovať údaje pre miestnu rovinu, ktorej pojmy sú znázornené na obr. 15.8.6.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image006.jpg' | relative_url }})

Údaje potrebné na definovanie miestnej roviny

Ako je znázornené na obr. 15.8.7., tieto funkčné údaje môžu predstavovať komplexný pohyb, ktorý v jednoduchej forme môže byť časovým a polohovým údajom na lokálnej rovine s konkrétnou orientáciou v priestore.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image007.jpg' | relative_url }})

Tabuľka funkčných údajov v miestnej rovine

## Zarovnanie stredu rotácie na stred objektu [2D, 3D]

Pri zarovnávaní je potrebné zarovnať stred otáčania objektu (štvorcová značka na obr. 15.8.8.) a stred geometrie (kruhová značka na obr. 15.8.8.), aby pohyb z času na čas sledoval dráhu so správnou orientáciou. Používateľ môže určiť stred objektu ako referenčný bod. (zobrazený ako stred osi na karte Rotácia v grafickom rozhraní pohybu, pozri obr. 15.8.12. a obr. 15.8.13.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image008.jpg' | relative_url }})

Základy zarovnania a otáčania vzhľadom na geometrický stred

## Synchronizácia s definovanými údajmi o ceste [2D, 3D]

Po zadaní referenčného bodu používateľom priraďte pohyb synchronizáciou s definovanými údajmi funkcie. Keďže "synchronizácia" znamená aktualizáciu údajov o objekte na základe údajov o pohybe v závislosti od času v doménach "čas" a "priestor". Na synchronizáciu sa ako referenčný čas používa aktuálny čas simulácie. Po vykonaní tejto synchronizácie sa poloha objektu môže zmeniť (pomocou systémovej správy, ako je uvedené na obr. 15.8.9.) na základe aktuálneho času procesu (pozri obr. 15.8.10.) a typu údajov funkcie (pozri obr. 15.8.11.) definovaných pre tento pohyb po ceste. Prejdite tiež Obr. 15.8.14. pre pohyb cesty zobrazený na lokálnej rovine.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image009.jpg' | relative_url }})

Systémové správy pri pokuse o synchronizáciu s referenčným bodom

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image010.jpg' | relative_url }})

Aktuálny čas

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image011.jpg' | relative_url }})

Typ pozemku

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image012.jpg' | relative_url }})

Vyhľadanie geometrického stredu

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image013.jpg' | relative_url }})

Možnosti zarovnania otáčania a stredu geometrie po výpočte

![]({{ '/assets/images/pre-processor/15_movement_controls/15_8_path/15_8_image005.jpg' | relative_url }})

Koncepty polohovania pri definovaní údajov o funkcii cesty

**Súvisiace témy:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)
