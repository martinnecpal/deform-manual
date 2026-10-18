---
lang: sk
title: "3D multifunkčné vyfukovacie kovacie laboratórium1"
---

# 3D Multifunkčné kovacie laboratórium

Zámerom laboratória je ukázať používateľovi, ako pripraviť simuláciu viacnásobného úderu v DEFORMÁCII pre tri po sebe nasledujúce údery kladivom pomocou operácie 3D Multi Blow Forging s adaptívnou funkciou DEFORMÁCIE ohrevu. Simulácia sa vykonáva ako 3D neizotermická simulácia.

1.1. Vytvorenie nového problému

1.2. Prevádzka pridávania

1.3. Definovanie nastavení procesu

1.4. Definovanie fúkacieho stola

1.5. Ovládacie prvky simulácie

1.6. Načítanie materiálu z knižnice

1.7. Pridávanie objektov

1.8. Definovanie obrobku

1.8.1. Definovanie geometrie obrobku

1.8.2. Generovanie pletiva pre obrobok

1.8.3. Priradenie materiálu obrobku

1.8.4. Priradenie BCC

1.9. Definovanie hornej matrice

1.9.1. Definovanie geometrie hornej matrice

1.9.2. Definovanie pohybu hornej matrice

1.10. Definovanie spodnej matrice

1.10.1. Definovanie geometrie spodnej matrice

1.11. Umiestnenie

1.12. Generovanie kontaktov

1.13. Krokové ovládacie prvky

1.14. Generovanie databázy

1.15. Spustenie simulácie

1.16. Po spracovaní výsledkov

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Nové vyskakovacie okno Problém

Vytvorte nový problém buď výberom * * Súbor * *![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Okno Nastavenie problému sa zobrazí, ako je znázornené na prepínači [Fig. 3DMBL1.1.]() Vyberte prepínač „* * Integrovaný výrobný proces * * “ a systém jednotiek ako „**Angličtina * * “ pomocou prepínača. Definujte názov problému ako "**3D_MB_Forging** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

V dialógovom okne Nový projekt sa otvorí sprievodca viacerými operáciami, v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „* * 3 ** * *D_MB_Forging * * “. Ak chcete pridať prvú operáciu ako **3D viacfúknuté kovanie * ***, začiarknite** začiarkavacie políčko * *, ako je znázornené na obr. 3DMBL1.2. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0002.jpg' | relative_url }})

Sprievodca MO Okno otvárania nového projektu

Používateľ môže tiež zmeniť systém jednotky a umiestnenie súboru uloženia projektu (pozri obr. 3DMBL1.2.). Pomocou možnosti kopírovať existujúci projekt môžeme importovať predchádzajúce uložené projekty ako nový projekt. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

## Pridanie operácie

Sprievodca viacnásobnou operáciou sa otvorí pridaním operácie 3D Multi Blow Forging automaticky, ak sa používateľ rozhodne použiť ju ako prvú operáciu, ako je znázornené na obr. 3DMBL1.3. Operáciu môžete pridať aj kliknutím na tlačidlo 3D Multi Blow Forging Operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj presunutím myšou do editora operácií.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0003.jpg' | relative_url }})

Pridaná operácia viacnásobného vyfukovania do editora operácií

## Definovanie nastavení procesu

Definujte nastavenia procesu, ako je uvedené nižšie (pozri obr. 3DMBL1.4).

* Na stránke Proces definujte Press * * Energy * * ako **240** Klb-in.

* Zapnite začiarkavacie políčko Použiť zotrvanie, definujte * * zotrvanie ** ** čas ** ako * * 1 * * s, * *čas na krok* * ako * *0,2** a ** koeficient prestupu tepla ** ako **0,0003**.

* **Otočte****na** Použite **obrobok****otočenie** začiarkavacie políčko.

* **Zapnite začiarkavacie políčko **** * ** *** * * ** * * * * * * ** * * *** ** * ** * * **2150* ** F.

* * * Zapnite * * * * ** ** ** * * * ** *** * * * * *** ** * * * ** ** * 800 * * * ** * * * * * * * * * * ** *** * *** ** * * * ** * * * * ** * * * ** * * * * * ** * * * ** ** ** * * * * 3 *** * * * * ** * * * ** * * * ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ** * * * * ** * * * ** * * * ** * * * * * ** * * * ** * * * * ** * * * ** * * * * * ** * * * * * * * ** * * * ** * * * ** * * * *

* **Zapnite začiarkavacie políčko Použiť adaptívne opätovné ohrievanie**, aby systém automaticky identifikoval, kedy začať opätovné ohrievanie na základe teploty predvalku na konci fúkania, definujte * * Horný limit ** ako ** 2150 ** F, * * Dolný limit * * ako * * 1750 * * F a * *Teplota na zastavenie opätovného ohrievania ** ako **1950** F.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0004.jpg' | relative_url }})

Okno nastavení procesu

## Definovanie fúkacieho stola

V tabuľke Fúkania definujte **počet zásahov** ako**9** a definujte zvyšok nastavení, ako je znázornené na obr. 3DMBL1.5.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0005.jpg' | relative_url }})

Okno nastavení fúkacieho stola

Ak chcete definovať nastavenia otáčania obrobku, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) vedľa nedefinovaného stavu parametra a definujte pohyb otáčania hore dnom pre obrobok okolo jeho stredu pozdĺž osi Z, ako je znázornené na obrázku 3DMBL1.6. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0006.jpg' | relative_url }})

Okno definovania parametra rotácie

## Ovládacie prvky simulácie

V tomto laboratóriu vám ukážeme, ako nastaviť jednoduchý neizotermický problém. Takže v ovládacích prvkoch simulácie nechajte zapnutý režim prenosu tepla aj režim deformácie (pozri obr. 3DMBL1.7.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0007.jpg' | relative_url }})

14 Okno riadenia simulácie

## Načítanie materiálu z knižnice

Načítajte materiál „**AISI-4340[1550-2200F (850-1200C)]** “ z knižnice materiálov DEFORM, **Oceľ * * kategória pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). Môžete to urobiť tak, ako je znázornené nižšie, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. 3DMBL1.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Objekt.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0008.jpg' | relative_url }})

Okno knižnice materiálov

pridávanie objektov

Pre túto operáciu sme požadovali tri objekty, preto v okne Objekt ponechajte tri objekty, ktoré sú predvolene pridané, inak pridajte 3 objekty, ako je znázornené na obr. 3DMBL1.9, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0009.jpg' | relative_url }})

Okno Pridávanie objektov

## Definovanie obrobku

Na domovskej stránke obrobku definujte teplotu obrobku ako * * 1950 * * F a vyberte Typ objektu ako * * Plast * *, ako je znázornené na obr. 3DMBL1.10. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0010.jpg' | relative_url }})

Okno obrobku

### Definovanie geometrie obrobku

V okne Geometria načítajte **MB_Forging_workpiece.geo** súbor geometrie z knižnice pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Skontrolujte geometriu pomocou možností ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) pre neplatné polygóny a počet povrchov (pozri obr. 3DMBL1.11.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku s povrchovou sieťou.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0011.jpg' | relative_url }})

Definovanie geometrie obrobku

### Generovanie pletiva pre obrobok

Definujte cieľový počet prvkov ako * * 25000 * * a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Vygeneruje sa sieť s približne 22 000 prvkami (pozri obr. 3DMBL1.12.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku materiálu.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0012.jpg' | relative_url }})

Generovanie pletiva obrobku

### Priradiť materiál obrobku

V okne zoznamu materiálov vyberte ** AISI-4340 [1550-2200F (850-1200C)]** zo zoznamu, ako je znázornené na obr. 3DMBL1.13. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0013.jpg' | relative_url }})

Okno priradenia materiálu obrobku

### Priradenie BCC

Na stránke BCC skontrolujte predvolenú priradenú deformáciu BCC pre obrobok, predvolená BCC je priradená automaticky na základe typu geometrickej symetrie (pozri obr. 3DMBL1.14.). Predvolený BCC je v poriadku, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) unitl Top die page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0014.jpg' | relative_url }})

Okno obrobku BCC

## Definovanie hornej matrice

Na hornej strane matrice (pozri obr. 3DMBL1.15.) vyberte Typ objektu ako * * Pevný * * a udržujte teplotu ako * * 300F * *, pretože v tomto laboratóriu nebudeme matrice mriežkovať, pretože nás teplota matrice nezaujíma. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0015.jpg' | relative_url }})

Okno objektu hornej matrice

### Definovanie geometrie hornej formy

V okne Geometria načítajte **MB_Forging_Top_die.geo** súbor geometrie z knižnice pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Skontrolujte geometriu pomocou možností ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) pre neplatné polygóny a číslo povrchu (pozri obr. 3DMBL1.16.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po hornú stranu pohybu matrice.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0016.jpg' | relative_url }})

Okno geometrie hornej matrice

### Definovanie pohybu hornej matrice

Používateľ môže použiť šablónu na kovanie s viacerými údermi pre kladivové aj skrutkové lisy. V tomto laboratóriu budeme používať kladivo, preto vyberieme typ pohybu kladiva a definujeme energiu ako 240 Klb-in a hmotnosť **0,025** Klb-s^2/in (pozri obr. 3DMBL1.17.). Keďže ide o viacnásobnú simuláciu vyfukovania, konštantné hodnoty účinnosti vyfukovania pre definíciu viacnásobných vyfukovaní sú povolené len v tabuľke vyfukovania. Ak používateľ používa účinnosť fúkania ako funkciu sily, údaje o funkcii účinnosti sa môžu definovať v okne pohybu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Spodná matrica.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0017.jpg' | relative_url }})

Okno pohybu hornej matrice

## Definovanie spodnej matrice

Na stránke Spodná matrica vyberte Typ objektu ako **Pevný** a definujte teplotu ako **300** F, (pozri obr. 3DMBL1.18.) kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku geometrie.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0018.jpg' | relative_url }})

Okno objektu spodnej matrice

### Definovanie geometrie spodnej matrice

V okne Geometria načítajte **MB_Forging_Bottom_die.geo** súbor geometrie z knižnice pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Skontrolujte geometriu pomocou možností ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) na neplatné polygóny a počet povrchov. (Pozri obr. 3DMBL1.19.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku polohovania.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0019.jpg' | relative_url }})

Okno geometrie spodnej matrice

VIZUÁL PRE

V tomto nastavení operácie použijeme možnosť Automatická poloha na umiestnenie objektov. Na stránke polohovania vyberte smer polohovania ako Z - smer a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}), umiestni objekty tak, ako je znázornené na obr. 3DMBL1.20. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Kontakt.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0020.jpg' | relative_url }})

Okno ovládacích prvkov umiestnenia objektu

## Generovanie kontaktov

Vyberte **user** typ contact a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Pridá vzťah medzi predvalkom, hornou matricou a spodnou matricou, ako je znázornené na obr. 3DMBL1.21. Keďže matrice sú tuhé a polotovar je plastový, horné a dolné matrice sa považujú za hlavné a polotovar za otroka. Definujte hodnotu šmykového trenia 0,2 a koeficient prestupu tepla ako 0,004 pre vzťah hornej matrice a obrobku. Definujte hodnotu šmykového trenia 0,25 a koeficient prestupu tepla ako 0,004 pre spodnú matricu a vzťah obrobku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna Inter-Object, pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určíte vhodnú toleranciu kontaktu (vypočíta sa hodnota približne0,00530 ") a potom kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujete kontakt. Ak otočíte objekty v grafickom okne, uvidíte, že medzi týmito dvoma objektmi bol vygenerovaný kontakt. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Step, pretože na definovanie tejto simulácie nie sú potrebné žiadne ovládacie prvky zastavenia.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0021.jpg' | relative_url }})

Okno definície medzipredmetov

## Ovládacie prvky krokov

V ovládacích prvkoch kroku definujte **počet krokov* * ako * * 400 * *, * * krok * * ** prírastok * * z * * 10 * * a * * čas * *** prírastok * * z * *0,0001 s **. ( Obr. 3DMBL1.22.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre okno generovania DB.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0022.jpg' | relative_url }})

Okno ovládacích prvkov simulácie

##  Generovanie databázy

Po úplnom nastavení problému je posledným krokom vygenerovanie databázového súboru. FEM engine (časť DEFORM®, ktorá vypočítava riešenie) používa databázový súbor na uloženie riešení konečných prvkov pre daný problém. Keď vygenerujete databázu v integrovanom výrobnom procese Deform, všetky informácie definované v predprocesore (ako sú vlastnosti materiálu, ovládacie prvky pohybu, geometrie objektov atď.) sa prenesú do databázového súboru.

V okne Generate DB (Generovať databázu) kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení problému niečo chýba. Počas procesu kontroly správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad keď zabudnete definovať akékoľvek údaje o materiáli).

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) vygenerujete databázu. Po dokončení zápisu databázy prepnite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

## Spustenie simulácie

Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. 3DMBL1.23. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať z posledného kroku** “ a potom vyberte režim simulácie ako **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0023.jpg' | relative_url }})

Okno Spustiť simuláciu

Priebeh simulácie je možné monitorovať počas jej priebehu tak, že sa pozriete na kartu Simulačná správa a Simulačná grafika z oblasti grafického zobrazenia v režime simulácie. Pokiaľ je možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) začiarknutá na karte Simulation Message (Správa simulácie), ktorá je predvoleným nastavením, súbor správy sa automaticky obnoví.

Súbor Správa poskytuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a tiež poskytuje informácie o tom, ako dobre simulácia prebieha.

Po dokončení simulácie bez akýchkoľvek problémov sa na koniec súboru správy pridá nasledujúca správa:„NORMÁLNE ZASTAVENIE: Simulácia sa dokončí a zastaví v časovom kroku zadanom používateľom“. (Pozri obr. 3DMBL1.24.)

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0024.jpg' | relative_url }})

Karta správy simulácie

## Po spracovaní výsledkov

Po dokončení simulácie prepnite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) a zobrazte výsledky, otvorí sa procesor MO post.

Prehrajte animáciu a prejdite otáčaním obrobku (otáčanie obrobku).

Priamo kliknutím na ikony stavových premenných môže používateľ vykresliť dôležité stavové premenné obrysové grafy, ako je znázornené na obr. 3DMBL1.25\. a obr. 3DMBL1.26.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0025.jpg' | relative_url }})

Efektívny stav stresu variabilný graf

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0026.jpg' | relative_url }})

Efektívny premenlivý graf stavu napätia

Používateľ môže prejsť viacerými operáciami úderov a opätovného ohrevu výberom konkrétneho kroku z prehliadača krokov a prehrávaním krokov. V poradí krokov operácií prehliadača môžeme pozorovať, že adaptívne opätovné zahriatie sa spustilo až po prevádzke BL5-DWL, pretože minimálna teplota objektu klesla pod minimálnu teplotu adaptívneho opätovného zahriatia 1750F. Aj adaptívna simulácia tepla sa zastavila, keď obrobok dosiahol teplotu zastavenia opätovného ohrevu 1950F. (Pozri obr. 3DMBL1.27.)

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0027.jpg' | relative_url }})

Prehliadač krokov indikujúci adaptívne simulácie opätovného ohrevu

Teplotný obrys obrobku pred a po adaptívnom ohreve, ako je znázornené na vyfukovacom obr. 3DMBL1.28\. Všimnite si, že pred spustením adaptívneho ohrevu je minimálna teplota predvalku 1748,845F (špecifikovaný limit je 1750F).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0028.jpg' | relative_url }})

Obrys teploty obrobku pred a po adaptívnom ohreve po BL3-DWL
