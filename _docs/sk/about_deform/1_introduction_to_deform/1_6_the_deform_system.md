---
lang: sk
title: "1.6. Systém DEFORM"
---

# 1.6. Systém DEFORM

1.6.1. Predbežné spracovanie

1.6.2. Spustenie simulácie

1.6.3. Následné spracovanie

Systém DEFORM pozostáva z troch hlavných komponentov:

## Predbežné spracovanie

Preprocesor na vytváranie, zostavovanie alebo úpravu údajov potrebných na analýzu simulácie a na generovanie požadovaného databázového súboru. DEFORM [pre-processor](/docs/sk/pre_processor/pre-processor_mainpg/) používa grafické používateľské rozhranie na zostavenie údajov potrebných na spustenie simulácie. Vstupné údaje zahŕňajú,

**Opis objektu**

[Object description](/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/) zahŕňa všetky údaje súvisiace s objektom vrátane [geometry](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/), [mesh](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/), teploty, [material](/docs/sk/pre_processor/10_material_data/10_material_data/) atď.

**Dáta o materiáli**

[Material](/docs/sk/pre_processor/10_material_data/10_material_data/)[ data](/docs/sk/pre_processor/10_material_data/10_material_data/) obsahuje údaje opisujúce správanie sa materiálu za podmienok, ktoré sa v ňom počas deformácie primerane vyskytnú.

**Vnútorné podmienky objektu**

[Inter object](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) podmienky popisujú, ako na seba objekty vzájomne pôsobia, vrátane kontaktu, trenia a prenosu tepla medzi objektmi.

**Simulačné ovládacie prvky**

[Simulation controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/) obsahuje inštrukcie o metódach, ktoré má DEFORM použiť na riešenie problému, vrátane podmienok prostredia spracovania, aké fyzikálne procesy sa majú modelovať, koľko diskrétnych časových krokov sa má použiť na modelovanie procesu atď.

**Interné údaje o materiáli**

Údaje [Inter material](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/) opisujú fyzikálny proces premeny jednej fázy materiálu na iné fázy toho istého materiálu v procese tepelného spracovania. Napríklad premena austenitu na perlit, bainit a martenzit.

**Integrovaný výrobný proces (MO)**

DEFORM [Integrated Manufacturing Process (MO)](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/)**** poskytuje používateľsky prívetivé rozhranie na zostavenie mnohých po sebe nasledujúcich operácií pri počiatočnom nastavení a ich postupnú simuláciu bez interakcie používateľa. Prostredie MO uľahčuje používateľovi prenášať objekty medzi operáciami a spájať rôzne operácie na prenos údajov.

## Spustenie simulácie

Simulačný mechanizmus na vykonávanie numerických výpočtov potrebných na analýzu procesu a zápis výsledkov do databázového súboru. Simulačný mechanizmus načíta databázový súbor, vykoná aktuálny výpočet riešenia a pripojí príslušné údaje o riešení do databázového súboru. Simulačný motor tiež bezproblémovo spolupracuje so systémom automatického generovania siete (AMG), ktorý v prípade potreby generuje novú sieť MKP na obrobku. Počas behu simulačného motora sa do súborov správ (.MSG) a protokolov (.LOG) zapisujú informácie o stave vrátane prípadných chybových hlásení.

**Simulačný motor**

Simulačný motor je program, ktorý skutočne vykonáva numerické výpočty na riešenie problému. Simulačný mechanizmus číta vstupné údaje z databázy a potom zapisuje údaje o riešení späť do databázy. Počas svojho behu vytvára dva užívateľsky čitateľné súbory, ktoré sledujú jeho priebeh.

**Záznamové súbory (LOG)**

Pri spustení simulácie sa vytvárajú súbory denníka. Obsahujú všeobecné informácie o časoch začiatku a konca, prípadných remeshingoch, môžu obsahovať chybové hlásenia, ak sa simulácia neočakávane zastaví, a typ spustenej úlohy MKP (32-bitová alebo 64-bitová simulácia) v prípade 3D úloh.

**Súbory správ (MSG)**

Súbory správ sa vytvárajú aj počas simulácie. Obsahujú podrobné informácie o správaní simulácie a môžu obsahovať informácie o dôvodoch zastavenia simulácie.

## **Postprocesor**

Postprocesor na čítanie databázového súboru zo simulačného stroja a grafické zobrazenie výsledkov a na extrakciu numerických údajov. Postprocesor sa používa na zobrazenie simulačných údajov po spustení simulácie. Postprocesor obsahuje grafické používateľské rozhranie na zobrazenie geometrie, údajov o poli, ako je deformácia, teplota, napätie, a ďalších simulačných údajov, ako je zaťaženie matrice. Postprocesor možno použiť aj na extrakciu grafických alebo číselných údajov na použitie v iných aplikáciách. Postprocesor sa používa aj na zobrazenie a extrakciu údajov z výsledkov simulácie v databázovom súbore. Poskytuje používateľovi prostredie na vytváranie 3D PDF správ o výsledkoch simulácie, interpretáciu výsledkov v databáze pomocou PIP, vykresľovanie výsledkov v oblasti záujmu, extrakciu údajov kupónov na vyhodnotenie mikroštruktúry a mechanických vlastností konkrétneho výrezu spolu so všeobecnými funkciami postprocesora.

**Súvisiace témy:**

[Pre-Processor](/docs/sk/pre_processor/7_introduction_to_pre-processor/)

[Post-Processor](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[Object Description](/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/)

[Material Data](/docs/sk/pre_processor/10_material_data/10_material_data/)

[Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Inter-Object Data](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[Simulation Controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

[Simulator](/docs/sk/simulator/23_deform_simulator/23_introduction_to_deform_simulator/)

[2D Stub Shaft Labs](/docs/sk/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/)

[3D Stub Shaft Labs](/docs/sk/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/)
