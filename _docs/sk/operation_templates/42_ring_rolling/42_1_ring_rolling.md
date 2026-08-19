---
lang: sk
title: "42.1. Valcovanie prstencov"
---

# 42.1. Operácia valcovania prstencov

42.1.1. Ako pridať operáciu valcovania prsteňov

42.1.2. Výber procesu

42.1.3. Nastavenie simulácie

42.1.4. Zoznam materiálov

42.1.5. Stránka objektu

  * Objekty pre nastavenie typu modelu „Symetria“

42.1.6. Definovanie obrobku – prstencový objekt

  * Vytvoriť priečny rez z importovanej 3D geometrie

  * Vytvoriť priečny rez z importovanej 3D siete

42.1.7. Definovanie 2D priečneho rezu

42.1.8. Vytvorenie 2D siete

42.1.9. Vytváranie 3D geometrie

  * Nastavenia Revolve

  * Import 3D geometrie

42.1.10. Vytvorenie 3D siete

42.1.11. Orientácia

42.1.12. Stránka s materiálmi

42.1.13. Kryštálová mriežka obrobku

41.1.14. Majetok

42.1.15. Inicializácia

42.1.16. Definícia hnacieho valca

  * Určenie orientácie hnacieho valca

  * Definícia pohybu hnacieho valca

42.1.17. Definícia tlakového valca

  * Orientácia tlakového valca

  * Definovanie pohybu tlakového valca

42.1.18. Definícia axiálneho naklonenia

  * Orientácia axiálneho valca

  * Stránka o axiálnom pohybe valca

42.1.19. Strana č. 2 – Axial Roll

42.1.20. Polohovanie

42.1.21. Plánované umiestnenie

42.1.22. Kontakt

42.1.23. Ovládacie prvky zastavenia pre simuláciu valcovania prstencov

42.1.24. Ovládacie prvky pre kroky a prepočítavanie siete pri valcovaní prstencov

42.1.25. Ovládacie prvky simulácie

  * Kontrola stability

  * Pokročilé ovládanie

42.1.26. Vytvorenie databázy

42.1.27. Nastavenie prevádzky valcovania prstencov v dávkovom režime

  * Obrobok – prstenec sa načíta z databázy

  * Vybrať priečny rez pre objekt „Read from DB“

  * Vytvorenie 2D siete priečneho rezu obrobku

  * Vytvorenie 3D siete obrobku

42.1.28. Spustenie simulácie

##  Ako pridať operáciu valcovania prsteňov

Operáciu valcovania prstencov je možné nastaviť v prostredí integrovaného výrobného procesu, ku ktorému sa dostanete z hlavného okna grafického používateľského rozhrania. Novú úlohu vytvoríte buď výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nová úloha, alebo kliknutím na ikonu Nová úloha ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). V časti Typ úlohy a Systém jednotiek vyberte prepínač 3D valcovanie prstencov. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) (pozri obr. 42.1.1.). Otvorí sa sprievodca integrovaným výrobným procesom a v editore operácií uvidíte, že operácia 3D valcovanie prsteňov bola pridaná.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image001.jpg' | relative_url }})

Pridanie operácie valcovania prsteňov z hlavného okna grafického rozhrania

  
Operáciu valcovania prstencov môžeme do prostredia Integrovaného výrobného procesu pridať aj z kontextového menu „Nový projekt“, keď sa v tomto prostredí otvorí nový problém, ako je znázornené na obr. 42.1.2. Pomocou možnosti „Kopírovať existujúci projekt“ môžeme z kontextového menu „Nový projekt“ importovať predtým uložené projekty ako nové projekty.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image002.jpg' | relative_url }})

V okne „Nový projekt“ zadajte názov projektu a vyberte prvú operáciu

Operáciu „Ring Rolling“ môžeme do editora operácií pridať aj z karty „Explorer“ v prostredí integrovaného výrobného procesu, a to kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie „Ring Rolling“ (pozri obr. 42.1.3.) alebo presunutím operácie „Ring Rolling“ do okna editora operácií pomocou funkcie drag and drop.   
Keď sa operácia „Ring Rolling“ pridá do editora operácií, v okne na úpravu nastavení vlastností sa otvorí stránka výberu procesov.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image003.jpg' | relative_url }})

Pridanie operácie zo zoznamu operácií v Průzkumníku

Operáciu valcovania prstencov je možné pridať aj v dávkovom režime ako súčasť nastavenia viacerých operácií; podrobnejšie informácie o tomto type nastavenia nájdete v bode 42.1.27. Nastavenie operácie valcovania prstencov v dávkovom režime.

## Výber procesu

Na stránke „Proces“ si používateľ vyberie typ simulácie valcovania, ktorá sa má vykonať (pozri obr. 42.1.4.). Predvolene je vybraný proces valcovania prstencov. Ak má používateľ záujem o proces valcovania železničných kolies, môže vybrať príslušnú možnosť procesu, ako je znázornené na obr. 42.1.5.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image004.jpg' | relative_url }})

Stránka procesu (valcovanie prstencov)

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image005.jpg' | relative_url }})

Stránka procesu (valcovanie železničných kolies)

## Nastavenie simulácie

Na stránke „Nastavenie simulácie“ bude používateľ zadávať nastavenia procesu, ktoré sa majú použiť pri definovaní úlohy.  
**Typ 3D modelu:** V položke „Typ 3D modelu“ máme na výber možnosti „Celý diel“ alebo „Symetria“ v závislosti od symetrie geometrie, ktorú chceme v nastavení modelovať.  
**Tepelné výpočty:** Na karte „Tepelné výpočty“ (pozri obr. 42.1.6.) sú k dispozícii možnosti na výber typov objektov, na ktorých sa majú vykonať tepelné výpočty. 

  * **Konštantná teplota (izotermická)**: Ak používateľ zvolí túto možnosť, simulácia nevykonáva žiadne tepelné výpočty. Túto možnosť môže používateľ využiť v prípade, že zmena teploty v procese je zanedbateľná.

  * **Iba obrobok (neizotermické):** Ak používateľ zvolí túto možnosť, simulácia vykoná tepelný výpočet iba pre obrobok; táto možnosť je užitočná vo väčšine prípadov, keď používateľa zaujíma iba zmena teploty obrobku.

  * **Obrobok a valce (neizotermické):** Túto voľbu je možné použiť v prípade, že je potrebné vykonať tepelné výpočty tak pre obrobok, ako aj pre valce, s cieľom sledovať zmeny teploty týchto objektov.

**Modelovanie zŕn:** Ak má používateľ záujem o výstup týkajúci sa veľkosti zŕn, môže zaškrtnúť políčko „Modelovanie zŕn“, čím sa aktivuje výpočet veľkosti zŕn. Modelovanie zŕn je k dispozícii iba pre neizotermický proces.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image006.jpg' | relative_url }})

Stránka s nastaveniami simulácie

## Zoznam materiálov

Stránka „Materiál“ slúži na vytvorenie nového materiálu alebo načítanie materiálu z databázy a v prípade potreby na úpravu jeho vlastností výberom príslušného materiálu zo stromu operácií. Na stránke Zoznam materiálov môže používateľ načítať materiál pomocou možnosti Importovať údaje o materiáli zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (pozri obr. 42.1.7.). Používateľ môže materiál tiež uložiť pomocou ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image007.jpg' | relative_url }})

Zoznam materiálov – Strana

## Stránka objektu

Na stránke „Objekty“ je uvedený zoznam objektov, ktoré je možné použiť na základe typu procesu vybraného na stránke „Proces“. Objekty dostupné pre proces valcovania do prstencov (pozri obr. 42.1.8.) sú:

  * Obrobok – prsteň, 

  * Hnací valec 

  * Tlakový valec (trn)

  * 2 axiálne valce 

V predvolenom nastavení sú vybrané obrobok – prstenec, hnací valec a tlakový valec (trn), ktoré sú povinné pre nastavenie procesu valcovania prstencov. Ak používateľ potrebuje ďalšie objekty, môže zaškrtnúť príslušné políčka pre axiálne valce, sekundárny hnací valec a sekundárny tlakový valec. 

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image008.jpg' | relative_url }})

Stránka objektu (valcovanie prsteňov)

### Objekty pre nastavenie typu modelu „Symetria“

Vzhľadom na symetrický model budeme modelovať iba jednu polovicu usporiadania, preto je zoznam objektov taký, ako je znázornené na obr. 42.1.9.

  
![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image009.jpg' | relative_url }})

Stránka objektov pre symetrický model

## Definícia obrobku – prstencový objekt

Na tejto stránke môžeme definovať názov objektu, teplotu a os/stred obrobku, ako je znázornené na obr. 42.1.10. Používateľ môže importovať objekty z iných databáz alebo kľúčových súborov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objektoch pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).  
V prípade, že používateľ importuje 3D objekt zo súboru, bude funkcia ![]({{ '/assets/icons/pre_icons/mo_extract_cross_section_label.jpg' | relative_url }}) aktivovaná, aby mohol vytvoriť priečny rez importovaného objektu (pozri obr. 42.1.11.) a vygenerovať 3D prstenec s vytvoreným priečnym rezom. Funkcia ![]({{ '/assets/icons/pre_icons/mo_extract_cross_section_label.jpg' | relative_url }}) je aktívna aj pri importe 3D geometrie prstena. Os/stred importovaného objektu je možné vypočítať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image010.jpg' | relative_url }})

Stránka „Obrobok – krúžok“

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image011.jpg' | relative_url }})

Extrahovanie priečneho rezu z 3D tvaru

### Vytvorenie priečneho rezu z importovanej 3D geometrie

  * **Vytvorenie priečneho rezu pod určitým uhlom:** Táto voľba sa používa v prípade, že používateľ chce z importovanej geometrie vytvoriť priečny rez pod zadaným uhlom. Používateľ môže zadať hodnotu uhla a priečny rez pod týmto uhlom sa v zobrazenom priestore na prstenci zvýrazní, pozri obr. 42.1.12.

  * **Extrahovať priečny rez z rezov a použiť ich priemer:** Táto možnosť sa volí v prípade nerovnomerného prstena, keď chce používateľ rozdeliť importovaný geometrický objekt na zadaný počet rezov, z každého rezu extrahovať priečny rez a použiť priemernú veľkosť ako priečny rez na vytvorenie 3D obrobku. Rezy a priečne rezy sa zobrazujú v zobrazovacej oblasti, pozri obr. 42.1.13.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image012.jpg' | relative_url }})

Výpočet prierezu pri uhle

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image013.jpg' | relative_url }})

Extrakcia viacerých priečnych rezov z rezon a použitie ich priemeru

###   
Vytvorenie priečneho rezu z importovanej 3D siete

  * **Extrahovať priečny rez z vrstvy č.** : Táto voľba sa používa v prípade, že používateľ chce extrahovať priečny rez zo špecifikovanej vrstvy. Používateľ môže zadať číslo vrstvy a príslušná vrstva sa na prstenci v zobrazovacej oblasti zvýrazní, pozri obr. 42.1.14.

  * **Vytvoriť priečny rez z vrstiev a použiť ich priemernú hodnotu**: Táto voľba sa volí v prípade nerovnomerného prstena, keď chce používateľ extrahovať viacero priečnych rezov zo všetkých vrstiev a použiť priemernú veľkosť ako priečny rez na vytvorenie prstena; počet vrstiev dostupných v importovanom objekte sa zobrazuje v zobrazovacej oblasti, pozri obr. 42.1.15.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image014.jpg' | relative_url }})

Výrez priečneho rezu vo vrstve č.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image015.jpg' | relative_url }})

Extrahovanie viacerých prierezov z vrstiev a použitie ich priemeru

  * **Poloha merania priemeru:**

    * **Vonkajší priemer**: Táto voľba sa používa v prípade, že používateľ chce zastaviť simuláciu valcovania prstena v okamihu, keď vonkajší priemer prstena dosiahne zadanú hodnotu na vybranom mieste, ako je znázornené na obr. 42.1.16.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image056.jpg' | relative_url }})

Zmeraný vonkajší priemer obrobku

  * **Vnútorný priemer**: Táto voľba sa používa v prípade, že používateľ chce zastaviť simuláciu valcovania prstena v okamihu, keď vnútorný priemer prstena dosiahne zadanú vonkajšiu hodnotu na vybranom mieste, ako je znázornené na obr. 42.1.17.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image057.jpg' | relative_url }})

Zmeraný vnútorný priemer obrobku

  * **Poloha Z**: Pomocou tohto poľa môže používateľ určiť počiatočnú polohu merania priemeru pozdĺž osi Z obrobku – výška prstena, ako je znázornené na obr. 42.1.18.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image058.jpg' | relative_url }})

Poloha Z – poloha merania priemeru

**Poznámka:** Ak nezakrúžkujeme políčko „Poloha merania priemeru“, ako definícia priemeru sa použije „Maximálny vonkajší priemer“. Ak políčko „Poloha merania priemeru“ zakrúžkujeme, pre ovládacie prvky zastavenia sa použije vybraný priemer, a to buď „Nameraný vonkajší priemer obrobku“, alebo „Nameraný vnútorný priemer obrobku“.

## Definovanie 2D priečneho rezu

Používateľ môže vytvoriť geometriu pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}), ako je znázornené na obr. 42.1.19. Používateľ môže tiež importovať 2D geometriu pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a uložiť 2D geometriu pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). Ďalšie vysvetlenia k jednotlivým voľbám nájdete v častiach [12.1. 2D Geometry Data Defining ](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) a [12.2. 2D Geometry Data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image016.jpg' | relative_url }})

Stránka s 2D rezom

## Vytvorenie 2D siete

Sieť 2D priečneho rezu môžeme vytvoriť tak, že v režime s návodom zadáme počet prvkov, ako je znázornené na obr. 42.1.20. K pokročilým nastaveniam na riadenie vytvárania 2D siete sa dostanete pomocou prepínača „expertný režim“ na paneli nástrojov, pozri obr. 42.1.22. Ďalšie informácie o pokročilých možnostiach nájdete v [13.1. 2D Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/).   
**Použiť hrubú vnútornú sieť**: V režime s návodom má používateľ k dispozícii toto zaškrtávacie políčko na vytvorenie hrubej vnútornej siete, ako je znázornené na obr. 42.1.21.   
**Pomer k najväčšiemu prvku**: Pomocou tohto nastavenia môže používateľ relatívne ovládať veľkosť prvkov  
**Vytvoriť sieť** ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}): Po nastavení parametrov siete môže používateľ pomocou tohto tlačidla vytvoriť 2D sieť. 

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image017.jpg' | relative_url }})

Stránka 2D siete (režim s návodom)

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image018.jpg' | relative_url }})

Vytvorenie 2D siete pomocou hrubej vnútornej siete (režim s vedením)

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image019.jpg' | relative_url }})

Stránka 2D siete (režim pre pokročilých)

## Vytváranie 3D geometrie

Používateľ môže pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_revolve_from_2d_label.jpg' | relative_url }}) previesť definovaný 2D priečny rez na 3D geometriu (pozri obr. 42.1.23.), nastavenia pre konverziu 2D na 3D otočením je možné definovať na stránke „Otočiť z 2D“, ako je znázornené na obr. 42.1.23, a na konverziu kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Ďalšie informácie o ostatných možnostiach nájdete v [12.3. 3D Geometry data modelling.](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

### Nastavenia Revolve

**Digitalizácia**: Na riadenie bodov digitalizácie na 2D priečnom reze je možné použiť „podiel tolerancie dĺžky“ / „maximálny prípustný uhol“ / „minimálny prípustný uhol“.  
**Počet vrstiev v smere obruče**: Používateľ môže určiť počet vrstiev pozdĺž rotácie 2D priečneho rezu.  
**Stred a os**: Tu je možné definovať stred objektu „Ring“ a os, ktorá sa má použiť na otočenie 2D priečneho rezu.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image020.jpg' | relative_url }})

Stránka „3D geometria obrobku – prstenec“

###   
Import 3D geometrie

Ak používateľ načítal 3D geometriu obrobku zo súboru, môže použiť voľbu ![]({{ '/assets/icons/pre_icons/mo_extract_cross_section_label.jpg' | relative_url }}) na extrakciu priečneho rezu z 3D geometrie a jeho následné otočenie do 3D geometrie.   
V prípade nerovnomerného prstencového objektu môže používateľ importovať 3D geometriu a priamo prejsť na stránku 3D siete, kde môže vygenerovať 3D sieť a zachovať nerovnomernosť obrobku.  
Ak chce používateľ vytvoriť priečny rez pre nerovnomerný prstencový objekt, môže sa vrátiť na stránku „Obrobok – objekt“ a pomocou funkcie ![]({{ '/assets/icons/pre_icons/mo_extract_cross_section_label.jpg' | relative_url }}) z tejto stránky vygenerovať 3D geometriu obrobku s priemerným priečnym rezom.

## Vytvorenie 3D siete

Po definovaní 2D priečneho rezu a 3D geometrie môže používateľ vygenerovať 3D sieť. Na vygenerovanie 3D siete musí používateľ určiť počet otáčajúcich sa rezov v smere obruče, pozri obr. 42.1.24. V závislosti od geometrie obrobku môže používateľ zvoliť „metódu otáčania“ na vytvorenie 3D siete obrobku.

  * **Rotácia s konštantným prierezom:** Táto voľba sa používa na vytvorenie 3D siete v prípade, že obrobok má rovnomerný prierez. V prípade importovaného objektu/geometrie je potrebné definovať alebo extrahovať 2D prierez. Používateľ si môže prierez zobraziť pomocou zaškrtávacieho políčka „Zobraziť prierez“.

  * **Otočenie tak, aby zodpovedalo 3D tvaru:** Táto voľba sa používa na vytvorenie 3D siete pre prstenec s nerovnomerným prierezom. 3D sieť sa vytvorí na základe importovanej 3D geometrie/siete, ako je znázornené na obr. 42.1.25. Pri použití tejto možnosti sa automaticky extrahuje 2D prierez a otočí sa podľa meniaceho sa tvaru prierezu.

**Parametre otáčania:** Tu je možné nastaviť „počet otáčajúcich sa úsekov“ v smere obruče.  
**Vytvorenie siete:** Používateľ musí kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby sa na základe zadaných nastavení vytvorila 3D sieť.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image021.jpg' | relative_url }})

Vytvorenie 3D siete pomocou operácie „revolve“ s konštantným rozmerom prierezu

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image022.jpg' | relative_url }})

Vytvorenie 3D siete pomocou funkcie „revolve“ tak, aby sa prispôsobila 3D tvaru

## Orientácia

Ak je os importovaného objektu naklonená voči osi +Z, môže ju používateľ vyrovnať s osou +Z pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_orient_to_+z_button.jpg' | relative_url }}). Uhol orientácie sa automaticky vypočíta a zobrazí tak, ako je znázornené na obr. 42.1.26.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image023.jpg' | relative_url }})

Stránka „Orientácia obrobku“

## Stránka s materiálmi

Na stránke materiálov sa zobrazujú všetky materiály pridané do zoznamu materiálov (ako je znázornené na obr. 42.1.27.). Používateľ môže vybrať požadovaný materiál a priradiť ho k príslušnému objektu. Ak požadovaný materiál nie je v zozname k dispozícii, môže ho používateľ načítať na stránke materiálov objektu pomocou funkcie Importovať údaje o materiáli zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Ak materiál nie je k dispozícii v knižnici DEFORM, môže používateľ vytvoriť nový materiál pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Používateľ môže materiál zo zoznamu odstrániť pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) alebo údaje o materiáli upraviť pomocou ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}). Upravený alebo novo definovaný materiál je možné uložiť pomocou ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image024.jpg' | relative_url }})

Priradenie materiálu k obrobku

## Obrobok BCC

Na stránke „Okrajové podmienky“ môže používateľ objektu priradiť rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s ostatnými objektmi a s prostredím. Medzi bežne používané okrajové podmienky patrí výmena tepla s prostredím pri simuláciách zahŕňajúcich prenos tepla, symetria a rýchlosť, ako je znázornené na obr. 42.1.28. Hraničné podmienky sa automaticky definujú pri generovaní 3D siete na základe nastavení simulácie v šablóne valcovania prstencov. Ak ich chce používateľ upraviť, môže využiť možnosti dostupné na tejto stránke. Ďalšie informácie o týchto možnostiach nájdete v [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image025.jpg' | relative_url }})

Obrobok BCC

## Nehnuteľnosť

V okne „Vlastnosti objektu“ sa zadávajú rôzne parametre objektu, ktoré ovplyvňujú buď termomechanické správanie objektu, alebo správanie numerického riešenia. (Pozri obr. 42.1.29.) Objemová kompenzácia sa najčastejšie používa pri valcovaní prstencov a je možné ju aktivovať výberom jednej z možností v časti „Cieľový objem“ a výpočtom aktuálneho objemu objektu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}). Ďalšie informácie nájdete v [16\. Object properties](/docs/en/pre_processor/16_object_properties/16_object_properties/).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image026.jpg' | relative_url }})

Stránka nehnuteľnosti

## Inicializácia

V okne „Initialize“ (Inicializácia) sú k dispozícii na inicializáciu niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posun, hustota, veľkosť zŕn mikrostruktúry a veľkosť častíc. Ak chce používateľ pri valcovaní s viacerými prstencami inicializovať teplotu, deformáciu alebo veľkosť zŕn, môže použiť túto stránku inicializácie.

  
Používateľ môže inicializovať hodnoty týchto stavových premenných tak, že ich zadá do príslušného poľa a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 42.1.30. znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne „Initialize“. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien uzlov a prvkov. Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“, nájdete v [17.1 Node data window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [11.2 Element data window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image027.jpg' | relative_url }})

Načítanie stránky

## Definícia hnacieho valca

Hnací valec je tuhý objekt v šablóne „Ring Rolling“. Teplotu, stred a os je možné nastaviť na stránke objektu „Hnací valec“, ako je znázornené na obr. 42.1.31. Ak je typ nastavenia simulácie neizotermický a výpočty teploty sa vykonávajú aj na valcoch, hnací valec musí mať sieť, aby bolo možné vypočítať teplotu tohto objektu. Definícia geometrie hnacieho valca a definícia siete sú podobné ako v prípade obrobku. Ďalšie informácie o definovaní geometrie a siete nájdete v častiach 42.1.6. Definovanie objektu obrobku – prstena, 42.1.7. Definovanie 2D priečneho rezu, 42.1.8. Vytvorenie 2D siete, 42.1.9. Vytvorenie 3D geometrie, 42.1.10. Vytvorenie 3D siete a 42.1.12. Stránka materiálu.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image028.jpg' | relative_url }})

Stránka „Driving Roll“

###   
Určenie orientácie hnacieho valca

Ak vytvorený alebo importovaný hnací valec nie je na správnom mieste, je možné použiť stránku „Orientácia“ v rámci objektu „Hnací valec“ v stromovej štruktúre objektov na umiestnenie valca vo vzťahu k obrobku pozdĺž osi, ako je znázornené na obr. 42.1.33. Používateľ môže valec umiestniť vzhľadom na stred objektu alebo na spodnú plochu. Na základe definovaných parametrov sa aktuálny objekt posunie a kolízia sa umiestni voči obrobku; smer kolízie závisí od aktuálneho typu objektu, ako je hnací valec, tlakový valec a axiálny valec.  
**Nastavenie relatívnej vzdialenosti od stredu objektu:** Táto voľba slúži na umiestnenie hnacieho valca tak, že sa definuje vertikálna vzdialenosť medzi stredom aktuálneho objektu a stredom obrobku spolu so smerom merania pomocou možnosti „Relatívna poloha aktuálneho objektu“ (+Z alebo -Z), pozri obr. 42.1.33.  
**Nastavenie relatívnej vzdialenosti medzi spodnými plochami objektov:** Táto voľba slúži na umiestnenie hnacieho valca tak, že sa definuje vertikálna vzdialenosť medzi spodnou plochou aktuálneho objektu a spodnou plochou obrobku spolu so smerom merania pomocou „Relatívnej polohy aktuálneho objektu“ (+Z alebo -Z), pozri obr. 42.1.38.  
**Reset**: Používateľ môže pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) vrátiť zariadenie do pôvodnej polohy pred otvorením stránky s nastavením orientácie.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image029.jpg' | relative_url }})

Vodiaci valec pred orientáciou

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image030.jpg' | relative_url }})

Vodíci valec po orientácii

### Definícia pohybu hnacieho valca

V šablóne „Ring Rolling“ môže hnací valec vykonávať ako posuvný, tak aj rotačný pohyb, ako je znázornené na obr. 42.1.34. Pohyb je potrebné definovať pomocou možností dostupných v režime „Guided Mode“. 

Pohyb pri preklade možno definovať ako rýchlosť alebo silu. Rýchlosť alebo silu možno definovať ako konštantu, funkciu času alebo funkciu priemeru (vonkajší priemer prstena). Smer pohybu je v šablóne na valcovanie prstencov pevne stanovený a nie je možné ho zmeniť, pozri obr. 42.1.34.

Rotačný pohyb možno definovať ako uhlovú rýchlosť alebo krútiaci moment. Uhlovú rýchlosť alebo krútiaci moment možno definovať ako konštantu, funkciu času alebo funkciu uhla (uhla otáčania), pozri obr. 42.1.35.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image031.jpg' | relative_url }})

Ovládacie prvky pre posun prekladu (pre režim s navádzaním)

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image032.jpg' | relative_url }})

Ovládacie prvky rotačného pohybu (pre režim s navádzaním)

## Definícia tlakového valca

Tlakový valec je tuhý objekt v šablóne „Ring Rolling“. Teplotu, stred a os je možné nastaviť na stránke objektu „Tlakový valec“, ako je znázornené na obr. 42.1.36. Ak je typ nastavenia simulácie neizotermický a výpočty teploty sa vykonávajú aj na valcoch, musí mať tlakový valec sieť, aby bolo možné vypočítať teplotu tohto objektu. Definícia geometrie tlakového valca a definícia siete sú podobné ako v prípade obrobku. Ďalšie informácie o definovaní geometrie a siete nájdete v častiach 42.1.6. Definovanie objektu obrobku – prstena, 42.1.7. Definovanie 2D priečneho rezu, 42.1.8. Vytvorenie 2D siete, 42.1.9. Vytvorenie 3D geometrie, 42.1.10. Vytvorenie 3D siete a 42.1.12. Stránka materiálu.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image033.jpg' | relative_url }})

Stránka o tlakových valcoch

###   
Orientácia tlakového valca

Podobne ako hnací valec, aj tlakový valec je možné umiestniť vo vzťahu k obrobku tak, ako je znázornené na obr. 42.1.37 a obr. 42.1.38. Ďalšie informácie o možnostiach umiestnenia nájdete v časti „Orientácia hnacieho valca“.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image034.jpg' | relative_url }})

Tlakový valec pred orientáciou

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image035.jpg' | relative_url }})

Tlakový valec po orientácii

###   
Definícia pohybu tlakového valca

Podobne ako hnací valec môže aj tlakový valec vykonávať posuvný aj rotačný pohyb, ako je znázornené na obr. 42.1.39. Pohyb je potrebné definovať pomocou možností dostupných v režime s vedením.

Pohyb prekladu možno definovať ako rýchlosť, dráhu alebo PID. Rýchlosť možno definovať ako konštantnú, ako funkciu času alebo ako funkciu priemeru. Dráhu možno definovať ako „zdvih (Y) ako funkciu času“. Pohyb typu PID sa môže použiť na definovanie pohybu na základe rastu prstena a môže byť definovaný ako „rýchlosť rastu prstena ako funkcia priemeru“. Smer pohybu je v šablóne valcovania prstena pevne stanovený a nemožno ho meniť, pozri obr. 42.1.39.

Rotačný pohyb možno definovať ako uhlovú rýchlosť alebo krútiaci moment. Uhlovú rýchlosť alebo krútiaci moment možno definovať ako konštantu, funkciu času alebo funkciu uhla (uhla otáčania), pozri obr. 42.1.39.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image036.jpg' | relative_url }})

Stránka o pohybe tlakového valca

## Definícia axiálneho naklonenia

Axiálny valec je tuhý objekt v šablóne „Ring Rolling“. Teplotu, stred a os je možné nastaviť na stránke objektu „Axiálny valec“, ako je znázornené na obr. 42.1.40. Ak je typ nastavenia simulácie neizotermický a výpočty teploty sa vykonávajú aj na valcoch, musí mať axiálny valec sieť, aby bolo možné vypočítať teplotu tohto objektu. Geometriu axiálnych valcov možno najčastejšie vytvoriť pomocou primitívu „Cone“ (kužeľ), ktoré je k dispozícii v 2D primitívoch, pozri obr. 42.1.41. Definícia geometrie axiálneho valca a definícia siete sú podobné ako v prípade obrobku. Ďalšie informácie o definovaní geometrie a siete nájdete v častiach 42.1.6. Definovanie objektu „Obrobok – prstenec“, 42.1.7. Definovanie 2D priečneho rezu, 42.1.8. Vytvorenie 2D siete, 42.1.9. Vytvorenie 3D geometrie, 42.1.10. Vytvorenie 3D siete a 42.1.12. Stránka materiálu.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image037.jpg' | relative_url }})

Stránka „Axial Roll“

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image038.jpg' | relative_url }})

Stránka s primitívom „Axial Roll“

### Orientácia axiálnej valcovacej osi

Na stránke „Orientácia axiálneho naklonenia“ môže používateľ definovať uhol polohy axiálneho naklonenia a horizontálnu vzdialenosť, ako je znázornené na obr. 42.1.42., a následne kliknúť na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}). Túto stránku „Orientácia“ je možné použiť na umiestnenie axiálneho valca po obvode prstena v smere obručí zadaním uhla v poli „Uhol otáčania“ a pozdĺž šírky prstena zadaním horizontálnej vzdialenosti medzi koncom kužeľa a stredom prstena, ako je znázornené na obr. 42.1.43.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image039.jpg' | relative_url }})

Axiálne valcovanie pred orientáciou

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image040.jpg' | relative_url }})

Axiálne valenie po orientácii

### Stránka o axiálnom pohybe valca

Podobne ako pri ovládaní pohybu valcov, môže používateľ pre axiálne valce definovať tak posuvný pohyb, ako aj rotačný pohyb, ako je znázornené na obr. 42.1.44.

Pohyb pri preklade možno definovať ako rýchlosť, silu alebo dráhu. Rýchlosť alebo silu možno definovať ako konštantu, funkciu času alebo funkciu priemeru, zatiaľ čo dráhu možno definovať ako funkciu času alebo funkciu priemeru, pozri obr. 42.1.44.

Rotačný pohyb možno definovať ako uhlovú rýchlosť alebo krútiaci moment. Uhlovú rýchlosť alebo krútiaci moment možno definovať ako konštantu, funkciu času alebo funkciu uhla (uhla otáčania), pozri obr. 42.1.44.

  * **Automatický radiálny pohyb:** Axiálne valce sa môžu automaticky pohybovať v radiálnom smere tak, aby sa vrchol axiálneho valca vždy nachádzal v strede prstena v súlade s jeho rozťahovaním. Na aktiváciu tejto funkcie musí používateľ zaškrtnúť políčko „Automatický radiálny pohyb vzhľadom na rozťahovanie obrobku“.

  * **Adaptívny rotačný pohyb:** Ak používateľ zaškrtne políčko „Adaptívne ovládanie rotačného pohybu“, axiálne valce sa budú otáčať v súlade s otáčaním prstena bez akéhokoľvek preklzávania.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image041.jpg' | relative_url }})

Stránka o axiálnom pohybe valca

## Axial Roll č. 2 – Strana

Pre druhý axiálny valec môže používateľ využiť možnosť „Kopírovať axiálny valec č. 1“, čím sa všetky údaje z axiálneho valca č. 1 skopírujú do objektu axiálneho valca č. 2 (pozri obr. 42.1.45.) a automaticky sa umiestni v smere -Z, pozri obr. 42.1.46.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image042.jpg' | relative_url }})

Axial Roll č. 2 – strana

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image043.jpg' | relative_url }})

Kopírovanie osového valca č. 1 do osového valca č. 2

## Polohovanie

Ak chce používateľ aj po nastavení orientácie ďalej upravovať polohu niektorého z týchto objektov, môže použiť tlačidlo „Poloha objektov“ na stránke „Polohovanie“. Na umiestnenie objektov sú k dispozícii rôzne možnosti polohovania, ako je znázornené na obr. 42.1.47. Ďalšie informácie o týchto možnostiach nájdete v [19\. Object positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image044.jpg' | relative_url }})

Ovládacie prvky na nastavenie polohy objektu

## Plánované umiestnenie

Ak si používateľ nie je istý umiestnením objektu, ako je to v prípade objektov typu „Čítanie z databázy“, naplánované umiestňovanie pomôže objekty presne umiestniť. Plánované umiestňovanie umožňuje používateľovi definovať umiestnenie objektov v nastaveniach integrovaného výrobného procesu pre nasledujúce operácie, pre ktoré sa databáza (DB) nevytvára, tak, aby boli objekty umiestnené pred vytvorením databázy počas spustenia simulácie v dávkovom režime (pozri obr. 42.1.48.).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image045.jpg' | relative_url }})

Možnosti plánovaného umiestnenia

## Kontakt

Používateľ môže definovať kontakt medzi obrobkom a ostatnými valcami tak, že stanoví vzťahy medzi objektmi, ako je znázornené na obr. 42.1.49. V prípade neizotermických procesov valcovania musí používateľ definovať koeficient trenia a koeficient prenosu tepla na rozhraní, zatiaľ čo v prípade izotermického procesu valcovania musí definovať hodnotu trenia.  
**Systém**: Po výbere tohto prepínača systém priradí predvolené vzťahy medzi objektmi. V prípade potreby môže používateľ pridať mazivá tak, že z roletového menu vyberie možnosť „Pridať nové“ a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), alebo môže na účely simulácie načítať požadované mazivá z knižnice.  
**Používateľ:** Pri operácii „Ring Rolling“ je štandardne zaškrtnuté tlačidlo „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), ako je znázornené na obr. 42.1.49. Používateľ môže zmeniť hodnotu každého vzťahu tak, že ho vyberie a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môže používateľ priradiť rovnaké hodnoty všetkým vzťahom. Kliknutím na tlačidlo môže používateľ vypočítať toleranciu kontaktu. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) môže používateľ vygenerovať vzťah kontaktu. Zaškrtnutím políčka vedľa vzťahu kontaktu môže používateľ definovať zotrvačný kontakt. Ďalšie informácie nájdete v časti [20\. Inter-Object Data Relations.](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image046.jpg' | relative_url }})

Stránka s kontaktnými údajmi

## Ovládacie prvky na zastavenie simulácie valcovania prsteňov

Používateľ môže simuláciu valcovania prstencov zastaviť pomocou nastavení dostupných na stránke Ovládacie prvky zastavenia, ako je znázornené na obr. 42.1.50.  
**Max. vonkajší priemer obrobku**: Táto možnosť sa zobrazuje na základe definície priemeru uvedenej na stránke objektu obrobku; na stránke objektu obrobku nedefinujeme riadenie zastavenia (pozri **Poloha merania priemeru**). Ak bola explicitne definovaná poloha merania priemeru, na tomto mieste sa zobrazia príslušné informácie. Ak nie je definovaná poloha merania priemeru, zobrazí sa maximálny vonkajší priemer obrobku, čo je predvolená definícia priemeru.

**Trvanie procesu****:** Simulácia sa zastaví po uplynutí nastaveného trvania procesu.  
**Max. posun primárneho valca**: Používateľ môže pomocou roletového menu vybrať jeden z valcov ako „primárny valec“ a nastaviť maximálny posun, pri ktorom sa má simulácia zastaviť. Zobrazí sa smer pohybu vybraného primárneho valca. Simulácia sa zastaví po tom, čo primárny valec prekročí nastavený posun.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image047.jpg' | relative_url }})

Stránka ovládacích prvkov zastavenia

## Ovládacie prvky pre krokovanie a prepočítavanie siete pri valcovaní prstencov

Simuláciu valcovania prstencov je možné riadiť na základe časového kroku a ukladať na základe frekvencie otáčok. Používateľ môže tiež nastaviť frekvenciu výpočtu teploty pri neizotermických simuláciách a naplánovať premenovanie siete. Ovládacie prvky pre časový krok a premenovanie siete sú znázornené na obr. 42.1.51.  
**Počet krokov:** Tu je možné zadať počet krokov, ktoré sa majú simulovať. Používateľ môže zadať vyšší počet krokov a pomocou kritérií ukončenia simuláciu predčasne ukončiť.  
**Veľkosť kroku rotácie na uloženie:** Pri spustení simulácie sa musí vypočítať každý krok, ale nie je nutné ho vždy ukladať do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať väčší úložný priestor. Údaje zo simulácie sa budú zapisovať do databázy na základe frekvencie kroku rotácie, ktorá je tu definovaná.  
**Maximálny povolený časový krok:** Používateľ musí určiť časový krok, ktorý sa bude používať ako časový interval na jeden krok pri rôznych výpočtoch.   
**Výpočet teploty:** Používateľ môže pomocou možností na karte „Výpočet teploty“ nastaviť frekvenciu výpočtov teploty tak, aby zodpovedala frekvencii deformácie, alebo aby sa vykonávala pri dosiahnutí určitého uhla otáčania.  
**Ovládacie prvky pre generovanie novej siete:** Používateľ môže naplánovať generovanie novej siete pre obrobok po uplynutí stanoveného počtu otáčok, aby sa zachoval správny tvar obrobku v prípade zložitých geometrií.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image048.jpg' | relative_url }})

Kroky a ovládacie prvky pre prepočítanie siete

## Ovládacie prvky simulácie

Na tejto stránke môže používateľ definovať obmedzenia na stabilizáciu obrobku počas jeho otáčania v priebehu simulácie, ako aj niekoľko pokročilých nastavení, ako je znázornené na obr. 42.1.52 a obr. 42.1.53. Údaje definované na tejto stránke sa zapíšu do súboru DEF_RRE.DAT.

### Kontrola stability

**Riadenie stredu obrobku:** Ak používateľ počas simulácie zistí akékoľvek problémy so stabilitou obrobku/krúžku, môže obmedziť otáčanie a posun obrobku v určených smeroch, aby sa zachoval stred obrobku, ako je znázornené na obr. 42.1.52.  
**Virtuálny stôl:** Používateľ môže tiež pridať virtuálny stôl v hornej alebo dolnej časti tak, že zaškrtne príslušné políčko a určí vzdialenosť umiestnenia virtuálneho stola od hornej/spodnej plochy obrobku, pozri obr. 42.1.52. Zobrazí sa aktuálna hodnota súradnice Z v príslušnom smere.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image049.jpg' | relative_url }})

Ovládacie prvky simulácie – Ovládacie prvky stability

### Pokročilé ovládanie 

**Kontrola prieniku uzlov:** Používateľ môže nastaviť frekvenciu krokov, pri ktorých sa overuje, či uzly zo zoznamu prenikajú do obrobku/krúžku, pozri obr. 42.1.53. Ak je hodnota nastavená na 0 alebo zápornú hodnotu, systém nepreveruje vniknutie. Ak je hodnota nastavená v rozmedzí od 1 do 50, systém preveruje vniknutie každých 50 krokov. Ak je hodnota nastavená na hodnotu väčšiu ako 50, systém vykonáva kontrolu s frekvenciou zodpovedajúcou nastavenému počtu krokov.  
**Vyhľadávanie kontaktov:** Používateľ môže tiež určiť uhol vyhľadávania kontaktov, čím sa zvýši rýchlosť výpočtu; pozri obr. 42.1.53. Uhol vyhľadávania začína na strane prívodu medzi hnacím valcom a tlakovým valcom (trnom).  
**Vynútiť otáčanie prstena:** Ak sa prstenec neotáča správne, používateľ môže zaškrtnúť políčko „Vynútiť otáčanie obrobku, ak sa v určitých krokoch neotáča správne“, čím sa počas procesu valcovania prstena vykonajú drobné korekcie jeho otáčania, pozri obr. 42.1.53.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image050.jpg' | relative_url }})

Ovládacie prvky simulácie – Pokročilé ovládacie prvky 

## Vytvoriť databázu

Akonáhle používateľ dokončí nastavenie úlohy valcovania prstencov, môže túto stránku použiť na kontrolu zadaných údajov a vytvorenie databázy. Od verzie v12.0.2 je k dispozícii prehľad nastavení simulácie prevádzky. (Pozri obr. 42.1.54.)  
**Kontrola Data![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}):** Táto kontrola overuje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však počas kontroly údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.  
**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}):** Kliknutím na toto tlačidlo sa vygeneruje databáza pre inštaláciu. (Pozri obr. 42.1.54.)  
**Pridať súbor .key:** Akékoľvek informácie, ktoré nie sú definované v šablóne, ale stále sa vzťahujú na daný proces, je možné načítať ako súbor .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt; tieto hodnoty je možné definovať v súbore .key a uložiť do zadaného umiestnenia. Následne je možné zmeniť len potrebné hodnoty v súbore .key a simuláciu znovu spustiť, aby sa preskúmal vplyv zmeny parametrov.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image051.jpg' | relative_url }})

Vytvoriť stránku databázy

## Nastavenie prevádzky valcovania prsteňov v dávkovom režime

Operáciu valcovania prstencov je možné nastaviť v dávkovom režime ako súčasť viacerých operácií v prostredí integrovanej výroby. Používateľ môže pridať operáciu valcovania prstencov do postupnosti s ostatnými operáciami, ako je znázornené na obr. 42.1.55.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image052.jpg' | relative_url }})

Typ objektu „Obrobok – krúžok“ sa načítava z databázy

### Obrobok – prstenec sa načíta z databázy

Pri načítaní objektu z databázy sa používateľovi zobrazí začiarkavacie políčko „Regenerovať prstenec“, ako je znázornené na obr. 42.1.56. Ak používateľ zaškrtne políčko „Regenerate Ring“, do stromu operácií ![]({{ '/assets/icons/pre_icons/mo_extract_cross_section_label.jpg' | relative_url }}) sa pridajú stránky 2D Mesh a 3D Mesh (pozri obr. 42.1.56), ktoré možno použiť na vytvorenie tvaru prstena a siete. Používateľ môže nastaviť os a stred. Ak nie je os nastavená a hodnoty sú „0“, ako os sa nastaví smer Z a pri opustení stránky objektu sa zobrazí kontextové okno „Zero Axis Vector“ informujúce o nastavenom smere (0,0,1), ako je znázornené na obr. 42.1.56.   
Keď je prsteň v stave „Načítané z databázy“ a používateľ klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránke objektu, otvorí sa stránka „Extrahovať priečny rez“, ako je znázornené na obr. 42.1.56.

###   
Prerez pre načítanie z objektu databázy

Používateľ má k dispozícii možnosti „Konštantný prierez“ a „Premenný prierez“ na vytvorenie prierezu z obrobku, ako je znázornené na obr. 42.1.56.   
**Konštantný prierez:** Ak je zvolený konštantný prierez, systém vygeneruje prstenec s konštantným prierezom. Ak sa očakáva, že výstup z predchádzajúcich operácií vytvorí rovnomerný prstenec, môže používateľ využiť možnosť „Extrahovať jeden prierez“ na vytvorenie prstenca s konštantným prierezom. Ak sa očakáva, že výsledkom predchádzajúcich operácií bude nerovnomerný prstenec, môže používateľ extrahovať viacero prierezov zo špecifikovaného počtu vrstiev a použiť priemernú veľkosť ako prierez pomocou možnosti „Extrahovať prierez z vrstiev(*)/rezov a použiť ich priemer“. Ak je typ siete objektu „Načítať z databázy“ tehlová sieť, počet vrstiev určí systém.  
**Premenlivý prierez:** Ak sa predpokladá, že výstup z predchádzajúcich operácií vytvorí nerovnomerný prstenec a používateľ chce vytvoriť prstenec s nerovnomerným prierezom, môže použiť túto možnosť. Používateľ môže pomocou funkcie „Extrahovať prierez z vrstiev(*)/rezov“ definovať extrakciu viacerých prierezov a ich zachovanie na vytvorenie nerovnomerného prstenca. Ak je typ siete objektu „Načítať z databázy“ tehlová sieť, počet vrstiev určí systém.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image053.jpg' | relative_url }})

Extrakcia priečneho rezu na regeneráciu prstena

###   
Vytvorenie 2D siete priečneho rezu obrobku

Keďže prierez sa získava z objektu, ktorý je „načítaný z databázy“, pri regenerácii tvaru prstena je vždy potrebné vygenerovať novú 2D sieť. Používateľ môže zaškrtnúť políčko „Vykonaj remesh pred touto operáciou“, ako je znázornené na obr. 42.1.57, a definovať nastavenia 2D siete, ktoré sa majú použiť pri generovaní novej siete. Viac informácií o nastaveniach siete nájdete v [13.1.2D Mesh Generation.](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/).

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image054.jpg' | relative_url }})

Stránka 2D siete pre objekt „Čítanie z databázy“

###  Vytvorenie 3D siete obrobku

Ak používateľ regeneruje tvar prstena pre objekt typu „Načítať z databázy“, musí pre obrobok vygenerovať 3D sieť. V závislosti od typu prierezu vybraného na stránke objektu „Obrobok“ (pozri časť „Extrahovanie prierezu pre objekt typu Načítať z databázy“) sa automaticky vyberie metóda otáčania. V nastaveniach 3D siete môže používateľ definovať počet rotujúcich úsekov v smere obruče, ako je znázornené na obr. 42.1.58.

![]({{ '/assets/images/operation_templates/42_ring_rolling/42_1_ring_rolling/image055.jpg' | relative_url }})

Stránka 3D siete pre objekt „Čítanie z databázy“

## Spustenie simulácie

Akonáhle používateľ vykoná všetky potrebné zmeny na vytvorenie priečneho rezu a generovanie siete počas simulácie pre obrobok, ktorý je „načítaný z databázy“, môže projekt uložiť a prejsť na kartu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Používateľ môže kliknúť na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) a z rozbaľovacieho menu vybrať príslušnú možnosť na spustenie simulácie.
