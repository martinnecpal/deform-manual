---
lang: sk
title: "Laboratórium 3D rezania 2"
---

# Laboratórium 3D rezania 2

2.1. Zhrnutie

2.2. Spustenie sprievodcu 3D obrábaním

2.3. Definovanie údajov o obrábacom procese

2.4. Definovanie geometrie vložky

2.5. Polohovanie rezných nástrojov

2.6. Priradenie materiálu nástroja

2.7. Vytvorenie siete pre nástroj

2.8. Geometria obrobku

2.9. Priradenie materiálu obrobku

2.10. Vytvorenie siete pre obrobok

2.11. Stránka „Okrajové podmienky obrobku“

2.12. Polohovanie nástroja

2.13. Nastavenie opotrebenia nástroja

2.14. Stránka s kontaktnými údajmi

2.15. Stránka „Step Control“

2.16. Vytvorenie databázy

2.17. Spustenie simulácie

2.18. Následné spracovanie

## Zhrnutie

V tomto cvičení si ukážeme, ako nastaviť sústruženie importovaním geometrie vložky v sprievodcovi 3D rezaním.

## Spustenie sprievodcu 3D obrábaním

**Sprievodcu 3D rezaním môžeme otvoriť dvoma spôsobmi:**

a. Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu **Nový****problém**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Anglický**“ pomocou prepínača. Názov úlohy zadajte ako „**3D_sústruženie**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „**Zobraziť dialógové okno s možnosťami**“ nezaškrtnete, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami, v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_turning**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. Otvorí sa sprievodca MO, zoznamu operácií v Průzkumníku pridajte operáciu 3D rezanie. Operáciu pridajte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky 3D rezanie alebo jej presunutím do editora operácií.

b. Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu **Nový****Problém![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) **. Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**3D rezanie**“ a ako systém jednotiek zvoľte „**anglický**“ pomocou prepínača (pozri obr. 3DTL2.1.). Názov úlohy zadajte ako „**3D_turning**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte v sprievodcovi MO novú úlohu s operáciou 3D rezania.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0001.jpg' | relative_url }})

Stránka s popisom úlohy

## Definovanie údajov o obrábacom procese

V ponuke „**Proces**“ nastavte typ rezania na „**Sústruženie**“, zadajte teplotu prenosu tepla v prostredí ako **68 °F** a použite predvolený koeficient konvekcie **7,7e-06** BTU/s/in²/°F. Zvoľte **rýchlosť rezu (v)** na hodnotu **500****in/sec**, **posuv (f)** na hodnotu **0,012****in/rev** a **hĺbku rezu (d)** na hodnotu **0,02 in** (pozri obr. 3DTL2.2.). Alternatívne môže používateľ namiesto povrchovej rýchlosti zadať aj rýchlosť otáčania obrobku a priemer dielu. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka Nástroj.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0002.jpg' | relative_url }})

Stránka procesu

## Definovanie geometrie vložky

Na stránke „**Nástroj**“ zadajte teplotu nástroja 68F. Používateľ môže importovať geometriu rezných hrán z predtým definovaného súboru s kľúčovými slovami simulácie alebo z databázového súboru pomocou možnosti Importovať objekt ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}). V rámci tohto cvičenia budeme importovať geometriu rezných hrán pomocou možnosti importu geometrie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste importovali geometriu vložky. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a importujte geometriu **DNMA432** zo zložky DEFORM installation \3D\Machining\Insert\EN. Zvoľte smer rezných plôch ako „**Y**“, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), vyberte referenčný bod a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (Pozri obr. 3DTL2.3.)

V tomto laboratórnom cvičení nastavíme polohu rezného nástroja ručne pomocou funkcie polohovania. Prejdite na stránku Ovládacie prvky kliknutím na položku „**Ovládanie**“ v stromovej štruktúre Operácie.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0003.jpg' | relative_url }})

Stránka na výber orientácie geometrie nástroja

## Polohovanie rezného nástroja

Na nástroji použijeme predný sklon -5 stupňov a bočný sklon -5 stupňov. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) na stránke Ovládacie prvky. Na stránke Polohovanie objektu vyberte polohu ![]({{ '/assets/icons/pre_icons/mo_rotational_radio_button.jpg' | relative_url }}) a zadajte otočenie okolo osi **+X** o „**-5**“ stupňov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Teraz zadajte otočenie o „**5**“ stupňov okolo osi **+Z** a opäť kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku „Polohovanie objektu“. Vráťte sa na stránku „Materiál nástroja“ kliknutím na možnosť „Materiál nástroja“ v časti „Nástroj“ v strome operácií.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0004.jpg' | relative_url }})

Polohovanie rezného nástroja

## Priradenie materiálu nástroja

Na stránke „**Materiál nástroja**“ vyberte možnosť „Načítať údaje o materiáli z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), vyberte kategóriu „**Nástroj****Materiál**“ a „**Karbid****(15 % kobaltu)** “ (pozri obr. 3DTL2.5.). Načítate tento materiál a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete sieť.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0005.jpg' | relative_url }})

Načítavanie materiálu pre nástroj

## Vytvorenie siete pre nástroj

Po vytvorení geometrie nástroja vygenerujte sieť s typom „Relative“ s pomerom veľkostí prvkov **7** a cieľovým počtom prvkov **10 000**, ako je znázornené na obr. 3DTL2.6. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby ste dokončili generovanie siete pre obrobok. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku BCC. Na stránke BCC skontrolujte predvolené nastavenie výmeny tepla (Heat exchange) priradené pre nástroj a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku Workpiece.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0006.jpg' | relative_url }})

Vytvorenie siete nástroja

## Geometria obrobku

Na stránke „Obrobok“ definujte obrobok ako plastový objekt s teplotou 68 °F a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte. Na stránke „Geometria obrobku“ kliknite na označenie ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Na stránke „Geometrický primitív obrobku“ zadajte podrobnosti o obrobku. V závislosti od priemeru obrobku môže používateľ zvoliť buď plochý, alebo zakrivený model. Šablóna vás vyzve na zadanie príslušných údajov a v zobrazovacej oblasti vygeneruje nastavenie obrobku. Pre aktuálne laboratórne cvičenie vyberte „**Zjednodušený****režim**“ s **dĺžkou** **0,3** palca. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}), aby ste vytvorili geometriu obrobku (pozri obr. 3DTL2.7.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste túto stránku zatvorili, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku Materiál objektu.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0007.jpg' | relative_url }})

Definovanie geometrie obrobku

## Priradenie materiálu obrobku

Na stránke „Objektový materiál“ vyberte možnosť „Načítať údaje o materiáli z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), vyberte kategóriu „**Oceľ**“ a „**AISI****-1045 (obrábanie)**“ (pozri obr. 3DTL2.8.). Načítate tento materiál a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete sieť.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0008.jpg' | relative_url }})

Načítanie typu materiálu obrobku z knižnice

## Vytvorenie siete pre obrobok

Po vytvorení geometrie obrobku vytvorte sieť s **pomerom veľkostí prvkov** **7** a minimálnou veľkosťou prvku **0,0024** palca (obr. 3DTL2.9.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby ste dokončili vytvorenie siete pre obrobok. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku BCC.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0009.jpg' | relative_url }})

Stránka „Mriežka obrobku“ 

## Stránka „Okrajové podmienky obrobku“

V ponuke „Zobraziť BCC obrobku“ skontrolujte okrajové podmienky, ktoré systém stanovil pre obrobok (pozri obr. 3DTL2.10.), a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky. Všimnite si, že rýchlostné okrajové podmienky sú priradené spodným povrchom vzdialeným od rezných plôch, aby sa zabránilo odletovaniu obrobku. Teplotné okrajové podmienky sú priradené všetkým povrchom s výnimkou rezných plôch.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0010.jpg' | relative_url }})

Predpísaná teplotná okrajová podmienka pre obrobok

## Polohovanie nástroja

V ponuke „Ovládacie prvky“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) a skontrolujte polohu vložky. Ak vložka nie je v kontakte s obrobkom, pomocou metódy ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) nastavte polohu vložky a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Nastavenie opotrebenia nástroja

V tomto laboratórnom cvičení nevypočítavame opotrebenie nástroja, preto zrušte zaškrtnutie políčka „Definovať model na výpočet opotrebenia nástroja“ (pozri obr. 3DTL2.11.) a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na ďalšiu stránku.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0011.jpg' | relative_url }})

Okno nastavení opotrebenia nástrojov

## Stránka s kontaktnými údajmi

Na stránke „Kontakt“ použite predvolené vzťahy. Kliknite na tlačidlo vzťahu **Nástroj – Obrobok** ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) a nastavte koeficient trenia pri **šmyku** na hodnotu **0,5** a **koeficient prenosu tepla na rozhraní** na hodnotu **0,01359** BTU/s/in²/F (ako je znázornené na obr. 3DTL2.12.), kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Riadenie krokov.

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0012.jpg' | relative_url }})

Stránka s kontaktnými údajmi

## Stránka „Ovládanie krokov“

Zaškrtnite políčko „Simulation Controls“ (Ovládacie prvky simulácie), nastavte dĺžku rezu na „**0,3** in“ (plná dĺžka rezu), ostatné hodnoty ponechajte v predvolenom nastavení a pokračujte vo vytvorení databázy.

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu. Pozrite si správu na karte „Message“, ktorá informuje o stave generovania databázy.

## Spustenie simulácie

Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DTL2.13. Použite predvolenú možnosť **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ (od kroku -1) a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“ (Možnosti spustenia), v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/machining_labs/3d_cutting_lab2/image0013.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie môžete sledovať na kartách „Simulation Message“ a „Simulation Log“, pričom sa uistite, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). V priebehu simulácie až do dosiahnutia zadaného dĺžky rezu si môžete v grafickom zobrazení simulácie prezerať priebeh rezania.

## Následné spracovanie

Po dokončení simulácie si výsledky prezrite tak, že prejdete do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov Simulácia. Prejdite si jednotlivé kroky simulácie a sledujte, ako sa čip formoval počas procesu rezania.
