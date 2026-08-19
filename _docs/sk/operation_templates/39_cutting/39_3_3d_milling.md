---
lang: sk
title: "39.3. 3D frézovanie"
---

# 39.3. 3D frézovanie

39.3.1. Prehľad systému

39.3.2. Pridanie frézovacej operácie

39.3.3. Stránka procesu

39.3.4. Zoznam materiálov

39.3.5. Nástroj

39.3.5.1. Vložiť geometriu

39.3.5.2. Materiál povlaku 

39.3.5.3. Výber materiálu nástroja

39.3.5.4. Vytvorenie siete nástroja

39.3.5.5. Nástroj BCC

39.3.6. Obrobok

39.3.6.1. Geometria obrobku

39.3.6.2. Výber materiálu obrobku

39.3.6.3. Vytvorenie siete obrobku

39.3.6.4. Kryštálová mriežka obrobku

39.3.7. Kontrola

39.3.8. Opotrebenie nástrojov

39.3.9. Kontakt

39.3.10. Riadenie krokov

39.3.11. Vytvorenie databázy

## Prehľad systému

DEFORM® poskytuje šablónu pre obrábanie, ktorú je možné použiť na nastavenie procesu frézovania. Šablónu je možné využiť na analýzu rezacích síl, rezacích teplôt, tvaru triesok, opotrebenia nástroja a na výpočet životnosti nástroja. Inžinier môže skúmať vplyv parametrov procesu, ako sú rýchlosť rezu, posuv a hĺbka rezu, na reakciu procesu. Šablóna zjednodušuje definíciu modelu a používa rovnaký technický jazyk ako procesný inžinier. Zjednodušený model sa generuje na základe posuvu a hĺbky rezu, ako je znázornené na obr. 39.3.1. Frézovací nástroj sa otáča okolo osi Z, pričom hĺbka rezu je v smere +Y a smer posuvu je -X; posuv a hĺbka rezu sa merajú od bodu X = Z = 0.

## Pridanie frézovacej operácie

Na nastavenie procesu frézovania musí používateľ pridať 3D šablónu rezu a na stránke „Proces“ vybrať možnosť „**Frézovanie**“, ako je znázornené na obr. 39.3.2. Ďalšie informácie o tom, ako pridať úlohu, nájdete v dokumente [39.2.1. How to add 3D Cutting Operation](39_2_3d_turning.htm#39_2_1_How_to_add_3D_Cutting_Operation).

## Stránka procesu

Parametre potrebné na nastavenie procesu frézovania sú uvedené na obr. 39.3.2.  
Prenos tepla v prostredí: Na tejto karte sa nastavujú teplota prostredia a koeficient konvekcie. Ďalšie informácie o nastavení týchto parametrov nájdete tu.

**Rýchlosť rezania** (v): Je definovaná ako rýchlosť, ktorou sa nástroj pohybuje. Rýchlosť rezania sa môže uvádzať v jednotkách mm/s alebo m/min v systéme SI a v jednotkách in/s alebo ft/min v anglických jednotkách.

**Rýchlosť otáčania**: Určuje rýchlosť otáčania nástroja. Rýchlosť otáčania možno uvádzať v otáčkach za minútu (rpm) alebo v radiánoch za sekundu.

**Priemer frézy** (D): Určuje priemer frézy. Táto hodnota priemeru sa použije na vytvorenie základného tvaru obrobku.

**Hĺbka rezu** (d): Ide o hrúbku kovu, ktorá sa odstraňuje počas obrábania. Je to kolmá vzdialenosť meraná medzi obrábanou plochou a neobrábanou plochou obrobku.

**Rýchlosť posuvu** (f): Je definovaná ako vzdialenosť, ktorú nástroj prejde počas jednej otáčky obrobku. Hodnota rýchlosti posuvu sa aktualizuje na stránke s geometrickými primitívami obrobku. Môže byť definovaná v jednotkách mm/ot alebo mm/s v systéme SI a v jednotkách in/ot alebo in/s v anglických jednotkách.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0001.jpg' | relative_url }})

Simulačný model a definícia základných parametrov rezania

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0002.jpg' | relative_url }})

Stránka o procese frézovania

## Zoznam materiálov

Na tejto stránke „Zoznam materiálov“ môže používateľ načítať materiál z knižnice, pomocou kľúčového slova alebo z databázového súboru pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. 39.3.3. Materiály načítané na tejto stránke je možné priradiť k objektom na príslušnej stránke materiálov. Používateľ môže tiež pridať nový materiál pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a definovať jeho vlastnosti. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) môže používateľ odstrániť načítaný materiál. Používateľ môže materiál uložiť aj pomocou možností ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0003.jpg' | relative_url }})

Priradenie materiálu do zoznamu materiálov

## Nástroj 

Na tejto stránke „Nástroj“ môže používateľ nastaviť teplotu objektu nástroja. Objekt nástroja môžeme načítať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}) (pozri obr. 39.3.4.). Ak chce používateľ vypočítať tepelné údaje pre objekt nástroja, zaškrtne políčko „**Vypočítať teplotu nástroja**“ a zistí, že sa aktivujú možnosti vytvorenia siete pre nástroj, vďaka čomu je možné vytvoriť sieť nástroja na výpočet rozloženia teploty.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0004.jpg' | relative_url }})

Stránka s nástrojmi

### Vložiť geometriu 

Pri frézovaní nie je k dispozícii definícia základnej geometrie pre výmenné doštičky, ako je znázornené na obr. 39.3.5. Používateľ môže importovať geometriu nástroja pomocou možností Import geometrie ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}). Po importe geometrie môže používateľ prepositionovať nástroj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_edit_position_label_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0005.jpg' | relative_url }})

Stránka s geometriou vložky

####   
Definovanie geometrie nástroja pomocou možnosti „Importovať geometriu“

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a naimportujte geometriu DNMA432 z programu DEFORM, ktorá sa nachádza v priečinku „\3D\Machining\Insert\SI“ alebo „\3D\Machining\Insert\EN“ v závislosti od systému jednotiek. Po naimportovaní geometrie sa otvorí okno s pokynmi na ručné polohovanie. Ak je importovaný nástroj už v správnej polohe, používateľ ho nemusí polohovať; v opačnom prípade môže pokračovať v ručnom polohovaní podľa pokynov. Po dokončení polohovania môže používateľ kliknúť na tlačidlo na zatvorenie okna, ako je znázornené na obr. 39.3.6. Možnosti ručného polohovania sú k dispozícii, ako je znázornené na obr. 39.3.7.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0006.jpg' | relative_url }})

Po importe geometrie sa zobrazia možnosti umiestnenia

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0007.jpg' | relative_url }})

Možnosti ručného nastavenia polohy

### Materiál povlaku 

Používateľ môže na výmennú dosku naniesť povlak tak, že na stránke „Materiál povlaku“ definuje povlakovú vrstvu a jej hrúbku. Materiál vrstvy povlaku a jej hrúbku môže používateľ definovať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}), ako je znázornené na obr. 39.3.8. Ak chce používateľ odstrániť akúkoľvek vrstvu, musí vybrať príslušnú vrstvu a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}).

**Extrahovať informácie o povlaku**: Po vytvorení povlaku môžeme pomocou tohto tlačidla extrahovať informácie o povlaku.

**Odstrániť vrstvu**: Pomocou tohto tlačidla môžeme odstrániť aj vrstvy s nákladmi. 

Zaškrtnutím políčka „**Zachovať stavové premenné a okrajové podmienky**“ môže používateľ vytvoriť povlakovú vrstvu bez straty údajov o stavových premenných a okrajových podmienkach nástroja.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0008.jpg' | relative_url }})

Stránka o materiáloch na povrchovú úpravu

### Výber materiálu nástroja

Na stránke materiálov sa zobrazujú všetky materiály pridané do zoznamu materiálov, ako je znázornené na obr. 39.3.9. Používateľ môže vybrať požadovaný materiál a priradiť ho k príslušnému objektu. Ak požadovaný materiál nie je k dispozícii v zozname, môže ho na stránke materiálov objektu načítať pomocou funkcie „Importovať materiál“ z súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti „Načítať z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Ak materiál nie je k dispozícii v knižnici DEFORM, môže ho používateľ vytvoriť pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Používateľ môže materiál zo zoznamu odstrániť pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) alebo údaje o materiáli upraviť pomocou ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Upravený alebo novo definovaný materiál je možné uložiť pomocou ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0009.jpg' | relative_url }})

Priradenie materiálu nástroja

### Generovanie siete nástrojov

Používateľ môže vytvoriť sieť pre nástroj definovaním údajov o relatívnej alebo absolútnej veľkosti ôk, ako je znázornené na obr. 39.3.10 a obr. 39.3.11. Po kliknutí na možnosť ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button.jpg' | relative_url }}) sa tiež zobrazí náhľad siete. Keďže informácie o reznom hrane sú súčasťou údajov o doštičke, sprievodca automaticky použije jemnejšiu sieť v blízkosti reznej zóny.

  
**Metóda relatívnej siete**

  * **Cieľový počet prvkov**: Počet prvkov, ktoré sa majú pre daný objekt vygenerovať, je možné určiť jednoduchým posunutím posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu.

  * **Pomer veľkostí:** Ide o pomer dĺžky hrany najväčšieho prvku k dĺžke hrany najmenšieho prvku.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0010.jpg' | relative_url }})

Vytvorenie siete pomocou relatívnej veľkosti ôk

  
**Metóda absolútnej siete**

**Minimálna veľkosť prvku**: Funkcia „Feed rate“ automaticky vypočíta minimálnu veľkosť prvkov siete, ktorá sa má vytvoriť, čím sa automaticky vypočíta hodnota „Počet prvkov“, ako je znázornené na obr. 39.3.11.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0011.jpg' | relative_url }})

Vytvorenie siete pomocou absolútnej veľkosti ok

### Nástroj BCC 

Na tejto stránke BCC môže používateľ definovať tepelné BCC, ako napríklad „Výmena tepla s okolím“ a „Teplota“. Predvolené BCC sa priradia automaticky po vytvorení siete, ako je znázornené na obr. 39.3.12.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0012.jpg' | relative_url }})

Predvolená hodnota výmeny tepla BCC

## Obrobok 

Na tejto stránke „Obrobok“ môže používateľ definovať typ objektu a nastaviť jeho počiatočnú teplotu. Predvolene je vybraný typ objektu „Plast“, ako je znázornené na obr. 39.3.13. Ak má používateľ záujem zohľadniť vplyv elastických vlastností, môže použiť typ objektu „Elastoplast“. Údaje o objekte môžeme tiež importovať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0013.jpg' | relative_url }})

Stránka obrobku

### Geometria obrobku 

Na tejto stránke „Geometria obrobku“ môže používateľ definovať geometriu obrobku pomocou funkcie ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Používateľ môže tiež importovať geometriu pomocou možností „Importovať geometriu“ ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. 39.3.14.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0014.jpg' | relative_url }})

Stránka „Geometria obrobku“

####   
Definovanie geometrie obrobku pomocou možnosti „Definovať primitív“

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) prejdeme na stránku „Workpiece Geo Primitive“. Na tejto stránke musí používateľ definovať geometrické parametre a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}), čím sa vygeneruje geometria, ako je znázornené na obr. 39.3.15. Na základe polohy nástroja musí používateľ definovať počiatočný uhol. Používateľ musí definovať „rotčný uhol“, aby sa pokryla doba trvania simulačného procesu. Obrobok sa vygeneruje na základe počiatočného uhla, rotčného uhla, priemeru frézy, posuvu a hĺbky rezu.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0015.jpg' | relative_url }})

Geometria frézovaného obrobku

### Výber materiálu obrobku

Na stránke materiálov sa zobrazujú všetky materiály pridané do zoznamu materiálov, ako je znázornené na obr. 39.3.16. Používateľ môže vybrať požadovaný materiál a priradiť ho k príslušnému objektu. Ak požadovaný materiál nie je k dispozícii v zozname, môže ho na stránke materiálov objektu načítať pomocou funkcie „Importovať materiál“ z súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti „Načítať z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Ak materiál nie je k dispozícii v knižnici DEFORM, môže ho používateľ vytvoriť pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Používateľ môže materiál zo zoznamu odstrániť pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) alebo údaje o materiáli upraviť pomocou ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Upravený alebo novo definovaný materiál je možné uložiť pomocou ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0016.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Vytvorenie siete obrobku

Používateľ môže vytvoriť sieť definovaním údajov o relatívnej alebo absolútnej veľkosti ôk, ako je znázornené na obr. 39.3.17 a obr. 39.3.18. Po kliknutí na možnosť ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button.jpg' | relative_url }}) sa tiež zobrazí náhľad siete.

  
**Metóda relatívnej siete:**

  * **Cieľový počet prvkov**: Počet prvkov, ktoré sa majú pre daný objekt vygenerovať, je možné určiť jednoduchým posunutím posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu.

  * **Pomer veľkostí**: Ide o pomer dĺžky hrany najväčšieho prvku k dĺžke hrany najmenšieho prvku.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0017.jpg' | relative_url }})

Vytvorenie siete obrobku s použitím relatívnej veľkosti ôk

  
**Metóda absolútnej siete:**

  * **Určenie veľkosti na základe percentuálneho podielu krmiva:** Na základe percentuálneho podielu krmiva sa automaticky vypočíta minimálna veľkosť ok siete.

  * **Minimálna veľkosť prvku:** Nastavuje minimálnu veľkosť prvku generovanej siete, ktorá sa vypočíta na základe percentuálnej hodnoty zadaného údaja.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0018.jpg' | relative_url }})

Vytvorenie siete obrobku s použitím absolútnej veľkosti ôk

### Obrobok BCC 

Na tejto stránke BCC môže používateľ definovať deformačné a tepelné parametre BCC (napr. rýchlosť, výmenu tepla s okolím a teplotu). Údaje BCC sa automaticky priradia po vytvorení siete, ako je znázornené na obr. 39.3.19 a obr. 39.3.20.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0019.jpg' | relative_url }})

Bola priradená predvolená rýchlosť BCC

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0020.jpg' | relative_url }})

Bola priradená predvolená hodnota BCC pre výmenu tepla

##  Ovládanie

Pomocou funkcie „Umiestnenie objektov“ je možné nástroj umiestniť na základe rýchlosti posuvu a polohy obrobku. K dispozícii sú rôzne možnosti umiestnenia objektov, ako je znázornené na obr. 39.3.21. Ďalšie informácie o týchto možnostiach nájdete v [16\. Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/).

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0021.jpg' | relative_url }})

Možnosti umiestnenia objektov

## Opotrebenie nástrojov

Používateľ môže aktivovať výpočet opotrebenia nástroja pomocou zaškrtávacieho políčka „**Definovať model na výpočet opotrebenia nástroja******“. Po zaškrtnutí tohto políčka môže používateľ vybrať model opotrebenia nástroja a definovať jeho parametre, ako je znázornené na obr. 39.3.22. Ďalšie informácie o týchto možnostiach nájdete v [20.4. Tool Wear](/docs/en/pre_processor/20_inter-object_data_definition/20_4_tool_wear/).

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0022.jpg' | relative_url }})

Stránka „Opotrebenie nástrojov“

## Kontakt

V predvolenom nastavení bude zaškrtnuté políčko „užívateľ“ a pre operáciu 3D rezania budú tiež definované predvolené vzťahy, ako je znázornené na obr. 39.3.23. Používateľ môže zmeniť hodnotu každého vzťahu tak, že ho vyberie a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Používateľ môže kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) na výpočet tolerancie kontaktu. Používateľ môže kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie vzťahu kontaktu. Používateľ môže zaškrtnúť políčko vedľa vzťahu kontaktu, aby definoval prilnavý kontakt.  
Ďalšie informácie nájdete v dokumente [20\. Inter-Object Relations](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0023.jpg' | relative_url }})

Stránka s kontaktnými údajmi

## Ovládanie krokov

Používateľ môže definovať údaje ovládacích prvkov krokov pomocou režimu s návodom (![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})), ako je znázornené na obr. 39.3.24. Ak chce používateľ využiť pokročilé nastavenia simulácie, môže prejsť do režimu Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), ako je znázornené na obr. 39.3.25. Ďalšie informácie a popis možností v nastaveniach simulácie nájdete v [9.Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/).

V režime s vedením môže používateľ nastaviť počet krokov, veľkosť kroku a spôsob riadenia veľkosti kroku. Používateľ môže nastaviť uhol oblúka, po dosiahnutí ktorého sa simulácia zastaví.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0024.jpg' | relative_url }})

Stránka s ovládacími prvkami krokov v režime s návodom

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0025.jpg' | relative_url }})

Stránka s ovládacími prvkami krokov v režime Expert

## Vytvoriť databázu

**Kontrola údajov** ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}): Týmto sa vykoná kontrola údajov. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však počas kontroly údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.  
  
**Vytvoriť databázu** ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}): Kliknutím na toto tlačidlo sa vygeneruje databáza pre inštaláciu (pozri obr. 39.3.26.).  
  
**Pridať súbor .key**: Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale stále sa vzťahujú na daný proces, je možné načítať ako súbor .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore .key, následne stačí zmeniť len tento súbor a simuláciu je možné odoslať znovu.

![]({{ '/assets/images/operation_templates/39_cutting/39_3_3d_milling/image0026.jpg' | relative_url }})

Vytvoriť stránku databázy

**Súvisiace témy:**

[39 Introduction to Cutting](/docs/en/operation_templates/39_cutting/39_introduction_to_cutting/)

[39.1. 2D Cutting](/docs/en/operation_templates/39_cutting/39_1_2d_cutting/)

[39.2. 3D Turning](/docs/en/operation_templates/39_cutting/39_2_3d_turning/)
