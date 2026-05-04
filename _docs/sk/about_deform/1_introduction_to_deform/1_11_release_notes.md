---
lang: sk
title: "1.11. Poznámky k vydaniu"
---

# 1.11. Poznámky k verzii - v14.0.2

![]({{ '/assets/images/about_deform/1_11_release_notes/deform.gif' | relative_url }})

**DEFORM****®****v14.0 SP2 (PC a Linux) **

**Poznámky k vydaniu**

****20. decembra**********,** 2024** **

_**Poďakovanie**_

Preklad pre medzinárodnú verziu vykonali:

  1. Yamanaka Engineering Co., Ltd. (japonská verzia)
  2. TESIS Corp. (ruská verzia)
  3. Laboratórium riešení (kórejská verzia)
  4. Consultores CPM (španielska verzia)
  5. PERA GLOBAL (čínska (zjednodušená) verzia)
  6. ECOTRE (talianska verzia)

![]({{ '/assets/images/about_deform/1_11_release_notes/sftc_with_address.jpg' | relative_url }})

Poznámky k verzii DEFORM v14.0.2 (v14.0 SP2)

Najdôležitejšie nové a vylepšené funkcie vo verzii V14.0 SP2

Vybrané novinky v DEFORM V14.0 SP2

V verzii 14.0 SP1 boli vyriešené tieto dôležité problémy

Najdôležitejšie nové a vylepšené funkcie vo verzii 14.0

Vybrané novinky v DEFORM v14.0

Dôležité vylepšenia grafického rozhrania a funkcií v DEFORM v14.0

Dôležité zmeny/vylepšenia MKP v DEFORM v14.0

Dôležité opravy chýb súvisiacich s MKP v DEFORM v14.0

Dôležité vylepšenia AMG v DEFORM v14.0

Dôležité opravy chýb súvisiacich s AMG v DEFORM v14.0

Aktualizácia knižnice materiálov v DEFORM v14.0

Zoznam aktualizácií dokumentov v DEFORM v14.0 SP2

Zoznam aktualizácií dokumentov v DEFORM v14.0

Zoznam nových a rozšírených kľúčových slov v DEFORM v14.0 a V14.0 SP2

Komentáre a otázky

_**Poznámky k vydaniu DEFORM v14.0.2 (v14.0 SP2)**_

SFTC poskytuje aktuálne poznámky k vydaniu systému DEFORM v14.0 SP2. Tento článok obsahuje informácie o posledných dôležitých zmenách, opravách chýb a aktualizáciách existujúcich funkcií.

DEFORM V14.0 SP2 podporuje operačné systémy Windows aj Linux. Medzi podporované distribúcie Linuxu patria CentOS 6, CentOS 7 a RHEL 8.

  * **DEFORM V14.0 SP2 Vylepšenia** : DEFORM V14.0 SP2 zavádza vylepšenia systému na základe požiadaviek zákazníkov a rieši opravy chýb zistené na základe spätnej väzby k verziám V14.0 a V14.0 SP1.

  * Balík **DEFORM V14.0 SP2** : Balík DEFORM V14.0 SP2 obsahuje License Manager (LM) V14.0 SP2 a DEFORM Service Control (SC) V14.0 SP2.

  * **DEFORM V14.0 Požiadavka na heslo:** Táto verzia programu DEFORM vyžaduje na prevádzku heslo V14.0. DEFORM V14.0 SP2 nebude fungovať s heslom DEFORM V13.1. Pre získanie súboru s heslom V14.0 kontaktujte SFTC.

  * **Aktualizácia na DEFORM V14.0 SP2** : Ak v súčasnosti používate DEFORM V14.0 SP1 (alebo akúkoľvek staršiu verziu, napríklad V14.0 alebo V13.1 SP1) a aktualizujete na V14.0 SP2, nemusíte odinštalovať predchádzajúce verzie DEFORM. Je však povinné odinštalovať predchádzajúcu verziu Správcu licencií a nainštalovať Správcu licencií V14.0 SP2.

_**Kľúčové prvky nových a vylepšených funkcií vo verzii V14.0 SP2**_

  
Na jesennom stretnutí skupiny používateľov DEFORM 2024 boli predstavené hlavné prvky systému DEFORM V14.0 SP2. Podrobný opis nájdete v materiáloch z tohto podujatia.

  * **Model ALE Linear Friction Welding (LFW)**, predstavený na jesennom stretnutí skupiny používateľov DEFORM 2024, bol oficiálne uvedený vo verzii V14.0 SP2. Tento model výrazne znižuje výpočtové náklady pri 3D simuláciách lineárneho trecieho zvárania ALE.

  * **Vylepšenia na prepichnutie trubice** : Pridané nové primitívum geometrie obuvi, funkcia zastavovacej roviny a podpora riadenia pohybu pre tŕň a obuv.

  * **Vylepšenia v súvislosti so zachádzaním** : Pridaná podpora pre import a export údajov tabuľky priechodov vo formáte CSV.

  * **Vylepšenia meracích nástrojov** : Pridané funkcie pre pohyblivé a upraviteľné štítky, ako aj možnosti úpravy alebo odstránenia meraní prostredníctvom kontextového menu.

  * **Zvýšená viditeľnosť** : Vylepšená funkcia zobrazovania rozmerov vo funkcii "Zobraziť rozmery".

  * **Vylepšenia zobrazenia pod výplňou** : Vylepšené zobrazenie pre simuláciu lapača oleja/plynu.

  * **Vylepšenie generovania správ** : Pridaná nová možnosť exportu pre tok kovov.

  * **Vylepšenie zobrazenia farebného pruhu** :**** Optimalizovaná predvolená veľkosť písma pre lepšiu čitateľnosť na monitoroch s vysokým rozlíšením. Vylepšená aj kontextová ponuka farebného pruhu pre jednoduchšie nastavenie názvu, veľkosti písma a farby.

  * **Podpora 3D objektov DEFORM v aplikácii MS PowerPoint** : Vyvinutá funkcia exportu pre 3D modely (geometria, sieť, SV). Objekty DEFORM je teraz možné importovať do aplikácie PowerPoint 365 alebo PowerPoint 2024.

  * **Sumárny graf záťaže v postprocesore** : Do okna Grafu (Load-Stroke) bola pridaná nová možnosť "Plot Type", ktorá umožňuje vykresliť súčet vybraných objektov.

  * **Načítanie - ťah Superimpose Plot v postprocesore** : Bol zavedený nástroj Superimpose na porovnávanie rôznych databáz. Pri použití s grafom Summation Plot (Súčet) v nástroji Load-Stroke (ťah zaťaženia) umožňuje vykresliť grafy viacerých projektov na tom istom grafe.

  * **Vylepšenie výstupu rovníc** : Vylepšené prostredníctvom viacerých opráv chýb.

  * **Prispôsobenie ponuky Štart systému Windows pre skratky DEFORM** : Do nastavenia DEFORM bola pridaná nová karta "Ponuka Štart", ktorá umožňuje používateľom vybrať, ktoré aplikácie sa zobrazia v ponuke Štart.

  * **Výstraha o uplynutí platnosti licencie** : V DEFORM Setup, DEFORM License Monitor a GUI Main sú teraz k dispozícii varovné informácie o blížiacom sa konci platnosti licencie.

  * **DEFORM Lokalizácia inštalačného programu** : Od verzie V14 SP2 je inštalačný program plne preložiteľný a zvolený jazyk sa prenesie na použitie v programe DEFORM.

  * **Viacnásobný hydraulický lis** : Do modelovania hydraulických lisov s viacerými baranmi bola pridaná možnosť min. rýchlosti zastavenia.

  * **Aktualizácia API DEFORM** : API teraz podporuje ukladanie viacerých formátov geometrie z posledného kroku databázy pomocou súboru "Save multiple geometry formats for last step.py".

  * **Beta verzia programu na vytváranie sietí V14.1 (AMG)** : Beta verzia programu na sieťovanie V14.1 (AMG) slúži ako záložný sieťovač vo vydaní V14.0 SP2. Záložný mesher 3D vylepšuje riadenie váhovania krivosti siete povrchu, čo vedie k zlepšeniu rozlíšenia jemnej siete okolo okrajov povrchu a filetov.

  * **Optimalizujte výkon DEF_SIM_64.EXE** (simulačný motor FEM) na **Intel 12. generácii** **a novších procesoroch** : Vytvorte súbor s názvom **D******EF_** PRIORITY.DAT** v priečinku s problémami. V prvom riadku súboru zadajte požadovanú úroveň priority: zadajte "**1** " pre **Above Normal** (Nad normálom**) alebo "**2** " pre **High** (Vysoká**). Táto úprava zvyšuje výkon simulácie na procesoroch Intel 12. generácie a novších s hybridnou architektúrou tým, že zabezpečuje, aby sa DEF_SIM_64.EXE pridelil výkonným jadrám na dosiahnutie optimálneho výkonu.

__Vylepšenia špecifické pre platformu Linux__

  * Zabezpečenie podpory záložného sieťovania počas paralelného remeshingu v systéme Linux.

  * Stabilita programu a procedúr na vytváranie sietí sa zlepšila v systéme Linux.

  * Opravená chyba v sledovaní prietokovej čiary pri viacpriechodovom valcovaní tvaru v systéme Linux.

  * Preview/Open Editor teraz podporuje súbory s malými písmenami ".log" alebo ".msg" v GUI Main na Linuxe.

_**Vybrané novinky v DEFORM V14.0 SP2**_

Niektoré z hlavných noviniek systému DEFORM V14.0 SP2 boli predstavené na **jesennom stretnutí skupiny používateľov DEFORM 2024**. Medzi vybrané vylepšenia verzie V14.0 SP2 patria:

  * Bol vyvinutý a zavedený model **Lineárneho zvárania trením (LFW)**.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image021.jpg' | relative_url }})

V dialógovom okne Simulation Controls (Ovládacie prvky simulácie) bol pridaný nový typ simulácie ALE lineárne zváranie trením.

  * **Graf priebehu zaťaženia v POST** teraz obsahuje nové možnosti typu grafu, ktoré umožňujú používateľom vykresliť súčet síl v grafe.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image022.jpg' | relative_url }})

  
Nové možnosti typov plôch "Iba individuálne plôšky", "Iba sumárna plôška" a "Sumárna a individuálna plôška".

  * **Vylepšenia piercingu v rúrke** : Pridané nové geometrické primitívum pre objekt topánky, podpora roviny zastavenia, ovládanie pohybu pre tŕň a topánky.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image023.jpg' | relative_url }})

  
Nový geometrický primitív (Extrude, Revolve) pre objekt topánky v nastavení prepichovania rúrky.

  * **Viacramenný hydraulický lis:** Pridané nové kritérium zastavenia s minimálnou rýchlosťou, pridaná možnosť "Minimálna rýchlosť zastavenia".

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image025.jpg' | relative_url }})

  
Nová možnosť "Min. rýchlosť zastavenia" pri viacramennom lisovaní v Simulation Controls.

  * **Vylepšené zobrazenie pod výplňou** : Keď sa prostredníctvom súboru DEF_GAS.DAT aktivuje lapač plynov, oblasť podplnenia sa zväčší vďaka lapačom plynov pri kovaní v uzavretej zápustke. Na zlepšenie zobrazenia podplnenia bola zavedená nová definícia farby pre oblasť podplnenia zachyteného plynom. Predvolená farba pre oblasť so zachyteným plynom je nebesky modrá.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image026.jpg' | relative_url }})

  
V dialógovom okne Predvoľby je pridaná oblasť záchytného plynového zariadenia (UNDERFILL_GAS_TRAP_REGION).

  * **Nová funkcia exportu dát 3D objektov/modelov** do programu MS PowerPoint: Bola vyvinutá nová funkcia exportu údajov 3D objektov/modelov do programu MS PowerPoint (365 alebo 2024), ktorá je k dispozícii v ponuke Súbor.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image027.jpg' | relative_url }})  
Nové možnosti exportu "Polygón (.ply)" a "Prenosový formát grafickej knižnice (.glb)" v type exportného súboru

  * **Upozornenie na vypršanie platnosti licencie** : V dialógových oknách DEFORM License Monitor a DEFORM Setup bolo implementované upozornenie na vypršanie platnosti licencie. V GUI Main V14 SP2 sa pri spustení zobrazí upozornenie, keď je nastavené, že platnosť licencie vyprší za menej ako štyri týždne.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image028.jpg' | relative_url }})

Správa o licencii DEFORM z GUI Main

  
![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image029.jpg' | relative_url }})

Upozornenie na vypršanie platnosti licencie v DEFORM License monitor (vľavo) a v DEFORM Setup (vpravo).

  * **Karta Štart menu v programe DEFORM Setup:** V programe DEFORM V14 SP2 bola do programu DEFORM Setup pridaná karta Štart menu. Používatelia teraz môžu pridať alebo odstrániť zástupcov DEFORM z ponuky Štart systému Windows a vybrať, ktoré aplikácie sa zobrazia.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image030.jpg' | relative_url }})

Výber alebo zrušenie výberu aplikácií v programe DEFORM Setup.

  * **DEFORM lokalizácia inštalačného programu**. Inštalačný program V14 SP2 je plne preložiteľný našimi distribútormi a zvolený jazyk sa prenesie na použitie v systéme DEFORM.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image031.jpg' | relative_url }})

Výber jazyka počas inštalácie v inštalačnom programe DEFORM (zobrazené s japončinou).

_**V verzii 14.0 SP1 sú vyriešené tieto dôležité problémy:**_

  * Vyriešený **kritický problém spätnej kompatibility** hlásený vo verzii 14.0, kde typ objektu "Čítanie z DB", ak sa použije v následnej operácii v rámci nastavenia viacerých operácií (MO), môže za určitých podmienok v prostredí MO (nastavenie modelu integrovaného výrobného procesu) spôsobiť chybu. _Je potrebné okamžite aktualizovať na verziu 14.0 SP1, aby ste sa vyhli tomuto možnému problému so spätnou kompatibilitou._

  * Vyriešený **problém vo verzii 14.0 súvisiaci s obnovou/aktualizáciou stromu objektov**, ktorý sa vyskytoval pri prepínaní medzi rôznymi typmi objektov.

  * Vyriešený **problém vo verzii 14.0 týkajúci sa podpory neanglických znakov**. Keď v nastaveniach operačného systému Windows nebol povolený štandard kódovania znakov UTF-8 (Unicode Transformation Format - 8-bit), pri spracovaní názvov priečinkov a súborov obsahujúcich neanglické znaky sa v systéme DEFORM v14.0 vyskytli problémy.

  * Spolu s vyššie uvedenou opravou sme **výrazne zlepšili podporu neanglických znakov** v rôznych oblastiach vrátane názvov projektov, názvov objektov, názvov simulácií, názvov operácií a ďalších.

  * Vyriešený problém, keď sa názov objektu zmenil na "Objekt 1" z "Obrobok", keď sa typ objektu zmenil z "Čítať z DB" na "Plast" v druhej operácii.

  * Vyriešený problém, keď funkcia "**Kopírovať vlastnosti materiálu** " nedokázala skopírovať určité elektrické/magnetické vlastnosti materiálu do iného materiálu.

  * Aktualizáciou na najnovšiu verziu balíka **MiKTeX** bol odstránený problém, pri ktorom zlyhávalo generovanie správ vo formáte PDF, keď bol DEFORM spustený v japonskom jazykovom režime.

  * Vyriešený problém s pádom, ku ktorému dochádzalo pri používaní funkcie **Zrkadlové zlúčenie**.

  * Vyriešený problém, pri ktorom sa stratila **referenčná teplota** pre typ objektu Environment Fluid (CFD).

  * Systém DEFORM v14.0 SP1 obsahuje projektový súbor Microsoft Visual Studio 2019 (**DEF_SIM_64_USR_Intel.vfproj**) na kompiláciu používateľských rutín FEM pomocou kompilátora Intel Fortran.

  * Intel® Fortran Compiler Classic (ifort) je už zastaraný a jeho používanie bude ukončené v októbri 2024. Spoločnosť Intel odporúča zákazníkom, aby pre pokračujúcu podporu v systémoch Windows a Linux prešli na **Intel® Fortran Compiler (ifx)**.

  * DEFORM v14.0 SP1 obsahuje dva nové dávkové súbory: "**build-FEM-USR-PC-64bit-intel-compiler-ifx.bat** " a "**Intel_ifx_build_all_dll_command** " pre 2D aj 3D.

  * **Ceníme si spätnú väzbu** od používateľov verzie 14.0, ktorá nám pomohla vyriešiť tieto problémy

**_Highlights of New and Enhanced Features in v14.0_**

_Väčšina hlavných bodov systému DEFORM v14.0 SP2 bola predstavená na stretnutí skupiny používateľov DEFORM na jar 2024 a na stretnutí skupiny používateľov DEFORM na jeseň 2023._

  * **Čiastočný doménový riešiteľ**, ktorý bol predstavený na stretnutí skupiny používateľov DEFORM na jar 2023, bol otestovaný/overený a teraz je oficiálne k dispozícii vo verzii 14.0/v14.0 SP1. Pomôže r**edukovať výpočtové** náklady pri simuláciách prírastkových/rotačných procesov tvárnenia, ako je napríklad odstreďovanie, prietokové tvárnenie a orbitálne tvárnenie.

  * **CFD riešiteľ** je k dispozícii s grafickým používateľským rozhraním pre simuláciu **hasenia plynu** vo verzii 14.0/v14.0 SP1. Simulácia prúdenia CFD môže generovať profil koeficientu prestupu tepla (HTC) a potom sa môže vykonať simulácia kalenia/deformácie pomocou vypočítaného HTC. Dokument 3D Lab pre kalenie plynom je k dispozícii v oficiálnom vydaní verzie v14.0.

  * **Model indukčného ohrevu** teraz dokáže modelovať B-H krivku a hysteréznu stratu. Boli pridané nové stavové premenné (intenzita magnetického poľa H, hustota magnetického toku, B), ktoré lepšie prezentujú výsledky simulácie indukčného ohrevu.

  * Boli pridané nové konštitutívne modely **Elasto-plastický pórovitý** model, **Všeobecný Neo-Hookeanov** model (hyperelastický).

  * Boli zavedené nové kritériá výťažnosti **Barlat Anisotropy 1991**.

  * Bol zavedený nový model spevnenia **Yoshida Uemori**.

  * **Vylepšenie hydraulického pohybu lisu.** Model pohybu lisu s viacerými baranmi bol novo vyvinutý a zavedený.

  * **3. rotácia pohybu **možnosť je pridaná v 3D.

  * **Vylepšenie modelu valcovania krúžkov**. Teraz môže podporovať umiestnenie priemeru krúžku zvoleného používateľom na zastavenie a použitie kontroly pohybu. Bola pridaná možnosť pokročilého riadenia pohybu, ako napríklad PID regulácia.

  * **Vylepšenie modelu valcovania tvaru**. Teraz môže podporovať Tet mesh (s možnosťami Boolean a Force remesh). Boli implementované rôzne požiadavky používateľov na vylepšenie pre jednoduchšie nastavenie viacprechodového procesu valcovania tvaru.

  * **2D adaptívny kontakt bcc** bol vyvinutý v 2D FEM. Môže byť užitočná pri simulácii kovania s viacerými deformujúcimi sa zápustkami.

  * Bola vyvinutá dynamická rekryštalizácia** hliníkových zliatin založená na mechanizme.

  * Bol vyvinutý **model precipitačného tvrdnutia** (založený na klasických teóriách nukleácie a rastu).

  * Bola vyvinutá **Plastickosť kryštálov pre model textúry**.

  * Na jednoduchšie spracovanie mnohých medziobjektových vzťahov bol vyvinutý nástroj **Examine Tool** pre medziobjektové vzťahy a **Explode view**.

  * **Termický (bezkontaktný) kontakt** bol zavedený na presné predpovedanie teploty v aplikáciách tvárnenia plechov pomocou tepelného výpočtu.

  * V nástroji **Process Monitor, DEFORM Setup, License Monitoring** bolo vykonaných mnoho nových užívateľsky prívetivých vylepšení.

_**Vybrané novinky v DEFORM v14.0**_

Niektoré z hlavných bodov systému DEFORM v14.0 boli predstavené na **jesennom stretnutí skupiny používateľov DEFORM** v roku 2023 a na S**jarnom stretnutí skupiny používateľov DEFORM v roku 2024**. Medzi vybrané vylepšenia verzie v14.0 patria:

  * **Model hydraulického lisu s viacerými ramenami** bol vyvinutý s cieľom podporovať rôzne plány pohybu razníka.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image001.jpg' | relative_url }})

Rozhranie hydraulického lisu s viacerými ramenami na stránkach Simulation control and Movement.

  * **Indukčný ohrev** teraz dokáže modelovať **Krivku B-H** , vzťah medzi intenzitou magnetického poľa (H) a hustotou magnetického toku (B), a **hysterézu** **straty** s podporou zobrazovania nových stavových premenných (intenzita magnetického poľa H, hustota magnetického toku, B).

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image002.jpg' | relative_url }})  
  
Možnosti "Definovať BH krivku" a "Definovať hysteréznu stratu" na stránke Materiál (vľavo), Intenzita elektrického poľa, Hustota prúdu, Intenzita magnetického poľa a Intenzita magnetického toku na stránke SV v Postprocesore (vpravo).

  * **Vylepšenie modelu odvaľovania krúžkov.** Implementované je umiestnenie krúžkov (vnútorných alebo vonkajších) zadané používateľom na kontrolu zastavenia. Je implementovaný axiálny valivý pohyb ako funkcia priemeru krúžku. Taktiež je možné definovať pohyb tŕňa ako PID riadenie, rýchlosť rastu prstenca ako funkciu priemeru prstenca.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image003.jpg' | relative_url }})  
  
Možnosti merania priemeru krúžku (vonkajší, vnútorný, poloha) (vľavo) a súvisiace ovládanie zastavenia (uprostred).   
Možnosť merania priemeru krúžku na stránke kritérií zastavenia na stránke Simulation Controls pre typ simulácie valcovania krúžku (vpravo).

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image004.jpg' | relative_url }})

  
PID regulácia, rastúca rýchlosť prstenca ako funkcia priemeru prstenca, pre pohyb tŕňa (vľavo) a Z-obvodový pohyb axiálneho valca ako funkcia priemeru prstenca (vpravo).

  * **Vykonalo sa viacero vylepšení** v **Valcovaní tvaru** s cieľom poskytnúť zjednodušené nastavenie procesu valcovania s viacerými priechodmi pohodlnejším spôsobom. Používateľ si môže zvoliť počiatočný počet priechodov 2,5D viacpriechodovej simulácie valcovania a nastavenie prostredia je možné prispôsobiť pre každý priechod. Pre Lagrangeovo valcovanie je teraz podporovaná sieť Tet a je možné importovať objekt obrobku.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image005.jpg' | relative_url }})

  
Stránka procesu s predvolenými nastaveniami kontaktov a predvolenými nastaveniami prostredia.  

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image006.jpg' | relative_url }})

  
Tabuľka priechodov zobrazená pre Lagrangeovo valcovanie (vľavo) a pre ALE valcovanie (vpravo).

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image007.jpg' | relative_url }})

  
Nastavenia prostredia pre vybraný priechod (prístupné priamo z tabuľky priechodov).  

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image008.jpg' | relative_url }})

  
Stránka 3D nastavenia v programe ALE (vľavo) a stránka 3D Roll mesh pre neizotermické valenie (vpravo).  

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image009.jpg' | relative_url }})

  
3D stránka siete obrobku pre Lagrangeovo valcovanie (vľavo) a ALE valcovanie (vpravo)

  * **CFD riešiteľ** bol vyvinutý na simuláciu prúdenia kvapalín a jeho integrácia do grafického rozhrania systému DEFORM teraz umožňuje simuláciu **hasenia plynu**. Simulácia prúdenia CFD môže generovať profil koeficientu prestupu tepla (HTC) a potom sa môže vykonať simulácia kalenia/deformácie pomocou vypočítaného HTC.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image010.jpg' | relative_url }})

  
Nová možnosť riešenia prúdenia CFD a kontrola frekvencie v dialógovom okne Simulation Controls.

  * **Riešiteľ s čiastočnou doménou** bol vyvinutý pre inkrementálne rotačné tvárnenie, ako je pradenie, prietokové tvárnenie a orbitálne tvárnenie, s cieľom znížiť výpočtové náklady.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image011.jpg' | relative_url }})

  
Riešiteľ čiastkovej domény s voliteľným rýchlym vyhodnotením (vľavo, stránka Simulation Controls) s funkciou Preview čiastkovej domény a oknom Inactive domain (vpravo, stránka Property).

  * **Tu sú ďalšie vybrané vylepšenia dostupné v Pre-procesore.**

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image012.jpg' | relative_url }})

  
Prepracovaná stránka objektu s dostupnými typmi objektov a typmi prvkov (vľavo) a sekundárnym ovládacím prvkom na stránke Simulation controls (vpravo).

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image013.jpg' | relative_url }})

  
Mapa spracovania, EP pórovitý, Barlat Yield 1991 model výťažnosti, Yoshida-Uemori model tvrdnutia v dialógovom okne Materiál (vľavo) a výpočet nestability pre mapu spracovania na stránke Vlastnosti (vpravo).

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image014.jpg' | relative_url }})

  
Model rekryštalizácie založený na mechanizme (modelovanie zrna, CDRX) (vľavo) a Poissonov pomer a tepelná rozťažnosť ako funkcia teploty a hustoty (vpravo) a všeobecný Neo-Hookeov model hyperelasticity (vpravo) na stránke Materiál.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image015.jpg' | relative_url }})

  
Nová stránka na ovládanie výstupu (vľavo) a možnosti výstupu tepla z uzlov (deformácia, trenie) (vpravo).

  * **DEFORM License Monitor** teraz zobrazuje "Product licensed", "Solver licensed" a "Solvers in use".

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image016.jpg' | relative_url }})

**DEFORM Process Monitor** obsahuje užitočné funkcie filtrovania na monitorovanie stavu úloh.

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image017.jpg' | relative_url }})

**DEFORM Setup** teraz zobrazuje číslo verzie pripojeného licenčného servera DEFORM a "Číslo verzie DEFORM", "Licencovaný produkt" a "Licencovaný riešiteľ" v súbore hesiel. Dodáva sa s vylepšenou stránkou simulačného servera. Teraz sa sleduje stav servera GeoCAD.  

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image018.jpg' | relative_url }})

![]({{ '/assets/images/about_deform/1_11_release_notes/fig_1_11_image019.jpg' | relative_url }})

_**Dôležité vylepšenia grafického rozhrania a funkcií v DEFORM v14.0**_

  * **GUI Main**

    * Vylepšená stabilita a výkon

  * **Pre-Processor**

    * **(Simulačné ovládacie prvky)**

      * Riešiteľ čiastočnej domény

      * Kritérium zastavenia maximálneho zaťaženia

      * Sekundárne ovládanie pre krokové šetrenie

      * Kritérium zastavenia priemeru krúžku

    * **(Materiál)**

      * Tvrdnutie hlasu

      * Prietokové napätie =f(deformácia,hustota,teplota)

      * Barlat Yield 1991

      * Vytvrdzovanie Yoshida-Uemori

      * Rekryštalizovaný model založený na mechanizme (zrno)

      * Mapa spracovania

      * Všeobecná Neo-Hookean (Hyper-elasticita)

    * **(Geometria)**

      * Nástroj na spresnenie

      * Konštrukcia odčítaním

    * **(Mesh)**

      * 2D lokálna remesh pre tehlovú sieť

      * Vylepšené správanie grafického rozhrania pre sieťovanie tehál

    * **(hraničná podmienka)**

      * Zmršťovacie spojenie pre montáž skrutiek

      * Symetria bcc pre 2D indukčný ohrev

      * Prietok kvapaliny bcc: vstup/výstup a stena

    * **(Pohyb)**

      * Pohyb viacerých rámov v hydraulickom lise

      * PID regulácia pohybu (krúžkovanie)

      * 3. rotácia (3D)

    * **(Inter-objekt)**

      * Pohľad po výbuchu

      * Preskúmajte nástroj

      * 2D adaptívny kontakt

      * Tepelný kontakt, HTC = f(gab)+f(tlak)

  * **Postprocesor**

    * Vylepšená krivka zaťaženia a zdvihu pre viacnásobnú prevádzku

    * Sledovanie prietokovej línie pre viacprechodové valcovanie ALE

    * Sledovanie prietokovej línie pre model CFD

    * Vylepšené sledovanie bodu pre viacpriechodové valcovanie ALE (s rotáciou obrobku)

    * Krivka zaťaženia a zdvihu, vylepšenia súhrnného grafu (pre valcovanie krúžkov)

    * Uzlové tepelné stavové veličiny: deformačné teplo, trecie teplo

    * Stavové premenné CFD: vypočítaný koeficient prestupu tepla, vypočítaný tepelný tok

    * Stavové premenné indukčného ohrevu: Intenzita elektrického poľa (E), hustota prúdu (I), intenzita magnetického poľa (H), intenzita magnetického toku (B)

  * **Tvarové valcovanie**

    * Podpora siete Tet v Lagrangeovom valcovaní.

    * Import obrobkov pre Lagrangeovo valcovanie.

    * Pokračujte v behu na 2,5D od určitého priechodu.

    * Prispôsobenie nastavenia prostredia každému priechodu

    * Obrátené hádzanie v tabuľke Pass.

    * Otáčanie obrobku (LAG) v priechodnom stole.

    * Priradenie 3D rolovacej siete/materiálu pre viacnásobný prechod.

  * **Ring Rolling**

    * Užívateľsky definované ovládanie dorazu priemeru krúžku.

    * Pohyb tŕňa (PID regulácia), rýchlosť rastu krúžku v závislosti od priemeru.

    * Axiálny valivý pohyb (Path), z-zdvih ako funkcia priemeru.

  * **Spinning**

    * Ovládanie výberu typu riešiteľa a typu objektu pre nastavenie prepichovania rúr a spriadania/formovania toku.

  * **Zabezpečenie**

    * Boolean medzi priechodmi podpora s obrobkom tet mesh.

  * **Štúdia životnosti náradia**

    * Vylepšená predikcia životnosti nástroja.

  * **Analýza údajov**

    * Zlepšenie grafu (rozptyl, čiara, plocha odozvy).

  * **DOE/OPT štúdia**

    * Podpora krivky SNR (odstup signálu od šumu).

  * **Vylepšenie licencie**

    * Vylepšená stabilita licenčných modulov/služieb.

    * DEFORM Setup (verzia licenčného servera, informácie o licencii, vylepšené grafické rozhranie na stránke Simulačný server, stav servera GeoCAD)

    * Sledovanie licencií (licencovaný produkt, licencovaný riešiteľ, používané riešitele)

    * Monitor procesov (zlepšená viditeľnosť s ovládaním zapnutia/vypnutia zobrazovaných položiek, filtrovanie)

  * **Všeobecné informácie o systéme**

    * V systéme DEFORM bol vylepšený preklad jazykov.

  
_**Dôležité zmeny/vylepšenia v DEFORM v14.0**_

  1. (2D) Adaptívny kontakt BCC bol implementovaný v 2D FEM. Túto možnosť možno použiť medzi viacerými deformujúcimi sa matricami, aby sa zabránilo neočakávanému úniku uzlov.

  2. (2D) Predvolená frekvencia riešenia Maxwellovej rovnice pre 2D simulácie indukčného ohrevu bola zmenená z 20 na 1. Teraz bude 2D MKP štandardne počítať Maxwellovu rovnicu v každom kroku.

  3. (3D) V prípade procesorov Intel vybavených architektúrou výkonných jadier (P-cores) a efektívnych jadier (E-cores) môže teraz DEFORM 3D FEM vždy využívať jadrá P s riadiacim súborom DEF_PCORECTL.DAT v pracovnom adresári, aby sa maximalizovala rýchlosť výpočtov.

  4. (3D) Plastickosť kryštálov pre model textúry bola implementovaná v 3D FEM.

  5. (3D) 3D Elasto-plasitc Tet prvky so zmiešanou formuláciou boli vylepšené. Vďaka vylepšenej formulácii deformácií má teraz 3D simulácia mini Tet prvkov lepšie konvergenčné správanie a presnejšie výsledky výpočtu napätia.

  6. (3D) Pre 3D simuláciu valcovania prstenca bolo pridané zobrazenie stavovej premennej posunu vnútorného toku.

  7. (3D) 3. Rotácia pre riadenie pohybu matrice bola implementovaná v 3D FEM.

  8. (3D) V prípade súčasného pórovitého modelu Tet element sa objemová deformácia počíta na základe interpolácie tlaku, čo niekedy vedie k nepresným výsledkom. Na zlepšenie presnosti riešenia bola implementovaná nová možnosť výpočtu objemovej deformácie na základe rýchlostných polí. Túto možnosť možno aktivovať pomocou súboru DAT DEF_PVSTR.DAT.

  9. (3D) V DEFORM v13.1 je pre 3D FEM zavedený SPRLOOP.DAT, ktorý zabraňuje tomu, aby sa posuvná pružina matrice zacykla viac ako stanovený počet krát. V DEFORM v14 bude táto funkcia predvolene aktivovaná s maximálnym počtom slučiek nastaveným na 2.

  10. (2D&3D) Zlepšila sa robustnosť motora MKP kompilovaného kompilátorom Intel Fortran Compiler.

  11. (2D&3D) Všeobecný Neo-Hookeov hyperelastický model bol implementovaný pre 2D aj 3D FEM

  12. (2D&3D) Modelovanie zrna "kontinuálnej dynamickej rekryštalizácie (CDRX)" a "geometrickej dynamickej rekryštalizácie (GDRX)" bolo implementované pre hliníkové zliatiny v 2D aj 3D MKP v DEFORM v14.

  13. (2D&3D) Modelovanie zrážania a pevnosti hliníkovej zliatiny bolo implementované v 2D aj 3D MKP v DEFORM v14.

  14. (2D&3D) Elasto-plastický model porézneho materiálu bol implementovaný pre 2D aj 3D a používateľ môže teraz nastaviť tento nový model prostredníctvom grafického rozhrania DEFORM v14.

  15. (2D&3D) Aktualizácia stavových premenných pre lomové prvky bola vylepšená pre 2D aj 3D počas deaktivácie prvkov. V predchádzajúcich verziách sa hodnota poškodenia naďalej zvyšovala pre už deaktivované prvky a vnášala chybu do prvkov v okolí prostredníctvom interpolácie, ak došlo k remeshingu.

  16. (2D&3D) Nové pravidlo tvrdenia modelu Yoshida-Uemori bolo implementované v 2D aj 3D MKP.

  17. (2D&3D) V DEFORM v14 je teraz možné definovať koeficient prestupu tepla ako funkciu tlaku a medzery a funkciu teploty pre neizotermickú simuláciu v 2D aj 3D MKP. Tolerancia tepelného kontaktu je teraz k dispozícii v 2D aj 3D.

  18. (2D&3D) Kritériá zastavenia zaťaženia matrice boli vylepšené v 2D aj 3D MKP. Keď sa primárne zaťaženie výlisku blíži k zadanému maximálnemu zaťaženiu výlisku, automaticky sa zapne čiastkové krokovanie času kontaktu a simulácia využije aktualizovanú veľkosť časového kroku na zastavenie pri presnej hodnote zaťaženia výlisku.

  19. (2D&3D) Pri simulácii zachytávania plynu/maziva môže teraz používateľ použiť súbor DEF_GAS_PAIR.DAT na výber definície zachytávania medzi rôznymi objektmi. Táto funkcia je k dispozícii v programe DEFORM 3D FEM od verzie 13.1 a v programe DEFORM 2D FEM od verzie 14.

**_Dôležité opravy chýb súvisiacich s konečným modelom v DEFORM v14.0_**

  1. (2D) Opravená chyba v 2D FEM pre neizotermický osovo symetrický typ simulácie týkajúca sa tepelného výpočtu z relatívneho natočenia. V predchádzajúcich verziách, ak používateľ definoval relatívne natočenie na stránke Inter-object thermal data (Tepelné údaje medzi objektmi), táto vstupná hodnota sa mohla počas simulácie stratiť.

  2. (2D) Opravená chyba v 2D FEM, ktorá môže spôsobiť, že 2D MPI úloha sa na novom počítači po inštalácii DEFORM v13.1.1 neočakávane zastaví alebo zavesí.

  3. (2D) Opravená chyba v interpolácii 2D údajov pre prilepenie kontaktu BCC. V predchádzajúcich verziách sa pri remeshovaní nemusel úplne interpolovať prilepený kontakt BCC.

  4. (2D) Opravená chyba v 2D FEM, ktorá mohla spôsobiť zavesenie 2D MPI simulácie po dokončení úlohy.

  5. (2D) Opravená chyba v 2D FEM, ktorá mohla spôsobiť nesprávny výpočet emisivity v zmesových materiáloch.

  6. (2D) Opravená chyba pri odstraňovaní 2D lomových prvkov pre interpoláciu stavových premenných. V predchádzajúcich verziách, ak používateľ vybral výstup integračného bodu, interpolácia stavovej premennej nemusela byť po vymazaní prvku správna.

  7. (3D) Opravená chyba v 3D FEM, keď sa aktualizácia uzlových súradníc v dôsledku kontaktu nedala aktivovať pomocou možnosti "Neaktualizovať" na stránke s údajmi medzi objektmi pre simuláciu valcovania tvaru ALE.

  8. (3D) Opravená chyba v interpolácii 3D údajov pre informácie o viacerých skupinách materiálov. V predchádzajúcich verziách sa pri simulácii ALE s viacerými materiálovými skupinami mohlo stať, že po remeshovaní sa informácie o materiálovej skupine stratili.

  9. (3D) Opravená chyba v simulácii 3D Ring Rolling s modelovaním zŕn JMAK, ktorá mohla spôsobiť nesprávnu zlomkovú hodnotu pre výstupné údaje o zrnách "režim vývoja" a predchádzajúci krok deformácie."

  10. (2D&3D) Opravená chyba v DEFORM 2D&3D FEM týkajúca sa aktualizácie referenčného bodu pre typ pohybu kladiva. V predchádzajúcich verziách nebola aktualizácia referenčného bodu pri protipohybe kladivovej matrice konzistentná, ak bolo prítomné roztiahnutie lisu.

  11. (2D&3D) Opravená chyba v DEFORM 2D&3D FEM týkajúca sa kritérií zastavenia kontaktného pomeru. V predchádzajúcich verziách, ak používateľ zadal 1 ako kritérium zastavenia pomeru kontaktov, simulácia sa nemusela zastaviť, aj keď obrobok dosiahol úplný kontakt z dôvodu príliš malej tolerancie chyby.

  12. (2D&3D) Opravená chyba v kritériách zastavenia vzdialenosti. V predchádzajúcich verziách mohla aktualizácia uzlových súradníc v dôsledku generovania kontaktov viesť k tomu, že referenčný bod objektu neočakávane prešiel rovinou zastavenia a spôsobil, že simulácia sa nezastavila.

_**Dôležité vylepšenia AMG v DEFORM v14.0**_

  1. (2D) 2D mesher bol vylepšený tak, aby zvládal problémy s viacnásobnými hranicami a skupinami materiálov. V aktuálnej verzii dokáže 2D mesher teraz spracovať geometriu s viac ako 100 geometrickými slučkami.

  2. (2D) Vylepšilo sa generovanie 2D mapovanej siete s určeným rozložením hustoty. Túto funkciu možno aktivovať pomocou súboru DAT MAP.DST v pracovnom adresári. Ďalšie informácie o používaní tejto funkcie získate od SFTC.

  3. (3D) V DEFORM v14 bolo implementované lokálne remeshing 2D prierezu na základe definície okna. Táto nová funkcia funguje pre obtočený aj vytlačený typ tehlovej siete.

  4. (3D) V aplikácii DEFORM v14 môže teraz tehlová sieť pre aplikáciu plechov podporovať definíciu hustoty okennej siete.

_**Dôležité opravy chýb súvisiacich s AMG v DEFORM v14.0**_

  1. (2D) Opravená chyba v extrakcii hraníc pri postupe 2D remeshingu. V predchádzajúcej verzii, keď mali hlavné a vedľajšie objekty veľmi podobnú konfiguráciu siete, výsledky extrakcie hraníc mohli byť nesprávne.

  2. (2D) Opravená chyba v postupe 2D remeshingu, že 2D lokálny remeshing založený na funkcii okna a zlúčenia prekrývajúcej sa siete nemusí fungovať, ak remeshingový obrobok nie je objektom č. 1.

  3. (3D) Opravená chyba v 3D remeshingu tehál, ktorá mohla spôsobiť problém pri objekte s geometriou typu revolved a pevným stredom. V predchádzajúcej verzii, ak sa 2D prierez málo zmenil, mohol nastať problém pri remeshovaní tehly.

  4. (3D) Opravená chyba v 3D Tet remeshingu s rotačnou symetriou BCC. V predchádzajúcej verzii, ak má objekt remeshingu rotačnú symetriu BCC, mohla sa geometrická funkcia počas remeshingu stratiť, ak sa vyskytne záhyb.

  5. (3D) Opravená chyba pri generovaní 3D extrudovanej siete s iba 1 vrstvou prvkov. V predchádzajúcej verzii mohlo počiatočné generovanie tehlovej siete zlyhať, ak všetky uzly tehlovej siete mali symetriu BCC.

  
_**Aktualizácia knižnice materiálov v DEFORM v14.0**_

  1. Opravená nepresná definícia teploty v BetaMaterials - Waspaloy(Grain) v údajoch funkcie vrcholovej deformácie a dynamickej rekryštalizácie (kinetika a veľkosť zrna).

  2. Opravené chýbajúce údaje o fázovej transformácii pre JIS-SNC815 (HeatTreatment) v anglickej jednotke materiálového kľúčového slova v zložke Steel.

  3. Opravené chýbajúce difúzne údaje pre 12Cr_Martensitic_Stainless_Steel v anglickom jednotkovom kľúčovom slove material v priečinku Stainless_steel.

  4. Aktualizácia odkazu na zdrojové údaje o napätí pri prúdení pre niektoré kľúčové slová hliníkového materiálu

  5. Opravený nesprávny názov nemeckého štandardného materiálu pre kľúčové slová týkajúce sa hliníka 6061.

  6. Napätie pri prúdení materiálu superzliatiny INCONEL-718-11[1700-2050F(925-1120C)] bolo upravené tak, aby zohľadňovalo zmäkčenie pri prúdení.

_**Zoznam aktualizácií dokumentov v DEFORM v14.0 SP2**_

Nasledujú hlavné aktualizácie dokumentov vo verzii 14.0 SP2.

**Kategória** | **Lokalita** | **Popis**
---|---|---
Preprocesor | 20\. Definícia medziobjektových údajov | Pridané zobrazenie Examination a Explode
Lab | (New) Shape rolling Lab3 | Lagrangeovo valcovanie s prvkom Tet
Porézne laboratórium | Tvarovanie obežných dráh valčekových ložísk pomocou porézneho materiálu
Aplikácie | Laboratórium deformačných textúr | Modifikovaný postup nastavenia
(Nové) Laboratórium kreslenia nábojníc | 2D Laboratórium kreslenia nábojníc
Technické poznámky | Technické poznámky sú k dispozícii v používateľskej oblasti DEFORM | Pridané technické poznámky s odkazmi na súbory PDF a ZIP.  
  
_**Zoznam aktualizácií dokumentov v DEFORM v14.0**_

Nasledujú hlavné aktualizácie dokumentov vo verzii 14.0.

**Kategória** | **Lokalita** | **Popis**
---|---|---
Pre-procesor | 9.5 Simulation controls | Nastavenie čiastočného doménového riešiteľa
16.10 Vlastnosti objektu | Čiastočná doména
Simulátor | 23.4 Simulátor DEFORM | Monitor procesov
Prevádzkové šablóny | 29.1 Manuál pre ozubené kolesá | Metóda polohovania výliskov
43.1 Rolovanie tvarov | vylepšenia verzie 14.0
42.1 Rolovanie krúžkov | vylepšenia verzie 14.0
Aplikácie | (Nové) 2D CFD laboratórium | 2D turbulentné prúdenie
(Nové) 3D CFD laboratórium | 3D Gas quenching
(New) Multipass spinning lab | Metóda rýchleho hodnotenia
(Nové) CP-FEM Lab | Plastickosť kryštálov na predpovedanie textúry
  
_**Zoznam nových a rozšírených kľúčových slov v DEFORM v14.0 a V14.0 SP2**_

**Nie** | **Kľúčové slovo** | **Kategória** | **Ver.** | **Popis**
---|---|---|---|---
1 | OBJTYP (rozšírený) | Objekt | v14.0 | Indukčné vykurovanie - Vzduchové prostredie (typ 11)
2 | PMEAB
(Rozšírené) | Materiál | v14.0 | Pridané typy magnetickej permeability (=5,11,14,15)
3 | BHCURB (New) | Material | v14.0 | BH krivka (intenzita magnetického toku v závislosti od hustoty toku)
4 | HYSIS
(Nový) | Materiál | v14.0 | Hysterézna krivka (hysterézna strata)
5 | SOLMTD (Extended) | Sim. Ctrl. | v14.0 | Riešiteľ pre čiastočnú doménu (typ 10)
6 | WPAXIS (Extended) | Objekt | v14.0 | Nastavenia čiastočného doménového riešiteľa (WPAXIS, typ 11)
7 | MRMPRS (Nový,3D) | Objekt | v14.0 | Model lisu s viacerými ramenami (hydraulický)
8 | TRANS (Extended) | Sim. Ctrl. | v14.0 | CFD: Simulation control (typ 7)
9 | ENVMOD
(Rozšírené) | Sim. Ctrl. | v14.0 | CFD: Teplota prostredia (typ 1, f(time))
10 | OBJTYP
(Rozšírené) | Objekt | v14.0 | CFD: Fluid (typ 10)
11 | FRQNCY (Extended) | Sim. Ctrl. | v14.0 | CFD: Frekvencia výpočtu (typ 7)
12 | DFLMAX (New) | Sim. Ctrl. | v14.0 | CFD: Krokové riadenie
13 | WPAXIS
(Rozšírené) | Objekt | v14.0 | CFD: Prúdenie riadené vztlakom (WPAXIS, typ 5, gravitácia)
14 | BCCFLO
(Nový) | Objekt | v14.0 | CFD: Typ turbulentného obmedzenia (typ 1, BCCFNC) (typ 2, FLVAR)
15 | FLVAR
(Nový) | Objekt | v14.0 | CFD: Turbulentná SV (Kinetická energia, Rýchlosť rozptylu) v uzloch
16 | BCCFFN
(Nové) | Objekt | v14.0 | CFD: Definícia funkcie obmedzenia turbulentného prúdenia
17 | ECCDEF
(Rozšírené) | Objekt | v14.0 | CFD: Tok bcc, definícia steny (typ 20)
18 | ECPRES
(Rozšírené) | Objekt | v14.0 | CFD: Flow bcc, pre rôzne typy stien
19 | ECHCFN
(Nové) | Objekt | v14.0 | CFD: Funkcia okrajovej podmienky pre výpočet súčiniteľa prestupu tepla
20 | ECFLFN
(Nové) | Objekt | v14.0 | CFD: Funkcia okrajovej podmienky pre výpočet tepelného toku
21 | ECCHTC
(Nový) | Objekt | v14.0 | CFD: Vypočítaný koeficient prestupu tepla. (na plochách)
22 | ECCFLB
(Nové) | Objekt | v14.0 | CFD: Vypočítaný tepelný tok (na plochách)
23 | PMCONS
(Rozšírené) | Materiál | v14.0 | EP Porézny: Rozšírenie porézneho modelu
24 | PMYLD
(Nový) | Materiál | v14.0 | EP Porézny : Výnos
25 | PMCRP
(Nový) | Materiál | v14.0 | EP Porézne: Plazivosť
26 | FSTRES
(Rozšírené) | Materiál | v14.0 | EP Porézne: Napätie pri prúdení = f(deformácia, hustota, teplota (typ 17)
27 | YOUNG
(Rozšírené) | Materiál | v14.0 | EP Pórovitý: Youngov modul = f(hustota a pod.)
28 | ROZŠÍRIŤ
(Rozšírené) | Materiál | v14.0 | EP Pórovitý : Tepelné rozšírenie = f(hustota a pod.)
29 | POISON
(Rozšírené) | Materiál | v14.0 | EP Pórovitý: Poissonov pomer = f(hustota a pod.)
30 | HYPREL
(Rozšírené) | Materiál | v14.0 | Hyperelasticita: (typ 3)
31 | GENGEO (Nový) | Akcia | v14.0 | DEFORM-API
32 | HDNRUL
(Rozšírené) | Materiál | v14.0 | Model vytvrdzovania Yoshi-Uemori
33 | YLDS
(Rozšírené) | Materiál | v14.0 | 1. zadné napätie pre Yoshida-Uemori
34 | YLDS2
(Nový) | Materiál | v14.0 | Druhé zadné napätie pre Yoshida-Uemori
35 | ANISO
(Rozšírené) | Materiál | v14.0 | Barlat Yield 1991 (typ 7)
36 | PRCMAP
(Nové) | Materiál | v14.0 | Spracovanie mapy: mapové údaje vo vlastnostiach materiálu
37 | PMPOBJ
(Nový) | Objekt | v14.0 | Mapa spracovania: možnosti výpočtu
38 | EFFMAP
(Nové) | Objekt | v14.0 | Mapa spracovania: energetická účinnosť a nestabilita pri prvkoch
39 | GRAIN
(Rozšírené) | Materiál | v14.0 | Model zrna (CDRX)
40 | GRNDAT
(Rozšírené) | Materiál | v14.0 | Model zrna (CDRX) (typ 6)
41 | SIZEMD
(Rozšírené) | Objekt | v14.0 | Model zrna (CDRX)
42 | SIZESH
(Rozšírené) | Objekt | v14.0 | Model zrna (CDRX)
43 | TTTD
(Rozšírené) | Inter-materiál | v14.0 | Zrážkové tvrdnutie (typ 18)
44 | HDNPHA
(Rozšírené) | Materiál | v14.0 | Zrážkové tvrdnutie
45 | HDNEST
(Rozšírené) | Materiál | v14.0 | Tvrdosť: zrazenina (typ 4)
46 | TXTURE
(Rozšírené) | Materiál | v14.0 | CP FEM (informácie o textúre)
47 | CPCTRL
(Nové) | Sim. Ctrl. | v14.0 | CP FEM (riadiace údaje simulácie)
48 | TXTCPV
(Nový) | Objekt | v14.0 | CP FEM (interné stavové premenné)
49 | TXTODF
(Rozšírené) | Objekt | v14.0 | CP FEM (funkcia rozdelenia orientácie)
50 | LMAX
(Rozšírené) | Sim. Ctrl. | v14.0 | Kritérium zastavenia maximálneho zaťaženia s toleranciou
51 | STPINC
(Rozšírené) | Sim. Ctrl. | v14.0 | Sekundárne ovládanie ukladania krokov DB
52 | RNGDIA
(Nové) | Objekt | v14.0 | Valcovanie krúžku, definícia priemeru krúžku (OD alebo ID s polohou)
53 | MOVCTL
(Rozšírené) | Objekt | v14.0 | Krúžkové valenie, PID riadenie pohybu (typ 12)
54 | ANGMO3
(Nový) | Objekt | v14.0 | 3. rotačný pohyb (3D)
55 | CNTRA3
(Nový) | Objekt | v14.0 | 3. rotačný pohyb (3D)
56 | FSTRES
(Rozšírené) | Materiál | v14.0 | Pridané napätie pri prúdení (typ 16) pre model tvrdnutia Voce
57 | IHTCOF
(Nový) | Medziobjektový kontakt | v14.0 | Tepelný/bezprostredný kontakt, HTC = f(medzera)+f(tlak)
58 | SEPRES (2D)
(Rozšírené) | Inter-objekt | v14.0 | 2D adaptívny kontaktný bcc
59 | WPAXIS
(Rozšírené) | Objekt | v14.0 | WPAXIS (typ 10) pre transformáciu objektu (valcovanie tvaru)
60 | CPYCNT
(Nové) | Akcia | v14.0 | Kopírovanie údajov o kontaktoch (medzi objektmi)
61 | NDHOUT
(Nové) | Sim. Ctrl. | v14.0 | Možnosť uzlového tepelného výkonu
62 | NDHOUT
(Rozšíriť) | Sim. Ctrl. | v14.0.2 | Lineárne zváranie trením(typ 14)
  
_**Komentáre a otázky**_
Používateľ sa môže kedykoľvek obrátiť na SFTC (support@deform.com) s akoukoľvek spätnou väzbou alebo obavami týkajúcimi sa tohto výrobku.
