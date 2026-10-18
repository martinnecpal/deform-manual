---
lang: sk
title: "Štúdia 3D napätia v čipe v rámci jedného kroku – Lab1"
---

# Laboratórium pre štúdium napätia v 3D formách 1

1.1. Úvod

1.2. Otvorenie súboru projektu

1.3. Pridať analýzu napätí v lisovacej forme

1.4. Pridávanie objektov

1.5. Horná matrica

1.6. Spodná forma

1.7. Ovládacie prvky simulácie

1.8. Vytvorenie databázy

1.9. Následné spracovanie

## Úvod

Cieľom tohto laboratórneho cvičenia je vykonať analýzu napätí v lisovacej forme. Ak sa analýza napätia vykonáva len na jednom nástroji, na získanie presných hodnôt napätia postačuje jednokroková simulácia. Ak sa analýza napätia vykonáva na zostavách lisovacích foriem, kde dochádza k interakcii medzi nástrojmi, zvyčajne je potrebných viac ako jeden krok, aby sa sústava foriem dostala do rovnovážneho stavu pri pôsobiacom zaťažení.

Pri typickej simulácii namáhania foriem sa obrobok odstráni a sily, ktoré obrobok pôsobí na formy, sa interpolujú na nástroje. 

## Otvorenie súboru projektu

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrated Manufacturing Process**“ a systém jednotiek pomocou prepínača „**English**“, aby ste úlohu nastavili v anglickom systéme jednotiek. Názov úlohy zadajte ako „**Die_stress_Lab1**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0001.jpg' | relative_url }})

Problém s definovaním okna

Otvorí sa sprievodca MO spolu s oknom na zadanie názvu projektu, ako je znázornené na obr. 3DDSL1.1., Do poľa s názvom projektu zadajte názov projektu **Die_stress_Lab1** a vyberte voľbu **kopírovať existujúci projekt**, pretože budeme kopírovať existujúci projekt zo zložky Labs, ktorý bude slúžiť ako základné nastavenie. Kliknite na tlačidlo prehľadávania zdrojovej lokality a importujte súbor **Spike_Forging.moproj** z inštalačnej cesty \SFTC\DEFORM\v*_*\3d\LABS, zaškrtnite políčko **C******o** py Database**, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a zatvorte okno Nový projekt. Simulácia Spike_forging sa načíta do projektu **Die_stress_Lab1**. (pozri obr. 3DDSL1.2.). Po načítaní operácie kovania hrotov vygenerujte databázu v operácii prenosu tepla pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}). Po vygenerovaní databázy prejdite do režimu (Simulácia) ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a simuláciu spustite pomocou možnosti ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}). Po dokončení simulácie prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0002.jpg' | relative_url }})

Projekt bol importovaný

Na konci prvej operácie tvárnenia vykonáme analýzu napätia v lisovacej forme.

## Pridať štúdiu o namáhaní matice

V ľavom hornom rohu okna displeja kliknite ľavým tlačidlom myši na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu **Pridať analýzu napätia v čipe**, ako je znázornené na obr. 3DDSL1.3.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0003.jpg' | relative_url }})

Pridanie štúdie o Diestress

Ak chcete vykonať analýzu napätia v lisovacej forme na konci prvej operácie tvárnenia, vyberte možnosť „**Krok zaťaženia z databázy**“ a následne na stránke výberu krokov vyberte posledný krok tretej operácie (**krok** **90**), ako je znázornené na obr. 3DDSL1.4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0004.jpg' | relative_url }})

Stránka výberu krokov

## Pridávanie objektov

Na toto laboratórne cvičenie nepotrebujeme žiadne ďalšie objekty. Nechajte teda predvolené nastavenia „Top die“ a „Bottom die“, ako je znázornené na obr. 3DDSL1.5., a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Zvoľte typ objektu „Elastic“, vygenerujte sieť s predvoleným počtom prvkov a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka „Top die object“. 

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0005.jpg' | relative_url }})

Stránka „Objekty“

## Horná matrica

### Definícia objektu „Top Die“

V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Top Die“ ponechajte typ objektu nastavený na „pružný“. Od verzie v13.1.1 boli na stránke objektu zavedené dve nové možnosti na umiestnenie foriem v budúcich krokoch pri analýze napätia foriem vo viacerých krokoch. Pri analýze napätia foriem v jednom kroku tieto možnosti nie je potrebné používať, preto ponechajte políčko „Potrebné umiestnenie“ nezaškrtnuté.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0013.jpg' | relative_url }})

Na začiatok stránky objektu Die

### Priradiť materiál

V okne materiálu vyberte materiál **AISI-H-13** zdedený z nominálnej simulácie, ako je znázornené na obr. 3DDSL1.7, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0006.jpg' | relative_url }})

Okno „Materiál“

### Priradenie okrajových podmienok

  1. Vyberte **okrajovú podmienku roviny symetrie** a potom pridajte okrajovú podmienku ku každej rovine symetrie hornej matrice, ako je znázornené na obr. 3DDSL1.8.

  2. Na hornú plochu hornej matrice uplatnite **hraničnú podmienku rýchlosti** **Vz = 0**. Táto hraničná podmienka zabraňuje odleteniu matrice pri pôsobení síl. (Pozri obr. 3DDSL1.9.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0007.jpg' | relative_url }})

Nastavenie okrajových podmienok symetrie

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0008.jpg' | relative_url }})

Priradenie rýchlosti BCC

### Interpolácia síl pre hornú matricu

Na stránke „Interpolácia sily“ kliknite na názov akcie „![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }})“ a po vykonaní interpolácie sa v editore vlastností zobrazia správy o interpolovanej sile, ako je znázornené na obr. 3DDSL1.10. Kliknite na „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0009.jpg' | relative_url }})

Okno interpolácie sily lisovacej matrice

## Spodná matrica

### Definícia objektu „Spodná matrica“

Pre spodnú formu ponecháme typ objektu „Elastic“ a zrušíme zaškrtnutie políčka „Need positioning“. Vygenerujte sieť s predvoleným počtom prvkov a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s materiálom spodnej formy.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0014.jpg' | relative_url }})

Stránka objektu „Spodná matrica“

### Priradiť materiál

V okne „Materiál“ vyberte materiál **AISI-H-13**, ako je znázornené na obr. 3DDSL1.12, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0006.jpg' | relative_url }})

Okno „Materiál“

### Priradenie okrajových podmienok

  1. Vyberte okrajovú podmienku „Rovina symetrie“ a následne pridajte okrajovú podmienku ku každej z rovín symetrie, ako je znázornené na obr. 3DDSL1.13.

  2. Na spodnú plochu spodnej matrice nastavte okrajovú podmienku rýchlosti Vz = 0. Táto okrajová podmienka zabraňuje odletu matrice pri pôsobení síl. (Pozri obr. 3DDSL1.14.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0011.jpg' | relative_url }})

Definícia symetrie BCC

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0012.jpg' | relative_url }})

Určenie rýchlosti BCC

### Interpolácia síl pre spodnú matricu

Na stránke „Interpolácia sily“ kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) a po vykonaní interpolácie sa v editore vlastností zobrazia správy o interpolovanej sile, ako je znázornené na obr. 3DDSL1.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0013.jpg' | relative_url }})

Vynútiť okno interpolácie

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku ovládacích prvkov. V tomto prípade nie je potrebné vykonávať polohovanie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku „Kontakt medzi objektmi“. V tomto prípade nie je potrebné definovať žiadne vzťahy typu „Kontakt medzi objektmi“, keďže sa žiadne objekty nedotýkajú.

## Ovládacie prvky simulácie

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdeme na stránku Ovládacie prvky simulácie. Nastavte **počet krokov simulácie** na hodnotu **1**, **krok prírastku na uloženie** na hodnotu **1** a **Max. uplynutý čas procesu na krok** na hodnotu **1**. Nechajte nastavený riešiteľ **Conjugate - Gradient** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku generovania databázy.

## Vytvoriť databázu

V ponuke **Súbor** vyberte možnosť **Exportovať** a uložte súbor s kľúčovými slovami pre danú úlohu pod názvom „**Diestress**“.

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať v spúšťaní**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom nastavte režim simulácie na **Interaktívny.** Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustíte simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa simulácia spustí.

Po dokončení simulácie prejdite do režimu Post stlačením tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

## Následné spracovanie

Pomocou ponuky **Premenná stavu** ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) znázornite **efektívne napätie** a **maximálne hlavné napätie**, ako je znázornené na obr. 3DDSL1.16 a obr. 3DDSL1.17.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0014.jpg' | relative_url }})

Graf závislosti od napätia

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0015.jpg' | relative_url }})

Maximálne hlavné napätie

**Súvisiace témy:**

[2D Die Stress Analysis - Theory]({{ '/docs/sk/operation_templates/30_die_stress/2d_die_stress_analysis_theory/' | relative_url }})

[3D Die Stress Analysis]({{ '/docs/sk/operation_templates/30_die_stress/30_introduction_to_die_stress/' | relative_url }})

[Coupled Die Stress analysis]({{ '/docs/sk/operation_templates/30_die_stress/coupled_die_stress_analysis/' | relative_url }})

[Lab 06 Die Stress]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_06_die_stress/' | relative_url }})

[Lab 12 Die Stress with Holder]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/' | relative_url }})

[Lab 13 Die Stress with Shrink Fit]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/' | relative_url }})

[Die Stress study]({{ '/docs/sk/operation_templates/49_die_stress_study/49_introduction_to_die_stress_study/' | relative_url }})

[49.1. 2D Die Stress Study]({{ '/docs/sk/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/' | relative_url }})

[49.2. 3D Die Stress Study]({{ '/docs/sk/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/' | relative_url }})
