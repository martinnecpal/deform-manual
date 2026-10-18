---
lang: sk
title: "Laboratórium 2D rezania"
---

# Laboratórium 2D rezania

1.1 Zhrnutie problému

1.2. Vytvorenie novej úlohy

1.3. Definovanie údajov o obrábacom procese

1.4. Zaťaženie rezných nástrojov – materiál povlaku

1.5. Definovanie geometrie rezných hrán

1.6. Definícia povlaku

1.7. Priradiť materiál nástroja

1.8. Vytvorenie siete nástroja

1.9. Okrajové podmienky nástroja

1.10. Nastavte údaje o geometrii obrobku

1.11. Určenie materiálu obrobku

1.12. Vytvorenie siete pre obrobok

1.13. Stránka „Okrajové podmienky obrobku“

1.14. Polohovanie nástroja

1.15. Nastavenie opotrebenia nástroja

1.16. Stránka s kontaktnými údajmi

1.17. Stránka riadenia krokov

1.18. Vytvorenie databázy

1.19. Spustenie simulácie

1.20. Následné spracovanie

## Zhrnutie problému

V tomto laboratórnom cvičení stručne ukážeme, ako pomocou šablóny obrábania pripraviť modelové údaje reprezentujúce ortogonálne reznú situáciu (rezná hrana je ortogonálna/kolmá na smer rezu) na simuláciu procesu tvorby triesok. Tu sa venujeme interaktívnemu definovaniu procesných podmienok, reznej hrany, povlaku, materiálu, ustáleného stavu a vlastností súvisiacich s namáhaním nástroja. Stručný popis ortogonálnych podmienok rezania a vzťahu medzi parametrami procesu a modelovacou oblasťou je uvedený tak, ako je znázornené v [Fig. 2DCL1.1.]()

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0001.jpg' | relative_url }})

Vzťah medzi procesnými údajmi a oblasťou analýzy

## Vytvorenie nového problému

**Sprievodcu 2D rezaním môžeme otvoriť dvoma spôsobmi:**

**a.** Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový****Problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte tlačidlo „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**SI**“ pomocou príslušného tlačidla. Zadajte názov úlohy ako „**2D_CUTTING**“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte novú úlohu s použitím integrovaného výrobného procesu. Otvorí sa sprievodca viacerými operáciami, v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**2D_CUTTING**“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. Otvorí sa okno Integrovaný výrobný proces, kde pridajte operáciu 2D rezanie zo zoznamu operácií v Průzkumníku. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky 2D rezanie alebo jej presunutím do editora operácií.

**b.** Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový****Problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**2D rezanie**“ a ako systém jednotiek zvoľte „**SI**“ pomocou prepínača, ako je znázornené na obr. 2DCL1.2. Názov úlohy zadajte ako „**2D_CUTTING**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte v sprievodcovi MO novú úlohu s operáciou 2D rezania.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0002.jpg' | relative_url }})

Stránka s popisom úlohy

## Definovanie údajov o obrábacom procese

V ponuke „**Proces**“ vyberte **Typ simulácie** ako „**Prechodová**Analýza**“, zadajte **teplotu prostredia pre prenos tepla** na hodnotu **22,5** °C a použite predvolený koeficient konvekcie **0,02** N/s/mm/°C. Zvoľte „**rýchlosť povrchu**“ ako **250****m/min** a **posuv** ako **0,15 mm/ot**“ (pozri obr. 2DCL1.3.). Alternatívne môže používateľ namiesto povrchovej rýchlosti špecifikovať aj rýchlosť otáčania obrobku a priemer dielu. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0003.jpg' | relative_url }})

Stránka procesu

## Načítanie: Materiál povlaku rezných nástrojov

Na priradenie povlaku k nástroju načítajte materiály „**Coating-TiN**“ a „**Coating-Al2O3**“ z kategórie **Tool_Material** pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Následne klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Nástroj.

## Definovanie geometrie rezných hrán

Na stránke „**Nástroj**“ zadajte teplotu nástroja ako **20** °**C**. Geometriu rezných hrán môžeme importovať z predtým definovaného súboru simulačných kľúčových slov alebo z databázového súboru pomocou voľby ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}). Pre toto laboratórne cvičenie definujeme geometriu rezných hrán pomocou primitív dostupných v systéme. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste otvorili menu „**Vložiť geometriu**“ (pozri obr. 2DCL1.4.), a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Na stránke Primitív vyberte **#** 3 **geometriu** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) na vytvorenie geometrie. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na opustenie ponuky „Geometrické primitívy“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na pokračovanie.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0004.jpg' | relative_url }})

Definícia primitívneho okna

## Definícia povlaku

V tabuľke „**Materiál povlaku**“ zadajte „**Materiál povlaku**“ a hrúbku, pridajte (![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }})) dve vrstvy povlaku. Pre **vonkajšiu vrstvu** vyberte **10****mikrónov** ako hrúbku povlaku a „**TiN**“ ako materiál a pre **vnútornú****vrstvu** zvoľte hrúbku povlaku **10** mikrónov a ako materiál povlaku „**Al2O3**“ (pozri obr. 2DCL1.5.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0005.jpg' | relative_url }})

Definícia povlakovej vrstvy a materiálu

## Priradiť materiál nástroja

V okne „Material“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), aby ste načítali údaje o materiáli z knižnice, a načítate materiál „**WC**“ z kategórie „**Tool_Material**“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. 2DCL1.6. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vygenerovali sieť pre nástroj.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0006.jpg' | relative_url }})

Načítavanie materiálu nástroja z knižnice materiálov

## Vytvorenie siete nástroja

V ponuke „Generovanie siete“ vyberte ako cieľový počet prvkov pre vloženie hodnotu „**700**“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (pozri obr. 2DCL1.7.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0007.jpg' | relative_url }})

Stránka s nástrojovou sieťou

## Okrajové podmienky nástroja

Ďalším krokom je zobrazenie teplotných okrajových podmienok vygenerovaných systémom v ponuke BCC. Program generuje výmenu tepla s okolím (ktorej časť pochádza z kontaktnej oblasti vložky) a BCC s pevnou uzlovou teplotou pre povrchy vzdialené od rezných hrán (pozri obr. 2DCL1.8.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite k nastaveniu obrobku.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0008.jpg' | relative_url }})

Okrajová podmienka nástroja

## Nastavenie údajov o geometrii obrobku

V časti „Nastavenie obrobku“ definujte obrobok ako **plastový****objekt** a **teplotu** nastavte na **22,5** °C a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

Kliknite na označenie ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) na stránke „Geometria obrobku“. Pomocou parametrov **L = 3** a **H = 1** kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}), čím vytvoríte geometriu obrobku (pozri obr. 2DCL1.9.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili toto menu geometrie, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Materiál“.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0009.jpg' | relative_url }})

Definovanie geometrie obrobku

## Priradenie materiálu obrobku

Na stránke „**Materiál obrobku******“ vyberte možnosť ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) „importovať materiál z knižnice“, vyberte kategóriu „**Oceľ**“ a „**AISI-1045 (obrábanie)** “ (pozri obr. 2DCL1.10.). „Načítajte“ tento materiál a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vytvorenie siete.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0010.jpg' | relative_url }})

Načítanie typu materiálu obrobku z knižnice

## Vytvorenie siete pre obrobok

Zvoľte **15** ako počet prvkov na hrúbku neobrobeného materiálu obrobku a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), čím dokončíte vytvorenie siete pre obrobok (pozri obr. 2DCL1.11.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0011.jpg' | relative_url }})

Stránka so sieťou obrobkov

## Stránka „Okrajové podmienky obrobku“

V ponuke „Zobraziť BCC obrobku“ skontrolujte okrajové podmienky, ktoré systém stanovil pre obrobok (pozri obr. 2DCL1.12.), a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky. Všimnite si, že na spodný okraj vzdialený od rezných plôch je priradená rýchlosť BCC, aby sa zabránilo odletovaniu obrobku. Výmena tepla s BCC je priradená na všetky plochy okrem spodného okraja a na spodný okraj je priradená teplota BCC. Od verzie V13.0.1 sa namiesto okrajovej podmienky „Rýchlosť povrchu (Vx)“ pre spodný okraj obrobku definuje okrajová podmienka „Pohyb“ (pozri obr. 2DCL1.12.) a pohyb sa definuje na stránke „Pohyb“ obrobku. Výmena tepla s BCC je priradená k hornému okraju a okraju -X (ľavá strana). Teplota BCC je priradená k spodnému okraju a okraju +X (pravá strana). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0012.jpg' | relative_url }})

Okrajová podmienka pre obrobok

##  Polohovanie nástroja

V ponuke „Poloha“ kliknite na položku „![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})“ (pozri obr. 2DCL1.13.). Funkcia automatického nastavenia polohy automaticky umiestni objekty v jednoduchom nastavení s jedným rezacím nástrojom a obrobkom; kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0013.jpg' | relative_url }})

Objekty po umiestnení

## Nastavenie opotrebenia nástroja

Vyberte Usuiho model a zadajte koeficienty a, b. Upozorňujeme, že tieto hodnoty (uvedené vedľa rovnice) sú len typickými hodnotami, ktoré je možné získať z odbornej literatúry, a za správnosť týchto údajov zodpovedá používateľ (pozri obr. 2DCL1.14.). Ak má používateľ záujem o výpočet opotrebenia nástroja, zaškrtnite políčko „Aktualizovať opotrebovanú geometriu“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na kontaktnú stránku.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0014.jpg' | relative_url }})

Okno nastavení opotrebenia nástrojov

## Stránka s kontaktnými údajmi

Na stránke **Kontakt** použite predvolené vzťahy. Kliknite na vzťah **Nástroj – Obrobok** ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (tlačidlo Upraviť) a nastavte koeficient **šmykového trenia** na hodnotu **0,48** a koeficient prenosu tepla na rozhraní na hodnotu **39,5****N/s/mm/°C**, ako je znázornené na obr. 2DCL1.15., kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku riadenia krokov.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0015.jpg' | relative_url }})

Stránka s kontaktnými údajmi

## Stránka na ovládanie krokov

Zaškrtnite políčko „Ovládacie prvky simulácie“ a nastavte **dĺžku****rezu** na hodnotu „**1 mm**“; ostatné nastavenia ponechajte na predvolených hodnotách, ako je znázornené na obr. 2DMDL1.16, a pokračujte vo vytváraní databázy.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0016.jpg' | relative_url }})

Stránka „Kontrola krokov“

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu. Pozrite si správu na karte „Message“, ktorá informuje o stave generovania databázy.

## Spustenie simulácie

Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DCL1.17. Použite predvolenú možnosť **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ (od kroku -1) a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0017.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie môžete sledovať na kartách „Simulačné správy“ a „Simulačný protokol“, pričom sa uistite, že je zaškrtnutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). V priebehu simulácie až do dosiahnutia zadaného dĺžky rezu si môžete v grafickom zobrazení simulácie prezerať priebeh rezania.

Po dokončení simulácie môžeme vidieť, že na koniec súboru Message bola pridaná nasledujúca správa:

"PROGRAM SA ZASTAVIL!

AKTUÁLNY ČAS 0,0002400

„SÚČASNÝ MIESTNY ČAS 0,0002400 DOSIAHOL NASTANENÝ LIMIT 0,0002400“

## Následné spracovanie

Po dokončení simulácie si výsledky prezrite tak, že prejdete do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov Simulácia.

Prejdite jednotlivými krokmi simulácie a pozrite sa, ako sa čip formoval počas procesu rezania. (pozri obr. 2DCL1.18.)

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0018.jpg' | relative_url }})

Režim MO Post

Vykreslite **efektívne****napätie** pre objekt obrobku a sledujte graf tak, ako je znázornené na nižšie uvedenej obr. 2DCL1.19.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0019.jpg' | relative_url }})

Graf efektívneho napätia pre objekt obrobku v poslednom kroku

Vykreslite **efektívne** **deformácie** pre objekt obrobku a sledujte graf tak, ako je znázornené na nižšie uvedenej obr. 2DCL1.20.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0020.jpg' | relative_url }})

Graf efektívneho deformácie pre objekt obrobku v poslednom kroku
