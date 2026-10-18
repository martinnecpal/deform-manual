---
lang: sk
title: "Laboratórna úloha č. 15 – Laboratórna úloha s posuvnou matricou – puzdro razníka"
---

# Laboratórna práca č. 15 – Laboratórna práca s posuvnou matricou – puzdro razníka

V tomto laboratórnom cvičení si ukážeme, ako nastaviť ovládanie pohybu pre puzdro razníka, do ktorého sú vložené pružiny, pričom druhý koniec pružín je pripevnený k razníku. Puzdro sa posunie dozadu, keď sa naň pôsobí zaťaženie presahujúce predpätie.

  
15.1. Vytvoriť nový problém

15.2. Typ geometrie

15.3. Ovládacie prvky simulácie

15.4. Vkladanie materiálu do stroja

15.5. Pridávanie objektov

15.6. Obrobok

15.7. Definícia dierovacieho nástroja

15.8. Definícia

15.9. Definícia rukáva

15.10. Definícia ejektora

15.11. Polohovanie

15.12. Generovanie kontaktov

15.13. Ovládacie prvky na zastavenie

15.14. Ovládacie prvky krokov

15.15. Vytvorenie databázy

15.16. Spustenie simulácie

15.17. Následné spracovanie výsledkov

## Vytvoriť nový problém

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrated Manufacturing Process**“ a v poli jednotiek vyberte prepínač „**English**“. Názov úlohy zadajte ako „**Punch_Sleeve**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt. V tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie; ako názov projektu použijeme „**Punch_Sleeve**“. Pridajte **2D tvarovaciu operáciu** ako **prvú operáciu** tak, že ju vyberiete z roletového zoznamu Prvá operácia a zaškrtnete políčko, ako je znázornené na obr. L15.1. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0001.jpg' | relative_url }})

Sprievodca MO – Nový projekt

## Typ geometrie

V tomto laboratórnom cvičení budeme používať osovo symetrické geometrie, preto na stránke s typmi geometrií vyberte voľbu **2D osovo symetrická**, ako je znázornené na obr. L15.2, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0002.jpg' | relative_url }})

Výber typu osovo symetrickej geometrie

## Ovládacie prvky simulácie

V tomto laboratórnom cvičení budeme modelovať nastavenie neizotermického pohybu kĺzavého lisovacieho nástroja, preto v okne „Simulation controls“ skontrolujte, či sú zaškrtnuté oba **režimy** **Deformation** a **Heat transfer**, ako je znázornené na obr. L15.3. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0003.jpg' | relative_url }})

Okno riadenia simulácie

## Vkladanie materiálu do stroja

V okne Zoznam materiálov načítajte materiál „**AISI-1015**“ z knižnice materiálov DEFORM v kategórii **Oceľ** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To môžete urobiť tak, ako je znázornené nižšie, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), pozri obr. L15.4. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Objekt.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0004.jpg' | relative_url }})

Okno „Zoznam materiálov“

##  Pridávanie objektov

Na túto operáciu potrebujeme päť objektov, preto v okne „Objekt“ pridajte **päť****objektov** kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) (pozri obr. L15.5.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0005.jpg' | relative_url }})

Okno na pridávanie objektov

## Obrobok

V okne „Workpiece“ (Obrobok) vyberte typ objektu **Plastic** a ponechajte teplotu na hodnote 68 °F, pozri obr. L15.6. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0006.jpg' | relative_url }})

Okno objektu obrobku

### Geometria obrobku

Na stránke Geometria vyberte ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a definujte valec s **polomerom** **0,4** ” a **výškou** **2,7** ” (pozri obr. L15.7.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Mesh“ (Sieť).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0007.jpg' | relative_url }})

Definovanie geometrie

### Vytváranie sietí

Predvolený počet prvkov je pre toto cvičenie postačujúci, preto ponechajte **počet prvkov** na hodnote **1000** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby ste vygenerovali sieť (pozri obr. L15.8.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0008.jpg' | relative_url }})

Okno so sieťou obrobkov

### Priradenie materiálu obrobku

Ak chcete obrobku priradiť materiál, vyberte v okne materiálov materiál **AISI-1015**. To môžete urobiť výberom materiálu zo zoznamu v okne materiálov, ako je znázornené na nižšie uvedenej obr. L15.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0009.jpg' | relative_url }})

Okno na výber materiálu

### Okrajové podmienky obrobku

Na stránke BCC skontrolujte, či je deformácia BCC priradená k ľavej strane obrobku v smere osi X a či je výmena tepla s okolím BCC priradená k celému vonkajšiemu povrchu obrobku (čo nezahŕňa stredovú os, keďže tieto uzly sa nachádzajú vnútri objektu), ktoré sú priradené štandardne počas vytvárania siete. Ak nie sú BCC priradené, priraďte ich ručne podľa obrázkov L15.10 a L15.11 nižšie. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Top die“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0010.jpg' | relative_url }})

Nastavená rýchlosť BCC pre obrobok

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0011.jpg' | relative_url }})

Priradená výmena tepla s okolím (BCC) pre obrobok

## Definícia pojmu „punch“

Na stránke „Top Die“ zmeňte názov na **Punch**, typ objektu ponechajte ako **Rigid** a teplotu objektu na 68 °F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie výseku

V okne Geometria načítajte súbor geometrie **PunchSleeve_Lab_Punch.geo** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice), ako je znázornené na obr. L15.12., V rozbaľovacom okne „User Library“ (Používateľská knižnica), v ktorom sa pýta, či chcete použiť cestu k inštalačnej zložke labs ako predvolené umiestnenie knižnice, kliknite na **Áno**. Geometria sa nachádza v inštalačnej zložke DEFORM v adresári \2D\Labs. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka s pohybmi.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0012.jpg' | relative_url }})

Stránka „Geometria dierovania“

### Priradiť pohyb k úderu

Pre toto laboratórne cvičenie nastavte **rýchlosť** **10** palcov za sekundu v smere **-Y** (pozri obr. L15.13.). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom Die“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0013.jpg' | relative_url }})

Stránka „Punch Movement“

## Definícia

Na stránke „Bottom Die“ zmeňte názov na **Die**, typ objektu ponechajte ako **rigid** a teplotu na 68 °F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie formy

Načítajte súbor **PunchSleeve_Lab_Die.geo** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. L15.14. Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stranu s objektom 4. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0014.jpg' | relative_url }})

Stránka „Geometria“

## Vysvetlenie pojmu „rukáv“

V objekte 4 na stránke zmeňte názov na **Sleeve**, typ objektu ponechajte ako **Rigid** a teplotu objektu ako 68°F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie lisovacej formy

Načítajte súbor **PunchSleeve_Lab_Sleeve.geo** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. L15.15. Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybmi.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0015.jpg' | relative_url }})

Stránka objektu „Sleeve“

### Priradiť pohyb k rukávu

Vyberte typ pohybu ako **Kĺzavý****lisovací nástroj**. Definujte smer posuvného pohybu ako **Y** s konštantnou **tuhosťou****10****klb/in**, **predpätím****1** **klb** a **max. posunom****0,5** ". Vyberte druhý koniec pružiny ako namontovaný na **objekte Punch**, ako je znázornené na obr. L15.16. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až do strany s objektom 5.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0016.jpg' | relative_url }})

Stránka o pohybe rukáva

## Definícia ejektora

V objekte 5 na stránke zmeňte názov na **Ejector**, typ objektu ponechajte ako **Rigid** a teplotu objektu 68°F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Geometria vyhadzovača

Načítajte súbor **DieSleeve_Lab_Ejector.geo** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (pozri obr. L15.17.). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Polohovanie“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0017.jpg' | relative_url }})

Definovanie geometrie vyhadzovača

## Polohovanie

Ak v tomto laboratórnom cvičení vytvoríte alebo naimportujete objekty podľa pokynov, budú sa nachádzať na správnej pozícii (pozri obr. L15.18). Ak objekty nie sú správne umiestnené, použite tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) na ich umiestnenie tak, ako je znázornené na obr. L15.18. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí kontaktná stránka.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0018.jpg' | relative_url }})

Poloha objektov

## Získavanie kontaktov

Vyberte typ kontaktu **Používateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridajú vzťahy medzi obrobkom, razníkom, matricou, puzdrom a vyhadzovačom, ako je znázornené na obr. L15.19.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0019.jpg' | relative_url }})

Predvolené vzťahy na stránke Vytvorenie kontaktu

Zvýraznite vzťah **Punch – Workpiece** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) tento vzťah upravte. V časti obrazovky venovanej treniu (pozri obr. L15.20.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0020.jpg' | relative_url }})

Okno definície údajov medzi objektmi

V roletovom menu **F******riction** vyberte zo zoznamu položku **Cold Forming (carbide dies)**; do poľa Constant friction sa vloží hodnota trenia **0,08**. Na **kartu „Thermal“****** vyberte zo zoznamu typ **tvarovania** „Koeficient prenosu tepla“; do poľa „Koeficient prenosu tepla“ sa vloží hodnota **0,002**. (Pozri obr. L15.21.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0021.jpg' | relative_url }})

Stránka „Inter Object Relation Thermal“

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna kontaktov. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných vzťahov. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie 0,08 a koeficient prenosu tepla 0,002.

Puzdro s ovládacími prvkami posuvného pohybu je namontované na razníku a v priebehu simulácie sa pohybuje spolu s ním. Puzdro prichádza do kontaktu s matricou a môže do nej preniknúť, preto definujte vzťah kontaktu medzi matricou a puzdrom a nastavte matricu ako hlavný objekt. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte kontaktný vzťah. Ako **hlavný objekt** vyberte **matricu** a ako **podriadený objekt** vyberte **rukáv** (ktorý má ovládače posuvného pohybu). (Pozri obr. L15.22.)

Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určte vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,000403"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. (Pozri obr. L15.22.) Prejdite na kartu Správa alebo sledujte stavový riadok, aby ste zistili informácie o vygenerovaných kontaktoch. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0022.jpg' | relative_url }})

Kontakt vznikajúci medzi objektmi

## Ovládacie prvky na zastavenie

Simuláciu zastavíme, keď sa razník posunie o 0,48”. Na obrazovke „Stopping Controls“ zaškrtnite možnosť **Max Die stroke** a následne nastavte hodnotu zdvihu v osi **Y** na **0,48** ". (Pozri obr. L15.23.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0023.jpg' | relative_url }})

Okno „Ovládacie prvky zastavenia“

## Ovládacie prvky krokov

Na stránke nastavení krokov nastavte **Počet krokov** na hodnotu **1000**, **Krok na uloženie** na hodnotu **5** a **Posun matrice na krok** na hodnotu **0,005**. Keďže sme definovali väčší počet krokov, ako je potrebný na celkový posun primárneho razníka, simulácia sa zastaví, keď dosiahne kontrolný bod zastavenia. Nastavte razník ako primárny razník, ak sa nevybral automaticky, pozri obr. L15.24. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0024.jpg' | relative_url }})

Okno „Ovládacie prvky krokov“

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu.

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia, ako je znázornené na obr. L15.25. Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0033.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na konci súboru so správami zobrazí nasledujúca správa (pozri obr. L15.26.):

"PROGRAM SA ZASTAVIL!

„HODNOTA STROKE -0,4800000 PREKROČILA ŠPECIFIKOVANÝ LIMIT 0,4800000“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0025.jpg' | relative_url }})

Súbor so simulačnými správami

## Následné spracovanie výsledkov

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), čím sa otvorí postprocesor MO. V zozname krokov vyberte možnosť „Zobraziť zdvih“ z ponuky, ktorá sa zobrazí po kliknutí pravým tlačidlom myši. Prehrávajte kroky, kým sa puzdro nezačne pohybovať nahor, keď je zdvih razníka približne 0,275". (Pozri obr. L15.27.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0026.jpg' | relative_url }})

Graf zaťaženia a zdvihu v okamihu, keď sa posuvná objímka začne posúvať nahor

Vykreslite krivku **zaťaženie – zdvih** a sledujte zaťaženie v tomto bode. Vidíme, že keď sa na puzdro pôsobí zaťaženie presahujúce definované predpätie, ktoré je 1 klb, začne sa pohybovať nahor. Pokračujte v prehrávaní animácie a zastavte ju, keď puzdro zmení smer pohybu. V tomto bode zmerajte vzdialenosť medzi pravým dolným rohom puzdra a pravým horným rohom matrice a porovnajte ju s maximálnym posunom definovaným v nastaveniach posuvu puzdra. Môžeme pozorovať, že puzdro prestalo stúpať hneď po dosiahnutí maximálneho posunu definovaného v nastaveniach posuvu puzdra. (Pozri obr. L15.28.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0027.jpg' | relative_url }})

Zaťaženie puzdra a jeho posunutie pri dosiahnutí maximálneho posunutia

Pokračujte v prehrávaní animácie, aby ste mohli sledovať tok materiálu, a v poslednom kroku skontrolujte celkový posun hornej formy pomocou možnosti merania. (Pozri obr. L15.29.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0028.jpg' | relative_url }})

Obrobok v poslednom kroku

####  Stavové premenné:

Prejdite na posledný krok a zo zoznamu **Stavové premenné** vyneste do grafu dôležité stavové premenné, ako sú **efektívne deformácie**, **efektívne napätia**, **teplota** a **poškodenie**, ako je znázornené na obr. L15.30 až obr. L15.33.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0029.jpg' | relative_url }})

Graf premennej stavu „efektívne deformácie“

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0030.jpg' | relative_url }})

Graf premennej stavu „efektívne napätie“

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0031.jpg' | relative_url }})

Graf premennej teploty

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0032.jpg' | relative_url }})

Graf premennej stavu poškodenia
