---
lang: sk
title: "Laboratórium 2D obrábania v ustálenom stave"
---

# Laboratórium 2D obrábania v ustálenom stave

1.1. Zhrnutie problému

1.2. Vytvorenie nového problému

1.3. Definovanie údajov o obrábacom procese

1.4. Zaťaženie rezných nástrojov – materiál povlaku

1.5. Definovanie geometrie rezných nástrojov

1.6. Definícia povlaku

1.7. Priradiť materiál nástroja

1.8. Vytvorenie siete nástroja

1.9. Okrajové podmienky nástroja

1.10. Nastavte údaje o geometrii obrobku

1.11. Určenie materiálu obrobku

1.12 Vytvorenie siete pre obrobok

1.13. Stránka „Okrajové podmienky obrobku“

1.14. Inicializácia

1.15. Nastavenie opotrebenia nástroja

1.16. Kontakt

1.17. Krokové riadenie

1.18. Vytvorenie databázy

1.19. Spustenie simulácie

1.20. Následné spracovanie

## Zhrnutie problému

V tomto laboratórnom cvičení stručne ukážeme, ako pomocou šablóny obrábania pripraviť modelové údaje reprezentujúce ortogonálne reznú situáciu (rezná hrana je ortogonálna/kolmá na smer rezu) na simuláciu procesu tvorby triesok. Tu sa venujeme interaktívnemu definovaniu procesných podmienok, reznej hrany, povlaku, materiálu, ustáleného stavu a vlastností súvisiacich s namáhaním nástroja. Stručný popis ortogonálnych podmienok rezania a vzťahu medzi parametrami procesu a modelovacou oblasťou je uvedený na obr. 2DSSL1.1.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0001.jpg' | relative_url }})

Vzťah medzi procesnými údajmi a oblasťou analýzy

## Vytvorenie nového problému

**Sprievodcu 2D rezaním môžeme otvoriť dvoma spôsobmi:**

**a.** Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Nový****Problém**, alebo kliknutím na ikonu **Nový****Problém**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**SI**“ pomocou prepínača. Názov úlohy zadajte ako „**2D_CUTTING_STEADY**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte novú úlohu s použitím integrovaného výrobného procesu. Otvorí sa sprievodca viacerými operáciami, v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**2D_CUTTING_STEADY**“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. Otvorí sa okno Integrovaný výrobný proces, kde pridajte operáciu 2D rezanie zo zoznamu operácií v Průzkumníku. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky 2D rezanie alebo jej presunutím do editora operácií.****

**b.** Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový****Problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**2D rezanie**“ a ako systém jednotiek zvoľte „**SI**“ pomocou prepínača, ako je znázornené na obr. 2DSSL1.2. Názov úlohy zadajte ako „**2D_CUTTING_STEADY**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte v sprievodcovi MO novú úlohu s operáciou 2D rezania.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0002.jpg' | relative_url }})

Stránka s popisom problému

## Definovanie údajov o obrábacom procese

V ponuke „**Proces**“ vyberte typ simulácie „**Steady-state****Analýza**“, zadajte **Teplotu prenosu tepla v prostredí** na hodnotu **22,5** °C a použite predvolený **koeficient konvekcie** **0,02****N/s/mm/°C**. Zvoľte „****Povrchovú rýchlosť**“ na hodnotu **250 m/min** a ****posuv**“ na hodnotu **0,15 mm/ot**** (pozri obr. 2DSSL1.3.). Alternatívne môže používateľ namiesto povrchovej rýchlosti zadať aj rýchlosť otáčania obrobku a priemer dielu. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0003.jpg' | relative_url }})

Stránka procesu

## Načítavanie: Materiál povlaku rezných nástrojov

Na stránke Zoznam materiálov načítajte materiály „**Coating-TiN**“ a „**Coating-Al2O3**“ z kategórie **Tool_Material**, aby ste ich mohli priradiť k povlaku nástroja. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Nástroj.

## Definovanie geometrie rezného nástroja

Na stránke „Nástroj“ zadajte teplotu nástroja 20 °C. Geometriu rezných hrán môžeme importovať z predtým definovaného súboru s kľúčovými slovami simulácie alebo z databázového súboru pomocou možnosti „Importovať objekt“. V rámci tohto cvičenia definujeme geometriu rezných hrán pomocou primitív dostupných v systéme. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) otvoríte ponuku „Insert Geometry“ (pozri obr. 2DSSL1.4.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Na stránke „Primitive“ vyberte **#3** **geometriu** a použite predvolené parametre geometrie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) na vytvorenie geometrie. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na opustenie menu „Geometry Primitive“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na pokračovanie.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0004.jpg' | relative_url }})

Okno „Vložiť primitív“

## Definícia povlaku

V tabuľke „Povlakový materiál“ zadajte „Povlakový materiál“ a hrúbku, pridajte (![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }})) dve vrstvy povlaku. Pre vonkajšiu vrstvu zvoľte hrúbku povlaku 10 mikrónov a materiál „TiN“ a pre vnútornú vrstvu zvoľte hrúbku povlaku 10 mikrónov a materiál „Al2O3“ (pozri obr. 2DSSL1.5.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0005.jpg' | relative_url }})

Definícia povlakovej vrstvy a materiálu

## Priradiť materiál nástroja

V okne „Material“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), aby ste načítali údaje o materiáli z knižnice, a načítate materiál „**WC**“ z kategórie „**Tool_Material**“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. 2DSSL1.6. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vygenerovali sieť pre nástroj.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0006.jpg' | relative_url }})

Načítavanie materiálu nástroja z knižnice materiálov

## Vytvorenie siete nástroja

V ponuke „Generovanie siete“ vyberte ako cieľový počet prvkov pre vloženie hodnotu „**700**“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (pozri obr. 2DSSL1.7.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0007.jpg' | relative_url }})

Stránka „Tool Mesh“

## Okrajové podmienky nástroja

Ďalším krokom je zobrazenie teplotných okrajových podmienok vygenerovaných systémom v ponuke BCC. Program generuje výmenu tepla s okolím (ktorej časť pochádza z kontaktnej oblasti vložky) a BCC s pevnou uzlovou teplotou pre povrchy vzdialené od rezných hrán (pozri obr. 2DSSL1.8.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite k nastaveniu obrobku.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0008.jpg' | relative_url }})

Okrajová podmienka nástroja

## Nastavenie geometrie obrobku 

V časti „Nastavenie obrobku“ definujte obrobok ako **plastový** objekt a teplotu ako **22,5** °C a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte. Na stránke „Geometria obrobku“ kliknite na označenie ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Vygenerujte geometriu pomocou nasledujúcich parametrov:

Dĺžka WP (L) = 4,5, výška WP (H) = 1, dĺžka rezu (L1) = 1,5, výška špony (H1) = 0,5, dĺžka kontaktu (D) = 0,4, R1 = 0,3, R2 = 0,1, Hrúbka triesky (C1) = 0,165. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}), aby ste vytvorili geometriu obrobku (pozri obr. 2DSSL1.9.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili toto menu geometrie, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku Materiál.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0009.jpg' | relative_url }})

Definovanie geometrie obrobku

## Priradenie materiálu obrobku

Na stránke „Materiál obrobku“ vyberte možnosť „importovať materiál z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})), vyberte kategóriu „**Oceľ**“ a „**AISI****-****10****45 (obrábanie)**, načítajte tento materiál kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) (pozri [Fig. 2DSSL1.10.]()) a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte sieť.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0010.jpg' | relative_url }})

Načítavanie typu materiálu obrobku z knižnice

## Vytvorenie siete pre obrobok

Zvoľte **15** ako **počet prvkov cez hrúbku neobrobeného čipu pre obrobok** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), čím dokončíte vytvorenie siete pre obrobok (pozri obr. 2DSSL1.11.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0011.jpg' | relative_url }})

Stránka so sieťou obrobkov

## Okrajová podmienka obrobku 

V ponuke „Zobraziť okrajové podmienky obrobku“ skontrolujte okrajové podmienky, ktoré systém nastavil pre obrobok (pozri obr. 2DSSL1.12.), a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Všímajte si okrajovú podmienku rýchlosti priradenú k spodnému okraju vzdialenému od rezných plôch, ktorá zabraňuje odletovaniu obrobku. Od verzie V13.0.1 sa namiesto okrajovej podmienky povrchovej rýchlosti (Vx) bude pre okraj +X a spodný okraj obrobku definovať okrajová podmienka pohybu (pozri obr. 2DSSL1.12.) a pohyb sa bude definovať na stránke „Pohyb“ obrobku. 

  
Počiatočná plocha BCC je priradená k ploche (-X hrana (ľavá strana) obrobku) vzdialenej od smeru rezania. Povrch BCC „voľný“ je priradený k hornému okraju triesky a k povrchu, od ktorého sa začína rezanie (okraj +X (pravá strana) obrobku), pozri obr. 2DSSL1.13.

  
Výmena tepla s BCC je priradená k povrchu horného okraja s výnimkou horného okraja čipu. Teplota BCC je priradená k okraju +X (pravá strana) a spodnému okraju obrobku, pozri obr. 2DSSL1.14. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0012.jpg' | relative_url }})

Hraničná podmienka pohybu pre obrobok

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0021.jpg' | relative_url }})

Pre obrobok bol priradený model BCC s voľným povrchom

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0022.jpg' | relative_url }})

Teplota BCC priradená pre obrobok

## Inicializácia

Na stránke „Initialize“ môžeme nastaviť počiatočnú hodnotu deformácie obrobku (pozri obr. 2DSSL1.15.). V tomto laboratórnom cvičení žiadnu hodnotu deformácie nenastavujeme, preto klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka „Tool wear“.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0013.jpg' | relative_url }})

Inicializovať stránku

## Nastavenie opotrebenia nástroja

Vyberte Usuiho model a zadajte koeficienty a, b. Upozorňujeme, že tieto hodnoty (uvedené vedľa rovnice) sú len typickými hodnotami, ktoré možno nájsť v odbornej literatúre, a za správnosť týchto údajov zodpovedá používateľ (pozri obr. 2DSSL1.16.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na kontaktnú stránku.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0014.jpg' | relative_url }})

Okno nastavení opotrebenia nástrojov

## Stránka s kontaktnými údajmi

Na stránke „Kontakt“ použite predvolené vzťahy. Kliknite na tlačidlo **Nástroj – Obrobok**, vyberte vzťah „Upraviť ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }})“ a nastavte **koeficient trenia pri šmyku****** na hodnotu **0,48** a **koeficient prenosu tepla na rozhraní****** na hodnotu ****koeficient prenosu tepla** na **39,5****N/s/mm/°C**, kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu (ako je znázornené na obr. 2DSSL1.17.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránke „Kontrola krokov“.

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0015.jpg' | relative_url }})

Stránka s kontaktnými údajmi

## Stránka na ovládanie krokov

Na stránke „Step controls“ použijeme predvolenú metódu konvergencie teploty a deformácie, ktorou je **UL solution: 50**, spolu s predvolenou hodnotou tolerancie konvergencie (ako je znázornené na obr. 2DSSL1.18.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0016.jpg' | relative_url }})

Stránka „Kontrola krokov“

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu. Pozrite si správu na karte „Message“, ktorá informuje o stave generovania databázy.

## Spustenie simulácie

Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DSSL1.19. Použite predvolenú možnosť **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ (od kroku -1) a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. 

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0019.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie môžete sledovať na kartách „Simulačné správy“ a „Simulačný protokol“, pričom sa uistite, že je zaškrtnutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). V priebehu simulácie až do dosiahnutia zadaného dĺžky rezu si môžete v grafickom zobrazení simulácie prezerať priebeh rezania.

Keď sa simulácia ukončí dosiahnutím ustáleného stavu, môžeme si všimnúť, že na koniec súboru Message sa pridá nasledujúca správa:

Tepelné riešenie v ustálenom stave dosiahlo konvergenciu

Riešenie deformácie v ustálenom stave sa zbieha

Výpočty voľnej hladiny čipu v ustálenom stave dosiahli konvergenciu

******Správa*******

Riešenie v ustálenom stave sa zbieha

## Následné spracovanie

Po dokončení simulácie si výsledky prezrite tak, že prejdete do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov Simulácia.

Zaznačte premennú „Teplota“ a prejdite jednotlivými krokmi, pričom sledujte teplotu, ktorá vzniká v rezacej zóne (pozri obr. 2DSSL1.20).

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0018.jpg' | relative_url }})

Graf teploty pri rezaní v ustálenom stave

![]({{ '/assets/images/labs/machining_labs/2d_steady_state_machining_lab/image0020.jpg' | relative_url }})

Graf poškodenia pre objekt obrobku
