---
lang: sk
title: "Laboratórium tvarovania 3"
---

# Laboratórna úloha č. 3. Laboratórna úloha na 3D ozubené kolesá s výpočtami teploty v programe Forming 

V tomto cvičení budeme modelovať kovanie toho istého polotovaru ozubeného kolesa, tentoraz však s výpočtami teploty, bez počiatočného zúženia a v **3D namiesto 2D (2D cvičenie s ozubenými kolesami)**.

Na simuláciu použijeme systém viacerých operácií:

  * Vyberanie rozžeraveného polotovaru z pece a jeho presun na vzduchu k kováckym nástrojom

  * Uloženie polotovaru na kováčske nástroje

  * Kovanie polotovaru.

Ak sa operácia prevrátenia nevykoná, na vnútornej strane polotovaru ozubeného kolesa vznikne záhyb. Na preskúmanie tohto záhybu použijeme rôzne nástroje na následné spracovanie.

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou prepínača. Zadajte názov úlohy „**Gear_3D_Thermal**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte novú úlohu s využitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami. Zadajte názov projektu **Gear_3D_Thermal** a uistite sa, že políčko „Prvá operácia“ nie je zaškrtnuté, keďže operáciu pridáme neskôr. Ako umiestnenie použite predvolený (domovský) adresár, ako je znázornené na obr. L3.1. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste pridali projekt. Na tento laboratórny cvičebný projekt sa budeme odvolávať v budúcich laboratórnych cvičeniach, preto je dôležité použiť uvedený názov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0001.jpg' | relative_url }})

Nové okno projektu MO

### Pridať operácie

Pridajte tri operácie z programu Explorer:

  1. [3D] Heat Transfer Express

  2. [3D] Prenos tepla a

  3. [3D] Tvarovanie

  
Dvojitým kliknutím na názov prvej operácie ho zmeňte na **Air Transfer**. Názov druhej operácie zmeňte na **Rest on Die**. Názov tretej operácie „Forming“ ponechajte bez zmeny (pozri obr. L3.2.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0002.jpg' | relative_url }})

Premenované názvy operácií v editore operácií

Kliknite pravým tlačidlom na **obrobok** a vyberte možnosť **Preniesť objekt do všetkých operácií**. Podobne kliknite pravým tlačidlom na **hornú maticu** a **spodnú maticu** a pre oba objekty použite možnosť **Preniesť objekt do nasledujúcej operácie** (pozri obr. L3.3.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0003.jpg' | relative_url }})

Editor operácií po odovzdaní objektov nasledujúcim operáciám

### Definícia pojmu „prenos vzduchu“

V Editoru operácií kliknite na operáciu **Air****Transfer**. V tomto cvičení budeme používať diel **Whole**. Skontrolujte, či je typ ohrevu nastavený na **Transfer**. Posuvníky **Presnosť** a **Zložitosť** nechajte v polohe **Stredná** (pozri obr. L3.4.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Obrobok.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0004.jpg' | relative_url }})

Okno procesu

### Definovanie všeobecných údajov o obrobku

Nastavte teplotu obrobku na **2250** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

#### Vytvorenie geometrie obrobku z primitívu

Definujte geometriu ako základný **valec** s **priemerom** **5** palcov, **výškou** **8,1** palca a **polomerom rohu** **0,2** palca. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa otvorila stránka s sieťou.

#### Vytvorenie siete pre obrobok

Vytvorte sieť s použitím predvoleného nastavenia **80000** prvkov.

#### Priradiť materiál k obrobku.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice). Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom **AISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Kliknite na položku **AISI-8620[1550–2200 °F (850 – 1200 °C)]** v okne s materiálmi, aby ste materiál priradili k obrobku. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

#### Obrobok BCC

Okrajové podmienky pre výmenu tepla s okolím by sa mali definovať automaticky. Overte to tak, že v stromovej štruktúre okrajových podmienok kliknete na položku **Definované** a skontrolujete, či sú všetky plochy zelené, ako je znázornené na obr. L3.5. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Heat Condition“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0005.jpg' | relative_url }})

Okno BCC obrobku

### Nastaviť teplotné podmienky

Nastavte **čas prenosu** na 5 sekúnd, potvrďte predvolenú teplotu prostredia a koeficient konvekcie (pozri obr. L3.6.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky simulácie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0006.jpg' | relative_url }})

Okno s nastavením teploty

### Ovládacie prvky simulácie

Použite predvolenú definíciu kroku a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte databázu.

### Vytvoriť databázu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}). Ak sa na karte „Správy“ nenachádzajú žiadne chyby ani varovania, pokračujte a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Teraz kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste prešli na ďalšiu operáciu.

### Operácia „Rest on Die“

Pri druhej operácii bude typ prenosu tepla **Odvod tepla cez matricu**. Tým sa simuluje únik tepla z obrobku do nástroja od momentu jeho umiestnenia na spodnú matricu až do dokončenia zdvihu lisu. Pri tejto operácii by mal obrobok priliehať k spodnej matrici, zatiaľ čo horná matrica by mala byť umiestnená v určitej vzdialenosti od obrobku.

Poznámka: Forma typu „Dwell on“ je určená na prenos tepla po kovaní a využíva vyššie koeficienty prenosu tepla, ktoré zodpovedajú úplnejšiemu kontaktu s formou.

### Typ prenosu tepla

V predvolenom nastavení je typ prenosu tepla nastavený na „Rest on die“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Process condition“

### Prevádzkové podmienky

**Doba odpočinku** bude **4** sekundy. Potvrďte predvolenú teplotu a koeficient konvekcie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Objekt“.

### Zoznam objektov

Overte, či sa v tabuľke nachádzajú 3 objekty. Ak nie, trikrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (vložiť objekt), aby ste pridali 3 objekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Obrobok“.

### Obrobok

Všetky údaje o obrobku sa načítajú z výsledkov prvej operácie v databáze. Preskočte obrobok a prejdite na hornú maticu.

### Hlavná stránka „Top die“

Skontrolujte, či je teplota hornej matrice **300** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou hornej matrice.

#### Import geometrie hornej matrice

Naimportujte geometriu matrice ozubeného kolesa zo súboru STL, naimportujte súbor „**gear top die.****STL**“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať geometriu zo súboru) tak, že vyhľadáte cestu k súboru s geometriou v inštalačnej zložke v adresári \**Tutorials******. Matrice je orientovaná pozdĺž inej osi ako obrobok. Tým sa budeme zaoberať v neskoršom kroku.

Pri spustení simulácie tvárnenia použijeme riadenie zastavenia na základe vzdialenosti medzi formami, ale keďže nástroje sú definované v aktuálnej operácii, je potrebné teraz definovať aj referenčné body. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Vlastnosti.

#### Hlavné vlastnosti matrice

Vyberte **Vlastnosti![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Referencia** Použiť súradnice a vyberte bod na plochu s výrezom (pozri obr. L3.7.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku spodnej formy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0007.jpg' | relative_url }})

Okno „Hlavné vlastnosti lisovacej formy“

### Všeobecná stránka o spodnej matrici

Skontrolujte, či je teplota spodnej matrice **300** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou spodnej matrice.

#### Import geometrie spodnej matrice

Načítajte geometriu spodnej matrice ozubeného kolesa zo súboru STL. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a otvorte (načítajte) súbor „**gear bottom die.****STL**“ tak, že vyhľadáte cestu k súboru s geometriou v inštalačnom priečinku v adresári \Tutorials. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Vlastnosti.

#### Vlastnosti spodnej matrice

Vyberte **Vlastnosti![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Referencia** Použiť súradnice a vyberte bod na medzere medzi stranami (pozri obr. L3.8.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s polohovaním.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0008.jpg' | relative_url }})

Okno „Vlastnosti spodnej matrice“

### Polohovacie matrice

V tomto bode je obrobok orientovaný pozdĺž osi Z a nástroje sú orientované pozdĺž osi Y.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}).

Najskôr otočte matrice tak, aby boli orientované pozdĺž osi Z. Nastavte metódu na **Rotácia**. Nastavte nasledujúce parametre:

Polohovací objekt: **Horná matrica**.

Osa: X

Stred otáčania: Definovaný používateľom (0,0,0)

Uhol: 90 stupňov

Chceme otáčať obe matrice spoločne, preto prejdite na kartu **Coupled** a zaškrtnite políčko „Bottom Die“. Tým sa prepojí akékoľvek nastavenie polohy (pozri obr. L3.9.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0009.jpg' | relative_url }})

Umiestnenie hornej matrice s prepojeným spodným objektom

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) otočte nástroje tak, aby boli zarovnané s obrobkom.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0010.jpg' | relative_url }})

Poloha objektov po otočení

V súčasnosti sú nástroje aj obrobok vyrovnané pozdĺž osi Z, avšak nástroje sú od seba príliš blízko, ako je znázornené na obr. L3.10. Ďalším krokom je posunutie hornej matrice do polohy „hore“, ďalej od obrobku. 

**Zrušte zaškrtnutie** možnosti **spojeného** polohovania a následne umiestnite **Top****Die** o vzdialenosť **12** in pomocou funkcie **Offset** v smere **Z**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0011.jpg' | relative_url }})

Horná matrica po posunutí polohy

Nakoniec sa musíme uistiť, že spodná forma bude správne priliehať k obrobku. Keďže obrobok sa pri tejto operácii načítava z databázy, nemôžeme použiť bežné polohovanie. Môžeme však využiť naplánované polohovanie, ktoré sa dokončí počas behu projektu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte dialógové okno Polohovanie objektu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Naplánované polohovanie.

### Plánované umiestnenie

Pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte naplánovanú polohovaciu operáciu a pomocou funkcie „Interference“ nastavte polohu **spodnej časti** **matrice** vo smere **Z** voči **obrobku**.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a na stránke naplánovaného polohovania by sa mala zobraziť táto naplánovaná operácia (pozri obr. L3.12.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre kontakt

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0012.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Kontakt

V okne „Kontakt“ priraďte predvolené vzťahy medzi kontaktmi a uistite sa, že sú zaškrtnuté možnosti „Inicializovať“ a „Generovať“ pre naplánovaný kontakt. Trenie nie je potrebné definovať, pretože táto operácia spočíva výlučne v prenose tepla. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ovládacie prvky krokov“.

### Ovládacie prvky krokov

V nastaveniach zastavenia je trvanie procesu už nastavené na 4 sekundy. Pri prenose tepla s kontaktom vykonajte 10 krokov za sekundu. Pre 4-sekundový model teda spustite 40 krokov s časovým krokom 0,1 s. Nastavte **počet krokov** na **40** a **konštantný čas na krok** na **0,1** s. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nevytvorí stránka databázy.

### Vytvorenie databázy

Prebehne kontrola údajov. Zobrazí sa správa, že databáza nebude vytvorená. Databáza pre túto operáciu sa vytvorí automaticky po dokončení simulácie prvej operácie.

### Tvarovacia operácia

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) alebo jednoducho kliknite na dlaždicu „Tvarovanie“ v editore operácií, aby ste nastavili operáciu tvarovania.

Všetky objekty sa načítajú z databázy na konci predchádzajúcej operácie „Rest on Die“, takže stačí len nastaviť:

  * Ovládanie pohybu

  * Polohovanie

  * Vzťahy medzi objektmi

  * Simulácia a ovládacie prvky na zastavenie

### Priradiť pohyb hornej matrice

V stromovej štruktúre operácií kliknite na stránku **Top****Die****Movement** a nastavte **rýchlosť** na konštantnú hodnotu **3** palcov za sekundu v smere **-Z**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Scheduled Positioning“.

### Plánované polohovanie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a definujte **polohu kolízie** medzi **hornou matricou** a **obrobkom** v smere **-Z**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Kontakt“.

### Vzťah medzi objektmi

Kliknite na **Kontakt** a nastavte vzťahy medzi objektmi s trením **0,3**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky zastavenia.

### Priradiť ovládacie prvky zastavenia a krokovania

V časti „Ovládacie prvky zastavenia“ nastavte kritérium **Vzdialenosť matrice pri zastavení** na hodnotu **0,25** palca, pričom ako referenčné objekty použite **Hornú matricu** a **Spodnú matricu** a ako smer nastavte **Z**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky krokovania.

Nastavte **počet krokov** na **100** a **krok pri ukladaní** na **5**.

Nastavte veľkosť kroku na **posun matrice** **0,085** palca. Uložte projekt.

Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustenie a sledovanie simulácie

3D simulácie je možné spustiť rýchlejšie využitím viacerých procesorov alebo viacerých jadier v jednom procesore. Ak má váš počítač 4 jadrá, kliknite na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}).

nastavte režim simulácie na **Interaktívny** a vyberte **Pokračovať****Spustiť**  
nastavte MPI 3D na hodnotu **4.** (Pozri obr. L3.13.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0017.jpg' | relative_url }})

Spustiť okno s možnosťami

Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) a následne na ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

Počas behu simulácie kliknite na tlačidlo „Temperatúra“ (![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }})), aby ste si v grafickom okne mohli prezrieť teploty. Odporúča sa použiť režim viacerých objektov (![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }})), aby sa formy stali priehľadnými. 

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky kontroly v režime príspevku

Prejdite jednotlivými krokmi a sledujte, ako sa súčiastka deformuje.

Kliknite na ikonu „Slicing ![]({{ '/assets/icons/post_icons/mo_slicing_option.jpg' | relative_url }})“. Obrobok a nástroje budú ohraničené žltým rámčekom. Kliknite na žltú čiaru tohto rámčeka. Objekty budú rozrezané kolmo na túto čiaru (ak sa matrice nerozrežú, skontrolujte, či je zaškrtnutá možnosť „slice all objects“). Posunutím modrého posuvníka doľava alebo doprava posuniete rovinu rozrezania dopredu alebo dozadu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0014.jpg' | relative_url }})

Okno na rezanie v príspevku na MO

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte dialógové okno na rozdelenie.

Zaznačte teplotu ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) v obrobku. Prejdite do dialógového okna Nastavenie ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) a nastavte mierku na Užívateľ s minimálnou hodnotou **1000** °F a maximálnou hodnotou **2500** °F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Kliknite pravým tlačidlom myši na farebný pruh **Teplota** v grafickom okne a vyberte **Farebný pruh****Typ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Teplota**. Teploty sa teraz zobrazujú pomocou intuitívnejšej farebnej schémy.

Kliknite na možnosť „Sledovanie bodu“ (![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }})). Funkcia sledovania bodu umožňuje sledovať pohyb bodu, ako aj vývoj stavových premenných v danom bode. Vyberte niekoľko bodov na rezanom úseku obrobku. 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0015.jpg' | relative_url }})

Okno sledovania bodov v príspevku MO

Kliknite na ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}). Program bude chvíľu trvať, kým zmeria teploty v týchto bodoch, a následne zobrazí výsledok v grafe.
