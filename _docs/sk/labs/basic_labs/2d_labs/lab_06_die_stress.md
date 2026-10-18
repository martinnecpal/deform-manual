---
lang: sk
title: "Laboratórna práca č. 06: Napätie v matrici"
---

# Laboratórna úloha č. 06: Napätie v matrici

  
6.1. Úvod

6.2. Otvorenie súboru projektu

6.3. Pridať analýzu napätia v lisovacej forme

6.4. Výber kroku

6.5. Nastavenie hornej matrice

6.6. Nastavenie spodnej matrice

6.7. Nastavenie ovládacích prvkov simulácie

6.8. Vytvorenie databázy

6.9. Spustenie simulácie

6.10. Následné spracovanie výsledkov

## Úvod

Cieľom tohto laboratórneho cvičenia je vykonať analýzu napätí v lisovacej forme. Ak sa analýza napätí vykonáva len na jednom nástroji, na získanie presných hodnôt napätí stačí jednokroková simulácia. Ak sa analýza napätí vykonáva na zostavách lisovacích nástrojov, kde dochádza k interakcii medzi nástrojmi, zvyčajne je potrebných viac ako jeden krok, aby sa sústava lisovacích nástrojov dostala do rovnovážneho stavu pri pôsobiacom zaťažení.

Pri typickej simulácii napätia v lisovacích formách sa obrobok odstráni a sily, ktoré obrobok pôsobí na lisovacie formy, sa interpolujú na nástroje. V tomto laboratóriu vykonávame analýzu napätia v lisovacích formách pre projekt Spike_Nonisothermal v 50. kroku.

## Otvorenie súboru projektu

Otvorte predtým simulovaný súbor **Spike_Nonisothermal.moproj** v programe DEFORM MO, ako je znázornené na obr. L6.1. Otvorí sa predspracovateľ programu MO.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania programu DEFORM

## Pridať analýzu napätia v matrici

V ľavom hornom rohu okna zobrazenia kliknite ľavým tlačidlom myši na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu „Add Die stress Study“, ako je znázornené na obr. L6.2. V editore operácií sa pridá karta „Die stress Study“ s operáciou „Die stress“, ako je znázornené na obr. L6.3.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0002.jpg' | relative_url }})

Pridanie operácie s napätím v matrici

## Výber kroku

Ak chcete vykonať výpočet napätia v matrici v jednom kroku, ako typ výpočtu napätia v matrici vyberte „**Jeden krok**“ a na stránke Výber kroku vyberte **krok****50**, ako je znázornené na obr. L6.3. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Horná matrica.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0003.jpg' | relative_url }})

Zoznam výberu krokov

## Nastavenie hornej matrice

### Definícia objektu „Top die“

V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Top Die“ ponechajte typ objektu ako pružný. Od verzie v13.1.1 boli na stránke objektov zavedené dve nové možnosti na umiestnenie matíc v budúcich krokoch pri analýze napätia matíc vo viacerých krokoch; pri analýze napätia matíc v jednom kroku tieto možnosti nepotrebujeme, preto nechajte políčko „Potrebné umiestnenie“ nezaškrtnuté. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka BCC, kde môžete priradiť okrajové podmienky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0011.jpg' | relative_url }})

Hlavná stránka objektu „Top die“

### Nastavenie okrajových podmienok

Na hornú plochu hornej matrice použite okrajovú podmienku rýchlosti **Vy****= 0**. Táto okrajová podmienka zabraňuje odletu matrice pri pôsobení síl, pozri obr. L6.5. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s interpoláciou síl hornej matrice.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0004.jpg' | relative_url }})

Na začiatok stránky BCC

### Vynútená interpolácia

Na stránke „Interpolácia sily“ kliknite na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) a po vykonaní interpolácie sily sa v zozname správ zobrazí správa o interpolácii sily, pozri obr. L6.6. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre spodnú matricu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0005.jpg' | relative_url }})

Okno interpolácie sily hornej matrice

##  Nastavenie spodnej matrice

### Definícia objektu „Spodná matrica“

Pre spodnú formu ponecháme typ objektu „Elastic“ a zrušíme zaškrtnutie políčka „Potrebné polohovanie“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka BCC, kde priradíte okrajové podmienky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0012.jpg' | relative_url }})

Stránka objektu spodnej matrice

### Nastavenie okrajovej podmienky pre spodnú formu

Na spodnú plochu spodnej matrice nastavte okrajovú podmienku rýchlosti **Vy** = 0. Táto okrajová podmienka zabraňuje odletu matrice pri pôsobení síl, pozri obr. L6.8. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Interpolácia síl spodnej matrice“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0006.jpg' | relative_url }})

Spodná časť stránky BCC

### Vynútená interpolácia

Kliknite na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) a po vykonaní interpolácie síl sa v zozname správ zobrazí správa o interpolácii síl, pozri obr. L6.9. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete k ovládacím prvkom simulácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0007.jpg' | relative_url }})

Vynútiť okno interpolácie

## Nastavenie ovládacích prvkov simulácie

V tejto operácii použijeme predvolené údaje ovládacích prvkov simulácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete stránku databázy.

## Vytvoriť databázu

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spúšťaní** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak simulácia prebehne bez problémov, na koniec súboru so správami sa pridá nasledujúca správa: „Simulácia bola dokončená a zastavená v časovom kroku určenom používateľom“.

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite do režimu zobrazenia výsledkov kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). (Pozri obr. L6.10.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0008.jpg' | relative_url }})

Okno príspevku MO

#### Stavová premenná

Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}), vykreslite **efektívne napätie** a **maximálne hlavné napätie** a sledujte graf tak, ako je znázornené na obr. L6.11 a obr. L6.12. Tieto dve veličiny sú najdôležitejšími premennými pri simulácii napätia v lisovacej forme.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0009.jpg' | relative_url }})

Graf pôsobenia napätia v zobrazení s plným tieňovaním

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0010.jpg' | relative_url }})

Graf maximálneho hlavného napätia v líniovom zobrazení

Ak chcete pokračovať v testoch Die Stress Labs s držiakom a v testoch s držiakom a zúženým uložením, nezatvárajte projekt MO. Pozrite si príslušné dokumenty [Lab 12 Die Stress with Holder]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/' | relative_url }}) a [13 Die Stress with Shrink Fit]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/' | relative_url }}).

**Súvisiace témy:**

[11\. General Object Data Definition]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }})

[14\. Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[6.2. Integrated Manufacturing Process Simulation layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})

[2D Die Stress Study with Single step]({{ '/docs/sk/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/' | relative_url }})

[2D Die Stress Study with Multiple Steps]({{ '/docs/sk/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/' | relative_url }})

[49.1. 2D Die Stress Study]({{ '/docs/sk/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/' | relative_url }})

[49.2. 3D Die Stress Study]({{ '/docs/sk/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/' | relative_url }})
