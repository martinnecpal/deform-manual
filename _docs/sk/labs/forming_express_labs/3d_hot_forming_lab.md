---
lang: sk
title: "Laboratórium 3D tvarovania za tepla"
---

# Laboratórium 3D tvarovania za tepla

V tomto laboratórnom cvičení nastavíme operáciu kovania metódou „Tee“ v programe Forming Express.

Operácia 1: Operácia lisovania

Operácia 2: Dokončenie operácie „Forge“

## : Operácia s negatívnym výsledkom

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main, ako je znázornené na obr. 3DHFL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 3DHFL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „**Tee**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa okno „Integrated Manufacturing Process“ (pozri obr. 3DHFL1.3.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „****Tee****“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0003.jpg' | relative_url }})

Okno na výber miesta problému

### Pridanie operácie 3D Forming Express – puzdro

Po kliknutí na tlačidlo „Dokončiť“ sa otvorí sprievodca viacerými operáciami, v ktorom môžete nastaviť úlohu. **Pridajte****3D Forming Express** zoznamu operácií v Průzkumníku. Operáciu môžete pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 3D Forming Express (pozri obr. 3DHFL1.4.) alebo ju môžete pridať aj pretiahnutím do Editoru operácií.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0004.jpg' | relative_url }})

Do editora operácií bola pridaná operácia „3D Forming Express“

**Zmeniť názov operácie**

Zmeňte názov operácie na „**Bush**“ dvojitým kliknutím na pole „Forming“ v editore operácií, ako je znázornené na obr. 3DHFL1.5.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0005.jpg' | relative_url }})

Zmena názvu operácie v editore operácií

### Nastavenia definovania procesu

Na **stránke Proces** vyberte typ procesu „Kovanie za tepla“ kliknutím na prepínač **Kovanie za tepla**. V rámci tohto cvičenia budeme simulovať celý diel; ak nezvolíte typ geometrie „Celý diel“, táto možnosť bude predvolene vybraná. Posuvníky „Zložitosť tvaru“ a „Presnosť simulácie“ ovplyvňujú nastavenia siete a počet časových krokov použitých v simulácii. To zase ovplyvňuje dobu behu a úroveň detailov dostupných v simulácii. Pre túto simuláciu použijeme geometriu „**Jednoduchá**“ a výpočty „**Rýchle**“, preto posuňte oba posuvníky úplne doľava, ako je znázornené na obr. 3DHFL1.6. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0006.jpg' | relative_url }})

Stránka procesu

### Výber tepelného výpočtu

V tejto simulácii budeme pracovať s **konštantnou teplotou (izotermicky)**. To znamená, že sa nastaví počiatočná teplota obrobku, ale program DEFORM nebude pri výpočtoch zohľadňovať žiadne zmeny teploty. Zvoľte tlačidlo **Konštantná teplota (izotermická)**, ako je znázornené na obr. 3DHFL1.7. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0007.jpg' | relative_url }})

Stránka na výber režimu tepelného výpočtu

### Vyberte počet objektov

Táto simulácia bude obsahovať 1 obrobok a 2 lisovacie formy; použite predvolený výber, ako je znázornené na obr. L1.8, a potom kliknite na .

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0008.jpg' | relative_url }})

Okno „Počet objektov“

### Všeobecná definícia obrobku

Obrobok bude mať počiatočnú teplotu 2250 °F. Zmeňte **Teplotu obrobku** na **2150 °F**, ako je znázornené na obr. 3DHFL1.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**Poznámka:** Na stránke „objekt“ sa nachádza tlačidlo „importovať objekt“. Slúži na import kompletných údajov o objekte z iného súboru s údajmi o objektoch.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0009.jpg' | relative_url }})

Stránka objektu obrobku

#### Import geometrie obrobku

Na stránke „Geometria“ kliknite na tlačidlo „Načítať geometriu z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})“ a importujte súbor **TeeBillet.stl**, ako je znázornené na obr. 3DHFL1.10.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0010.jpg' | relative_url }})

Stránka „Importovať geometriu“

Skontrolujte geometriu kliknutím na akčný štítok ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Okno „Výsledok kontroly geometrie“ obsahuje popis toho, čo predstavuje správnu geometriu, ako je znázornené na obr. 3DHFL1.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0011.jpg' | relative_url }})

Okno kontroly geometrie

#### Vytvorenie siete obrobku

Vytvorte sieť pre hodnotu nastavení typu **systém** kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 3DHFL1.12. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Materiál“.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0012.jpg' | relative_url }})

Stránka „Mriežka obrobku“

#### Priradiť materiál k obrobku

V okne „Material“ načítajte materiál **AISI-316[70-2020F(20-1100C)]** z knižnice materiálov DEFORM, z kategórie **Steel_at_Extended_Temperature** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na nižšie uvedenom obr. 3DHFL1.13, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v prehliadači. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Top Die.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0013.jpg' | relative_url }})

Okno s materiálmi

### Definícia pojmu „Top Die“

Na stránke „Top Die“ použite predvolenú teplotu objektu (**300** °F), ako je znázornené na obr. 3DHFL1.14. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0014.jpg' | relative_url }})

Hlavná stránka Die

#### Import geometrie hornej matrice

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **TeeTop.stl**, ako je znázornené na obr. 3DHFL1.15. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0015.jpg' | relative_url }})

Možnosť „Importovať geometriu“

#### Priradiť pohyb hornej matrice

V nastaveniach pohybu vyberte možnosť rýchlosti. Uistite sa, že pohyb prebieha v smere **–Z**, a zadajte **rýchlosť** **10** palcov za sekundu, ako je znázornené na obr. 3DHFL1.16. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0016.jpg' | relative_url }})

Na začiatok stránky „Pohyb matrice“

### Definícia spodnej matrice

Na stránke „Spodná forma“ použite predvolenú hodnotu **Teplota** objektu (**300** °F) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import geometrie spodnej matrice

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **TeeBottom.stl**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Umiestňovanie objektov

Túto operáciu vykonáme so sústruženým dielom v zvislom smere. Najskôr umiestnime sústružený diel na spodnú matricu. Aby sme mali lepší prehľad, prepnime sa do režimu „**Zobrazenie objektov definovaných používateľom**“ na ovládacom paneli v spodnej časti stromu objektov. V okne „Object mode“ vyberte „Top Die“ a zrušte zaškrtnutie políčka v stĺpci „Visible“, ako je znázornené na obr. 3DHFL1.17., potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0017.jpg' | relative_url }})

Okno režimu objektu na vypnutie hornej matrice v okne zobrazenia

Kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) sa otvorí okno na nastavenie polohy objektu, vyberte polohu ![]({{ '/assets/icons/pre_icons/mo_rotational_radio_button.jpg' | relative_url }}). Vyberte obrobok. Pomocou myši vyberte bod v blízkosti stredu obrobku a potom vyberte os „**X**“ ako os otáčania. Zadajte uhol **90** stupňov a ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Obrobok by mal byť teraz umiestnený vo vertikálnej polohe. (Pozri obr. 3DHFL1.18.)

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0018.jpg' | relative_url }})

Okno na umiestňovanie objektov

Prepnite na polohovanie ![]({{ '/assets/icons/pre_icons/mo_drag_radio_button.jpg' | relative_url }}). Kliknite na os „**X**“ alebo „**Y**“ a pomocou myši presuňte polotovar na rovnú časť formy, nie príliš blízko k formovacej dutine ani k okraju formy. Použite polohovanie ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) na umiestnenie polotovaru na spodnú formu. (Pozri obr. 3DHFL1.19.)

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0019.jpg' | relative_url }})

Umiestnenie polotovaru na spodnú matricu

Teraz kliknite na používateľsky definovaný režim ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) a zaškrtnite políčko **Horná matrica** je viditeľná, potom umiestnite hornú matricu pomocou polohovania podľa interferencie na sochoru tak, aby bola v kontakte so sochorom. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definícia pojmu „kontakt“ (vzťah medzi objektmi)

Vyberte **Užívateľsky definované** – „**Kovanie za tepla (s mazáním)**“ ako podmienku trenia, ako je znázornené na obr. 3DHFL1.20, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). Program DEFORM automaticky označí uzly, ktoré sú spočiatku v kontakte s lisovacou formou. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0020.jpg' | relative_url }})

Stránka na získavanie kontaktov

### Definícia zdvihu primárneho lisovacieho nástroja

Hlavný zdvih matrice je odhad vzdialenosti, ktorú matrica prejde počas tvárnenia. Táto hodnota nemusí byť presná (presné kritériá zastavenia budú špecifikované na nasledujúcej obrazovke).

V tejto úlohe budeme zúžovať polotovar s rozmerom 3,300” na 1,500”. Zdvih primárneho lisovacieho nástroja je približne 1,800”, preto definujte **celkový zdvih primárneho lisovacieho nástroja** ako **1,8** palca, ako je znázornené na obr. 3DHFL1.21. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0021.jpg' | relative_url }})

Hlavná stránka o zdvihu matrice

### Definícia ovládacích prvkov na zastavenie

Chceme zastaviť, keď budú matrice od seba vzdialené 1,500”. Nastavte teda položku „Stop Controls“ na „Distance between objects“. Zadajte hodnotu **1,5** ”, ako je znázornené na obr. 3DHFL1.22. Zapnite tieňovanú sieť a vyberte bod na spodnej ploche hornej matrice a druhý bod na hornej ploche spodnej matrice. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0022.jpg' | relative_url }})

Stránka ovládacích prvkov zastavenia

### Definícia ovládacích prvkov simulácie

Počet simulačných krokov a veľkosť kroku sa určujú nastavením posuvníka „zložitosť tvaru objektu“. Ak chcete zmeniť predvolené hodnoty, môžete tak urobiť v tomto okne. V rámci tohto cvičenia použijeme predvolené hodnoty, ako je znázornené na obr. 3DHFL1.23., a potom klikneme na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0023.jpg' | relative_url }})

Ovládacie prvky simulácie

### Vytvoriť databázu

Na stránke „Generate DB“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). 

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DHFL1.24. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0024.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Keď sa simulácia bez problémov dokončí, skontrolujte správy v súbore správ; po dokončení operácie sa tam objavia správy typu: „."„VZDIALENOSŤ MEDZI DVOMA OBJEKTMI (2 3): 1,5000000 DOSIAHLA ŠPECIFIKOVANÝ LIMIT 1,5000000“.

### Následná úprava po operácii zúženia

Po dokončení simulácie prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) na následné spracovanie. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) v prehliadači krokov si môžete zobraziť všetky uložené kroky, ako je znázornené na obr. 3DHFL1.25.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0025.jpg' | relative_url }})

Režim MO Post

**Stavová premenná:**

V ponuke stavových premenných kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}), vyberte efektívnu premennú deformácie, ako typ zobrazenia zvoľte **Plná** a kliknite na **![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }})**, ako je znázornené na obr. 3DHFL1.26. Môžete zobraziť čiarové alebo tieňované kontúry. Je tiež možné zvoliť vyplnenie celoplošným tieňovaním alebo tieňovaním prvkov. Vyskúšajte si každé z týchto nastavení.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0026.jpg' | relative_url }})

Deformácia – graf efektívnej stavovej premennej

**Sledovanie bodov:**

Vyberte ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) **sledovanie bodov**. Vyberte niekoľko bodov na objekte a sledujte ich pomocou možnosti ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) (pozri obr. 3DHFL1.27.). Ak sa zobrazuje stavová premenná, hodnoty týchto premenných sa v týchto bodoch znázornia graficky.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0027.jpg' | relative_url }})

Sledovanie bodov

## : Ukončiť operáciu v kováčskej dielni

Po dokončení simulácie prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

### Pridať a definovať druhú operáciu

Pridajte ďalšiu operáciu „Forming express“ na nastavenie operácie „Finish forge“. V tejto operácii umiestňujeme obrobok nad dutinu v lisovacej forme a simulujeme operáciu „Finish forge“.

**Vyberte režim hromadného spracovania:**

V editore operácií vyberte druhú operáciu, zobrazí sa rozbaľovacie okno „Typ nastavenia“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) (keďže nastavujeme druhú operáciu v dávkovom režime).

**Zmena názvu operácie:**

V editore operácií zmeňte názov operácie na „**Finish Forge**“, ako je znázornené na obr. 3DHFL1.28.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0028.jpg' | relative_url }})

Zmena názvu operácie

### Nastavenie procesu pre dokončovaciu operáciu

Zmeňte zložitosť tvaru objektu na „**Stredná**“. Presnosť ponechajte na hodnote „**Rýchla**“, ako je znázornené na obr. 3DHFL1.29, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Plánované polohovanie“.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0029.jpg' | relative_url }})

Nastavenia procesu pre dokončovaciu operáciu

### Plánované umiestnenie

Vytvorte vzťah kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), ako polohovací objekt vyberte **Obrobok** a zvoľte možnosť **Posun**, potom zadajte hodnoty **X** a **Y** na umiestnenie obrobku do dutiny formy.

Podobne pridajte vzťahy k polohe **Horná matrica** na **Obrobku** v smere **-Z** a **Spodná******Spodná forma** pod **obrobkom** v smere **+Z** pomocou možností polohovania **Interference**, ako je znázornené na obr. 3DHFL1.30. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0030.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Definícia pojmu „kontakt“ (vzťah medzi objektmi)

Ako podmienku trenia vyberte **Užívateľsky definované** – „**Kovanie za tepla (s mazáním)**“, ako je znázornené na obr. 3DHFL1.20. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definícia primárneho zdvihu matrice

Budeme kovať od počiatočnej výšky 1,500” až po výšku výstupku 0,250”, pričom celkový zdvih bude 1,250”. Zadajte hodnotu **1,25** ako hodnotu **primárneho zdvihu matrice**, ako je znázornené na obr. 3DHFL1.31. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0031.jpg' | relative_url }})

Okno primárneho zdvihu matrice

### Ovládacie prvky na zastavenie

Kujeme na hrúbku 0,250". Zaškrtnite teda políčko „Vzdialenosť medzi objektmi“, vyberte body na spodnej strane hornej matrice a na hornej strane spodnej matrice. Zadajte zastavovaciu vzdialenosť **0,250** a vyberte smer **Z**, ako je znázornené na obr. 3DHFL1.32. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0032.jpg' | relative_url }})

Okno s ovládacími prvkami na zastavenie

### Ovládacie prvky simulácie

Použite predvolené hodnoty definície systémového kroku, ako je znázornené na obr. 3DHFL1.33, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0033.jpg' | relative_url }})

Okno ovládacích prvkov simulácie

### Vytvorenie databázy

Keď používateľ navštívi stránku na vytvorenie databázy, môže skontrolovať, či sú objekty umiestnené podľa údajov o naplánovanom umiestnení, overiť, či je poloha obrobku v dutine formy správna, a následne skontrolovať a vygenerovať databázu (pozri obr. 3DHFL1.34.). Po vygenerovaní databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0034.jpg' | relative_url }})

Stránka „Vytvoriť databázu“

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DHFL1.24. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia.

Keď sa simulácia bez problémov dokončí, skontrolujte správy v súbore správ; po dokončení operácie sa zobrazia správy typu:

„PROGRAM SA ZASTAVIL!

VZDIALENOSŤ MEDZI DVOMA OBJEKTMI (2 3): 0,2500000 DOSIAHLA ŠPECIFIKOVANÚ HORNÚ HRANICU 0,2500000 “.

Po dokončení simulácie prepnite do režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

### Dokončovacie operácie v rámci následného spracovania

Prejdite si simuláciu. Vyplnil diel dutinu formy? Možno budete chcieť vypnúť jednu alebo druhú formu, prípadne použiť priehľadnosť, aby ste diel lepšie videli.

Kliknite pravým tlačidlom myši na ikonu obrobku v strome procesu a zapnite zobrazenie kontaktu. Sledujte, ako sa kontakt mení v priebehu vyplňovania formy obrobkom, pozri obr. 3DHFL1.35.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0035.jpg' | relative_url }})

Dotknite sa displeja a skontrolujte podplnenie

Vykreslite krivku **zaťaženia v zdvihu** podľa obr. 3DHFL1.36. Pozorujte, ako sa zaťaženie zvyšuje v priebehu vyplňovania formy dielom a vytvárania prebytku materiálu.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0036.jpg' | relative_url }})

Graf závislosti zaťaženia od zdvihu

Zaznačte rýchlosť deformácie počas tvárnenia tak, ako je znázornené na obr. 3DHFL1.37. Pozorujte, čo sa deje v oblasti výstupku.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0037.jpg' | relative_url }})

Graf efektívnej stavovej premennej rýchlosti deformácie
