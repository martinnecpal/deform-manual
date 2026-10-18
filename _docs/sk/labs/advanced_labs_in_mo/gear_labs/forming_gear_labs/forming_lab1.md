---
lang: sk
title: "Laboratórium tvarovania 1"
---

## Laboratórium 2D Gear v oblasti tvárnenia

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem**, alebo kliknutím na ikonu New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. L1.1. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou prepínača. Názov úlohy zadajte ako „**2DGear**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak políčko „**Zobraziť dialógové okno s možnosťami**“ nezaškrtnete, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno „Nastavenie nového problému“

Otvorí sa sprievodca viacerými operáciami, v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**2DGear**“. Uistite sa, že políčko „Prvá operácia“ nie je zaškrtnuté, pretože operáciu pridáme neskôr, a použite predvolenú polohu (domovský adresár), ako je znázornené na obr. L1.2. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pridajte projekt. Na tento laboratórny cvičenie sa budeme odvolávať v budúcich laboratórnych cvičeniach, preto je dôležité použiť uvedený názov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0002.jpg' | relative_url }})

Nové okno projektu MO

### Otvoriť preprocesor

Pridajte **operáciu 2D tvarovania** ako prvú operáciu z karty **Explorer**, ako je znázornené na obr. L1.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0003.jpg' | relative_url }})

Pridanie operácie 2D tvárnenia z prehliadača operácií

Zmeňte predvolený názov operácie z „Forming“ na „**upset**“ tak, že v editore operácií vyberiete názov, ako je znázornené na obr. L1.4, a stlačíte klávesu **Enter**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0004.jpg' | relative_url }})

Zmena názvu operácie na „upset“

### Výber typu geometrie a režimov simulácie

Na stránke „Typ geometrie“ overte, či je vybraný typ geometrie **Axi-symetrický**, a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

V tomto cvičení ukážeme, ako nastaviť jednoduchú izotermickú úlohu. Na stránke „Simulation controls“ (Ovládacie prvky simulácie) **odznačte** políčko **Heat****transfer****mode** (pozri obr. L1.5.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0005.jpg' | relative_url }})

Okno riadenia simulácie

### Pridať materiál z knižnice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice), ako je znázornené na obr. L1.6. Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom **AISI-8620[1550–2200 °F (850–1200 °C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0006.jpg' | relative_url }})

Načítavanie materiálu z knižnice

Materiál sa načíta do zoznamu materiálov. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) otvoríte okno „Zoznam materiálov“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) otvoríte okno „Vlastnosti materiálu“, keďže v tomto cvičení používame predvolené vlastnosti dostupné v databáze.

### Nastaviť počet objektov

Simulovaná operácia kovania vyžaduje obrobok a hornú a dolnú matricu. Uistite sa, že v tabuľke sú prítomné 3 objekty. Ak nie, kliknite trikrát na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (vložiť objekt), aby ste pridali 3 objekty: obrobok a dve matrice. Okno s objektmi vyzerá tak, ako je znázornené na obr. L1.7. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0007.jpg' | relative_url }})

Okno „Objekty“ na pridávanie alebo odstraňovanie objektov

Než budeme pokračovať ďalej, prejdite do ponuky **Možnosti**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Nastavenia** a uistite sa, že ako preferovaná os smerujúca nahor je nastavená **os Y**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

_**Ikony na grafickom displeji**_

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) |  Zobraziť tieňované objekty |  Zobrazí všetky objekty, ktoré sú tieňované bez siete  
![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}) |  Zobraziť len sieť |  Zobrazí všetky objekty bez tieňovania, len so sieťou  
![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}) |  Zobraziť tieňované siete |  Zobrazí všetky objekty, ktoré sú tieňované sieťou  
![]({{ '/assets/icons/pre_icons/mo_feature_line_mode_icon.jpg' | relative_url }}) |  Zobraziť povrchovú náplasť |  Zobrazujú sa iba charakteristické čiary objektov  
![]({{ '/assets/icons/pre_icons/mo_refresh_icon.jpg' | relative_url }}) |  Obnoviť |  Obnoví okno DISPLAY a vymaže predchádzajúce meracie čiary  
![]({{ '/assets/icons/pre_icons/mo_fit_all_icon.jpg' | relative_url }}) |  Zobraziť prispôsobenie |  Všetky objekty sa zmestia do okna DISPLAY  
![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }}) |  Zachytiť obrázok |  Zachytí okno DISPLAY a uloží ho do súboru  
![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}) |  Zaznamenať obrázok do schránky |  Zaznamená okno DISPLAY a uloží ho do pamäťovej schránky  
  
### Definovanie všeobecných údajov o obrobku

Prijmite predvolený názov objektu „Workpiece“. Nastavte teplotu na **2250** °F a overte, či je ako typ objektu zvolený **plast**. (Pozri obr. L1.8.) Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0008.jpg' | relative_url }})

Okno objektu obrobku

### Vytvorenie geometrie obrobku z primitívu

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) vytvoríte geometriu v programe DEFORM. Priemer obrobku je 5,00”, takže šírku definujeme ako polovicu priemeru, teda 2,50”. Dĺžka je 7,48” a polomery rohov sú 0,10”. Zadajte **polomer** **2,50** palca, **výšku** **7,48** palca a R1 a R2 s hodnotou **0,1** (pozri obr. L1.9.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a potom si prezrite geometriu v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0009.jpg' | relative_url }})

Okno s 2D osovo-symetrickými geometrickými primitívami

_**Manipulácia s displejom**_

Funkcie na manipuláciu s oknom DISPLAY (napríklad Posun, Zväčšenie, Zväčšenie a Otočenie) je možné aktivovať pomocou ikon v hornej časti okna predspracovateľa. Tieto funkcie majú tiež jednoduché klávesové skratky kombinujúce klávesy a myš, ktoré vám umožňujú rýchlo ich vykonať. Akonáhle sa s týmito funkciami oboznámite, neváhajte ich použiť na úpravu zobrazenia polotovaru v okne DISPLAY.

_**Ikony na displeji**_

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) |  Posúvanie |  Objekty v okne DISPLAY je možné dynamicky posúvať nahor, nadol, doľava alebo doprava pohybom myši pri stlačenom ľavom tlačidle myši. (Klávesová skratka: Shift + ľavé tlačidlo myši)  
![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) |  Zväčšenie/zmenšenie |  Okno DISPLAY je možné dynamicky zväčšiť alebo zmenšiť tak, že podržíte ľavé tlačidlo myši a pohybujete ňou nahor alebo nadol. (Klávesová skratka: Alt + ľavé tlačidlo myši)  
![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) |  Zväčšiť |  Časť okna DISPLAY je možné zväčšiť tak, že kliknete a podržíte ľavé tlačidlo myši v jednom rohu rámčeka na zväčšenie a potiahnutím kurzora vytvoríte okno, ktoré ohraničuje oblasť zväčšenia. (Klávesová skratka: Ctrl + Alt + ľavé tlačidlo myši)  
  
_**Výber bodu**_

Súradnice bodov a vzdialenosti medzi bodmi je možné získať z aktuálneho zobrazenia.

**_Ikony na výber bodov_**

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) |  Meranie |  Vzdialenosti medzi ľubovoľnými dvoma bodmi je možné zmerať kliknutím na prvý bod a následným kliknutím na druhý bod. Meracie čiary zostanú na obrazovke, kým nekliknete na tlačidlo „Obnoviť“.  
![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) |  Vybrať |  Toto je predvolený režim zobrazenia, ktorý slúži na výber uzlov a plôch prvkov a na získanie informácií o nich. Tento režim sa používa aj pri meraní.  
  
Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete sieť obrobku.

### Vytvorenie siete pre obrobok

Nastavte **cieľový počet prvkov** na **2000** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujte sieť pre obrobok, ako je znázornené na obr. L1.10. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) priraďte materiál k obrobku.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0010.jpg' | relative_url }})

Okienko so sieťkou na obrobok

### Priradiť materiál k obrobku

Kliknite na položku **AISI-8620[1550–2200 °F (850–1200 °C)]** v okne materiálov, aby ste obrobku priradili tento materiál, ako je znázornené na obr. L1.11.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0011.jpg' | relative_url }})

Okno na priradenie materiálu objektu

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) nastavíte okrajové podmienky obrobku.

### Nastavenie okrajovej podmienky obrobku

V predvolenom nastavení sú pozdĺž stredovej osi priradené okrajové podmienky s rýchlostným obmedzením **Vx=0**, keďže ako typ geometrie je zvolená osovo symetrická geometria. Overte, či je rýchlosť nastavená na nulu a či je vybraný smer X, a to výberom riadku „**X,****Fixed**“, ktorý sa zobrazuje v strome „Boundary Conditions“ (Okrajové podmienky), a pozorovaním grafického okna (pozri obr. L1.12.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0012.jpg' | relative_url }})

Okno „Okrajové podmienky obrobku“

Ak táto čiara chýba, znamená to, že neboli pridané okrajové podmienky. V takom prípade použite nástroj na vytvorenie hrany ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) a potom kliknite na ľubovoľný uzol na stredovej čiare obrobku, aby ste vybrali všetky uzly na tejto hrane. Následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}), aby ste nastavenia uplatnili.

Kliknite na **Top****die** v strome operácií, keďže pre objekt obrobku nie sú k dispozícii žiadne nastavenia týkajúce sa pohybu, vlastností a inicializácie, ktoré by bolo možné meniť.

### Definovanie všeobecných údajov o objekte „Top die“

Nastavte teplotu hornej formy na **300** °F a uistite sa, že je vybraný typ objektu **tuhý** a že je vybraná ako primárna forma, ako je znázornené na obr. L1.13.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0013.jpg' | relative_url }})

Hlavné okno „Die General“

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte geometriu hornej matrice.

### Import a úprava geometrie hornej matrice

Načítajte geometriu lisovacej formy s plochým vrcholom zo súboru IGS. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) otvorte (načítajte) súbor „**flat top die.****igs**“ tak, že vyhľadáte cestu k súboru s geometriou. Geometria hornej matrice sa nachádza v inštalačnom priečinku programu DEFORM v adresári \Tutorials.

Vždy je dobré skontrolovať geometriu, aby ste sa uistili, že je v súlade s pravidlami. 

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), čím otvoríte dialógové okno „Skontrolovať a opraviť geometriu“. Zmeňte typ otvorenia/zatvorenia/automatického nastavenia geometrie na „otvoriť“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Malo by sa vám zobraziť hlásenie, že geometria je platná, ako je znázornené na obr. L1.14. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustíte ponuku.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0014.jpg' | relative_url }})

Okno na kontrolu a opravu geometrie hornej matrice

Nástroj na kontrolu geometrie by ste mali použiť na každú 2D geometriu, ktorú importujete do programu DEFORM, aj keď sa zdá, že je v poriadku.

Keďže ide o izotermickú simuláciu, nie je potrebné vytvárať sieť ani priraďovať materiál pre hornú matricu; kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka s pohybom hornej matrice.

### Priradiť pohyb hornej matrice

Predvoleným režimom je konštantná **rýchlosť**. Do poľa „Constant“ zadajte hodnotu **3** in/sec a overte, či je smer nastavený na **-Y**, ako je znázornené na obr. L1.15. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom die“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0015.jpg' | relative_url }})

Okno s ovládacími prvkami pre pohyb hornej matrice

### Definovanie všeobecných údajov o spodnej matrici

Nastavte teplotu spodnej formy na **300** °F a overte, či je jej typ objektu **tuhý**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) otvoríte stránku na definovanie geometrie spodnej formy.

### Vytvorenie geometrie spodnej matrice v editore geometrie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_xyr_button.jpg' | relative_url }}), aby ste v editore geometrie definovali geometriu spodnej formy. Uistite sa, že v tabuľke geometrie je vybraný formát XYR. Na definovanie geometrie zadajte body geometrie do tabuľky tak, ako je znázornené na obr. L1.16.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0016.jpg' | relative_url }})

Tabuľka geometrie spodnej matrice s geometriou

Tieto body vymedzia geometriu proti smeru hodinových ručičiek. Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_show_inside.jpg' | relative_url }}) (Zobraziť vnútornú stranu), aby ste sa uistili, že orientácia geometrie je na vnútornej strane geometrie, ako je znázornené na obr. L1.16. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) uzavrite definíciu geometrie a kliknutím na položku **Polohovanie** v strome operácií otvoríte okno na polohovanie objektov.

### Pozícia

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) umiestnite nástroje tak, aby prichádzali do styku s obrobkom (vo vertikálnom smere tvarovania). Uistite sa, že obrobok je umiestnený na spodnej matrici a že horná matrica prilieha k obrobku, ako je znázornené na obr. L1.17.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0017.jpg' | relative_url }})

Správne umiestnenie objektov

Kliknutím na položku **Kontakt** v strome operácií otvoríte okno „Medzi objektmi“, keďže pre túto operáciu nie je potrebné naplánované polohovanie.

### Stránka „Kontakt“ (vzťahy medzi objektmi)

Program DEFORM automaticky vytvorí predvolené vzťahy typu „master-slave“; pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) vytvorí tri vzťahy, ako je znázornené na obr. L1.18. Program DEFORM vytvorí tri vzťahy. V dvoch z nich je každý nástroj hlavným prvkom a obrobok je podriadeným prvkom. Tretí vzťah bude vzťahom typu (obrobok – obrobok). Tento vzťah umožní vzájomný kontakt obrobkov v prípade, že sa vytvorí záhyb.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) pre jeden z vzťahov. V poli **Hodnota trenia ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})****** použite roletové menu „Konštanta“ a vyberte možnosť **Kovanie za tepla** (mazané) **0,3**. Ak máte skúsenosti, ktoré naznačujú, že iná hodnota trenia by v prípade vášho procesu priniesla lepšie výsledky, môžete túto hodnotu zadať priamo do tohto poľa. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustíte ponuku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) použijete túto hodnotu trenia na ďalšie dva vzťahy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0018.jpg' | relative_url }})

Okno „Kontakt“ a zobrazenie objektov s kontaktmi medzi objektmi

Ďalej je potrebné vytvoriť kontakt medzi objektmi. Kliknite na tlačidlo „Predvolená tolerancia kontaktu“ (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})), aby ste vypočítali toleranciu pre vytvorenie kontaktu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vytvoríte kontakt. Na obrobku by ste mali vidieť kontaktné uzly v miestach, kde bol kontakt vytvorený.

Tento počiatočný kontakt predstavuje počiatočné podmienky pre riešiteľ konečných prvkov. Po spustení simulácie sa kontakt automaticky aktualizuje.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) nastavíte primárne ovládacie prvky na zastavenie zdvihu matrice.

### Priradiť ovládacie prvky zastavenia

Musíme pridať kritérium ukončenia, ktoré zastaví simuláciu, keď sa nástroj posunie o 6 palcov. Zaškrtnite políčko **Max****die****stroke** a zadajte hodnotu **6** (smer Y), ako je znázornené na obr. L1.19.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0019.jpg' | relative_url }})

Okno s ovládacími prvkami na zastavenie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali v priraďovaní ovládacích prvkov krokov.

### Priradiť ovládacie prvky krokov

Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do expertného režimu) (na paneli nástrojov v hlavičke), aby ste získali prístup k nastaveniam pokročilých ovládacích prvkov simulácie, pretože pre túto simuláciu je potrebné definovať kritériá pre vytvorenie novej siete.

Všimnite si, že názov simulácie sa zmenil na „upset“, tak ako ste ho premenovali v editore operácií na karte „Main“. Prejdite na kartu **Simulation****Steps**.

DEFORM používa dvojfázový proces na stanovenie celkovej vzdialenosti pohybu razníka:

Na karte **Simulácia****Kroky** sa nastavuje počet krokov a interval ukladania. Na karte „Prírastok kroku“ sa nastavuje čas alebo pohyb nástroja na jeden časový krok. Ak nie sú definované žiadne ďalšie obmedzenia, celková dĺžka simulácie bude približne rovná súčinu prírastku kroku a počtu krokov.

Na vykonanie tejto operácie sa musí nástroj posunúť o 6,0’’, aby sa dosiahol požadovaný tvar. Na takéto jednoduché vyťahovanie by malo stačiť 100 krokov. Zmeňte **Počet krokov simulácie** na **100**. Zmeňte **Krok****Prírastok****na****Uložiť** na hodnotu **5**, ako je znázornené na obr. L1.20.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0020.jpg' | relative_url }})

Pokročilé nastavenia – karta „Kroky simulácie“

Ďalej prejdite na **Krok****Prírastok**. Hodnota posunu matrice predstavuje celkovú vzdialenosť, ktorú má nástroj prekonať (6,0’’), vydelenú počtom krokov (100). Pomocou možnosti *With Die Displacement* nastavte **posun matrice** na hodnotu **0,06** ’’ (6,0 / 100), ako je znázornené na obr. L1.21.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0021.jpg' | relative_url }})

Karta „Krok“ v nastaveniach „Pokročilé kroky“

Prejdite na kartu **Remesh****Kritériá**. Hodnota hĺbky interferencie by mala byť polovicou dĺžky hrany malého prvku. Zmerajte dĺžku jedného z menších prvkov, vydelte ju 2 a túto hodnotu zadajte do poľa hĺbky interferencie (pozri obr. L1.22.). Mali by ste dostať hodnotu okolo 0,02''. Prepočítanie sietí sa spustí, ak niektorý z nástrojov dokáže preniknúť do obrobku o vzdialenosť **0,02**''.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0022.jpg' | relative_url }})

Karta „Kritériá pre výpočet novej siete“ v okne „Advanced Step“

Teraz kliknite na položku **Pohyb** pod položkou „Horná matrica“ v strome operácií, aby ste si prezreli náhľad pohybu hornej matrice, pretože pred zobrazením náhľadu pohybu je potrebné definovať krok a pohyb.

### Potvrdiť pohyb

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) (Náhľad pohybu objektu) v pravom dolnom rohu obrazovky (pozri obr. L1.15.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_movement_play_button.jpg' | relative_url }}) (prehrávanie) (pozri obr. L1.23.) a sledujte, ako sa horná matica pohybuje cez obrobok. Tento nástroj potvrdí, že sa váš nástroj pohybuje správnym smerom a že máte dostatok krokov na dokončenie zdvihu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0023.jpg' | relative_url }})

Okno s náhľadom pohybu hornej matrice

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili menu, a v strome operácií kliknite na **Generate****DB**, čím prejdete k generovaniu databázy.

### Kontrola údajov a vytvorenie databázy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Program DEFORM skontroluje všetky vstupné údaje a overí, či sú definované všetky potrebné údaje. V okne Správy by sa mala zobraziť nasledujúca správa.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0001.jpg' | relative_url }})

Červené označenia signalizujú chýbajúce alebo nesprávne údaje, ktoré zabránia spusteniu simulácie. Pred vytvorením databázy je potrebné chybu opraviť.

Žlté značky označujú údaje, ktoré môžu byť podozrivé a mali by sa skontrolovať. Tieto údaje je potrebné dôkladne preveriť, pretože by mohli spôsobiť nestabilitu systému alebo chybné (nesprávne) výsledky.

Preverte si informácie o kontrole údajov. Ak sa nevyskytujú žiadne chyby, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

V okne Správy by ste mali hľadať nasledujúcu správu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0002.jpg' | relative_url }})

Ak sa vám zobrazí táto správa, znamená to, že nastavenia simulácie boli uložené do databázy a simulácia je pripravená na spustenie.

Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustenie a sledovanie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0024.jpg' | relative_url }})

Spustenie simulácie z režimu simulácie MO

V pravom hornom rohu sa aktualizuje pole „Status“, ktoré vás informuje o tom, že simulácia práve prebieha na konkrétnom počítači. (Pozri obr. L1.24.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0003.jpg' | relative_url }})

Karty „Simulačná správa“ a „Simulačný protokol“ v pravom dolnom rohu vám poskytujú informácie o priebehu simulácie.

Priebeh simulácie je možné sledovať v grafickom okne počas jej vykonávania. V predvolenom nastavení sa grafika aktualizuje vždy, keď sa do databázy uloží nový krok. 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0004.jpg' | relative_url }})

Ak chcete, aby sa grafika aktualizovala častejšie, môžete v roletovom menu „Update“ (v pravom dolnom rohu grafického okna) zmeniť nastavenie na „Current Step“. Pri 2D simuláciách to zvyčajne nie je potrebné, keďže prebiehajú veľmi rýchlo.

Osvedčeným postupom je sledovať prvých niekoľko krokov simulácie v grafickom režime simulácie, aby sa overilo, či sa pohyby nástroja a deformácia obrobku vyvíjajú podľa očakávaní.

Po dokončení simulácie sa obraz v grafickom okne prestane meniť a zobrazí sa konečný deformovaný tvar dielu. Posledné riadky na karte „Simulačné správy“ budú signalizovať, že simulácia bola dokončená.

"PROGRAM SA ZASTAVIL!

HODNOTA STROKE -6,0000000 PREKROČILA ŠPECIFIKOVANÝ LIMIT 6,0000000 "

### Výsledky kontroly v režime príspevku

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Zoznam krokov a ovládacie prvky prehrávania

V grafickom okne sa zobrazujú výsledky simulácie. Uložené kroky sú uvedené v prehliadači krokov v spodnej časti grafického okna.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0025.jpg' | relative_url }})

Krokový prehliadač pre prevádzku v núdzovom režime

Ovládacie prvky hry slúžia na:

![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) **Prehrávanie dopredu**: Zobrazuje kroky jeden po druhom, až kým sa od aktuálne vybraného kroku nezobrazí posledný krok.

![]({{ '/assets/icons/pre_icons/mo_preview_stop_button.jpg' | relative_url }}) **Stop** : Zastaví prehrávanie (dopredu alebo dozadu) krokov.

**![]({{ '/assets/icons/pre_icons/mo_preview_one step_forward_button.jpg' | relative_url }})Jeden krok vpred** : Prejsť na ďalší uložený krok v zozname krokov.

![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }}) **Preskočiť na koniec** : Preskočí na posledný uložený krok v zozname krokov.

![]({{ '/assets/icons/pre_icons/mo_preview_play_back_button.jpg' | relative_url }}) **Prehrávať spätne**: Zobrazuje kroky jeden po druhom v opačnom poradí, až kým sa od aktuálneho vybraného kroku nezobrazí prvý krok.

![]({{ '/assets/icons/pre_icons/mo_preview_one_step_back_button.jpg' | relative_url }}) **Jeden krok späť**: Posuňte zoznam krokov späť o jeden uložený krok.

**![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }})Preskočiť na začiatok** : Vráťte zoznam krokov späť na prvý uložený krok.

**Graf závislosti zaťaženia od zdvihu**

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) v nástrojoch stĺpca. Vykreslite graf **Y****zaťaženie** (os Y) v závislosti od **zdvihu** (os X) pre hornú matricu výberom tlačidla ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) (pozri obr. L1.26.). Graf zobrazuje zaťaženie počas celej simulácie. Zvislý indikátor kroku označuje aktuálny krok.

Kliknutím na ľubovoľný bod na grafe zaťaženia a zdvihu (alebo na akýkoľvek graf v programe DEFORM) sa zobrazia výsledky v danom kroku. Prípadne je možné vybrať ľubovoľný krok v zozname krokov a vertikálny ukazovateľ krokov preskočí na tento bod v simulácii. Graf je možné odstrániť kliknutím pravým tlačidlom myši na graf a výberom možnosti **Odstrániť**.

Poznámka: Grafy sa štandardne otvárajú v tom istom grafickom okne ako simulácia. Ak chcete dosiahnuť podobný vzhľad ako na obrázku nižšie, prejdite do **Možnosti** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Nastavenia** a v časti Zobrazenie grafu zaškrtnite políčko vedľa položky Nové okno a potom stlačte ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}). Znovu vykreslite graf, aby ste videli zmeny.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0026.jpg' | relative_url }})

Graf zdvihu hornej matrice

**Grafy stavových premenných**

  * **Graf rýchlosti**

Vyberte krok **75** (alebo akýkoľvek iný medzistupeň na lište výberu krokov). Kliknite na ikonu stavovej premennej ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}) (Celková rýchlosť) v nástrojoch Post – Stavové premenné. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) otvoríte dialógové okno s vlastnosťami stavovej premennej. Vyberte typ zobrazenia ![]({{ '/assets/icons/post_icons/mo_vector_plot_button.jpg' | relative_url }}). Okamžité rýchlosti sa zobrazujú ako vektory v zvolenom časovom kroku. Farby šípok označujú veľkosť rýchlosti. (Pozri obr. L1.27.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0027.jpg' | relative_url }})

Graf rýchlostného vektora s grafom zdvihu zaťaženia pre hornú maticu

  * **Graf efektívneho napätia**

V dialógovom okne „Stavová premenná“ vyberte **Deformácia**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Efektívna**. Nastavte **Mierku** na **Globálnu** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Efektívna deformácia predstavuje veľkosť deformácie počas simulovaného procesu. Pri tvárnení za studena súvisí s pracovným spevnením.

Prejdite si simuláciu a sledujte, ako sa napätie mení v priebehu tvarovania dielu. Pri globálnom škálovaní farebný pruh znázorňuje maximálny rozsah premennej kdekoľvek v obrobku.

Nastavte mierku na **Lokálnu** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Spustite simuláciu. V každom kroku sa stavové premenné prispôsobia na maximálnu hodnotu v danom kroku.

Vyberte zobrazenie ![]({{ '/assets/icons/post_icons/mo_solid_plot_button.jpg' | relative_url }}) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Okraje kontúr sa zmenia na ostré hrany (pozri obr. L1.28.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0028.jpg' | relative_url }})

Kontúra efektívnej premennej deformácie v miestnom aj globálnom meradle

Keď dokončíte prezeranie výsledkov, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili okno „State variable“. Mierku a typ grafu je možné zmeniť aj pomocou možností, ktoré sa zobrazia po kliknutí pravým tlačidlom myši na lištu s vrstevnicami.

Kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) MO, aby ste prešli do režimu Pre a mohli pokračovať v ďalšom laboratórnom cvičení.

### Pridať druhú operáciu

K plochému dielu pridáme záverečnú operáciu kovania. Na karte **Explorer** v ľavej časti používateľského rozhrania prejdite na položku **Forming![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Single** a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky **[2D] Forming**. (Pozri obr. L1.29.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0029.jpg' | relative_url }})

Okno prehliadača

V editore operácií bude pridaná nová dlaždica operácie. (Pozri obr. L1.30.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0030.jpg' | relative_url }})

Zoznam operácií v okne Editor operácií

Kliknite na dlaždicu **Forming**. Zobrazí sa vyskakovacie okno s výzvou na výber nastavenia **Interactive** alebo **Batch**. Interaktívne nastavenie umožňuje priamejšie ovládanie vstupných údajov. Dávkové nastavenie však zaručuje, že bude možné zálohovať a znovu spustiť celý projekt od začiatku bez prerušenia. _Pre takmer všetky projekty_ _poskytuje dávkové nastavenie väčšiu flexibilitu_. 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0031.jpg' | relative_url }})

Vyskakovacie okno s typom nastavenia pre operáciu 2D tvárnenia

V tomto dialógovom okne kliknite na ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}). V stromovej štruktúre procesov sa otvorí druhá operácia. Všimnite si, ako sú objekty z prvej operácie teraz prepojené s druhou operáciou a sú zobrazené ako „Prečítané z databázy“. Všetky objekty sa v druhej operácii zobrazujú červenou farbou, čo znamená, že sa načítajú z predchádzajúcej operácie v databáze.

Pre túto operáciu sa budú importovať nové formy, takže formy sa naozaj nebudú načítať z databázy tak ako obrobok. Toto sa dá ľahko zmeniť. Pri importe nižšie uvedených foriem nezabudnite, že geometrie sa nachádzajú v inštalačnej zložke DEFORM v adresári \Tutorials.

#### Priradiť ovládacie prvky simulácie

V časti „Simulačné ovládacie prvky“ **zrušte zaškrtnutie** políčka **Heat****Transfer**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die“.

#### Definovanie všeobecných údajov o objekte hornej matrice

Vyberte objekt typu **Rigid**, nastavte teplotu hornej formy na **300°** F a označte ju ako primárnu formu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou hornej formy.

#### Definovanie geometrie hornej matrice

Načítajte geometriu „**gear top die.****IGS**“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a otvorte (načítajte) súbor „gear top die.IGS“. Geometria polotovaru sa nachádza v inštalačnom priečinku DEFORM v adresári \Tutorials. Pomocou ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) skontrolujte geometriu a upravte tieňovanie tak, aby bolo správne na vnútornej strane dielu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Top die Movement.

#### Priradiť pohyb hornej matrice

Uistite sa, že rýchlosť je nastavená na **3** palce za sekundu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Vlastnosti.

#### Definovanie vlastností hornej matrice

V ďalšej časti tohto nastavenia definujeme kritérium zastavenia na základe vzdialenosti medzi formami v mieste odlievacej medzery. Na to musíme v časti „Vlastnosti“ definovať referenčné body. Prejdite do časti Reference a pomocou myši vyberte výstupok v hornej matrici, ktorý zodpovedá oblasti prebytočného materiálu, ako je znázornené na obr. L1.32. (Aby to fungovalo, kurzor musí byť v režime Select ![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }})).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0032.jpg' | relative_url }})

Referenčný bod na hornej matrici

#### Definovanie všeobecných údajov o spodnej forme

Vyberte objekt typu **Pevný** a nastavte teplotu spodnej formy na **300** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou spodnej formy.

#### Definovanie geometrie spodnej matrice

Načítajte geometriu „**gear bottom die.****IGS**“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a pomocou ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) (importovať) načítajte súbor „gear bottom die.IGS“. Geometria polotovaru sa nachádza v inštalačnom priečinku programu DEFORM v adresári \Tutorials. Pomocou ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) skontrolujte geometriu a upravte tieňovanie tak, aby bolo správne na vnútornej strane dielu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Vlastnosti spodnej matrice.

####  Definovanie vlastností spodnej matrice

Prejdite do položky **Referencia** a pomocou myši vyberte bod na spodnej ploche odliatku, ako je znázornené na obr. L1.33. (Aby to fungovalo, kurzor musí byť v režime „Select ![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }})“). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Scheduled positioning“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0033.jpg' | relative_url }})

Výber referenčného bodu na spodnej matrici

#### Plánované umiestnenie

Keďže sa obrobok načítava z databázy po predchádzajúcej operácii tvarovania, jeho rozmery a tvar sa môžu zmeniť, ak sa projekt spustí od začiatku. Z tohto dôvodu je lepšie umožniť flexibilné polohovanie nástrojov vo vzťahu k obrobku, ako im nastavovať pevnú polohu.

V programe DEFORM je k dispozícii možnosť s názvom **Plánované polohovanie**, ktorá umožňuje presunúť nástroje do kontaktu s ľubovoľným tvarom obrobku vždy, keď sa obrobok načíta z predchádzajúcej operácie.

V strome procesov prejdite na položku **Plánované****polohovanie** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte operáciu polohovania. 

Najskôr nastavíme pohyb spodnej matrice smerom nahor k obrobku. Vyberte možnosť **Interference** a ako **positioning****object** vyberte **Bottom****Die** a ako **Reference****object** vyberte **Workpiece**. Ako smer priblíženia vyberte **Y** (nahor). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). 

Upozorňujeme, že nástroj sa v tejto chvíli nepohybuje, ale polohovanie sa vykoná pri generovaní databázy pre túto operáciu.

Kliknite opäť na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), aby ste naplánovali druhé polohovanie. Vyberte **Interferencia** a nastavte polohu **Horná forma** smerom nadol (**-Y**) voči **obrobku**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (Pozri obr. L1.34.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali kontaktný vzťah.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0034.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

#### Údaje o kontaktoch (vzťahy medzi objektmi)

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) nastavte predvolené vzťahy medzi objektmi. Obrobok by mal byť podriadený tak hornej, ako aj spodnej matrici. Pri 3D simuláciách sa vlastný kontakt (obrobok ako hlavný objekt vo vzťahu k sebe samému) zvyčajne nepoužíva, pretože môže výrazne predĺžiť dobu simulácie. Na sledovanie ohýbania sú k dispozícii aj iné nástroje. Tým sa budeme venovať v neskoršom laboratórnom cvičení.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) pre jeden z vzťahov. V poli **Hodnota trenia ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})****, použite roletové menu „Konštanta“ a vyberte **Kovanie za tepla (s mazaním)****0,3**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustite ponuku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) použite hodnotu trenia na ďalšie dva vzťahy. Keďže obrobok pridaný vo vzťahu sa načíta z databázy objektov, medzi objektmi sa teraz nemôžu generovať vzťahy ako v laboratóriu 1, preto sa uistite, že sú zaškrtnuté políčka **Initialize** a **Generate****contact****check****. Tým sa počas behu simulácie inicializujú predchádzajúce kontakty a vygenerujú nové kontakty. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku Ovládacie prvky zastavenia.

#### Priradenie ovládacích prvkov na zastavenie v režime Expert

Na rozdiel od merania vzdialenosti pohybu nástroja, ako sme to robili v prvej operácii, tento proces zastavíme pri pevne stanovenej vzdialenosti medzi nástrojmi. V tomto prípade nastavíme hrúbku prebytku na 0,2 in.

Vzdialenosť blesku sa meria v referenčných bodoch určených na hornej a dolnej matrici.

Kliknite na položku „Stopping controls“ (Ovládacie prvky zastavenia) v strome operácií. Najskôr skontrolujte, či je ovládací prvok zastavenia **Primary****die****displacement** nastavený späť na hodnotu **0**. Následne vyberte **kartu „Vzdialenosť matrice“** a nastavte objekt „Referencia 1“ na **„Horná matrica“** a objekt „Referencia 2“ na **„Spodná matrica“**. Nastavte metódu na **Y- Distance** a vzdialenosť na **0,2** in (pozri obr. L1.35.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Step controls“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0035.jpg' | relative_url }})

Režim pre pokročilých – Ovládacie prvky zastavenia – Okno vzdialenosti medzi maticami

#### Priradiť ovládacie prvky krokov

Chceme prejsť približne 1,5 in. za 100 krokov, takže použijeme **krok****inkrement** **0,015** in/krok. NECHCE sa nám však, aby simulácii došli kroky, keďže je nastavené ďalšie kritérium zastavenia (vzdialenosť medzi maticami). Keďže chceme mať pri opätovnom spustení tohto prípadu flexibilitu, nastavíme **počet****simulačných****krokov** na **1000**, nie na 100. Tým sa zabezpečí, že ak projekt spustíme znovu s inými nastaveniami, nebudeme sa musieť obávať, že dôjdu kroky. Ukončenie simulácie bude vždy riadiť vzdialenosť medzi nástrojmi.

Zmeňte **počet krokov** na **1000** a nastavte **krok** na **5**.

Prejdite na položku **Krok****prírastok** a vyberte možnosť **Matrica****posun** na krok. Nastavte ovládací prvok Prírastok kroku na hodnotu **0,015** palca na krok. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte stránku databázy.

#### Vytvoriť databázu

Systém sa na chvíľu pozastaví, kým vykoná naplánované polohovanie a vytvorenie kontaktu. Farba obrobku sa zmení z červenej (načítané z databázy) na žltú (plastový predmet).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Kliknutím na tlačidlo „MO![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

#### Spustiť a sledovať simuláciu

Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) a potom zrušte začiarknutie políčka „Odoslať úlohu do fronty simulácie“. Zrušením začiarknutia tejto možnosti sa úloha spustí na lokálnom počítači. Použite predvolenú možnosť **Začať od posledného záporného kroku**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) spustíte simuláciu.

#### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

Prejdite všetky kroky. Všimnite si, že diel úplne nevyplňuje dutinu formy (pozri obr. L1.36.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0036.jpg' | relative_url }})

Tvar obrobku v poslednom kroku druhej operácie

Ak chceme spustiť výpočet s väčšou veľkosťou polotovaru, vytvoríme nový projekt na základe existujúceho projektu. Pozrite si prosím [Lab 2. Rerun Sequence with a Larger Bille]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/forming_lab2/' | relative_url }})t
