---
lang: sk
title: "17. Inicializácia údajov objektu"
---

# 17\. Inicializácia údajov objektu

17.1. Karta Hlavné premenné stavu

17.2. Použitie karty Premenné stavu uzla

17.3. Použitie karty Premenné stavu prvku

17.4. Karta Premenné stavu mikroštruktúry

17.5. Ostatné štátne premenné Tab

Používateľ môže inicializovať údaje objektu pomocou inicializačnej stránky, okna uzlových údajov, okna prvkových údajov alebo interpolovať údaje objektu z DB pomocou interpolácie údajov. V okne inicializácie je na inicializáciu k dispozícii niekoľko stavových premenných, ktoré sa bežne používajú, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posunutie, hustota, používateľská uzlová premenná, používateľská prvková premenná a veľkosť zrna mikroštruktúry a veľkosť častíc. Používateľ môže inicializovať aj hodnotu priemernej rýchlosti deformácie a hraničnej rýchlosti deformácie v záložke "Other" (Iné) na stránke "Initialize" (Inicializovať).

Používateľ môže inicializovať hodnoty týchto stavových premenných definovaním v poli vedľa a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Hodnota sa inicializuje pre celý objekt. Na obr. 17.1. sú znázornené rôzne stavové premenné, ktoré sú k dispozícii v okne Inicializovať. Pre stavové premenné, ako je rýchlosť a posunutie, poskytnuté vstupné polia toľko, koľko je rozmerov, používateľ musí definovať smerové hodnoty premenných v príslušných poliach a potom kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) sa vypočíta celková rýchlosť a posunutie.

Ak stavové premenné nie sú k dispozícii na stránke inicializácie objektu alebo ak chce používateľ použiť možnosti výberu na selektívne použitie stavovej premennej na časť objektu, potom môže používateľ použiť dátové okná Uzol a Prvok, viac informácií o tom, ako inicializovať stavové premenné v oknách Uzol a Prvok, nájdete v [Object node Data](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [Object element Data](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/).

## **Tabuľka s hlavnými premennými stavu**

V záložke **Major** môže používateľ inicializovať stavové premenné teplota, deformácia, napätie, poškodenie, posunutie a hustota (pozri obr. 17.1).

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_image001.jpg' | relative_url }})

2D objekt Inicializácia okna Major

## **Použiť kartu Premenné stavu uzla**

V záložke **Užívateľský uzol** sa v poli užívateľského uzla zobrazia premenné uzla definované používateľom. Používateľ môže inicializovať hodnoty premenných uzla definovaných používateľom. (Pozri obr. 17.2.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_image002.jpg' | relative_url }})

Objekt inicializuje okno uzla User

## **Použiť kartu Premenné stavu prvku**

V záložke **Užívateľský prvok** sa v poli užívateľského prvku zobrazia premenné prvku definované používateľom. Používateľ môže inicializovať hodnoty premenných prvkov definovaných používateľom. (Pozri obr. 17.3.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_image003.jpg' | relative_url }})

Objekt inicializuje okno uzla User

## **Premenné stavu mikroštruktúry na karte**

Na karte **Mikroštruktúra** môže používateľ inicializovať hodnoty premenných Grain size (veľkosť zrna) a Particle size (veľkosť častíc). (Pozri obr. 17.4.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_image004.jpg' | relative_url }})

Inicializácia objektu Okno mikroštruktúry

## **Ostatné premenné štátu Tab**

V záložke **O****ther** môže používateľ inicializovať hodnotu Priemerná miera deformácie a Obmedzujúca miera deformácie (pozri obr. 17.5).

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_image005.jpg' | relative_url }})

Inicializácia objektu Iné okno

**Súvisiace témy:**

[17.1. Node Data Window](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/)

[17.2. Element Data Window](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/)

[17.3. Data interpolation Window](/docs/sk/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/)
