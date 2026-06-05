---
lang: sk
title: "10.7. Údaje o tvrdosti"
---

# 10.7. Údaje o tvrdosti

10.7.1. Tvrdosť jednotlivých fáz (HDNPHA)

10.7.2. Jominyho krivka (JOMINY)

10.7.3. Čas chladenia (HDNTIM)

Existujú dve metódy, ktorými možno určiť tvrdosť predmetu po ochladení. Obrazovka, na ktorej sa tieto údaje nastavujú, je znázornená na obr. 10.7.1. Prvá metóda spočíva v zadaní tvrdosti každej fázy (HDNPHA) v zmesi a DEFORM použije zákon zmesi na určenie tvrdosti každého prvku. Druhou metódou je použitie experimentálnych výsledkov z Jominyho krivky a závislosti času chladenia od vzdialenosti na určenie tvrdosti počas chladenia. Počiatočnú tvrdosť a typ chladenia objektu možno pridať z okna Object Element (Prvok objektu). Metódu výpočtu tvrdosti je možné určiť pre každý objekt v okne Object Properties (Vlastnosti objektu) - Hardness (Tvrdosť), Keď je v záložke [Object properties – Hardness](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/) zvolená možnosť "Use Jominy curves (Použiť Jominyho krivky)" alebo "Only cooling time (Iba čas chladenia)", vyžadujú sa vstupy údajov o materiáli Jominyho krivka aj čas chladenia.

  
V programe DEFORM možno použiť akúkoľvek jednotku tvrdosti, ak sa použije v spojení s koeficientmi, ktoré boli kalibrované na konkrétnu jednotku tvrdosti. Napríklad ak boli koeficienty určené na základe experimentálnych údajov HRC, potom sa v simulácii DEFORM, ktorá používa tieto koeficienty, musí použiť jednotka tvrdosti HRC.  
Hodnoty tvrdosti podľa Brinella a Vickersa možno previesť na jednotky MPa vynásobením hodnôt tvrdosti metrickou štandardnou hodnotou tiaže (9,80665 m/s^2). Ak sú požadované jednotky KSI, vykonajte ďalší prevod z MPa na KSI.

![]({{ '/assets/images/pre-processor/10_material_data/10_7_hardness_data/10_7_image001.jpg' | relative_url }})

Okno s údajmi o tvrdosti materiálu

## Tvrdosť každej fázy (HDNPHA)

Tvrdosť každej fázy (skupiny materiálov) je možné špecifikovať. Tvrdosť každej fázy ([HDNPHA](/docs/sk/keyword_documentation/h/hdnpha/)) možno definovať ako konštantu alebo ako funkciu obsahu atómov alebo teploty alebo hustoty alebo teploty a atómov. Tvrdosť objektu sa vypočíta na základe objemového podielu každej fázy v prvku a na základe tvrdosti každej fázy.

  
Z verzie 14.0. možno tvrdosť odhadnúť pomocou modelu pevného roztoku so zrazeninami, ako je znázornené na obr. 10.7.2.

![]({{ '/assets/images/pre-processor/10_material_data/10_7_hardness_data/10_7_image002.jpg' | relative_url }})

Pevný roztok s možnosťou zrážania

## Krivka Jominy (JOMINY)

Tu sa musí uviesť závislosť tvrdosti od vzdialenosti pre Jominyho skúšobnú vzorku, ako je znázornené na obr. 10.7.3. Jominyho krivka je určenie tvrdosti v Jominyho vzorke v určitej vzdialenosti od chladného konca. Jominyho krivka je preto užitočná pri určovaní tvrdosti materiálu v závislosti od vzdialenosti od vodou chladeného konca.

![]({{ '/assets/images/pre-processor/10_material_data/10_7_hardness_data/10_7_image003.jpg' | relative_url }})

Stránka s funkciou krivky Jominy

## Čas chladenia (HDNTIM)

Pomocou možnosti Jominyho vzdialenosť vs. čas chladenia definujte čas chladenia v závislosti od vzdialenosti pre Jominyho skúšobnú vzorku, ako je znázornené na obr. 10.7.4. Pomocou údajov o Jominyho krivke ([JOMINY](/docs/sk/keyword_documentation/j/jominy/)) a údajov o čase chladnutia ([HDNTIM](/docs/sk/keyword_documentation/h/hdntim/)) DEFORM odhadne tvrdosť objektu počas chladnutia.

![]({{ '/assets/images/pre-processor/10_material_data/10_7_hardness_data/10_7_image004.jpg' | relative_url }})

Vzdialenosť Jominy vs. čas chladenia

**Súvisiace témy:**

[16.5. Hardness Properties](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/)

[17.2. Element Data Window](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/)
