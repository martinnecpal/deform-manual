---
lang: sk
title: "9.10. Ovládacie prvky výstupu"
---

# 9.10. Ovládacie prvky výstupu ![]({{ '/assets/icons/pre_icons/mo_output_controls.jpg' | relative_url }})

9.10.1. Elementárne/uzlové [2D, 3D]

9.10.2. Deformácia [2D, 3D]

9.10.3. Teplo v uzloch [2D, 3D]

## Elementárne/uzlové [2D, 3D]

Ovládanie výstupu, ktoré má používateľ k dispozícii, slúži na zlepšenie reprezentácie stavových premenných v oblasti analýzy a na minimalizáciu chyby interpolácie pri postupoch vytvárania novej siete. Takáto reprezentácia dokáže v porovnaní so súčasnou reprezentáciou založenou na prvkoch lepšie zachovať lokálne gradienty stavových premenných. V aktuálnej verzii si môže používateľ zvoliť reprezentáciu poškodenia, deformácie a napätia ako prvkové + uzlové údaje. To znamená, že okrem aktuálne dostupných prvkových údajov môže používateľ ukladať tieto premenné ako uzlové premenné. Od verzie v11 je možné stavové premenné vypočítať aj v integračných bodoch.

Od verzie V14.0 bola karta „Output Control“ (Ovládanie výstupu) odstránená z časti „Advanced options“ (Pokročilé nastavenia) a je k dispozícii ako samostatná karta, ako je znázornené na obr. 9.10.1. Okrem existujúcich premenných stavu, ako sú napätie, deformácia a poškodenie, je možné vypočítať aj teplo vygenerované na úrovni uzla.  

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_10_output_controls/9_10_image001.jpg' | relative_url }})

Stránka výberu výstupu Elemental/Nodal

## Deformácia [2D, 3D]

Široký výber zložiek deformácie, ktoré môže používateľ zaznamenať, závisí od typu analýzy a objektu. Tieto možnosti pre typický elastoplastický objekt umožňujú používateľovi zaznamenať plastické, elastické a celkové deformácie. V prípade neizotermických modelov s elastoplastickými objektmi je možné pre každý uložený krok simulácie uložiť aj tepelné objemové deformácie. Ak je zapnutá transformácia, je možné uložiť aj zložky deformácie, ktoré vznikajú v dôsledku fázovej transformácie. 

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_10_output_controls/9_10_image002.jpg' | relative_url }})

Možnosti výstupu napätia

Po nastavení v predspracovateľovi sú všetky tieto zložky deformácie (STNOUT), ako je znázornené na obr. 9.10.3, k dispozícii v post-spracovaní na sledovanie bodov, kontúrové grafy a ďalšie bežné možnosti zobrazenia (pozri obr. 9.10.4). 

K týmto dodatočným uzlovým a prvkovým premenným je možné pristupovať z príslušných dialógových okien pre uzly a prvky, ako je znázornené na obr. 9.10.5.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_10_output_controls/9_10_image003.jpg' | relative_url }})

Nastavenie dodatočných zložiek napätia a údajov o prvkoch a uzloch

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_10_output_controls/9_10_image004.jpg' | relative_url }})

Zoznam stavových premenných pre dodatočné zložky deformácie a údaje o prvkoch a uzloch

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_10_output_controls/9_10_image005.jpg' | relative_url }})

Vylepšené dialógové okná uzlov a prvkov vrátane ďalších uzlových premenných a zložiek deformácie.

## Teplo v uzloch [2D, 3D]

Od verzie 14.0 bola v časti Ovládacie prvky simulácie pridaná možnosť „Nodálne teplo“. 

Výkon uzlového tepla je možné vypočítať buď ako časovo integrovaný, alebo pre aktuálny krok. Tieto možnosti má používateľ k dispozícii, ak je na stránke Hlavné nastavenia zaškrtnuté políčko Režim prenosu tepla. 

Funkcia „Integrovaný uzlový tepelný výkon v čase“ je štandardne zapnutá a nie je možné ju vypnúť.

Tepelný výkon v uzle spôsobený rôznymi faktormi počas formovania v konkrétnom kroku je možné vyjadriť ako normalizované zložky tepelného výkonu v uzle. V súčasnosti môžeme znázorniť tepelný výkon v uzle spôsobený deformáciou a trením spolu s celkovým výkonom.

  * **Súčet**: Ak zaškrtnete políčko „Súčet“, počas simulácie sa vypočíta celkové teplo v uzle v aktuálnom kroku a uloží sa do databázy.

  * **Deformácia**: Ak zaškrtnete políčko „Deformácia“, počas simulácie sa vypočíta teplo v uzloch vzniknuté v dôsledku deformácie v aktuálnom kroku a uloží sa do databázy.

  * **Trenie**: Ak zaškrtnete políčko „Trenie“, počas simulácie sa vypočíta teplo v uzloch vzniknuté v dôsledku trenia v aktuálnom kroku a uloží sa do databázy.

Na základe výberu normalizovaných uzlových tepelných zložiek v programe Pre na karte „State variable – Thermal“ (pozri obr. 9.10.6) môžeme vidieť výstupy vybraných normalizovaných uzlových tepelných zložiek (pozri obr. 9.10.7).

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_10_output_controls/9_10_image006.jpg' | relative_url }})

Stránka na výber tepelného výkonu uzlov

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_10_output_controls/9_10_image007.jpg' | relative_url }})

Možnosti normalizovaných teplotných zložiek uzlov.

  
**Súvisiace témy:**

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.6. Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)

[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)
