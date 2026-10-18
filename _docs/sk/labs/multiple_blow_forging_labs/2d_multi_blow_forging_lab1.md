---
lang: sk
title: "2D Multifunkčné kovacie laboratórium1"
---

# 2D Multifunkčné kovacie laboratórium1

Zámerom laboratória je ukázať používateľovi, ako pripraviť simuláciu viacnásobného úderu v DEFORMÁCII pre následné údery kladivom pomocou operácie 2D Multi Blow Forging s adaptívnou funkciou DEFORMÁCIE ohrevu. Simulácia sa vykonáva ako 2D neizotermická simulácia.

1.1. Vytvorenie nového problému

1.2. Prevádzka pridávania

1.3. Definujte nastavenia procesu

1.4. Definovanie fúkacieho stola

1.5. Výber typu geometrie

1.6. Ovládacie prvky simulácie

1.7. Načítanie materiálu

1.8. Pridávanie objektov

1.9. Definujte obrobok

1.10. Definovanie hornej matrice

1.11. Definovanie spodnej matrice

1.12. Umiestnenie

1.13. Generovanie kontaktov

1.14. Stránka krokových ovládacích prvkov

1.15. Generovanie databázy

1.16. Spustenie simulácie

1.17. Následné spracovanie výsledkov

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI, ako je znázornené na obr. 2DMBL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORMÁCIA hlavného grafického používateľského rozhrania

Vytvorte nový problém buď výberom * * Súbor * *![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 2DMBL1.2. Pomocou prepínača vyberte možnosť „**Integrated Manufacturing Process** “ (Integrovaný výrobný proces * *) a systém jednotiek ako „**English** “ (Angličtina * *). Definujte názov problému ako "**2D_MB_Forging** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

V dialógovom okne Nový projekt sa otvorí sprievodca viacerými operáciami, v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**2D_MB_Forging * * “. Ak chcete pridať prvú operáciu ako operáciu 2D viacfúknutého kovania, začiarknite políčko, ako je znázornené na obr. 2DMBL1.2. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0002.jpg' | relative_url }})

Otváracie okno nového projektu sprievodcu MO

## Pridanie operácie

Sprievodca viacnásobnou operáciou sa otvorí pridaním operácie 2D Multi Blow Forging automaticky, ako je znázornené na obr. 2DMBL1.3, ak sa používateľ rozhodne použiť ju ako prvú operáciu. Operáciu je možné pridať aj kliknutím na tlačidlo 2D Multi Blow Forging Operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo presunutím myšou do editora operácií.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0003.jpg' | relative_url }})

Pridávanie operácií viacnásobného vyfukovania

## Definovať nastavenia procesu

Definujte nastavenia procesu, ako je uvedené nižšie (pozri obr. 2DMBL1.4).

* Na stránke Proces definujte * * Stlačte * *** Energy * * ako **240****Klb-in**.

* Uistite sa, že metóda špecifikácie energie je **Pomer k maximálnej energii** (%).

* Zapnite začiarkavacie políčko **Použiť*** zotrvanie **, definujte * * zotrvanie ** ** čas ** ako ** 1 ** s, čas na krok ako * * 0,2 * * a * * teplo * ***prenos* ***koeficient** ako **0,0003**.

* Zapnite **Reheat****začiarknite****box** a definujte **reheat * ***teplotu** ako **2150°** F.

* Zapnite**Použite otáčanie obrobku ** na otáčanie obrobku medzi údermi a * * Inicializujte * * **namáhanie pri opätovnom zahriatí ** začiarkavacie políčka na inicializáciu namáhania na nulu pri opätovnom zahriatí.

* Zapnite **Použite zaškrtávacie políčko Heating Simulation**, definujte **Heating* ** time * * as * *800** sec, Heat ** * * step ** as ** 1 ** * sec ** , na simuláciu tepelných strát pri prenose z lisovníc do pece a naopak definujte * * Transfer-in-time ** as ** 3 ** sec, Transfer-out-time as * * 3 * * sec a **Transfer time* ** *step** as **1** sec.

* Zapnite **Použite začiarkavacie políčko Adaptívne opätovné ohrievanie**, aby systém automaticky identifikoval, kedy začať opätovné ohrievanie na základe teploty predvalku na konci fúkania, Definujte * * horný ** ** limit ** ako ** 2150° * * F, * * dolný limit * * ako * * 1750° * * F a * * Teplota * ** * do * ** zastavenie * * ** opätovného ohrievania ** ako **1950°** F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre stôl fúkania.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0004.jpg' | relative_url }})

Stránka procesu

## Definovanie fúkacieho stola

V tabuľke Fúkania definujte * * číslo * ****z*** *zásahov* * ako * * 9 * * a definujte zvyšok nastavení, ako je uvedené na obr. 2DMBL1.5. Maximálna dostupná energia pre tento úder je definovaná pod % úderu a tiež účinnosť každého úderu je definovaná pod účinnosťou. Obrobok sa na konci každého úderu prevráti. ![]({{ '/assets/icons/pre_icons/mo_reheat_check_box.jpg' | relative_url }}) pod Reheat označuje, že sa kontroluje adaptívny ohrev a systém rozhodne, kedy sa má obrobok ohriať. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0005.jpg' | relative_url }})

Definovať nastavenia tabuľky fúkania

## Výber typu geometrie

Vyberte typ geometrie ako **2D osovo symetrický**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0006.jpg' | relative_url }})

Stránka výberu typu geometrie

## Ovládacie prvky simulácie

V tomto laboratóriu, keď nastavujeme jednoduchý neizotermický problém, v ovládacích prvkoch simulácie nechajte zapnuté režimy ** Prenos tepla *** * a ** Deformácia * * (pozri obr. 2DMBL1.7). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0007.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie

## Načítanie materiálu

Načítajte materiál „**AISI-4340[1550-2200F (850-1200C)]** “ z knižnice materiálov DEFORM, **Oceľ * * kategória pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). Môžete to urobiť, ako je znázornené nižšie, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. 2DMBL1.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku objektu.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0008.jpg' | relative_url }})

Okno knižnice materiálov

pridávanie objektov

Pre túto operáciu požadujeme tri objekty, preto v okne Objekt ponechajte tri objekty, ktoré sú predvolene pridané, inak pridajte 3 objekty pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (pozri obr. 2DMBL1.9.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0009.jpg' | relative_url }})

Okno Pridávanie objektov

## Definovať obrobok

Na stránke obrobku definujte teplotu obrobku ako * * 1950 * * ° F a vyberte typ objektu ako **Plast * *, ako je znázornené na obr. 2DMBL1.10. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0010.jpg' | relative_url }})

Stránka obrobku

### Načítanie geometrie obrobku

V okne Geometria načítajte **MB_Forging_workpiece.geo ** súbor geometrie z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete tiež importovať pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru), ako je znázornené na obr. 2DMBL1.11. Geometria sochora sa nachádza v priečinku DEFORMÁCIE inštalácie\2D\LABS. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku s povrchovou sieťou.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0011.jpg' | relative_url }})

Stránka geometrie obrobku

### Generovanie pletiva pre obrobok

Definujte **Cieľový počet prvkov* * ako * *400** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Vygeneruje sa sieť s približne 400 prvkami, ako je znázornené na obr. 2DMBL1.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku materiálu.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0012.jpg' | relative_url }})

Generovanie pletiva obrobku

### Priradiť materiál obrobku

V okne zoznamu materiálov vyberte zo zoznamu „**AISI-4340 [1550-2200F (850-1200C)]** “, ako je znázornené na obr. 2DMBL1.13. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Podmienky ohraničenia.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0013.jpg' | relative_url }})

Výber materiálu obrobku

### Obrobok BCC

Na stránke BCC skontrolujte predvolenú priradenú deformáciu BCC pre ľavú stranu obrobku v smere X, predvolené BCC sú priradené automaticky z dôvodu výberu typu problému ako osovo symetrického (pozri obr. 2DMBL1.14.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Top die.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0014.jpg' | relative_url }})

Stránka BCC obrobku

## Definovanie hornej matrice

Na hornej strane matrice ( obr. 2DMBL1.15.) vyberte Typ objektu ako **Pevný** a udržujte teplotu ako **300** ° F, nebudeme mriežkovať matrice v tomto laboratóriu, pretože nemáme záujem o teplotu matrice. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0015.jpg' | relative_url }})

Horná strana matrice

### Geometria hornej formy

V okne Geometria načítajte **MB_Forging_Top_die.geo ** súbor geometrie z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať aj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru), ako je znázornené na obr. 2DMBL1.16. Geometria sa nachádza v priečinku DEFORMÁCIE\2D\LABS. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že geometria je v poriadku. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku pohybu hornej matrice.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0016.jpg' | relative_url }})

Stránka geometrie hornej matrice

### Pohyb hornej matrice

Používateľ môže použiť šablónu na kovanie s viacerými údermi pre kladivové aj skrutkové lisy. V tomto laboratóriu budeme používať * * kladivo * * , preto vyberte * * kladivo * *** pohyb * * typ a definujte * * energiu * *** ako * ** 240 * * ** Klb-in * * a * * hmotnosť * * ako * * 0,025 * *** Klb-s ^2/in**, ako je znázornené na obr. 2DMBL1.17. Keďže ide o viacnásobnú simuláciu vyfukovania, konštantné hodnoty účinnosti vyfukovania pre definíciu viacnásobných vyfukovaní sú povolené len v tabuľke vyfukovania. Ak používateľ používa účinnosť fúkania ako funkciu sily, údaje o funkcii účinnosti sa môžu definovať v okne pohybu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Spodná matrica

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0017.jpg' | relative_url }})

Stránka pohybu hornej matrice

## Definovanie spodnej matrice

Na stránke Spodná matrica vyberte Typ objektu ako **Pevný** a definujte **teplotu** ako **300** °F (pozri obr. 2DMBL1.18.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku geometrie

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0018.jpg' | relative_url }})

Spodná strana matrice

### Definícia geometrie spodnej matrice

V okne Geometria načítajte **MB_Forging_Bottom_die.geo** súbor geometrie z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice). Geometria sa nachádza v priečinku DEFORMÁCIE\2D\LABS. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že geometria je v poriadku. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až do stránky Positioning.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0019.jpg' | relative_url }})

Definícia geometrie spodnej matrice

VIZUÁL PRE

V tomto nastavení operácie použijeme možnosť **Automatická* ** *poloha * * na umiestnenie objektov. Na stránke Polohovanie vyberte smer polohovania ako Z (Y) - smer a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}), umiestni objekty tak, ako je znázornené na obr. 2DMBL1.20. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Kontakt.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0020.jpg' | relative_url }})

Umiestnenie objektov

## Generovanie kontaktov

Vyberte **user****type** contact a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Pridá vzťah medzi predvalkom, hornou matricou a spodnou matricou, ako je znázornené na obr. 2DMBL1.21. Keďže matrice sú tuhé a polotovar je plastový, horné a dolné matrice sa považujú za hlavné a polotovar za otroka. Aby bolo možné predpovedať záhyb počas deformácie, pre Billet bude priradený vlastný kontakt.

Definujte **strihové* ** *trenie** hodnotu * * 0,2 * * a * * teplo * *** prenos * ***koeficient** ako **0,004** pre **hornú matricu** a **obrobok** vzťah.

Definujte **strihové* ***trenie** hodnotu * * 0,25 * * a * * teplo * *** prenos * ***koeficient** ako **0,004** pre **spodnú matricu** a **obrobok** vzťah.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna Inter-Object, pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určíte vhodnú toleranciu kontaktu (vypočíta sa hodnota približne0,00123929 ") a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vygenerovanie kontaktu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Krok, pretože na definovanie tejto simulácie nie sú potrebné žiadne ovládacie prvky zastavenia

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0021.jpg' | relative_url }})

Vzťahy medzi objektmi

## Stránka krokových ovládacích prvkov

V krokových ovládacích prvkoch definujte **počet krokov** ako **400** , **krok*** * prírastok * * 10 * * a **čas****prírastok** 0,0001 **, ako je znázornené na obr. 2DMBL1.22. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre generovanie DB.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0022.jpg' | relative_url }})

Stránka krokových ovládacích prvkov

## Generovanie databázy

Po úplnom nastavení problému je posledným krokom vygenerovanie databázového súboru. FEM engine (časť DEFORM®, ktorá vypočítava riešenie) používa databázový súbor na uloženie riešení konečných prvkov pre daný problém. Keď vygenerujete databázu v predprocesore DEFORM MO, všetky informácie definované v predprocesore (ako sú vlastnosti materiálu, ovládacie prvky pohybu, geometrie objektu atď.) sa prenesú do databázového súboru.

Na stránke Generate DB môžeme pozorovať zhrnutie nastavenia simulácie prevádzky. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) skontrolujete program, aby ste zistili, či v nastavení problému niečo chýbalo. Počas procesu kontroly správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad keď zabudnete definovať akékoľvek údaje o materiáli).

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) vygenerujete databázu. Po dokončení zápisu databázy prepnite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

## Spustenie simulácie

Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. 2DMBL1.23. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať z posledného kroku** “ a potom vyberte režim simulácie ako **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0023.jpg' | relative_url }})

Okno Spustiť simuláciu

Priebeh simulácie je možné monitorovať počas jej priebehu tak, že sa pozriete na kartu Simulačná správa a Simulačná grafika z oblasti grafického zobrazenia v režime simulácie. Pokiaľ je možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) začiarknutá na karte Simulation Message (Správa simulácie), ktorá je predvoleným nastavením, súbor správy sa automaticky obnoví.

Súbor Správa poskytuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a tiež poskytuje informácie o tom, ako dobre simulácia prebieha.

Po dokončení simulácie bez akýchkoľvek problémov sa na koniec súboru správy pridá nasledujúca správa:PROGRAM ZASTAVENÝ!

AKTUÁLNY ČAS 41,8737368

AKTUÁLNY MIESTNY ČAS 1.0085369 DOSIAHOL STANOVENÝ LIMIT 1.0085369 (pozri obr. 2DMBL1.24.)

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0024.jpg' | relative_url }})

Karta správy simulácie

## Následné spracovanie výsledkov

Po dokončení simulácie prepnite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) a zobrazte výsledky, otvorí sa procesor MO post.

Prehrajte animáciu a prejdite preklopením obrobku (otáčanie obrobku).

Priamo kliknutím na ikony stavových premenných môže používateľ vykresliť dôležité stavové premenné obrysové grafy, ako je znázornené na obr. 2DMBL1.25. a obr. 2DMBL1.26.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0025.jpg' | relative_url }})

Efektívna krivka napätia

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0026.jpg' | relative_url }})

Kmeň Efektívny graf

Používateľ môže prejsť viacerými operáciami úderov a opätovného ohrevu výberom konkrétneho kroku z prehliadača krokov a prehrávaním krokov. Z poradia operácií prehliadača Step môžeme pozorovať, že adaptívne opätovné zahriatie sa spustilo po operácii BL5-DWL, keď minimálna teplota objektu klesla pod minimálnu teplotu adaptívneho opätovného zahriatia 1750° F. Aj adaptívna simulácia tepla sa zastavila, keď obrobok dosiahol teplotu zastavenia opätovného ohrevu 1950° F. (pozri obr. 2DMBL1.27.)

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0027.jpg' | relative_url }})

Prehliadač krokov indikujúci adaptívne simulácie opätovného ohrevu

Teplotný obrys obrobku pred a po adaptívnom ohreve, ako je znázornené na obr. 2DMBL1.28. Všimnite si, že pred začatím adaptívneho ohrevu je minimálna teplota predvalku 1740° F (špecifikovaný limit je 1750° F).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0028.jpg' | relative_url }})

Obrys teploty obrobku pred a po adaptívnom ohreve po BL5-DWL
