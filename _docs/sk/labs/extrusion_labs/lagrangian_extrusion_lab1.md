---
lang: sk
title: "Laboratórium Lagrangovej extruzie 1"
---

# Lagrangeovská extrúzia – laboratórna práca č. 1

V tomto laboratórnom cvičení nastavujeme prevádzku Lagrangeovho vytláčania.

V rámci tohto laboratórneho cvičenia sa z veľkého valcového polotovaru vytlačia 5 malých valcových dielov. Model obrobku je znázornený na obr. LAGEXL1.1. Priemer D0 je 140 mm. Priemer D1 je 26 mm. Priemery D2 a D4 sú 27 mm. Priemery D3 a D5 sú 28 mm. Vzhľadom na to, že model je symetrický, v tomto cvičení použijeme na simuláciu štvrtinový model.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0001.jpg' | relative_url }})

Model obrobku

1.1. Vytvorenie nového problému

1.2. Pridať operáciu

1.3. Nastavenie simulácie

1.4. Zoznam materiálov

1.5. Matrice

1.6. Ram

1.7. Kontajner

1.8. Zomrieť

1.9. Obrobok

1.10. Ovládacie prvky

1.11. Kontakt

1.12. Ovládacie prvky krokov

1.13. Vytvorenie databázy

1.14. Spustenie simulácie

1.15. Následné spracovanie

## Vytvorenie nového problému 

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obrázku LAGEXL1.2.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0002.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. LAGEXL1.3. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek „**SI**“. Zadajte názov úlohy ako „********3D_Lagrangian_EX_Lab1****“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0003.jpg' | relative_url }})

Stránka „Nový problém“

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“, kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_Lagrangian_EX_Lab1**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

## Pridanie operácie

Pridajte **operáciu 3D extruzného tvarovania** zo zoznamu operácií v Průzkumníku. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky 3D Extrusion alebo ju môžete pridať aj pretiahnutím do editora operácií (pozri obr. LAGEXL1.4.). Po pridaní operácie 3D Extrusion sa štandardne otvorí okno nastavení procesu.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0004.jpg' | relative_url }})

Pridanie operácie extrudovania

## Nastavenie simulácie

V dialógovom okne Nastavenie simulácie vyberte v položke Metóda simulácie voľbu **Lagrangeovská extruzia (inkrementálna)**. Nastavte položku Tepelný výpočet na **Iba obrobok (neizotermický)** a typ modelu formy na **S podmienkou symetrie**. Nastavenia simulácie sú zobrazené na obr. LAGEXL1.5. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Zoznam materiálov.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0005.jpg' | relative_url }})

Nastavenia simulačného prostredia

## Zoznam materiálov

V dialógovom okne „Materiál“ kliknite na možnosť „Načítať údaje o materiáli z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})“. Načítajte materiál „**ALUMINUM-6061[70-1000F(20-550C)]**“ z kategórie **Hliník**, ako je znázornené na obr. LAGEXL1.6., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku „Matrice“.

.![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0006.jpg' | relative_url }})

Zoznam materiálov

## Matrice

V predvolenom nastavení sa do prevádzky pridajú 2 matrice, v tomto laboratórnom cvičení však potrebujeme 3 matrice. Kliknite teda na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}), aby ste nastavili počet matríc na 3 (pozri obr. LAGEXL1.7.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Top Die“ (Horná matrica).

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0007.jpg' | relative_url }})

Pridané matrice

## Ram

Zmeňte názov objektu „Top Die“ na **Ram**. Nastavte **teplotu** matrice na **400** °C a typ objektu ponechajte ako **Rigid**. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Geometry“.

### Geometria berana

Kliknite na položku „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a načítajte súbor **Ram_Geo.stl** zo zložky 3D/LABS, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). V dialógovom okne „Symetria“ nastavte pre Ram **rovinnú symetriu** na symetrických rovinách, ako je znázornené na obrázku (pozri obr. LAGEXL1.8.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Pohyb“.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0008.jpg' | relative_url }})

Geometria berana

### Pohyb barana

V dialógovom okne „Pohyb“ nastavte **rýchlosť** na hodnotu **4** mm/s, ako je znázornené na obr. LAGEXL1.9. Kliknite na stránku „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) do spodnej formy“.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0009.jpg' | relative_url }})

Stránka hnutia Ram

## Kontajner

Zmeňte názov spodnej formy na **Container**. Nastavte **teplotu** formy na **350** °C a typ objektu ponechajte na **Rigid**. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Geometria.

### Geometria kontajnera

Kliknite na „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a načítajte súbor **Container_Geo.stl** zo zložky 3D/LABS, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). V dialógovom okne Symetria nastavte pre kontajner **rovinnú symetriu** na symetrických rovinách, ako je znázornené na obr. LAGEXL1.10. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Pohyb.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0010.jpg' | relative_url }})

Geometria kontajnera

### Preprava kontajnerov

V dialógovom okne „Pohyb“ ponechajte hodnotu **Rýchlosť** na **0** mm/s. Kliknite na stránku „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) do objektu 4“.

## Zomrieť

Zmeňte názov objektu 4 na **Die**. Nastavte **teplotu** formy na **350** °C a typ objektu ponechajte ako **Rigid**. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Geometria.

### Geometria lisovacej formy

Kliknite na položku „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a načítajte súbor **Die_Geo.stl** zo zložky 3D/LABS, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). V dialógovom okne „Symetria“ nastavte pre maticu **rovinnú symetriu** na symetrických rovinách, ako je znázornené na obr. LAGEXL1.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Pohyb“.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0011.jpg' | relative_url }})

Geometria

### Pohyb matrice

V dialógovom okne „Pohyb“ ponechajte hodnotu **Rýchlosť** na **0** mm/s. Prejdite na stránku „Obrobok“ kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Obrobok

Názov objektu obrobku ponechajte ako predvolený, t. j. **Workpiece**. Nastavte teplotu obrobku na **400** °C a typ objektu ponechajte ako **Plastic**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Geometria.

### Geometria obrobku

Obrobok je symetrický valec, ktorý možno v programe DEFORM ľahko vytvoriť. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), vyberte **Valec** a nastavte **Výšku** (H) na **178** mm a **Priemer****(2R)** na **138** mm. Nastavte **Počiatočný uhol** na **0**, **Uhol otáčania** na **90** a **Počet rezov** na **90**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). V dialógovom okne Symetria nastavte pre obrobok **Rovinnú symetriu** na symetrických rovinách, ako je znázornené na obr. LAGEXL1.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku s typom generovania siete.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0012.jpg' | relative_url }})

Geometria obrobku

### Sieť obrobku

Vo všeobecnosti platia dve pravidlá pre nastavenie hustoty siete pri simulácii extruzie. Po prvé, v celej hrúbke najtenšieho profilu by mali byť aspoň tri prvky. Zároveň by sieť v blízkosti nosných zón mala byť jemnejšia ako na ostatných miestach.

Na stránke „Mesh Generation Type“ sú k dispozícii dve možnosti vytvárania siete. Jednou z nich je „Mesh Extruding Utility“ a druhou „Regular Meshing“. Pre Lagrangeovú extruziu vyberte možnosť **Regular Meshing**. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku „Regular meshing“.

V dialógovom okne **Všeobecné** vyberte typ „**Absolútny** “, nastavte **Pomer veľkostí** na hodnotu „**3**“ a **Minimálnu veľkosť prvku** na hodnotu „**2** mm“, ako je znázornené na obr. LAGEXL1.13.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0013.jpg' | relative_url }})

Hlavná stránka sekcie „Mesh“

V dialógovom okne **Váha******faktory** nastavte faktor **okien siete** na hodnotu „**1,0**“ a **ostatné****faktory** na hodnotu „**0,0**“, ako je znázornené na obr. LAGEXL1.14.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0014.jpg' | relative_url }})

Stránka „Mriežka obrobku – váhový koeficient“

V dialógovom okne „Mesh Windows“ kliknite na položku „Import Mesh Windows from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})“ a otvorte súbor **UL_Workpiece_Mesh_Window.key** zo zložky **3D/LABS**.

Namiesto importovania sieťových okien ich môžete vytvoriť aj postupne.

  1. Na karte „Mesh Window“ (Okno siete), ak sa tam nachádza nejaké okno siete, kliknite na ![]({{ '/assets/icons/pre_icons/mo_delete_symmetry_icon.jpg' | relative_url }}), aby ste najskôr odstránili všetky existujúce okná siete.

  2. Na karte „Mesh Window“ postupne klikajte na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), aby ste vytvorili 4 okná siete.

  3. V každom z týchto okien kliknite na jeho názov, aby ste ho označili, potom v ľavom hornom rohu **dialógového okna Definícia okna** kliknite na tvar valcového okna a kliknutím na obrazovku v oblasti obrobku vložte okno s valcovou sieťou do **zobrazovacieho okna.**

  4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}), aby ste upravili rozmery jednotlivých okien. Upravte rozmery mriežky „Okno 1“, nastavte horný stred na (0,0,10) a dolný stred na (0,0,-20), polomer nastavte na 80. Upravte rozmery mriežky Okno 2, nastavte horný stred na (0,0,-19) a dolný stred na (0,0,-250), polomer nastavte na 150. Upravte rozmery mriežky „Okno 3“, nastavte horný stred na (0,0,35) a dolný stred na (0,0,9), polomer nastavte na 90. Upravte rozmery siete v okne 4, nastavte horný stred na (0,0,200) a dolný stred na (0,0,34), polomer nastavte na 100. Po každej úprave kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

  5. Nastavte veľkosť prvkov siete v okne 1 na „2 mm“, veľkosť prvkov siete v okne 2 na „3 mm“, veľkosť prvkov siete v okne 3 na „4 mm“ a veľkosť prvkov siete v okne 4 na „6 mm“.

Pri Lagrangeovej extrúzii sa okná siete použijú na počiatočné vytvorenie siete a na opätovné vytvorenie siete počas simulácie. Musíme teda zohľadniť rozsah toku materiálu počas simulácie a definovať správne okná siete.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0015.jpg' | relative_url }})

Po definovaní okien siete kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). V dialógovom okne **Predvolené okrajové podmienky** kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}).

Vytvorenie siete obrobku je znázornené na obr. LAGEXL1.15. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku „Materiál“.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0015_1.jpg' | relative_url }})

Stránka „Okná so sieťou obrobkov“

### Materiál obrobku

Ako materiál pre obrobok zadajte **ALUMINUM-6061[70-1000F(20-550C)]** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s okrajovými podmienkami.

### Okrajová podmienka obrobku

Systém po vytvorení siete automaticky priradil obrobku rovinu symetrie BCC (pozri obr. LAGEXL1.16.).

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0016.jpg' | relative_url }})

Symetria BCC obrobku

Systém po vytvorení siete automaticky priradil k obrobku výmenu tepla s prostredím BCC. Výsledok je zobrazený na obr. LAGEXL1.17. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostanete na stránku Vlastnosti.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0017.jpg' | relative_url }})

Tepelná BCC obrobku

### Cieľový objem obrobku

Na stránke **Vlastnosti** zaškrtnite políčko Aktívne v časti **FEM + vytváranie siete**, kliknite na ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) a nastavte Objem ako počiatočný objem obrobku (pozri obr. LAGEXL1.18.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostanete na stránku Ovládanie.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0018.jpg' | relative_url }})

Nastavenie cieľového objemu obrobku

## Ovládacie prvky

Na stránke „Ovládanie“ môžeme pomocou ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) nastaviť polohy objektov.

Všetky súčasti formy boli naimportované zo súborov .stl. Kontajner aj forma sa nachádzali na správnych miestach. Závit je vzdialený od obrobku. Keďže bol obrobok vytvorený ako primitív v programe DEFORM, musíme posunúť závit nadol, aby sa dotýkal obrobku.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) a zadajte polohovanie s ohľadom na kolízie. Ako polohovací objekt vyberte beran a ako referenčný bod obrobok. Overte, či je smer priblíženia **–Z**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku „Kontakt“.

## Kontakt

Na stránke „Kontakt“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), aby ste vytvorili všetky vzťahy obrobku s ostatnými objektmi. Následne upravme nastavenie parametrov pre kontaktné vzťahy obrobku.

  * Vyberte vzťah **Ram – Obrobok** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Nastavte oddelenie kontaktov na hodnotu „**Oddeliteľné**“, trenie **šmykové** na hodnotu „**1,0**“ a koeficient prenosu tepla na hodnotu „**11,0**“.

  * Vyberte vzťah **Kontajner – Obrobok** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Nastavte oddeľovateľnosť kontaktu na hodnotu „**Oddeliteľný**“, trenie **šmykové** na hodnotu „**1,0**“ a koeficient prenosu tepla na hodnotu „**11,0**“.

  * Vyberte vzťah **Forma – Obrobok** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Nastavte oddelenie kontaktných plôch na hodnotu „**Oddeliteľné**“, trenie **šmykové** na hodnotu „**0,4**“ a koeficient prenosu tepla na hodnotu „**11,0**“.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) nastavíte inteligentnú toleranciu kontaktov. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujete kontakty pre všetky vzťahy.

Kontakty obrobku s inými objektmi sú znázornené na obr. LAGEXL1.19. Vidíme kontakty obrobku s piestom a maticou. V súčasnosti nedochádza ku kontaktu obrobku s nádobou, pretože medzi týmito dvoma objektmi je medzera. Počas simulácie sa obrobok roztiahne a dostane sa do kontaktu s nádobou. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Step Control.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0019.jpg' | relative_url }})

Dotykové body obrobku

## Ovládacie prvky krokov

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) v hornom paneli ponúk prepnite do expertného režimu pre krokové riadenie.

### Kroky simulácie

V dialógovom okne **Simulačný krok** nastavte **Počet simulačných krokov** na hodnotu **400** a **Krok ukladania** na hodnotu **20**. Nastavte **Primárny čip** na ' **2 -Ram** ' (pozri obr. LAGEXL1.20.).

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0020.jpg' | relative_url }})

Nastavenie simulačného kroku

### Krok prírastku

Pri simulácii extruzie podľa Lagrangeovej metódy, ak medzi polotovarom a nádobou existuje medzera, prvou fázou deformácie je stlačenie polotovaru s cieľom vyplniť túto medzeru, druhou fázou deformácie je samotný proces extruzie.

Pri simulácii extrudovania platí všeobecné pravidlo pre nastavenie veľkosti kroku, že v žiadnom kroku nechceme, aby sa materiál posunul o viac ako 1/3 veľkosti prvku.

Aby sme správne nastavili veľkosť kroku, mali by sme sa oboznámiť s niektorými základnými parametrami extrudovania v danej aplikácii.

V tomto príklade má štvrťový model vstupnú plochu 3846,50 mm² a výstupnú plochu 726,52 mm². Pomerný výtlak je teda 5,29.

Ak v Lagrangeovej simulácii použijeme sochoru s priemerom 138 mm a výškou 178 mm, plocha sochory pre štvrtinový model je 3737,39 mm². Objemová medzera medzi sochárskou tyčou a nádobou je 19 421,58 mm³ ((3 846,50 – 3 737,39) × 178). Výška, o ktorú musí polotovar vyjsť, aby vyplnil objemovú medzeru, je 5,20 mm (19 421,58 / 3 737,39). Ak je rýchlosť pohybu piestu 4 mm/s, čas potrebný na vyplnenie objemovej medzery je 1,30 s.

Na základe uvedeného môžeme v jednotlivých fázach deformácie nastaviť rôzne krokové prírastky. Vo fáze vyplňovania medzery je minimálna veľkosť prvku 2 mm, rýchlosť pohybu piestu je 4 mm/s, takže vhodný čas na jeden krok piestu by bol 0,17 s/krok. Vo fáze extrudovania je minimálna veľkosť prvku 2 mm, rýchlosť pohybu extrudátu je 21,16 mm/s, takže vhodný čas kroku piestu by bol 0,03 s/krok.

V dialógovom okne **Krok prírastku** nastavte **Definíciu kroku riešenia** na **Čas**. Nastavte **Ovládanie kroku** na **f(zdvih)** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}). Nastavte funkciu podľa obr. LAGEXL1.21. a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

**Mŕtvica** |  **Definícia kroku**  
---|---  
0 |  0,17  
5,2 |  0,17  
5,21 |  0,03  
200 |  0,03  
  
![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0021.jpg' | relative_url }})

Definícia kroku

Mimochodom, ak je medzera veľmi malá, môžeme pre celý proces deformácie použiť aj konštantný krok s primeraným časom na krok v fáze extrudovania.

### Kritériá na ukončenie

V dialógovom okne **Kritériá zastavenia** nastavte hodnotu **Primárny****posun****matrice** Z na **28** mm, ako je znázornené na obr. LAGEXL1.22.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0022.jpg' | relative_url }})

Ovládanie zastavenia

### Nastavenia dvojitých obmedzení

Aby sa zabránilo úniku rýchlosti v tvárnici a aby bolo možné vypočítať správnu výstupnú rýchlosť, je pri extrudovaní lepšie nastaviť na hranách dvojité obmedzenia.

V dialógovom okne „Kontrolné súbory“ zaškrtnite políčko **Dvojité obmedzenia na hranách**, nastavte **rozsah uhlov** od **75** stupňov do **105** stupňov a zaškrtnite tiež políčko **Zahrnúť konvexné** hrany (pozri obr. LAGEXL1.23.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vygenerovanie databázy.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0023.jpg' | relative_url }})

Nastavenie dvojitých obmedzení

## Vytvoriť databázu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali, či sa pri nastavení na niečo nezabudlo, a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy. Pozrite si správu na karte Správa, ktorá informuje o stave vytvárania databázy.

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. LAGEXL1.24. Použite predvolenú možnosť **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ (od kroku -1) a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“, v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0024.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie môžete sledovať na kartách „Simulation Message“ a „Simulation Log“; uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže sledovať proces extrudovania na simulačných grafoch v priebehu simulácie až do dosiahnutia zadaného kroku.

## Následné spracovanie

Zo súboru so správami je zrejmé, že po kroku 215 sa zobrazili hlásenia „PROGRAM STOPPED!“ a „THE Z STROKE 28.0000000 HAS REACHED THE SPECIFIED LIMIT 28.0000000“.

Po dokončení simulácie si výsledky prezrite tak, že prejdete do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov Simulácia.

Prejdite jednotlivými krokmi simulácie a sledujte, ako sa obrobok pohybuje v oblasti extrudátu pri Lagrangeovom procese extrudovania. Z výsledkov simulácie je zrejmé, že okrajové profily (D2 a D3) sa počas procesu extrudovania ohýbajú smerom k centrálnemu profilu (D1).

Grafy efektívneho deformácie a teploty obrobku v poslednom kroku sú uvedené na obr. LAGEXL1.25 a obr. LAGEXL1.26.

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0025.jpg' | relative_url }})

Efektívne rozloženie deformácie obrobku v poslednom kroku

![]({{ '/assets/images/labs/extrusion_labs/lagrangian_extrusion_lab1/image0026.jpg' | relative_url }})

Rozloženie teploty obrobku v poslednom kroku
