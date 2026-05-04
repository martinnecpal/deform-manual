---
lang: sk
title: "4.1. Hlavné rozloženie grafického rozhrania"
---

# 4.1. Hlavné rozloženie grafického rozhrania

4.1.1. Integrované grafické rozhranie (GUI Main)

  * Pre-Procesor

  * Simulátor

  * Postprocesor

4.1.2. Adresár problémov

  * Preskúmať kartu

  * Karta Čakanie v rade

  * Karta Nedávne

4.1.3 Sekcia problémových súborov

  * Karta Problémové súbory

  * Karta Všetky súbory

  * Ponuka kliknutia pravým tlačidlom myši pre problémové súbory

4.1.4. Panel s ponukami

  * Ponuka súborov

  * Upraviť

  * Zobraziť ponuku

  * Ponuka predbežného spracovania

  * Ponuka simulácie

  * Ponuka postprocesora

  * Ponuka nástrojov

  * Možnosti

  * Rozloženie

  * Pomoc

4.1.5. Náhľad

4.1.6. Správa

4.1.7. Záznam

4.1.8. Súhrn

4.1.9. Memo

## Integrované grafické rozhranie (GUI Main)

Integrované grafické rozhranie (GUI Main) v systéme DEFORM vedie používateľa tým, že poskytuje odkazy na rôzne komponenty DEFORM v rámci Pre-Processor, Simulator a Post-processor. V klasickom režime rozloženia má GUI main viacero sekcií, ako napríklad Adresár problémov, Súbory problémov, Náhľad a Zobrazenie informácií o súboroch (súbor s kľúčmi, protokol, správa, zhrnutie, poznámka a akýkoľvek textový súbor) a odkazy v kategóriách Pre-Processor (predspracovateľ), Simulator (simulátor) a Post-Processor (postprocesor), ako je znázornené na obr. 4.1.1. GUI Main (Hlavné grafické rozhranie) je veľmi intuitívne a používateľ môže použiť možnosti Layout (Rozloženie) na prispôsobenie zobrazenia GUI Main (Hlavné grafické rozhranie).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image001.jpg' | relative_url }})

GUI DEFORM Main

###
Pre-Procesor

Predprocesor na vytváranie, zostavovanie alebo úpravu údajov potrebných na analýzu simulácie a na generovanie požadovaného databázového súboru. Predprocesor DEFORM používa grafické používateľské rozhranie na zostavenie údajov potrebných na spustenie simulácie. Vstupné údaje zahŕňajú opis objektu, údaje o materiáli, vzťahy medzi objektmi, ovládacie prvky simulácie, údaje o materiáli atď. na nastavenie problému. V časti Pre-Processor (Predbežný procesor) sa nachádzajú odkazy, ktoré možno použiť na úpravu existujúceho nastavenia alebo vytvorenie nového nastavenia.

Pre-Processor zobrazuje odkazy na základe výberu súboru na karte "Problémové súbory". Napríklad,

  * Ak je vybraný súbor ".moproj" pozostávajúci z Extrusion, zobrazí sa odkaz na Sprievodcu extrudovaním

  * Ak je vybraný súbor DB, zobrazia sa odkazy na Integrovaný výrobný proces a NG Pre

  * Ak je vybraný súbor s kľúčom, zobrazia sa odkazy na NG Pre a Textový editor

  * Ak je vybraný prázdny priečinok, zobrazia sa odkazy na vytvorenie Nového problému a Nového priečinka.

###
Simulátor

Simulačný mechanizmus na vykonávanie numerických výpočtov potrebných na analýzu procesu a zápis výsledkov do databázového súboru. Simulačný mechanizmus načíta databázový súbor, vykoná aktuálny výpočet riešenia a pripojí príslušné údaje o riešení do databázového súboru. Simulačný motor tiež bezproblémovo spolupracuje so systémom automatického generovania siete (AMG), ktorý v prípade potreby generuje novú sieť MKP na obrobku. Počas behu simulačného motora sa do súborov správ (.MSG) a protokolov (.LOG) zapisujú informácie o stave vrátane prípadných chybových hlásení.

Pod simulátorom máme,
**Prevádzka** : Táto možnosť sa používa na okamžité spustenie simulácie.   
**Možnosti spustenia** : Táto možnosť sa používa na definovanie simulačného prostredia, ako je MPICH, simulačný server a jeho nastavenia, ukladanie súborov správ, počiatočný beh alebo pokračovanie predchádzajúceho behu atď. Ďalšie informácie nájdete v časti [simulator](/docs/sk/simulator/23_deform_simulator/23_introduction_to_deform_simulator/)
**Pridať do fronty** : Používateľ môže vybrať problém a kliknutím na tento štítok zaradiť problém do fronty na vybranom simulačnom serveri.
Pokračujte: Táto možnosť sa používa na pokračovanie v probléme, ktorý bol predčasne zastavený.  
**Monitor procesov** : Monitor procesov sa používa na zistenie aktuálneho stavu rôznych problémov, ktoré sa majú predložiť na simuláciu v tomto systéme alebo týmto systémom, Viac informácií nájdete v časti [simulator](/docs/sk/simulator/23_deform_simulator/23_introduction_to_deform_simulator/).  
**Simulačná grafika** : Túto možnosť možno použiť na spustenie nezávislého prehliadača "DEFORM Viewer" na monitorovanie aktuálnych problémov, ktoré sa simulujú.

###
Postprocesor

Postprocesor na čítanie databázového súboru zo simulačného stroja a grafické zobrazenie výsledkov a na extrakciu numerických údajov. Postprocesor sa používa na zobrazenie simulačných údajov po spustení simulácie. Postprocesor obsahuje grafické používateľské rozhranie na zobrazenie geometrie, údajov o poli, ako je deformácia, teplota a napätie, a ďalších simulačných údajov, ako je zaťaženie matrice. Postprocesor možno použiť aj na extrakciu grafických alebo číselných údajov na použitie v iných aplikáciách.

V časti Post-Processor nájdete odkazy na Next Gen Post-Processor, DEFORM Viewer a Material Suite. Ak priečinok Problem (Problém) pozostáva zo štúdie DOE/ Optimization (Optimalizácia), zobrazí sa prepojenie na DOE Post-Processor (Postprocesor DOE).

## Adresár problémov

Sekcia Adresár problémov obsahuje karty Prieskumník, Čakanie a Posledné, ako je znázornené na obr. 4.1.2.  
![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) **Prehľadávať** : Pomocou možnosti Browse (Prehľadávať) môže používateľ pripojiť vybraný priečinok ako problémový priečinok na karte Explorer (Prieskumník). Používateľ môže tiež pridať viac problémových priečinkov na karte Prieskumník.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image002.jpg' | relative_url }})

Preskúmať kartu

###
  
Preskúmať kartu

Na karte Preskúmať, ako je znázornené na obr. 4.1.2, sa zobrazí zoznam priečinkov vo vybranom adresári.   
**Montáž priečinka** : Používateľ môže pripojiť ľubovoľný priečinok ako "problémový priečinok", aby tak urobil, môže kliknúť na tlačidlo "Prehľadávať priečinok" a v dialógovom okne "Prehľadávať" zaškrtnúť políčko "Pripojiť ako problémový priečinok". Namontovaný priečinok možno odmontovať pomocou RMB na namontovanom priečinku a výberom možnosti "Unmount problem folder" (Odmontujte problémový priečinok) (pozri obr. 4.1.3.).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image003.jpg' | relative_url }})

Ponuka kliknutia pravým tlačidlom myši pre priečinok Mounted Problem

**Nastaviť ako umiestnenie na prehliadanie** : Používateľ môže vybrať ľubovoľný priečinok a nastaviť ho ako umiestnenie na prehliadanie pomocou RMB na priečinku a výberom možnosti "Nastaviť ako umiestnenie na prehliadanie".  
**Zobraziť v Prieskumníkovi** : Používateľ môže vybrať "Zobraziť v Prieskumníkovi" z RMB na priečinku, aby sa priečinok a jeho obsah zobrazil v Prieskumníkovi okien.  
**Kópia** : Používateľ môže pomocou tejto možnosti skopírovať priečinok a vložiť ho do ľubovoľného priečinka na karte Prieskumník.   
**Duplikát** : Používateľ môže použiť túto možnosť z RMB na priečinok, aby ho duplikoval, priečinok sa duplikuje s novým názvom na rovnakom mieste ako zdrojový adresár.   
**Delete**![]({{ '/assets/icons/pre_icons/mo_delete_folder_icon.jpg' | relative_url }}) : Používateľ môže odstrániť priečinok zo systému pomocou tejto možnosti z možností RMB na priečinku.  
**Názov(F2)** : Názov priečinka možno premenovať pomocou tejto možnosti z možností RMB alebo klávesom F2 na priečinku.  
**Archív databázy** : Dialógové okno "Archív databázy" možno spustiť na archiváciu projektov vo vybranom priečinku, viac informácií o "Archíve databázy" nájdete v [Database Archive](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_4_main_menu.htm#Database_Archive) in**** kapitola 6.4. Hlavná ponuka
**Upratovanie súborov** : Táto možnosť z možností RMB sa používa na vyčistenie dočasných súborov vytvorených programom DEFORM počas nastavovania problému alebo simulácie.
**Vyčistiť stav chodu** : Ak je simulácia zastavená alebo ukončená používateľom a zostane zachovaný stav behu, potom je možné použiť túto možnosť RMB na vyčistenie stavu behu.  
**Projekt sťahovania** : Priečinok projektu môžeme presunúť z jedného adresára do iného adresára pretiahnutím, ako je znázornené na obr. 4.1.4.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image004.jpg' | relative_url }})

Presúvanie projektu pomocou funkcie ťahaj a pusť

###
Karta Čakanie vo fronte

Na karte Queued, ako je znázornené na obr. 4.1.5, sa zobrazuje zoznam úloh pridaných do frontu na simuláciu z daného systému spolu so stavom úloh zaradených do frontu.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image005.jpg' | relative_url }})

Karta Čakanie vo fronte

###
Karta Nedávne

Na karte Recent (Posledné), ako je znázornené na obr. 4.1.6, sa zobrazuje zoznam naposledy otvorených adresárov databázy.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image006.jpg' | relative_url }})

Nedávna karta

## Sekcia problémových súborov

V časti Problémové súbory sú karty "Problémové súbory" a "Všetky súbory". Na karte "Problémové súbory" sa zobrazujú súbory, ktoré možno použiť na prepojenie modulov DEFORM vo vybranom priečinku, a na karte "Všetky súbory" sa zobrazujú všetky súbory a priečinky vo vybranom priečinku.

###
Karta Problémové súbory

Na karte Problémové súbory, ako je znázornené na obr. 4.1.7, sú zobrazené súbory .DB, .KEY a Project.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image007.jpg' | relative_url }})

Karta Problémové súbory

### Karta Všetky súbory

Na karte All Files (Všetky súbory), ako je znázornené na obr. 4.1.8, sú zobrazené všetky súbory a priečinky dostupné v priečinku projektu. V záložke "Všetky súbory" má používateľ k dispozícii možnosť Filter (Filtrovanie) na filtrovanie súborov na základe prípony súboru pre jednoduchšie zobrazenie, pozri obr. 4.1.9. .

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image008.jpg' | relative_url }})

Karta Všetky súbory

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image009.jpg' | relative_url }})

Možnosť filtrovania súborov na karte Všetky súbory

###
  
Ponuka kliknutia pravým tlačidlom myši pre problémové súbory

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image010.jpg' | relative_url }})

Ponuka kliknutia pravým tlačidlom myši pre problémové súbory

**Duplikát** : Pomocou možnosti Duplikovať môžeme vytvoriť duplicitnú kópiu súboru alebo priečinka s novým názvom v zdrojovom priečinku.  
**Delete**![]({{ '/assets/icons/pre_icons/mo_delete_folder_icon.jpg' | relative_url }}) : Používateľ môže odstrániť priečinok alebo súbor zo systému pomocou tejto možnosti z možností RMB na priečinku.  
**Názov(F2)** : Názov priečinka alebo súboru možno premenovať pomocou tejto možnosti z možností RMB alebo klávesom F2 na priečinku.  
**Upraviť pomocou Edito****r** : Táto možnosť sa vzťahuje len na súbor s kľúčom. Pomocou tejto možnosti môže používateľ otvoriť súbor v textovom editore a zobraziť jeho obsah alebo ho upraviť.

## Panel ponuky

V rôznych ponukách grafického rozhrania Main je k dispozícii niekoľko možností na prístup k priečinkom projektu, navigáciu medzi priečinkami a odkazy na rôzne moduly. Všetky možnosti menu sú sprístupnené pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_menu_bar_icon.jpg' | relative_url }}) dostupnej v GUI Main, pozri obr. 4.1.11.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image011.jpg' | relative_url }})

Vyskakovacie menu

### Menu súborov

Na nasledujúcom obr. 4.1.12. sú zobrazené možnosti v ponuke File (Súbor) v hlavnom grafickom rozhraní.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image012.jpg' | relative_url }})

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image013.jpg' | relative_url }})

Možnosti ponuky Súbor

  
  
**Nový problém![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) : **Užívateľ môže vytvoriť nový problém buď výberom **![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }})** Nový problém. Možnosť vytvorenia New Problem (Nový problém) je dostupná z ponuky súborov, z panela nástrojov, z odkazov v rámci možností Folder (Priečinok) a RMB na prázdnom priečinku.  
Keď používateľ klikne na New problem (Nový problém), zobrazí sa okno New Problem (Nový problém), ako je znázornené na obr. 4.1.13).

**Vytvoriť nový** : Používateľ môže použiť "Create New" (Vytvoriť nový) na začatie nového nastavenia problému pomocou jedného z modulov DEFORM. Dialógové okno New Problem (Nový problém) zobrazí zoznamy modulov dostupných v programe DEFORM, keď používateľ vyberie možnosť "Create New" (Vytvoriť nový), potom môže vybrať sprievodcu, ako napríklad 2D3D Pre / Integrated Manufacturing Proc. (2D3D Pre / Integrovaný výrobný postup) alebo akúkoľvek šablónu a systém jednotiek pre nový problém. Používateľ môže určiť umiestnenie problému v systéme v poli Location (Umiestnenie) a definovať názov problému v poli Name (Názov) a kliknúť na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image014.jpg' | relative_url }})

Nový problém - Vytvoriť novú kategóriu

**Import šablóny** : Používateľ môže začať nové nastavenie problému pomocou uložených Šablón definovaných používateľom (pozri obr. 4.1.14.). Umiestnenie šablón možno prehliadať a požadovanú šablónu možno vybrať. Používateľ môže v poli Location (Umiestnenie) určiť umiestnenie problému v systéme a v poli Name (Názov) definovať názov problému a kliknúť na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Otvorí sa nový projekt spolu s údajmi zo šablóny definovanej používateľom.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image015.jpg' | relative_url }})

Nový problém - kategória Import šablóny

**Príklad importu** : Používateľ môže začať nový problém skopírovaním údajov z jedného z kľúčových súborov Príklad do priečinka Projekt (pozri obr. 4.1.15.). Ak používateľ začiarkne políčko Open Pre-processor (Otvoriť preprocesor) a klikne na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), potom sa vybraný príklad skopíruje do priečinka projektu a otvorí sa v 2D/3D preprocesore.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image016.jpg' | relative_url }})

Nový problém - Importovať kategóriu Príklad

  
**Nový priečinok** ![]({{ '/assets/icons/pre_icons/mo_new_folder_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ vytvoriť nový podpriečinok vo vybranom priečinku.  
**Ukončenie (Ctrl +Q)** ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}): Možnosť ukončenia sa používa na ukončenie hlavného grafického rozhrania DEFORM.

### Upraviť

Na nasledujúcom obr. 4.1.16. sú zobrazené možnosti ponuky Edit v grafickom používateľskom rozhraní.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image017.jpg' | relative_url }})

Možnosť Upraviť menu

**Copy![]({{ '/assets/icons/pre_icons/mo_copy_file_icon.jpg' | relative_url }})** : Pomocou tejto možnosti môže používateľ skopírovať vybraný projekt.  
**Vložiť![]({{ '/assets/icons/pre_icons/mo_paste_file_icon.jpg' | relative_url }})** : Pomocou tejto možnosti môže používateľ skopírovaný projekt vložiť do vybraného problémového priečinka.

###
Zobraziť menu

Na nasledujúcom obrázku 4.1.17. sú zobrazené možnosti ponuky View (Zobraziť) v grafickom používateľskom rozhraní.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image018.jpg' | relative_url }})

Možnosť Zobraziť ponuku

  
  
**Pás s nástrojmi:** Používateľ môže ovládať zobrazenie panelov s nástrojmi začiarknutím a zrušením začiarknutia v časti Panel s nástrojmi, ako je znázornené na obr. 4.1.18.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image019.jpg' | relative_url }})

Možnosť panela nástrojov

**Standard** : Používateľovi sa na paneli s ponukami zobrazia niektoré štandardné možnosti (Nový problém, Prehľadávať priečinok, Späť, Dopredu, ...atď.). Ikony na paneli nástrojov sa aktualizujú na základe vybraného priečinka a typu projektu v ňom.  
**Rozloženie** : Používateľ bude mať k dispozícii prepínacie tlačidlá na ovládanie zobrazenia rôznych sekcií v GUI Main alebo na zmenu rozloženia, ako je znázornené na obr. 4.1.19. Na paneli nástrojov Layout (Rozloženie) sa nachádzajú rôzne možnosti,

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image020.jpg' | relative_url }})

Možnosti rozloženia

**Prepínač priečinkov![]({{ '/assets/icons/pre_icons/mo_toggle_folder_button.jpg' | relative_url }})** : Toto tlačidlo sa používa na zobrazenie/skrytie primárneho adresára na displeji.  
**Prepínač súborov** ![]({{ '/assets/icons/pre_icons/mo_toggle_file_icon.jpg' | relative_url }}): Toto tlačidlo sa používa na zobrazenie/skrytie okna súborov.  
**Prepínač Vlastnosti** ![]({{ '/assets/icons/pre_icons/mo_toggle_properties_icon.jpg' | relative_url }}) : Toto tlačidlo sa používa na aktiváciu zobrazenia okna Vlastnosti.  
**Prepínač Akcie** ![]({{ '/assets/icons/pre_icons/mo_toggle_action_icon.jpg' | relative_url }}): Toto tlačidlo sa používa na aktiváciu zobrazenia okna Akcie.  
**Nie rozdeliť** ![]({{ '/assets/icons/pre_icons/mo_no_split_icon.jpg' | relative_url }}): Toto tlačidlo sa nepoužíva na rozdelenie kariet Náhľad a Správa.  
**Delenie vľavo vpravo** ![]({{ '/assets/icons/pre_icons/mo_left_right_split_icon.jpg' | relative_url }}): Toto tlačidlo sa používa na rozdelenie kariet Náhľad a Správa vľavo a vpravo.  
**Rozdelenie nahor a nadol** ![]({{ '/assets/icons/pre_icons/mo_up_down_icon.jpg' | relative_url }}): Toto tlačidlo sa používa na rozdelenie kariet Náhľad a Správa nahor a nadol.  
**Predvoľby rozloženia** ![]({{ '/assets/icons/pre_icons/mo_layout_preferences_icon.jpg' | relative_url }}): Toto tlačidlo slúži na otvorenie okna predvolieb rozloženia.

**Stavový riadok** : Používateľ môže skryť a zobraziť stavový riadok zrušením začiarknutia a začiarknutím tejto možnosti v ponuke zobrazenia.  
**Domov![]({{ '/assets/icons/pre_icons/mo_home_icon.jpg' | relative_url }})** : Pomocou tejto možnosti môže používateľ prejsť do adresára Home, ako je uvedené v nastaveniach prostredia.  
**Back****(Ctrl +B)![]({{ '/assets/icons/pre_icons/mo_back_icon.jpg' | relative_url }})** : Táto možnosť sa používa na navigáciu späť na predtým zvolenú cestu na karte Prieskumník.  
**Prechod dopredu (Ctrl +F)** ![]({{ '/assets/icons/pre_icons/mo_forward_icon.jpg' | relative_url }}): Táto možnosť sa používa na prechod na problémovú cestu na karte Prieskumník pred použitím možnosti "Späť".   
**Nahor (Ctrl +U)** ![]({{ '/assets/icons/pre_icons/mo_up_arrow_iocn.jpg' | relative_url }}): Táto možnosť sa používa na prechod na jednu úroveň nad aktuálne vybraný adresár na karte Prieskumník.  
**Obnoviť (F5)** : Táto možnosť sa používa na obnovenie hlavného grafického rozhrania.   
**Scan Subdirectory** ![]({{ '/assets/icons/pre_icons/mo_scan_subdirectory_button.jpg' | relative_url }}): Táto možnosť sa používa na zobrazenie obrazových súborov každého problému v aktuálne vybranom adresári problému. Používateľ môže otvoriť príslušný priečinok s problémami dvojitým kliknutím na súbor s obrázkom.

Po kliknutí pravým tlačidlom myši na zónu obrazového súboru je k dispozícii možnosť **Preskenovať problémy**, ktorá sa používa na opätovné skenovanie príslušného adresára s problémami a obnovenie zoznamu problémov, ako je znázornené na obr. 4.1.20.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image021.jpg' | relative_url }})

Preskúmanie problémov

### Ponuka predbežného procesora

Na nasledujúcom obrázku 4.1.21. sú zobrazené možnosti ponuky Pre-Processor, ktoré sú k dispozícii na paneli ponúk aj v okne prepínacích akcií v časti Pre-Processor. Možnosti zobrazené v časti "Pre-Processor" závisia od vybraného priečinka a typu projektu v ňom. Ak je napríklad vybraný projekt Forming express (Tvarovanie expres), potom sa používateľovi zobrazia možnosti Forming express operation (Tvarovanie expres), Integrated Manufacturing Proc. (Integrované výrobné postupy) a 2D/3D Pre.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image022.jpg' | relative_url }})

Možnosť ponuky Pre-Processor

###
Ponuka simulácie

Na nasledujúcom obr. 4.1.22. sú zobrazené možnosti ponuky simulácie, ktoré sú k dispozícii na paneli ponúk aj v okne prepínania akcií v časti Simulátor. V závislosti od vybraného priečinka projektu alebo prázdneho priečinka sa aktualizujú možnosti simulátora.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image023.jpg' | relative_url }})

Možnosť ponuky Simulátor

**Run** ![]({{ '/assets/icons/simulator_icons/mo_run_icon.jpg' | relative_url }}): Táto možnosť sa používa na spustenie úlohy
**Run (options)** ![]({{ '/assets/icons/simulator_icons/run_option_icon.jpg' | relative_url }}): Táto možnosť sa používa na otvorenie vyskakovacieho okna Run option (Spustiť) pre podrobnejšie nastavenia simulácie vybraného projektu.  
**Pridať do frontu** ![]({{ '/assets/icons/simulator_icons/mo_add_to_queue_icon.jpg' | relative_url }}): Používa sa na pridanie vybraných úloh do frontu na simuláciu.  
**Stop**![]({{ '/assets/icons/simulator_icons/mo_stop_icon.jpg' | relative_url }}) : Táto možnosť sa používa na zastavenie vybranej úlohy, ktorá sa simuluje.  
**Pokračovať** ![]({{ '/assets/icons/simulator_icons/mo_continue_icon.jpg' | relative_url }}): Táto možnosť sa používa na pokračovanie úlohy, ktorá bola predčasne zastavená.  
**Monitor procesov**![]({{ '/assets/icons/simulator_icons/mo_process_monitor_icon.jpg' | relative_url }}) : Monitor procesov zobrazuje stav všetkých simulácií spustených na CPU.  
**Simulačná grafika** ![]({{ '/assets/icons/simulator_icons/mo_simulation_graphics_icon.jpg' | relative_url }}): Táto možnosť sa používa na monitorovanie problému simulácie.

Ďalšie informácie o týchto možnostiach nájdete v časti [Chapter 23. DEFORM Simulator](/docs/sk/simulator/23_deform_simulator/23_introduction_to_deform_simulator/).

###
Ponuka postprocesora

Na nasledujúcom obrázku 4.1.23. sú zobrazené možnosti ponuky Post Processor, ktoré sú k dispozícii na paneli ponúk aj v okne prepínania akcií v časti Post Processor v závislosti od vybraného priečinka projektu a projektu v ňom. Ak vybraný priečinok obsahuje projekt DOE alebo Optimization (Optimalizácia) v rámci neho, sprístupní sa modul DOE Post Processor (Postavenie DOE).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image024.jpg' | relative_url }})

Možnosť ponuky Post Processor

  
**2D/3D post:** Táto možnosť sa používa na otvorenie Next gen Post, viac informácií nájdete v [Post-Poocessor](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/).  
**DOE Post** : Táto možnosť sa používa na otvorenie DOE Post, viac informácií nájdete v [DOE Post processor](/docs/sk/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/).  
**DEFORM Viewer** : Táto možnosť sa používa na otvorenie prehliadača deformácií, viac informácií nájdete v časti DEFORM Viewer.  
**Súbor materiálov:** Táto možnosť sa používa na otvorenie súboru materiálov, viac informácií nájdete v časti Súbor materiálov.

###
Ponuka nástrojov

Na nasledujúcom obr. 4.1.24. sú zobrazené možnosti v ponuke Tools (Nástroje) v hlavnom grafickom rozhraní.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image025.jpg' | relative_url }})

Možnosť ponuky nástrojov

  
**Správca databázy![]({{ '/assets/icons/pre_icons/mo_database_manager_icon.jpg' | relative_url }})**
Database Manager pomáha používateľovi spravovať veľkosť databázy. V správcovi DB môžeme vykonávať operácie Purge (vyčistiť), Merge (zlúčiť) a Convert (konvertovať).

**Purge** : Vyčistenie možno použiť na zmenšenie veľkosti DB odstránením nerelevantných uložených krokov. Ak chcete databázu prečistiť, používateľ musí vybrať požadované kroky zo zoznamu krokov vybranej databázy![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Kliknite na záložku Purge (Prečistiť)![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Do políčka " To " ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) zadajte umiestnenie a názov, kam chcete prečistenú databázu uložiť, a potom kliknite na " Save Selected Steps (Uložiť vybrané kroky) ", ako je znázornené na obr. 4.1.25.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image026.jpg' | relative_url }})

Okno Vyčistiť databázu

**Zlúčenie** : Možnosť slúži na zlúčenie dvoch databáz do jednej databázy. Na zlúčenie databázy vyberte súbory .DB, ktoré sa majú zlúčiť, v poli "Database 1" (Databáza 1) a "Database 2" (Databáza 2) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Do poľa "To" (Do) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) zadajte nové umiestnenie a názov nového súboru DB a potom kliknite na tlačidlo "Start Merging" (Spustiť zlúčenie), ako je znázornené na obr. 4.1.26.

Poznámka:
Na zlúčenie by mala mať databáza rovnaké číslo oka a číslo kroku by malo pokračovať.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image027.jpg' | relative_url }})

Okno Zlúčenie databázy

**Konvertovať** : Táto možnosť sa používa na prevod staršej verzie databázy na novšiu verziu. Ak chcete konvertovať, vyberte staršiu verziu databázy ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Do poľa "To" (Do) zadajte nové umiestnenie a názov nového súboru DB ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})a potom kliknite na tlačidlo "Start Converting" (Spustiť konverziu) na karte konvertovania, ako je znázornené na obr. 4.1.27.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image028.jpg' | relative_url }})

Previesť okno

**Archív databázy**
Táto funkcia sa používa na zmenšenie dokončeného projektu na veľkosť, ktorá sa zmestí na archívne médium (napríklad DVD) na zálohovanie alebo distribúciu, pozri obr. 4.1.28. Táto možnosť je k dispozícii aj v ponuke RMB priečinka. Používateľ môže nastaviť "Destination (Cieľ)" a "Options (Možnosti)" a kliknutím na "Archive (Archivovať)" spustiť archiváciu.  
V záložke "Cieľ" môže používateľ zadať umiestnenie v systéme do poľa "Umiestnenie" a názov archívu do poľa "Názov archívu".

Táto možnosť sa používa na archiváciu projektových súborov, projektových databáz a databáz DOE/OPT zaškrtnutím príslušných políčok.

**No Purge** : Pomocou tejto možnosti môže používateľ archivovať databázu bez čistenia databázy.

**Uložiť prvý/posledný krok** : Používateľ môže archivovať databázu vyčistením databázy a zachovaním len prvého a posledného kroku databázy.

**Uloženie krokov začiatku/konca operácie** : Používateľ môže archivovať databázu vyčistením databázy a zachovaním iba počiatočného a koncového kroku operácie.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image029.jpg' | relative_url }})

Archív databázy

  
**Upratovanie súborov![]({{ '/assets/icons/pre_icons/mo_clean_up_files_icon.jpg' | relative_url }})**

Používa sa na odstránenie dočasných súborov v problémovom adresári, ktoré boli vytvorené počas simulácie.

**Čistenie stavu behu![]({{ '/assets/icons/pre_icons/mo_clean_up_running_status_icon.jpg' | relative_url }})**
Používa sa na odstránenie súborov so stavom behu v adresári s problémami, ak sa súbor so stavom behu zachoval.

### Možnosti

Používateľ môže nastaviť pracovné prostredie DEFORM pomocou možnosti prostredia. Tu môže používateľ vykonať zmeny v zobrazovaní a grafických nastaveniach a môže si ich uložiť podľa svojho pohodlia (pozri obr. 4.1.29).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image030.jpg' | relative_url }})

Ponuka možností

**Prostredie** : Používateľ môže nastaviť pracovné prostredie DEFORM pomocou možnosti prostredia. Tu môže používateľ vykonať zmeny v zobrazovaní a grafických nastaveniach a môže si tieto nastavenia uložiť podľa svojho pohodlia. Nastavenia sa budú aktualizovať od nasledujúcej relácie.  
****

  * Región:

Používateľ môže vybrať preferovaný jazyk v položke Language (Jazyk) a nastaviť anglický jazyk alebo jednotky SI v položke Unit (Jednotka) ako predvolený systém jednotiek pre nový problém. Používateľ môže vybrať normy pre materiály v položke Material Library (Knižnica materiálov), ktoré sa majú použiť ako predvolené pre import materiálov v probléme. (Pozri obr. 4.1.30.).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image024.jpg' | relative_url }})

Možnosti regiónu v okne Nastavenia prostredia

  * Typ používateľa:

V okne Nastavenia prostredia sa zobrazí možnosť Typ používateľa, ako je znázornené na obr. 4.1.31. V závislosti od typu používateľa sa aktivujú predvolené podmienky a vyskakovacie okná.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image025.jpg' | relative_url }})

Možnosti typu používateľa v okne Nastavenia prostredia

  * **Novice** : Ak je používateľ v programe DEFORM nový, uprednostňuje sa táto možnosť.
  * I** stredne pokročilý** : Táto možnosť je určená pre používateľa, ktorý je trochu oboznámený s prostredím DEFORM. Ak napríklad v grafickom používateľskom rozhraní vyberieme možnosť quit (ukončiť), zobrazí sa vyskakovacie okno so správou " Do you want to quit (Chcete ukončiť)" (Chcete ukončiť), používateľ môže kliknúť na tlačidlo "Yes (Áno)" (Ukončiť), aby opustil grafické používateľské rozhranie.
  * **Pokročilé:** Táto možnosť je určená pre používateľa, ktorý dobre pozná DEFORM, môže odstrániť niekoľko vyskakovacích okien. Ak napríklad v grafickom používateľskom rozhraní vyberieme možnosť quit (Ukončiť), program DEFORM sa zatvorí bez vyskakovacieho varovného hlásenia.

  * Adresár používateľov:

V okne Nastavenia prostredia sa zobrazí možnosť Adresár používateľov, ako je znázornené na obr. 4.1.32. Používateľ môže vyhľadať požadované umiestnenie a nastaviť ho ako pracovný adresár v časti Problem (Problém), tento adresár sa bude používať ako predvolené umiestnenie na ukladanie vygenerovaných DB, kľúčových súborov a pracovných súborov súvisiacich s DEFORM. Cesta v položke Library root (Knižničný koreň) sa použije ako predvolená cesta na uloženie používateľských údajov vygenerovaných v programe DEFORM. cesta v položke Geometry import (Import geometrie) sa použije ako predvolená cesta na prístup ku geometriám, čo môže byť samotný adresár Problem (Problém). Ak ide o iné umiestnenie, musí byť uvedené pod cestou importu geometrie samostatne pre 2D a 3D. Dočasné súbory vytvorené pri spustení deformácie sa nachádzajú v uvedenej ceste v položke Temporary Directory (Dočasný adresár).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image026.jpg' | relative_url }})

Možnosti používateľského adresára v okne Nastavenia prostredia

  * Systémový adresár:

V okne Nastavenia prostredia sa zobrazí možnosť Systémový adresár, ako je znázornené na obr. 4.1.33. Prístup k tejto karte používateľovi aktivuje iba výber Advanced user type (ako je uvedené v časti User type). Pomocou tejto možnosti môže používateľ zmeniť cestu ku knižnici materiálov, lisov a zariadení DEFORM v príslušných poliach, tento adresár sa bude používať ako predvolené umiestnenie pre knižnicu materiálov, lisov a zariadení v programe DEFORM. V predvolenom nastavení sú tieto adresáre nasmerované na knižnicu DEFORM dostupnú v mieste inštalácie, používateľ ich môže zmeniť na používateľské cesty ku knižniciam, táto cesta bude vyvolaná pri výbere importu materiálu, pohybu alebo vloženia geometrie z grafického rozhrania DEFORM.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image048.jpg' | relative_url }})

Možnosti systémových adresárov v okne Nastavenia prostredia

  * Možnosť simulácie:

V programe DEFORM - V12 možno predvolené nastavenia na spustenie simulácie nastaviť pomocou možností na karte Simulation Option v nastaveniach prostredia. Zobrazí sa okno Simulation Options (Možnosti simulácie), ako je znázornené na obr. 4.1.34. Zapnutím možnosti Keep Message Files (Uchovávať súbory správ) DEFORM ukladá simulačné správy bez prepisovania aj po opätovnom premietnutí. Používateľ môže zapnúť Parallel meshing (Paralelné sieťovanie) a nastaviť ho ako predvolené pre všetky simulácie, používateľ môže aplikovať paralelné sieťovanie buď na Solid (Teleso), alebo na obidva Solid+Surface (Teleso+Povrch). Používateľ môže zapnúť No automatic remeshing (Žiadne automatické remeshovanie) ako predvolené nastavenie pre simulácie, aby simulácia mohla preskočiť automatické remeshovanie z dôvodu nekonvergencie. Predvolené nastavenia možno zmeniť pre každú simuláciu v dialógovom okne Run options (Možnosti spustenia).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image027.jpg' | relative_url }})

Možnosti simulácie

  * Viacnásobný procesor:

V okne Nastavenia prostredia sa zobrazí možnosť Viacero procesorov, ako je znázornené na obr. 4.1.35. Používateľ môže aktivovať tabuľku len zaškrtnutím vedľa možnosti Použiť viacero procesorov, ako je znázornené na obr. 4.1.35. Používateľ môže určiť počítače použité na riešenie problému, ako aj počet procesorov použitých na každom počítači. Pre spustenie simulácie je veľmi dôležité, aby používateľ zadal správny sieťový názov počítača. Poskytuje aj informácie o pamäti zdieľanej medzi procesormi.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image028.jpg' | relative_url }})

Viacnásobný procesor

  * Proces:

V okne Nastavenia prostredia sa zobrazí možnosť Proces, ako je znázornené na obr. 4.1.36. Používateľ môže nastaviť predvolené režimy simulácie, ako je Deformácia, Transformácia prenosu tepla... atď. a ovládať automatické priradenie primárnej matrice.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image029.jpg' | relative_url }})

Možnosti procesu v okne Nastavenia prostredia

  * Ovládanie výstupu:

Používateľ môže nastaviť predvolený typ výstupu ako Elemental alebo Elemental+Node pre premenné Strain, Stress a Damage, ako je znázornené na obr. 4.1.37.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image030.jpg' | relative_url }})

Možnosti Output Controls v okne Nastavenia prostredia

  * E-mail

V okne Nastavenia prostredia sa zobrazí možnosť E-mail, ako je znázornené na obr. 4.1.38. Táto funkcia umožňuje programu DEFORM odoslať e-mailové oznámenie na začiatku simulácie a s poslednými 25 riadkami zo súboru správ a súboru protokolu na konci simulácie. E-maily sa odosielajú prostredníctvom protokolu SMTP s použitím protokolu StartTLS (alebo bez zabezpečenia). Ďalšie informácie nájdete v časti [23.7. Email notification of the simulation](/docs/sk/simulator/23_deform_simulator/23_7_email_the_results/).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image031.jpg' | relative_url }})

Možnosti e-mailu v okne Nastavenia prostredia

  * Pamäť:

Používateľ môže nastaviť požadovanú veľkosť pamäte v závislosti od použitia, ako je znázornené na obr. 4.1.39. Z väčšej časti môžu predvolené hodnoty týchto nastavení pokryť široký rozsah požiadaviek modelu. V prípade veľmi veľkých modelov (vzhľadom na celkový počet prvkov a uzlov) môže byť potrebné tieto nastavenia zvýšiť v závislosti od operačného systému, aby sa zvládli niektoré postupy počas behu, ako je napríklad remeshing.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image032.jpg' | relative_url }})

Možnosti pamäte v okne Nastavenia prostredia

  * Ikona/šablóna:

Používateľ môže zmeniť ikonu a veľkosť písma v závislosti od požiadavky, ako je znázornené v [Fig. 4.1.40.](4_1_gui_main_layout.htm#Fig_4_1_40_Icon/Font_options_under_Environment_Settings_window)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image033.jpg' | relative_url }})

Možnosti ikony/písma v okne Nastavenia prostredia

  * Ochrana pracovných miest:

Používateľ môže chrániť úlohu Running pred ukončením nastavením hesla, ako je znázornené na obr. 4.1.41.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image034.jpg' | relative_url }})

Možnosti ochrany práce v okne Nastavenia prostredia

  
V systéme Linux vyberte prepínač Povoliť ochranu, potom zadajte heslo do poľa Heslo a kliknite na tlačidlo Uložiť, aby sa heslo uložilo (pozri obr. 4.1.41.).

V systéme Windows vyberte tlačidlo Pokračovať, potom použite heslo vo vyskakovacom okne nastavenia hesla úlohy a kliknite naň, ako je znázornené na obr. 4.1.42.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image035.jpg' | relative_url }})

Spustenie ochrany úloh v okne nastavenia hesla systému Windows

  * Správa:

Z V12 Možnosti automatického generovania hlásení sú k dispozícii v položke Report (Hlásenie) v okne Environment Settings (Nastavenia prostredia), zobrazia sa nastavenia automatického generovania hlásení, ako je znázornené na obr. 4.1.43. Používateľ môže nastaviť predvolenú možnosť Auto Report (Automatické vytváranie správ) podľa požiadaviek pre Normal run (Normálny beh), DOE run (Beh DOE) a OPT run (Beh OPT) zapnutím zaškrtávacieho políčka. V závislosti od nastavení DEFORM automaticky vygeneruje správu na konci simulácie.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image036.jpg' | relative_url }})

Možnosti hlásenia v okne Nastavenia prostredia

### Rozloženie

Používateľ môže zmeniť rozloženie grafického rozhrania pomocou možnosti Layout scheme (pozri obr. 4.1.44).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image031.jpg' | relative_url }})

Stránka s predvoľbami rozloženia

**Klasický**

****Toto rozloženie je ako hlavné rozloženie GUI verzie DEFORM v11.X (pozri obr. 4.1.1.).

  
**Express**

Rozloženie ****Express je znázornené na obr. 4.1.45. Toto rozloženie je zjednodušené rozloženie. Používateľ môže v rozložení Express otvoriť viacero kariet na sledovanie rôznych projektov pomocou možnosti "Browse in New tab" (Prechádzať v novej karte) z možností RMB na priečinku, ako je znázornené na obr. 4.1.46. Pridané okno Nová karta, ako je znázornené na obr. 4.1.47.

**Vlastnosti** : V tomto okne sa zobrazujú údaje problémového priečinka, ktorý je vybraný na karte Prieskumník. Z tohto okna vlastností môžeme tiež vytvoriť súbor MEMO v priečinku projektu, ako je znázornené na obr. 4.1.48.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image032.jpg' | relative_url }})

Expresné rozloženie

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image033.jpg' | relative_url }})

Výber možnosti Prehľadávať na novej karte v ponuke pravého tlačidla myši

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image034.jpg' | relative_url }})

Otvorenie viacerých kariet v grafickom rozhraní Express layout Main

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image035.jpg' | relative_url }})

Okno s vlastnosťami

**Vlastné rozloženie**

****Pomocou možnosti Vlastné rozloženie si používateľ môže vytvoriť vlastné hlavné rozloženie grafického rozhrania. Možnosti dostupné na prispôsobenie rozvrhnutia sú znázornené na obr. 4.1.49. Po prispôsobení rozloženia môže používateľ kliknúť na Apply for GUI layout (Použiť pre rozloženie GUI), aby použil vlastné rozloženie. Možnosti prispôsobenia sú nasledovné,

**Složky** : V záložke priečinky môže používateľ vybrať alebo skryť zobrazenie vlastností priečinka a panela priečinkov, ak sa prezerá len jeden problémový priečinok, ako je znázornené na obr. 4.1.49.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image036.jpg' | relative_url }})

Vlastné rozloženie - stránka priečinkov

**Súbory** : V záložke Súbory môže používateľ vybrať alebo skryť zoznam súborov a môžeme tiež vybrať typ filtra súborov, ako je znázornené na obr. 4.1.50.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image037.jpg' | relative_url }})

Vlastné rozloženie - stránka Súbory

**Hlavný pohľad** : Používateľ si môže prispôsobiť zobrazenie grafických, protokolových a správových súborov. (Pozri obr. 4.1.51.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image038.jpg' | relative_url }})

Vlastné rozloženie - stránka Hlavné zobrazenie

**Akcie** : Na karte Akcie si používateľ môže vybrať, či chce zobraziť len panely s odkazmi na akcie alebo len panel s nástrojmi akcií, prípadne oboje. (Pozri obr. 4.1.52.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image039.jpg' | relative_url }})

Vlastné rozloženie - stránka Akcia

  
**Tabuľky** : Používateľ si môže prispôsobiť zobrazenie kariet pomocou možností dostupných v časti "Tabs".

**Povolenie viacerých okien s kartami** : Používateľ môže pristupovať k rôznym priečinkom v rôznych záložkách a sledovať každý projekt samostatne

**Obnovenie kariet pri spustení programu** : Obnoví viacero kariet pri spustení hlavného programu GUI.

**Zobraziť karty v dolnej časti** : Karty sa zobrazia v spodnej časti. (Pozri obr. 4.1.53.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image040.jpg' | relative_url }})

Vlastné rozloženie - stránka s kartami

###
Pomoc

Na nasledujúcom obrázku 4.1.54. sú zobrazené možnosti ponuky Pomocník v grafickom používateľskom rozhraní.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image041.jpg' | relative_url }})

Možnosť ponuky Pomocník

  
**DEFORM manuál**

****Spustí príručku DEFORM Manual zobrazí príručku DEFORM prostredníctvom webového prehliadača.

**O SFTC**

V okne sa zobrazia informácie o SFTC.

**O**

Zobrazuje informácie o DEFORM-2D/3D(GUI) v okne.  
  
**O motore FEM:**

V okne sa zobrazia informácie o motore FEM.  
  
**Informácie o licencii:**

V okne sa zobrazia informácie o licenčnom súbore, dátume vypršania platnosti licencie a ID stroja.

## Náhľad

Na karte Preview (Náhľad) môže používateľ sledovať snímku displeja z posledného prístupu k problému. Používateľ má k dispozícii aj odkaz na otvorenie grafiky simulácie v záložke Preview (Náhľad) počas bežiacej simulácie (pozri obr. 4.1.55.). V závislosti od typu projektu a stavu R databázy sa karta "Preview" (Náhľad) neustále aktualizuje. Ak je typ projektu DOE alebo Optimization (Optimalizácia), zobrazujú sa prípady DOE a snímka z príspevku DOE. Ak ide o simuláciu DOE alebo Optimization (Optimalizácia), potom sa karta náhľadu aktualizuje s tabuľkou premenných DOE, ako je znázornené na obr. 4.1.56. Pre každý ukončený beh môže používateľ kliknúť na beh a zobraziť príslušný priečinok behu v priečinku Problem (Problém).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image042.jpg' | relative_url }})

Karta Náhľad

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image043.jpg' | relative_url }})

Karta Náhľad štúdie DOE

## Správa

V záložke Message (Správa) môže používateľ sledovať správy o výpočte problému metódou konečných prvkov. Súbor správ sa priebežne aktualizuje počas simulácie s informáciami o výpočtoch MKP a príslušnými informáciami v závislosti od typu problému. (Pozri obr. 4.1.57.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image044.jpg' | relative_url }})

Karta Správa

## Log

Na karte Protokol môže používateľ sledovať informácie o súbore protokolu. V súbore denníka sa zobrazujú informácie o začiatku problému, čase potrebnom na simuláciu, informácie o remeselnom spracovaní a stave viacerých operácií. Ak je typ problému DOE alebo Optimization (Optimalizácia), zobrazí sa súbor DOE Log file (Súbor denníka DOE), v ktorom sa zobrazia informácie o spawnovaní databáz, behu DOE a stave extrakcie (pozri obr. 4.1.58).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image045.jpg' | relative_url }})

Karta Denník

## Zhrnutie

Na karte Súhrn môže používateľ sledovať súhrn problémov. Tento súbor sa vytvorí, keď otvoríme databázu v príspevku NG. (Pozri obr. 4.1.59.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image046.jpg' | relative_url }})

Karta Súhrn

## Memo

Na karte Memo môže používateľ pridať poznámku. (Pozri obr. 4.1.60.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image047.jpg' | relative_url }})

Karta Memo
