---
lang: sk
title: "1.10. Základný súborový systém"
---

# 1.10. Základný súborový systém

Primárnou štruktúrou na ukladanie údajov je databázový súbor. V databázovom súbore je uložený kompletný súbor simulačných údajov vrátane údajov o objektoch, ovládacích prvkov simulácie, údajov o materiáloch a medziobjektových vzťahov, a to z pôvodného vstupu aj z vybraných krokov riešenia. Postupnosť ukladania informácií v databázovom súbore je znázornená na obr. 1.10.1. Preprocesor používa na vytvorenie vstupov súbor vo formáte ASCII nazývaný súbor s kľúčovými slovami.

![]({{ '/assets/images/about_deform/1_10_basic_file_system/1_10_image001.jpg' | relative_url }})

DEFORM Štruktúra databázy

Každý problém DEFORM má pridelené ID problému a mal by byť vytvorený vo vlastnom priečinku alebo adresári. Pre každý problém systém DEFORM vytvára štyri typy súborov, ktoré sú všeobecne prístupné používateľom:

**Súbory databázy (DB)**

Databázový súbor obsahuje kompletný súbor simulačných údajov pre vstupné údaje a každý uložený krok simulácie. Informácie sú uložené v komprimovanom, strojovo čitateľnom formáte a sú prístupné len prostredníctvom DEFORM [pre-procesor](/docs/sk/pre_processor/7_introduction_to_pre-processor/) a [post-processor](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/). Počas simulácie sa údaje pre každý krok zapisujú na koniec databázového súboru. Ak je zapisovaný krok špecifikovaný ako krok, ktorý sa má uložiť, informácie pre ďalší krok sa pridajú za aktuálny krok s údajmi. Ak krok nie je špecifikovaný na uloženie a nájde sa riešenie pre nasledujúci krok, údaje pre aktuálny krok sa prepíšu údajmi pre nasledujúci krok.

**Súbory s kľúčovými slovami (KEY)**

Súbory s kľúčovými slovami obsahujú špecifické údaje o definícii problému, ktoré sa načítajú v predprocesore a použijú sa na vytvorenie vstupného databázového súboru. Súbor kľúčových slov môže obsahovať úplnú definíciu problému alebo môže obsahovať len špecifické informácie, napríklad o konkrétnom objekte alebo materiáli. Informácie sú uložené vo formáte ASCII a možno ich čítať a upravovať pomocou ľubovoľného textového editora, napríklad Notepad, VI alebo Emacs. K dispozícii je odkaz na kľúčové slová, ktorý opisuje formát údajov pre každé kľúčové slovo.

**Súvisiace témy:**

[Creating Input data](/docs/sk/about_deform/1_introduction_to_deform/1_8_creating_input_data/)

[File structure](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_5_files_structure/)

[Database Generation](/docs/sk/pre_processor/21_database_generation/21_database_generation/)

[Keyword Documentation](/docs/sk/keyword_documentation/deform_keywords_list/)
