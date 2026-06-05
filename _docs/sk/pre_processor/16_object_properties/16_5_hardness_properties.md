---
lang: sk
title: "16.5. Typ odhadu tvrdosti"
---

# 16.5. Typ odhadu tvrdosti

[2D, 3D]: (Pozri obr. 16.5.1 až obr. 16.5.5.)

  * Objemový podiel rôznych fáz
  * Údaje o krivke Jominy
  * Čas chladenia
  * Pevný roztok so zrážaním

Údaje o tvrdosti materiálu možno definovať vo Vlastnostiach materiálu príslušného materiálu objektu a budú sa odhadovať na základe typu odhadu zvoleného v časti Vlastnosti príslušného objektu, Obr. 16.5.1. zobrazuje možnosti typu odhadu dostupné v časti Tvrdosť vo Vlastnostiach objektu. Je tam uvedený popis metódy predpovedania tvrdosti. Ďalšie informácie o definovaní tvrdosti v časti Vlastnosti materiálu nájdete v časti [10.7. Hardness data.](/docs/sk/pre_processor/10_Material_Data/10_7_Hardness_Data/10_7_Hardness_Data/)

  
**Referenčná počiatočná teplota, koncová teplota** : Horné a dolné hodnoty teploty pre Jominyho alebo krivky predpovede tvrdosti v čase chladnutia.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image001.jpg)

Typ odhadu tvrdosti v okne Vlastnosti objektu

  1. "**Použite objemové podiely** ": Tvrdosť sa vypočíta na základe jednotlivých fáz (pravidlo zmesi), ktoré sa vyvíjajú počas procesu kalenia v príslušnom prvku, s použitím údajov o tvrdosti definovaných vo vlastnostiach materiálu príslušnej fázy.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image003.jpg)

Použitie kriviek typu jominy Odhad tvrdosti

  1. "**Používajte krivky jominy** ": Na odhad tvrdosti pomocou Jominyho kriviek, ktoré sa použijú na aktiváciu rozsahu chladenia, je potrebné definovať referenčnú počiatočnú teplotu a koncovú teplotu. Čas strávený bodom materiálu v teplotnom rozsahu + Jominyho údaje uvedené v časti vlastnosti materiálu sa použijú na výpočet tvrdosti, pozri obr. 16.5.3. Čas strávený bodom materiálu v tomto teplotnom rozsahu a rýchlosť teplotného rozsahu je základom pre výpočty času a rýchlosti chladnutia.

  1. Ak je teplota vyššia ako referenčná vysoká teplota, príznak tvrdosti sa nastaví na -2.
  2. Keď teplota dosiahne (rovnú alebo nižšiu) referenčnú vysokú teplotu, príznak "Tvrdosť" sa nastaví na -3 a tento okamžitý čas sa zaznamená do "času chladnutia". Tento príznak a čas ochladzovania sa nastaví len raz a zachová sa pre nasledujúce kroky, kým teplota nedosiahne referenčnú nízku teplotu, pozri obr. 16.5.4.
  3. Ak sa materiálový bod nachádza v referenčnom teplotnom rozsahu, čas chladnutia udáva len časovú značku vstupu materiálového bodu do tohto teplotného rozsahu, pozri obr. 16.5.4.
  4. Keď sa bod materiálu úplne ochladí pod ochladením, aktualizuje sa správna hodnota tvrdosti, pozri obr. 16.5.4.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image002.jpg)

Použitie odhadu tvrdosti typu jominyho krivky

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image006.jpg)

Výsledky simulácie s použitím jominyho krivky typu Odhad tvrdosti

  1. "**Pouhý čas chladenia** ": Referenčná počiatočná teplota a koncová teplota sa používa na aktiváciu rozsahu chladenia. Čas, ktorý strávil bod materiálu v tomto teplotnom rozsahu + poskytnuté údaje Jominy, je základom pre čas chladenia, pozri obr. 16.5.5.. Nevypočítava sa žiadna tvrdosť.

V dialógu údajov o prvku,

  1. Ak je teplota vyššia ako referenčná vysoká teplota, príznak tvrdosti sa nastaví na -2.
  2. Keď teplota dosiahne (rovnú alebo nižšiu) referenčnú vysokú teplotu, príznak "Tvrdosť" sa nastaví na -3 a tento okamžitý čas sa zaznamená do "času chladnutia". Tento príznak a čas ochladzovania sa nastaví len raz a zachová sa pre nasledujúce kroky, kým teplota nedosiahne referenčnú nízku teplotu.
  3. Keď teplota dosiahne (rovnakú alebo nižšiu) referenčnú nízku teplotu, príznak "Tvrdosť" sa nastaví na -4, čas, ktorý uplynul od dosiahnutia referenčnej vysokej teploty po dosiahnutie referenčnej nízkej teploty, sa zaznamená do "Času chladenia". Tento príznak a čas chladenia sa nastaví len raz a v ďalších krokoch sa zachová. V každom kroku simulácie sa rozdelí na 10 čiastkových krokov, aby sa čas do dosiahnutia referenčnej teploty dal určiť presnejšie.

Ak je príznak "Tvrdosť" -3, "čas chladenia" znamená čas do dosiahnutia referenčnej vysokej teploty; ak je príznak "Tvrdosť" -4, "čas chladenia" znamená časový interval od referenčnej vysokej teploty po referenčnú nízku teplotu.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image003.jpg)

Odhad tvrdosti len podľa času chladenia

  1. Pri možnosti "**Tvrdý roztok so zrazeninami** " sa tvrdosť vypočíta na základe modelu zrážania, pozri obr. 16.5.6..

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image003.jpg)

Pevný roztok s typom zrazeniny Odhad tvrdosti

**Súvisiace témy:**

[16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.2. Thermal properties](/docs/sk/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/sk/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/sk/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.6. Heating Properties](/docs/sk/pre_processor/16_object_properties/16_6_heating_properties/)

[16.7. Symmetry Properties](/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/sk/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/sk/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/sk/pre_processor/16_object_properties/16_10_user/)

[Material Hardness properties](/docs/sk/pre_processor/10_Material_Data/10_7_Hardness_Data/10_7_Hardness_Data/)
