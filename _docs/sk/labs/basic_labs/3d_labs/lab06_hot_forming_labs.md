---
lang: sk
title: "Lab06 – Laboratóriá pre tvárnenie za tepla"
---

# Lab06 – Laboratórne cvičenia z tvárnenia za tepla

V tomto laboratórnom cvičení nastavíme operáciu kovania typu „Tee“ pomocou operácie MO Forming.

  
Laboratórium 1. Operácia 1: Operácia lisovania

1.1. Vytvorenie nového problému

1.2. Pridanie operácie 3D tvarovania

1.3. Ovládacie prvky simulácie

1.4. Pridávanie objektov

1.5. Obrobok

1.6. Import geometrie obrobku

1.7. Vytvorenie siete obrobku

1.8. Priradiť materiál k obrobku

1.9. Definícia hornej matrice

1.10. Import geometrie hornej matrice

1.11. Priradiť pohyb hornej matrice

1.12. Definícia spodnej matrice

1.13. Import geometrie spodnej formy

1.14. Polohovanie objektov

1.15. Definícia kontaktu (vzťah medzi objektmi)

1.16. Definícia ovládacích prvkov na zastavenie

1.17. Ovládacie prvky krokov

1.18. Vytvorenie databázy

1.19. Spustenie simulácie

1.20. Následná úprava po operácii zhutňovania

Laboratórium 2. Operácia 2 – Dokončenie operácie v kováčskej dielni

2.1. Pridanie a definovanie druhej operácie

2.2. Plánované umiestnenie

2.3. Definícia vzťahu (vzťah medzi objektmi)

2.4. Ovládacie prvky na zastavenie

2.5. Ovládacie prvky krokov

2.6. Vytvorenie databázy

2.7. Spustenie simulácie

2.8. Dokončovacie operácie v rámci následného spracovania

## Operácia 1: Operácia lisovania

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obr. L1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Vytvorenie nového projektu z hlavného okna grafického rozhrania

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obrázku 1. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli Jednotky vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „**Tee**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

Spolu s oknom Nový projekt sa otvorí sprievodca MO (pozri obr. L1.2.), pričom definovaný názov úlohy „**Tee**“ sa aktualizuje ako názov projektu spolu so systémom jednotiek. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.  
V prípade potreby môže používateľ zmeniť systém jednotiek a pridať operáciu tak, že z roletového zoznamu „Prvá operácia“ vyberie príslušnú operáciu a zaškrtne príslušné políčko. Pomocou možnosti „Kopírovať existujúci projekt“ môže používateľ importovať predtým uložené projekty ako nové projekty. 

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0002.jpg' | relative_url }})

Okno „Definícia nového projektu“ v MO

### Pridanie operácie 3D tvarovania 

Po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) sa otvorí sprievodca viacerými operáciami, v ktorom je možné nastaviť úlohu. Pridajte operáciu 3D tvarovania zo zoznamu operácií v Průzkumníku. Operáciu môžete pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky **Operácia 3D tvarovania** (pozri obr. L1.3.) alebo ju môžete pridať aj pretiahnutím do Editoru operácií.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0003.jpg' | relative_url }})

Pridanie operácie 3D tvárnenia

### Ovládacie prvky simulácie

Toto laboratórium je izotermické zariadenie, preto na stránke **Simulácia****ovládacie prvky** **zrušte zaškrtnutie** políčka režimu **Prenos tepla** (pozri obr. L1.4.). Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0004.jpg' | relative_url }})

Výber režimu simulácie

### Pridávanie objektov

Na túto operáciu sme potrebovali tri objekty. Ak ešte nemáte tri objekty, pridajte ich kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). Tieto tri objekty budú pomenované ako „Obrobok“, „Horná matrica“ a „Spodná matrica“ (pozri obr. L1.5.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0005.jpg' | relative_url }})

Pridávanie objektov na stránke objektov

### Obrobok

Zmeňte teplotu obrobku na **2150** °**F**, ako je znázornené na obr. L1.6. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0006.jpg' | relative_url }})

Stránka „Objekt obrobku“

### Import geometrie obrobku

Na stránke **Geometria** kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice) a naimportujte súbor **TeeBillet.stl** zo zložky /3D/Labs/, ako je znázornené na obr. L1.7.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0007.jpg' | relative_url }})

Import geometrie obrobku

Skontrolujte geometriu kliknutím na akčný štítok ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Zobrazí sa okno „Výsledok kontroly geometrie“ s popisom výsledku kontroly geometrie spolu s popisom toho, čo predstavuje platnú geometriu, ako je znázornené na obr. L1.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0008.jpg' | relative_url }})

Stránka s výstupnými údajmi o geometrii

### Vytvorenie siete obrobku

Nastavte **cieľový počet prvkov** na hodnotu **32000** a kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. L1.9. V expertnom režime sú k dispozícii rôzne typy nastavení siete, v tomto cvičení však budeme používať predvolené nastavenia siete. Vygenerovaná sieť pre obrobok vyzerá tak, ako je znázornené na obr. L1.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0009.jpg' | relative_url }})

Vytvorenie siete pre obrobok

### Priradiť materiál k obrobku

V okne „Material“ načítajte materiál **AISI-316[70-2020F(20-1100C)]** z knižnice materiálov DEFORM, z kategórie **Nerezová****** pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. L1.10 nižšie, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) v okne Knižnica materiálov. Materiál je možné načítať aj zo zoznamu materiálov v Průzkumníku. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Horná matrica“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0010.jpg' | relative_url }})

Nakladanie materiálu pre obrobok

### Definícia pojmu „Top Die“

Na stránke „Top Die“ nastavte teplotu objektu na hodnotu **300 °F**, ako je znázornené na obr. L1.11, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0011.jpg' | relative_url }})

Na začiatok stránky objektu „Die“

### Import geometrie hornej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a načítajte súbor **TeeTop.stl** zo zložky **/3D/Labs/**, ako je znázornené na obr. L1.12. Následne skontrolujte geometriu pomocou položky ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) na stránke Geometria. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0012.jpg' | relative_url }})

Import geometrie pre hornú matricu

### Priradiť pohyb hornej matrice

Na stránke „Pohyb“ vyberte typ pohybu **rýchlosť**, uistite sa, že pohyb prebieha v smere **–Z**, a potom zadajte hodnotu **10** palcov/sekundu ako hodnotu **Konštanta**, ako je znázornené na obr. L1.13. Horná matrica sa bude pohybovať rýchlosťou 10 in/sec. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0013.jpg' | relative_url }})

Definovanie pohybu hornej matrice

### Definícia spodnej matrice

Na stránke „Spodná forma“ nastavte teplotu objektu na **300°** F a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie spodnej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor **TeeBottom.stl**. Následne skontrolujte geometriu pomocou položky ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) na stránke Geometria. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Umiestňovanie objektov

Túto operáciu vykonáme so sústružným obrobkom v zvislom smere. Najskôr umiestnime sústružný obrobok na spodnú matricu. Aby to bolo lepšie vidieť, prepnite sa do režimu „Zobrazenie objektov definovaných používateľom“ na ovládacom paneli v spodnej časti stromu objektov. V okne „Object mode“ vyberte hornú matricu a zrušte zaškrtnutie políčka v stĺpci „Visible“, ako je znázornené na obr. L1.14, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0014.jpg' | relative_url }})

Stránka pre výber zobrazenia objektov definovaných používateľom a pre umiestňovanie objektov

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Otvorí sa stránka na polohovanie objektu, ako je znázornené na obr. L1.14. Vyberte polohovanie „**Rotácia**“ a potom ako polohovací objekt vyberte **obrobok**. Pomocou **myši** vyberte bod v blízkosti stredu obrobku a potom ako os otáčania vyberte os „**X**“. Zadajte uhol **90** stupňov a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Obrobok by mal byť teraz umiestnený zvisle, pozri obr. L1.15.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0015.jpg' | relative_url }})

Stránka okna na umiestňovanie objektov

Prepnite na polohovanie „**Drag**“ a pomocou myši presuňte obrobok na rovnú plochu na matrici, ako je znázornené na obr. L1.16, nie príliš blízko k formovacej dutine ani k okraju matrice. Teraz použijeme polohovanie „**Interference**“ na umiestnenie obrobku na spodnú formu. 

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0016.jpg' | relative_url }})

Umiestnenie obrobku na spodnú matricu

Kliknite na používateľsky definovaný režim ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) a zaškrtnite políčko „Horná matrica je viditeľná“. Teraz umiestnite hornú matricu pomocou polohovania **interferenciou** na obrobku tak, aby bola v kontakte s obrobkom. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

###  Definícia pojmu „kontakt“ (vzťah medzi objektmi)

Vyberte kontakt typu **Používateľ****typ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi obrobkom, hornou maticou a spodnou maticou, ako je znázornené na obr. L1.17.

  
Zvýraznite vzťah „Horná matrica – obrobok“ a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), aby ste tento vzťah upravili. Na karte „Trenie“ (pozri obr. L1.18) sa nachádza roletové menu pre pole **Konštanta**, ktoré umožňuje používateľovi vybrať vhodné podmienky trenia bežných procesov tvárnenia. Vyberte z roletového menu položku **Kovanie za tepla (s mazáním)**, čím sa do poľa Konštanta trenia vloží hodnota trenia **0,3**.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna Inter-Object. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, tlačidlom ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie **0,3**. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určite vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,001169"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Ak otočíte objekty v grafickom okne, uvidíte, že medzi dvoma objektmi vznikol kontakt. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno Stopping controls.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0017.jpg' | relative_url }})

Stránka s kontaktmi zobrazujúca dvojice kontaktov

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0018.jpg' | relative_url }})

Nastavenie hodnoty trenia z roletového menu 

### Definícia ovládacích prvkov na zastavenie

Zastavíme sa, keď bude vzdialenosť medzi formami 1,500”. Nastavte teda „Stop Controls“ na „**Vzdialenosť****medzi objektmi**“ a zadajte hodnotu **1,5**” v smere Z, ako je znázornené na obr. L1.19. Na definovanie zastavovacej vzdialenosti medzi maticami zapnite režim tieňovania pomocou ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}), vyberte bod na spodnej ploche hornej matice a potom druhý bod na hornej ploche spodnej matice. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Step“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0019.jpg' | relative_url }})

Určenie vzdialenosti medzi ovládacími prvkami na zastavenie lisovacích foriem

### Ovládacie prvky krokov

Na stránke „Step“ (Krok) zmeňte **počet krokov** na **50**, **nastavte krok ukladania** na **5** a definíciu kroku riešenia na **0,036** Posun matrice (pozri obr. L1.20.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0020.jpg' | relative_url }})

Stránka na ovládanie krokov

### Vytvoriť databázu

Na stránke „Generate DB“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly:  
Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáli).   
  
Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Akonáhle program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), ako je znázornené na obr. L1.21, potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

.

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0021.jpg' | relative_url }})

Stránka okna simulácie behu

  
Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá možnosť „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.  
  
Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a poskytuje údaje o tom, ako dobre simulácia prebieha.  
  
Keď simulácia prebehne bez problémov, skontrolujte správy v súbore správ; po dokončení operácie sa zobrazia správy typu „VZDIALENOSŤ MEDZI DVOMA OBJEKTAMI (2 3): 1,5000000 DOSIAHLA ŠPECIFIKOVANÝ LIMIT 1,5000000“

### Následná úprava po operácii lisovania

Po dokončení simulácie prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste si mohli prezrieť výstup simulácie. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) v prehliadači krokov si môžete zobraziť všetky uložené kroky, ako je znázornené na obr. L1.22.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0022.jpg' | relative_url }})

Prehliadač krokov v aplikácii MO Post, ktorý zobrazuje všetky uložené kroky

  
**Stavová premenná:**  
V ponuke stavových premenných kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}), vyberte premennú „**Stress![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})** **Efektívna**“, typ zobrazenia **Plná** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), ako je znázornené na obr. L1.23. Výstup stavovej premennej si môžete zobraziť aj vo forme prvkových, čiarových alebo tieňovaných kontúr. Vyskúšajte si každé z týchto nastavení.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0023.jpg' | relative_url }})

Rozloženie efektívneho napätia v obrobku na konci prvej operácie

  
**Sledovanie bodov:**  
Vyberte sledovanie bodov ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}). Vyberte niekoľko bodov na objekte a sledujte ich pomocou možnosti ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) (pozri obr. L1.24.). Ak sa zobrazuje stavová premenná, hodnoty tejto premennej sa v týchto bodoch znázornia graficky.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab01_image0024.jpg' | relative_url }})

Výstup sledovania bodov pre efektívnu deformáciu  

## Operácia 2 – Dokončenie operácie v kováčni

Po dokončení simulácie a následného spracovania prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

### Pridať a definovať druhú operáciu

Pridajte ďalšiu operáciu tvárnenia na nastavenie operácie dokončovacieho kovania. V tejto operácii umiestnime obrobok nad dutinu v matrici a simulujeme operáciu dokončovacieho kovania.

**Zvoľte režim hromadného spracovania:**  
V editore operácií vyberte druhú operáciu; zobrazí sa vyskakovacie okno „Typ nastavenia“. V tomto okne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}), pretože chceme nastaviť druhú operáciu v režime **Batch**.

**Zmena názvu operácie:**  
Zmeňte názov operácie na „**Finish Forge**“ v editore operácií tak, že dvakrát kliknete na názov operácie, ako je znázornené na obr. L2.1, a potom kliknite na tlačidlo **Enter**, čím úpravu dokončíte.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0001.jpg' | relative_url }})

Zmena názvu operácie na stránke editora operácií

### Plánované polohovanie

Keďže sa všetky objekty načítajú z databázy a nedochádza k žiadnym zmenám v nastaveniach siete ani v BCC, prejdeme na stránku **Polohovanie**. Na stránke Ovládacie prvky kliknite na **Plánované polohovanie**. Na stránke Plánované polohovanie pridajte vzťah kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) na definovanie plánovaného polohovania, ako objekt polohovania vyberte Obrobok a ako typ polohovania Offset, nastavte „**Y**“ na hodnotu **-3,4**, aby sa obrobok umiestnil do dutiny formy.  
Podobne pridajte vzťahy pre umiestnenie hornej matrice na obrobok v smere **-Z** a spodnej matrice pod obrobok v smere **+Z** pomocou možností polohovania podľa kolízie, ako je znázornené na obr. L2.2. Polohovanie objektov sa vykoná pred vytvorením databázy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0002.jpg' | relative_url }})

Určenie umiestnenia v rozvrhu

### Definícia pojmu „kontakt“ (vzťah medzi objektmi)

Na stránke „Kontakt“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Vyberte vzťah „Obrobok – horná matrica“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Z roletového zoznamu poľa „Constant“ na karte „Deformation“ vyberte ako podmienku trenia **„Hot forging (lubricated)**“, ako je znázornené na obr. L1.18. Vráťte sa do okna „Inter-object relations“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste podobné podmienky aplikovali na všetky vzťahy. Uistite sa, že na stránke „Kontakt“ sú zaškrtnuté políčka „**Plán**“ a „**Inicializovať**“, ako je znázornené na obr. L2.3., aby sa podmienky kontaktu na rozhraní inicializovali a regenerovali pred vytvorením databázy pre druhú operáciu. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0003.jpg' | relative_url }})

Stránka s kontaktnými údajmi

### Ovládacie prvky na zastavenie

Kujeme na hrúbku **0,250"**. Zaškrtnite teda políčko **Vzdialenosť medzi objektmi**, vyberte body na spodnej strane hornej matrice a na hornej strane spodnej matrice. Zadajte zastavovaciu vzdialenosť **0,250** v smere **Z**, ako je znázornené na obr. L2.4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0004.jpg' | relative_url }})

Stránka okna na zastavenie riadenia

### Ovládacie prvky krokov

Na stránke „Kroky“ zmeňte „Počet krokov“ na **50**, **nastavte prírastok na uloženie** na **5** a definíciu kroku riešenia na **posun matrice** s hodnotou **0,036** in (pozri obr. L2.5.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0005.jpg' | relative_url }})

Stránka na ovládanie krokov

### Vytvorenie databázy

Keď používateľ navštívi stránku na vytvorenie databázy, uvidí, že objekty sú umiestnené podľa údajov o naplánovanom umiestnení. Skontrolujte, či je poloha obrobku vo forme taká, ako je znázornené na obr. L2.6., a potom skontrolujte a vytvorte databázu (pozri obr. L2.6.). Po vygenerovaní databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0006.jpg' | relative_url }})

Stránka „Vytvoriť databázu“

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), aby sa otvorilo dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

  
Keď simulácia prebehne bez problémov, skontrolujte správy v súbore správ. Po dokončení operácie sa zobrazí správa v tvare

  
„PROGRAM SA ZASTAVIL!  
VZDIALENOSŤ MEDZI DVOMA OBJEKTMI (2 3): 0,2500000 DOSIAHLA ŠPECIFIKOVANÚ HORNÚ HRANICU 0,2500000 “.

  
Po dokončení simulácie prepnite do režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

### Dokončovacie operácie v rámci následného spracovania

Kliknite pravým tlačidlom myši na ikonu obrobku v strome procesov a zapnite zobrazenie kontaktu. Sledujte, ako sa kontakt mení v priebehu vyplňovania formy obrobkom – pozri obr. L2.7.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0007.jpg' | relative_url }})

Dotknite sa displeja, aby ste skontrolovali výplň v poslednom kroku operácie „Finish Forge“

Nakreslite krivku zaťaženia a zdvihu podľa obr. L2.8. Pozorujte, ako sa zaťaženie zvyšuje v miere, ako sa diel vyplňuje formu a vytvára prebytok materiálu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0008.jpg' | relative_url }})

Graf závislosti zaťaženia od zdvihu

Zaznačte rýchlosť deformácie počas tvárnenia tak, ako je znázornené na obr. L2.9., a sledujte, čo sa deje v oblasti prebytku materiálu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab06_hot_forming_labs/lab02_image0009.jpg' | relative_url }})

Efektívna rýchlosť deformácie na konci operácie dokončovacieho kovania
