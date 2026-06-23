---
lang: sk
title: "23.3. Simulačná grafika"
---

# 23.3. Simulačná grafika

Počas behu simulácie je možné zobraziť druhý najnovší uložený krok (pozri obr. 23.3.1.). Na karte Monitor je možné zobraziť mnoho rôznych premenných, ako napríklad plastické deformácie, rýchlosť plastického deformovania, teplotu a mnoho ďalších. Grafiku simulácie ![]({{ '/assets/icons/simulator_icons/mo_simulation_graphics_icon.jpg' | relative_url }}) je možné otvoriť z hlavného okna grafického rozhrania kliknutím na ikonu ![]({{ '/assets/icons/simulator_icons/mo_simulation_graphics_icon.jpg' | relative_url }}), v rámci možnosti Simulator ![]({{ '/assets/icons/simulator_icons/gui_simulation_graphics_button.jpg' | relative_url }}) alebo v rámci možnosti na karte Preview ![]({{ '/assets/icons/simulator_icons/open_simulation_graphics_label.jpg' | relative_url }}) (pozri obr. 23.3.2.)

V module Simulation Graphics na karte Step view (vedľa karty Monitor) môže používateľ vykonať následné spracovanie krokov uložených v databáze pomocou nástroja na následné spracovanie dostupného na karte Step view, ako je znázornené na obr. 23.3.3.

Užívateľ môže vidieť súbor správ na karte „Simulation Message“ a súbor protokolu na karte „Simulation Log“. 

![]({{ '/assets/images/simulator/23_deform_simulator/23_3_simulation_graphics/image001.jpg' | relative_url }})

Okno so simulačnou grafikou

![]({{ '/assets/images/simulator/23_deform_simulator/23_3_simulation_graphics/image002.jpg' | relative_url }})

Simulačná grafika na karte „Náhľad“

![]({{ '/assets/images/simulator/23_deform_simulator/23_3_simulation_graphics/image003.jpg' | relative_url }})

Karta „Pohľad na krok“ v okne „Simulačná grafika“

Existujú tiež štyri ďalšie spôsoby, ako sledovať simuláciu, a to:

  * Pomocou nástroja Process Monitor zistite číslo aktuálneho kroku.

  * Prečítajte súbor so správami, aby ste zistili číslo aktuálneho kroku a informácie o iterácii.

  * Otvorte simuláciu v postprocesore. Počas simulácie sa súbor databázy premenuje na FOR003 a po opätovnom vytvorení siete a zastavení/ukončení simulácie sa opäť premenuje na pôvodný názov súboru databázy.

  * V závislosti od frekvencie krokov uložených v databáze sa odporúča zvoliť zobrazenie uložených krokov namiesto aktuálneho kroku.

Ďalšie informácie týkajúce sa grafického znázornenia stavových premenných nájdete v kapitole 4.5.2. Stavové premenné a informácie o grafických možnostiach nájdete v [6.2. Integrated Manufacturing Process Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/) a v kapitole 4.2. Grafické zobrazenie.

**Režim objektov**: Možnosť slúžiaca na výber objektov a na nastavenie režimu ich zobrazenia v grafickom rozhraní simulácie. (Pozri obr. 23.3.4.)

![]({{ '/assets/images/simulator/23_deform_simulator/23_3_simulation_graphics/image004.jpg' | relative_url }})

Okno režimu objektu

**Súvisiace témy:**

[Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/)

[Pre-Processor](/docs/en/post_processor/post_processor_mainpg/)

[Integrated Manufacturing Process (MO)](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_integrated_manufacturing_process_layout/)

[Post-Processor](/docs/en/post_processor/post_processor_mainpg/)
