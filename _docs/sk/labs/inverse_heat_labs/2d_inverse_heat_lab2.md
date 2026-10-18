---
lang: sk
title: "2D inverzná tepelná analýza – laboratórna práca č. 2"
---

# Laboratórna práca č. 2 z oblasti 2D inverznej tepelnej analýzy: Ochladzovanie disku v oleji

  
**Zhrnutie problému:**

V tomto laboratórnom cvičení si ukážeme, ako pomocou sprievodcu „Inverse Heat Transfer Wizard“ určiť koeficienty prenosu tepla pri procese rýchleho ochladzovania disku. Na to sú potrebné experimentálne namerané údaje o teplote. Koeficienty prenosu tepla môžu byť funkciami teploty alebo času. Disku sa priradia viaceré zóny s rôznymi koeficientmi prenosu tepla.

2.1. Začatie riešenia novej úlohy

2.2. Nastavenie typu a režimu geometrie

2.3. Nastavenie podmienok procesu

2.4. Definícia materiálu

2.5. Definovanie objektu obrobku

2.6. Import geometrie

2.7. Vytvorenie siete

2.8. Priradenie materiálu

2.9. Vytvorenie štruktúrovanej siete

2.10. Meracie body teploty

2.11. Definovanie časových pásiem

2.12. Rozdelenie zón HT

2.13. Vymedzenie zón prenosu tepla

2.14. Definovanie ovládacích prvkov krokov

2.15. Optimalizačné riadenie

2.16. Vytvorenie databázy

2.17. Optimalizácia

2.18. Výsledky optimalizácie

## Vytvorenie novej úlohy

Spustite nový problém v Sprievodcovi inverzným prenosom tepla s ID problému **DISK_INVHEAT**. Môžete tak urobiť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) a výberom možnosti „**2D Inverse Heat**“, zadajte názov problému ako ****DISK_INVHEAT** ** a v položke „Unit System“ (Systém jednotiek) vyberte „**English** “ (pozri obr. 2DINVL2.1.). V poli „Location“ (Umiestnenie) môžete vybrať adresár a potom kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoriť sprievodcu inverzným prenosom tepla.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0001.jpg' | relative_url }})

Okno „Nastavenie problému“

## Nastavenie typu a režimu geometrie

Po otvorení sprievodcu 2D Inverse Heat by sa malo zobraziť okno, ako je znázornené na obr. 2DINVL2.2. Nastavte „**Geometry****Type**“ na „**Axisymmetric**“. Ak má používateľ záujem o výpočet transformácií alebo obsahu atómov v dôsledku difúzie, môže zaškrtnúť príslušné políčka na karte „Mode“. V tomto laboratórnom cvičení nebudeme zaškrtávať žiadne políčka, pretože budeme počítať iba koeficienty prenosu tepla. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0002.jpg' | relative_url }})

Okno inicializácie

## Nastavenie prevádzkových podmienok

Na tejto stránke môže používateľ nastaviť podmienky prostredia. Ak proces zahŕňa kalenie a prenos tepla, je možné zaškrtnúť príslušné políčka a definovať tak podmienky prostredia. Náš proces zahŕňa iba kalenie a teplota prostredia je konštantná, preto **zaškrtnite** políčko „**Quench** a nastavte **teplotu** **prostredia** na **68** °F (pozri obr. 2DINVL2.3.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0003.jpg' | relative_url }})

Nastavenie podmienok procesu

## Definícia materiálu

Na stránke „**Zoznam materiálov**“ vyberte ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a v knižnici materiálov vyberte kategóriu „**Superzliatina** “ a načítajte „**INCONEL-718- 11[1700-2050F (925-1120C)]** “, ako je znázornené na obr. 2DINVL2.4. (Upozorňujeme, že teplotné rozsahy sa vzťahujú iba na údaje o plastickosti). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Obrobok“.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0004.jpg' | relative_url }})

Načítavanie údajov o materiáloch z knižnice

## Definovanie objektu obrobku

Na stránke obrobku nastavte „Teplotu objektu“ na **2000****°F**, ako je znázornené na obr. 2DINVL2.5. Uistite sa, že typ objektu je **plast** a že je zaškrtnuté políčko „Primárna forma“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku geometrie.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0005.jpg' | relative_url }})

Definícia objektu obrobku

## Import geometrie

Na stránke **Geometria** kliknite na ikonu „Načítať geometriu zo súboru“ ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a importujte súbor s geometriou „**INVHEAT_DISK****.****GEO**“ z adresára „2D/LABS“, ako je znázornené na obr. 2DINVL2.6. Zaškrtnite políčko „Zobraziť geometriu vnútri značky“ a kliknite na štítok ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste skontrolovali a opravili geometriu, pozri obr. 2DINVL2.6.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0006.jpg' | relative_url }})

Okno Geometria

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím sa otvorí okno na korekciu geometrie, a následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím opustíte stránku korekcie geometrie, pozri obr. 2DINVL2.7. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0007.jpg' | relative_url }})

Okno „Skontrolovať a opraviť geometriu“

## Vytvoriť sieť

Keď sa používateľ nachádza na stránke „Mesh“, môže využiť expertný režim na prístup k pokročilým nastaveniam siete. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) na paneli nástrojov prejdite do expertného režimu a potom zadajte **800** ako **T******a** cieľový počet prvkov** na karte „**Všeobecné**“ pre nestruktúrovanú sieť, pozri obr. 2DINVL2.8. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), potom na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku Materiál a priradili materiál.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0008.jpg' | relative_url }})

Definovanie nestruktúrovanej siete

## Priradenie materiálu

Zoznamu materiálov vyberte materiál „**INCONEL****-718- 11[1700–2050 °F (925–1120 °C)]**“, aby ste ho priradili k obrobku, ako je znázornené na obr. 2DINVL2.9.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0009.jpg' | relative_url }})

Priradenie materiálu

## Vytvorenie štruktúrovanej siete

Štruktúrovaná povrchová sieť prispieva k vyššej presnosti tepelného výpočtu pri kratšom výpočtovom čase. Preto na stránke „Materiál“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}). Použijeme **2 vrstvy** štruktúrovanej povrchovej siete s použitím povlakovej siete s hrúbkou **818****mikrónov** a **1116****mikrónov** pre vrstvu 1, resp. 2 s materiálom „**INCONEL****-718- 11[1700–2050 °F (925–1120 °C)]“** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 2DINVL2.10. Nepoužívajte tlačidlo „Generate Coating“ (Vytvoriť povlak). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), čím sa zobrazí okienko „Chcete vygenerovať sieť povlaku?“. Po vygenerovaní siete zväčšite ľavý horný roh objektu a skontrolujte, či vygenerovaná sieť obsahuje štruktúrované vrstvy. Objekt so sieťou vyzerá tak, ako je znázornené na obr. 2DINVL2.11. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Temperature Measurement Points“ (Body merania teploty); pre toto laboratórne cvičenie sú v poriadku predvolene priradené body BCC.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0010.jpg' | relative_url }})

Vytváranie štruktúrovanej siete pomocou metódy „Coating mesh“

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0011.jpg' | relative_url }})

Objekt so sieťou po vytvorení štruktúrovanej siete

## Meracie body teploty

Na stránke „Body merania teploty“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }}) (ako je znázornené na obr. 2DINVL2.12) a načítajte súbor „**InvHeat_Disk_Meas_Pnts.DAT**“ z adresára **/2D/LABS**. V grafickom okne by sa mali zobraziť body, ako je znázornené nižšie na obr. 2DINVL2.12. Vidíme, že zo súboru sa na obrobok načítalo 13 bodov merania teploty.

Údaje o teplotnom vývoji pre každý bod je možné definovať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) v poslednom stĺpci tabuľky. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) a načítajte súbor „InvHeat_Disk_Thermal_History_P1“ pre bod 1 pomocou tlačidla „Load“ zo zložky /2D/Labs a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) (pozri obr. 2DINVL2.13.), podobne načítajte údaje pre body 2 až 13 z príslušných súborov „InvHeat_Disk_Thermal_History_P2“ až „InvHeat_Disk_Thermal_History_P13“, ktoré sú k dispozícii v zložke /2D/LABS. Tlačidlo „Define“ v poslednom stĺpci tabuľky sa po definovaní údajov o tepelnej histórii pre daný bod zmení na ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_edit_button.jpg' | relative_url }}). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_exam_ all_button.jpg' | relative_url }}) (pozri obr. 2DINVL2.13.) môžeme overiť údaje definované pre všetky body. Obr. 2DINVL2.14. zobrazuje teplotu definovanú pre všetky body. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0012.jpg' | relative_url }})

Miesta merania teploty

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0013.jpg' | relative_url }})

Okno s údajmi o tepelnej histórii pre bod 1

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0014.jpg' | relative_url }})

Údaje o teplotnom vývoji definované pre všetkých 13 bodov

## Definovanie časových pásiem

Na stránke „Časové zóny“ môže používateľ definovať časové zóny pre ochladzovanie a presun. Keďže sme sa v tomto laboratórnom cvičení rozhodli simulovať iba „ochladzovanie“, je k dispozícii iba definícia časovej zóny pre „ochladzovanie“. Chceli by sme simulovať proces po dobu 600 sekúnd, keďže posledný bod merania teploty, ktorý je k dispozícii z tepelnej histórie, je pri 600 sekundách. Zadajte teda **Čas začiatku** ako **0** sekúnd a **Čas ukončenia** ako **600** sekúnd. Graf teplotnej histórie všetkých bodov v rámci zadaného času je zobrazený v zobrazovacej oblasti, pozri obr. 2DINVL2.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0015.jpg' | relative_url }})

Definícia času ochladenia na stránke „Časové pásmo“

## Rozdelenie zóny HT

Na stránke „HT Zone Partitioning“ vidíme, že systém automaticky vygeneroval zóny na základe definovaných teplotných bodov. Zaškrtnite políčko „Display Zone“, aby ste si overili vytvorené zóny. V rámci tohto cvičenia vytvoríme päť zón ručne. Vnútorný polomer ako zóna 1, spodný okraj ako zóna 2, vonkajší polomer a horná plocha až po koncový bod stupňovitého zaoblenia ako zóna 3, stupňovité zaoblenie ako zóna 4 a horná plocha od vnútorného polomeru až po začiatok stupňovitého zaoblenia ako zóna 5.

Už definované zóny odstránime pomocou tlačidla „Odstrániť všetko“. Štandardne sa celé okraje vonkajšej plochy považujú za jednu zónu. Po vymazaní bodov vyberieme ako prvý bod počiatočný bod vnútorného polomeru, ako druhý bod koncový bod vnútorného polomeru, ako tretí bod rohový bod spodnej hrany, ako štvrtý bod koncový bod stupňovitého zaoblenia a ako piaty bod počiatočný bod stupňovitého zaoblenia, ako je znázornené na obr. 2DINVL2.16. Kliknutím na „Generate Zone“ (Vytvoriť zónu) vygenerujeme zóny. Zóny sa vytvoria medzi vybranými dvojicami bodov, pozri obr. 2DINVL2.16. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0016.jpg' | relative_url }})

Okno na rozdelenie zón HT

## Vymedzenie zón prenosu tepla

Na stránke „Zóny prenosu tepla“ vidíme, že bolo vytvorených 5 zón. Výber zóny v tabuľke spôsobí zobrazenie príslušnej zóny na objekte, pozri obr. 2DINVL2.17.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0017.jpg' | relative_url }})

Zobrazenie zóny 1

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_iniitialize_htc_button.jpg' | relative_url }}), aby ste definovali regulačné body a limity; uistite sa, že funkcia HTC je založená na teplote. Systém štandardne pridá niekoľko regulačných bodov; pre toto cvičenie ich vymažeme a použijeme osem bodov. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_all_button2.jpg' | relative_url }}) a potom zadajte osem hodnôt **70, 600, 900, 1200, 1400, 1600, 1800,** a **2000**, pozri obr. 2DINVL2.18. Uistite sa, že metóda interpolácie je Lineárna. Ako **počiatočný odhad** použijeme hodnotu **1e-3** a ako **dolnú** a **hornú** **hranicu** použijeme hodnoty **7e-5** a **5e-3**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili okno inicializácie.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0018.jpg' | relative_url }})

Odstránenie nežiaducej zóny č. 3

Nastavenia kontrolných bodov a limitov je možné nastaviť pre každú zónu samostatne pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_edit..._button.jpg' | relative_url }}) vedľa položky „Zone“ na stránke „Heat Transfer Zones“ (Zóny prenosu tepla), pozri obr. 2DINVL2.17. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Step“ (Krok). 

## Definovanie ovládacích prvkov krokov

Na stránke „Step“ zmeňte hodnotu „**Zmena teploty na jeden krok**“ na **5,0** a ostatné hodnoty ponechajte na predvolených hodnotách, ako je znázornené na obr. 2DINVL2.19. Kliknite na .![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0019.jpg' | relative_url }})

Definovanie ovládacích prvkov krokov

## Optimalizačné riadenie

Na stránke „Optimization Control“ (Oblasti riadenia optimalizácie), ako je znázornené na obr. 2DINVL2.20., sú všetky predvolené nastavenia v poriadku. Uistite sa, že je zaškrtnutá možnosť **BFGS**, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0020.jpg' | relative_url }})

Okno riadenia optimalizácie

## Vytvorenie databázy

Na stránke „DB Generation“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali nastavenie z hľadiska chýb a varovaní. Ak nie sú žiadne chyby, mala by sa zobraziť správa „Data Valid!“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu.

## Optimalizácia

Po vytvorení databázy prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov a kliknutím na ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) spustite optimalizáciu, pozri obr. 2DINVL2.21. Po dokončení optimalizácie sa na konci súboru protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0021.jpg' | relative_url }})

Optimalizácia behu

## Výsledky optimalizácie

Ak chcete zobraziť výsledky optimalizácie, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). Na stránke „Nástroje“ v časti „Nástroje“ uvidíte dve ikony (pozri obr. 2DINVL2.22.),

![]({{ '/assets/icons/pre_icons/mo_inverse_heat_optimal_htc.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Zobrazenie optimalizovaných hodnôt HTC.

![]({{ '/assets/icons/pre_icons/mo_inverse_heat_local_objective_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Zobrazenie simulovaných hodnôt teploty v bodoch merania teploty.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0022.jpg' | relative_url }})

Nástroje príspevku na zobrazenie výsledkov optimalizácie

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_optimal_htc.jpg' | relative_url }}) zobrazíte optimalizované hodnoty HTC pre každú zónu; otvorí sa okno „Heat Transfer Zone“ (Zóna prenosu tepla), ako je znázornené na obr. 2DINVL2.23. Vyberte každú zónu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_thermal_icon.jpg' | relative_url }}), aby ste si prezreli optimalizované hodnoty HTC; optimalizované hodnoty HTC pre zónu č. 1 nájdete na obr. 2DINVL2.24. 

Pomocou ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) je možné zobraziť históriu objektívnych hodnôt, pozri obr. 2DINVL2.25.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0023.jpg' | relative_url }})

Okno „Zóny prenosu tepla“ na karte „Príspevok“

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0024.jpg' | relative_url }})

Optimalizované hodnoty HTC pre zónu č. 1

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0025.jpg' | relative_url }})

Cieľ Hodnota História

Výsledok lokálnej optimalizácie je možné zobraziť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_local_objective_button.jpg' | relative_url }}); poskytuje porovnanie medzi experimentálnymi a simulovanými hodnotami teploty pri použití optimalizovaných hodnôt koeficientu prenosu tepla. Tieto hodnoty je možné v prípade potreby uložiť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) (pozri obr. 2DINVL2.26.). Používateľ môže vybrať bod (pozri obr. 2DINVL2.28.) a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_thermal_icon.jpg' | relative_url }}), čím sa vykreslí porovnanie medzi experimentálnymi a simulovanými hodnotami teploty; obr. 2DINVL2.27. znázorňuje porovnanie medzi experimentálnymi a simulovanými hodnotami teploty pre bod 1. Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_all_button.jpg' | relative_url }}) (pozri obr. 2DINVL2.26.) možno použiť na zobrazenie porovnania medzi experimentálnymi a simulovanými hodnotami teploty pre všetky body, pozri obr. 2DINVL2.28.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0026.jpg' | relative_url }})

Miesta merania teploty v stĺpe

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0027.jpg' | relative_url }})

Výsledok lokálnej optimalizácie pre bod 1

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0028.jpg' | relative_url }})

Výsledok lokálnej optimalizácie pre všetky body
