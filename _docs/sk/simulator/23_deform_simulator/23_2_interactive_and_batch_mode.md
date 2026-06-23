---
lang: sk
title: "23.2. Interaktívny a dávkový režim"
---

# 23.2. Interaktívny a dávkový režim

23.2.1. Interaktívny režim

23.2.2. Režim fronty dávok

23.2.3. Simulácie čakania v rade

  * Spustenie servera fronty dávok a simulačného servera

  * Požiadavky na konfiguráciu počítača

  * Nastavenie simulačného servera

23.2.4. Funkcie dialógového okna „Run Options“

## Interaktívny režim

Ak sa má simulovať séria úloh, po dokončení predchádzajúcej simulácie pomocou možnosti „Run“ v integrovanom grafickom rozhraní alebo v dialógovom okne „Run options“ je možné použiť ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na interaktívne odosielanie simulácií jedna po druhej.

## Režim fronty úloh

Interaktívne odosielanie simulácií si vyžaduje, aby používateľ dohliadal na spúšťanie simulácií jedna po druhej; používateľ však môže využiť voľbu ![]({{ '/assets/icons/simulator_icons/gui_add_to_queue.jpg' | relative_url }}) v grafickom rozhraní alebo v dialógovom okne „Run options“ (![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }})), aby sa jednotlivé úlohy spúšťali automaticky jedna po druhej alebo súčasne, a to v závislosti od nastavení simulačného servera.

Stav behu úlohy je možné sledovať v nástroji Process Monitor; ďalšie možnosti týkajúce sa vykonávania simulácií v interaktívnom a dávkovom režime nájdete v kapitole [23.4. Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/).

Od verzie 11.0 môžu používatelia odosielať úlohy na simuláciu pomocou vzdialených simulačných serverov v dávkovom režime z dialógového okna „Run options“ (Možnosti spustenia). (Pozri časť [6.2. MO Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/).) Týmto spôsobom sa úlohy dočasne presunú na vzdialený simulačný server na účely simulácie; po dokončení simulácie sa projekt skopíruje späť, čím sa zníži zaťaženie lokálneho počítača.

## Simulácie čakania v rade

**Spustenie servera fronty dávok a simulačného servera**

****  
(Informácie o nastavení, simulačných serveroch, serveroch fronty dávkových úloh a správe priradených diskov v sieti na spúšťanie simulácií DEFORM nájdete v dokumente [Chapter 23.6. Running Shared folder Simulations](/docs/en/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/))

(Inštalácia týchto služieb – Batch Queue a Simulation Server – je súčasťou štandardného inštalačného procesu a informácie uvedené v tomto texte slúžia iba ako alternatívne možnosti v prípade, že daný systém má nejaké problémy alebo obmedzenia pri spracovaní týchto služieb)

Ak chcete úlohy zaradiť do fronty alebo spustiť na inom počítači, nainštalujte si prosím simulačný server.

Inštalácia je jednoduchá, stačí spustiť priložené dávkové súbory (v inštalačnom adresári DEFORM):

  * InstallBatchQueueServer.bat (príklad cesty na počítači: C:\Program Files\SFTC\License Manager\\)

  * InstallSimulationServer.bat (príklad cesty na počítači: C:\Program Files\SFTC\DEFORM\Configuration\\)

Potom sa aj tieto dva programy zaregistrujú ako služby, rovnako ako správca licencií. Spustia sa automaticky.

**Požiadavky na konfiguráciu počítača**

****

  * **Si******m**ulačný server**: Centrálny počítač – pravdepodobne s vysokým výkonom – určený na vykonávanie výpočtov metódou konečných prvkov (FEM).

  * **Licenčný server**: Centrálny počítač – nemusí byť nutne veľmi výkonný – slúžiaci na správu licencií.

  * **Server fronty dávkových úloh**: Centrálny počítač na riadenie poradia spúšťania úloh. Licenčný server a server fronty dávkových úloh budú bežať na tom istom počítači, zatiaľ čo simulačný server musí bežať na počítačoch, z ktorých používatelia odosielajú úlohy do fronty.

  * **Pre / Post klient(i)** : Počítač, na ktorom budú používatelia vykonávať predspracovanie a následné spracovanie simulácií. Na tomto počítači sa spúšťajú programy na predspracovanie a následné spracovanie.

  * **Umiestnenie súborov databázy**: Súbory databázy by mali byť umiestnené na zdieľanom sieťovom disku, ku ktorému majú prístup simulačný server aj klientsky počítač používaný pred a po simulácii. Pre optimálny výkon simulácie by mali byť súbory databázy umiestnené na pevnom disku fyzicky integrovanom do simulačného servera. Inými slovami, ak bude simulačný server nútený pristupovať k databáze cez sieť, pravdepodobne to spôsobí predĺženie doby behu simulácie.

**Nastavenie simulačného servera**  
Na karte „Simulačný server“ zadajte názov zdieľaného priečinka alebo IP adresu počítača, na ktorom beží simulačný server. Ak ide o počítač s viacerými procesormi alebo viacerými jadrami, zadajte počet procesorov (jadier), ktoré sú k dispozícii a licencované v programe DEFORM (Počet procesorov), a maximálny počet úloh (zvyčajne 1). Používateľ môže ako server pre simuláciu a frontu úloh použiť iný počítač ako lokálny, a to jeho nastavením v programe DEFORM (pozri obr. 23.2.1.).

![]({{ '/assets/images/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/image001.jpg' | relative_url }})

Nastavenie DEFORM – okno Simulačný server

**Nastavenia spustenia (možnosti)**  
Po konfigurácii prosím použite nastavenia ![]({{ '/assets/icons/simulator_icons/gui_run_options_button.jpg' | relative_url }}) v hlavnom okne grafického rozhrania (GUI), ak chcete využívať frontu dávok a simulačný server.

**Ako pridať úlohy do fronty:**

Vyberte databázu v hlavnom okne grafického rozhrania (z pracovného priečinka).

V hlavnom okne grafického rozhrania otvorte ![]({{ '/assets/icons/simulator_icons/gui_run_options_button.jpg' | relative_url }}).

Počiatočné údaje sa zvyčajne preberajú z údajov získaných pri spustení programu DEFORMSetup.

Stav fronty dávkových úloh na príslušných serveroch skontrolujte pomocou tlačidla „Check Server![]({{ '/assets/icons/simulator_icons/mo_check_server_button.jpg' | relative_url }})“.

V tomto dialógovom okne kliknite na ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}), aby ste úlohu „job1“ pridali do fronty.

Vyberte úlohu 2, kliknite na položku ![]({{ '/assets/icons/simulator_icons/gui_add_to_queue.jpg' | relative_url }}) v časti „Simulator“ na hlavnej obrazovke grafického rozhrania a rovnaký postup zopakujte pre zostávajúce úlohy 3 a 4 (pozri obr. 23.2.2.).

![]({{ '/assets/images/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/image002.jpg' | relative_url }})

Simulácie čakania v rade z možností spustenia

Úlohy pridané do fronty je možné vidieť v okne programu Process Monitor v zozname „Running“ a „Pending“.

Akonáhle je úloha dokončená, odstráni sa zo zoznamu fronty dávok a spustí sa ďalšia čakajúca úloha.

Používateľ môže zmeniť pozíciu úlohy pomocou tlačidiel „Presunúť nahor“ (![]({{ '/assets/icons/simulator_icons/move_up_button.jpg' | relative_url }})) a „Presunúť nadol“ (![]({{ '/assets/icons/simulator_icons/move_down_button.jpg' | relative_url }})) a úlohu je možné odstrániť z fronty pomocou tlačidla „Ukončiť alebo odstrániť“ (![]({{ '/assets/icons/simulator_icons/mo_kill_button.jpg' | relative_url }})). (Pozri obr. 23.4.2)

## **Funkcie dialógového okna „Run Options“******

![]({{ '/assets/icons/simulator_icons/run_option_icon.jpg' | relative_url }}) alebo ponuka Simulácia > Spustiť (možnosti) ![]({{ '/assets/icons/simulator_icons/gui_run_options_button.jpg' | relative_url }}) ponúka pokročilejšie možnosti spustenia simulácie, ako napríklad interaktívny alebo dávkový režim, spustenie s jedným alebo viacerými (len v 3D) procesormi a 32-bitové alebo 64-bitové spustenie.

  * **Typ úlohy**: Uvádza typ spustených úloh, ako napríklad MO (viacnásobné operácie), DOE (návrh experimentov) alebo OPT (optimalizácia).

  * **Názov databázy/ID problému**: V prípade projektov s bežnými operáciami MO sa tu zobrazuje názov aktuálnej projektovej databázy. V prípade projektov DOE a OPT sa tu ako názov projektu DOE/OPT zobrazuje ID problému; databázy potrebné na dokončenie štúdie DOE/OPT sa vygenerujú po odoslaní problému na simuláciu.

  * **Zadala** : Zobrazí sa názov počítača, na ktorom sa projekt nachádza.

  * **Heslo na ukončenie úlohy**: Ak používateľ na simulacom serveri v prostredí DEFORM použil na ochranu simulácie nejaké heslo, je potrebné toto heslo zadať práve tu pred výberom tlačidiel ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) na spustenie simulácie.

  * **Súbežné úlohy**: Používateľ môže určiť počet simulácií alebo úloh, ktoré sa môžu spúšťať súbežne, pričom tento počet by mal byť rovnaký alebo menší ako maximálny počet úloh špecifikovaný v DEFORMSetup a mal by tiež zodpovedať dostupnej licencii. Táto možnosť je k dispozícii iba pri odosielaní úloh typu DOE/OPT do fronty.

  * **Simulačný režim**: Existujú dva simulačné režimy, a to:

  
![]({{ '/assets/icons/simulator_icons/mo_interactive_mode_rb.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ spúšťať simulácie bez simulačného servera kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}). Táto možnosť nevyžaduje, aby bol simulačný server spustený. (Pozri obr. 23.2.3.) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image003.jpg' | relative_url }})

Spustiť okno s voľbami pre úlohu MO v interaktívnom simulačnom režime

  
Nastavenia interaktívneho simulačného režimu sú nasledovné:

**Názov počítača:** Tu sa zobrazí názov počítača

**Typ**: Tu sa zobrazí, či ide o simuláciu s jedným alebo viacerými procesormi

**Cesta v počítači:** Tu sa zobrazí cesta k databáze a v prípade programov DOE/OPT sa tu uvádza cesta, kam sa budú databázy generovať.

**Počet procesorov na úlohu:** Pomocou tejto možnosti môže používateľ zvoliť počet procesorov, ktoré sa majú použiť na jednu úlohu počas simulácie; táto možnosť je v súčasnosti k dispozícii iba pre 3D simulácie alebo úlohy.

**Veľkosť zdieľanej pamäte:** Zobrazuje veľkosť zdieľanej pamäte alokovanej v systéme simulačného servera pre simuláciu DEFORM.

Používateľ môže nastavenia uložiť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) a okno „Run options“ zatvoriť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_close_button.jpg' | relative_url }}).

![]({{ '/assets/icons/simulator_icons/mo_batch_mode_rb.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ spúšťať simulácie iba v dávkovom režime (pozri obr. 23.2.4.). Na simuláciu problémov s dávkovou frontou je nevyhnutné vybrať niektorý z uvedených dostupných simulačných serverov alebo prvý dostupný simulačný server a kliknúť na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}), čím sa začne pridávanie úlohy do fronty. Zobrazený zoznam obsahuje iba simulačné servery, ktoré sú pridané do nastavení programu DEFORM.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image004.jpg' | relative_url }})

Spustiť okno s voľbami pre úlohu MO v režime dávkovej simulácie

  
V režime hromadnej simulácie je možné nastaviť parametre vybraných simulačných serverov tak, že vyberiete konkrétny simulačný server a kliknete na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}). (Pozri obr. 23.2.5.)

![]({{ '/assets/icons/simulator_icons/mo_server_settings_button.jpg' | relative_url }}): Pomocou tohto tlačidla môže používateľ nastaviť vybrané parametre simulačného servera, ako napríklad počet procesorov, ktoré sa majú využiť na jednu úlohu počas simulácie, a zdieľanú pamäť.

**Názov servera**: Zobrazí sa názov vybraného simulačného servera

**Typ**: Tu sa zobrazí, či ide o simuláciu s jedným alebo viacerými procesormi

**Cesta na serveri**: Tu sa zobrazí cesta k databáze, ak používateľ zvolil lokálny počítač  
ako simulačný server, inak sa zobrazí ako „Kopírované z: <Phisical_DB_existing_Machine_name>“

**Počet procesorov na úlohu**: Pomocou tejto možnosti môže používateľ zvoliť počet procesorov, ktoré sa majú použiť  
na jednu 3D simuláciu alebo úlohu.

**Veľkosť zdieľanej pamäte:** Zobrazuje veľkosť zdieľanej pamäte pridelenú na simulačnom serveri  
systém na simuláciu DEFORM.

  
Používateľ môže nastavenia uložiť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) a okno „Možnosti spustenia“ zatvoriť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_close_button.jpg' | relative_url }}).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image005.jpg' | relative_url }})

Nastavenia servera v režime hromadnej simulácie

  
**Typy spustenia simulácie:** V prípade bežného projektu s viacerými operáciami, či už v interaktívnom alebo dávkovom režime, môže používateľ spustiť simuláciu od počiatočného kroku, alebo ak bola simulácia v priebehu zastavená, prípadne ak ju chce používateľ reštartovať z daného bodu, môže tak urobiť pomocou možností pokračovania. (Pozri obr. 23.2.6.)

**Prvé spustenie:** Týmto sa simulácia spustí od prvého kroku začiatku operácie. Túto možnosť môže používateľ využiť aj na opätovné spustenie simulácie od začiatku v prípade, že sa simulácia v priebehu prerušila kvôli problémom s licenciou alebo sieťou.

**Pokračovanie v hre:** Toto pokračovanie v hre ponúka dve možnosti, a to: 

  * **Pokračovať od posledného kroku:** Týmto sa simulácia pokračuje od posledného dostupného negatívneho kroku. Je to užitočné v prípade, ak používateľ vykonal nejaké úpravy nastavení a chce simuláciu obnoviť z ľubovoľnej fázy.
  * **Spustiť simuláciu od vybraného bodu:** Týmto sa simulácia spustí od ktoréhokoľvek bodu v rámci simulácie priebežných operácií – stačí vybrať príslušnú operáciu a jej simuláciu.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image006.jpg' | relative_url }})

Typy simulačných behov z možností spustenia pre bežné projekty

**Súvisiace témy:**

[23.3 Simulation Graphics](/docs/en/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/)

[23.5. Setting up MPICH](/docs/en/simulator/23_deform_simulator/23_5_setting_up_mpich/)

[23.8. Trouble Shooting Simulation Running](/docs/en/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/)

[Pre-Processor](/docs/en/post_processor/post_processor_mainpg/)

[Integrated Manufacturing Process (MO)](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_integrated_manufacturing_process_layout/)

[Post -Processor](/docs/en/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)
