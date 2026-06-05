---
lang: sk
title: "18.1. Boolean"
---

# 18.1. Logická operácia![]({{ '/assets/icons/pre_icons/mo_boolean_icon.jpg' | relative_url }})

18.1.1. Logická operácia pre 2D objekt

18.1.2. Logická operácia pre 3D objekt

Čo robiť po vykonaní logickej operácie

**[2D, 3D]** Táto funkcia umožňuje používateľovi odčítať objem zo siete objektu od geometrie iného objektu alebo logického člena vzhľadom na rovinu (možnosť je k dispozícii len pre 3D) alebo vrstvy Slice (možnosť je k dispozícii len pre 3D)

**Definície:**

**Objekt s mriežkou:** Objekt s pevnou mriežkou, ktorý definuje objem objektu.

**Geometrický objekt:** Objekt s definíciou iba povrchu.

Všimnite si, že niektoré objekty môžu mať obidve definície, napríklad tuhý objekt so zapnutými tepelnými výpočtami. Geometria sa používa na výpočty deformácie a sieť sa používa na tepelné výpočty. V prípade plastického, pružného, porézneho alebo elasto-plastického objektu sa geometria používa len na účely tvorby siete a nepoužíva sa na simulačné výpočty.

Dialógové okno Boolean operation je k dispozícii na hornej lište nástrojov a je potrebné vybrať objekt, od ktorého sa má odčítať, a vybrať tlačidlo Boolean ![]({{ '/assets/icons/pre_icons/mo_boolean_icon.jpg' | relative_url }}).

## Logická operácia pre 2D objekt

Existuje len jeden spôsob, ako vykonať tento logický výpočet z 2D:

**Boolean vzhľadom na iný objekt** **:** užívateľ by mal vybrať objekt, ktorý sa má odčítať. Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (pozri obr. 18.1.1.). V nasledujúcej časti Pozri obr. 18.1.2. zobrazujúci boolean obrobku vzhľadom na objekt Top.

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image001.jpg' | relative_url }})

Boolean Obrobok z horného dielu (pred Boolean)

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image002.jpg' | relative_url }})

Boolean Obrobok z horného dielu (po Boolean)

Poznámka:

V niektorých zriedkavých prípadoch, keď logická definícia presne zodpovedá umiestneniu uzlov, môžu niektoré uzly pretínať vami definovanú logickú rovinu. V takom prípade to vyrieši mierne upravenie polohy roviny (len 1e-6 palcov alebo mm).

## Logická operácia pre 3D objekt

Pre boolean 3D objekt máme tri možnosti:

  * **Odčítanie objektu** : pomocou tejto funkcie by mal používateľ vybrať objekt, ktorý sa má od aktuálne vybraného objektu odčítať. Po výbere objektu môže používateľ kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

V možnosti odčítania objektov máme dva typy logických metód:

  * **Geometria (nová metóda)** : Pri použití možnosti založenej na geometrii, ak vykonáme logickú operáciu, vykoná sa logická operácia a potom lokálne premeranie podľa definovaného vstupu ( pozri obr. 18.1.3.). Tým sa vytvorí hladká sieť, ako je znázornené na obr. 18.1.5.

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image008.jpg' | relative_url }})

3D Geometria objektu (nová metóda) Booleovská operácia

  * **Solid mesh based (stará metóda)** : Pri použití metódy Solid mesh based (založená na Solid mesh), ak vykonáme operáciu Boolean (pozri obr. 18.1.4.), vykoná sa Boolean a potom sa vygeneruje iba Solid mesh, pozri obr. 18.1.5.

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image006.jpg' | relative_url }})

3D operácia Pevná sieť (stará metóda) Booleovská operácia

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image007.jpg' | relative_url }})

Generovanie siete po booleovskej operácii s inou možnosťou typu objektu Subtract

  * **Rozrezanie pomocou roviny** : Používateľ môže tiež boolovský objekt definovať len rovinou, aj keď objekt nie je k dispozícii pomocou tejto možnosti, používateľ by mal vybrať rovinu a potom definovať bod a normálu k boolovskej rovine (pozri obr. 18.1.6.). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). (Pozri obr. 18.1.7.)

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image009.jpg' | relative_url }})

Výrez 3D objektu s rovinnou logickou operáciou (Pred logickou operáciou)

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image010.jpg' | relative_url }})

Výrez 3D objektu s rovinnou logickou operáciou (After Boolean)

  * **Vrstvy plátkov:** Pomocou možnosti vrstvy plátkov môžeme vytvoriť viacero plátkov objektu a po rozrezaní objektov môžeme vygenerovať novú sieť pre každú vrstvu plátkov definovaním nastavení siete vo výstupných možnostiach. Táto možnosť je užitočná pre simulácie aditívnej výroby a pre objekty, ktoré majú viacero materiálov, podobne ako viacvrstvové kompozity. Nasledujúci príklad demonštruje rozrezanie ložiska na 6 vrstiev (pozri obr. 18.1.8).

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image003.jpg' | relative_url }})

Stránka s vrstvami plátkov

Jednoduchý blok Bearing rozrežeme na 6 vrstiev pomocou možnosti Slicing layers.

  * Po vygenerovaní **Tet Mesh** pre blok ložiska otvorte možnosť **Boolean** a vyberte možnosť Slice layers. Definujte počet vrstiev ako 6 a s údajmi o sieti kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Pozri obr. 18.1.9.

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image004.jpg' | relative_url }})

Blok ložiska nakrájaný na plátky pomocou možnosti Slice layers

  * Teraz sa vráťte na stránku **Geometria**, vyberte položku **Vyšetrenie** a sledujte počet plôch ložiskového bloku. (Pozri obr. 18.1.10.)

![]({{ '/assets/images/pre-processor/18_object_manipulation_tools/18_1_boolean/18_1_image005.jpg' | relative_url }})

Preskúmať okno

**Čo robiť po logickej operácii?**

V rezaných rovinách sa zobrazí zle štruktúrovaná sieť. Je to preto, že bolo vyrezaných veľa prvkov. Ak chcete zlepšiť kvalitu siete, vykonajte nasledujúce činnosti (Z programu DEFORM V12 možno na generovanie hladšej siete použiť metódu založenú na geometrii ):

  1. Stlačte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), keď je logická operácia uspokojivá.

  2. Prejdite na položku Geometria

  3. Extrahujte sieť (účelom je zabrániť použitiu definície geometrie na vytvorenie siete)

  4. Prejdite na mesh a vytvorte mesh objektu (nevykonávajte manuálne remeshovanie)

  5. Prejdite na [Data Interpolation](/docs/sk/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/), aby ste obnovili stavové premenné.

Potom by ste mali úspešne aktualizovať svoju časť s odstráneným požadovaným zväzkom.

**Súvisiace témy:**

[18\. Object Manipulation Tools](/docs/sk/pre_processor/18_object_manipulation_tools/18_object_manipulation_tools/)

[18.2. Slicing](/docs/sk/pre_processor/18_object_manipulation_tools/18_2_slicing/)

[18.3. Mirror Merge](/docs/sk/pre_processor/18_object_manipulation_tools/18_3_mirror_merge/)

[17.3. Data Interpolation Window](/docs/sk/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/)

[13.2. 3D Tet Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/)
