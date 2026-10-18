---
lang: sk
title: "Laboratórium 3D rezania 1"
---

# Laboratórium 3D rezania 1

1.1. Zhrnutie

1.2. Spustenie sprievodcu 3D obrábaním

1.3. Definovanie údajov o obrábacom procese

1.4. Definovanie geometrie vložky

1.5. Definícia držiaka nástroja

1.6. Priradenie materiálu na vloženie

1.7. Vytvorenie vkladacej siete

1.8. Zadanie okrajových podmienok

1.9. Geometria obrobku

1.10. Priradenie materiálu obrobku

1.11. Vytvorenie siete pre obrobok

1.12. Stránka „Okrajové podmienky obrobku“

1.13. Polohovanie nástroja

1.14. Nastavenie opotrebenia nástroja

1.15. Stránka s kontaktnými údajmi

1.16. Stránka „Ovládanie krokov“

1.17. Vytvorenie databázy

1.18. Spustenie simulácie

1.19. Následné spracovanie

## Zhrnutie

Tento dokument podrobne opisuje súčasné modelovacie možnosti dostupné v systéme DEFORM na simuláciu 3D prostredia rezania kovu pri sústružení. Systém je možné použiť na modelovanie priemyselného procesu sústruženia bez akýchkoľvek predpokladov spojených s ortogonálnymi rezacími podmienkami. Tieto modelovacie postupy umožňujú inžinierovi skúmať reakciu procesu na akúkoľvek zmenu procesných podmienok. Pomocou tohto systému je možné vykonávať výpočty rezacích síl, rezacích teplôt, tvaru triesok, opotrebenia nástroja a životnosti nástroja. Inžinier môže skúmať vplyv procesných parametrov, ako sú rýchlosť rezania, posuv a hĺbka rezu, na reakciu procesu. DEFORM® podporuje špeciálnu šablónu, ktorá zjednodušuje definíciu modelu a používa rovnaký technický jazyk ako procesný inžinier. V prípade sústruženia sú rotujúci obrobok, doštička a ich vzťah k oblasti analýzy znázornené na obr. 3DTL1.1. Typický analytický model vygenerovaný pomocou súčasného systému je znázornený na obr. 3DTL1.2. Hlavnými požiadavkami na údaje potrebné na modelovanie procesu obrábania sú údaje o napätí v toku materiálu pre materiál obrobku a geometrické údaje o doštičke. Údaje o napätí v toku materiálu by mali pokrývať rozsah rýchlosti deformácie, deformácie a teploty pre proces rezania kovov. Pre väčšinu materiálov je typický rozsah rýchlosti deformácie 0 – ~10⁶/s, rozsah deformácie 0 – 5 a rozsah teploty 20 – 1200 °C. Na zvládnutie tohto rozsahu zaťažovacích podmienok sú potrebné špeciálne techniky charakterizácie materiálov. Geometria doštičky môže byť k dispozícii vo formáte STL, vygenerovanom z ľubovoľného CAD systému. Toto laboratórium vysvetľuje postup vytvárania modelu krok za krokom. Zahŕňa to špecifikáciu údajov o procese, načítanie materiálov, doštičiek a držiakov nástrojov z knižnice. Špecifikovaním údajov špecifických pre model môže používateľ vygenerovať kompletné údaje potrebné na analýzu. Táto fáza analýzy predstavuje počiatočnú prechodovú analýzu. Po vykonaní simulácie a vytvorení dostatočného množstva triesok môže používateľ vypočítať ustálenú odozvu procesu, ktorá zahŕňa predikciu ustálenej tepelnej odozvy a geometrie triesok. Z hľadiska tepelnej odozvy vložky táto fáza výrazne skráti výpočtový čas, ktorý je bežne spojený s prechodovou analýzou. Výsledky získané v tejto fáze tvoria dôležitý vstup pre výpočty opotrebenia a životnosti nástroja. Šablóna obrábania obsahuje súbor knižničných súborov pre geometriu vložky. Používateľ môže použiť aj akúkoľvek inú geometriu vložky a uložiť ju spolu so systémovou knižnicou pre akékoľvek neskoršie použitie. Zoznam informácií v prílohe uvádza aktuálne dostupné údaje o vložkách a držiakoch nástrojov.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0001.jpg' | relative_url }})

Základné zložky otáčania a ich vzťah k oblasti analýzy

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0002.jpg' | relative_url }})

Simulačný model a definícia základných parametrov rezania

## Spustenie sprievodcu 3D obrábaním

**Sprievodcu 3D rezaním môžeme otvoriť dvoma spôsobmi:**

a. Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**SI**“ pomocou prepínača. Názov úlohy zadajte ako „**3D_cutting**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

Spustí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt, v ktorom bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_cutting**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. Otvorí sa sprievodca MO, pridajte operáciu 3D rezanie zo zoznamu operácií v Průzkumníku. Operáciu pridajte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky 3D rezanie alebo jej presunutím do editora operácií.

b. Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu **Nový****Problém![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) **. Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**3D rezanie**“ a ako systém jednotiek zvoľte „**SI**“ pomocou prepínača (pozri obr. 3DTL1.3.). Zadajte názov úlohy ako „**3D_cutting**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte v sprievodcovi MO novú úlohu s operáciou 3D rezania.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0003.jpg' | relative_url }})

Stránka s novým zadaním úlohy

## Definovanie údajov o obrábacom procese

V tomto laboratórnom cvičení si prejdeme typickú konfiguráciu s nasledujúcimi prevádzkovými podmienkami:

  * Použitý materiál: oceľ AISI 1045, počiatočná teplota = 20 °C.

  * Použitá vložka: TNMA332 (nepoťahovaná, základný materiál WC), Držiak nástroja: DTGNL

  * Proces: Rýchlosť rezania = 250 mm/s, posuv = 0,35 mm/ot., hĺbka rezu = 0,3 mm

V ponuke „**Proces**“ vyberte typ rezania „**Sústruženie**“, zadajte teplotu okolia **20** °C a použite predvolený koeficient konvekcie **0,02** N/s/mm/°C. Nastavte „**Rýchlosť rezu** (v) na **250****mm****/****s**, **posuv (f)** na **0,35****mm/ot** a **hĺbku rezu (d)** na **0,3** **mm** (pozri obr. 3DTL1.4.). Alternatívne môže používateľ namiesto povrchovej rýchlosti zadať aj rýchlosť otáčania obrobku a priemer dielu. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Nástroj.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0004.jpg' | relative_url }})

Stránka procesu

## Definovanie geometrie vložky

Na stránke „**Nástroj**“ zadajte teplotu nástroja 20 °C. Používateľ môže importovať geometriu rezných hrán z predtým definovaného súboru simulačných kľúčových slov alebo z databázového súboru pomocou možnosti Importovať objekt. Pre toto laboratórne cvičenie definujeme geometriu rezných hrán pomocou primitív dostupných v systéme. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre vstup na stránku „Vložiť geometriu“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Na stránke „Vložiť primitív“ vyberte geometriu **TNMA332** (obr. 3DTL1.5.). Po identifikácii vložky môže používateľ skontrolovať základné parametre tejto vložky, podrobnosti o základnom materiáli a prípadné povlaky. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) na vytvorenie geometrie vložky. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na opustenie stránky „Geometrické prvky“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na pokračovanie.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0005.jpg' | relative_url }})

Základné tvary geometrie nástroja

## Definícia držiaka nástroja

Pre vybranú doštičku je možné načítať príslušné držiaky nástrojov z knižnice držiakov nástrojov alebo definovať nový držiak nástrojov zadaním základných rezacích uhlov. Pre doštičku TMNA332 sprievodca zobrazí dostupné držiaky z knižnice. Načítajte držiak **DTGNL** z knižnice (obr. 3DTL1.6.). Základné rezných uhly, ktoré sa preberajú z údajov držiaka nástroja, sú SCEA (uhol bočnej reznú hrany alebo uhol sklonu), BR (uhol zadného sklonu) a SR (uhol bočného sklonu). Tieto základné uhly a údaje o procese (posuv a hĺbka rezu) riadia správnu polohu doštičky vo vzťahu k obrobku. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) na vytvorenie držiaka nástroja. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0006.jpg' | relative_url }})

Vložiť možnosti načítania

## Priradenie materiálu na vloženie

V okne „Materiál“ sa pri vytváraní geometrie nástroja vybraný základný materiál vložky načíta do zoznamu materiálov z knižnice. Zozname teda vyberte materiál „**WC**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte sieť pre vložku.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0007.jpg' | relative_url }})

Stránka „Priradenie materiálu na vloženie“

## Vytvorenie vloženej siete

Na stránke „Vytvorenie siete nástroja“ vyberte možnosť „**Použiť relatívnu veľkosť siete**“, nastavte pomer veľkostí na **4** a nastavte cieľový počet tetraedrických prvkov na **45000**. Vytvorte sieť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Keďže informácie o reznom hrane sú súčasťou údajov o vložke, sprievodca automaticky použije jemnejšiu sieť v blízkosti reznej zóny. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0008.jpg' | relative_url }})

Stránka „Vložiť sieť“

## Vložiť okrajové podmienky

Ak sa výmena tepla s okolím (BCC) nepriradí ručne, bude štandardne priradená na celú plochu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Geometria obrobku

V časti „**Nastavenie obrobku**“ definujte obrobok ako plastový objekt a teplotu na **20** °C a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

Kliknite na označenie ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) na stránke „Geometria obrobku“. V časti „Primitív“ zadajte podrobnosti o obrobku. V závislosti od priemeru obrobku môže používateľ zvoliť buď plochý, alebo zakrivený model. Šablóna vás vyzve na zadanie príslušných údajov a v zobrazovacej oblasti vygeneruje nastavenie obrobku. Pre aktuálne laboratórne cvičenie použijeme „**zjednodušený model**“ s dĺžkou **7** mm. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}), aby ste vytvorili geometriu obrobku (pozri obr. 3DTL1.9.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili toto menu geometrie, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Material“ (Materiál).

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0009.jpg' | relative_url }})

Definovanie geometrie obrobku

## Priradenie materiálu obrobku

Na stránke „Materiál obrobku“ vyberte možnosť „importovať materiál z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})), vyberte kategóriu „**Oceľ**“ a „**AISI-1045 (obrábanie)** “ (pozri obr. 3DTL1.10.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) pre tento materiál a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vytvorenie siete.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0010.jpg' | relative_url }})

Načítanie typu materiálu obrobku z knižnice

## Vytvorenie siete pre obrobok

Po vytvorení geometrie obrobku vytvorte sieť s **pomerom veľkostí prvkov** **7** a minimálnou veľkosťou **prvku** **0,0595** mm. (Obr. 3DTL1.11.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby ste dokončili vytvorenie siete pre obrobok. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku BCC.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0011.jpg' | relative_url }})

Stránka „Mriežka obrobku“

## Stránka „Okrajové podmienky obrobku“

V ponuke „Workpiece BCC“ skontrolujte okrajové podmienky, ktoré systém ukladá obrobku (pozri obr. 3DTL1.12.), a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Controls“. Všimnite si, že rýchlostné okrajové podmienky sú priradené spodným plochám vzdialeným od rezných plôch, aby sa zabránilo odletovaniu obrobku. Teplotné okrajové podmienky sú priradené všetkým plochám s výnimkou rezných plôch.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0012.jpg' | relative_url }})

Predpísaná teplotná okrajová podmienka pre obrobok

## Polohovanie nástroja

V ponuke Ovládacie prvky kliknite na ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Skontrolujte polohu vložky. Ak vložka nie je v kontakte s obrobkom, nastavte jej polohu pomocou metódy kolízie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Nastavenie opotrebenia nástroja

Ak zvolíte Usuiho model, koeficienty použité v tomto modeli by sa mali stanoviť na základe experimentálnej kalibrácie, keďže pre dosiahnutie presných výsledkov závisia od podmienok procesu a použitých materiálov. Ako príklad v tomto prípade použijeme **a = 0,0000002** a **b = 650,5** (pozri obr. 3DTL1.13.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na kontaktnú stránku.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0013.jpg' | relative_url }})

Okno nastavení opotrebenia nástrojov

## Stránka s kontaktnými údajmi

Na stránke „Kontakt“ použite predvolené vzťahy. Kliknite na tlačidlo „Upraviť“ vzťahu **Nástroj – Obrobok** a nastavte koeficient trenia **šmykového** na hodnotu **0,5** a koeficient **tepelného prenosu** na rozhraní na hodnotu **45** N/s/mm/°C (ako je znázornené na obr. 3DTL1.14.), kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku **Kontrola krokov**.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0014.jpg' | relative_url }})

Stránka s kontaktnými údajmi

## Stránka „Ovládanie krokov“

Zaškrtnite políčko „Ovládacie prvky simulácie“, nastavte dĺžku rezu na „**3,5 mm**“, ostatné hodnoty ponechajte v predvolenom nastavení a pokračujte vo vytvorení databázy.

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu. Pozrite si správu na karte „Message“, ktorá informuje o stave generovania databázy.

## Spustenie simulácie

Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na označenie akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DTL1.15. Použite predvolenú možnosť **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“, v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0015.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie môžete sledovať na kartách „Simulačné správy“ a „Simulačný protokol“, pričom sa uistite, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). V priebehu simulácie až do dosiahnutia zadaného dĺžky rezu si môžete v grafickom zobrazení simulácie prezerať priebeh rezania.

## Následné spracovanie

Po dokončení simulácie si výsledky prezrite tak, že prejdete do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov Simulácia.

Prejdite si jednotlivé kroky simulácie a pozrite sa, ako sa čip formoval počas procesu rezania.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0016.jpg' | relative_url }})

Režim MO Post

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0017.jpg' | relative_url }})

Rozloženie teploty v obrobku a nástroji

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0018.jpg' | relative_url }})

Príloha A

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0019.jpg' | relative_url }})

Príloha B

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab1/image0020.jpg' | relative_url }})

Príloha C
