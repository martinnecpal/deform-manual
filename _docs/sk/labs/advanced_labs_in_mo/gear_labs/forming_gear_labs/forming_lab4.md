---
lang: sk
title: "Laboratórium tvárnenia 4"
---

# Cvičenie č. 4. Symetria

### Vytvorenie nového problému

Ak chcete preskúmať 3D symetriu v programe DEFORM, otvorte nový projekt s názvom **Gear_3D_Thermal_Sym** a jednotkami **English**.

Tento projekt je rovnaký ako predchádzajúci **Gear_3D_Thermal** (laboratórna úloha 3), s tým rozdielom, že je modelovaných len 45° obrobku. Aby sa tento 45° sektor dielu deformoval rovnako ako celý diel, je potrebné použiť symetrické okrajové podmienky. V tomto laboratórnom cvičení sa budeme venovať rozdielom pri nastavovaní simulácie so symetriou.

### Pridať operácie

Pridajte tri operácie z programu Explorer:

  * [3D] Heat Transfer Express

  * [3D] Prenos tepla a

  * [3D] Tvarovanie

  
Dvojitým kliknutím na názov prvej operácie ho zmeňte na **Air****Transfer**. Názov druhej operácie zmeňte na **Rest****on****Die**. Názov tretej operácie „Forming“ ponechajte bez zmeny.

Kliknite pravým tlačidlom na **obrobok** a vyberte možnosť **Preniesť objekt do všetkých operácií**. Podobne kliknite pravým tlačidlom na **hornú matricu** a **spodnú****matricu** a pre oba objekty použite možnosť **Preniesť objekt do nasledujúcej operácie**.

### Definícia pojmu „prenos vzduchu“

V editore operácií kliknite na operáciu **Air****Transfer**. V tomto cvičení budeme používať diel **Symmetry**. Skontrolujte, či je typ ohrevu nastavený na **Transfer**. Vyberte typ geometrie Symmetry, posuvníky **Accuracy** a **Complexity** nechajte v polohe **Moderate** (pozri obr. L4.1.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Workpiece.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0001.jpg' | relative_url }})

Okno procesu prevádzky leteckej prepravy

### Definovanie všeobecných údajov o obrobku

Nechajte teplotu obrobku na hodnote 2250 °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

#### Vytvorenie geometrie obrobku z primitívu

Definujte geometriu ako základný **valec** s priemerom **5** palcov, **výškou** **8,1** palca, **uhol otáčania****45** stupňov a **polomer rohu****0,2** palca. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste na stránke symetrie priradili roviny symetrie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0002.jpg' | relative_url }})

Okno „Geometrické primitíva obrobku“

#### Nastaviť symetriu pre obrobok

Vyberte obe rezané plochy a pridajte ich ako **symetrickú****rovinu** tak, že ich označíte myšou a potom kliknete na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Kliknite na jednotlivé položky v časti „Planárna symetria“ a sledujte, ktoré plochy sa zvýraznia (pozri obr. L4.3.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0003.jpg' | relative_url }})

Okno „Symetria obrobku“

#### Vytvorenie siete pre obrobok

Vyberte voľbu **User****defined** a nastavte cieľový počet prvkov na hodnotu **10000** a vygenerujte sieť. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Material“.

#### Priradiť materiál k obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice). Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom **AISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Kliknite na položku **AISI-8620[1550–2200 °F (850 – 1200 °C)]** v okne s materiálmi, aby ste materiál priradili k obrobku. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

#### Obrobok BCC

Štandardne sa generujú okrajové podmienky BCC pre roviny symetrie a výmena tepla s okolím. Uistite sa, že na rovinách symetrie sú definované okrajové podmienky symetrie a že výmena tepla s okolím je definovaná na všetkých plochách okrem rovín symetrie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Heat Condition“ (Teplotné podmienky).

### Nastaviť teplotné podmienky

Nastavte **čas prenosu** na **5** sekúnd, ponechajte predvolené hodnoty **teploty okolia** a **konvekčného koeficientu**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky simulácie.

### Ovládacie prvky simulácie

Použite predvolenú definíciu kroku a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte databázu.

### Vytvoriť databázu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}). Ak sa na karte „Správy“ nenachádzajú žiadne chyby ani varovania, pokračujte a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Teraz kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli k ďalšej operácii.

### Operácia „Rest on Die“

Pri druhej operácii bude typ prenosu tepla **Odpočinok na matrici**. Tým sa simuluje únik tepla z obrobku do nástroja od okamihu jeho umiestnenia na spodnú matricu až do dokončenia zdvihu lisu. Pri tejto operácii by mal obrobok priliehať k spodnej matrici, zatiaľ čo horná matrica by mala byť umiestnená v určitej vzdialenosti od obrobku.

Poznámka: Forma typu „Dwell on“ je určená na odvod tepla po kovaní a využíva vyššie koeficienty odvodu tepla, ktoré zodpovedajú úplnejšiemu kontaktu s formou.

### Typ prenosu tepla

V predvolenom nastavení bude typ prenosu tepla **Rest on die**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Process condition“ (Podmienky spracovania).

### Prevádzkové podmienky

**Doba odpočinku** bude **4** sekundy. Potvrďte **predvolenú teplotu** a **koeficient konvekcie**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Objekt“.

### Zoznam objektov

Overte, či sa v tabuľke nachádzajú 3 objekty. Ak nie, kliknite trikrát na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (vložiť objekt), aby ste pridali 3 objekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Obrobok“.

### Obrobok

Všetky údaje o obrobku sa načítajú z výsledkov prvej operácie v databáze. Preskočte obrobok a prejdite k hornej matrici.

### Hlavná stránka „Top die“

Skontrolujte, či je teplota hornej matrice **300** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou hornej matrice.

#### Import geometrie hornej matrice

Načítajte geometriu hornej matrice ozubeného kolesa zo súboru STL. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) otvorte (načítajte) súbor „**gear top die.STL**“. Geometria hornej matrice sa nachádza v inštalačnej zložke programu DEFORM v adresári \Tutorials. Matrice je orientovaná pozdĺž inej osi ako obrobok. Týmto sa budeme zaoberať v neskoršom kroku.

Pri spustení simulácie tvárnenia použijeme riadenie zastavenia na základe vzdialenosti medzi formami, ale keďže nástroje sú definované v aktuálnej operácii, je potrebné teraz definovať aj referenčné body. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Vlastnosti.

#### Hlavné vlastnosti matrice

Vyberte **Vlastnosti![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Referencia**. Použite **Súradnice** a vyberte bod na plochu s výrezom (pozri obr. L3.7.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Spodná forma“.

### Všeobecná stránka o spodnej matrici

Skontrolujte, či je teplota spodnej matrice **300** °F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku s geometriou spodnej matrice.

#### Import geometrie spodnej matrice

Načítajte geometriu spodnej matrice zo súboru STL. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) otvorte (načítajte) súbor „**gear bottom die.STL**“. Súbor môžete importovať aj pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) tak, že vyhľadáte cestu k súboru s geometriou. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Vlastnosti.

#### Vlastnosti spodnej matrice

Vyberte **Vlastnosti![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Referencia**. Použite **Súradnice** a vyberte bod na odtokovom žľabe (pozri obr. L3.8.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s polohovaním.

### Polohovacie matrice

V tomto bode je obrobok orientovaný pozdĺž osi Z a nástroje sú orientované pozdĺž osi Y.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}).

Najskôr otočte matrice tak, aby boli orientované pozdĺž osi Z. Nastavte metódu na **Rotácia**. Nastavte nasledujúce parametre:

Polohovací objekt: **Horná matrica**.

Osa: X

Stred otáčania: Definovaný používateľom (0,0,0)

Uhol: 90 stupňov.

Chceme otočiť obe matrice súčasne, preto prejdite na kartu **Coupled** a zaškrtnite políčko „Bottom Die“. Tým sa prepojí akékoľvek vykonané polohovanie (pozri [Fig. L3.9.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/forming_lab3/' | relative_url }}#Fig_L3_9_Positioning_Top_die_with_Coupled_Bottom_object)). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) otočte nástroje tak, aby boli zarovnané s obrobkom.

V súčasnosti sú nástroje aj obrobok zarovnané pozdĺž osi Z, nástroje sú však umiestnené príliš blízko pri sebe. Ďalším krokom je posunúť hornú matricu do „hornej“ polohy, ďalej od obrobku. 

**Zrušte zaškrtnutie** voľby „spojené polohovanie“ a následne nastavte polohu hornej matrice pomocou funkcie „Offset“ na vzdialenosť **12** v smere **Z**.

Nakoniec sa musíme uistiť, že spodná forma bude správne priliehať k obrobku. Keďže obrobok sa pri tejto operácii načítava z databázy, nemôžeme použiť bežné polohovanie. Môžeme však použiť naplánované polohovanie, ktoré sa dokončí počas behu projektu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte dialógové okno Polohovanie objektu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku Plánované polohovanie.

### Plánované polohovanie

Pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte naplánovanú polohovaciu operáciu a pomocou funkcie **Interference** nastavte polohu **spodnej** **matrice** vo smere **Z** voči **obrobku**.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a na stránke naplánovaného polohovania by sa mala zobraziť táto naplánovaná operácia. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku „Kontakt“.

### Kontakt

V okne „Kontakt“ priraďte predvolené vzťahy medzi kontaktmi a uistite sa, že sú zaškrtnuté možnosti „Inicializovať“ a „Generovať“ pre naplánovaný kontakt. Trenie nie je potrebné definovať, pretože táto operácia spočíva výlučne v prenose tepla. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ovládacie prvky krokov“.

### Ovládacie prvky krokov

V nastaveniach zastavenia je trvanie procesu už nastavené na 4 sekundy. Pri prenose tepla s kontaktom vykonajte 10 krokov za sekundu. Pre 4-sekundový model teda spustite 40 krokov s časovým krokom 0,1 s. Nastavte **Počet krokov** na **40** a konštantný **čas na krok** na **0,1** s. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nevytvorí stránka databázy.

### Vytvorenie databázy

Prebehne kontrola údajov. Zobrazí sa správa, že databáza nebude vytvorená. Databáza pre túto operáciu sa vytvorí automaticky po dokončení simulácie prvej operácie.

### Tvarovacie operácie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) alebo jednoducho kliknite na dlaždicu „Forming“ v editore operácií, aby ste nastavili operáciu tvárnenia.

Všetky objekty sa načítajú z databázy na konci predchádzajúcej operácie „Rest on Die“, takže stačí len nastaviť:

  * Ovládanie pohybu

  * Polohovanie

  * Vzťahy medzi objektmi

  * Simulácia a ovládacie prvky na zastavenie

### Priradiť pohyb hornej matrice

Kliknite na stránku „Top Die **Movement**“ v strome operácií a nastavte **rýchlosť** na konštantnú hodnotu **3** palcov za sekundu v smere **-Z**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Scheduled Positioning“.

### Plánované polohovanie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a nastavte polohu **interferencie** medzi **hornou matricou****Die** a **obrobkom** v smere **-Z**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Kontakt“.

### Vzťah medzi objektmi

Kliknite na **Kontakt** a definujte vzťahy medzi objektmi s trením 0,3. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky zastavenia.

### Priradenie ovládacích prvkov krokov a zastavenia

V časti „Ovládacie prvky zastavenia“ nastavte kritérium zastavenia **Vzdialenosť medzi maticami** na 0,25 in., pričom ako referenčné objekty použite **Hornú maticu** a **Spodnú maticu** a ako smer nastavte **Z**. Projekt uložte. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky krokovania.

Nastavte **Počet krokov** na **100** a **Krok pri ukladaní** na **5**.

Nastavte veľkosť kroku na **posun matrice** **0,085** palca.

Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustenie a sledovanie simulácie

3D simulácie je možné spustiť rýchlejšie využitím viacerých procesorov alebo viacerých jadier na jednom procesore. Ak má váš počítač 4 jadrá, kliknite na štítok ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}).

nastavte režim simulácie na **Interaktívny** a vyberte **Pokračovať****Spustiť**  
Nastavte počet procesorov na úlohu na hodnotu **4.** Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) a následne na **![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}). (Pozri [ Fig. L3.13.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/forming_lab3/' | relative_url }}#Fig_L3_13_Run_option_window)).**

Počas behu simulácie kliknite na tlačidlo „Temperature“ (![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }})), aby ste si v grafickom okne mohli prezrieť teploty. Na zviditeľnenie čipov je užitočné použiť režim „Multi object“ (![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }})). 

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky kontroly v režime príspevku

Kliknite na ikonu 3D zrkadlenie ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}). Uistite sa, že je zvolená možnosť **Pridať**, a kliknite na rovinu symetrie objektu. Pridá sa zrkadlovo otočený objekt. Pokračujte v klikaní na rovinu symetrie, kým nevytvoríte celý objekt. Ak urobíte chybu, pridané časti môžete odstrániť pomocou možnosti Vymazať.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0004.jpg' | relative_url }})

Okno 3D zrkadlenia v príspevku na MO

Prejdite jednotlivými krokmi simulácie. Porovnajte výsledky s výsledkami úplného modelu. Výsledky by mali byť v podstate rovnaké.

Poznámka: Pri vykresľovaní krivky závislosti zaťaženia od zdvihu sa zobrazované zaťaženie vzťahuje iba na tento 45° úsek. Dialógové okno Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) obsahuje možnosť Scale, ktorá umožňuje vynásobiť zaťaženie číslom 8, čím sa získa zaťaženie potrebné na vytvorenie celého dielu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0005.jpg' | relative_url }})

Graf zdvihu zaťaženia so stupnicou
