---
lang: sk
title: "2D inverzná tepelná analýza – laboratórna práca č. 1"
---

# 2D inverzná tepelná analýza – laboratórna úloha č. 1

**Zhrnutie problému:**

V tomto laboratórnom cvičení si ukážeme, ako pomocou sprievodcu „Inverse Heat Transfer Wizard“ určiť koeficienty prenosu tepla medzi obrobkom a médiom počas procesu prenosu tepla. Na to sú potrebné údaje z merania teploty. Koeficienty prenosu tepla môžu byť funkciou teploty alebo času. Obrobku sa priradia viaceré zóny s rôznymi koeficientmi prenosu tepla.

1.1. Vytvorenie novej úlohy

1.2. Nastavenie typu a režimu geometrie

1.3. Nastavenie prevádzkových podmienok

1.4. Definícia materiálu

1.5. Definovanie objektu obrobku

1.6. Import geometrie

1.7. Vytvorenie siete

1.8. Priradenie materiálu

1.9. Vytvorenie štruktúrovanej siete

1.10. Definícia BCC

1.11. Meracie body teploty

1.12. Definovanie časových pásiem

1.13. Rozdelenie zón HT

1.14. Vymedzenie zón prenosu tepla

1.15. Definovanie ovládacích prvkov krokov

1.16. Optimalizačné riadenie

1.17. Vytvorenie databázy

1.18. Optimalizácia

1.19. Výsledky optimalizácie

## Vytvorenie novej úlohy

Spustite nový problém v Sprievodcovi inverzným prenosom tepla s ID problému **SIMPLE_INVHEAT**. To môžete urobiť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) a výberom možnosti „**2D inverzný prenos tepla**“, zadajte názov úlohy ako „**SIMPLE_INVHEAT**“ a v poli „Systém jednotiek“ vyberte možnosť „**English**“ v položke „Unit System“ (pozri obr. 2DINVL1.1.). V poli „Location“ môžete vybrať adresár a potom kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoriť sprievodcu inverzným prenosom tepla.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0001.jpg' | relative_url }})

Okno „Nastavenie problému“

## Nastavenie typu a režimu geometrie

Po otvorení sprievodcu 2D Inverse Heat by sa malo zobraziť okno, ako je znázornené na obr. 2DINVL1.2. Nastavte „**Geometry****Type**“ na „**Axisymmetric**“. Ak má používateľ záujem o výpočet transformácií alebo obsahu atómov v dôsledku difúzie, môže zaškrtnúť príslušné políčka na karte „**Mode**“. V tomto laboratórnom cvičení nebudeme zaškrtávať žiadne políčka, pretože budeme počítať iba koeficienty prenosu tepla. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0002.jpg' | relative_url }})

Okno inicializácie

## Nastavenie podmienok procesu

Na tejto stránke môže používateľ nastaviť podmienky prostredia. Ak proces zahŕňa kalenie a prenos tepla, je možné zaškrtnúť príslušné políčka a definovať tak podmienky prostredia. Náš proces zahŕňa iba prenos tepla a teplota prostredia je konštantná, preto zaškrtnite políčko „**Prenos**“ a nastavte teplotu prostredia na 68 °F (pozri obr. 2DINVL1.3.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0003.jpg' | relative_url }})

Nastavenie podmienok procesu

## Definícia materiálu

Na stránke „Zoznam materiálov“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), aby ste vytvorili nový materiál, a premenujte ho na „**Simple**“ kliknutím na pridanú položku „Nový materiál“ (pozri obr. 2DINVL1.4.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali vlastnosti materiálu.

Vyberte kartu **Tepelné vlastnosti** a zadajte hodnotu **0,1** pre **Tepelná******tepelnej vodivosti**, **0,2** pre **tepelnú kapacitu** a **0,3** pre **emissivitu** ako konštantné hodnoty, ako je znázornené na obr. 2DINVL1.5. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Workpiece“.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0004.jpg' | relative_url }})

Vytvorenie nového materiálu

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0005.jpg' | relative_url }})

Definovanie tepelných vlastností materiálov

## Definovanie objektu obrobku

Na stránke obrobku nastavte teplotu objektu na **600** °F, ako je znázornené na obr. 2DINVL1.6. Uistite sa, že typ objektu je **Plast** a že je zaškrtnuté políčko Primárna forma. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku geometrie.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0006.jpg' | relative_url }})

Definícia objektu obrobku

## Import geometrie

Na stránke „Geometria“ kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a importujte súbor s geometriou „**SIMPLE_INVHEAT.IGS**“ z adresára „/2D/LABS“, ako je znázornené na obr. 2DINVL1.7.V predvolenom nastavení bude zaškrtnuté políčko „Zobraziť geometriu vnútri značky“. Ak nie je zaškrtnuté, odškrtnite ho a kliknite na popisok ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste skontrolovali a opravili geometriu, pozri obr. 2DINVL1.7.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0007.jpg' | relative_url }})

Okno Geometria

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím sa otvorí okno na korekciu geometrie, a následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím opustíte stránku korekcie geometrie (pozri obr. 2DINVL1.8). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku vytvárania siete.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0008.jpg' | relative_url }})

Okno „Skontroluj a oprav geometriu“

## Vytvoriť sieť

Keď sa používateľ nachádza na stránke „Mesh“, môže využiť expertný režim na prístup k pokročilým nastaveniam siete. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) na paneli nástrojov prejdite do expertného režimu a potom na karte „**Všeobecné**“ zadajte **100** ako cieľový počet prvkov pre nestruktúrovanú sieť, pozri obr. 2DINVL1.9. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Material“ (Materiál), kde môžete priradiť materiál.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0009.jpg' | relative_url }})

Definovanie nestruktúrovanej siete

## Priradenie materiálu

Zoznamu materiálov vyberte materiál „**Simple**“, ktorý chcete priradiť k obrobku, ako je znázornené na obr. 2DINVL1.10.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0010.jpg' | relative_url }})

Priradenie materiálu

## Vytvorenie štruktúrovanej siete

Štruktúrovaná povrchová sieť prispieva k vyššej presnosti tepelného výpočtu pri kratšom výpočtovom čase. Preto na stránke „Materiál“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}). Použijeme 2 vrstvy štruktúrovanej povrchovej siete s použitím povlakovej siete s hrúbkou **381****mikrónov** a **762****mikrónov** pre vrstvu 1, resp. 2 s materiálom „**Simple**“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 2DINVL1.11. Nepoužívajte tlačidlo „Generate Coating“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) v kontextovom okne „Chcete vygenerovať sieť povlaku?“. Po vygenerovaní siete zväčšite zobrazenie pravého horného rohu a skontrolujte vygenerovanú sieť pre štruktúrované vrstvy. Objekt so sieťou vyzerá tak, ako je znázornené na obr. 2DINVL1.12. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka BCC.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0011.jpg' | relative_url }})

Vytváranie štruktúrovanej siete pomocou metódy „Coating mesh“

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0012.jpg' | relative_url }})

Objekt so sieťou po vytvorení štruktúrovanej siete

## Definícia pojmu BCC

Štandardne sú obrobku priradené BCC „Výmena tepla s okolím“ a osovo symetrické BCC (Vx = 0), čo je možné overiť výberom príslušného BCC zo stromu BCC. V položke „Výmena tepla s okolím“ vyberte BCC „Definované“ a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}), čím odstránite predvolené BCC. Teraz na definovanie BCC „Výmena tepla s prostredím“ vyberte pravý okraj a horný okraj obrobku a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}); priradené BCC sú zobrazené na obr. 2DINVL1.13. Na definovanie symetrie na spodnom okraji vyberte „Rýchlosť“ pod BCC „Deformácia“, potom vyberte smer Y, uistite sa, že hodnota rýchlosti je nula, a potom vyberte spodný okraj a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}); definované BCC sú zobrazené na obr. 2DINVL1.14. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Body merania teploty“.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0013.jpg' | relative_url }})

Definovaná výmena tepla s okolím (BCC)

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0014.jpg' | relative_url }})

Definovaná symetria Bcc

## Meracie body teploty

Na stránke „Body merania teploty“ trikrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_insert_row_icon.jpg' | relative_url }}) a zadajte súradnice (**0,6; 1,0**), (**1,5; 0,5**) a (**0,0, 0,0**) do tabuľky pre body 1, 2 a 3, ako je znázornené na obr. 2DINVL1.15. Údaje o teplotnom priebehu pre každý bod je možné definovať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) v poslednom stĺpci tabuľky. Kliknite na tlačidlo Načítať a načítajte súbor „SIMPLE_INVHEAT_P1_Thermal_History.DAT“ pre bod 1 zo zložky /Labs a kliknite na tlačidlo (pozri obr. 2DINVL1.16.), podobne načítajte súbory SIMPLE_INVHEAT_P2_Thermal_History.DAT a SIMPLE_INVHEAT_P3_Thermal_History.DAT pre bod 2, resp. 3. Tlačidlo „Define“ v poslednom stĺpci tabuľky sa po definovaní údajov o tepelnej histórii pre daný bod zmení na ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_edit_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0015.jpg' | relative_url }})

Stránka „Body merania teploty“

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0016.jpg' | relative_url }})

Okno s údajmi o teplotnom vývoji pre bod 1

## Definovanie časových pásiem

Na stránke „Časové zóny“ môže používateľ definovať časové zóny pre ochladzovanie a presun. Keďže sme sa v tomto laboratórnom cvičení rozhodli simulovať iba presun, je k dispozícii iba definícia časovej zóny pre presun. Chceme simulovať proces trvajúci 10 sekúnd, keďže posledný bod merania teploty, ktorý je k dispozícii z tepelnej histórie, sa nachádza v čase 10 sekúnd. Zadajte teda čas začiatku ako 0 sekúnd a čas konca ako 10 sekúnd. Graf tepelnej histórie všetkých bodov v rámci zadaného času je viditeľný v zobrazovacej oblasti, pozri obr. 2DINVL1.17. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0017.jpg' | relative_url }})

Definícia času prenosu na stránke „Časové pásmo“

## Rozdelenie zóny HT

Na stránke „HT Zone Partitioning“ vidíme, že systém automaticky vygeneroval zóny na základe definovaných teplotných bodov. Zaškrtnite políčko „Display Zone“, aby ste si overili vytvorené zóny. Vidíme, že tieto zóny boli vytvorené bez zohľadnenia symetrie na spodnom okraji a že počiatočné a koncové body zón sa nachádzajú na okrajoch, preto predefinujeme rozdelenie tak, aby sme mohli odstrániť nepotrebné zóny. Už definované zóny odstránime pomocou tlačidla „Delete All“. Predvolene sa celé okraje vonkajšej plochy považujú za jednu zónu. Po odstránení bodov vyberieme tri body proti smeru hodinových ručičiek: pravý dolný roh, pravý horný roh a ľavý horný roh, ako je znázornené na obr. 2DINVL1.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_zone_button.jpg' | relative_url }}) na vytvorenie zón. Zóny sa vytvoria medzi vybranými dvojicami bodov, pozri obr. 2DINVL1.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0018.jpg' | relative_url }})

Okno na rozdelenie zón HT

## Vymedzenie zón prenosu tepla

Na stránke „Zóny prenosu tepla“ vidíme, že sú vytvorené 3 zóny: zóna č. 1 pokrýva pravý okraj, zóna č. 2 pokrýva horný okraj a zóna č. 3 pokrýva spodný symetrický okraj. Zóna č. 3 nie je potrebná, preto ju vyberieme a klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_htz_button.jpg' | relative_url }}), ako je znázornené na obr. 2DINVL1.19.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0019.jpg' | relative_url }})

Odstránenie nežiaducej zóny č. 3

Po odstránení nepotrebnej zóny č. 3 kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_iniitialize_htc_button.jpg' | relative_url }}), aby ste definovali regulačné body a limity; uistite sa, že funkcia HTC je založená na teplote. Systém štandardne pridá niekoľko regulačných bodov; pre účely tohto cvičenia ich odstránime a použijeme štyri body. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_all_button2.jpg' | relative_url }}) a odstráňte všetky riadky okrem 4 riadkov a potom zadajte štyri hodnoty **300**, **400**, **500** a **600**, pozri obr. 2DINVL1.20. Uistite sa, že metóda interpolácie je Lineárna a počiatočný odhad, dolná a horná hranica sú v poriadku. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili okno inicializácie.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0020.jpg' | relative_url }})

Odstránenie nežiaducej zóny č. 3

Nastavenia kontrolných bodov a limitov je možné nastaviť pre každú zónu samostatne pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_edit..._button.jpg' | relative_url }}) vedľa položky „Zone“ na stránke „Heat Transfer Zones“ (Zóny prenosu tepla), pozri obr. 2DINVL1.20. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Step“ (Krok).

## Definovanie ovládacích prvkov krokov

Na stránke „Step“ zmeňte hodnotu „Zmena teploty na jeden krok“ na **5,0** a ostatné hodnoty ponechajte na predvolených hodnotách, ako je znázornené na obr. 2DINVL1. 21. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0021.jpg' | relative_url }})

Definovanie ovládacích prvkov krokov

## Optimalizačné riadenie

Na stránke „Optimization Control“, ako je znázornené na obr. 2DINVL1.22., sú všetky predvolené nastavenia v poriadku, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0022.jpg' | relative_url }})

Okno riadenia optimalizácie

## Vytvorenie databázy

Na stránke „DB Generation“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali nastavenie z hľadiska chýb a varovaní. Ak nie sú žiadne chyby, mala by sa zobraziť správa „Data Valid!“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu.

## Optimalizácia

Po vytvorení databázy prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov a kliknutím na ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) spustite optimalizáciu, pozri obr. 2DINVL1.23. Po dokončení optimalizácie sa na konci súboru protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0023.jpg' | relative_url }})

Optimalizácia behu

## Výsledky optimalizácie

Ak chcete zobraziť výsledky optimalizácie, prepnite do režimu „Post“ kliknutím na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). Na stránke „Nástroje“ v časti „Nástroje“ uvidíte dve ikony (pozri obr. 2DINVL1.24.),

![]({{ '/assets/icons/pre_icons/mo_inverse_heat_optimal_htc.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Zobrazenie optimalizovaných hodnôt HTC.

![]({{ '/assets/icons/pre_icons/mo_inverse_heat_local_objective_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Zobrazenie simulovaných hodnôt teploty v bodoch merania teploty.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0024.jpg' | relative_url }})

Nástroje príspevku na zobrazenie výsledkov optimalizácie

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_optimal_htc.jpg' | relative_url }}) zobrazíte optimalizované hodnoty HTC pre každú zónu; otvorí sa okno „Heat Transfer Zone“ (Zóna prenosu tepla), ako je znázornené na obr. 2DINVL1.25. Vyberte každú zónu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_thermal_icon.jpg' | relative_url }}), aby ste si prezreli optimalizované hodnoty HTC; optimalizované hodnoty HTC pre zónu č. 1 nájdete na obr. 2DINVL1.26.

Pomocou ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) je možné zobraziť históriu objektívnych hodnôt, pozri obr. 2DINVL1.27.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0025.jpg' | relative_url }})

Okno „Zóny prenosu tepla“ na karte „Príspevok“

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0026.jpg' | relative_url }})

Optimalizované hodnoty HTC pre zónu č. 1

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0027.jpg' | relative_url }})

Cieľ Hodnota História

Výsledok lokálnej optimalizácie je možné zobraziť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_local_objective_button.jpg' | relative_url }}); poskytuje porovnanie medzi experimentálnymi a simulovanými hodnotami teploty pri použití optimalizovaných hodnôt koeficientu prenosu tepla. Tieto hodnoty je možné v prípade potreby uložiť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) (pozri obr. 2DINVL1.28.). Používateľ môže vybrať bod (pozri obr. 28) a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_thermal_icon.jpg' | relative_url }}), aby sa zobrazil graf porovnania medzi experimentálnymi a simulovanými hodnotami teploty, alebo na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_all_button.jpg' | relative_url }}), aby sa zobrazil graf pre všetky hodnoty, obr. 2DINVL1.29. ukazuje porovnanie medzi experimentálnymi a simulovanými hodnotami teploty pre bod 1.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0028.jpg' | relative_url }})

Miesta merania teploty v stĺpe

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0029.jpg' | relative_url }})

Výsledok lokálnej optimalizácie pre bod 1
