---
lang: sk
title: "20.2 Tepelné údaje rozhrania"
---

# 20.2. Tepelné údaje rozhrania

20.2.1. Koeficient prenosu tepla na rozhraní  
20.2.2. Relatívna rotácia

## Koeficient prenosu tepla na rozhraní (IHTCOF)

**[2D, 3D]** : Koeficient prenosu tepla na rozhraní ([IHTCOF](/docs/sk/keyword_documentation/i/ihtcof/)) určuje koeficient prenosu tepla medzi dvoma objektmi, ktoré sú v kontakte. Môže byť zadaný ako konštanta alebo ako funkcia času či tlaku na rozhraní. Koeficient prenosu tepla na rozhraní je vo všeobecnosti zložitá funkcia, ktorú určuje tlak na rozhraní, miera kĺzania a teplota na rozhraní. Ak sú tieto údaje k dispozícii, je možné ich zadať vo forme tabuľky.

Ak nie sú k dispozícii žiadne údaje, hodnoty 0,004 (anglický systém) alebo 11 (systém SI) by mali poskytnúť primerané výsledky (pozri obr. 20.2.1. a obr. 20.2.2.).

##  Relatívna rotácia (FRCROT)

**[2D]:** Tento parameter ([FRCROT](/docs/sk/keyword_documentation/f/frcrot/)) určuje rozdiel v otáčaní dvoch objektov okolo osi symetrie. Jednotky sú radiány za sekundu. Napríklad, ak sa horná matrica otáča a zároveň sa pohybuje smerom nadol, rozhranie medzi hornou matricou a polotovarom by malo mať rovnakú uhlovú rýchlosť (rad/s) ako horná matrica. To umožňuje programu DEFORM vypočítať tvorbu tepla z trenia spôsobeného rotáciou pri procesoch, ako je zváranie zotrvačnosťou. Relatívna rotácia môže byť definovaná ako konštanta alebo ako funkcia času.

Modelovanie zvárania zotrvačným zváraním je možné pomocou programu DEFORM, odporúča sa však vykonať ho s využitím formulácie torzných prvkov.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_2_interface_thermal_data/image001.jpg' | relative_url }})

Medziobjektové tepelné okno pre 2D

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_2_interface_thermal_data/image002.jpg' | relative_url }})

Medziobjektové tepelné okno pre 3D

**Súvisiace témy:**

[20\. Inter-Object Data Definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/)

[20.1. Friction and Contact criteria](/docs/sk/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/)

[20.3. Interface Resisitivity](/docs/sk/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/)

[20.4. Tool Wear](/docs/sk/pre_processor/20_inter-object_data_definition/20_4_tool_wear/)

[20.5. Rigid Contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/)
