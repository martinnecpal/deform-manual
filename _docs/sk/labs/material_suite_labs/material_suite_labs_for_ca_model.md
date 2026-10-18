---
lang: sk
title: "Laboratóriá Material Suite pre model Cellular Automata (CA)"
---

# Material Suite Labs pre model mobilných automatov (CA)

Abstrakt

Laboratórium 1: CA model pre dynamickú rekryštalizáciu

1.1 Spustenie modelu CA v Material Suite

1.2 Zadajte rozsah krokov, výber objektu a výber bodu

1.3 Nastavenie modelu CA

1.4 Spustiť simuláciu CA

Bežné obdobie

Laboratórium 2: CA model pre statický rast zŕn

2.1 Spustiť model CA v Material Suite

2.2 Špecifikovať rozsah krokov Výber objektu a výber bodu

2.3 Nastavenie modelu CA

2.4 Spustiť simuláciu CA

2.5 Výstup

Abstrakt

Rozšírená rekryštalizácia a kinetika rastu zŕn na úrovniach mesoscale [1-6] sú teraz k dispozícii v modeloch deformovaných 12.1 bunkových automatov (CA). Model CA je možné spustiť v režime následného spracovania buď v postprocesore Material Suite alebo Next Generation (NG) na vybraných miestach a dokončená nominálna 2D alebo 3D databáza je predpokladom na spustenie modelu DEFORMÁCIE CA. Je možné uvažovať o rôznych mechanizmoch, vrátane dynamickej rekryštalizácie (DRX), metadynamickej rekryštalizácie (MRX), statickej rekryštalizácie (SRX) a statického rastu zrna (SGG). Môžu sa zvážiť tri typické kryštálové štruktúry pre kovové materiály (FCC, BCC a HCP) a dezorientačný uhol medzi susednými zrnami sa vypočíta z hľadiska kryštálovej symetrie. Používateľské rutiny a modely CA sú podporované. Materiál môže byť jednofázový, dvojfázový alebo viacfázový. Počiatočná mikroštruktúra pre CA model môže byť generovaná deformáciou na základe priemernej veľkosti zrna, odchýlky veľkosti zrna, pomeru strán, objemového podielu fázy a rozdelenia sekundárnej fázy. Import údajov EBSD pre počiatočnú mikroštruktúru modelu CA je podporovaný. Pre dvojfázový alebo viacfázový materiál s rekryštalizáciou sekundárnej fázy by mal používateľ v súčasnosti implementovať svoj vlastný model CA prostredníctvom používateľských rutín.

Základnými vstupnými údajmi pre model CA sú údaje bodového sledovania modelu termomechanického procesu (TMP) (čas, krok, deformácia, rýchlosť deformácie, teplota, gradient deformácie a gradient rýchlosti), parametre materiálu a počiatočná mikroštruktúra. Pre každý uložený krok v nominálnej databáze výstup z modelu CA zahŕňa podrobnú mikroštruktúru, ako je priemerná hustota dislokácie, prietokové napätie, počet zŕn, priemerná veľkosť zŕn a podiel objemu rekryštalizácie. Je možné vykresliť odchýlku prietokového napätia, priemernú veľkosť zrna a objemový podiel rekryštalizácie s deformáciou (alebo časom).

V tomto laboratóriu sa simuluje dynamická rekryštalizácia počas kovania a statický rast zŕn počas žíhania superzliatiny na báze niklu IN718 modelom CA v DEFORM Material Suite.

Laboratórium 1: CA model pre dynamickú rekryštalizáciu

## Spustiť model CA v balíku materiálov

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v12.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI.
  
Požadujeme nominálnu DB na vykonanie simulácie CA v súbore materiálov, pre toto laboratórium použijeme * * Forging_IN718_Nominal.key* * z priečinka **\MANUALS\PDF \DEFORM_CA_Lab** na vygenerovanie nominálnej DB. Operácia je rovnomerná kompresia predvalku IN718 pri teplote 1050 °C pri rýchlosti deformácie 1/s. Otvorte NG Pre pomocou prepojenia DEFORMÁCIE GUI Main a definujte ID problému ako "**Forging_IN718 ** ", vyberte prepínač "* * 2D * * " Dimension a "**System International (SI)** " unit System prepínač v okne New Problem, potom importujte ** Forging_IN718_Nominal.key ** z priečinka **\MANUÁLY\PDF \DEFORM_CA_Lab **. Prejdite na stránku Generovať databázu a kliknite na " Generovať databázu ", aby ste vytvorili databázu. Prepnite na kartu "Simulácia" a spustite simuláciu, uistite sa, že simulácia sa zastaví normálne bez akéhokoľvek problému. Teraz z hlavného grafického rozhrania kliknite na **Material Suite** v časti „Post Processor“ a otvorte modul Material Suite. Používateľ môže tiež dvakrát kliknúť na "DEF_GUI_MAT.exe" v inštalačnom adresári DEFORMAČNÉHO softvéru a spustiť sadu materiálov.
  
Po zobrazení hlavného okna pre sadu materiálov kliknite na ikonu "Otvoriť..." ( ![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}) ) v hornom paneli nástrojov a importujte vzorovú databázu (**Forging_IN718.DB**). Do stromu úloh sa pridá predvolená položka úlohy „DEFORMOVAŤ“. Rozbaľte položku „Mikroštruktúra“ a kliknite na ikonu „Model zrna CA“, do stromu úloh sa pridá nová položka úlohy „Model CA“, ako je znázornené na obr. L1.1.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0001.jpg' | relative_url }})

Spustiť model CA v balíku materiálov

## Zadajte rozsah krokov, výber objektu a výber bodu

Ako je znázornené na obr. L1.2., v strome úloh „DEFORMOVAŤ“ kliknite na položku „**Zadať rozsah** “ a vyberte prepínač „* * Všetky kroky * * “. Po dokončení definície údajov klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdeme na ďalšiu položku stromu úloh. Môžeme tiež kliknúť priamo na položku v strome úloh a otvoriť okno definície údajov.

Pre položku „** Výber objektu ** “ vyberte položku „**Obrobok* * “ ( obr. L1.3.). Pre položku „* * Výber bodu * * “ definujte číslo kroku ako „-1“ a definujte jeden bod na obrobku ( obr. L1.4.). Vyberieme jeden bod v sochore (napr. súradnicu (69.22, 132.09, 0, 1)). Používatelia si môžu zvoliť ľubovoľné číslo kroku, ktoré im vyhovuje, napríklad posledný krok, na definovanie bodov.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0002.jpg' | relative_url }})

Zadajte rozsah krokov

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0003.jpg' | relative_url }})

Object Selection

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0004.jpg' | relative_url }})

Výber bodu

## Nastavenie modelu CA

Všetky údaje pre model CA sú pripravené položkami uvedenými v strome úloh „** Model CA ** “. Kliknite na položku „**Config** “, jej okno definície údajov sa zobrazí tak, ako je znázornené na obr. L1.5. Kliknutím na tlačidlá definície (![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }})) zadajte spustiteľný súbor pre simuláciu CA a pracovný adresár. Predvolený spustiteľný súbor pre simuláciu CA implementovanú v DEFORMÁCII je „DEF_CA.EXE“, ktorý sa nachádza v inštalačnom adresári softvéru DEFORM. Pracovný adresár musí byť ten, v ktorom sa nachádza nominálna databáza.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0005.jpg' | relative_url }})

Stránka konfigurácie

  
Kliknite na položku „* * Initial ** * * input * * “ pod položkou stromu „* * Input * * “, ako je znázornené na obr. L1.6. Ak chcete definovať veľkosť modelu CA, zadajte 320 buniek pre riadky a 320 buniek pre stĺpce a zadajte 1 mikrón pre dĺžku jednotkovej bunky. Pre susedstvo vyberte prepínač „Moore (9 buniek)“.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0006.jpg' | relative_url }})

Počiatočný vstup

Počas definície vstupných údajov pre každú položku stromu sa môžeme vrátiť na stránku „* * Initial * ****** input * * “ a kliknutím na „**Save project** “ uložiť údaje o projekte. Ak existuje uložené nastavenie projektu, môžeme ho načítať kliknutím na tlačidlo „* * Importovať projekt * * “. Rovnaké funkcie sú k dispozícii po rozbalení ponuky „**Súbor** “ a kliknutí na položku ponuky „**Uložiť projekt sady materiálov * *“ alebo „* *Importovať projekt sady materiálov ** “.

Kliknite na položku „**Počiatočná možnosť** “ a zobrazí sa jej okno s údajmi, ako je znázornené na obr. L1.7. Existujú dve možnosti generovania počiatočnej mikroštruktúry pre CA model a to (1) import z experimentálnych údajov EBSD alebo (2) generovaný deformačný systém. V tomto laboratóriu vyberte prepínač „System generated“, nastavte priemernú veľkosť zrna na 32,58 mikrónov, štandardnú odchýlku na 5 mikrónov, pomer strán na 1 a typ kryštálu na „FCC“, kliknite na tlačidlo „Generate“. Po vygenerovaní mikroštruktúry sa v zobrazovacom okne zobrazí obraz morfológie zŕn, obraz hraníc a fáz zŕn (pre dvojfázový materiál) a histogram pre rozdelenie veľkosti zŕn so štatistickými informáciami. Taktiež je uvedený počet zŕn.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0007.jpg' | relative_url }})

Počiatočná možnosť

Pri metóde „generovanej systémom“ je možné okrem jednofázovej mikroštruktúry generovať aj dvojfázovú mikroštruktúru. Pre sekundárnu fázu musíme zaškrtnúť políčko „Sekundárna fáza“ a kliknutím na tlačidlo „Nastaviť…“ otvoriť okno s definíciou údajov ( obr. L1.8., len na demonštračné účely, nevyžaduje sa pre toto laboratórium). Okrem priemernej veľkosti zrna je potrebné definovať štandardnú odchýlku, pomer strán a typ kryštálu spolu s ďalšími údajmi na definovanie sekundárnej fázy, ktoré zahŕňajú objemový podiel sekundárnej fázy, rozdelenie sekundárnej fázy, či je deformovateľná a rekryštalizovateľná. Realizujú sa štyri typy distribúcie sekundárnej fázy: (1) jednotlivé zrná; (2) častice náhodne distribuované; (3) častice distribuované pozdĺž hranice zrna; (4) kontinuálna distribúcia pozdĺž hraníc čiastkových zŕn. Príklady počiatočnej mikroštruktúry pomocou metódy „System generated“ pre jednofázový materiál a dvojfázový materiál sú znázornené na obr. L1.9. (len na demonštračné účely, nevyžaduje sa pre toto laboratórium). Pre dvojfázovú mikroštruktúru s rekryštalizovateľnou sekundárnou fázou musí byť model CA používateľa implementovaný prostredníctvom používateľskej rutiny.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0008.jpg' | relative_url }})

Definícia sekundárnej fázy (len demonštrácia)

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0009.jpg' | relative_url }})

  
(A)

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0010.jpg' | relative_url }})

  
(b)

Príklady počiatočnej mikroštruktúry pomocou metódy „generovanej systémom“: (a) jednofázový materiál; (b) dvojfázový materiál (len demonštrácia)

Pre metódu „import z experimentálnych údajov EBSD“ kliknite na tlačidlo „Nastavenie údajov EBSD“, zobrazí sa okno pre nastavenie údajov EBSD, ako je znázornené na obr. L1.10. (iba na demonštračné účely, nevyžaduje sa pre toto laboratórium). Údaje EBSD by sa mali riadiť špecifikovaným formátom. Každý riadok v hlavičke je označený hviezdičkou „#“. Každý dátový riadok môže mať 9~14 číselných polí. Prvých 9 polí musí byť usporiadaných ako:

Phi1, PHI, Phi2, X, Y, IQ, CI, Phase ID, grain ID, …

Eulerove uhly sú v Bungeovej notácii v radiánoch. Predpokladá sa, že každý údajový riadok je platným bodom skenovania.

Okrem požiadavky na formát údajov musíme špecifikovať typ mriežky (štvorec alebo šesťuholník), počet skenovacích riadkov, počet stĺpcov (alebo počet stĺpcov pre nepárne a párne riadky pre šesťuholníkovú mriežku), veľkosť kroku skenovania, stav ID zrna, počet fáz, typ kryštálu každej fázy a vzťah fázového mapovania medzi údajmi EBSD a modelom CA. Maximálny počet fáz je 5. Ak ID zrna nie je stanovené v údajoch EBSD, kód triedenia bude priradený k ID zrna. Po dokončení nastavenia údajov EBSD kliknite na tlačidlo importu (![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }})) na načítanie údajov EBSD a zobrazenie obrazu mikroštruktúry zrna, ako je znázornené na obr. L1.11. (iba na demonštračné účely, nevyžaduje sa pre toto laboratórium). Keď je oblasť skenovania EBSD väčšia ako veľkosť domény CA, môžeme vybrať požadovanú oblasť v obraze presunutím okna orezania a potom kliknutím na tlačidlo „Orezať“.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0011.jpg' | relative_url }})

Nastavenie údajov EBSD (len ukážka)

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0012.jpg' | relative_url }})

Importovanie údajov EBSD (len ukážka)

  
Po vygenerovaní počiatočnej mikroštruktúry kliknite na položku „**Mechanizmy** “ v strome úloh. V okne definície údajov začiarknite políčko „Ukončuje dynamickú rekryštalizáciu“ pre toto laboratórium (obr. L1.12.). Pre každý mechanizmus je tiež podporovaný model CA používateľa.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0013.jpg' | relative_url }})

Výber mechanizmov

Kliknite na položku „* * Základné ** * * vlastnosti materiálu * * “ v okne údajov ( obr. L1.13.), nastaviť nasledujúce materiálové vlastnosti: Burgers vector (b) = 0.249 nm, modul šmyku (G0) = 38.95 GPa, referenčná teplota (T0) = 1050°C, sklon modulu šmyku oproti teplote (KG) = 0.0782, hraničná energia zrna pre hranicu zrna s vysokým uhlom = 0.424 J/m2. Ostatné vlastnosti materiálu môžu používať predvolené hodnoty.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0014.jpg' | relative_url }})

Základné vlastnosti materiálu

Pre prietokové napätie a hraničnú energiu zrna sú podporované užívateľské rutiny (PODPROGRAM USR_FLOWSTRESS a PODPROGRAM USR_UGBE). Pre model CA používateľa (napr. PODPROGRAM USR_CA_DRX) sú podporované premenné interného stavu definované používateľom pre každú bunku. Premenné interného stavu definované používateľom by sa mali inicializovať na začiatku prvého kroku a aktualizovať každý krok prostredníctvom používateľskej rutiny (PODPROGRAM USR_UISV). Používanie používateľských rutín bude predstavené na konci sekcie.

Ďalšou položkou stromu je „**Dislokácia****hustota počas deformácie** “ a príslušné okno s údajmi je zobrazené na obr. L1.14. Hustota dislokácie je dôležitou premennou vnútorného stavu pre každú bunku v modeli CA-DRX, pretože určuje nukleáciu a rast zrna, ako aj prietokové napätie. Poskytujeme tri modely hustoty dislokácie, t.j. modifikovaný model Yoshie–Lassraoui–Jonas (YLJ-GM), model Goetz-Seetharaman (GS) a model Kocks-Mecking (KM). Podporovaná je aj používateľská rutina pre vývoj hustoty dislokácie (PODPROGRAM USR_DRX_DISDEN). V tomto laboratóriu vyberáme model YLJ-GM a definujeme nasledujúce materiálové parametre: referenčná rýchlosť deformácie = 1/s, h0 = 32,1917 um-2, mh = 0,0066, Qh = 75212,8 J/mol, r0 = 1713,79, mr = 0,221256, Qr = 31721,4 J/mol.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0015.jpg' | relative_url }})

Model hustoty dislokácie počas deformácie

Pretože DRX je jediný mechanizmus, ktorý je potrebné zvážiť pri skúmanom prípade, nemusíme definovať žiadne údaje pre položku „Hustota dislokácie počas tepelného spracovania“.

Ďalej kliknite na položku **Kritická*** * hustota dislokácie * *. Existujú dva typické prístupy na určenie kritickej hustoty dislokácie: kritickým napätím alebo rovnicou Robert-Ahlblom. Podporovaná je aj používateľská rutina (PODPROGRAM USR_CRIDIS). V tomto laboratóriu zvoľte prepínač „Kritickým namáhaním“ a nastavte nasledujúce parametre materiálu: ![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/epsolon_c_0.jpg' | relative_url }}) = 0.000349, mc = 0.157, Qc = 63433 J/mol (pozri obr. L1.15.).

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0016.jpg' | relative_url }})

Kritická hustota dislokácie

Ďalšou položkou stromu, ktorú treba definovať, je „**Nucleation** ** rate * * “ a zodpovedajúce okno definície údajov je zobrazené na obr. L1.16. Existujú dve možnosti výpočtu rýchlosti nukleácie: zovšeobecnený model alebo rutina používateľa (PODPROGRAM USR_DRX_NUCRAT ). V tomto laboratóriu vyberieme prepínač „Zovšeobecnený model“ a zadáme parametre materiálu nasledovne: cn = 13,18, mn = 1, Qn= 52793,1 J/mol.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0017.jpg' | relative_url }})

Rýchlosť nukleácie

Posledná položka stromu, ktorá sa má definovať, je „* * Zrno *** *rast** “, ako je znázornené na obr. L1.17. Na výpočet migračnej rýchlosti hranice zŕn sa implementuje zovšeobecnený model použiteľný pre rekryštalizáciu aj statický rast zŕn. Hnacou silou rastu zrna (![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/delta_p.jpg' | relative_url }})) sú štyri termíny (PD, PC , PZ a PS). P D je hnacou silou prispievajúcou k rozdielu hustoty dislokácie medzi dvoma susednými zrnami, ktoré zohrávajú dominantnú úlohu pri rekryštalizácii (DRX, MRX a SRX). PC je hnacou silou znižovania energie hranice zŕn, ktorá zohráva dominantnú úlohu pri statickom raste zŕn (PD = 0). ![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/aplha_k.jpg' | relative_url }}) je korekčný faktor na zakrivenie hranice zrna, ktorý sa kalibruje pomocou statických údajov o raste zrna. PZ považuje Zenerov pripínací efekt a PS za efekt rozpusteného ťahu. Podporovaná je aj užívateľská rutina pre rast obilia (PODPROGRAM USR_LOC_VEL). V tomto laboratóriu vyberieme prepínač „Zovšeobecnený model“ a nastavíme ![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/delta_d_0.jpg' | relative_url }}) = 1,15954e-6 m3/s, Qm = 330008 J/mol, ![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/aplha_k.jpg' | relative_url }}) = 0,0048, A = 0, z1 = 0,0. Ostatné parametre materiálu používajú predvolené hodnoty.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0018.jpg' | relative_url }})

Rýchlosť rastu zrna

  
Treba spomenúť, že ak sú používateľské rutiny alebo modely CA definované z GUI, musia byť implementované v programe CA_user_routines.f, ktorý sa nachádza v inštalačnom priečinku\DEFORM\ UserRoutine\CA_Model. Nachádza sa tu aj potrebný knižničný súbor a stavebný nástroj. Nástroje Absoft na vytvorenie DEF_CA.EXE s používateľskými rutinami sú znázornené na obr. L1.18.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0019.jpg' | relative_url }})

Vytvorte súbor DEF_CA.EXE pomocou používateľských rutín

## Spustiť simuláciu CA

Kliknite na položku „* * Spustiť * * “ v strome úloh a v okne údajov kliknite na tlačidlo „** Vypočítať * *“ (pozri obr. L1.19.). V pracovnom adresári sa vytvorí priečinok s názvom „CA Model“ a pod ním sa vytvorí priečinok pre každý vybraný bod s názvom „Bod*“ (* označuje číslo bodu) na uloženie výsledkov simulácie.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0020.jpg' | relative_url }})

Spustiť simuláciu CA

vzoru.

Po dokončení simulácie sú všetky vybrané body uvedené v položke „**Výstup** “ v strome úloh. Zadajte číslo kroku v prehliadači krokov a vyberte bod, výsledky simulácie je možné skontrolovať, ako je znázornené na obr. L1.20. Kliknutím na rôzne možnosti zobrazenia je možné zobraziť rôzne aspekty mikroštruktúry vrátane morfológie zŕn (reprezentovanej id zŕn), hraníc zŕn, ako aj hustoty dislokácie. Okrem toho sa zobrazujú aj štatistické informácie zo simulovanej mikroštruktúry, vrátane histogramov veľkosti zrna, dezorientačného uhla a pomerov strán zrna. Zobrazia sa aj hodnoty min, max, priemer a štandardná odchýlka. Môžu sa zobraziť aj krivky, ako je zmena prietokového napätia, priemerná hustota dislokácie, priemerná veľkosť zrna, podiel rekryštalizačného objemu s deformáciou alebo časom.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0021.jpg' | relative_url }})

Výstup simulácie CA

Ikony ovládania animácie prehrávajú databázu a zobrazujú vývoj mikroštruktúry pre každý časový krok. Obr. L1.21. demonštruje vývoj mikroštruktúry v rôznych časových krokoch. Obr. L1.22. porovnáva výsledky simulácie CA s experimentálnymi údajmi [7-8]. Je zrejmé, že výsledky simulácie CA dobre súhlasia s experimentálnymi údajmi.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0022.jpg' | relative_url }})

Vývoj mikroštruktúry so simulačným krokom

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0023.jpg' | relative_url }})

(a)

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0024.jpg' | relative_url }})

(b)

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal1_image0025.jpg' | relative_url }})

(c)

Porovnanie výsledkov simulácie CA s experimentálnymi údajmi [7-8]: (a) prietokové napätie; (b) priemerná veľkosť zrna; (c) objemová frakcia DRX

Laboratórium 2: CA model pre statický rast zŕn

## Spustiť model CA v balíku materiálov

Ak chcete spustiť model CA v balíku materiálov, pozrite si časť 1.1.
  
Ako už bolo spomenuté, na vykonanie simulácie CA v súbore materiálov požadujeme nominálnu DB. Pre toto laboratórium použijeme priečinok * *HT_IN718_Nominal.key** z**\MANUALS\PDF \DEFORM_CA_Lab** na vygenerovanie nominálnej DB. Operácia je izotermické tepelné ošetrenie predvalku IN718 pri teplote 1050 °C počas 70 minút. Otvorte NG Pre pomocou prepojenia DEFORMOVAŤ Hlavné GUI a definujte ID problému ako "HT_IN718", vyberte "2D" Rozmer prepínač a "System International (SI)" jednotka Systém prepínač v okne Nový problém, potom importujte HT_IN718_Nominal.key z priečinka\MANUALS\PDF \DEFORM_CA_Lab. Prejdite na stránku Generovať databázu a kliknite na " Generovať databázu ", aby ste vytvorili databázu. Prepnite na kartu "Simulácia" a spustite simuláciu, uistite sa, že simulácia sa zastaví normálne bez akéhokoľvek problému. Teraz z hlavného grafického rozhrania kliknite na Material Suite v časti „Post Processor“ a otvorte modul Material Suite. Používateľ môže tiež dvakrát kliknúť na "DEF_GUI_MAT.exe" v inštalačnom adresári DEFORMAČNÉHO softvéru a spustiť sadu materiálov.
  
Po zobrazení hlavného okna pre sadu materiálov kliknite na ikonu "Otvoriť..." ( ![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}) ) v hornom paneli nástrojov a importujte vzorovú databázu (HT_IN718.DB). Do stromu úloh SA pridá predvolená položka úlohy „** deformácia * *“. Rozbaľte položku „Mikroštruktúra“ a kliknite na ikonu „Model zrna CA“, do stromu úloh sa pridá nová položka úlohy „Model CA“, ako je znázornené na obr. L2.1.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0001.jpg' | relative_url }})

Spustiť model CA v balíku materiálov

## Zadajte rozsah krokov, výber objektu a výber bodu

Pozri časť 1.2. Pre položku „* * Zadajte rozsah * * “ vyberte „Všetky kroky“; pre položku „Výber objektu“ vyberte „Obrobok“; pre „Výber bodu“ vyberte krok -1 a vyberte bod v centrálnej oblasti obrobku, napríklad bod (5.06, 5.36, 0, 1), pozri obr. L2.2.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0002.jpg' | relative_url }})

Výber bodu

## Nastavenie modelu CA

Pozri časť 4.3.

Na stránke „**Konfigurácia** “ sa uistite, že pracovný adresár je tam, kde sa nachádza nominálna databáza, ako je znázornené na obr. L2.3.

  
![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0003.jpg' | relative_url }})

Stránka konfigurácie

  
Na stránke „**I***** * n * * itial input**“ nastavte nasledujúcu veľkosť modelu CA: riadky = 300 a stĺpce = 300. Nastavte dĺžku bunkovej jednotky na 1 mikrón a vyberte "Moore (9 buniek)" pre okolie, ako je znázornené na obr. L2.4.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0004.jpg' | relative_url }})

Počiatočný vstup

Na stránke **Initial option** vyberte metódu **System generated* *. Nastavte priemernú veľkosť zrna na 10,46 mikrónov, štandardnú odchýlku na 2 mikróny, pomer strán na 1 a typ kryštálu na „FCC“. Kliknite na tlačidlo „Generovať“, vygeneruje sa počiatočná mikroštruktúra pre model CA a v okne displeja sa zobrazia obrázky morfológie a hranice zŕn, ako je znázornené na obr. L2.5.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0005.jpg' | relative_url }})

Počiatočná možnosť

Na stránke „**Mechanizmy** “ začiarknite políčko „**Statický rast zrna (SGG)** “, ako je znázornené na obr. L2.6.

Môžeme tiež skontrolovať ďalšie začiarkavacie políčka, ako sú DRX, MRX a SRX. Na základe historických dát termomechanického spracovania sledovaného bodu dokáže CA model automaticky určiť, ktorý mechanizmus bude aktivovaný pre každý simulačný krok. Pre skúmaný prípad, pretože nedochádza k deformácii, ostatné mechanizmy nebudú aktivované, aj keď sú zaškrtnuté ich políčka.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0006.jpg' | relative_url }})

Mechanizmy

Pre zostávajúce vstupné položky z položky „**Základné vlastnosti materiálu ** “ do položky „** Rast zrna ** “ sú vstupné údaje rovnaké ako tie, ktoré sú opísané v časti 1.3, obr. L1.13. až obr. L1.17.

## Spustiť simuláciu CA

Postup je rovnaký ako je popísaný v časti 1.4.

vzoru.

Výstupná strana pre vybraný bod v poslednom kroku je zobrazená na obr. L2.7. Vidíme, že priemerná veľkosť zrna sa časom zvyšuje. Obr. L2.8. demonštruje vývoj mikroštruktúry v rôznych časových krokoch. Na obr. L2.9. je znázornené porovnanie predpokladanej priemernej veľkosti zrna CA modelu s experimentálnymi údajmi [7,9]. Výsledky simulácie CA dobre súhlasia s experimentálnymi údajmi.

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0007.jpg' | relative_url }})

Výstup simulácie CA

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0008.jpg' | relative_url }})

Vývoj mikroštruktúry so simulačným krokom

![]({{ '/assets/images/labs/material_suite_labs/material_suite_labs_for_ca_model/cal2_image0009.jpg' | relative_url }})

Porovnanie výsledkov simulácie CA s experimentálnymi údajmi [7,9]

  
Odkazy

[1] Humphreys F. J., Hatherly M. Recrystallization and related annealing phenomena. Druhé vydanie. Elsevier Ltd, Oxford, Veľká Británia, 2004.
[2] Rollett A. D., 1997. Prehľad modelovania a simulácie rekryštalizácie. Progress in Materials Science , zv. 42, s. 79 - 99.
[3] Ding R., Guo Z., 2002. Mikroštrukturálne modelovanie dynamickej rekryštalizácie pomocou rozšíreného prístupu bunkového automatu. Computational Materials Science, Vol 23 (1), s. 209 - 218.
[4] Montheillet F., Jonas J.J., 2009. Modely rekryštalizácie. ASM Handbook, zväzok 22A: Základy modelovania pre spracovanie kovov. D.U. Furrer and S.L. Semiatin, editors, s. 220-231.
[5] Hallberg H., 2011. Prístupy k modelovaniu rekryštalizácie. Kovy, Vol 1, s. 16-48.
[6] Chen F., Cui Z., Chen J., 2014. Predikcia vývoja mikroštruktúry počas kovania za tepla. Manufacturing Rev., roč. 1, s. 6.
[7] Tang X., Wang, B., Zhang N., Huo Y., Zhou J., 2015. Modelovanie mikroštruktúrneho vývoja a tokového správania superzliatiny IN718 pomocou fyzikálne založených vnútorných stavových premenných . Rare Met., doi 10.1007/s12598-015-0602-6).
[8] Zhang J.M., Gao Z.Y., Zhong J.Y.,Zhong Z.Y., 1999. Matematické modelovanie správania horúcej deformácie superzliatiny IN718. Metall Mater Trans A. Vol 30 (10), s. 2701-2712.
[9] Chen L.Q., Sui F.L., Liu X.H., 2009. Model rastu zrna zliatiny kovanej dosky Inconel 718 v procese ohrevu pred tvrdým valcovaním. Acta Metall Sin., Vol 45 (10), s. 1242-1248.
