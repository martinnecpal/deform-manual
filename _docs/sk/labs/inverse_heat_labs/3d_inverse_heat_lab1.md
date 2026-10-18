---
lang: sk
title: "3D inverzná tepelná analýza – laboratórna práca č. 1"
---

# 3D inverzná tepelná analýza – laboratórna úloha č. 1

**Zhrnutie problému**

V tomto laboratórnom cvičení si ukážeme, ako pomocou sprievodcu „Inverse Heat Transfer Wizard“ určiť koeficienty prenosu tepla medzi obrobkom a prostredím počas procesu prenosu tepla. Na to sú potrebné údaje z merania teploty. Koeficienty prenosu tepla môžu byť funkcie teploty alebo času. Obrobku sa priradia viaceré zóny s rôznymi koeficientmi prenosu tepla.

1.1. Vytvorenie novej úlohy

1.2. Stránka výberu režimu

1.3. Nastavenie podmienok procesu

1.4. Definícia materiálu

1.5. Definovanie objektu obrobku

1.6. Import geometrie

1.7. Vytvorenie siete

1.8. Priradenie materiálu

1.9. Definícia BCC

1.10. Meracie body teploty

1.11. Definovanie časových pásiem

1.12. Vymedzenie zón prenosu tepla

1.13. Definovanie ovládacích prvkov krokov

1.14. Optimalizačné riadenie

1.15. Vytvorenie databázy

1.16. Optimalizácia

1.17. Výsledky optimalizácie

## Vytvorenie novej úlohy

Spustite nový problém v Sprievodcovi inverzným prenosom tepla s ID problému **BAR_INVHEAT**. Môžete tak urobiť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) a výberom „**3D inverzný****prenos tepla** “ a v poli „Systém jednotiek“ vyberte možnosť „**English** “ (pozri obr. 3DINVL1.1.). V poli „Umiestnenie“ môžete vybrať adresár pre projekt a potom kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoriť sprievodcu inverzným prenosom tepla.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0001.jpg' | relative_url }})

Okno „Nastavenie problému“

## Stránka výberu režimu

Po otvorení sprievodcu 3D Inverse Heat by sa malo zobraziť okno, ako je znázornené na obrázku [Fig. 3DINVL1.2.]({{ '/docs/sk/labs/machining_labs/3d_cutting_lab2/' | relative_url }}#Fig_3DTL2_2_Process_page). Ak má používateľ záujem o výpočet transformácií alebo obsahu atómov v dôsledku difúzie, môže zaškrtnúť príslušné políčka na karte „Sim Mode“. V tomto laboratórnom cvičení nebudeme zaškrtávať žiadne políčka, pretože budeme počítať iba koeficienty prenosu tepla. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0002.jpg' | relative_url }})

Okno inicializácie

## Nastavenie prevádzkových podmienok

Na tejto stránke môže používateľ nastaviť podmienky prostredia. Ak proces zahŕňa kalenie a prenos tepla, je možné zaškrtnúť príslušné políčka a definovať tak podmienky prostredia. Náš proces zahŕňa iba prenos tepla a teplota prostredia je konštantná. Preto zrušte začiarknutie políčka „Quench“, začiarknite políčko „**Transfer**“ a nastavte teplotu prostredia na **150F** (pozri obr. 3DINVL1.3.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0003.jpg' | relative_url }})

Nastavenie podmienok procesu

## Definícia materiálu

Na stránke „**Zoznam materiálov**“ vyberte a v knižnici materiálov vyberte kategóriu „**Oceľ**“ a načítajte „**AISI****-1015[70-2000F(20-1100C)]**“, ako je znázornené na obr. 3DINVL1.4. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Workpiece“.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0004.jpg' | relative_url }})

Načítavanie údajov o materiáloch z knižnice

## Definovanie objektu obrobku

Na stránke obrobku nastavte „Teplotu objektu“ na hodnotu **1575F**, ako je znázornené na obr. 3DINVL1.5. Uistite sa, že typ objektu je „Plast“ a že je zaškrtnuté políčko „Primárna forma“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0005.jpg' | relative_url }})

Definícia objektu obrobku

## Import geometrie

Na stránke „Geometria“ kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a naimportujte súbor s geometriou „**BAR_INVHEAT.STL**“ z adresára „/3d/LABS“, ako je znázornené na obr. 3DINVL1.6. Kliknutím na „Setup brick mesh“ otvoríte dialógové okno ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}). Zvoľte tlačidlo **Extrude** a ako počiatočnú plochu vyberte povrch obrobku v smere **+Z** a ako koncovú plochu povrch v smere -Z, pozri obr. 3DINVL1.7. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste zatvorili dialógové okno „Setup brick mesh“, a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}), čím otvoríte dialógové okno „Symmetry“. V dialógovom okne Symmetry vyberte Planar surface a potom vyberte povrchy obrobku v smere **+X** a **-Y** ako rovinné symetrické plochy. Na označenie každej roviny vyberte plochu a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), pozri obr. 3DINVL1.8. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) zatvorte dialógové okno „Symmetry“ a potom kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte sieť.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0006.jpg' | relative_url }})

Stránka o geometrii

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0008.jpg' | relative_url }})

Nastavenie stránky „Brick mesh“

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0007.jpg' | relative_url }})

Údaje o priradenej rovine symetrie

## Vytvoriť sieť

Keď sa používateľ nachádza na stránke „Mesh“, môže využiť expertný režim na prístup k pokročilým nastaveniam siete. Kliknutím na ikonu n ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) na paneli nástrojov prejdite do expertného režimu a vyberte voľbu **Brick****mesh**. V nastaveniach mriežky typu Brick vyberte voľbu **Finer mesh area** a trikrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), čím pridáte tri oblasti s jemnejšou mriežkou (0 – 0,59, 0,59 – 4,41, 4,41 – 5) a pre všetky tri oblasti s jemnejšou sieťou nastavte počet vrstiev na „7“, pozri obr. 3DINVL1.9.   
Vyberte kartu **2D priečny rez**, nastavte **cieľový počet prvkov** na hodnotu „**110**“, **Hrúbku prvkov** na „**4**“, **pomer veľkostí** na „**10**“ a zaškrtnite políčko **Mapovaná sieť**. Kliknite na kartu váhových faktorov a nastavte počet ok sietky na „**1**“. Kliknite na kartu **ok sietky** a pridajte okno sietky nad 2D sietku, vyberte okno 1 a nastavte hodnoty kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DINVL1.9. Nastavte Relatívnu veľkosť prvku na hodnotu „**100**“ a ako nasledujúci objekt vyberte **Obrobok**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) na vytvorenie tehlovej siete. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na priradenie materiálu.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0009.jpg' | relative_url }})

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0010.jpg' | relative_url }})

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0028.jpg' | relative_url }})

Vytvorenie siete

## Priradenie materiálu

Zoznamu materiálov vyberte materiál „**AISI****-1015[70-2000F(20-1100C)]**“, ktorý chcete priradiť k obrobku, ako je znázornené na obr. 3DINVL1.10. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku BCC.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0011.jpg' | relative_url }})

Priradenie materiálu

## Definícia pojmu BCC

V predvolenom nastavení mala byť funkcia „Výmena tepla s prostredím“ priradená k nesymetrickým plochám objektu (pozri obr. 3DINVL1.11.). Skontrolujte, či bola použitá funkcia „Výmena tepla s prostredím BCC“. Ak ešte nebola priradená, ručne priraďte BCC k nesymetrickým plochám. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Body merania teploty“.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0012.jpg' | relative_url }})

Vymieňač tepla BCC priradený k obrobku

## Meracie body teploty

Na stránke „Body merania teploty“ trikrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_row_button.jpg' | relative_url }}) a zadajte súradnice (1,249; 4,5; 4,5), (1,249; 0; 0,5) a (1,249; -4,9; 2,5) do tabuľky pre body 1, 2 a 3, ako je znázornené na obr. 3DINVL1.12.

Údaje o teplotnom priebehu pre každý bod je možné definovať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) v poslednom stĺpci tabuľky. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) a načítajte súbor „BAR_INVHEAT_Thermal_History_1.dat“ pre bod 1 zo zložky /Labs a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) (pozri obr. 3DINVL1.13.). Podobne načítajte súbory BAR_INVHEAT_Thermal_History_2.dat a BAR_INVHEAT_Thermal_History_3.dat pre bod 2, resp. 3. Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) v poslednom stĺpci tabuľky sa po definovaní údajov o tepelnej histórii pre daný bod zmení na ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_edit_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**Poznámka:** Ak chce používateľ definovať body merania teploty pre všetky tri body naraz, môže použiť tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }}) na stránke Body merania teploty na načítanie súboru „BAR_INVHEAT_Thermal_History.DAT“ zo zložky /Labs, pričom sa údaje všetkých troch bodov načítajú do sprievodcu.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0013.jpg' | relative_url }})

Stránka „Body merania teploty“

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0014.jpg' | relative_url }})

Okno s údajmi o teplotnom vývoji pre bod 1

## Definovanie časových pásiem

Na stránke časových zón môže používateľ definovať časové zóny pre ochladzovanie a prenos. Keďže sme sa v tomto laboratórnom cvičení rozhodli simulovať iba prenos, je k dispozícii iba definícia časovej zóny pre prenos. Chceme simulovať proces po dobu 506 sekúnd, keďže posledný bod merania teploty dostupný z tepelnej krivky je v čase 506 sekúnd. Zadajte teda čas začiatku 0 sekúnd a čas ukončenia 506 sekúnd. Graf tepelnej histórie všetkých bodov v rámci zadaného času je viditeľný v zobrazovacej oblasti, pozri obr. 3DINVL1.14. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0015.jpg' | relative_url }})

Definícia času prenosu na stránke „Časové pásmo“

## Vymedzenie zón prenosu tepla

Na stránke „Zóny prenosu tepla“ dvakrát kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_htc_zone_button.jpg' | relative_url }}), čím vytvoríte dve zóny. Na definovanie každej zóny prenosu tepla najprv vyberte príslušný riadok v tabuľke a potom vyberte plochy na objekte. (Na dosiahnutie ideálnych výsledkov výberu môže byť potrebné použiť ![]({{ '/assets/icons/pre_icons/mo_bcc_surface_patch_icon.jpg' | relative_url }}) v možnostiach výberu na dolnom paneli nástrojov.) Vyberte zónu č. 1 v tabuľke a vyberte plochy kolmé na smery -X, +Y a +Z, aby ste ich priradili k zóne č. 1 (pozri obr. 3DINVL1.15.). Vyberte zónu č. 2 v tabuľke a vyberte plochu kolmú na smer -Z, aby ste ju priradili k zóne č. 2 (pozri obr. 3DINVL1.16.).

**Poznámka**: Tieto dve symetrické roviny nie sú zahrnuté v žiadnej zóne prenosu tepla.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0016.jpg' | relative_url }})

Vymedzenie zóny prenosu tepla č. 1

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0017.jpg' | relative_url }})

Vymedzenie zóny prenosu tepla č. 2

Po definovaní zóny prenosu tepla kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_iniitialize_htc_button.jpg' | relative_url }}), aby ste definovali kontrolné body a limity; uistite sa, že funkcia HTC je založená na teplote. Systém pridáva kontrolné body štandardne, pre toto cvičenie ich však vymažeme a použijeme šesť ručne definovaných bodov. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_all_button2.jpg' | relative_url }}) vyprázdnite tabuľku. Zadajte nasledujúcich šesť hodnôt: 100, 400, 700, 1000, 1300 a 1600, ako je znázornené na obr. 3DINVL1.17. Uistite sa, že metóda interpolácie je Lineárna a že počiatočný odhad, dolná a horná hranica sú v poriadku. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili okno inicializácie.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0018.jpg' | relative_url }})

Definícia funkcie koeficientu prenosu tepla

Nastavenia kontrolných bodov a limitov je možné nastaviť pre každú zónu samostatne pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) vedľa položky „Zone“ na stránke „Heat Transfer Zones“ (Zóny prenosu tepla), pozri obr. 3DINVL1.15. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Step“ (Krok). 

## Definovanie ovládacích prvkov krokov

Na stránke „Step“ ponechajte hodnotu „Zmena teploty na jeden krok“ nastavenú na **1,8 F** a ostatné hodnoty ponechajte na predvolených hodnotách, ako je znázornené na obr. 3DINVL1.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0019.jpg' | relative_url }})

Definovanie ovládacích prvkov krokov

## Optimalizačné riadenie

Na stránke „Optimization Control“ (Optimalizačné riadenie), ako je znázornené na obr. 3DINVL1.19, sa uistite, že políčko BFGS nie je zaškrtnuté. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0020.jpg' | relative_url }})

Okno riadenia optimalizácie

## Vytvorenie databázy

Na stránke „DB Generation“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali nastavenie z hľadiska chýb a varovaní. Ak nie sú žiadne chyby, mala by sa zobraziť správa „Data Valid!“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu.

## Optimalizácia

Po vytvorení databázy prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) spustite optimalizáciu, pozri obr. 3DINVL1.20. Po dokončení optimalizácie sa na konci súboru protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0021.jpg' | relative_url }})

Optimalizácia behu

## Výsledky optimalizácie

Ak chcete zobraziť výsledky optimalizácie, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) vedľa karty ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}). Na stránke „Post Tools“ v časti „Tools“ uvidíte dve ikony (pozri obr. 3DINVL1.21.),

![]({{ '/assets/icons/pre_icons/mo_inverse_heat_optimal_htc.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Zobrazenie optimalizovaných hodnôt HTC.

![]({{ '/assets/icons/pre_icons/mo_inverse_heat_local_objective_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Zobrazenie simulovaných hodnôt teploty v bodoch merania teploty.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0022.jpg' | relative_url }})

Nástroje príspevku na zobrazenie výsledkov optimalizácie

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_optimal_htc.jpg' | relative_url }}) si môžete zobraziť optimalizované hodnoty HTC pre každú zónu; otvorí sa okno „Heat Transfer Zone“ (Zóna prenosu tepla), ako je znázornené na obr. 3DINVL1.22. Vyberte jednotlivé zóny a kliknutím na tlačidlo „View“ (Zobraziť) si môžete prezrieť optimalizované hodnoty HTC, pozri obr. 3DINVL1.23, ktorý znázorňuje optimalizované hodnoty HTC pre zónu č. 1.

Pomocou ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) je možné zobraziť históriu objektívnych hodnôt, pozri obr. 3DINVL1.24.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0023.jpg' | relative_url }})

Okno „Zóny prenosu tepla“ na karte „Príspevok“.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0024.jpg' | relative_url }})

Optimalizované hodnoty HTC pre zónu č. 1.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0025.jpg' | relative_url }})

Cieľ Hodnota História

Výsledok lokálnej optimalizácie je možné zobraziť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_local_objective_button.jpg' | relative_url }}); poskytuje porovnanie medzi experimentálnymi a simulovanými hodnotami teploty pri použití optimalizovaných hodnôt koeficientu prenosu tepla. Tieto hodnoty je možné v prípade potreby uložiť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) (pozri obr. 3DINVL1.25.). Používateľ môže vybrať bod (pozri obr. 3DINVL1.25.) a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_thermal_icon.jpg' | relative_url }}), aby sa zobrazil graf porovnania medzi experimentálnymi a simulovanými hodnotami teploty, alebo na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_all_button.jpg' | relative_url }}), aby sa zobrazil graf pre všetky hodnoty (obr. 3DINVL1.26.). ukazuje porovnanie medzi experimentálnou teplotou a simulovanými hodnotami teploty pre bod 1.

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0026.jpg' | relative_url }})

Miesta merania teploty v stĺpe

![]({{ '/assets/images/labs/inverse_heat_labs/3d_inverse_heat_lab1/image0027.jpg' | relative_url }})

Výsledok lokálnej optimalizácie pre bod 1
