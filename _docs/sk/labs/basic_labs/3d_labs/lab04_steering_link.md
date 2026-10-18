---
lang: sk
title: "Lab04 – riadiaca tyč"
---

# Laboratórna práca č. 4. Riadiaci čap

  
4.1. Úvod

4.2. Vytvorenie novej úlohy

4.3. Pridávanie operácií a objektov

4.4. Definovanie obrobku

4.5. Definovanie hornej matrice

4.6. Definovanie spodnej matrice

4.7. Umiestňovanie objektov

4.8. Priradenie vzťahu medzi objektmi

4.9. Priradenie ovládacích prvkov na zastavenie

4.10. Ovládacie prvky krokov

4.11. Vytvorenie databázy

4.12. Následné spracovanie

## Úvod

Nemecké združenie kováčskeho priemyslu (Industrieverband Deutscher Schmieden, IDS) organizuje pravidelné porovnávacie testy simulačných kódov pre kovanie. Ide o skutočné priemyselné diely, pri ktorých sú k dispozícii všetky procesné údaje na zverejnenie.

V tomto cvičení a v nasledujúcom cvičení sa na ilustráciu reálnej konfigurácie úlohy použijú dve časti z benchmarku z roku 1999. V závislosti od hardvéru a nastavení systému bude riešenie týchto úloh trvať od niekoľkých hodín až po jeden alebo dva dni. Jedným z kľúčových faktorov pri optimalizácii výkonu simulácie je definícia siete, ktorej sa budeme podrobne venovať neskôr v rámci tohto cvičenia.

Presná simulácia procesu kovania kladivom si vyžaduje nadpriemerné množstvo údajov o lisovacom stroji a určitú dodatočnú námahu pri nastavení a spustení simulácie.

## Vytvorenie nového problému

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu **Nový problém**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. V poli jednotiek vyberte radiacie tlačidlo „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte radiacie tlačidlo „**SI**“. Názov úlohy zadajte ako „**Steering_Link**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak toto políčko nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca MO a v tomto momente bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**Steering_Link**“.

Používateľ môže tiež zmeniť systém jednotiek a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka. Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nový projekt. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

##  Pridávanie operácií a objektov

Pridajte operáciu 3D tvarovanie zo zoznamu operácií v prehliadači. Operáciu pridáte kliknutím na tlačidlo 3D tvarovanie ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Objekty. 

Na stránke „Objekty“ sa štandardne pridajú 3 objekty, ak ich nepridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}); pridajte tri objekty tak, ako je znázornené na obr. 3DL4.1. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0001.jpg' | relative_url }})

Pridávanie objektov

## Definovanie obrobku

### Nastavenie teploty obrobku

Na stránke „Obrobok“ zadajte teplotu obrobku **1300** °C, ako je znázornené na obr. 3DL4.2. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0002.jpg' | relative_url }})

Nastavenie teploty pre obrobok

### Import geometrie

Na stránke Geometria kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **ids_link_billet.stl** z inštalačného priečinka DEFORM, konkrétne z adresára \3d\LABS. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. V okne „Display“ (Zobrazenie) sa zobrazí vyskakovacie okno na kontrolu geometrie, ako je znázornené na obr. 3DL4.3. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0003.jpg' | relative_url }})

Okno na kontrolu geometrie

### Definovanie siete obrobku

Zo všetkých nastavení simulácie má sieť obrobku najväčší vplyv na presnosť a rýchlosť simulácie. Hrubá sieť umožní extrémne vysokú rýchlosť simulácie, rozlíšenie povrchu však bude nízke. Väčší počet prvkov siete zlepší rozlíšenie povrchu, avšak na úkor dĺžky simulácie.

Vo všeobecnosti sa nezachytia prvky a chyby, ktorých veľkosť je rovnaká alebo menšia ako veľkosť prvku.

DEFORM® ponúka dve možnosti popisu [mesh]({{ '/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/' | relative_url }}):

**Absolútna sieť** umožňuje používateľovi určiť rozlíšenie siete. Celkový počet prvkov siete určí systém, rozlíšenie však zostane konštantné.

**Relatívna sieť** umožňuje používateľovi určiť celkový počet objemových prvkov. Počet objemových prvkov zostane relatívne konštantný, pričom rozlíšenie povrchu sa bude v priebehu simulácie meniť.

Vo všeobecnosti poskytuje absolútna sieť lepší výkon, pretože pri danom rozlíšení simulácia spočiatku používa menej prvkov a podľa potreby pridáva ďalšie prvky, aby sa zachovalo rozlíšenie. Oba typy sietí ponúkajú adaptívne automatické zjemňovanie siete – v oblastiach, kde je potrebné vyššie rozlíšenie, sa používajú jemnejšie prvky.

### Definícia hustoty siete pre vysoké rozlíšenie

Definícia siete sa zvyčajne zakladá na rozmeroch prvkov v nástroji. V prípade tejto súčiastky sú kritickými prvkami polomery prechodu vedúce z dříku do otvorov a zaoblenia vedúce do polomeru prebytku materiálu. Tieto zaoblenia majú veľkosť približne 2 mm. Na ich spracovanie by minimálna veľkosť prvku mala byť približne ½ tejto hodnoty, teda 1 mm.

Zmeňte režim nastavenia preprocesora na „Expert“ pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do režimu Expert) na paneli nástrojov. Na stránke „Mesh“ (Sieť) vyberte prepínač „absolute mesh“ (absolútna sieť), ako parametre siete pre obrobok by mala byť zadaná **Minimálna veľkosť prvku** **1** mm a **Pomer veľkostí** **3**, ako je znázornené na obr. 3DL4.4.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0004.jpg' | relative_url }})

Okno „Všeobecné nastavenia siete“

Váhovacie parametre určujú relatívny vplyv zakrivenia povrchu, deformácie, rýchlosti deformácie a teplotného gradientu na definíciu siete. Vyššie váhy pre zakrivenie zabezpečia lepšie rozlíšenie **hraníc**. Zmeňte váhy na približne **0,9** pre **Zakrivenie povrchu** a na **0,1** pre **Deformáciu** aj **Rýchlosť deformácie**, ako je znázornené na obr. 3DL4.5.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0005.jpg' | relative_url }})

Okno „Váhovacie koeficienty siete“

Najskôr vygenerujte súbor ![]({{ '/assets/icons/pre_icons/mo_surface_mesh_button.jpg' | relative_url }}) a potom súbor ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) pre polotovar. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}) otvoríte okno s predvolenými okrajovými podmienkami. Vygeneruje sa sieť s približne 76 000 objemovými prvkami. Pri každom prepočítaní siete sa zachovajú definované absolútne nastavenia siete, takže celkový počet prvkov sa bude zvyšovať s rastúcou geometrickou zložitosťou obrobku.

### Import údajov o materiáloch

V okne „Materiál“ vyberte kategóriu **oceľ** a načítajte materiál **DIN41Cr4** pomocou možnosti „Načítať údaje o materiáli z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})“, ako je znázornené na obr. 3DL4.6.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0006.jpg' | relative_url }})

Okno „Materiál“

Po načítaní údajov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) – otvorí sa okno „Materiál“. V tomto okne si môžete prezrieť tepelné a plastické vlastnosti kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) vedľa každej z vlastností. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Priradenie okrajových podmienok

Modeluje sa iba polovica riadiaceho ramena. Aby sme zabezpečili symetriu, musíme definovať okrajovú podmienku **roviny symetrie** pre **koniec** dielu v smere **+X**, ako je znázornené na obr. 3DL4.7, a okrajovú podmienku výmeny tepla s okolím pre všetky povrchy okrem konca dielu +X, ako je znázornené na obr. 3DL4.8., a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno Vlastnosti.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0007.jpg' | relative_url }})

Definícia symetrie BCC

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0008.jpg' | relative_url }})

Výmena tepla s okolím – definícia podľa BCC

### Aktivácia kompenzácie hlasitosti

Na stránke vlastností kliknite na tlačidlo **Deformácia** a nastavte **Cieľový objem** na hodnotu **Aktívny v FEM + vytváranie siete**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) vypočítajte objem siete a geometrie obrobku. Obvykle je objem siete o niečo menší ako objem geometrie. Ak ako cieľový objem použijete objem geometrie, program DEFORM® bude postupne zvyšovať objem obrobku späť na cieľovú hodnotu. Ak ako cieľový objem použijete objem siete, program DEFORM® bude udržiavať konštantný objem.

Ak budete vyzvaní, nastavte ako cieľový objem geometrický objem kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), ako je znázornené na obr. 3DL4.9.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0009.jpg' | relative_url }})

Vyskakovacie okno s cieľovým objemom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top Die“

## Definovanie hornej matrice

###  Nastaviť teplotu

Na stránke „Top Die“ nastavte teplotu pre „Top Die“ na **90** °C, ako je znázornené na obr. 3DL4.10. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0010.jpg' | relative_url }})

Nastavenie maximálnej teploty matrice

### Import geometrie

Na stránke „Geometria“ kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **Ids_link_top.stl** z inštalačného priečinka programu DEFORM, konkrétne z adresára \3D\LABS. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Pohyb“.

### Priradiť pohyb

Pre zjednodušenú simuláciu nastavíme konštantnú rýchlosť hornej matrice **150** mm/s v smere **-Z** (pozri obr. 3DL4.11.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Spodná matrica“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0011.jpg' | relative_url }})

Okno riadenia pohybu

## Definícia spodnej formy

### Nastaviť teplotu

Na stránke „Spodná forma“ nastavte teplotu spodnej formy na **90** °C, ako je znázornené na obr. 3DL4.12. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku s geometriou.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0012.jpg' | relative_url }})

Nastavenie teploty spodnej matrice

### Import geometrie

Na stránke Geometria kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **ids_link_bottom.stl** z inštalačného priečinka programu DEFORM, konkrétne z adresára \3D\LABS. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Positioning“ (Polohovanie).

## Umiestňovanie objektov

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) a vyberte voľbu ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **Top Die** a referenčný bod na **Workpiece**. Zmeňte smer priblíženia na **-Z** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

Znovu vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **Spodná časť****Matrica** a referenčný bod na obrobok. Zmeňte smer priblíženia na **Z** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka s kontaktmi.

## Priradenie vzťahov medzi objektmi

V okne „Kontakt“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}); pridajú sa predvolené vzťahy, ako je znázornené na obr. 3DL4.13.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0013.jpg' | relative_url }})

Okno medzi objektmi s predvolenými vzťahmi

Obrobok by mal byť podriadený obom formám. Použite hodnotu trenia **0,3** (typickú pre tvárnenie za tepla) a koeficient prenosu tepla na rozhraní **5** (typický pre jednotky SI, keď formy nie sú v zábere). Nezabudnite vytvoriť kontaktné okrajové podmienky.

Zvýraznite prvý vzťah v tabuľke a kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Na karte **Deformácia** použite roletové menu „Trenie“ a zo zoznamu vyberte položku **Kovanie za tepla (s mazaním)**, ako je znázornené na obrázku [Fig. 3DL3.47]({{ '/docs/sk/labs/basic_labs/3d_labs/lab03_spike_forging/' | relative_url }}#Fig_3DL3_47_Inter-Object_Data_Deformation_definition_Window), a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

Vyberte kartu **Thermal** a zadajte **koeficient prenosu tepla medzi fázami** s hodnotou **5** (typická hodnota pre jednotky SI, ak nie sú čipy modelované ako sieť), ako je znázornené na obr. 3DL4.14. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0014.jpg' | relative_url }})

Okno „Definícia teplotných údajov“

V okne „Kontakt“ kliknite na položku ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste zmenili nastavenia ostatných vzťahov tak, ako je znázornené na obr. 3DL4.15.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0015.jpg' | relative_url }})

Okno medzi objektmi

Pomocou ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určite vhodnú toleranciu kontaktov a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktov. Kontakt sa vytvorí medzi polotovarom a hornou aj spodnou matricou. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Priradenie ovládacích prvkov na zastavenie

Prepnite do režimu „Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})“, vyberte ikonu ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}); v okne displeja sa zobrazí vyskakovacie okno so správou; zrušte zaškrtnutie políčka „obrobok“ v tomto vyskakovacom okne, ako je znázornené na obr. 3DL4.16.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0016.jpg' | relative_url }})

Režim užívateľsky definovaných objektov

V okne „Stopping Controls“ zaškrtnite políčko „Distance between Objects“. Pre objekt 1 vyberte **Horná matrica** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}). Vyberte bod na spodnej strane hornej matrice. Pre objekt 2 vyberte **Spodná matrica** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}). Vyberte bod na hornej strane spodnej matrice. Program vypočíta vzdialenosť a zobrazí ju v okne „Display“. Ako kritérium zastavenia zadajte **Z****Distance** s hodnotou **11,0** mm, ako je znázornené na obr. 3DL4.17. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0017.jpg' | relative_url }})

Okno „Ovládacie prvky zastavenia“

## Ovládacie prvky krokov

Celkový zdvih bude približne 40 mm. Pre zložitú operáciu blesku je primeraný počet 200 časových krokov. Voľba tohto čísla nie je kritická, pretože nastavenia podkrokov budú riadiť skutočnú veľkosť kroku použitú vo výpočtoch deformácie. V okne „Step controls“ (Ovládacie prvky krokov) zmeňte režim nastavenia preprocesora na „Expert“ (Odborný) pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do odborného režimu) na paneli nástrojov.

V nastaveniach krokov vyberte ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) a nastavte **Počet simulačných krokov** na **200** a **krok****prírastok****na****uloženie****10** krokov. Nastavte **hornú maticu** ako **primárnu maticu**. (Pozri obr. 3DL4.18.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0018.jpg' | relative_url }})

Okno „Kroky“

Vyberte ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) a nastavte hodnotu zdvihu/kroku na **0,2** mm/krok, ako je znázornené v [Fig. 3DL4.19.]({{ '/docs/sk/labs/basic_labs/3d_labs/lab03_spike_forging/' | relative_url }}#Fig_3DL3_19_Heat_Transfer_type_selection_page)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0019.jpg' | relative_url }})

Okno „Ovládacie prvky krokov“

## Vytvorenie databázy

Uložte súbor s kľúčovými slovami pre danú úlohu tak, že v ponuke **Súbor** vyberiete možnosť **Exportovať**.

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), aby sa otvorilo dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať v spúšťaní**, vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

## Následné spracovanie

Po dokončení simulácie si výsledky prezrite tak, že prejdete do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov Simulácia.

Prejdite jednotlivými krokmi a vyneste do grafu premenné teploty, efektívneho napätia, poškodenia a efektívneho deformácie. (Pozri obr. 3DL4.20 a obr. 3DL4.21.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0020.jpg' | relative_url }})

Graf premennej stavu poškodenia

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0021.jpg' | relative_url }})

Graf premennej efektívneho stavu pri napätí

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}). Keď sa zobrazí okno GRAPH, vyberte iba položku „Top Die“; os X sa nastaví na **Stroke** a os Y na **Z Load**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a nad objektmi v okne DISPLAY sa zobrazí priehľadná krivka zaťaženia a zdvihu, ako je znázornené na obr. 3DL4.22.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0022.jpg' | relative_url }})

Graf zdvihu zaťaženia

**Zobrazenie plnenia formy:**

V postprocesore existuje niekoľko spôsobov vyhodnotenia vyplnenia formy.

Uzly, ktoré sú v kontakte s formami, je možné zobraziť tak, že v strome objektov označíte obrobok a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) zobrazíte kontakt. Oblasti, ktoré nie sú vyplnené, možno rozpoznať podľa chýbajúceho kontaktu. Zobrazenie dielu v rôznych krokoch umožňuje sledovať vývoj kontaktu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0023.jpg' | relative_url }})

Zobrazenie oblasti výplne formy
