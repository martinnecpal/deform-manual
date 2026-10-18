---
lang: sk
title: "Lab05 – Laboratórne cvičenia s krátkymi hriadeľmi"
---

# Laboratórna práca č. 5. Laboratórne cvičenia s krátkou hriadeľou

5.1. Operácia 1: Operácia s kužeľom

5.2. Operácia 2: Operácia na hlave

5.3. Symetria/tepelné operácie

5.4. Analýza namáhania nástroja

5.5. Pridanie zúžovacieho krúžku na lisovaciu formu

5.6. Mechanický lis

## Operácia 1: Operácia s kužeľom

### Vytvorenie nového problému

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu **Nový****problém**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek zvoľte systém jednotiek pomocou prepínača „**Anglický**“. Názov úlohy zadajte ako „**Stub_Shaft**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca MO, v tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**Stub_Shaft**“.

Používateľ môže tiež zmeniť systém jednotiek a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka. Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

### Pridávanie operácií

Pridajte **dve****3D****tvarovacie****operácie** zo zoznamu operácií v Průzkumníku. Operácie pridáte kliknutím na tlačidlo 3D Forming ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ich môžete pridať aj pretiahnutím do Editoru operácií.

### Ovládacie prvky simulácie

V tomto cvičení ukážeme, ako nastaviť jednoduchú izotermickú úlohu. V okne „Simulation controls“ teda **odznačte** políčko režimu **Heat****transfer** (pozri obr. 3DL5.1.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0001.jpg' | relative_url }})

Okno riadenia simulácie

### Zoznam materiálov

V okne Zoznam materiálov kliknite na možnosť Načítať údaje o materiáli z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a načítajte materiál „**AISI-4120**“ z kategórie **Oceľ**, ako je znázornené na obr. 3DL5.2. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Objekt.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0002.jpg' | relative_url }})

Okno „Zoznam materiálov“

### Pridávanie objektov

Ak tam ešte nie sú štyri objekty, pridajte ich kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (pozri obr. 3DL5.3.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0003.jpg' | relative_url }})

Okno na pridávanie objektov

### Obrobok

V okne „Workpiece“ (Obrobok) zmenite názov objektu na **Billet** a ako typ objektu vyberte **Plastic**, ako je znázornené na obr. 3DL5.4. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0004.jpg' | relative_url }})

Objekt „Billet“ – Okno

#### Geometria polotovaru

Na stránke Geometria vyberte ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a definujte **valec** s **priemerom** **0,8** ” a **výškou** **2,7** ” (pozri obr. 3DL5.5.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka siete.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0005.jpg' | relative_url }})

Definovanie geometrie obrobku

#### Vytváranie sietí

Predvolené nastavenia sú na vytvorenie siete postačujúce. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby ste vytvorili sieť. (pozri obr. 3DL5.6.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0006.jpg' | relative_url }})

Vytvorenie siete obrobku

#### Priradenie materiálu na výkovky

Ak chcete obrobku priradiť materiál, vyberte v okne materiálov materiál **AISI-4120**. Postupujte podľa obrázku 3DL5.7 nižšie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0007.jpg' | relative_url }})

Okno na výber materiálu

### Definícia pojmu „Top Die“

Na stránke „Top Die“ zmenite názov hornej matrice na **Punch** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

#### Importovať geometriu dierovania

Naimportujte súbor **StubShaft_ConePunch.STL** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DL5.8. Skontrolujte geometriu a klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybmi.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0008.jpg' | relative_url }})

Import geometrie výseku 

#### Priradiť pohyb k hornej kocku

Pre toto laboratórne cvičenie nastavte rýchlosť **10** palcov za sekundu v smere **-Z**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom Die“.

### Definícia spodnej matrice

Na stránke „Bottom die“ nastavte typ objektu na **Rigid** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (pozri obr. 3DL5.9.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0009.jpg' | relative_url }})

Stránka spodnej matrice

#### Import geometrie spodnej matrice

Načítajte súbor **StubShaft_ConeDie.STL** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DL5.10. Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekt 4“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0010.jpg' | relative_url }})

Import geometrie spodnej matrice

### Definícia ejektora

V okne „Objekt 4“ zmeňte názov objektu 4 na **Ejector** a potvrďte typ objektu ako **Rigid**, ako je znázornené na obr. 3DL5.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0011.jpg' | relative_url }})

Okno objektu „Ejector“

#### Geometria vyhadzovača

V okne „Geometria vyhadzovača“ vyberte a definujte **valec** s **priemerom** **0,817** ” a výškou **1** ” (pozri obr. 3DL5.12.), kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Positioning“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0012.jpg' | relative_url }})

Definícia geometrie vyhadzovača

### Polohovanie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}) a vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **vysúvač** a referenčný objekt na **surovinový blok**. Zmeňte smer priblíženia na **Z**, stlačte ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (pozri obr. 3DL5.13.) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Kontakt.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0013.jpg' | relative_url }})

Okno „Polohovanie objektu“

### Získavanie kontaktov

Vyberte typ kontaktu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom, razníkom, spodnou matricou a vyhadzovačom, ako je znázornené na obr. 3DL5.14. Keďže matrice sú tuhé a polotovar je plastický, razník, spodná matrica a vyhadzovač sa považujú za hlavné prvky a polotovar za podriadený prvok.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0014.jpg' | relative_url }})

Stránka na získavanie kontaktov

Zvýraznite vzťah **Punch – Billet** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej treniu (pozri obr. 3DL5.15.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže táto simulácia prebieha pri izbovej teplote a formy sú oceľové, použite rozbaľovacie menu a zo zoznamu vyberte možnosť **Tvarovanie za studena (oceľové formy)**. Hodnota trenia **0,12** sa nastaví automaticky.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0015.jpg' | relative_url }})

Okno definície údajov medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna kontaktu. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie 0,12. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určte vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,001"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Prejdite na kartu Správy alebo sledujte stavový riadok, aby ste zistili informácie o vytvorených kontaktoch. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky na zastavenie

Chceme simuláciu zastaviť, keď sa razník a matrica nachádzajú vo vzdialenosti do 0,025” od seba. Na obrazovke „Stopping Controls“ zaškrtnite možnosť **Vzdialenosť medzi objektmi** a potom kliknite na body na spodnej strane razníka a na hornej strane spodnej matrice. Nastavte hodnotu tejto vzdialenosti na **0,025** ” v smere **Z**. (pozri obr. 3DL5.16.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0016.jpg' | relative_url }})

Okno „Ovládacie prvky zastavenia“

### Ovládacie prvky krokov

Chceme, aby sa razník posunul o 0,5” v 50 krokoch, takže každý krok bude mať dĺžku 0,5/50, teda 0,01”. V okne „Step Controls“ (Ovládacie prvky krokov) v časti **Solution Steps Definition** (Definícia krokov riešenia) nastavte **Die Displacement** (Posun razníka) na hodnotu **0,01** ”. Nastavte **Počet simulačných krokov** na **50** a **Krok na uloženie** na **5**. Nastavte **razník** ako **primárny razník**, ak sa nezvolil automaticky (pozri obr. 3DL5.17). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0017.jpg' | relative_url }})

Okno „Ovládacie prvky krokov“

### Vytvoriť databázu

Na stránke „Generate DB“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť, aby bolo možné spustiť simuláciu (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste prešli k ďalšej operácii.

## Operácia 2: Operácia na hlave

### Ovládacie prvky simulácie

V časti „Ovládacie prvky simulácie“ zrušte zaškrtnutie políčka **Prenos tepla**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekty“.

###  Pridávanie objektov

Ak tam ešte nie sú štyri objekty, pridajte štyri objekty kliknutím na tlačidlo „Vložiť objekt“ ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (pozri obr. 3DL5.18.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0018.jpg' | relative_url }})

Okno na pridávanie objektov

### Definícia obrobku

Chceme použiť obrobok z posledného kroku predchádzajúcej operácie, preto nastavíme objekt „Obrobok“ na „Načítať z databázy“. Na stránke „Obrobok“ vyberte prepínač **Načítať z databázy**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Horná matrica (razník)“. (pozri obr. 3DL5.19.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0019.jpg' | relative_url }})

Stránka objektu obrobku

### Definícia pojmu „Top Die“

Na stránke „Top Die (Punch)“ zmeňte typ objektu na **Rigid**. Ak sa objekt nenazýva „Punch“, premenujte ho na „Punch“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import geometrie dierovacieho nástroja:

Naimportujte súbor **StubShaft_HeadPunch.STL** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DL5.20. Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybmi.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0020.jpg' | relative_url }})

Načítavanie geometrie razníka

#### Priradiť pohyb k úderu

Pre toto laboratórne cvičenie nastavte rýchlosť **10** palcov za sekundu v smere **-Z**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom Die“.

### Definícia spodnej formy

Na stránke „Bottom die“ zmeňte typ objektu na **Rigid** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import geometrie spodnej formy

Načítajte súbor **StubShaft_HeadDie.STL** pomocou tlačidla „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})). Skontrolujte geometriu a klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka s objektom 4 (vysúvač).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0021.jpg' | relative_url }})

Načítanie geometrie spodnej matrice

### Definícia vyhadzovača

Objekt „Ejector“ nastavíme tak, aby čítal údaje z databázy. Na stránke „Ejector“ vyberte tlačidlo „Read from DB“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Positioning“.

### Polohovanie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) a zmeňte objekt polohovania na **Punch**. Vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) a umiestnite ho (x=0, y=0 a **Z** =**2**) v smere **Z**, kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (pozri obr. 3DL5.22.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0022.jpg' | relative_url }})

Okno „Poloha objektu“

### Plánované polohovanie

Pomocou polohovania na základe interferencie polohujeme razník voči obrobku. Na stránke „Naplánované polohovanie“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **razník** a referenčný bod na **surovinový blok**. Zmeňte smer priblíženia na **-Z** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (pozri obr. 3DL5.23.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0023.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Získavanie kontaktov

Definujte vzťahy medzi kontaktmi pomocou rovnakých nastavení, aké sme definovali pre prvú operáciu v časti 5.1.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky zastavenia

Zapnite možnosť „Vzdialenosť medzi objektmi“ a definujte referenčné body tak, ako je znázornené na obr. 3DL5.24. Nastavte brzdnú vzdialenosť na **0,375** ” v smere **Z**.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0024.jpg' | relative_url }})

Ovládanie zastavenia na základe vzdialenosti medzi objektmi

Pre tento diel tiež určíme **maximálne****zaťaženie**. Na karte **Deformácia** nastavte maximálne zaťaženie na X = 0, Y = 0 a Z = **600**. Ak teraz zaťaženie lisu prekročí hodnotu **600 Klb** (300 ton), simulácia sa zastaví, aj keď ešte nebola dosiahnutá vzdialenosť medzi nástrojmi (pozri obr. 3DL5.25.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0025.jpg' | relative_url }})

Stránka ovládacích prvkov zastavenia

### Ovládacie prvky krokov

Odhadnite celkový zdvih razníka, ktorý bude približne 1,5”. Na konci simulácie chceme dosiahnuť medzeru 0,375. Nevadí, ak tu mierne prekročíme zdvih razníka, pretože nastavíme podmienku zastavenia, aby sa nástroje zastavili, keď budú od seba vzdialené 0,375”. Od hodnoty 1,5 teda odpočítame len 0,3. Tým získame celkový zdvih razníka 1,2. Pri 100 krokoch to znamená, že razník sa musí pri každom kroku posunúť o 0,012”.

Nastavte **počet simulačných krokov** na **100**, **krok pri ukladaní** na **5** a **konštantný posun matrice** na **0,012** ''. (pozri obr. 3DL5.26.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0026.jpg' | relative_url }})

Okno „Ovládacie prvky krokov“

### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“; ak sa zobrazí chyba zadávania údajov, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto laboratórnej úlohy by sa mala zobraziť správa: „Pre túto operáciu nie je potrebné generovať databázu. K tomu dôjde počas behu programu.“

Uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. 3DL5.27). Otvorí sa dialógové okno „Možnosti spustenia“, ako je znázornené na obr. 3DL5.28. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0028.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Keď sa simulácia bez problémov dokončí, skontrolujte správy v súbore LOG; po dokončení všetkých operácií sa v súbore LOG zobrazia správy: „MULTIPLE OPERATION COMPLETED“.

### Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

#### Výsledky hry

Pomocou funkcie ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) prehrávajte tak úder na kužeľ, ako aj úder na hlavu.

Vyskúšajte si rôzne možnosti tieňovania častí. 

#### Hľadanie záhybov

Kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) otvoríte okno „Stavové premenné“.

Kliknite na **uhol ohybu****** a zmeňte režim mierky na „**Používateľ**“. Do polí Min a Max zadajte hodnoty 270, resp. 271. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). (Pozri obr. 3DL5.29.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0029.jpg' | relative_url }})

Okno s premennou polohou a ohybom na obrobku

Zlomenie je teraz zobrazené červenou farbou. Používateľ môže prechádzať jednotlivými časovými krokmi a sledovať, ako sa zlomenie formuje. Používateľ môže tiež kliknúť pravým tlačidlom myši na farebný pruh a vyskúšať si rôzne typy farebných pruhov. (Pozri obr. 3DL5.30.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0030.jpg' | relative_url }})

Obrázok znázorňujúci ohyb v obrobku

Na zvislé rozrezanie dielu použite rezací nástroj ![]({{ '/assets/icons/pre_icons/mo_slicing_option.jpg' | relative_url }}). Kliknite na prepínač vedľa položky „**Krivka + rovina**“, ako je znázornené na obr. 3DL5.31.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0031.jpg' | relative_url }})

Okno rezania

Na tomto pohľade môžete ľahko vidieť záhyby. (Pozri obr. 3DL5.32.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0032.jpg' | relative_url }})

Rozrezaný objekt

#### Určenie výplne

Stlačte tlačidlo „Vymazať“ (![]({{ '/assets/icons/post_icons/mo_clear_sv_icon.jpg' | relative_url }})), aby ste deaktivovali všetky premenné. Následne aktivujte zobrazenie kontaktných uzlov (![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }})).

Funkcia DEFORM umiestňuje bodky na miesta, kde došlo ku kontaktu s nástrojom. Miesta bez bodiek môžu znamenať nedostatočné vyplnenie (pozri obr. 3DL5.33.). Vyplnenie je možné skontrolovať aj rezom cez diel.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0033.jpg' | relative_url }})

Určenie vyplnenia objektu

Vypnite kontakt ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}). Zobrazte všetky nástroje a obrobok ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}).

Pomocou nástroja na rezanie rozrežte objekty v rovine x-y (nastavte smer N na (0,0,1). V možnosti „Zobrazenie roviny rezu“ vyberte položku „**Krivka**“. (Pozri obr. 3DL5.34.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0034.jpg' | relative_url }})

Okno na krájanie 

Kliknite na súradnicu Z vedľa poľa na zadanie P (bod). Potom pomocou posuvníka posuňte rezovú rovinu nahor alebo nadol po osi Z.

Kliknite na tlačidlo „+ smer Z“, aby ste si objekty prezreli zo smeru +Z, ako je znázornené na obr. 3DL5.35.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0035.jpg' | relative_url }})

Objekt v pohľade +Z

Používateľ môže priamo vidieť medzeru medzi nástrojom a obrobkom. Odstráňte ![]({{ '/assets/icons/pre_icons/mo_delete_symmetry_icon.jpg' | relative_url }}) rovinu rezania z ponuky rezania.

Doposiaľ sme na zistenie nedopĺňania použili kvalitatívne metódy. Používateľ môže tiež znázorniť vzdialenosť medzi obrobkom a nástrojom.

Kliknite na ikonu „Štátne premenné“ ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}). Vyberte položku „**Minimálna****vzdialenosť**“ a stlačte ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

Vypnite všetky nástroje a zobrazte iba obrobok ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}). Zobrazí sa bežná vzdialenosť medzi obrobkom a najbližším nástrojom. Používateľ môže kliknúť ľavým tlačidlom myši kdekoľvek na obrobku. Tým sa na farebnej lište zaznačí hodnota minimálnej vzdialenosti. (Pozri obr. 3DL5.36.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0036.jpg' | relative_url }})

Obrázok znázorňujúci oblasť minimálnej vzdialenosti

## Symetria/Tepelné operácie

### Vytvoriť novú simuláciu

Teraz vykonáme operáciu Cone_Blow zhora s vyhreteným polotovarom. To zahŕňa zahriatie polotovaru, jeho ponechanie na vzduchu po dobu 6 sekúnd (prevod), ponechanie v matrici po dobu 2 sekúnd (zdržanie) a následné tvarovanie (kužeľ). Všetko toto vykonáme simuláciou 1/12 dielu s využitím symetrie, ako je znázornené v [Fig. 3DL5.37.]({{ '/docs/sk/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/' | relative_url }}#FIg_3DL5_37_Workpiece_showing_1/12th_of_the_symmetry)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0037.jpg' | relative_url }})

Obrobok znázorňujúci 1/12 symetrie

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu **Nový****problém**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek zvoľte systém jednotiek pomocou prepínača „**Anglický**“. Názov úlohy zadajte ako „****Stub_shaft_symmetry****“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém pomocou integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0038.jpg' | relative_url }})

Problém s definovaním okna

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu, ako je znázornené na obr. 3DL5.38. V poli pre názov projektu nastavte názov projektu na „**Stub_shaft_symmetry**“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Pridať operácie

Zoznamu operácií v Průzkumníku pridajte **dve operácie 3D prenosu tepla** a **jednu operáciu 3D tvarovania**. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa príslušnej operácie alebo ju môžete pridať aj pretiahnutím do oblasti Editoru operácií.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0039.jpg' | relative_url }})

Pridávanie operácií

### Import databázy

Po pridaní všetkých troch operácií načítajte predtým simulovaný súbor **Stub_Shaft.DB**, vyberte **prvý****krok** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0040.jpg' | relative_url }})

Import databázy

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0041.jpg' | relative_url }})

Okno výberu kroku

### Výber typu prenosu tepla

Pre prvý prevádzkový režim vyberte typ prenosu tepla „Prenos vzduchom“, ako je znázornené na obr. 3DL5.42. Tým sa nastavia predvolené parametre prenosu tepla pre režim kúrenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0042.jpg' | relative_url }})

Výber typu prenosu tepla pre prevádzku ohrevu v peci

### Nastavenie podmienok procesu

Nastavte **dĺžku ohrevu****** na **6** sekúnd pri teplote pece alebo okolitej teplote **68°F**, ako je znázornené na obr. 3DL5.43, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0043.jpg' | relative_url }})

Okno s podmienkami procesu

### Vyberte ovládacie prvky simulácie

Nechajte zaškrtnutý len **režim prenosu tepla**, pretože sa modeluje iba prenos tepla, ako je znázornené na obr. 3DL5.44, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0044.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre vykurovanie pece

### Stránka s materiálmi

**Odstráňte** zo zoznamu importovaný materiál **AISI-4120[70-2200F(20-1200C)]**.

### Stránka „Objekty“

Na stránke „Objekty“ vidíme všetky objekty importované z databázy stubshaft.

### Definícia pojmu „billet“

V okne objektu „Billet“ nastavte **typ objektu** na „**Plast**“ a zmeňte **teplotu objektu** na **2100** °**F**. (Pozri obr. 3DL5.45.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0045.jpg' | relative_url }})

Stránka s definíciami pojmov v oblasti výkovkov

#### Geometria polotovaru

Na stránke „Geometria“ vyberte a definujte **valec** s **priemerom** **0,8** ”, **výšku** **2,7** ” a **uhol otáčania****** **30** stupňov (pozri obr. 3DL5.46.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a definujte rovinnú symetriu pre obe symetrické plochy (pozri obr. 3DL5.47. a obr. 3DL5.48.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka siete.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0046.jpg' | relative_url }})

Definovanie geometrie obrobku

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0047.jpg' | relative_url }})

Stránka o geometrii

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0048.jpg' | relative_url }})

Definícia rovinná symetria

#### Vytvoriť sieť

Vytvorte sieť s použitím **32 000** prvkov (pozri obr. 3DL5.49.). V expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) je k dispozícii aj kompletná škála možností vytvárania sietí, ak potrebujete mať väčšiu kontrolu nad vytvorenou sieťou. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0049.jpg' | relative_url }})

Okno na generovanie siete

#### Priradiť materiál obrobku

Pomocou možnosti „Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})“ načítajte materiál **AISI****-8620** z kategórie **Oceľ**; na priradenie materiálu k obrobku vyberte materiál „**AISI****-8620**“ z okna materiálov. Postupujte podľa obrázku 3DL5.50. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0050.jpg' | relative_url }})

Okno na výber materiálu objektu

#### Definovanie okrajových podmienok

Na stránke BCC skontrolujte, či je na celý vonkajší povrch polotovaru (s výnimkou symetrických plôch) predvolene priradená výmena tepla s prostredím BCC. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Punch Movement“ (Pohyb razníka).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0051.jpg' | relative_url }})

Okno s definíciami BCC

### Definícia pohybu úderu

Na stránke „Punch movement“ (Pohyb razníka) nastavte „konštantnú hodnotu“ rýchlosti na **0**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Positioning“ (Polohovanie).

### Polohovanie

Nástroje posunieme ďalej od objektu, aby nebránili procesu chladenia. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) otvoríte stránku s nastavením polohy. Pomocou ![]({{ '/assets/icons/pre_icons/mo_offset.jpg' | relative_url }}) posuňte **razník****2** palce v smere „**Z**“. Posuňte tiež **spodnú****matricu** a vyhadzovač o **-2** palce v smere „**Z**“. Stlačte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili menu polohovania. (Pozri obr. 3DL5.52.) Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno Ovládacie prvky krokov

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0052.jpg' | relative_url }})

Okno na umiestňovanie objektov

### Definovanie ovládacích prvkov krokov

Nastavte **počet simulačných krokov** na **50** s dĺžkou každého kroku **0,12** s a ukladajte každých **5** krokov (pozri obr. 3DL5.53.). Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0053.jpg' | relative_url }})

Nastavenia riadenia simulácie prevádzky ohrevu pece

### Vytvoriť databázu

Na stránke „Generate DB“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) necháte program skontrolovať, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) a prejdite k ďalšej operácii.

### Výber typu prenosu tepla (2. operácia)

Pre druhú operáciu vyberte typ prenosu tepla **Rest on die**, ako je znázornené na obr. 3DL5.54. Tým sa nastavia predvolené nastavenia prenosu tepla pre operáciu ohrevu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0054.jpg' | relative_url }})

Výber typu prenosu tepla pre prevádzku ohrevu v peci

### Nastavenie podmienok procesu

Nastavte **doba odpočinku** na **2** sekundy pri teplote pece alebo okolitej teplote **68** °F, ako je znázornené na obr. 3DL5.55, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0055.jpg' | relative_url }})

Okno s podmienkami procesu

### Vyberte ovládacie prvky simulácie

Nechajte zaškrtnutý len **režim prenosu tepla**, pretože sa modeluje iba prenos tepla, ako je znázornené na obr. 3DL5.56, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s objektmi.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0056.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre vykurovanie pece

### Definovanie objektov

Keď prejdeme do druhej operácie, všetky objekty sa nám zobrazujú ako „Prečítané z databázy“; potvrďte všetky objekty ako „Prečítané z databázy“ (pozri obr. 3DL5.57.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Plánované polohovanie“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0057.jpg' | relative_url }})

Stránka „Objekty“

### Plánované polohovanie

Pomocou možnosti polohovania ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) posuňte spodnú matricu a vyhadzovač o **2** palce v smere „**Z**“ (pozri obr. 3DL5.58.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0058.jpg' | relative_url }})

Plánované polohovanie

### Získavanie kontaktov

Vyberte typ kontaktu **user**, dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať vzťah) a pre prvý vzťah vyberte **Bottom******matrica** ako hlavný prvok a **sústružný polotovar** ako podriadený prvok pre prvý vzťah a pre druhý vzťah vyberte **vysúvač** ako hlavný prvok a **sústružný polotovar** ako podriadený prvok, ako je znázornené na obr. 3DL5.59.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0059.jpg' | relative_url }})

Vzťah medzi obrobkom a spodnou matricou

Kliknite na tlačidlo vzťahu ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) (Upraviť) a v sekcii **tepelná** vyberte z roletového menu možnosť „**Voľný pokojový stav**“, čím definujete koeficient prenosu tepla medzi objektmi, ako je znázornené na obr. 3DL5.60. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úpravy. Tým sa počas simulácie vytvorí kontakt medzi objektmi na začiatku operácie voľného odpočinku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno ovládania krokov.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0060.jpg' | relative_url }})

Výber koeficientu prenosu tepla medzi objektmi v stave pokoja

### Definovanie ovládacích prvkov krokov

Nastavte **počet simulačných krokov** na **20** s dĺžkou **0,1** sekundy na každý krok a ukladajte **každých** **5** krokov (pozri obr. 3DL5.61.). Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0061.jpg' | relative_url }})

Nastavenia riadenia simulácie prevádzky ohrevu pece

### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“; ak sa zobrazí chyba zadávania údajov, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto laboratórnej úlohy by sa mala zobraziť správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“ Uložte projekt a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}).

### Výber ovládacích prvkov simulácie (3. operácia)

Pre operáciu tvarovania **zaškrtnite** políčko **Deformácia** spolu s **prenosom tepla**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s objektmi.

### Definovanie objektov

Ak tam ešte nie sú štyri objekty, pridajte ich kliknutím na tlačidlo „Vložiť objekt“ ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (pozri obr. 3DL5.62.). Všetky štyri objekty by mali byť definované ako objekty typu „Čítať z databázy“. Ak tomu tak nie je, nastavte ich takto na stránke každého objektu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0062.jpg' | relative_url }})

Stránka s objektmi

### Definovanie obrobku

**Vlastnosti obrobku:**

Na stránke „Billet Properties“ zaškrtnite políčko „**Redefine : Target volume**“ a vyberte tlačidlo „**Active in Meshing**“, potom kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) otvoríte vyskakovacie okno. (Pozri obr. 3DL5.63.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0063.jpg' | relative_url }})

Stránka „Vlastnosti“

### Definícia úderu

**Definícia pohybu úderu:**

Nastavte pre objekt „Punch“ rýchlosť **4** palcov za sekundu v smere **-Z**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Scheduled positioning“.

### Plánované polohovanie

Na stránke „Plánované polohovanie“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte „Polohovací objekt“ ako **Punch** a metódu ako „**Interference**“ vo vzťahu k „**Billet**“ v smere **-Z** (pozri obr. 3DL5.64.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0064.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Získavanie kontaktov

Vyberte kontakt typu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom, razníkom, spodnou maticou a vyhadzovačom (pozri obr. 3DL5.66.). Keďže matrice sú tuhé a polotovar je plastický, horná a spodná matrica sa považujú za hlavné a polotovar za podriadený.

Zvýraznite vzťah **Punch – Billet** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej treniu (pozri obr. 3DL5.65.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže ide o simuláciu tvárnenia za tepla a formy sú oceľové, použite roletové menu a zo zoznamu vyberte možnosť **Tvárnenie za tepla (s mazaním)**. Hodnota trenia **0,3** sa vyberie automaticky. Na karte **Tepelné** vyberte zo zoznamu položku „**Tvarovanie**“ a koeficient prenosu tepla „**0,002**“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0065.jpg' | relative_url }})

Okno na definovanie koeficientu trenia medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna Kontakt. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy trenie 0,3, ako je znázornené na obr. 3DL5.66. Keďže sa kontakt inicializuje a vygeneruje počas vytvárania databázy, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0066.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre formovaciu operáciu

### Ovládacie prvky na zastavenie

Chceme simuláciu zastaviť, keď sa razník a matrica nachádzajú vo vzdialenosti do 0,025” od seba. Na obrazovke „Stopping Controls“ zaškrtnite možnosť **Vzdialenosť medzi objektmi** a potom kliknite na body na spodnej strane razníka a na hornej strane spodnej matrice. Nastavte hodnotu tejto vzdialenosti na **0,02****5** ” v smere **Z** (pozri obr. 3DL5.67.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky krokovania.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0067.jpg' | relative_url }})

Okno „Ovládacie prvky zastavenia“

### Ovládacie prvky krokov

Chceme, aby sa razník posunul o 0,5” v 50 krokoch, takže každý krok bude 0,5/50, teda 0,01”. V okne „Step Controls“ zadajte definíciu krokov riešenia ako „With Equal Die Displacement of 0,01”“. Nastavte **Počet simulačných krokov** na **50** a **Krok prírastku na uloženie** na **5**. Nastavte **razník** ako **Primárny****matricu**, ak sa nevyberie automaticky (pozri obr. 3DL5.68.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku generovania databázy.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0068.jpg' | relative_url }})

Okno „Ovládacie prvky krokov“

### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“; ak sa zobrazí chyba zadávania údajov, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto laboratórnej úlohy by sa mala zobraziť správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“

Uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Spustenie simulácie

Kliknite na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. 3DL5.70.), keď kliknete na možnosť Spustiť, použite predvolenú možnosť **Pokračovať v spúšťaní** na výber možnosti „**Pokračovať od posledného kroku**“ a potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0070.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá možnosť „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a tiež informácie o tom, ako dobre simulácia prebieha.

Keď simulácia prebehne bez problémov, skontrolujte správy v súbore LOG; po dokončení všetkých operácií sa v súbore LOG objaví správa: „MULTIPLE OPERATION COMPLETED“.

### Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}), aby bol viditeľný len obrobok. Kliknite na stavovú premennú **Teplota**, aby sa vykreslila teplota obrobku. Kliknite pravým tlačidlom myši na stupnicu teploty a vyberte „**Farebný****typu pruh**“ a potom „**Teplota**“. (Pozri obr. 3DL5.71.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0071.jpg' | relative_url }})

Objekt zobrazujúci hodnoty teploty s typom farebnej stupnice teploty

Kliknite na ikonu **Zrkadlová symetria** ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}). Klikajte na symetrické plochy, kým neuvidíte celý diel. Bude to vyžadovať 11 kliknutí. (Pozri obr. 3DL5.72.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0072.jpg' | relative_url }})

Zrkadlenie symetrických plôch

## Analýza napätí v nástroji

### Otvorenie súboru projektu

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu **Nový****problém**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek pomocou prepínača „**Anglický**“. Názov úlohy zadajte ako „**StubShaft_ToolStress**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca MO spolu s oknom na zadanie názvu projektu. V poli pre názov projektu vyberte prepínač **kopírovať existujúci projekt**. Kliknite na tlačidlo prehľadávania zdrojového umiestnenia a **importujte** súbor **Stub_Shaft.moproj** z predtým simulovaného projektu Stub_shaft, **zaškrtnite** **políčko Kopírovať databázu** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) v okne na zadanie názvu projektu. Simulácia Stub_shaft sa naimportuje do projektu „StubShaft_ToolStress“.

### Pridať operáciu „Diestress“

Zoznamu operácií v prehliadači vyberte operáciu „Diestress 3D“ a pridajte ju kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}). Operáciu môžete pridať aj pretiahnutím a upustením do editora operácií.

Teraz v Editoru operácií vyberte operáciu Diestress 3D

### Pridať objekty

Na túto operáciu sme potrebovali tri objekty, preto ponechajte objekty „Obrobok“, „Horná forma“ a „Spodná forma“ a odstráňte objekt „Vytláčadlo“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Objekt 1“.

### Objekt1

V predvolenom nastavení je pre objekt 1 zaškrtnuté políčko „Obrobok (načítať objekt z databázy)“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Horná matrica

V prípade Top Die je štandardne zaškrtnuté políčko Dies (**Elastic**). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku generovania siete.

#### Generovanie sietí

Vytvorte sieť s **40 000** prvkami. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Interpolácia s vynútením

Po vytvorení siete je potrebné interpolovať formovacie zaťaženia z obrobku na hornú matricu. Silu interpolujte kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Priradiť materiál pre hornú matricu

Naimportujte materiál formy AISI-D3 z knižnice materiálov. Zo zoznamu vyberte **AISI-D3**, aby ste tento materiál priradili hornej forme. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Nastavenie okrajovej podmienky pre hornú formu

Ďalej musíme na hornú matricu aplikovať okrajové podmienky, aby neodletela do vesmíru, keď na ňu pôsobia zaťaženia vznikajúce pri tvárnení.

Na hornej ploche hornej matrice nastavte okrajovú podmienku Vx = Vy = Vz = 0. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Spodná matrica“.

### Spodná forma

V prípade spodnej matrice je štandardne zaškrtnuté políčko „Matrice (pružné)“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka na generovanie siete.

#### Generovanie siete

Vytvorte sieť s 40 000 prvkami. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Interpolácia s vynútením

Po vytvorení siete je potrebné interpolovať formovacie zaťaženia z obrobku na spodnú formu. Interpolujte silu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Priradiť materiál pre spodnú matricu

Zo zoznamu vyberte **AISI-D3**, aby ste priradili materiál pre spodnú matricu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Nastavenie okrajovej podmienky pre spodnú formu

Ďalej musíme na spodnú matricu aplikovať okrajové podmienky, aby neodletela do vesmíru, keď na ňu pôsobia deformujúce zaťaženia.

Na spodnej ploche spodnej formy nastavte okrajovú podmienku Vx=Vy=Vz = 0. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Simulation controls“ (Ovládacie prvky simulácie).

### Ovládacie prvky simulácie

Nastavte **počet krokov** na hodnotu **1**, **krok prírastku na uloženie** na hodnotu **1** a **čas na jeden krok** na hodnotu **1**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť databázu

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), aby sa otvorilo dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať v spúšťaní**, vyberte možnosť „**Pokračovať od posledného kroku**“ a potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

### Následné spracovanie

Pomocou roletového menu „Stavová premenná“ vyneste do grafu **efektívne napätie** a **maximálne hlavné napätie.**

Ak efektívne napätie prekročí medzu tečnosti materiálu, dôjde k plastickému deformovaniu nástrojov.

Ak je maximálne hlavné napätie veľké, môže to byť miesto, kde dôjde k vzniku únavového porušenia.

U karbidových nástrojov môžu kladné hlavné napätia, aj keď sú relatívne malé, naznačovať začiatok únavového poškodenia.

Všimnite si, že v tejto simulácii je efektívne napätie mimoriadne vysoké.

## Pridanie zúženého krúžku na maticu

Po dokončení následného spracovania sa vráťte do režimu „Pre“ kliknutím na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

### Pridať operáciu „Analýza napätia v matrici“

V ľavom hornom rohu okna zobrazenia kliknite ľavým tlačidlom myši na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu „Add Die stress Study“. Operácia „Die stress Study“ sa pridá do editora operácií. 

### Výber kroku

Ak chcete vykonať operáciu „Die stress“, vyberte v zozname výberu krokov druhý krok od konca. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Pridať objekty

V tejto štúdii namáhania formy budeme analyzovať iba hornú formu a spodnú formu so zmenšovacím krúžkom, preto odstránime objekt „Ejector“ pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) a pridáme nový objekt na vytvorenie krúžku kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). 

Postupujte podľa pokynov od časti 5.4.5 „Horná forma“ až po časť 5.4.6.4, aby ste vytvorili sieť, priradili materiál, pridali BCC a interpolovali sily na hornej a spodnej forme. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekt 4“.

### Objekt 4

Zmeňte názov objektu na **Ring** a potvrďte výber matíc (**Elastic**). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Definícia geometrie prsteňa

Vyberte ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a definujte **dutý****valec** s **3** ” ako **vnútorný priemer**, **8** ” ako **vonkajší priemer** a **3,25** ” **výškou**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Vytváranie sietí

Vygenerujte sieť s **20 000** prvkami. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Priradiť materiál pre Ring

Zo zoznamu vyberte **AISI-H-13**, aby ste priradili materiál pre krúžok. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Okrajové podmienky

Na spodnej ploche prstena stanovte okrajovú podmienku rýchlosti Vx = Vy = Vz = 0.

Nastavte **shrink****fit** na hodnotu 0,01” pozdĺž **vnútorného priemeru** **krúžku**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s polohovaním.

### Umiestňovanie objektov

Kliknite pravým tlačidlom myši v grafickom okne a vyberte možnosť „štýl merania“ > „štýl CAD v smere Z“. Vyberte bod na hornej ploche prstena a bod na hornej ploche spodnej matrice a zmerajte vzdialenosť; bude to približne 0,7499. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Zvoľte prepínač ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}), ako polohovací objekt zvoľte **prsteň** a posuňte ho o **0,7499** v smere „**-Z**“ (0,0,-0,7499). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), aby ste posunuli prsteň. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste ukončili polohovanie objektu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Získavanie kontaktov

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať vzťah), vyberte **Prsteň** ako hlavný prvok a ****Spodná****matrica**** ako podriadený prvok pre tento vzťah a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky simulácie

Nastavte **počet krokov** na **1**, **krok prírastku** **na** **uloženie** na **1** a **čas****na****krok** na **1**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť databázu

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), aby sa otvorilo dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať v spustení**, vyberte možnosť „**Pokračovať od posledného kroku**“ a potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

### Následné spracovanie

Porovnajte napätia pri prvom napäťovom cykle (bez zúžovacieho krúžku) s druhým napäťovým cyklom (so zúžovacím krúžkom). Napätia pri druhom napäťovom cykle by mali byť nižšie, ale stále pomerne vysoké. Využite vlastnosti stavových premenných a uprednostnite globálne škálovanie pred lokálnym.

Všimnite si, že napätia v krúžku sa pohybujú v rozmedzí 200 KSI alebo vyššie. Použitie ťažšieho lisovaného spojenia pravdepodobne spôsobí plastickú deformáciu krúžku.

## Mechanický lis

### Otvorenie súboru projektu

Otvorte hlavné okno grafického rozhrania DEFORM tak, ako ste to robili v predchádzajúcich cvičeniach. Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}), aby ste vytvorili nový problém. Zobrazí sa okno Nový problém. Vyberte prepínač **Integrovaný výrobný proces** a prepínač **Anglické** jednotky. Uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte nový problém s využitím integrovaného výrobného procesu Deform.

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu. Do poľa pre názov projektu zadajte názov „**StubShaft_Mechanical**“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Pridať operáciu tvarovania

Pridajte **3D tvarovaciu operáciu** zo zoznamu operácií v prehliadači. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií.

### Import databázy

Po pridaní operácie 3D tvarovania načítajte predtým simulovaný súbor **Stub_shaft_symmetry.DB**, vyberte prvý krok tretej operácie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). 

#### Definícia pohybu úderu

V stromovej štruktúre Operácie vyberte stránku Pohyb lisovacieho stroja, v Průzkumníku vyberte knižnicu pohybov a vyberte položku „mechanical_press_700_Ton_National“. Pridajte pohyb mechanického lisu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré sa nachádza pred pohybom „**mechanical_press_700_Ton_National**“ (pozri obr. 3DL5.73).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0073.jpg' | relative_url }})

Knižnica mechanických lisov

### Vytvoriť databázu

Skontrolujte údaje a vytvorte databázu. Po vytvorení databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), aby sa otvorilo dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

### Postprocesor

V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky. Prejdite si kroky, aby ste videli deformáciu.

**Sledovanie bodov:**  
Kliknite na ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) a vyberte niekoľko bodov na obrobku, ako je znázornené na obr. 3DL5.74. Kliknite na ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím sa otvorí okno na sledovanie bodov.

Potom kliknite na premennú „Teplota“. Tým sa vykreslí graf „Teplota v závislosti od času“ pre všetky body, ktoré ste vybrali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0074.jpg' | relative_url }})

Graf sledovania bodov
