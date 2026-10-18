---
lang: sk
title: "2D HT Laboratórium 3: Difúzia"
---

# 2D HT Lab 3 Modelovanie difúzie zuba ozubeného kolesa

  
3.1. Otvorenie súboru projektu

3.2. Pridanie operácie

3.3. Nastavenie ovládacích prvkov simulácie

3.4. Vytvorenie databázy

3.5. Spustenie simulácie

3.6. Následné spracovanie výsledkov

## Otvorenie súboru projektu

Hlavné okno grafického rozhrania DEFORM by už malo byť otvorené. Keď je v zozname súborov zvýraznený súbor **Gear_Blank**.**moproj**, kliknite na ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}), ako je znázornené na obrázku. Otvorí sa okno „[Fig. 2DHTML2.1.]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab2_carburization/' | relative_url }}#Fig_2DHTML2_1_DEFORM_GUI_Main_Window) Integrated Manufacturing Proc.“.

## Pridanie operácie

V Průzkumníku pridajte operáciu 2D tvarovanie zo zoznamu operácií. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie **2D****Tvarovanie** alebo ju môžete pridať aj pretiahnutím do oblasti Editor operácií.

V editore operácií vyberte 3. operáciu; zobrazí sa rozbaľovacie okno „Typ nastavenia“; kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}). V editore operácií vyberte 3. operáciu, dvakrát na ňu kliknite myšou, zmeňte jej názov na „**Diffusion**“ a stlačte klávesu Enter na klávesnici. (Pozri obr. 2DHTML3.1.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0001.jpg' | relative_url }})

Zmena názvu operácie v editore operácií

## Nastavenie ovládacích prvkov simulácie

Vyberte kartu **Step****Increment![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})** a nastavte konštantu **Time****Increment** na hodnotu **60** sekúnd, ako je znázornené na obr. 2DHTML3.2.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0002.jpg' | relative_url }})

Karta „Krok“ v expertnom režime

Vyberte kartu **Zastavenie****Controls![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }})** a nastavte **Trvanie procesu****** na **13200** sekúnd, ako je znázornené na obr. 2DHTML3.3.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0003.jpg' | relative_url }})

Karta „Ovládacie prvky zastavenia“ v režime Expert

Kliknite na kartu **Process****Conditions![]({{ '/assets/icons/pre_icons/mo_process_conditions.jpg' | relative_url }}) **v okne Simulations Controls. Vyberte kartu **Diffusion**, nastavte hodnotu koeficientu reakčnej rýchlosti na **0** mm/s a obsah atómov v prostredí by sa mal zmeniť na **0** % atómov, ako je znázornené na obr. 2DHTML3.4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka Generate DB.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0004.jpg' | relative_url }})

Karta „Podmienky procesu“ v expertnom režime

## Vytvorenie databázy

Na stránke **Generate****DB** kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly červené správy označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). Ak sa nezobrazujú žiadne chyby, databázu je možné vygenerovať.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu (pozri obr. 2DHTML3.5.). Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0005.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia.[]({{ '/docs/sk/labs/tool_life_study_lab/tool_life_study_lab1/' | relative_url }}#Fig_TLSL1_17_Run_Options_Popup) Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku** a potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) ****sa simulácia spustí.

Ak simulácia prebehne bez problémov, na koniec súboru Message sa pridá nasledujúca správa, ako je znázornené na obr. 2DHTML3.6.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0006.jpg' | relative_url }})

Karta „Simulačné správy“

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky; otvorí sa postprocesor MO.

Kľúčovou stavovou premennou v tejto simulácii je „Dominant Atom“. Prejdite na posledný krok v databáze. Kliknutím na tlačidlo „State Variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})“ otvoríte dialógové okno stavových premenných. V časti „Diffusion“ vyberte premennú „Dominant Atom“ a znázornite ju ako tieňovanú kontúru. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (pozri obr. 2DHTML3.7.). Používateľ by mal vidieť premennú v podobnom stave ako na konci operácie karburizácie. V tejto simulácii zostáva celkové množstvo uhlíka konštantné, ale difunduje po celom zube ozubeného kolesa.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0007.jpg' | relative_url }})

Graf atómov s prevládajúcou difúziou

Po dokončení následného spracovania uložte projekt a zatvorte sprievodcu MO kliknutím na tlačidlo „Quit ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }})“ alebo výberom možnosti „Quit“ v ponuke „File“. Ak chce používateľ pokračovať v nastavení, môže priamo prejsť do režimu „pre“ a pokračovať v nastavení pridaním operácie.

Súvisiace témy:

[2D HT Lab1 Heating]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab1_heating/' | relative_url }})

[2D HT Lab2 Carburization]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab2_carburization/' | relative_url }})

[2D HT Lab4 Quenching ]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab4_quenching/' | relative_url }})
