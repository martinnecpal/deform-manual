---
lang: sk
title: "Laboratórium 25 – Laboratóriá s odbočkovými hriadeľmi"
---

# Laboratórium 25 – Laboratórne cvičenia s krátkymi hriadeľmi

25.1. Laboratórne cvičenie s krátkou hriadeľou pri 2D tvárnení metódou MO

25.2. Analýza namáhania nástroja

25.3. Pridanie zúžovacieho krúžku k matrici

25.4. Simulácia tepelných účinkov

25.5. Zahriaty hriadeľ s mechanickým lisovacím mechanizmom

25.6. Ohrev krátkej hriadeľovej trubice s pohybom hydraulického lisu

25.7. Zahriata šachta s pohybom skrutkového lisu

25.8. Teplá šachta so systémom „Hammer“

## Laboratórium na výrobu krátkych hriadeľov v 2D MO tvárnení

V tomto cvičení nastavíme 2 operácie:

**Operácia 1:** Operácia s kužeľom.

**Operácia 2:** Operácia hlavy.

**Operácia 1: Operácia s kužeľom**

### Vytvoriť nový problém

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main, ako je znázornené nižšie ([Fig. L25.1.]()).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavná obrazovka DEFORM GUI 

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. L25.2. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou prepínača. Názov úlohy zadajte ako „**Stub_Shaft**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. L25.3.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Stub_Shaft**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0001.jpg' | relative_url }})

Sprievodca MO – Nový projekt

### Pridávanie operácií 2D tvárnenia

Otvorí sa sprievodca viacerými operáciami s novým projektom s názvom **Stub_Shaft** na nastavenie úlohy. Zoznamu operácií v Průzkumníku pridajte **dve****2D tvárovacie operácie**. Operáciu môžete pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa 2D tvárovacej operácie (pozri obr. L25.4.) alebo ju môžete pridať aj pretiahnutím do oblasti Editoru operácií.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0002.jpg' | relative_url }})

Do editora operácií bola pridaná operácia 2D tvárnenia

### Typ geometrie

V tomto laboratórnom cvičení budeme používať osovo symetrické geometrie, preto na stránke s typmi geometrií vyberte voľbu **2D****Axisymmetric**, ako je znázornené na obr. L25.5, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0003.jpg' | relative_url }})

Výber typu osovo symetrickej geometrie

### Ovládacie prvky simulácie

V tomto cvičení ukážeme, ako nastaviť jednoduchú izotermickú úlohu. V okne „Simulation controls“ teda **odznačte** políčko **Heat****transfer****mode** (pozri obr. L25.6.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0004.jpg' | relative_url }})

Okno riadenia simulácie

### Priradenie materiálu k obrobku

V okne Zoznam materiálov načítajte materiál „**AISI-4120**“ z knižnice materiálov DEFORM v kategórii **Oceľ** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To môžete urobiť tak, ako je znázornené nižšie, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. L25.7. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Objekt.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0005.jpg' | relative_url }})

Okno „Zoznam materiálov“

### Pridávanie objektov

Na túto operáciu sme potrebovali štyri objekty, preto v okne „Objekty“ pridajte štyri objekty kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (pozri obr. L25.8.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0006.jpg' | relative_url }})

Okno na pridávanie objektov

### Obrobok

V okne „Workpiece“ (Obrobok) zmeňte názov objektu na **Billet** a ako typ objektu vyberte **Plastic**, ako je znázornené na obr. L25.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0007.jpg' | relative_url }})

Objekt „Billet“ – okno

#### Geometria polotovaru

Na stránke Geometria vyberte ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a definujte **valec** s **polomerom** **0,4** ” a **výškou** **2,7** ” (pozri obr. L25.10.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0008.jpg' | relative_url }})

Definovanie geometrie

#### Vytváranie sietí

Prepnite do expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}); predvolené nastavenia sú na vytvorenie siete postačujúce. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vytvorte sieť (pozri obr. L25.11.).

Zmerajte jeden z menších prvkov v obrobku – ich rozmery sa pohybujú v rozmedzí 0,020”. Kliknite na **kartu** **Kritériá pregenerovania siete** a nastavte hĺbku interferencie na polovicu tejto hodnoty, teda na **0,01** ”. Toto nastavenie zabraňuje nadmernému prekrývaniu medzi nástrojmi a obrobkom, keď sa materiál tečie okolo rohov (pozri obr. L25.12.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0009.jpg' | relative_url }})

Okno z mriežky z hliníkového bloku

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0010.jpg' | relative_url }})

Definovanie kritérií pre vytvorenie novej siete

#### Priradenie materiálu na výkovky

Ak chcete obrobku priradiť materiál, vyberte v okne materiálov materiál **AISI-4120**. Postupujte podľa obrázku L25.13 nižšie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0011.jpg' | relative_url }})

Okno na výber materiálu

#### Okrajové podmienky pre polotovar

Na stránke BCC zaškrtnite predvolené priradenie BCC pre deformáciu ľavej strany obrobku v smere osi X, ako je znázornené na obr. L25.14. Predvolené priradenia BCC sa nastavia automaticky na základe výberu typu úlohy ako osovo symetrickej. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Top die“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0012.jpg' | relative_url }})

Okno BCC z hliníkového bloku

### Definícia pojmu „Top Die“

Na stránke „Top Die“ zmeňte názov hornej matrice na **Punch** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Importovať geometriu dierovania

Naimportujte súbor **StubShaft_ConeTools.igs** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. L25.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), čím sa otvorí kontextové menu „Multiple boundary“ (pozri obr. L25.16). Po kliknutí na „Yes“ v tomto kontextovom menu sa otvorí okno na úpravu geometrie, ako je znázornené na obr. L25.17. **Odstráňte****smyčku 2** pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) (pozri obr. L25.18.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybmi.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0013.jpg' | relative_url }})

Import geometrie výseku

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0014.jpg' | relative_url }})

Vyskakovacie okno na prechod do úpravy geometrie

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0015.jpg' | relative_url }})

Okno „Upraviť geometriu“

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0016.jpg' | relative_url }})

Odstránenie slučky 2 z importovanej geometrie

#### Priradiť pohyb k hornej kocku

Pre toto laboratórne cvičenie nastavte **rýchlosť** **10** palcov za sekundu v smere **-Y**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Bottom Die“.

### Definícia spodnej matrice

Na stránke „Spodná forma“ nastavte typ objektu na **Tuhý** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (pozri obr. L25.19.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0017.jpg' | relative_url }})

Stránka spodnej matrice

#### Import geometrie spodnej matrice

Načítajte súbor **StubShaft_ConeTools.igs** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), čím sa otvorí kontextové menu „Viac hraníc“. Po kliknutí na „Áno“ v tomto kontextovom menu sa otvorí okno na úpravu geometrie. **Odstráňte****slučku 1** pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) (pozri obr. L25.20.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Object 4.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0018.jpg' | relative_url }})

Odstránenie Loop1 z importovanej geometrie

### Definícia ejektora

V okne „Object 4“ zmeňte názov objektu 4 na **Ejector** a ako typ objektu vyberte **Rigid**, ako je znázornené na obr. L25.21. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0019.jpg' | relative_url }})

Okno objektu Ejector

#### Geometria vyhadzovača

V okne „Geometria vyhadzovača“ vyberte ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}), čím sa otvorí okno na úpravu geometrie, a do tabuľky zadajte geometrické body tak, ako je znázornené na obr. L25.22. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka „Ovládacie prvky“.

**X** |  **Y** |  **R**  
---|---|---  
0 |  -2 |  0  
0,406 |  -2 |  0  
0,406 |  0 |  0  
0 |  0 |  0  
  
Údaje o geometrii vyhadzovača

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0020.jpg' | relative_url }})

Definovanie geometrie vyhadzovača

### Ovládacie prvky

Uistite sa, že obrobok je priložený k vyhadzovaču, spodná matrica je umiestnená voči obrobku a razník je priložený k obrobku, pozri obr. L25.23. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Kontakt“. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0021.jpg' | relative_url }})

Umiestnenie objektov

### Získavanie kontaktov

Vyberte typ kontaktu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom, razníkom, spodnou matricou a vyhadzovačom, ako je znázornené na obr. L25.24. Keďže matrice sú tuhé a polotovar je plastický, razník, spodná matrica a vyhadzovač sa považujú za hlavné prvky a polotovar za podriadený prvok. S cieľom predpovedať ohyb počas deformácie sa polotovaru priradí vlastný kontakt.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0022.jpg' | relative_url }})

Stránka na získavanie kontaktov

Zvýraznite vzťah **Punch – Billet** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej trenie (pozri obr. L25.25.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže táto simulácia prebieha pri izbovej teplote a formy sú oceľové, použite roletové menu a zo zoznamu vyberte možnosť **Tvárnenie za studena (oceľové formy)**. Hodnota trenia **0,12** sa nastaví automaticky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0023.jpg' | relative_url }})

Okno definície údajov medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna kontaktu. Keďže podmienky trenia sú pre všetky páry objektov rovnaké, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie 0,12. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určite vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,00040"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Prejdite na kartu Správy alebo sledujte stavový riadok, aby ste zistili informácie o vytvorených kontaktoch. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky na zastavenie

Chceme simuláciu zastaviť v momente, keď sa razník a matrica nachádzajú vo vzdialenosti do 0,025” od seba. Na obrazovke „Stopping Controls“ kliknite na riadený režim ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) a **zaškrtnite** možnosť **Vzdialenosť medzi objektmi**. Nastavte hodnotu tejto vzdialenosti na **0,025** ” v smere **Y**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) vedľa **Objektu 1** a kliknite na spodnú časť objektu razníka na displeji. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) vedľa **Objektu 2** a kliknite na hornú časť objektu Spodná matrica na displeji (pozri obr. L25.26.), kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na ďalšiu stránku.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0024.jpg' | relative_url }})

Okno „Ovládacie prvky zastavenia“

### Ovládacie prvky krokov

Chceme, aby sa razník posunul o 0,5” v **100****krokoch**, takže každý krok bude 0,5/100, teda 0,005”. V okne „Step Controls“ zadajte definíciu krokov riešenia ako „With Equal **Die****Displacement** of **0,005**.” Nastavte **počet simulačných krokov** na **100** a **krok pre uloženie** na 5. Nastavte razník ako primárny lisovací nástroj, ak sa nevybral automaticky (pozri obr. L25.27.), kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0025.jpg' | relative_url }})

Okno „Ovládacie prvky krokov“

### Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) a prejdite k ďalšej operácii.

**Operácia 2: Operácia na hlave.**

### Typ geometrie

Na stránke s typmi geometrie vyberte **2D****Osovo symetrické****polomer** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky simulácie

V okne „Simulation controls“ **zrušte zaškrtnutie** políčka **Heat****transfer****mode**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objects“.

### Pridávanie objektov

Na túto operáciu sme potrebovali štyri objekty; štandardne sú do zoznamu objektov pridané štyri objekty z predchádzajúcej operácie. Ak objekty neboli pridané automaticky, pridajte štyri objekty kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (pozri obr. L25.28.), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0026.jpg' | relative_url }})

Okno na pridávanie objektov

### Definícia obrobku

Objekt „Workpiece“ nastavíme ako „Read Form DB“. Na stránke „Workpiece“ vyberte voľbu „Read from DB“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Top Die“. (Pozri obr. L25.29.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0027.jpg' | relative_url }})

Stránka objektu obrobku

### Definícia pojmu „Top Die“

Na stránke „Top Die“ zmeňte typ objektu z „Read from DB“ na **Rigid** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import geometrie dierovania:

Načítajte súbor **StubShaft_HeadTools.igs** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. L25.30. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), čím sa otvorí kontextové menu „Viac hraníc“. Po kliknutí na „Áno“ v tomto kontextovom menu sa otvorí okno na úpravu geometrie. **Odstráňte slučku 1** pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) (pozri obr. L25.31) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybmi.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0028.jpg' | relative_url }})

Načítať geometriu dierovania

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0029.jpg' | relative_url }})

Okno „Upraviť geometriu“

#### Priradiť pohyb k hornej kocky

Pre toto laboratórne cvičenie nastavte **rýchlosť** **10** palcov za sekundu v smere **-Y**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom Die“.

### Definícia spodnej matrice

Na stránke „Bottom die“ zmeňte typ objektu z „Read from DB“ na **Rigid****** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import geometrie spodnej matrice

Načítajte súbor **StubShaft_HeadTools.igs** pomocou tlačidla „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) otvoríte kontextové menu „Viac hraníc“. Po kliknutí na „Áno“ v tomto kontextovom menu sa otvorí okno na úpravu geometrie. **Odstráňte slučku 2** pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) (pozri obr. L25.32.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ejector“ (Vysúvač).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0030.jpg' | relative_url }})

Odstránenie Loop2 z importovanej geometrie

### Definícia ejektora

Objekt Ejector nastavíme ako „Čítanie z databázy“. Na stránke Ejector vyberte voľbu „Čítanie z databázy“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Polohovanie“.

### Polohovanie

Na stránke „Polohovanie objektu“ nastavte polohu **razníka** pomocou **posunu****polohovania** (x = 0, y = 2) v smere osi Y (pozri obr. L25.33.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Plánované polohovanie“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0031.jpg' | relative_url }})

Nastavenie polohy razníka

### Plánované polohovanie

Pomocou polohovania na základe interferencie nastavujeme polohu razníka voči obrobku. Na stránke **Plánované polohovanie** kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte volič ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte **Polohovaný objekt** na **Vrták** a **Referenciu** na **Polotovar**. Zmeňte smer priblíženia na **-Y** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (Pozri obr. L25.34.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0032.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Získavanie kontaktov

Definujte vzťahy medzi kontaktmi pomocou rovnakých nastavení, aké sme definovali pre prvú operáciu, pozri 25.1.12. Vytvorenie kontaktov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky na zastavenie

Chceme simuláciu zastaviť, keď sa razník a sochor nachádzajú vo vzdialenosti do 0,401” od seba. Na obrazovke „Stopping Controls“ zaškrtnite možnosť **Vzdialenosť medzi objektmi**. Nastavte hodnotu tejto vzdialenosti na **0,401** ” v smere Y. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) vedľa **Objektu 1** a kliknite na objekt **Razník**, ako je znázornené na obr. L25.35. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) vedľa **Objektu 2** a kliknite na objekt **Matrica**, ako je znázornené na obr. L25.35.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0033.jpg' | relative_url }})

Ovládanie zastavenia na základe vzdialenosti medzi objektmi

Pre túto súčiastku tiež určíme maximálne zaťaženie. Zaškrtnite možnosť **Max. zaťaženie**. Nastavte maximálne zaťaženie na X = 0, Y = 600, ako je znázornené na obr. L25.36. Ak teraz zaťaženie lisu prekročí hodnotu 600 Klb (300 ton), simulácia sa zastaví, aj keď ešte nebola dosiahnutá vzdialenosť medzi nástrojmi. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0034.jpg' | relative_url }})

Stránka ovládacích prvkov zastavenia

### Ovládacie prvky krokov

Odhadnite celkový zdvih razníka, ktorý bude približne 1,25”. Zdvih na jeden krok ponecháme na hodnote **0,005**”, takže simulácia bude vyžadovať približne 250 krokov (1,25/0,005). Nastavte **Počet simulačných krokov** na **250.** (Pozri obr. L25.37.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0035.jpg' | relative_url }})

Okno „Ovládacie prvky krokov“

### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“; ak sa zobrazí chyba zadávania údajov, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto laboratórnej úlohy by sa mala zobraziť správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa v čase spustenia.“

Uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia, ako je znázornené na obr. L25.38. Pomocou predvolenej možnosti **Pokračovať v behu** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0060.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Keď simulácia prebehne bez problémov, skontrolujte správy v súbore LOG; po dokončení všetkých operácií sa v súbore LOG objaví správa: „MULTIPLE OPERATION COMPLETED“.

### Následná spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

#### Premenné stavu:

V zozname stavových premenných kliknite na ikonu **Efektívne deformácie**, aby ste znázornili veľkosť deformácie, ktorá pôsobila na obrobok. Ak chcete zmeniť nastavenia grafu, môžete kliknúť na ikonu Nastavenie ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}). Na tejto obrazovke môžete zobraziť rôzne druhy kontúr (čiarové, tieňované alebo plné) a tiež zmeniť rozsah premenných, ktorý sa zobrazuje na kontúrovej lište. Pomocou možnosti Nastavenia si môžete rozsah kontúrovej lišty definovať podľa vlastných potrieb. Neváhajte experimentovať so zobrazením rôznych stavových premenných a možnosťami grafu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0036.jpg' | relative_url }})

Graf závislosti napätia od deformácie

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0037.jpg' | relative_url }})

Graf pôsobenia napätia

#### Flownet

Pomocou programu Flownet je možné vytvoriť mriežku na počiatočnom tvare obrobku a následne sledovať deformáciu tejto mriežky v priebehu simulácie.

Kliknutím na ikonu Flownet ![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}) otvoríte dialógové okno Flownet.

Začneme s **obdĺžnikovou** sieťou Flownet. Vyberte „**Grid**“ a kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). Nastavte „**Spacing**“ na hodnotu **0,1** v smere X a **1** v smere Y. Kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_preview_button.jpg' | relative_url }}) si zobrazenie mriežky. Potom kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). Keďže nebudeme ukladať žiadne údaje, kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}). Po výpočte siete Flownet spustite simuláciu a sledujte jej vývoj (pozri obr. L25.41.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0038.jpg' | relative_url }})

(a) Mriežka Flownet v prvom kroku druhej operácie. (b) Mriežka Flownet v poslednom kroku druhej operácie

## Analýza napätí v nástroji

### Otvorenie súboru projektu

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou prepínača. Názov úlohy zadajte ako „**StubShaft_ToolStress**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém pomocou integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. L25.42.), v tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**StubShaft_ToolStress**“. Zaškrtnite tlačidlo „Kopírovať existujúci projekt“, kliknite na tlačidlo prehľadávania zdrojovej lokality a naimportujte súbor **Stub_Shaft.moproj** z predtým simulovaného projektu Stub_shaft, **zaškrtnite** políčko **Kopírovať****Databázu** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pre otvorenie okna na pomenovanie projektu. Simulácia Stub_shaft sa importuje do projektu „StubShaft_ToolStress“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0039.jpg' | relative_url }})

Kopírovanie projektu „Stub_Shaft“ pomocou možnosti „Kopírovať projekt“

### Pridať operáciu s napätím v matrici

Zo zoznamu operácií v prehliadači vyberte operáciu „Die stress 2D“ a pridajte ju kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}). Operáciu môžete pridať aj pretiahnutím do editora operácií. Teraz v editore operácií vyberte operáciu „Die stress 2D“.

### Pridať objekty 

Na túto operáciu sme potrebovali tri objekty, preto ponechajte objekty „Obrobok“, „Horná matrica“ a „Spodná matrica“ a objekt „Vysúvač“ odstráňte pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Objekt1

Pre objekt 1 je štandardne zaškrtnuté políčko „Obrobok (načítať objekt z databázy)“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Horná matrica

V prípade položky „Top Die“ je štandardne zaškrtnuté tlačidlo „Dies (Elastic)“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Mesh“.

#### Generovanie sietí

Vytvorte sieť s **2000** prvkami. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Materiál.

#### Priradiť materiál pre hornú matricu

Naimportujte materiál matrice **AISI-D3** z knižnice materiálov. Zo zoznamu vyberte **AISI-D3**, aby ste tento materiál priradili hornej matrici. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku BCC.

#### Nastaviť okrajovú podmienku pre hornú formu

Ďalej musíme na hornú matricu aplikovať okrajové podmienky, aby neodletela do vesmíru, keď na ňu pôsobia formovacie zaťaženia. Nastavte okrajovú podmienku Vy = 0 na hornom okraji hornej matrice. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Vynútiť interpoláciu“.

#### Interpolácia s vynútením

Po vytvorení siete je potrebné interpolovať formovacie zaťaženia z obrobku na hornú matricu. Silu interpolujte kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Spodná matrica“.

### Spodná matrica

V prípade spodnej matrice je štandardne zaškrtnuté políčko „Matrice (pružné)“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Mriežka“. 

#### Generovanie siete

Vytvorte sieť s **2000** prvkami. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Materiál.

#### Priradiť materiál pre spodnú formu

Zo zoznamu vyberte **AISI-D3**, aby ste priradili materiál pre spodnú formu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku BCC.

#### Nastavenie okrajovej podmienky pre spodnú formu

Ďalej musíme na spodnú matricu aplikovať okrajové podmienky, aby neodletela do vesmíru, keď na ňu pôsobia tvárniace zaťaženia.

Na spodnom okraji spodnej formy nastavte okrajovú podmienku Vy = 0. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím otvoríte stránku „Vynútiť interpoláciu“.

#### Interpolácia s vynútením

Po vytvorení siete je potrebné interpolovať formovacie zaťaženia z obrobku na spodnú formu. Silu interpolujte kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazia ovládacie prvky simulácie.

### Ovládacie prvky simulácie

Nastavte **počet****krokov****na** **1**, **prírastok kroku na uloženie** ako **1** a **čas na krok** ako **1**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvorenie databázy

Kliknutím na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) skontrolujte problém. Vytvorte databázu kliknutím na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

### Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať v spúšťaní**, vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

### Následné spracovanie

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

Pomocou možnosti „Stavová premenná“ vyneste do grafu efektívne napätie a maximálne hlavné napätie.

Ak efektívne napätie prekročí medzu tečnosti materiálu, dôjde k plastickej deformácii nástrojov.

Ak je maximálne hlavné napätie veľké, môže to byť miesto, kde dôjde k vzniku únavového poškodenia.

U karbidových nástrojov môžu kladné hlavné napätia, aj keď sú relatívne malé, naznačovať začiatok únavového zlyhania.

Všimnite si, že v tejto simulácii je efektívne napätie mimoriadne vysoké.

## Pridanie zúžovacieho krúžku na lisovaciu formu

Po dokončení následného spracovania sa vráťte do režimu predspracovania kliknutím na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

### Pridať operáciu s napätím pri lisovaní

Zo zoznamu operácií v prehliadači vyberte operáciu „Die stress 2D“ a pridajte ju kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}). Operáciu môžete pridať aj pretiahnutím myšou do editora operácií.

Teraz v editore operácií vyberte pridanú operáciu „Die stress 2D“.

###  Pridať objekty

Na túto operáciu sme potrebovali štyri objekty, preto v okne „Objekt“ pridajte ďalší objekt kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka „Objekt 4“. 

### Definícia kruhu

Na stránke Object4 zmeňte názov objektu na **Ring** a potvrďte typ objektu **Dies (Elastic)**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Definícia geometrie puzdra

Vyberte ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a definujte **dutý****valec** s **vnútorným****polomerom** **1,5** ", **vonkajším polomerom** **3,5** " a **výškou** **3,25** ”, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa zobrazila stránka „Mesh“ (Sieťovanie).

#### Vytváranie sietí

Vytvorte sieť s 2000 prvkami. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

#### Priradiť materiál k prípadu

Zo zoznamu vyberte **AISI-D3**, aby ste priradili materiál pre krúžok. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Okrajové podmienky

Nastavte rýchlosť Vy = 0 pozdĺž spodného okraja prstena.

Nastavte termické sťahovanie na hodnotu 0,007” pozdĺž vnútorného priemeru krúžku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Polohovanie“.

### Umiestňovanie objektov

Pomocou funkcie **offset** s nastavením **Dva body** nastavte **krúžok** ako **polohovací objekt**. Kliknite na **spodný vnútorný roh prstena** a potom na **spodný vonkajší roh spodnej formy**. Funkcia DEFORM by mala vybrať body od (1,5; 0) do (1,5; -0,75). Ak sa v okne polohovania objektov nezobrazujú presne tieto hodnoty, upravte ich tak, aby boli presné. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) presuňte prstenec. Potom kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) ukončite polohovanie objektov. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Kontakt.

### Získavanie kontaktov

Spodnú matricu nastavíme ako podriadený objekt a krúžok ako nadradený objekt. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáme **krúžok** \- **Spodná forma**, vyberte **Hlavný objekt** ako **Prsteň** a **Podriadený objekt** ako **Spodná forma**, nastavte hodnotu trenia na **0,12** a vytvorte kontakt kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_button.jpg' | relative_url }}). Užívateľ by mal vidieť líniu bodiek pozdĺž hranice. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky simulácie

Nastavte počet krokov na 1, krok prírastku na 1 a čas na jeden krok na 1. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte stránku databázy. 

### Vytvoriť databázu

Kliknutím na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) skontrolujte problém. Vytvorte databázu kliknutím na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

### Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte možnosti spustenia. Použite predvolenú možnosť **Pokračovať v spustení**, vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

### Následné spracovanie

Porovnajte napätia pri prvom napäťovom cykle (bez zmršťovacieho krúžku) s napätiami pri druhom napäťovom cykle (so zmršťovacím krúžkom). Napätia pri druhom napäťovom cykle by mali byť nižšie, ale stále pomerne vysoké. Využite vlastnosti stavových premenných a použite globálne, nie lokálne škálovanie.

Všimnite si, že napätia v tomto prípade sú rádovo 1000 KSI alebo vyššie. Použitie ťažšieho lisovaného spojenia pravdepodobne spôsobí, že prstenec dosiahne medzu plasticity.

## Simulácia tepelných účinkov

V nasledujúcej simulácii zopakujeme tento proces ako kovanie za tepla. Simulovať budeme prenos tepla z kovanej súčiastky na matricu a úder pri kužeľovom kovaní.

### Preprava letecky

#### Otvorenie súboru projektu

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno programu DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou prepínača. Názov úlohy zadajte ako „**Stub_shaft_Warm**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu (pozri obr. L25.43.). Do poľa s názvom projektu v tejto relácii zadáme ako názov projektu „****Stub_shaft_Warm****“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0040.jpg' | relative_url }})

Problém s definovaním okna

#### Pridať operácie

Pridajte dve operácie **2D prenos tepla** a **jednu****2D tvarovanie** zo zoznamu operácií v Průzkumníku, ako je znázornené na obr. L25.44. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa príslušnej operácie alebo ju môže používateľ pridať aj pretiahnutím a umiestnením do oblasti Editor operácií.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0041.jpg' | relative_url }})

Pridávanie operácií

#### Import databázy

Po pridaní všetkých troch operácií naimportujte predtým simulovaný súbor **Stub_Shaft**.**DB**, vyberte prvý krok a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), ako je znázornené na obr. L25.46.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0042.jpg' | relative_url }})

Import databázy

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0043.jpg' | relative_url }})

Okno výberu kroku

#### Typ geometrie

V tomto cvičení budeme používať osovo symetrické geometrie, preto na stránke s typmi geometrií vyberte políčko **2D****Axisymmetric** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (Pozri obr. L25.47.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0003.jpg' | relative_url }})

Výber typu osovo-symetrickej geometrie

#### Výber typu prenosu tepla

Pre prvý prevádzkový režim vyberte typ prenosu tepla „**Prenos vzduchom**“, ako je znázornené na obr. L25.48. Týmto sa nastavia predvolené nastavenia prenosu tepla pre režim kúrenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0044.jpg' | relative_url }})

Výber typu prenosu tepla pre prevádzku ohrevu v peci

#### Nastavenie podmienok procesu

Nastavte **čas ohrevu** na **5** **sekúnd** pri teplote pece alebo okolitej teplote 68 °F, ako je znázornené na obr. L25.49, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0045.jpg' | relative_url }})

Okno s podmienkami procesu

#### Vybrať ovládacie prvky simulácie

Nechajte zaškrtnutý **len režim prenosu tepla**, pretože sa modeluje iba prenos tepla, ako je znázornené na obr. L25.50, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Billet“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0046.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre vykurovanie pece

#### Definícia pojmu „billet“

V okne „Billet object“ (Objekt sochory) potvrďte typ objektu ako „**Plastic**“ a zmeňte teplotu objektu na **1750°F**, ako je znázornené na ****obr. L25.51. Použijeme rovnakú geometriu a sieť ako v simulácii tvárnenia za studena. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Punch“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0047.jpg' | relative_url }})

Stránka s definíciou pojmu „billet“

#### Vysvetlenie pojmu „punch“

Na stránke „Punch“ nastavte premennú „temp“ na hodnotu **300F** a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Mesh“.

##### Generovanie siete

Vytvorte sieť pre existujúcu geometriu. Vytvorte sieť s predvoleným počtom prvkov (pozri obr. L25.52.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Materiál.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0048.jpg' | relative_url }})

Vytvorenie siete Punch Mesh

##### Priradenie materiálu pre razník

Naimportujte materiál na výrobu foriem AISI-H-13 z knižnice materiálov. Zo zoznamu vyberte **AISI-H-13**, aby ste tento materiál priradili k razníku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Pohyb“.

##### Vymazanie definície pohybu

Odstráňte existujúci pohyb razníka pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_folder_icon.jpg' | relative_url }}) na hornej stránke pohybu razníka. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka spodného razníka.

#### Definícia spodnej matrice

Na stránke „Bottom die“ nastavte hodnotu premennej temp na **300F** a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Mesh“.

##### Generovanie sietí

Vytvorte sieť pre existujúcu geometriu. Vytvorte sieť s predvoleným počtom prvkov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Materiál“.

##### Priradenie materiálu pre spodnú matricu

Zo zoznamu vyberte **AISI-H-13**, aby ste priradili materiál pre spodnú formu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ejector“.

#### Definícia ejektora

Na stránke „Ejector“ nastavte pre objekt „temp“ hodnotu **300F** a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Mesh“.

##### Vytváranie sietí

Vygenerujte sieť pre existujúcu geometriu. Vygenerujte sieť s predvoleným počtom prvkov. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Materiál“.

##### Priradenie materiálu pre vyhadzovač

Zo zoznamu vyberte **AISI-H-13**, aby ste priradili materiál pre vyhadzovač. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Polohovanie“.

#### Polohovanie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Pomocou ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) posuňte **razník****3** palce v smere „Y“. Posuňte tiež **obrobok** o **2** palce v smere „Y“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím opustíte menu polohovania. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno Step controls.

#### Riadenie krokov

Nastavte **počet simulačných krokov** na **50** s dĺžkou každého kroku 0,1 s a ukladaním každých **5** krokov (pozri obr. L25.53.). Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0049.jpg' | relative_url }})

Nastavenia ovládacích prvkov krokov

#### Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastaveniach úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) a prejdite k ďalšej operácii.

### Odpočinok na čipe

#### Výber typu prenosu tepla

Pre druhú operáciu vyberte typ **Rest on die transfer**. Tým sa nastavia predvolené nastavenia prenosu tepla pre operáciu ohrevu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

#### Nastavenie podmienok procesu

Nastavte **doba odpočinku** na **1** sekundu pri teplote okolia 68**°** F, ako je znázornené na obr. L25.54, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0050.jpg' | relative_url }})

Okno s podmienkami procesu

#### Vybrať ovládacie prvky simulácie

Nechajte **zaškrtnutý** iba **režim prenosu tepla**, keďže sa modeluje iba prenos tepla, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Definovanie objektov

V predvolenom nastavení budú všetky objekty v režime „Čítanie z databázy“; potvrďte predvolené typy objektov a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka s plánovaním polohovania.

#### Plánované umiestnenie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a pomocou možnosti polohovania ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) nastavte polohu **surového kusu** voči **vyhadzovaču** v smere „-Y“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Získavanie kontaktov

Vyberte kontakt typu **užívateľ**, dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať vzťah) a pre prvý vzťah vyberte **Spodok******matrica** ako **hlavný** a **sústružný polotovar** ako **podriadený** pre prvý vzťah a pre druhý vzťah vyberte **vyhadzovač** ako hlavný a **sústružný polotovar** ako podriadený, ako je znázornené na obr. L25.55.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0051.jpg' | relative_url }})

Vzťah medzi obrobkom a spodnou matricou

Kliknite na tlačidlo vzťahu **Spodná matrica – polotovar** ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Upraviť) a v sekcii „Teplo“ vyberte z roletového menu možnosť „**Voľný odpočinok**“, čím definujete koeficient prenosu tepla medzi objektmi, ako je znázornené na obr. L25.56. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno Úpravy. Následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste skopírovali vlastnosti rozhrania z prvého vzťahu do ostatných vzťahov. Tým sa počas simulácie vytvorí kontakt medzi objektmi na začiatku fázy odpočinku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno ovládania krokov.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0052.jpg' | relative_url }})

Výber koeficientu prenosu tepla medzi objektmi v stave pokoja

#### Riadenie krokov

Nastavte **počet simulačných krokov** na **50**, pričom dĺžka každého kroku je **0,1** s, a uložte výsledky každých **5 krokov**. Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_explorer_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy vytvárania databázy.

#### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“. Ak sa zobrazí hlásenie „Input error“, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto série cvičení by sa mala zobraziť správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“ Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

###  Prevádzka formovacieho kužeľa

Pre operáciu tvarovania **zaškrtnite** políčko **Deformácia** spolu s políčkom **Prenos tepla** na stránke Ovládacie prvky simulácie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Definovanie objektov

Na stránke „Objekty“ sú štandardne v zozname pridané všetky štyri objekty. Ak tomu tak nie je, pridajte štyri objekty pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) a na stránke každého objektu nastavte všetky štyri objekty ako objekty typu „Načítané z databázy“. (Pozri obr. L25.57.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0053.jpg' | relative_url }})

Stránka „Objekty“

#### Vysvetlenie pojmu „punch“

**Vysvetlenie pohybu úderu**  
Nastavte pre objekt „Punch“ **rýchlosť** **10** palcov za sekundu v smere **-Y**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Scheduled positioning“.

#### Plánované polohovanie

Na stránke „Plánované polohovanie“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a vyberte „**Polohovanie******objekt**“ ako **Vykrajovanie**, metódu ako „**Interferencia**“ vo vzťahu k „**Sochoru**“ v smere **-Y**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

#### Získavanie kontaktov

Vyberte kontakt typu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi surovcom, razníkom, spodnou maticou a vyhadzovačom. Keďže matice sú tuhé a surovec je plastový, horná a spodná matica sa považujú za hlavné a surovec za podriadený.

Zvýraznite vzťah **Punch – Billet** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej treniu (pozri obr. L25.58.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže ide o simuláciu tvárnenia za tepla a formy sú z ocele, použite roletové menu a zo zoznamu vyberte možnosť **Tvárnenie za tepla**. Hodnota trenia **0,25** sa vyberie automaticky. Prejdite na **kartu „Thermal“****** a v časti „Forming“ vyberte z roletového menu možnosť „**Forming**“, čím definujete koeficient prenosu tepla medzi objektmi.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0054.jpg' | relative_url }})

Okno na definovanie koeficientu trenia medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“; keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy trenie **0,25** a prenos tepla cez rozhranie **0,004**, ako je znázornené na obr. L25.59. Keďže sa kontakt inicializuje a vytvorí počas generovania databázy, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a pokračujte.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0055.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre formovaciu operáciu

#### Ovládacie prvky na zastavenie

Nastavte ovládacie prvky zastavenia podľa pokynov uvedených v časti „Ovládacie prvky zastavenia“ 25.1.13.

#### Ovládacie prvky krokov

Nastavte ovládacie prvky krokov podľa pokynov uvedených v časti Ovládacie prvky krokov 25.1.14.

#### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“. Ak sa zobrazí chyba zadávania údajov, skontrolujte chýbajúce údaje a doplňte ich. V rámci tejto série cvičení by sa mala zobraziť správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“

#### Spustenie simulácie

Prepnite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

#### Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

skontrolujte zaťaženie v postprocesore. 

Ako sa zaťaženie líši v porovnaní s prípadom tvárnenia za studena?

Merajte teplotu v niekoľkých bodoch v hornej časti dielu. Ako sa mení teplota počas tvarovania dielu?

## Hriadeľ s teplým výstupkom a mechanickým lisovacím mechanizmom

### Otvorenie súboru projektu

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrated Manufacturing Process**“ a ako systém jednotiek zvoľte „**English**“ pomocou prepínača. Názov úlohy zadajte ako „**StubShaft_Mechanical**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak toto políčko nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu (pozri obr. L25.60.). Do poľa pre názov projektu použijeme v tejto relácii názov „****StubShaft_Mechanical****“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0056.jpg' | relative_url }})

Problém s definovaním okna

### Pridať operáciu tvarovania

  
Pridajte operáciu 2D tvárnenia zo zoznamu operácií v prehliadači. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií.

### Import databázy

Po pridaní operácie 2D tvárnenia načítajte predtým simulovaný súbor **Stub_shaft_Warm.DB**, vyberte **prvý krok tretej operácie** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Pohyb razníka“.

### Vysvetlenie pojmu „punch“

**Definícia pohybu úderu**

Ako typ pohybu vyberte **Mechanický lis**. Celkový zdvih predstavuje pohyb piestu od horného mŕtveho bodu po dolný mŕtvy bod (alebo zozadu dopredu v prípade horizontálneho lisu).

Určíme **celkový zdvih** na **10**”.

Zdvih kováčskej lisovacej hlavy je vzdialenosť, ktorú prekoná razník od okamihu dotyku s obrobkom až po dosiahnutie dolnej mŕtvej polohy. V tejto simulácii bude **zdvih kováčskej lisovacej hlavy** **0,5** ”.

Počet cyklov za sekundu predstavuje rýchlosť zotrvačníka. Pri hlave alebo lise bez spojky sa táto hodnota rovná počtu cyklov za sekundu lisu. Pri lise so spojkou sa vypočíta ako otáčky zotrvačníka za minútu / 60 otáčok za sekundu alebo cyklov za sekundu.

Nastavíme hodnotu **1,1 cyklu za sekundu**.

Zvyšné nastavenia ponecháme tak, ako boli importované. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka „DB Generation“.

### Vytvoriť databázu

Skontrolujte údaje a vytvorte databázu. Po vytvorení databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

### Postprocesor

V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky. Prejdite si kroky, aby ste videli deformáciu.

Prejdite na graf „load-stroke ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }})“ a vyneste rýchlosť razníka v závislosti od času. Vyneste záťaž v závislosti od času.

Používateľ môže porovnať maximálne zaťaženie vypočítané na základe modelu lisu s maximálnym zaťažením vypočítaným pomocou aproximácie s konštantnou rýchlosťou.

## Hriadeľ s teplým výstupkom a hydraulickým pohonom lisu

### Otvorenie súboru projektu

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou prepínača. Názov úlohy zadajte ako „**StubShaft_Hydraulic**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu (pozri obr. L25.61.). Do poľa pre názov projektu v tejto relácii zadáme názov „****StubShaft_Hydraulic****“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0057.jpg' | relative_url }})

Problém s definovaním okna

### Pridať operáciu tvarovania

Pridajte operáciu 2D tvárnenia zo zoznamu operácií v prehliadači. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií.

### Import databázy

Po pridaní operácie 2D tvárnenia naimportujte predtým simulovaný súbor **Stub_shaft_Warm.DB**, vyberte **prvý krok tretej operácie** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Punch Movement“ (Pohyb razníka).

### Definícia pohybu úderu

Ako typ pohybu vyberte **Hydraulický lis**. Pre túto simuláciu zaškrtnite políčko „Obmedzenie výkonu“, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) a zadajte nasledujúce hodnoty.

**Sila** |  **Rýchlosť**  
---|---  
0 |  1,5  
20 |  1,3  
25 |  1,1  
30 |  0,7  
35 |  0,25  
38 |  0  
  
To znamená, že maximálna rýchlosť lisu – bez zaťaženia – je 1,5 palca za sekundu.

Maximálne zaťaženie lisu je 38 Klb v poslednom kroku (rýchlosť zastavenia).

Pri 25 Klb dokáže lis udržiavať rýchlosť 1,1 in/sec.

Upozorňujeme, že tieto hodnoty zaťaženia sú vytvorené len na ilustráciu správania lisu v tomto návode. Zaťaženia sú pomerne malé.

Nastavte **konštantnú rýchlosť** na **1,5** palca/sek.

Zvyšné nastavenia ponecháme tak, ako boli importované. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste definíciu zatvorili, a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „DB Generation“.

### Vytvoriť databázu

Skontrolujte údaje a vytvorte databázu. Po vytvorení databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }})...

### Postprocesor

V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobrazili všetky kroky. Prejdite si kroky, aby ste videli deformáciu.

Prejdite na graf zaťaženia a zdvihu a znázornite rýchlosť razníka v závislosti od času. Znázorňte zaťaženie v závislosti od času.

Používateľ môže porovnať maximálne zaťaženie vypočítané pomocou modelu lisu s maximálnym zaťažením vypočítaným pomocou aproximácie s konštantnou rýchlosťou.

## Zahriaty hriadeľ s posuvom pomocou skrutkového lisu

### Otvorenie súboru projektu

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou prepínača. Názov úlohy zadajte ako „**StubShaft_Screw**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu pomocou integrovaného výrobného procesu Deform.

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu (pozri obr. L25.62.). Do poľa pre názov projektu v tejto relácii zadáme ako názov projektu „****StubShaft_Screw****“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0058.jpg' | relative_url }})

Problém s definovaním okna

### Pridať operáciu tvarovania

Pridajte operáciu 2D tvarovania zo zoznamu operácií v prehliadači. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií.

### Import databázy

Po pridaní operácie 2D tvárnenia naimportujte predtým simulovaný súbor **Stub_shaft_Warm.DB**, vyberte **prvý** krok tretej operácie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vysvetlenie pojmu „punch“

**Definícia pohybu úderu**

Ako typ pohybu vyberte **Šnekový lis**.

Uveďte:

**Energia** = **9** Klb-in  
**Moment zotrvačnosti** = 0,125 Klb-in-s²  
**Krok vodiacich skrutiek** = 5 palcov/otáčka  
**Účinnosť** = 0,8  
Zvyšné nastavenia ponecháme tak, ako boli importované. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „DB Generation“.

### Vytvoriť databázu

Skontrolujte údaje a vytvorte databázu. Po vytvorení databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}).

### Postprocesor

V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky. Prejdite si jednotlivé kroky a sledujte deformáciu.

Prejdite na graf zaťaženia a zdvihu a znázornite rýchlosť razníka v závislosti od času. Znázorňte zaťaženie v závislosti od času.

Používateľ môže simuláciu spustiť znovu od začiatku s vyššou energiou.

## Hriadeľ s teplým výstupkom a kladivovým mechanizmom

### Otvorenie súboru projektu

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte voľbové tlačidlo „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou voľbového tlačidla. Názov úlohy zadajte ako „**StubShaft_Hammer**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak toto políčko nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu (pozri obr. L25.63.). Do poľa pre názov projektu v tejto relácii zadáme názov „****StubShaft_Hammer****“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0059.jpg' | relative_url }})

Problém s definovaním okna

### Pridať operáciu kovania viacerými údermi

Pridajte operáciu **2D Multi Blow Forging** zo zoznamu operácií v prehliadači. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií.

###  Import databázy

Po pridaní operácie 2D Multi Blow Forging naimportujte predtým simulovaný súbor **Stub_shaft_Warm.DB**, vyberte **prvý krok tretej operácie** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Vysvetlenie pojmu „punch“

**Definícia pohybu úderu**  
Ako typ pohybu vyberte **Hammer**.

Nastavte ovládacie prvky pre Hammer.

Sada:

**Energia** = **6** Klb-in  
**Hmotnosť** = **0,03** Klb-s²/in

### Tabuľka výdychov

Na stránke **Tabuľka úderov** nastavte účinnosť na hodnotu 0,5 a počet zásahov na 4.

Zvyšné nastavenia ponecháme tak, ako boli importované. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „DB Generation“.

### Vytvoriť databázu

Skontrolujte údaje a vytvorte databázu. Po vytvorení databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

**Poznámka**: Ak sa počas simulácie splnia kritériá na ukončenie, ďalšie operácie sa nebudú simulovať.

### Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa simulácia spustí.

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}).

### Postprocesor

V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky. Prejdite si jednotlivé kroky a sledujte deformáciu.

Prejdite na graf zaťaženia a zdvihu a znázornite rýchlosť razníka v závislosti od času. Znázorňte zaťaženie v závislosti od času.

Používateľ môže simuláciu spustiť znova od začiatku s vyššou energiou.
