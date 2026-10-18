---
lang: sk
title: "Laboratórium 3D sprievodcu tepelným spracovaním"
---

# Laboratórium 3D sprievodcu tepelným spracovaním

1.1. Úvod

1.2. Vytvorenie novej úlohy

1.3. Nastavenia procesu

1.4. Definícia pojmu „materiál“

1.5. Typ objektu obrobku

1.6. Inicializácia obrobku

1.7. Definícia pojmu „stredný“

1.8. Definícia pojmu „plánovaný“

1.9. Ovládacie prvky simulácie

1.10. Vytvorenie databázy

1.11. Spustenie simulácie

1.12. Následné spracovanie

## Úvod

Sprievodca tepelným spracovaním je praktický nástroj na nastavenie zložitých úloh tepelných procesov pozostávajúcich z viacerých operácií. V tomto laboratórnom cvičení si ukážeme, ako pomocou tohto sprievodcu pripraviť simuláciu nauhličovania, kalenia a popúšťania oceľového dielu. Toto laboratórne cvičenie môže používateľom pomôcť pochopiť možnosti schémy výpočtu fázových prechodov v programe DEFORM-HT.

## Vytvorenie novej úlohy

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené nižšie (pozri obr. 3DHTWL1.1.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DHTWL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek vyberte „**SI**“ pomocou prepínača. Názov úlohy zadajte ako „**GearHT**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca integrovaným výrobným procesom (pozri obr. 3DHTWL1.3.), v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a nadpisu. V tomto cvičení použijeme ako názov projektu „**GearHT**“.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0003.jpg' | relative_url }})

Sprievodca MO – Nový projekt

Používateľ môže tiež zmeniť systém jednotiek (systém jednotiek vybraný v ponuke Súbor sa nastaví ako predvolený) a pridať operáciu HT jej výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. 3DHTWL1.3.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

Otvorí sa sprievodca viacerými operáciami. Zo zoznamu operácií v Průzkumníku pridajte operáciu 3D HT Wizard. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky **3D HT Wizard** alebo ju môžete pridať aj pretiahnutím do Editoru operácií (pozri obr. 3DHTWL1.4.).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0004.jpg' | relative_url }})

Do Editoru operácií bol pridaný sprievodca 3D HT

## Nastavenia procesu

Po pridaní operácie sa otvorí stránka „Nastavenia procesu“, ako je znázornené na obr. 3DHTWL1.4. Používateľ môže nastaviť režim simulácie podľa požiadaviek simulácie spolu s ovládacími prvkami na definovanie krokov.

Zapnite možnosti „**Deformácia**“, „**Difúzia**“ a „**Fázová transformácia**“. Definícia kroku sa nastaví na stránke Ovládacie prvky simulácie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), ponechajte nastavenia na stránke inicializácie bez zmien (pozri obr. 3DHTWL1.5.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0005.jpg' | relative_url }})

Okno nastavení inicializácie

## Definícia materiálu

Na stránke „Materiál“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať materiál zo súboru) a importujte materiál „**Demo_Temper_Steel.KEY**“ z inštalačnej cesty do adresára \SFTC\DEFORM\v*_*\3d\LABS (pozri obr. 3DHTWL1.6.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte kontextové okno výberu materiálu, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostanete na stránku objektu obrobku.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0006.jpg' | relative_url }})

Import materiálu

## Typ objektu obrobku

Na stránke „Workpiece“ (Obrobok) zmeňte typ objektu na **Elasto-plastic** a z roletového menu vyberte ako typ prvku pre elasto-plastický materiál možnosť „**Mixed (Tet mesh)**“ (pozri obr. 3DHTWL1.7.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Geometria.

**Poznámka**: Pre takmer všetky modely 3D tepelného spracovania by sa mali používať prvky typu (Tet Mesh) alebo „brick mesh“, nie však „štandardné“ tet-prvky.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0007.jpg' | relative_url }})

Stránka objektu obrobku

### Import geometrie

Na stránke Geometria kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (importovať geometriu z knižnice) a importujte súbor **GearTooth.STL** z inštalačnej cesty \SFTC\DEFORM\v*_*\3d\LABS, ako je znázornené na obr. 3DHTWL1.8. Pomocou akcie ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Pri správnej geometrii by sa mala zobraziť správa, ako je znázornené na obr. 3DHTWL1.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0008.jpg' | relative_url }})

Import geometrie

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0009.jpg' | relative_url }})

Skontrolujte geometriu

### Vytvoriť sieť

Na stránke „Mesh“ zadajte cieľový počet prvkov siete ako **16000** alebo posuňte posuvník na hodnotu 16000 a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Sieť sa vygeneruje a objekt so sieťou vyzerá tak, ako je znázornené na obr. 3DHTWL1.10. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0010.jpg' | relative_url }})

Okno „Vytvoriť sieť“

### Priradenie materiálu

Vyberte a priraďte materiál **Demo.Steel**, ako je znázornené na obr. 3DHTWL1.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0011.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Nastavenie okrajových podmienok

  1. Určite symetrické plochy na oboch stranách obrobku, ako je znázornené na obr. 3DHTWL1.12. Upozorňujeme, že táto geometria predstavuje polovicu zuba ozubeného kolesa.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0012.jpg' | relative_url }})

Priradenie symetrie BCC

  1. Keďže sa bude modelovať elastoplastická deformácia, je potrebné tu špecifikovať niektoré okrajové podmienky s pevnými uzlami. Na to vyberte položku okrajovej podmienky a následne ju priraďte k príslušným okrajovým uzlom. V tomto modeli, keďže symetrické roviny poskytujú obmedzenia v smeroch kolmých na ich vlastnú rovinu, potrebujeme obmedzenia v smere Z. Tu zafixujeme uzol na spodnej strane, ako je znázornené na obr. 3DHTWL1.13.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0013.jpg' | relative_url }})

Priradenie rýchlosti BCC

## Inicializácia obrobku

Kliknite na uzly objektu ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) a vyberte **difúziu**, potom pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) nastavte **percento atómov** na hodnotu **0,2** (pozri obr. 3DHTWL1.14.), priraďte pomocou možnosti **Rozsah** tak, že ako hodnotu zadáte **0,2**, a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili dialógové okno Inicializácia, a kliknutím zatvorte dialógové okno Údaje o uzloch.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0014.jpg' | relative_url }})

Okno definície údajov uzla objektu

Kliknite na prvky objektu ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) a v časti **Mikrostruktúra** vyberte kartu **Fázová transformácia**. Nastavte hodnotu **Perlit+Bainit** na **1** a ostatné fázy na nulu tak, že vyberiete každú fázu a použijete ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) (pozri obr. 3DHTWL1.15.), priraďte pomocou možnosti **Rozsah** tak, že ako hodnotu zadáte 1, a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}), aby ste zatvorili dialógové okno **Inicializácia**, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili dialógové okno **Údaje o prvkoch**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali podrobnosti o prostredí.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0015.jpg' | relative_url }})

Okno definície údajov prvku objektu

## Definícia pojmu „stredný“

Na stránke „**Podrobnosti o médiách**“ definujete rôzne médiá a s nimi súvisiace zóny prenosu tepla, ako je znázornené na obr. 3DHTWL1.16.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0016.jpg' | relative_url }})

Okno „Podrobnosti o médiu“

  1. Premenujte prvé médium na „Kúrená pec“ a nastavte „predvolený“ koeficient prenosu tepla (HTC) na konštantu 0,1. Aktivujte žiarenie zaškrtnutím políčka „Žiarenie“.

  2. Pridajte prostredie „Carb. Furnace“ (Carb. pre nauhličovanie). Nastavte „predvolený“ koeficient prenosu tepla (HTC) na konštantu 0,05. Pre „Carb. Furnace“ zadajte hodnotu 0,0001 do poľa „Rýchlosť difúznej povrchovej reakcie“. Aktivujte žiarenie zaškrtnutím tlačidla „Radiation“.

  3. Pridajte médium „Oil“. Deaktivujte položku „Radiation“. Do poľa „default“ HTC zadajte hodnotu 5,5.

Pridajte zónu prenosu tepla (zóna č. 1) k médiu „Olej“. Kliknutím na hranicu obrobku určite túto zónu tak, aby sa vzťahovala na spodnú časť obrobku, ako je znázornené na obr. 3DHTWL1.17. Upozorňujeme, že na správne určenie zóny môže byť potrebné zmeniť režimy výberu v okne výberu bodov.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0017.jpg' | relative_url }})

Okno so strednou úrovňou detailov zobrazujúce rozdelenie zón

Pre zónu č. 1 definujte HTC ako funkciu teploty nasledovne: vyberte f(Temp) z roletového menu a použite tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (pozri obr. 3DHTWL1.18 a obr. 3DHTWL1.19).

**Teplota** |  **HTC**  
---|---  
20 |  2.1  
250 |  2,8  
500 |  6,8  
750 |  4,0  
1000 |  2,5  
  
Tabuľka HTC

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0019.jpg' | relative_url }})

Okno definície funkcie

  1. Pridajte ešte jedno médium „Air“. Do poľa „HTC“ zadajte hodnotu 0,02. Aktivujte žiarenie zaškrtnutím políčka „Radiation“.

## Definícia plánu

V tomto laboratórnom cvičení budeme vykonávať päťstupňový proces tepelného spracovania. Na tento účel zadajte na stránke „Schedule“ päťstupňový plán podľa nižšie uvedeného postupu. (Pozri obr. 3DHTWL1.20.)

  1. Pol hodiny (1800 s) predhrievania pri teplote 550 °C.

  2. Dve hodiny (7200 s) nauhličovania pri teplote 850 °C. Uveďte obsah „Atomu“ na hodnotu 0,8.

  3. 20 minút (1200 s) kalenia v oleji s teplotou oleja 100 °C.

  4. 30 minút (1800 s) temperovania pri teplote 280 °C.

  5. Jedna hodina (3600 s) chladenia na vzduchu.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0020.jpg' | relative_url }})

Okno „Plán tepelného spracovania“

Nastavenia jednotlivých fáz je možné nastaviť alebo upraviť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define.._button.jpg' | relative_url }}) v stĺpci „Pokročilé“. Používateľ môže začať z akejkoľvek fázy nastavením čísla „Začať operáciu“ na základe definovaných fáz. V tomto laboratórnom cvičení použijeme číslo 1. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ovládacie prvky simulácie“.

## Ovládacie prvky simulácie

V časti „Definícia kroku“ vyberte prepínač **Auto** a zmeňte hodnotu „Zmena teploty na krok“ na **2** °C. Ostatné predvolené nastavenia ponechajte bez zmeny. (Pozri obr. 3DHTWL1.21.)

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0021.jpg' | relative_url }})

Okno ovládacích prvkov simulácie

## Vytvoriť databázu

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0022.jpg' | relative_url }})

Okno na vytvorenie databázy

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DHTWL1.23. Použite predvolenú možnosť **Pokračovať v spustení**, vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“, v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0023.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie je možné počas jej vykonávania sledovať prostredníctvom okien „Simulation Message“ a „Process Monitor“ v režime simulácie. Kliknutím na kartu „Simulation Message“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}), čo je predvolené nastavenie, súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa správa pridá na koniec súboru správ. (Pozri obr. 3DHTWL1.24.)

Každá definovaná fáza sa vykoná ako samostatná operácia a používateľ musí počkať, kým sa simulácia všetkých fáz dokončí.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0024.jpg' | relative_url }})

Karta „Simulačné správy“

## Následné spracovanie

Po ukončení simulácie kliknite na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky. Priebeh minimálnej a maximálnej teploty by mal vyzerať ako na grafe nižšie (pozri obr. 3DHTWL1.25.).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0025.jpg' | relative_url }})

Stavová premenná zobrazujúca históriu minimálnych a maximálnych teplôt

Pri následnom spracovaní odporúčame vykonať nasledujúce úlohy:

  1. Skontrolujte stav obrobku po kalení v oleji. Medzi relevantné stavové veličiny môžu patriť obsah uhlíka, objemové podiely martenzitu (M), feritu (F) a perlitu + banitu (PB) a zvyškové napätie. Všimnite si, že v tomto bode dosahuje M v blízkosti povrchu zuba hodnotu až 0,797 a maximálne efektívne napätie je ~128 MPa.

  2. Po temperovaní skontrolujte tie isté stavové veličiny. Všimnite si, že hodnota M sa v blízkosti povrchu zuba znížila na ~0,2, pričom väčšina z neho sa premenila na temperovaný ferit + cementit (TFC). Maximálne efektívne napätie sa znížilo na ~82 MPa.

  3. Okrem toho môže byť sledovanie objemových podielov vo fáze bodového sledovania na rôznych miestach obrobku užitočné pre pochopenie zložitých javov, ktoré sa vyskytli.
