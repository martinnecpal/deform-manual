---
lang: sk
title: "Laboratórium výpočtu TTT"
---

# Lab 1. Laboratórium Material Suite pre výpočet TTT diagramu

1.1. Zavedenie teórie výpočtu TTT v DEFORMÁCII

1.2. Spustiť výpočet TTT v Material Suite

1.3. Definujte pracovný adresár

1.4. Definujte vstup TTT

## Zavedenie teórie výpočtu TTT v DEFORMÁCII

Program výpočtu TTT je založený na Kirkaldyho difúznych a martenzitických modeloch [1]. Pôvodný model bol transformovaný na stavovo variabilný model, ktorý umožňuje výpočty kinetiky transformácie objemových frakcií. Cieľom programu je modelovať kinetiku transformácie objemovej frakcie feritu, perlitu, bainitu a martenzitu na kalenie austenitu, pričom sa ignoruje podrobné rozlíšenie podľa morfológie fázy. Hlavné predpoklady zahŕňajú jednoduché fázové škálovanie pre viacfázovú tvorbu, pravidlo aditivity pre CCT, ferit a perlit sa nevyskytujú v rovnakej časovej mierke, perlit sa nevyskytuje pod teplotou Bs atď. Program vygeneruje TTT diagram na základe zloženia vstupnej zliatiny používateľa, veľkosti zrna, ako aj ďalších parametrov. Program preukázal primeranú predpoveď TTT diagramu pre nízkolegované ocele (<0,6 hm. % C, <2 hm. % Mn, <5 hm. % Ni, <2 hm. % Cr, <1 hm. % Si).

Nižšie je uvedené porovnanie vypočítaných TTT a CCT diagramov s použitím DEFORMÁCIE s experimentálnymi nameranými diagramami pre tri rôzne ocele: AISI 1035, AISI5140 a AISI1050. Horné tri hodnoty sú z experimentálnych meraní a spodné hodnoty sú vypočítané z tohto programu. Celkovo vypočítaný diagram veľmi dobre súhlasí s experimentmi.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0001.jpg' | relative_url }})

Porovnanie vypočítaných TTT a CCT diagramov s použitím DEFORMÁCIE s experimentálnymi nameranými diagramami

## Spustiť výpočet TTT v súbore materiálov

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v12.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI. Z hlavného grafického rozhrania kliknite na **Material Suite** v časti „Post Processor“ a otvorte modul Material Suite. Používateľ môže tiež dvakrát kliknúť na "DEF_GUI_MAT.exe" v inštalačnom adresári DEFORMAČNÉHO softvéru a spustiť sadu materiálov. Po zobrazení hlavného okna pre balík materiálov rozbaľte položku „vlastnosti“ a kliknite na ikonu „** Výpočet TTT ** “, do stromu úloh sa pridá nová položka úlohy „** Diagram TTT * *“ (pozri obr. TTTL1.2.). Postupujte podľa každej položky stromu a pripravte TTT diagram v okne s údajmi o vlastnostiach (pravé dolné okno).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0002.jpg' | relative_url }})

Spustiť výpočet TTT v balíku materiálov

## Definovať pracovný adresár

V stromu úloh „TTT Diagram“ kliknutím na „**Config** “ otvorte okno a zadajte pracovné adresáre, ako je znázornené na obrázku nižšie. TTTL1.3. Zadajte pracovný adresár, do ktorého sa budú ukladať vypočítané údaje TTT.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0003.jpg' | relative_url }})

Konfiguračné okno na definovanie pracovného adresára

## Definovať vstup TTT

V stromu úloh „**TTT diagram** “ kliknite na „**TTT vstup** “ a zadajte TTT vstup.

Na vstupnej stránke TTT umožňujeme používateľovi zadať nasledujúce informácie:

1. Chémia materiálov alebo zloženie uhlíkových a hlavných zliatinových prvkov vrátane Mn, Si, Ni, Cr, Mo, Cu, V a Nb.

2. Veľkosť zrna (v čísle ASTM)

3. Začiatok a koniec objemového zlomku (napr. 1%začiatok a 99% koniec)

4. Teplota transformácie martenzitu a austenitu: používateľ môže zadať tieto teploty ako vstup, ak sú k dispozícii informácie, inak kliknutím na tlačidlo "Auto" program automaticky vypočíta tieto hodnoty.

V tomto laboratóriu sme zvolili **AISI 3120** ako príklad a zadali sme nasledujúce parametre: **C(0,17%), Mn (0,88%), Si(0,22%), Ni(0,86%), Cr(0,59%), Mo(0,05%), Cu (0), V(0), Nb(0), veľkosť zrna 7, východiskový objemový zlomok 1%, končiac 99%** , Martenzitová a Austenzitická transformačná teplota je vypočítaná programom. Po zadaní všetkých parametrov kliknite na "**Vypočítať** " pre výpočet TTT diagramu. Po vykonaní výpočtu sa v pracovnom adresári vygenerujú tieto dva súbory:

**TTT.KEY**

**CCT.DAT**

Vypočítané údaje TTT sú zahrnuté v súbore „**TTT.KEY** “. Tlačidlo „**Graf** “ v grafickom používateľskom rozhraní je tiež aktivované na zobrazenie vypočítaných výsledkov. Ak to chcete urobiť, používateľ si môže vybrať navrhnutú kinetiku transformácie v ponuke vedľa tlačidla „**Graf** “ a potom kliknúť na „**Graf** “.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0004.jpg' | relative_url }})

Vstupná stránka TTT

V tomto príklade sú nižšie zobrazené údaje o transformácii TTT pre austenit na perlit, austenit na bainit a austenit na ferit (pozri obr. TTTL1.5., obr. TTTL1.6. a obr. TTTL1.7.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0005.jpg' | relative_url }})

Vypočítané údaje o transformácii TTT pre austenit - perlitovú transformáciu (krivka 1)

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0006.jpg' | relative_url }})

Vypočítané údaje o transformácii TTT pre austenit - bainitovú transformáciu (krivka 1)

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0007.jpg' | relative_url }})

Vypočítané údaje o transformácii TTT pre austenit - feritovú transformáciu (krivka 1)

Značka:

[1] „Predikcia mikroštruktúry a kaliteľnosti v nízkolegovaných oceliach“ J. S. Kirkaldy, D. Venugopalan - Fázové transformácie v zliatinách železa, 1983
