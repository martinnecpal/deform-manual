---
lang: sk
title: "14.5. Hraničné podmienky vykurovania"
---

# 14.5. Hraničné podmienky vykurovania

14.5.1. Odporové vykurovanie [2D, 3D]

14.5.2. Indukčný ohrev

14.5.3. Indukčný ohrev (BEM)

## Odporové vykurovanie [2D, 3D]

**Napätie BCC**

Určuje pevné napätie nad uzlami alebo prvkami ohraničenými uvedenými hranami. Jednotkami sú volty. Toto sa zvyčajne definuje pre problémy odporového a indukčného typu.

**Aktuálny tok BCC**

Určuje pevnú dominantnú rýchlosť toku prúdu cez prvky ohraničené uvedenými hranami. Jednotky sú Amp/čas.

Od verzie V12 pribudla možnosť PID regulácie do Current flux BCC pre 2D objekty, ako je znázornené na obr. 14.5.1. Pomocou tejto možnosti môže používateľ automaticky riadiť prúdový tok definovaním parametrov PID regulácie, cieľovej teploty a umiestnenia termočlánku.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_5_Heating_Boundary_Conditions/14_5_Image001.jpg)

Možnosť PID prúdového toku [len pre 2D]

## Indukčné vykurovanie

**[2D]** : Po zaškrtnutí políčka Indukčný ohrev v ovládacích prvkoch simulácie sa aktivuje indukčný ohrev v okne vlastností a záložka Ohrev vo Vzťahoch medzi objektmi. Ďalšie informácie nájdete v dokumentoch [16.6. Heating Properties](/docs/sk/pre_processor/16_Object_Properties/16_6_heating_properties/) a [20.3. Interface Resistivity.](/docs/sk/pre_processor/20_Inter-object_Data_Definition/20_3_Interface_Resisitivity/)

**[3D]** : Pre 3D cievky sú k dispozícii počiatočné a koncové plochy bcc (pozri obr. 14.5.2.).

**Začiatok cievky [3D]** : Určuje počiatočný povrch cievky.

**Koncový povrch cievky [3D]** : Určuje koncový povrch cievky.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_5_Heating_Boundary_Conditions/14_5_Image004.jpg)

Indukčné okno BCC pre 3D

## Indukčný ohrev (BEM)

Táto možnosť BCC je k dispozícii len pre proces Induction BEM.

**Vykurovací povrch[2D, 3D]**
Vykurovací povrch BCC určuje povrch cievky, ktorý ohrieva obrobok, a tiež obrobok, ktorý sa ohrieva cievkou.

**Povrch cievky Začiatok [3D]**
Určuje počiatočný povrch cievky.

**Koncový povrch cievky [3D]**
Určuje koncový povrch cievky. Nastavenia indukčného BEM BCC sú uvedené na obr. 14.5.3.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_5_Heating_Boundary_Conditions/14_5_Image002.jpg) ![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_5_Heating_Boundary_Conditions/14_5_Image003.jpg)

(a) (b)

Indukčné (BEM) okno BCC: (a) pre 2D a (b) pre 3D

**Súvisiace témy:**

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.2. Deformation Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)

[14.3. Thermal Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)

[14.4. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)
