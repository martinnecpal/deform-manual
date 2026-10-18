---
lang: sk
title: "Polotovar na ozubené kolesá EN Laboratórium 1"
---

# Laboratórna práca 1.2D – operácia deformácie

### Vytvoriť nový problém

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obrázku [Fig. L1.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_1_New_Problem_setup_window). Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou prepínača. Názov úlohy zadajte ako „**Gear**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém pomocou integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na zadanie nového problému

Otvorí sa sprievodca viacerými operáciami. V tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „******Gear** ** **“ a uistíme sa, že políčko „Prvá operácia“ nie je zaškrtnuté, keďže operáciu pridáme neskôr, a použijeme predvolený (domovský) adresár, ako je znázornené v [Fig. L1.2.](#Fig_L1_2_MO%20New%20Project%20window). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pokračujte v otváraní nového projektu. Na túto laboratórnu úlohu sa budeme odvolávať v budúcich laboratórnych úlohách, preto je dôležité použiť vyššie uvedený názov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0002.jpg' | relative_url }})

Okno „Nový projekt“ v programe MO

### Otvoriť preprocesor

Pridajte **operáciu 2D tvárnenia** ako prvú operáciu z karty Explorer, ako je znázornené na obrázku [Fig. L1.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_3_Adding_2D_Forming_operation_from_operation_explorer)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0003.jpg' | relative_url }})

Pridanie 2D tvárnej operácie z prehliadača operácií

Zmeňte predvolený názov operácie z „Forming“ na „**upset**“ tak, že v editore operácií vyberiete názov, ako je znázornené na obrázku [Fig. L1.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_4_Renaming_operation_title_to_upset), a stlačíte klávesu **Enter**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0004.jpg' | relative_url }})

Zmena názvu operácie na „upset“

### Výber typu geometrie a režimov simulácie

Na stránke „Typ geometrie“ overte, či je zvolený typ geometrie **Axi-symetrický**, a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

V tomto laboratórnom cvičení ukážeme, ako nastaviť jednoduchú izotermickú úlohu. Na stránke „Simulation controls“ (Ovládacie prvky simulácie) **zrušte zaškrtnutie** políčka **Heat transfer mode** (Režim prenosu tepla) (pozri [Fig. L1.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_5_Simulation_control_window)). Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0005.jpg' | relative_url }})

Okno riadenia simulácie

### Pridať materiál z knižnice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice), ako je znázornené na obrázku [Fig. L1.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_6_Loading_material_from_library). Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom A**ISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0006.jpg' | relative_url }})

Načítavanie materiálu z knižnice

Materiál sa načíta do zoznamu materiálov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa otvorilo okno „Zoznam materiálov“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa otvorilo okno „Vlastnosti materiálu“, keďže v tomto cvičení používame predvolené vlastnosti z databázy.

### Nastaviť počet objektov

Simulovaná operácia kovania vyžaduje obrobok a hornú a dolnú matricu. Ak ešte nemáte tri objekty, pridajte ich kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (vložiť objekt): obrobok a dve matrice. Okno s objektmi vyzerá tak, ako je znázornené na obrázku [Fig. L1.7.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_7_Objects_window_to_Add_or_Delete_the_objects). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0007.jpg' | relative_url }})

Okno „Objekty“ na pridávanie alebo odstraňovanie objektov

Než budeme pokračovať ďalej, prejdite do položky ponuky **Možnosti**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Nastavenia** a uistite sa, že ako preferovaná os smerujúca nahor je nastavená **os Y**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

**Ikony na grafickom displeji**

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) |  Zobraziť tieňované objekty |  Zobrazí všetky objekty, ktoré sú tieňované bez siete  
![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}) |  Zobraziť len sieť |  Zobrazí všetky objekty bez tieňovania s sieťou  
![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}) |  Zobraziť tieňované sieťové modely |  Zobrazí všetky objekty tieňované pomocou sieťového modelu  
![]({{ '/assets/icons/pre_icons/mo_feature_line_mode_icon.jpg' | relative_url }}) |  Zobraziť povrchovú náplasť |  Zobrazujú sa iba charakteristické čiary objektov  
![]({{ '/assets/icons/pre_icons/mo_refresh_icon.jpg' | relative_url }}) |  Obnoviť |  Obnoví okno DISPLAY a vymaže predchádzajúce meracie čiary  
![]({{ '/assets/icons/pre_icons/mo_fit_all_icon.jpg' | relative_url }}) |  Zobraziť prispôsobenie |  Všetky objekty sa zmestia do okna DISPLAY  
![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }}) |  Zachytiť obrázok |  Zachytí okno DISPLAY a uloží ho do súboru  
![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}) |  Zaznamenať obrázok do schránky |  Zaznamená okno DISPLAY a uloží ho do pamäťovej schránky  
  
### Definovanie všeobecných údajov o obrobku

Prijmite predvolený názov objektu „Workpiece“. Nastavte teplotu na **2250** °F a potvrďte, že vybraný typ objektu je **plast**. (Pozri [Fig. L1.8.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_8_Workpiece_object_window)). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0008.jpg' | relative_url }})

Okno objektu obrobku

Poznámka:

Tlačidlo „Importovať objekt“ na karte „Všeobecné“ slúži na import údajov z iného kľúčového slova úlohy DEFORM alebo z inej databázy. Vo väčšine prípadov budete používať možnosť „Importovať geometriu“ na nasledujúcej karte.

### Vytvorenie geometrie obrobku z primitívu

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), aby ste v programe DEFORM vytvorili geometriu. Vyberte typ **valec**. Priemer obrobku je 5,00", takže nastavíte polomer **2,50**", **výšku** **8,15**” a **polomery rohov** **0,10**”. Zadajte **polomer** 2,50, **výšku** 8,15 a R1 a R2 0,10 (pozri [Fig. L1.9.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_9_2D_axi-symmetric_geometry_primitive_window)). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a potom si prezrite geometriu v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0009.jpg' | relative_url }})

Okno s 2D osovo-symetrickými geometrickými prvkami

**Manipulácia s displejom**

Funkcie na manipuláciu s oknom DISPLAY (napríklad Posun, Zväčšenie, Zväčšenie a Otočenie) je možné aktivovať pomocou ikon v hornej časti okna predprocesora. Tieto funkcie majú tiež jednoduché klávesové skratky kombinujúce klávesy a myš, ktoré vám umožňujú rýchlo ich vykonať. Akonáhle si prečítate informácie o týchto funkciách, neváhajte ich použiť na úpravu zobrazenia polotovaru v okne DISPLAY.

**Ikony na displeji**

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) |  Posúvanie |  Objekty v okne DISPLAY je možné dynamicky posúvať nahor, nadol, doľava alebo doprava pohybom myši pri stlačenom ľavom tlačidle myši. (Klávesová skratka: Shift + ľavé tlačidlo myši)  
![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) |  Zväčšenie/zmenšenie |  Okno DISPLAY je možné dynamicky zväčšiť alebo zmenšiť tak, že podržíte ľavé tlačidlo myši a pohybujete ňou nahor alebo nadol. (Klávesová skratka: Alt + ľavé tlačidlo myši)  
![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) |  Zväčšiť |  Časť okna DISPLAY je možné zväčšiť tak, že kliknete a podržíte ľavé tlačidlo myši v jednom rohu rámčeka na zväčšenie a pretiahnutím kurzora vytvoríte okno, ktoré ohraničuje oblasť zväčšenia. (Klávesová skratka: Ctrl + Alt + ľavé tlačidlo myši)  
  
**Výber bodu**

Súradnice bodov a vzdialenosti medzi bodmi je možné získať z aktuálneho zobrazenia.

**Ikony na výber bodov**

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) |  Meranie |  Vzdialenosti medzi ľubovoľnými dvoma bodmi je možné zmerať kliknutím na prvý bod a následným kliknutím na druhý bod. Meracie čiaročka zostane na obrazovke, kým nekliknete na tlačidlo „Obnoviť“.  
![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) |  Vybrať |  Toto je predvolený režim zobrazenia, ktorý slúži na výber uzlov a plôch prvkov a na získavanie informácií o nich. Tento režim sa používa aj pri meraní.  
  
Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vytvorili sieť obrobku.

### Vytvoriť sieť pre obrobok

Predvolený cieľový **počet prvkov** je **1000**. Potvrďte predvolený počet prvkov a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujte sieť pre obrobok, ako je znázornené na obrázku [Fig. L1.10.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_10_Mesh_generation_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0010.jpg' | relative_url }})

Okno na generovanie siete

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste obrobku priradili materiál.

### Priradiť materiál k obrobku

Kliknite na položku **AISI-8620[1550–2200 °F (850–1200 °C)]** v okne materiálov, aby ste obrobku priradili tento materiál, ako je znázornené na obrázku [Fig. L1.11.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_11_Object_Material_Assigning_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0011.jpg' | relative_url }})

Okno na priradenie materiálu objektu

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili okrajové podmienky obrobku.

### Nastavenie okrajovej podmienky obrobku

V predvolenom nastavení sú pozdĺž stredovej osi priradené okrajové podmienky s rýchlostným obmedzením Vx=0, keďže typ geometrie je nastavený na „Axi-symmetric“. Overte, či je rýchlosť nastavená na nulu a či je vybraný smer X, a to výberom riadku „X, Fixed“, ktorý sa zobrazí v stromovej štruktúre „Boundary Conditions“, a pozorovaním grafického okna (pozri [Fig. L1.12.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_12_Workpiece_Boundary_Conditions_window)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0012.jpg' | relative_url }})

Okno „Okrajové podmienky obrobku“

Ak táto čiara chýba, znamená to, že neboli pridané okrajové podmienky. V takom prípade použite nástroj na vytvorenie hrany ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) a potom kliknite na ľubovoľný uzol na stredovej čiare obrobku, aby ste vybrali všetky uzly na danej hrane, a následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) na uplatnenie nastavení.

Kliknite na položku **Horná matrica** v strome operácií, keďže pre objekt obrobku nie je možné meniť nastavenia „Pohyb“, „Vlastnosti“ a „Inicializácia“.

### Definovanie všeobecných údajov o objekte „Top die“

Nastavte predvolenú teplotu hornej formy na 68 °F a skontrolujte, či je ako typ objektu zvolená možnosť **tuhý** a či je táto forma zvolená ako primárna, ako je znázornené na obrázku [Fig. L1.13.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_13_Top_die_object_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0013.jpg' | relative_url }})

Okno s objektom „Top die“

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali geometriu hornej matrice.

### Import a úprava geometrie hornej matrice

Načítajte geometriu hornej matrice zo súboru IGS. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a otvorte (načítajte) súbor „**Flat_dies_ENG****.****igs**“. Túto geometriu je možné importovať aj pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) vyhľadaním cesty k súboru s geometriou. Geometria hornej matrice sa nachádza v inštalačnej zložke programu DEFORM v adresári \2D\Labs.

Keďže tento súbor obsahuje viac ako jednu geometriu, budete musieť v kontextovom menu vybrať možnosť ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), aby sa automaticky otvorila príslušná geometria na úpravy. (Pozri [Fig. L1.14.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_14_Top_die_Geometry_window))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0014.jpg' | relative_url }})

Okno „Geometria hornej matrice“

Otvorí sa editor geometrie. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_xyr_button.jpg' | relative_url }}) nad tabuľkou geometrie aktivujete všetky možnosti na paneli nástrojov na úpravu geometrie. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_area select.jpg' | relative_url }}) (Výber oblasti) nakreslite obdĺžnik okolo spodnej geometrie, aby ste ju vybrali, a stlačte kláves Delete, čím zachováte iba hornú geometriu (pozri [Fig. L1.15.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_15_Boundary_selection_from_Geometry_editor_for_top_die)). Vybranú geometriu môžete odstrániť aj tak, že pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_delete_selected.jpg' | relative_url }}) (Výber na odstránenie) vyberiete hranicu, ktorú chcete odstrániť.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0015.jpg' | relative_url }})

Výber hraníc v editore geometrie pre hornú formu

Je potrebné vizuálne skontrolovať orientáciu geometrie na diele. Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_show_inside.jpg' | relative_url }}) (Zobraziť vnútornú stranu) v hornom paneli nástrojov geometrie, aby sa zobrazila orientácia geometrie, ako je znázornené na obrázku [Fig. L1.16.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_16_Reversing_the_direction_of_the_geometry_orientation). Vyberte tiež ikonu ![]({{ '/assets/icons/pre_icons/mo_show_vertex_numbers_icon.jpg' | relative_url }}) (Zobraziť čísla vrcholov), aby ste mohli sledovať smer vytvárania hranice geometrie pomocou poradia číslovania vrcholov geometrie; pri vytváraní v smere hodinových ručičiek bude orientácia geometrie smerovať dovnútra. Tienenie / šípky orientácie geometrie by mali smerovať dovnútra dielu. Ak smerujú von, použite ikonu ![]({{ '/assets/icons/pre_icons/mo_reverse_direction.jpg' | relative_url }}) (Obrátiť smer) a kliknite na hranicu geometrie, ktorú chcete obrátiť, ako je znázornené na obrázku [Fig. L1.16.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_16_Reversing_the_direction_of_the_geometry_orientation). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) uzavrite úpravy geometrie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0016.jpg' | relative_url }})

Zmena smeru orientácie geometrie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), čím otvoríte ponuku „Skontrolovať a opraviť geometriu“. Zmeňte typ geometrie **otvoriť/zatvoriť/automaticky** na „otvoriť“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Malo by sa vám zobraziť hlásenie, že geometria je platná, ako je znázornené na obrázku [Fig. L1.17.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_17_Check_and_correct_geometry_window_for_top_die_geometry). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustíte ponuku.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0017.jpg' | relative_url }})

Okno na kontrolu a opravu geometrie hornej matrice

Nástroj na kontrolu geometrie by ste mali použiť na každú 2D geometriu, ktorú importujete do programu DEFORM, aj keď geometria vyzerá správne.

Kliknite na položku **Pohyb** pod položkou **Horná forma** v strome operácií; keďže ide o izotermickú simuláciu, nie je potrebné vytvárať sieť ani priraďovať materiál k hornej forme.

### Priradenie ovládacích prvkov pohybu k hornej kocky

Predvoleným režimom je konštantná **rýchlosť**. Do poľa **Constant** zadajte hodnotu **3** in/sec a overte, či je smer nastavený na **-Y**, ako je znázornené na obrázku [Fig. L1.18.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_18_Top_die_movement_controls_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0018.jpg' | relative_url }})

Okno s ovládacími prvkami pre pohyb hornej matrice

Kliknite na **spodnú****matricu** v strome operácií, keďže vo okne vlastností hornej matrice nie je potrebné vykonávať žiadne zmeny.

### Definovanie všeobecných údajov o spodnej matrici

Nechajte predvolenú teplotu spodnej formy na hodnote 68 °F a overte, či je typ objektu **tuhý**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte geometriu spodnej formy.

### Vytvorenie geometrie spodnej matrice v editore geometrie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}), aby ste v editore geometrie definovali geometriu spodnej matrice. Uistite sa, že v tabuľke geometrie je vybraný formát **XYR**. Geometriu definujte tak, že body geometrie zadáte do tabuľky tak, ako je to znázornené na obrázku [Fig. L1.19.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_19_Bottom_die_geometry_table_with_geometry).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0019.jpg' | relative_url }})

Tabuľka geometrie spodnej matrice s geometriou

Tieto body budú vymedzovať geometriu proti smeru hodinových ručičiek, aby sa zabezpečilo, že orientácia geometrie bude smerovať dovnútra geometrie, ako je znázornené na obrázku [Fig. L1.20.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_20_Bottom_die_geometry_orientation)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0020.jpg' | relative_url }})

Orientácia geometrie spodnej matrice

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste uzavreli definíciu geometrie, a kliknite na položku **Polohovanie** v strome operácií, čím otvoríte okno na polohovanie objektov.

### Potvrdiť pozíciu a vytvoriť kontakt

**Potvrdiť pozíciu**

Geometrické prvky by mali byť v správnej polohe. Uistite sa, že obrobok je umiestnený na spodnej matrici a že horná matrica je priložená k obrobku, ako je znázornené na obrázku [Fig. L1.21.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_21_Correct_objects_positioning). Ďalšie polohovanie nie je pre túto operáciu potrebné.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0021.jpg' | relative_url }})

Správne umiestnenie objektov

Kliknutím na položku **Kontakt** v strome operácií otvoríte okno „Medzi objektmi“, keďže pre túto operáciu nie je potrebné naplánované polohovanie.

Poznámka:

Postup plánovaného umiestnenia je vysvetlený v dokumente [lab3]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Lab3_Sequential_3D_forge_operation).

**Vzťahy medzi objektmi: Nastavenie trenia; Vytvorenie kontaktu**

DEFORM automaticky vytvorí predvolené vzťahy typu „Master-Slave“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), čím vzniknú tri vzťahy, ako je znázornené na obrázku [Fig. L1.22.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_22_Inter_object_window_and_Objects_with_inter-object_contacts_display). DEFORM vytvorí tri vzťahy. Dva z nich budú také, v ktorých je každý nástroj hlavným prvkom a obrobok podriadeným prvkom. Tretí vzťah bude vzťahom typu (obrobok – obrobok). Tento vzťah umožní samokontakt obrobku v prípade, že dôjde k ohybu.

Kliknite na tlačidlo „Edit“ pri jednom z vzťahov. V poli **Friction**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Value** použite roletové menu „Constant“ a vyberte položku **Hot****forging**(lubricated) **0.3**. Ak máte skúsenosti, ktoré naznačujú, že iná hodnota trenia by pre váš proces priniesla lepšie výsledky, môžete túto hodnotu zadať priamo do tohto poľa. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustíte ponuku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) použijete túto hodnotu trenia na ďalšie dva vzťahy.

Ďalej priraďte kontakt. Počiatočné podmienky kontaktu predstavujú východiskovú situáciu pre riešiteľ konečných prvkov. Po spustení výpočtu riešiteľa sa kontakt automaticky aktualizuje.

Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerancia) vypočíta tolerancie pre vytvorenie kontaktov. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerancia) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) (v spodnej časti okna medzi objektmi). Mali by ste vidieť uzly kontaktu na obrobku, kde bol kontakt vygenerovaný. Pozrite si [Fig. L1.22.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_22_Inter_object_window_and_Objects_with_inter-object_contacts_display), kde je zobrazené, ako vyzerá okno Inter object a ako sa generovanie kontaktu zobrazuje v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0022.jpg' | relative_url }})

Okno medzi objektmi a zobrazenie objektov s kontaktmi medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili primárne ovládacie prvky zastavenia zdvihu matrice.

### Nastavenie zdvihu primárneho valca

Zadajte kritériá ukončenia, ktoré zastavia simuláciu, keď sa nástroj posunie o **6,25** ’’. Do poľa **Max****die****stroke** (smer **Y**) zadajte hodnotu 6,25, ako je znázornené v súbore [Fig. L1.23.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_23_Primary_die_displacement_Max_die_stroke_stopping_controls)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0023.jpg' | relative_url }})

Ovládacie prvky na zastavenie primárneho posunu formy (maximálny zdvih formy)

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali v priraďovaní ovládacích prvkov krokov.

### Priradiť ovládacie prvky krokov

Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do expertného režimu) (na paneli nástrojov v hlavičke), aby ste získali prístup k nastaveniam pokročilých ovládacích prvkov simulácie, pretože pre túto simuláciu je potrebné definovať kritériá pre vytvorenie novej siete.

Všimnite si, že názov simulácie sa zmenil na „**upset**“, tak ako ste ho premenovali v editore operácií na karte „Hlavné“. Prejdite na kartu **Simulácia****Kroky**.

DEFORM používa dvojfázový postup na stanovenie celkovej vzdialenosti pohybu razníka:

Na karte **Simulačné kroky** sa nastavuje počet krokov a interval ukladania. Na karte **Krok****Prírastok** sa definuje čas alebo pohyb nástroja na jeden časový krok. Ak nie sú definované žiadne ďalšie kontrolné mechanizmy zastavenia, celková dĺžka simulácie bude približne rovná **prírastku kroku** * **počtu krokov**.

Na vykonanie tejto operácie sa musí nástroj posunúť o 6,25’’, aby sa dosiahol požadovaný tvar. Na takéto jednoduché vyťahovanie by malo stačiť 75 krokov. Zmeňte **Počet simulačných krokov** na **75**. Zmeňte **Krok na uloženie** na **5**, ako je znázornené v [Fig. L1.24.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_24_Advanced_Step_controls_Simulations_steps_tab)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0024.jpg' | relative_url }})

Pokročilé nastavenia – karta „Kroky simulácie“

Ďalej prejdite na **Krok****Prírastok**. Hodnota posunu matrice predstavuje celkovú vzdialenosť, ktorú má nástroj prekonať (6,25’’), vydelenú počtom krokov (75). Pomocou možnosti „With Die Displacement“ (S posunom matrice) nastavte posun matrice na hodnotu **0,083** ’’ (6,25 / 75), ako je znázornené na obrázku [Fig. L1.25.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/' | relative_url }}#Fig_L1_25_Advanced_Step_controls_Step_increment_tab).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0025.jpg' | relative_url }})

Karta „Krok“ v nastaveniach „Pokročilé“

Na karte **Zastavenie** je možné nastaviť voliteľné špecifické riadenie zastavenia, ktoré môže byť založené na:

\- pôsobenie zaťaženia na objekt 2 (razník alebo pohyblivú matricu)

\- celkový posun objektu 2

\- dosiahnutie kritickej vzdialenosti alebo rozmeru medzi bodmi na dvoch rôznych nástrojoch.

Ovládacie prvky zastavenia odrážajú hodnotu 6,25’’ v poli **Primárny posun matrice** (smer Y), ktorá bola predtým definovaná v okne ovládacích prvkov zastavenia v režime vedenia.

Prejdite na kartu **Kritériá pregenerovania siete**. Hodnota **Hĺbka interferencie** by mala predstavovať polovicu dĺžky hrany malého prvku. Zmerajte dĺžku jedného z menších prvkov, vydelte ju 2 a túto hodnotu zadajte do poľa pre hĺbku interferencie (pozri [Fig. L1.26.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_26_Advanced_Step_controls_Remesh_criteria_tab)). Mali by ste dostať hodnotu okolo 0,02’’. Prepočítanie siete sa spustí, ak niektorý z nástrojov dokáže preniknúť do obrobku do vzdialenosti 0,02’’.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0026.jpg' | relative_url }})

Karta „Kritériá pre výpočet novej siete“ v nástroji Advanced Step

Teraz kliknite na položku **Pohyb** pod položkou „Horná matrica“ v strome operácií, aby ste si prezreli náhľad pohybu hornej matrice, pretože pred zobrazením náhľadu pohybu je potrebné definovať krok a pohyb.

### Potvrdiť pohyb

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) (Náhľad pohybu objektu) v pravom dolnom rohu obrazovky (pozri [Fig. L1.18.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_18_Top_die_movement_controls_window)). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_movement_play_button.jpg' | relative_url }}) (prehrávanie) (pozri [Fig. L1.27.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_27_Top_die_movement_preview_window)) a sledujte, ako sa horná matica pohybuje cez obrobok. Tento nástroj potvrdí, že sa váš nástroj pohybuje správnym smerom a že máte dostatok krokov na dokončenie zdvihu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0027.jpg' | relative_url }})

Okno s náhľadom pohybu hornej matrice

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili ponuku, a v strome operácií kliknite na **Generate****DB**, čím spustíte generovanie databázy.

### Kontrola údajov a vytvorenie databázy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), ako je znázornené na obrázku [Fig. L1.28.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_28_DB_generation_window). Systém kontroly údajov potvrdí, že všetky údaje sú vhodné na spustenie simulácie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0028.jpg' | relative_url }})

Okno na generovanie databázy

Červené označenia signalizujú chýbajúce alebo nesprávne údaje, ktoré zabránia spusteniu simulácie. Pred vytvorením databázy je potrebné chybu opraviť.

Žlté značky označujú údaje, ktoré môžu byť pochybné a mali by sa preveriť. Tieto údaje je potrebné dôkladne preskúmať, pretože môžu spôsobiť nestabilitu systému alebo chybné (nesprávne) výsledky.

Preverte informácie o kontrole údajov. Ak sa nezobrazujú žiadne žlté ani červené značky, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Mali by ste hľadať text: **Databáza bola vytvorená**. Keď sa vám tento text zobrazí, môžete si byť istí, že vaše údaje boli uložené do databázy a teraz ste pripravení spustiť simuláciu.

Kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustenie a sledovanie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spustení) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0029.jpg' | relative_url }})

Spustenie simulácie z režimu simulácie MO

Aktualizácie stavu simulácie v simulačných úlohách, ako aj simulačné a protokolové správy je možné sledovať na iných kartách.

V grafickej oblasti sa zobrazí grafika simulácie. V grafike simulácie môžete sledovať priebeh simulácie počas jej vykonávania; štandardne sa tu aktualizuje posledný uložený krok. Ak chce používateľ aktualizovať aktuálny krok, musí kliknúť pravým tlačidlom myši a zvoliť možnosť „Monitorovanie aktuálneho kroku“.

Osvedčeným postupom je sledovať prvých niekoľko krokov simulácie v grafickom režime simulácie, aby ste sa uistili, že pohyby nástroja a deformácia obrobku prebiehajú podľa očakávaní.

V grafickom zobrazení simulácie sú k dispozícii obmedzené ovládacie prvky pre zobrazenie. Okrem toho sú k dispozícii nasledujúce ovládacie prvky pre priblíženie:

\- **Ctrl** – **ľavé tlačidlo myši**: zmenšenie/zväčšenie okna

\- **alt** – **ľavé tlačidlo myši** : dynamické priblíženie

\- **shift** – **ľavé tlačidlo myši** : posun

Používateľ môže tiež zmeniť klávesové skratky v časti **Možnosti![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nastavenia ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Klávesové skratky.**

Tieto funkcie možno využiť na lepší prehľad o podrobnostiach obrobku počas prebiehajúcej simulácie. Po dokončení simulácie sa obrázok v prehliadači Simulation Graphics skryje. V poslednom riadku súboru so správami (predvolené zobrazenie v hlavnom okne) a v súbore protokolu bude uvedené, že simulácia bola dokončená.

Po dokončení simulácie kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky kontroly v režime príspevku

V grafickom okne sa zobrazujú výsledky výpočtu.

Uložené kroky sú zobrazené v prehliadači krokov v spodnej časti grafického okna, ako je znázornené na obrázku [Fig. L1.30.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_30_Step_browser_for_upset_operation)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0030.jpg' | relative_url }})

Krokový prehliadač pre prevádzku v núdzovom režime

Ovládacie prvky hry slúžia na:

![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) **Prehrávanie dopredu**: Zobrazuje kroky jeden po druhom, až kým sa od aktuálne vybraného kroku nezobrazí posledný krok.

![]({{ '/assets/icons/pre_icons/mo_preview_stop_button.jpg' | relative_url }}) **Stop** : Zastaví prehrávanie (dopredu alebo dozadu) krokov.

**![]({{ '/assets/icons/pre_icons/mo_preview_one step_forward_button.jpg' | relative_url }})Jeden krok vpred** : Prejsť na ďalší uložený krok v zozname krokov.

![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }}) **Preskočiť na koniec** : Preskočí na posledný uložený krok v zozname krokov.

![]({{ '/assets/icons/pre_icons/mo_preview_play_back_button.jpg' | relative_url }}) **Prehrávať spätne**: Zobrazuje kroky jeden po druhom v opačnom poradí, až kým sa od aktuálne vybraného kroku nezobrazí prvý krok.

![]({{ '/assets/icons/pre_icons/mo_preview_one_step_back_button.jpg' | relative_url }}) **Jeden krok späť**: Posuňte zoznam krokov späť o jeden uložený krok.

**![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }})Preskočiť na začiatok** : Vrátiť zoznam krokov späť na prvý uložený krok.

**Prejdite si simuláciu.**

**Graf závislosti zaťaženia od zdvihu**

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) v nástrojoch príspevku. Vykreslite graf závislosti zaťaženia (Y) na zdvihu pre hornú maticu výberom tlačidla ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}). Graf zobrazuje zaťaženie v ľubovoľnom bode simulácie (pozri [Fig. L1.31.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_31_Velocity_vector_plot_with_Load_stroke_graph_for_top_die)). Vertikálny indikátor krokov označuje aktuálny krok. Kliknutím na ľubovoľný bod na grafe zaťaženia v závislosti od zdvihu (alebo na akýkoľvek graf v programe DEFORM) sa zobrazia výsledky v danom kroku. Graf je možné skryť alebo odstrániť kliknutím pravým tlačidlom myši na položku grafu v spodnej časti stromu.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustíte okno „Load stroke“ a môžete vykresliť stavové premenné.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0031.jpg' | relative_url }})

Graf rýchlostného vektora s grafom zdvihu zaťaženia pre hornú matricu

**Grafy stavových premenných**

  * **Graf rýchlosti**

Vyberte krok **75** (alebo akýkoľvek iný medzistupeň na lište výberu krokov). Kliknite na ikonu stavovej premennej ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}) (Celková rýchlosť) v skratkách **Post tools![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})** **State****Variables**. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) otvoríte dialógové okno s vlastnosťami stavovej premennej. Vyberte typ zobrazenia Vektorový graf a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) potvrďte zmeny. Okamžité rýchlosti sa zobrazujú ako vektory v zvolenom časovom kroku. Farby slúžia na zvýraznenie veľkosti rýchlosti. (Pozri [Fig. L1.31.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_31_Velocity_vector_plot_with_Load_stroke_graph_for_top_die))

  * **Graf efektívneho napätia**

V dialógovom okne so stavovými premennými vyberte zoznam premenných ![]({{ '/assets/icons/post_icons/mo_deformation_icon.jpg' | relative_url }}) (Deformácia) položku **Strain![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Effective******. Táto hodnota predstavuje veľkosť deformácie počas simulovaného procesu. Pri tvárnení za studena súvisí s pracovným spevnením.

Prejdite si simuláciu a sledujte, ako sa deformácia vyvíja počas tvarovania dielu. Premenná stavu dosahuje maximálnu hodnotu kdekoľvek v priebehu simulácie.

Vyberte **Lokálne** škálovanie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Spustite simuláciu. V každom kroku sa stavové premenné preškálujú na maximálnu hodnotu v danom kroku.

Vyberte možnosť „Solid display“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Obrysy sa zmenia na ostré hrany (pozri [Fig. L1.32.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_32_Effective_strain_state_variable_contour_at_local,_global_scale)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0032.jpg' | relative_url }})

Kontúra efektívnej premennej deformácie v miestnom a globálnom meradle

Keď dokončíte prezeranie výsledkov, kliknutím zatvorte okno „State variable“. Mierku a typ grafu je možné zmeniť aj pomocou možností, ktoré sa zobrazia po kliknutí pravým tlačidlom myši na lištu s vrstevnicami.

Kliknutím na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) prejdete do režimu „Pre“ a budete môcť pokračovať v ďalšom laboratórnom cvičení č. 2.

Kliknite na [Lab 2. 2D to 3D Conversion to sequence 3D operation after 2D operation]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab2/' | relative_url }}), aby ste nastavili Lab6.
