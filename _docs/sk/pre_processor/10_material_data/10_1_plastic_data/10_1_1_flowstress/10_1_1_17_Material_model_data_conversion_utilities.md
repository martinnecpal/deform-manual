---
lang: sk
title: "10.1.1.17. Nástroje na konverziu údajov materiálového modelu"
---

# 10.1.1.17. Nástroje na konverziu údajov materiálového modelu

Ak sú k dispozícii údaje o napätí pri prúdení materiálu vo forme tabuľky údajov Obr. 10.1.1.17.1, používateľ môže tieto údaje previesť na modelovú rovnicu blízkeho tvaru pomocou nástrojov "Conversion". Používateľ môže vybrať model materiálu z dostupného zoznamu a prispôsobiť parametre modelu tak, aby zodpovedali bodom údajov v tabuľke, pomocou techniky prispôsobenia krivky obr. 10.1.1.17.2. Po vykonaní tohto úkonu systém zobrazí obidve formy údajov, s ktorými môžu používatelia ďalej pracovať. Obvykle plné čiary v grafe označujú pôvodné údaje a prerušované čiary z krivky prietoku vypočítanej na základe prispôsobených parametrov modelu.

![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_17_Material_model_data_conversion_utilities/10_1_1_17_Image001.JPG)

Údaje o napätí v toku materiálu vo forme tabuľky v teplotách, rýchlosti deformácie a rozmeroch deformácie

![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_17_Material_model_data_conversion_utilities/10_1_1_17_Image002.JPG)

Výsledky konverzie údajov materiálového modelu

  
Používateľ by si mal uvedomiť, že podobne ako pri iných technikách prispôsobovania kriviek, aj tu platí, že charakter pôvodných údajov a počiatočný odhad (ak ho používateľ môže urobiť) parametrov modelu výrazne ovplyvní kvalitu výsledkov konverzie. Tento nástroj poskytuje aj možnosti na selektívne vykonávanie potrieb fitovania krivky s kontrolou jednotlivých parametrov modelu. Keď používateľ odsúhlasí konverziu, konvertované modelové údaje nahradia pôvodné tabuľkové údaje.

  
**Načítanie súborov s meraniami**

  
Bola pridaná ďalšia funkcia, ktorá umožňuje používateľom importovať viacero súborov s údajmi o nameraných prietokových napätiach, pričom každý z nich je nastavený na danú teplotu a rýchlosť deformácie, ako je znázornené na obr. 10.1.1.17.3.

![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_17_Material_model_data_conversion_utilities/10_1_1_17_Image003.jpg)

Nástroje na nahrávanie nameraných údajov o prietokovom napätí do systému DEFORM

[10.1.1.1. Tabular data format](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_1_Tabular_data_format/)
[10.1.1.2. Power Law](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_2_Power_Law/)
[10.1.1.3. Flow stress for aluminum alloys (Type 1)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_3_Flow_stress_for_aluminum_alloys_Type_1/)
[10.1.1.4. Flow stress for aluminum alloys (Type 2)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_4_Flow_stress_for_aluminum_alloys_Type_2/)
[10.1.1.5. Linear hardening](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_5_Linear_hardening/)

[10.1.1.6. Tabular data format (Atom)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_6_Tabular_data_format_2/)

[10.1.1.7. Generalized Johnson and Cook model](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_7_Generalized_Johnson_and_Cook_model/)
[10.1.1.8. Zerilli-Armstrong model](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_8_Zerilli-Armstrong_model/)
[10.1.1.9. Norton-Hoff Law model](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_9_Norton-Hoff_Law_model/)
[10.1.1.10. Microstructure Flow stress model based on dislocation density and burgers vector](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_10_Microstructure_dislocation_density_and_burgers_vector/)
[10.1.1.11. Texture based flow stress model f(strn,strnrt,O,T)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_11_Texture_based_flow_stress_model_fstrnstrnrtOT/)
[10.1.1.12. User defined Tabular data](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_12_User_defined_Tabular_data/)
[10.1.1.13. User defined Tabular data (Log)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_13_User_defined_Tabular_data_log/)
[10.1.1.14. Bird-Mukharjee-Dorn equation](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_14_Bird-Mukharjee-Dorn_equation/)

[10.1.1.15. User defined flow stress routine](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_15_User_defined_flow_stress_routine/)
[10.1.1.16. Flow stress database](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_16_Flow_stress_database/)
