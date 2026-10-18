---
lang: sk
title: "Polotovar na ozubené kolesá EN, laboratórium 3"
---

# Lab3. Postupné operácie v programe 3D Forge

V tomto cvičení sa dozviete, ako pokračovať v postupných 3D operáciách po prevode 2D objektov na 3D pomocou nástroja na prevod z 2D na 3D.

### Pridať operáciu 3D tvárnenia

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky **3D Forming** v zozname operácií tvárnenia na karte **Explorer**, ako je znázornené na obr. STPL1.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0001.jpg' | relative_url }})

Pridanie operácie 3D tvarovania po konvertore z 2D na 3D

Otvorte operáciu 3D tvarovania v editore operácií kliknutím na ňu a v rozbaľovacom okne **Typ nastavenia** (pozri obr. STPL1.2.) vyberte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}), aby ste nastavili úlohu v dávkovom režime.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0002.jpg' | relative_url }})

Vyskakovacie okno s typom nastavenia pre 3. operáciu – 3D tvarovanie

Premenujte operáciu 3D tvárenia na **Kovanie** tak, že v editore operácií kliknete na názov „Tvárenie“ pri operácii 3D tvárenia a stlačením klávesy **Enter** potvrdíte zmenu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Nastavenie režimu simulácie a pridávanie objektov

V nastaveniach simulácie **zrušte zaškrtnutie** režimu **Prenos tepla** na hlavnej karte nastavení simulácie, keďže ide o izotermickú simuláciu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekty“.

Pokračujte v nastavení pridaním troch objektov, ktoré budú slúžiť ako polohovacie prvky pre obrobok a hornú a spodnú matricu potrebné pri tejto operácii.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste začali definovať objekt obrobku.

### Definícia objektu obrobku

Vyberte typ objektu obrobku „načítané z databázy“, ako je znázornené na obr. STPL1.3. Objekt typu „načítané z databázy“ načíta všetky údaje objektu z posledného kroku predchádzajúcej operácie, takže načíta údaje o konvertovanom 3D objekte.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0003.jpg' | relative_url }})

Okno s objektom obrobku pre operáciu v programe 3D Forge

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili nastavenia siete obrobku.

### Zmena nastavení siete obrobku

Zaškrtnite políčko **Definovať nastavenia siete**, ak chcete zmeniť nastavenia siete. Nastavte **veľkosť****pomer** na hodnotu 2 a potom vyberte typ **Absolútny**, ako je znázornené na obr. STPL1.4. Týmto sa definuje cieľový počet prvkov na základe najmenšej veľkosti prvku a pomeru veľkostí. Počet prvkov sa bude zvyšovať s rastúcou zložitosťou geometrie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0004.jpg' | relative_url }})

Všeobecné nastavenia siete v expertnom režime pre objekt „Čítanie z databázy“

Vyberte kartu **Remesh** a zmeňte hodnotu **hĺbky interferencie** na **0,7** **relatívnej**. (Pozri obr. STPL1.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0005.jpg' | relative_url }})

Nastavenia kritérií pregenerovania siete v expertnom režime pre objekt „Read from DB“

Keďže údaje, ako napríklad materiál a okrajové podmienky, sa preberajú z predchádzajúcej operácie, nie je potrebné tieto údaje meniť. Na nastavenie cieľového objemu vyberte v stromovej štruktúre operácií pod položkou „obrobok“ položku **Vlastnosť**.

### Nastavenie cieľového objemu obrobku

Na karte Vlastnosti **Deformácia** zaškrtnite políčko **Predefinovať**: Cieľový objem a priraďte iba možnosť **Cieľový objem ako aktívny v FEM**. Toto nastavenie by sa malo používať pri väčšine simulácií kovania. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) (Vypočítať objem) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), aby ste potvrdili odporúčaný objem. Upozorňujeme, že sa môže mierne líšiť od hodnoty uvedenej na obr. STPL1.6.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0006.jpg' | relative_url }})

Definícia cieľového objemu v okne vlastností deformácie

Kliknite na položku **Geometria** pod položkou **Horná forma** v strome operácií, aby ste pokračovali v definovaní hornej formy.

### Definícia hornej matrice

Načítajte geometriu „**gear_top_die_ENG****.****STL**“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) (importovať) súbor „**gear_top_die_ENG****.****STL**“. Geometria polotovaru sa nachádza v inštalačnej zložke DEFORM v adresári **\3D\Labs**.

Skontrolujte geometriu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a overte, či sú neplatné hrany a orientácia, malé plochy a počet voľných hrán rovné 0 a počet plôch je 1, ako je uvedené vo výsledku na obr. STPL1.7. To znamená, že geometria je v poriadku, preto kliknite na položku **Pohyb** pod hornou matricou v strome operácií, aby ste nastavili ovládacie prvky pohybu hornej matrice.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0007.jpg' | relative_url }})

Výsledok kontroly geometrie hornej matrice

V okne „Pohyb“ nastavte pohyb s konštantnou **rýchlosťou** **3** in/s v smere **–Y**, ako je znázornené na obr. STPL1.8.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0008.jpg' | relative_url }})

Okienko pre pohyb hornej matrice

Kliknite na položku **Geometria** pod položkou „spodná forma“ v strome operácií, aby ste definovali spodnú formu.

### Definícia spodnej formy

Načítajte súbor „**gear_bottom_die_ENG****.****STL**“ pre spodnú matricu (objekt 3) z knižnice. Skontrolujte geometriu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a uistite sa, že je geometria bez chýb, ako je vysvetlené v [3.6. Top die definition.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/' | relative_url }}#3_6_Define_Top_die)

Na umiestnenie objektov kliknite na položku **Plánované****Umiestnenie** v časti Ovládacie prvky v stromovej štruktúre operácií.

### Objekty pozícií v rozvrhu

Po importe nových foriem sa môže stať, že nebudú v správnej polohe. Preto použite funkciu „Polohovanie podľa kolízie“ na posunutie hornej formy v smere –Y, kým sa nedotkne obrobku, a spodnej formy v smere +Y, kým sa nedotkne obrobku. Keďže sa obrobok načítava z objektu DB, v tejto operácii nemôže byť umiestnený, preto musí byť naplánovaný tak, aby bol umiestnený počas behu programu.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a nastavte polohu **hornej matrice** tak, aby dochádzalo k interferencii v smere **-Y** vo vzťahu k **obrobku**, ako je znázornené na obr. STPL1.9. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) definíciu uzavrite.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0009.jpg' | relative_url }})

Najdôležitejšie nastavenia plánovaného polohovania matrice

Podobne nastavte **spodnú****matricu** tak, aby došlo k **tlakovému dosadnutiu** v smere **+Y** voči **obrobku** pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať). Po pridaní zoznamu naplánovaných polôh sa zobrazia podrobnosti o pridaných naplánovaných polohách, ako je znázornené na obr. STPL1.10.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0010.jpg' | relative_url }})

Plánované údaje o polohe pre prevádzku kováčskej dielne

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Kontakty“.

### Definovanie vzťahov medzi objektmi

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) nastavte predvolené vzťahy medzi objektmi. Obrobok by mal byť podriadený tak hornej, ako aj spodnej matrici. Pri 3D simuláciách sa vlastný kontakt (obrobok ako hlavný objekt voči sebe samému) zvyčajne nepoužíva, pretože môže výrazne predĺžiť dobu simulácie. Na sledovanie ohýbania sú k dispozícii aj iné nástroje. Tým sa budeme venovať v neskoršej laboratórnej úlohe.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) pre jeden z vzťahov. V poli **Friction![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Hodnota****** použite roletové menu Constant na výber možnosti**Kovanie za tepla (mazané) 0,3**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustíte ponuku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) použijete hodnotu trenia na ďalšie dva vzťahy. Keďže obrobok pridaný vo vzťahu sa číta z databázy, medziobjektový kontakt sa teraz nedá vygenerovať tak ako v laboratórnej úlohe 1, preto sa uistite, že sú zaškrtnuté políčka Scheduled Initialize a Generate contact, ako je znázornené na obr. STPL1.11. Tým sa počas simulácie inicializujú predchádzajúce kontakty a vygenerujú nové kontakty.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0011.jpg' | relative_url }})

Nastavenia generovania plánovaných kontaktov medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pridali ovládacie prvky na zastavenie.

### Určenie vzdialenosti medzi objektmi a brzdnými ovládacími prvkami

V režime s vedením je možné nastaviť kritérium zastavenia pre hrúbku prebytku zaškrtnutím políčka **Vzdialenosť medzi objektmi**. Táto voľba aktivuje výber pomocou myši, čo vám umožní vybrať dva referenčné body. Vyberte referenčné body na ploche prebytku. Rozrežte objekty pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_slicing_option.jpg' | relative_url }}) (Rezanie) v smere **+Z** do bodu (0,0,0,001) a potom vyberte ikonu ![]({{ '/assets/icons/pre_icons/mo_plus_z_icon.jpg' | relative_url }}) pred výberom bodov na hrúbke výstupku, ako je znázornené na obr. STPL1.12.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0012.jpg' | relative_url }})

Definícia ovládacích prvkov na zastavenie matíc

V tomto prípade je dôležité vybrať vnútornú stranu plochy výrezu. Vyberte smer **Y**, aby ste použili vzdialenosť v osi Y, a potom do poľa „Die Distance between objects“ zadajte hodnotu **0,2** palca. Ak chcete tento rez odstrániť, môžete sa opäť vrátiť do ponuky rezania.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky simulácie.

### Nastavenie ovládacích prvkov simulačného kroku

Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do expertného režimu) (na paneli nástrojov v hlavičke) otvoríte nastavenia pokročilých ovládacích prvkov simulácie. Všimnite si, že číslo operácie sa automaticky aktualizuje na 3, ako je znázornené na obr. STPL1.13.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0013.jpg' | relative_url }})

Hlavná karta „Ovládanie simulačných krokov“

Prejdite na kartu **Krokový prírastok**. Určite vhodný posun matrice na jeden krok (DSMAX) a počet simulačných krokov, ktoré budete potrebovať na uzavretie nástrojov. Zmerajte vzdialenosť medzi hornou a dolnou matricou pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) (merací nástroj). Pri používaní meracieho nástroja môžete kliknúť pravým tlačidlom myši na hlavný displej a vybrať možnosť **CAD Style**. Tým sa zobrazí meranie v definovanom smere osi (X, Y alebo Z). Znovu kliknite pravým tlačidlom myši na displej a vyberte požadovanú os. Vzdialenosť Y medzi nástrojmi je ~1,9 palca. Táto operácia kovania by mala trvať približne 100 krokov. Celkovú vzdialenosť (1,9) vydelíme počtom krokov, čím získame **posun matrice** **0,019**. (Pozri obr. STPL1.14.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0014.jpg' | relative_url }})

Definícia krokového posunu pre hornú maticu

Vyberte kartu **Krok po kroku**, aby ste nastavili **100** ako **počet****krokov** a aby sa údaje **ukladali** každých **5** krokov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vytvorili databázu.

### Kontrola a vytvorenie databázy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a prezrite si informácie o kontrole údajov v súbore so správami. Uistite sa, že kontrola databázy nepreukázala žiadne problémy. Následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy a počkajte, kým sa zobrazí správa „Databáza bola vytvorená“.

Kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustiť simuláciu na viacerých procesoroch

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. L3.15. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“, v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0015.jpg' | relative_url }})

Spustiť možnosti nastavení pre viacprocesorové systémy

Sledujte okno so simulačnou grafikou a kartu „Simulačné správy“, aby ste mohli monitorovať stav prebiehajúcej úlohy, ako je znázornené na obr. STPL1.16.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab3_image0016.jpg' | relative_url }})

Režim simulácie MO – stav 3. operácie počas prevádzky

Pre ďalšie laboratórne cvičenie č. 4 kliknite na odkaz [Lab 4. 3D Non-isothermal Air transfer operation.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab4/' | relative_url }})
