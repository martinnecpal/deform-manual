---
lang: sk
title: "9.8. Kontrolné súbory"
---

# 9.8. Kontrolné súbory ![]({{ '/assets/icons/pre_icons/mo_control_files.jpg' | relative_url }})

9.8.1. Kategória 1

  * Dvojité rožné obmedzenia

  * Ovládanie prepínača riešiteľa

**[3D]** : V rámci programu DEFORM – Preprocessor existuje mnoho rôznych špecializovaných funkcií, ktoré sa ovládajú prostredníctvom dátových súborov. Účelom tohto typu implementácie je, že tieto funkcie sa používajú len vo veľmi zriedkavých prípadoch a ak sa stanú populárnymi, môžu byť začlenené do kľúčových slov programu DEFORM. Pri použití týchto dátových súborov je funkcia dostupná, ak sa dátový súbor nachádza v tom istom adresári ako aktuálny spustený problém. Keďže nie sú obsiahnuté ani v databáze, ani v súboroch kľúčových slov, kontrolný súbor sa musí presunúť spolu s databázou alebo kľúčovým slovom, aby sa problém spustil s rovnakou funkčnosťou, ak sa na spustenie simulácie používa iný adresár alebo počítač. Pri použití jedného z týchto riadiacich súborov sa automaticky zobrazí varovanie v hlavičke súboru správ, ktoré informuje používateľa o existencii jedného z týchto súborov. 

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_8_control_files/9_8_image001.jpg' | relative_url }})

Nastavenia súborov kategórie 1

Od verzie 6.0 je možné tieto dátové súbory špecifikovať prostredníctvom grafického rozhrania v okne „Control File“ (Pozri obr. 9.8.1.)

## Kategória 1

**Obmedzenia dvoch rohov**

Týmto sa definujú dva uhly, pri ktorých, ak sa uzol dotýka rohu čipu v uhle medzi týmito hodnotami, bude pre tento uzol nastavená podmienka dvojitého kontaktu. Bližšie vysvetlenie nájdete v [Appendix XV: The Double Concave Corner Constraint.](/docs/sk/appendices/appendix_xv_the_double_concave_corner_constraint/)

**Ovládanie prepínača riešiteľa**

Týmto sa definuje niekoľko prípadov, v ktorých je prechod na riešiteľ riedkych matíc blokovaný. Cieľom je zabrániť aktivácii riešiteľa riedkych matíc v prípadoch, keď je úloha príliš rozsiahla.

Súvisiace témy:

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.6. Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)
