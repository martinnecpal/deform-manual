---
lang: sk
title: "Laboratórium modelovania deformačných textúr"
---

# Material Suite Lab pre model deformačnej textúry

1.1. Abstrakt

1.2. Spustite model deformačnej textúry v súbore materiálov

1.3. Výber objektu a výber bodu

1.4. Nastavenie modelu deformačnej textúry

1.5. Simulátor bodu točenia materiálu

1.6. Výstup

Abstrakt

Model deformačnej textúry v súbore materiálov simuluje vývoj deformačnej textúry vo vybraných zaujímavých bodoch po spustení 2D alebo 3D nominálnej databázy. Môže sa aplikovať na akýkoľvek jednofázový alebo dvojfázový polykryštalický materiál. Kryštalická štruktúra každej fázy môže byť FCC, BCC alebo HCP. deformácia poskytuje spustiteľný súbor kryštálovej plasticity (CP) (DEF_CP.EXE) alebo používatelia môžu vytvoriť svoje vlastné spustiteľné súbory. Pre vykonateľnú krištáľovú plasticitu poskytnutú deformáciou je možné použiť homogenizačnú schému Taylor alebo VPSC. Textúra môže byť reprezentovaná buď v Rodriguesovom priestore alebo v priestore Eulerových uhlov. Základné vstupné údaje zahŕňajú kontrolné údaje simulácie CP, definíciu materiálu, počiatočnú textúru a mikroštruktúru. Pre každý uložený krok v nominálnej databáze výstupné údaje zahŕňajú makroskopický tenzor napätia polykryštalického agregátu, lokálne zložky napätia v každom zrne a údaje o textúre, t. j. funkcie distribúcie orientácie (ODF) v Rodriguesovom priestore alebo Eulerove uhly s váhami. K dispozícii sú nástroje na analýzu textúr, ako sú pólové čísla, inverzné pólové čísla a Kearnsovo číslo kryštálu HCP. Pre nominálnu databázu s existujúcimi údajmi o textúre je možné tento modul použiť na extrakciu informácií o textúre a vykonanie analýzy textúry na zaujímavých bodoch vybraných používateľom.

V tomto laboratóriu sa simuluje vývoj textúry Ti-6Al-4V počas kovania.

## Spustite model deformačnej textúry v súbore materiálov

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v13.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI.

Požadujeme nominálnu DB na vykonanie analýzy textúry v súbore materiálov, pre toto laboratórium použijeme * * Double_Cone_Forging_Nominal.key * * z * *\MANUÁLY\ PDF \ DEFORM3D_Texture_Evolution_Lab** priečinok na vygenerovanie nominálnej DB. Otvorte **NG Pre** pomocou prepojenia DEFORMÁCIE GUI Main a definujte ID problému ako " **Double_cone_Forging** ", vyberte prepínač "* * 3D * * " Dimension a "**System International (SI)** " unit System prepínač v okne New Problem, potom importujte ** Double_Cone_Forging_Nominal.key ** z priečinka **\MANUAL\PDF \ DEFORM3D_Texture_Evolution_Lab**. Prejdite na stránku Generate DB a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) pre vygenerovanie databázy. Zatvorte NG Pre a spustite simuláciu z GUI Main, uistite sa, že simulácia sa zastaví normálne bez akéhokoľvek problému. Teraz z hlavného GUI bez výberu * ***Double_CONE_Forging* ***.DB súbor kliknite na **Materiál * ***Suite * * v časti „Post Processor“ a otvorte modul Material Suite.

Po zobrazení hlavného okna pre sadu materiálov kliknite na ikonu "Otvoriť..." (![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }}) ) v hornom paneli nástrojov a importujte vzorovú databázu (**Double_cone_Forging.DB**). Do stromu úloh sa pridá predvolená položka úlohy „DEFORMOVAŤ“. Rozbaľte položku „Mikroštruktúra“ a kliknite na ikonu „Model textúry“, do stromu úloh sa pridá nová položka úlohy „Model vývoja textúry“.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0001.jpg' | relative_url }})

Spustite model deformačnej textúry v súbore materiálov.

## Výber objektu a výber bodu

Ako je znázornené na obr. DTML1.2., v strome úloh „DEFORMOVAŤ“ kliknite na položku „** Výber objektu ** “ a vyberte položku „**obrobok** “. Kliknite na položku „* * Výber bodu * * “, definujte číslo kroku ako **„-1** “ a definujte dva body na obrobku ( obr. DTML1.3.) Súradnica bodu 1 (P1) je (0,738, 0,147,0,967, 1) a súradnica bodu 2 (P2) je (7,93, 0,071, 12,04, 1). Používatelia si môžu zvoliť ľubovoľné číslo kroku, ktoré im vyhovuje, napríklad posledný krok, na definovanie bodov.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0002.jpg' | relative_url }})

Object Selection

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0003.jpg' | relative_url }})

Výber bodu

## Nastavenie modelu deformačnej textúry

Všetky údaje pre model deformačnej textúry sú pripravené položkami uvedenými v strome úloh „** Model vývoja textúry ** “. Kliknite na položku „**Config** “, jej okno s údajmi sa zobrazí tak, ako je znázornené na obr. DTML1.4. Kliknutím na tlačidlá definície (![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }})) zadajte spustiteľný súbor pre simuláciu CP a pracovný adresár. Predvolený spustiteľný súbor pre simuláciu CP implementovanú v DEFORMÁCII je „DEF_CP.EXE“, ktorý sa nachádza v inštalačnom adresári softvéru DEFORM. Používatelia môžu tiež vytvoriť svoj vlastný spustiteľný súbor pre simuláciu CP a zadať názov súboru tu. Pracovný adresár musí byť ten, v ktorom sa nachádza nominálna databáza.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0004.jpg' | relative_url }})

Stránka konfigurácie

Kliknite na položku „** Kontrola simulácie polykryštalickej plasticity ** “, jej okno s údajmi je zobrazené na obr. DTML1.5. Je potrebné špecifikovať nasledujúce údaje: metódu reprezentácie textúry (Eulerove uhly alebo Rodriguesov priestor), rozsah krokov na uplatnenie simulácie CP, zdroj údajov o textúre, zdroj spustiteľných údajov, homogenizačnú schému (Taylor alebo VPSC), linearizačnú schému úrovne zrna (Secant, affine, intermediate a tangens), konvergenčné a iteračné kritériá. Predvolené hodnoty sú uvedené, ale používatelia môžu tieto hodnoty zmeniť. Ak v databáze existujú textúrne údaje (ODF), dajú sa automaticky zistiť a podľa toho sa nastaví grafické používateľské rozhranie, napríklad prepínač **"Existujúce ODF v databáze** " je vybratý, keď v databáze existujú textúrne údaje (ODF). V tomto laboratóriu budeme používať metódu reprezentácie textúr ako **Rodriguesov priestor** a zdroj údajov o textúrach ako **Nová definícia * *, pretože nominálna databáza nemá údaje ODF. Zadajte rozsah krokov od -1 do 500. Homogenizačnú schému ponecháme na VPSC a linearizačnú schému na úrovni zrna na Affine a ďalšie polia sa použijú s predvolenými hodnotami, ako je znázornené na obr. DTML1.6.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0005.jpg' | relative_url }})

Kontrola simulácie polykryštalickej plasticity - Existujúce ODF v databáze

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0006.jpg' | relative_url }})

Kontrola simulácie polykryštalickej plasticity - nová definícia

Ak údaje o textúre existujú v databáze, údaje o materiáli sa automaticky extrahujú z databázy a zobrazia sa. Vlastnosti materiálu si môžete prezrieť kliknutím na tlačidlo „**Upraviť** “. V tomto prípade by sa nemali meniť vlastnosti materiálu. Jedinou dotknutou vlastnosťou sú základné informácie o textúre (typ kryštálu, typ textúry a typ Rodriguesovej siete). Ak je v riadení simulácie CP použitá "** Nová definícia * * " pre zdrojové dáta textúry, potom je potrebné predefinovať materiál pre vybraný objekt . Novým materiálom pre obrobok môže byť jednofázový materiál alebo zmesový materiál. Ak ide o jednofázový materiál, musíme definovať jeho základné informácie o textúre a údaje o napätí toku CP (v plastovej stránke „![]({{ '/assets/icons/pre_icons/mo_plastic_button.jpg' | relative_url }}) “), ako je znázornené na obr. DTML1.8. a obr. DTML1.9. Ak je novým materiálom pre obrobok zmesový materiál, musíme definovať základné informácie o textúre a údaje modelu napätia prietoku CP pre každú fázu. V súčasnosti možno uvažovať iba s kryštálovými štruktúrami BCC (body-centered cubic), FCC (face-centered cubic), HCP (hexagonal close packed). Na obr. DTML1.8. je uvedený príklad na definovanie modelu CP prietokového napätia pre kryštál HCP (ako fáza „Alpha“ na obr. DTML1.10.). Pre kryštál HCP musíme špecifikovať pomer c/a (napríklad 1,588 pre zliatiny titánu). Režim deformácie je definovaný podľa rodiny roviny sklzu a smeru sklzu.

Keďže pri riadení simulácie CP pre toto laboratórium používame pre zdrojové dáta textúr „Nová definícia“, je potrebné predefinovať materiál pre vybraný objekt (obrobok). Kliknite na položku „Definícia materiálu“, príklad súboru kľúčového slova s parametrami materiálu CP pre Ti64 sa nachádza v priečinku Texture Evolution Lab (Ti64_LabTxr_CP.key). Importujte tento súbor kľúčových slov pomocou tlačidla „Import“ zobrazeného na obr. DTML1.7. Importované údaje o materiáli je možné zobraziť pomocou tlačidla Upraviť. V tomto laboratóriu máme dve fázy Alpha a Beta a pre každú fázu použijeme Rodriguesovu sieť typu 2.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0007.jpg' | relative_url }})

Definícia materiálu

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0008.jpg' | relative_url }})

Dialóg úpravy materiálu pre vlastnosť Plastic

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0009.jpg' | relative_url }})

Dialóg úpravy materiálu pre základné informácie o textúre

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0010.jpg' | relative_url }})

CP model prietokového napätia pre kryštál HCP

V aktuálnom kóde DEFORMÁCIE CP sa režim twinning deformácie neberie do úvahy. Kryštál HCP má tri režimy deformácie: bazálny sklz (3 x {0001}<11-20>), prizmatický sklz (3 x {10-10}<11-20>) a pyramídový sklz (6 x {10-11}<11-20> +12 x {10-11}<11-23> \+ 6 x {11-22}<11-23>). FCC kryštál má jeden deformačný režim: 12 x {111}<110>. Kryštál BCC má tri režimy deformácie: 12 x {110}<111>, 12 x {112}<111>, 24x {123} <111>. Všetky režimy deformácie sú aktivované. Parametre materiálu CP sú definované pre každý režim deformácie a latentné kalenie je definované medzi režimami deformácie. Parametre materiálu CP môžu byť konštantné alebo môžu byť funkciou teploty. Dve kaliace pravidlá sú implementované v DEFORMÁCII. Pravidlo vytvrdzovania 1 sa uplatňuje pre Taylorovu schému a pravidlo vytvrdzovania 2 sa uplatňuje pre schému VPSC. Symboly v pravidle prietoku a pravidle vytvrdzovania sú stručne vysvetlené v GUI a tu sa neopakujú. Je zodpovednosťou používateľa špecifikovať príslušné parametre materiálu CP, napríklad získavanie z literatúry, určovanie vlastným prístupom používateľa alebo montáž modulom deformačného prietokového napätia v materiáli z hľadiska experimentálne nameraných údajov o prietokovom napätí a počiatočnej mikroštruktúry (nad rámec tohto laboratória a tu ďalej nediskutované).

Kliknutím na položku „**Počiatočná textúra a mikroštruktúra** “ otvoríte okno s údajmi (obr. DTML1.11.). Ak je na kontrolnej stránke simulácie CP vybratá možnosť „** Existujúce ODF v databáze * *“, všetky údaje sa automaticky extrahujú a vyplnia na tejto stránke. Údaje je možné skontrolovať, ale nie upraviť. Keďže na kontrolnej stránke simulácie CP sa vyberie „Nová definícia“ pre údaje zdroja textúry, mali by sa tu definovať všetky údaje pre každý vybraný bod. Osi textúry (RD-TD-ND) sú definované v globálnom súradnicovom systéme pre simuláciu MKP, ako je znázornené na obr. DTML1.11\. Kliknutím na tlačidlo "* * Použiť os * * " použijete definovanú hodnotu osi textúry pre vybraný bod 1.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0011.jpg' | relative_url }})

Počiatočná štruktúra a mikroštruktúra: osi textúry

Kliknite na kartu **Orientačné údaje * *, obr. DTML1.12\. zobrazuje orientačné údaje alfa fázy pre vybraný bod (bod 1). Ak je v ovládacom prvku simulácie CP zvolené „** Existujúce ODF v databáze * *“, hodnoty ODF sa extrahujú z databázy a zobrazia sa v textúre

tabuľka, čo znamená, že hodnoty ODF sú reprezentované v systéme RD-TD-ND. Ak je vybratá možnosť „Nová definícia“, musíme špecifikovať formát orientačných údajov, súbor orientačných údajov a uhol vyhladenia (stupeň) pre ODF (ak je priestor reprezentácie textúry

je Rodriguesova medzera); potom kliknite na tlačidlo ("![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }})") na inicializáciu údajov o textúre a zobrazenie výsledku v tabuľke textúr. Keď je priestor reprezentácie textúry Rodriguesov priestor, hodnoty ODF sa vypočítajú v globálnom súradnicovom systéme; keď je priestor reprezentácie textúry Eulerov priestor, v tabuľke textúr sa zobrazia uhly a hmotnosti Eulera v systéme RD-TD-ND (ako prijaté údaje). Môžeme vykresliť obrysy ODF a čísla pólov, aby sme preskúmali, či sú údaje o textúre definované správne.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0012.jpg' | relative_url }})

Počiatočná textúra a mikroštruktúra: orientačné údaje

Aby bolo možné pohodlne importovať pôvodné údaje o textúre, je navrhnutých päť typov orientácií alebo formátov údajov v DEFORMÁCII:

* Rozdelenie náhodnej orientácie, pre ktoré sú hodnoty ODFs 1,0 v každom nezávislom uzle v Rodriguesovom priestore. Pre materiál s izotropnými mechanickými vlastnosťami je možné aplikovať tento typ textúry. Ak je priestorom reprezentácie textúry Eulerov priestor, zodpovedajúce uhly a hmotnosti Eulera sa generujú podľa základných informácií o textúre uvedených na stránke „** Definícia materiálu ** “.

* EBSD TSL/General (Bunge, radians)

Eulerove uhly sú vyjadrené v radiánoch v Bungeovej notácii. Toto je predvolené nastavenie v DEFORMÁCII na výpočet orientačnej matice. Efektívne údaje EBSD (za predpokladu, že počet orientácií je N) sú preusporiadané v nasledujúcom formáte:

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/eq_1.jpg' | relative_url }})

* EBSD HKL (Bunge, stupne)

Eulerove uhly sú vyjadrené v stupňoch v Bungeovej notácii. Efektívne údaje EBSD

(za predpokladu, že počet orientácií je N) sú preusporiadané v nasledujúcom formáte:

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/eq_2.jpg' | relative_url }})

Pred výpočtom orientačnej matice sa pripočítajú tretie Eulerove uhly o 90 stupňov, aby sa konvertoval z formátu HKL do formátu TSL.

* WTD (Kocks, Degrees, Weights)

V "Weighted (WTD)" (Kocks, Degrees, Weights) sú Eulerove uhly vyjadrené v stupňoch v Kockovej notácii. Efektívne vážené orientačné údaje (za predpokladu, že počet orientácií je N) sú usporiadané v nasledujúcom formáte (Eulerove uhly a závažia):

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/eq_3.jpg' | relative_url }})

* WTD (Bunge, Radiány, Závažia)

V "Weighted (WTD)" (Bunge, Radians, Weights) sú Eulerove uhly vyjadrené v radiánoch v Bungeovej notácii. Formát údajov je rovnaký ako v type 4.

Ak pôvodné experimentálne namerané údaje o textúre nie sú v týchto formátoch, používateľ by mal previesť pôvodné údaje do jedného z piatich navrhnutých formátov a potom importovať prevedený dátový súbor. Hodnoty ODF v Rodriguesovom priestore závisia od uhla vyhladenia, ktorý je všeobecne nastavený na 5~10 stupňov. Všeobecne platí, že uhol vyhladzovania je nastavený na 10 stupňov pre Rodriguesovo pletivo typu 2, 5 stupňov pre Rodriguesovo pletivo typu 3 a 2,5 stupňa pre Rodriguesovo pletivo typu 4.

V tomto laboratóriu, pretože používame „novú definíciu“, definujeme uhol vyhladenia ODF na 10 stupňov pre Alpha aj Beta a klikneme na ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Počiatočné údaje o textúre pre alfa a beta sú umiestnené v priečinku laboratória vývoja textúry: **DEFORM_Sample_alpha.wts** , **DEFORM_Sample_beta.wts**. Formát údajov typu 4 (WTD: Kocks, Degrees, Weight) je prijatý. Použitie možnosti importovať dátový súbor **DEFORM_Sample_alpha.wt** pre materiál Alpha a **DEFORM_Sample_beta.wts** pre model Beta.

Keďže v tomto laboratóriu používame zmesový materiál, objemové frakcie pre všetky fázy je potrebné špecifikovať tak, ako je znázornené na obr. DTML1.13. v záložke objemové zlomky.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0013.jpg' | relative_url }})

Počiatočná štruktúra a mikroštruktúra: objemový zlomok

Po dokončení definície počiatočnej textúry a mikroštruktúry pre jeden bod môžeme kliknutím na tlačidlo „**Aplikovať na** “ skopírovať údaje do iného bodu alebo všetkých zostávajúcich bodov, ak majú rovnakú počiatočnú textúru a mikroštruktúru. Kliknutím na „**Aplikovať na** “ skopírujete údaje pre bod 2, ako je znázornené na obr. DTML1.13. Po dokončení nastavenia modelu deformačnej textúry sa môžeme vrátiť na stránku „** Kontrola simulácie polykryštalickej plasticity ** “ a kliknutím na „**Uložiť projekt** “ uložiť údaje o projekte. Ak existuje uložené nastavenie projektu, môžeme ho načítať kliknutím na tlačidlo „* * Importovať projekt * * “.

## Spustiť simulátor materiálových bodov

Kliknite na položku „* * Spustiť * * “ v strome úloh a v okne údajov kliknite na tlačidlo „Vypočítať“ (pozri obr. DTML1.14.). V pracovnom adresári sa vytvorí priečinok s názvom „TEXTÚRA“ a pod ním sa vytvorí priečinok pre každý vybraný bod s názvom „Bod*“ (* označuje číslo bodu) na uloženie výsledkov simulácie.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0014.jpg' | relative_url }})

Spustiť simuláciu

Vo všeobecnosti sa pre každý vybraný bod vytvoria nasledujúce dátové súbory. Ak sa použije spustiteľný súbor simulácie CP používateľa, mali by sa dodržiavať rovnaké formáty súborov vstupných a výstupných údajov, aby nástroje na analýzu textúr mohli správne importovať údaje.

Vstupné súbory pre spustiteľný súbor simulácie CP:

STEP.txt: uložené čísla krokov v nominálnej databáze.

temp_mean.txt: Jednotkový systém a história teploty.

VELGRD.txt: História rýchlostného gradientu.

DEFGRD.txt: História deformačného gradientu.

SIMCTRL_CP.DAT: Dáta riadenia simulácie CP.

MAT_CP.DAT: Parametre materiálu CP.

TxrInfo.txt: Základné informácie o textúre a počiatočné objemové zlomky pre všetky fázy.

RDTDND.txt: Počiatočné osi textúry.

ODF_S-1.txt: Počiatočné hodnoty ODF.

EulerAng_S-1.txt: Počiatočné Eulerove uhly a hmotnosti.

Výstupné súbory zo spustiteľného súboru simulácie CP:

Orm_S*.txt: Orientačná matica pre jednotlivé zrná v uloženom kroku.

ODF_S*.txt: Hodnoty ODF v uloženom kroku.

STRESS_LOCAL_S*.txt: Lokálne zložky napätia pre jednotlivé zrná v uloženom kroku.

STRESS_MACRO.txt: Komponenty makroskopického napätia pre polykryštalický agregát vo všetkých uložených krokoch.

Pre dvojfázové zliatiny titánu sa generujú nasledujúce dátové súbory:

DeformHis.Dat: údaje histórie deformácií.

InitialTexture.Dat: Počiatočné údaje o textúre pre fázu alfa a fázu beta.

MATAX_S*.txt: Osi materiálu v uloženom kroku, ak sú definované v databáze s existujúcim ODF.

vzoru.

Po dokončení simulácie sú všetky vybrané body uvedené v položke „Výstup“ v strome úloh. Zadajte číslo kroku v prehliadači krokov (malo by byť v rozsahu definovanom na kontrolnej stránke simulácie CP) a vyberte bod, výsledky simulácie je možné skontrolovať, ako je znázornené na obr. DTML1.15. Na vykonanie analýzy textúry je potrebné špecifikovať osi textúry v globálnom súradnicovom systéme. Ich hodnoty sa môžu líšiť od počiatočných osí textúry definovaných na stránke „Počiatočná textúra a mikroštruktúra“. V tomto príklade je RD zarovnaný v globálnom smere X, TD v globálnom smere Z a ND v globálnom zápornom smere Y.

Orientačné údaje pre bod 1 v poslednom kroku sú znázornené na obr. DTML1.16. Pomocou poskytnutých nástrojov na analýzu textúr môžeme vykresliť obrys ODF v Rodriguesovom priestore, pólové čísla, inverzné pólové čísla a vypočítať Kearnsovo číslo fázy HCP. Pre kovy BCC alebo FCC je možné zakresliť 4 typy pólových čísel: (100), (110), (111) alebo všetky tri pólové čísla. Pre kovy HCP je možné zakresliť 4 typy pólových čísel: (0001), (11-20), (10-10) alebo všetky tri pólové čísla. Príklady výsledkov sú zobrazené na obr. DTML1.16. \- Obr. DTML1.21.

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0015.jpg' | relative_url }})

Výstup: Definícia osí textúry pre analýzu textúry

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0016.jpg' | relative_url }})

Výstup: orientačné údaje a nástroje na analýzu textúry na vykreslenie obrysu ODF - pólové čísla

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0017.jpg' | relative_url }})

Výstup: orientačné údaje a nástroje na analýzu textúry na vykreslenie obrysu ODF - inverzné pólové čísla

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0018.jpg' | relative_url }})

Výstup: orientačné údaje a nástroje na analýzu textúr na vykreslenie obrysu ODF - Kearnsovo číslo

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0019.jpg' | relative_url }})

Kontúry ODF (pomocou hodnôt v tabuľke) a čísla pólov pre bod 1 v poslednej fáze - alfa fáze

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0020.jpg' | relative_url }})

Kontúry ODF (pomocou hodnôt v tabuľke) a pólové čísla pre bod 1 v poslednom kroku: beta fáza

![]({{ '/assets/images/labs/material_suite_labs/deformation_texture_model_lab/image0021.jpg' | relative_url }})

Hodnoty inverzného pólu pre RD pre bod 1 v poslednom kroku pre alfa fázu
