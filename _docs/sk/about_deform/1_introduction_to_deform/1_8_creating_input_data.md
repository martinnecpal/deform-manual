---
lang: sk
title: "1.8. Vytvorenie vstupných údajov"
---

# 1.8. Vytvorenie vstupných údajov

Údaje do DEFORM [Pre-Processor]({{ '/docs/sk/pre_processor/7_introduction_to_pre-processor/' | relative_url }}) môžete zadávať niekoľkými spôsobmi. V závislosti od požiadaviek konkrétneho problému sa často používa kombinácia nasledujúcich metód.

**Ručný vstup**

Ponuky [pre-processor]({{ '/docs/sk/pre_processor/7_introduction_to_pre-processor/' | relative_url }}) obsahujú vstupné polia pre takmer všetky možné vstupné údaje v programe DEFORM. Používateľ môže zadať, zobraziť alebo upraviť ktorúkoľvek z týchto hodnôt. Diskusie ku každému poľu sú obsiahnuté v referenčnej časti tejto príručky.

**Vstupný súbor s kľúčovými slovami**

Väčšina dátových polí v preprocesore DEFORM zodpovedá priamo kľúčovému slovu DEFORM. Jednotlivé kľúčové slová opisujú veľmi špecifické informácie o konkrétnej charakteristike objektu, vzťahu [simulation control]({{ '/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/' | relative_url }}), [material characteristic]({{ '/docs/sk/pre_processor/10_material_data/10_material_data/' | relative_url }}) alebo [inter object]({{ '/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/' | relative_url }}). Údaje o kľúčových slovách možno uložiť do súboru kľúčových slov (.KEY). Súbor kľúčových slov je ľudsky čitateľná (ASCII) reprezentácia údajov simulácie DEFORM.

Typický formát kľúčového slova je:

[Názov kľúčového slova] [Parametre kľúčového slova] [Predvolené údaje]

[Údaje]

[Údaje]...

Súbor s kľúčovými slovami môže obsahovať kompletný súbor simulačných údajov alebo môže obsahovať len jedno alebo niekoľko konkrétnych kľúčových slov.

**Skladanie súborov s kľúčovými slovami**

Keď sa súbor s kľúčovým slovom načíta do preprocesora, zmenia sa len konkrétne dátové polia uvedené v danom kľúčovom slove; ostatné údaje sa nezmenia. Takto je možné zostaviť kompletný súbor údajov o probléme načítaním jedného súboru s kľúčovými slovami, ktorý obsahuje len údaje o jednom objekte, ďalšieho súboru s kľúčovými slovami, ktorý obsahuje údaje o materiáloch atď.

Ak chcete uložiť konkrétne prvky súboru s kľúčovými slovami, je potrebné uložiť celý súbor a potom pomocou textového editora, ako je Notepad, VI, Emacs alebo iný ekvivalent, odstrániť nežiaduce informácie. Funkcie načítania a uloženia súboru kľúčových slov v hlavnej ponuke preprocesora načítajú alebo uložia celý súbor údajov. Ak chcete načítať čiastočné súbory kľúčových slov, použite možnosť Import alebo Importovať kľúčové slová z [File menu.](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#8.1.1._File_Menu)

**Ďalšie vstupy súborov**

Rôzne typy údajov, najmä part[ geometries]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/' | relative_url }}) a [material data]({{ '/docs/sk/pre_processor/10_material_data/10_material_data/' | relative_url }}), možno čítať z príslušných formátových súborov.

**Modifikácia údajov o probléme**

Údaje o riešení alebo vstupných krokoch z ľubovoľného kroku uloženého v databázovom súbore možno načítať do preprocesora, upraviť ich a buď pripojiť k existujúcej databáze, alebo zapísať do nového databázového súboru.

**Zobrazenie konkrétnych údajov o problémoch**

Väčšina problémových údajov uložených v databázovom súbore je prístupná v [post-processor]({{ '/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/' | relative_url }}). Určité špecifické informácie, ako napríklad stavy[ boundary conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }}) alebo [inter-object contact]({{ '/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/' | relative_url }}), sa však v [pre-processor]({{ '/docs/sk/pre_processor/7_introduction_to_pre-processor/' | relative_url }}) zobrazujú odlišne. Pri ladení problému, ktorý neprebieha správne, je niekedy užitočné použiť zobrazenie údajov pred procesorom na zobrazenie týchto informácií.

**Súvisiace témy:**

[Pre-Processor]({{ '/docs/sk/pre_processor/7_introduction_to_pre-processor/' | relative_url }})

[Keyword Documentation]({{ '/docs/sk/keyword_documentation/deform_keywords_list/' | relative_url }})

[Database Generation]({{ '/docs/sk/pre_processor/21_database_generation/21_database_generation/' | relative_url }})

[Post-processor]({{ '/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/' | relative_url }})
