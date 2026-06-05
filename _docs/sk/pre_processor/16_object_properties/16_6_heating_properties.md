---
lang: sk
title: "16.6. Vykurovacie vlastnosti"
---

# 16.6. Vykurovacie vlastnosti

16.6.1. Aktuálna frekvencia

16.6.2. Objemový poplatok

16.6.3. Definícia údajov

[**2D, 3D**]: Ak sa vyžadujú výpočty indukčného ohrevu, je potrebné ho najprv zapnúť v ovládacích prvkoch simulácie a až potom definovať súvisiace hodnoty objektu, ako je napríklad frekvencia prúdu (pozri obr. 16.6.1 a obr. 16.6.2). Riešiteľ CG je tiež možnosťou riešenia modelov indukčného ohrevu a je schopný riešiť modely s primeranou veľkosťou.

Výber režimu simulácie indukčného ohrevu nájdete v časti [Fig. 9.1.3.](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#Fig._9.1.3. Simulation Controls window - Heating). Elektrické a magnetické vlastnosti materiálu nájdete v časti [10.8. Electromagnetic data](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/).

Motor DEFORM FEM teraz dokáže spracovať modely indukčného ohrevu s dvojfrekvenčnými vstupnými údajmi pre aktuálnu frekvenciu v 2D a 3D.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_6_Heating_Properties/16_6_Image001.jpg)

Okno vlastností objektu indukčného ohrevu pre nastavenie jednej frekvencie

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_6_Heating_Properties/16_6_Image002.jpg)

Okno vlastností indukčného ohrevu pre nastavenie dvojitej frekvencie

## Aktuálna frekvencia [2D, 3D]

Určuje frekvenciu prúdu pre vykurovanie objektu. Môže to byť konštantná hodnota alebo funkcia času.

## Objemový náboj [2D, 3D]

Objemové nabíjanie môže prebiehať v troch režimoch:

  * **Hustota prúdu** : Je to miera hustoty elektrického prúdu. Je definovaná ako vektor, ktorého veľkosť je elektrický prúd na plochu prierezu. Jednotkou prúdovej hustoty je Amp/mm2 alebo Amp/inch2 v 2d axi-symetrickom modeli a 3d modeli. V prípade 2d rovinného modelu bude prierezom cievky hranová čiara a hrúbka je jednotkou dĺžky, takže jednotkou prúdovej hustoty bude Amp/mm alebo Amp/inch.
  * **Vstupný výkon** : Elektrický výkon, ktorý elektrický nástroj odoberá zo zdroja energie.
  * **Pokles napätia** : Je to zníženie napätia v elektrickom obvode medzi zdrojom a záťažou.

## Definícia údajov [2D, 3D]

Definícia údajov môže byť konštantná alebo funkcia času pre objemový náboj typu Vstupný výkon, Hustota prúdu a Úbytok napätia.

**Súvisiace témy:**

[16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.2. Thermal properties](/docs/sk/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/sk/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/sk/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.5. Hardness Properties](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.7. Symmetry Properties](/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/sk/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/sk/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/sk/pre_processor/16_object_properties/16_10_user/)

[Material Electrical and magnetic properties](/docs/sk/pre_processor/10_Material_Data/10_8_Elec_Mag_Data/10_8_Elec_Mag_Data/)

[10\. Material Data](/docs/sk/pre_processor/10_Material_Data/10_Material_Data/)
