---
lang: sk
title: "40.2. Deformácia pri 3D obrábaní"
---

# 40.2. Deformácie pri 3D obrábaní

40.2.1. Ako pridať operáciu „3D deformácia pri obrábaní“

40.2.2. Okno objektu

40.2.3. Obrobok

  * Všeobecné informácie

  * Okrajové podmienky

  * Inicializovať

  * Vytvorené v programe Flownet

40.2.4. Zápasy

  * Všeobecné informácie

  * Geometria

40.2.5. Prejsť

  * Všeobecné informácie

  * Geometria

40.2.6. Polohovanie

40.2.7. Plánované umiestnenie

40.2.8. Kontakt

40.2.9. Náhľad simulácie

40.2.10. Ovládacie prvky simulácie

40.2.11. Vytvorenie databázy

## Ako pridať operáciu „3D deformácia pri obrábaní“

Operáciu „3D Machining Distortion“ je možné nastaviť v prostredí Integrated Manufacturing Process, ku ktorému sa dostanete z hlavného okna grafického používateľského rozhrania (GUI). Operáciu „3D Machining Distortion“ je možné pridať v sprievodcovi MO na karte „Explorer“ kliknutím na tlačidlo vedľa položky „3D Machining Distortion“. Používateľ ju môže tiež pridať pomocou funkcie drag and drop do editora operácií, ako je znázornené na obrázku [Fig. 40.2.1.](40_1_2d_machining_distortion.htm#Fig_40_1_1_Adding_2D_Machining_Distortion_Operation_to_operation_editor).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image001.jpg' | relative_url }})

Pridanie operácie „3D deformácia pri obrábaní“ do editora operácií

## Okno objektu

Okrem obrobku môže používateľ pridať do simulácie požadovaný počet upínacích prípravkov a prechodov tak, že na stránke „Objekty“ zadá „Počet upínacích prípravkov“ a „Počet prechodov“. Obr. 40.2.2. znázorňuje štyri upínacie prípravky a jeden priechod pridané pre jednoduchú operáciu 3D deformácie pri obrábaní. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), aby ste vybrané objekty pridali do operácie 3D deformácie pri obrábaní. (Pozri obr. 40.2.2.)

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image002.jpg' | relative_url }})

Okno objektu

## Obrobok

### Všeobecné informácie

V tomto okne môže používateľ zmeniť názov obrobku. V prípade obrobku v module „Machining Distortion“ musí používateľ importovať objekt z iných databáz alebo zo súborov kľúčov pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}), preto nemá žiadnu inú možnosť na definovanie obrobku (pozri obr. 40.2.3.). Ak chce používateľ inicializovať posun obrobku, môže zaškrtnúť políčko Init displacement. 

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image003.jpg' | relative_url }})

Okno obrobku

### Okrajové podmienky

V okne „Okrajové podmienky“ môže používateľ priradiť objektu okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s ostatnými objektmi a s prostredím. Obr. 40.2.4. znázorňuje okrajové podmienky, ktoré je možné priradiť k obrobku v rámci deformácie pri obrábaní. Najbežnejšími okrajovými podmienkami požadovanými pre deformáciu pri obrábaní sú stanovenie rýchlosti na zastavenie posunu obrobku počas obrábania alebo pôsobenie tlaku na pridržanie obrobku.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image003.jpg' | relative_url }})

Okno s okrajovými podmienkami

### Inicializácia

V okne „Initialize“ sú na inicializáciu k dispozícii niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posunutie atď.

Používateľ môže inicializovať hodnoty týchto stavových premenných kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 40.2.5. znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne „Initialize“. Ďalšie informácie týkajúce sa možnosti inicializácie nájdete v časti [17\. Object Data Initialize](/docs/en/pre_processor/17_object_data_initialization/17_object_data_initialize/). 

V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien „Node“ a „Element“. Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“, nájdete v dokumentácii [17.1 Node node Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [17.2. Element Data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image004.jpg' | relative_url }})

Inicializovať okno

### Vstavaná sieť Flownet

Pomocou možnosti „Vstavaný Flownet“ môže používateľ vygenerovať sieť Flownet pre daný objekt. Ak používateľ použije možnosť „Vstavaný Flownet“, sieť Flownet sa vykresľuje priebežne počas simulácie úlohy. Ďalšie informácie týkajúce sa možnosti „Vstavaný Flownet“ nájdete v [13.2.9. Built in Flownet.](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13_2_9_Built_In_Flownet).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image005.jpg' | relative_url }})

Vytvorené v Flownet

## Rozpis zápasov

### Všeobecné informácie

Sú definované upínacie prípravky, ktoré držia obrobok. Upínacie prípravky sa v tejto operácii považujú za tuhé objekty. V tomto okne môže používateľ zmeniť názov upínacieho prípravku (pozri obr. 40.2.7.).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image006.jpg' | relative_url }})

Okno s rozpisom zápasov

### Geometria

Používateľ môže definovať novú geometriu pomocou možností v okne geometrie. Okno geometrie ponúka základné možnosti na definovanie geometrie (pozri obr. 40.2.8.). Geometriu je možné importovať aj pomocou možnosti Importovať geometriu zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Importovať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Používateľ môže tiež importovať geometrie v iných formátoch, ako sú .key, .DB, .STL, .PDA, .NAS a .UNV. Na jednoduché definovanie základných geometrických tvarov sú k dispozícii primitívy. Ďalšie informácie o vytváraní a úprave 3D geometrií nájdete v [12.3. 3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image006.jpg' | relative_url }})

Okno Geometria

## Prejsť

### Všeobecné informácie

Z hľadiska modelu sú informácie o obrábacom priechode tiež geometrickými údajmi, ktoré pri prekrývaní so surovcom určujú polohu a rozsah materiálu určeného na odstránenie. Ide teda tiež o geometrické údaje, ktoré je možné definovať alebo načítať. V tomto okne môže používateľ zmeniť názov obrobku (pozri obr. 40.2.9.).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image008.jpg' | relative_url }})

Okno na prechod

### Geometria

Používateľ môže definovať novú geometriu pomocou možností v okne geometrie. Okno geometrie ponúka základné možnosti na definovanie geometrie (pozri obr. 40.2.10.). Geometriu je možné importovať aj pomocou možnosti „Importovať geometriu zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo pomocou možnosti „Importovať z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})). Používateľ môže tiež importovať geometrie v iných formátoch, ako sú .key, .DB, .STL, .PDA, .NAS a .UNV. Na jednoduché definovanie základných geometrických tvarov sú k dispozícii primitívy. Ďalšie informácie o vytváraní a úprave 3D geometrií nájdete v [12.3. 3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image006.jpg' | relative_url }})

Okno Geometria

## Polohovanie

Na obr. 40.2.11. je zobrazené okno na nastavenie polohy.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image007.jpg' | relative_url }})

Okno na nastavenie polohy

**Automatické polohovanie**![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}): Funkciu automatického polohovania používa používateľ na umiestnenie tuhých objektov voči obrobku. Táto možnosť sa osvedčuje pri troch objektoch v operácii tvarovania, avšak po použití automatického polohovania v režime „Machining Distortion“ musí používateľ skontrolovať polohu objektov.

**Umiestňovanie objektov** ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}): Kliknutím na toto tlačidlo môže používateľ umiestniť objekty do požadovaných smerov. K dispozícii sú rôzne typy možností umiestňovania, ako napríklad [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Drop](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_5_Drop_positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning) a [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning), ako je znázornené na obr. 40.2.12. Ďalšie informácie o týchto možnostiach nájdete v časti [19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image008.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Ak si používateľ nie je istý polohou objektu – napríklad v prípade objektov typu „Načítanie z databázy“ a ak je v dávkovom režime pridaná operácia „Obrábacia deformácia“ –, naplánované polohovanie pomôže objekty presne umiestniť.

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastaveniach MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby boli objekty umiestnené ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime (pozri obr. 40.2.13.)

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image009.jpg' | relative_url }})

Plánované časové okno na umiestnenie

## Kontakt 

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty – upínacie prostriedky a obrobok – v simulácii vzájomne interagujú. Tabuľka vzťahov zobrazuje aktuálne vzťahy medzi objektmi, ktoré boli definované tak, ako je znázornené na obr. 40.2.14. Všetky objekty, ktoré môžu prísť do kontaktu v priebehu simulácie, musia mať definovaný kontaktný vzťah. Správne definovanie týchto vzťahov je veľmi dôležité, aby simulácia mohla presne modelovať proces deformácie pri obrábaní. Používateľ by mal mať na pamäti, že medzi objektom priechodu a obrobkom nie je potrebný žiadny vzťah medzi objektmi.

**Systém**: Po výbere tohto prepínača systém priradí predvolené vzťahy medzi objektmi. V prípade potreby môže používateľ pridať mazivá výberom možnosti „Pridať nové“ z roletového menu a kliknutím na tlačidlo „Upraviť“, alebo môže na účely simulácie načítať požadované mazivá z knižnice.

**Používateľ**: Pri operácii „Deformácia pri obrábaní“ je štandardne zaškrtnuté políčko „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), ako je znázornené na obr. 40.2.14.

Ďalšie informácie nájdete v dokumente [20\. Inter-Object Relations](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image010.jpg' | relative_url }})

Kontaktný formulár

## Náhľad simulácie

Náhľad simulácie poskytuje prehľad o operácii, ktorá sa má vykonať, na základe definície procesu a priechodu. V okne Náhľad simulácie sa po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) spustí animácia, ktorá zobrazí náhľad objektu po odstránení materiálu v dôsledku priechodu. (Pozri obr. 40.2.15.)

V 3D máme dva typy booleovských metód:

**Na základe geometrie (nová metóda)**: __Pri voľbe „Na základe geometrie“ sa najskôr vykoná boolovská operácia a následne lokálne prečlenenie siete podľa zadaných vstupných údajov. Výsledkom bude hladká sieť, ako je znázornené na obr. 40.2.16.)

**Na základe pevnej siete (starý spôsob)**: Pri voľbe „Pevná sieť“ sa vykoná boolovská operácia a následne sa vygeneruje iba pevná sieť, ako je znázornené na obr. 40.2.15.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image011.jpg' | relative_url }})

Náhľad simulácie: Metóda založená na pevnej sieti

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image012.jpg' | relative_url }})

Náhľad simulácie: Metóda založená na geometrii 

## Riadenie simulácie

**Počet simulačných krokov**: Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú vykonať vo fázach „Pass“ a „Unloading“ počnúc počiatočným číslom kroku. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí príkaz na zastavenie simulácie alebo ak simulácia nenarazí na problém. Simulácia deformácie pri obrábaní prebieha v 3 fázach,

Fáza 1 – Načítanie, načíta prevádzkové údaje a

Fáza 2 – Prechod, simuluje obrábací prechod

3. etapa – Vykládka, demontáž upínacích prvkov a simulácia spätného pruženia.

**Počet krokov na uloženie**: Počet krokov na uloženie ([STPINC](/docs/en/keyword_documentation/s/stpinc/)) do databázy určuje, koľko krokov systém uloží do databázy. Každý krok sa musí uložiť na účely simulácie deformácie pri obrábaní.

**Riadenie veľkosti kroku**: Veľkosť kroku riešenia sa riadi časovým krokom. Maximálny čas trvania procesu na jeden krok možno pri operáciách s deformáciou pri obrábaní nastaviť na 1 sekundu. 

Na obr. 40.2.17 sú zobrazené ovládacie prvky simulácie v režime s navádzaním.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image013.jpg' | relative_url }})

Riadenie simulácie v režime s navádzaním

Ďalšie informácie a popis možností v časti „Ovládacie prvky simulácie“ nájdete v dokumente [9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/).

## Vytvoriť databázu

Na stránke „Generate DB“ môžeme vidieť súhrn nastavení simulácie operácie. (Pozri obr. 40.2.18.)

**Vytvoriť databázu** ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}): Kliknutím na toto tlačidlo sa vygeneruje databáza potrebná na inštaláciu.

**Pridať súbor .key**: Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale stále sa vzťahujú na daný proces, je možné načítať ako súbor .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore .key, následne stačí zmeniť len tento súbor a simuláciu je možné odoslať znovu.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/image014.jpg' | relative_url }})

Okno na generovanie databázy
