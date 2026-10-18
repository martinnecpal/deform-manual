---
lang: sk
title: "2D HT Lab 2 – Karburácia"
---

# 2D HT Lab2. Modelovanie karburácie zubov ozubeného kolesa

  
2.1. Otvorenie súboru projektu

2.2. Operácia sčítania

2.3. Nastavenie ovládacích prvkov simulácie

2.4. Nastavenie okrajových podmienok

2.5. Vytvorenie databázy

2.6. Spustenie simulácie

2.7. Následné spracovanie výsledkov

## Otvorenie súboru projektu

Hlavné okno grafického rozhrania DEFORM by už malo byť otvorené. Keď je v zozname súborov zvýraznený súbor **Gear_Blank**.**moproj**, kliknite na ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}), ako je znázornené na obr. 2DHTML2.1. Otvorí sa okno „Integrated Manufacturing Proc.“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania DEFORM

## Pridávanie operácie

Pridajte operáciu 2D tvarovanie zo zoznamu operácií v Průzkumníku. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie **2D****Tvarovanie** (pozri obr. 2DHTML2.2.) alebo ju môžete pridať aj pretiahnutím do oblasti Editoru operácií.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0002.jpg' | relative_url }})

Pridanie operácie 2D tvárnenia do editora operácií

V editore operácií vyberte 2. operáciu; zobrazí sa rozbaľovacie okno „Typ nastavenia“, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}). (Pozri obr. 2DHTML2.3.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0003.jpg' | relative_url }})

Vyskakovacie okno s typom nastavenia

## Nastavenie ovládacích prvkov simulácie

Vyberte kartu **Main![]({{ '/assets/icons/pre_icons/mo_main_setting.jpg' | relative_url }})** a zmeňte **Názov operácie** na **Karburácia**. Zapnite **modul difúzie** a **vypnite** modul **deformácie**. (Pozri obr. 2DHTML2.4.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0004.jpg' | relative_url }})

Karta „Simulačné ovládacie prvky“ v režime pre pokročilých

Vyberte kartu **Krok****Prírastok**![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) a nastavte **Konštanta****Čas****Prírastok** na **10** sekúnd (pozri obr. 2DHTML2.5.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0005.jpg' | relative_url }})

Ovládacie prvky simulácie – karta „Krok“ v expertnom režime

Vyberte kartu **Zastavenie****Ovládacie prvky**![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) a nastavte **Trvanie procesu****** na **6000** sekúnd. (Pozri obr. 2DHTML2.6.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0006.jpg' | relative_url }})

Karta „Ovládanie zastavenia“ v režime Expert

V časti **Proces****Podmienky** /**Difúzia** nastavte hodnotu **koeficientu** rýchlosti **reakcie** na **0,0001** mm/s a hodnotu **obsahu atómov** v prostredí**obsah** by mal byť nastavený na hodnotu **1,69**, ako je znázornené na obr. 2DHTML2.7. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Workpiece Boundary conditions“ (Hranicové podmienky obrobku).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0007.jpg' | relative_url }})

Karta „Podmienky procesu“ v režime Expert

## Nastavenie okrajových podmienok

V tejto fáze musí používateľ určiť hranicu, za ktorou je obrobok vystavený atmosfére obsahujúcej uhlík. V tomto prípade bude celá plocha – tak vonkajšia plocha, ako aj plocha vnútorného otvoru – vystavená prostrediu obsahujúcemu uhlík.

Kliknite na položku „Difúzia s prostredím“. Vyberte a priraďte okrajové podmienky pre vnútorný priemer ozubeného kolesa aj pre jeho vonkajšiu plochu, ako je znázornené na obr. 2DHTML2.8. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Generate DB“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0008.jpg' | relative_url }})

Prerez zubom ozubeného kolesa s difúziou a okrajovými podmienkami prostredia

## Vytvorenie databázy

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly červené správy označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). Ak sa nezobrazujú žiadne chyby, databázu je možné vygenerovať.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu (pozri obr. 2DHTML2.9.). Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0009.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Spustenie simulácie

Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia.[]({{ '/docs/sk/labs/tool_life_study_lab/tool_life_study_lab1/' | relative_url }}#Fig_TLSL1_17_Run_Options_Popup) Použite predvolenú možnosť **Pokračovať v spúšťaní**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“ a potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

Ak simulácia prebehne bez problémov, na koniec súboru Message sa pridá nasledujúca správa, ako je znázornené na obr. 2DHTML2.10.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0010.jpg' | relative_url }})

Karta „Simulačné správy“

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky; otvorí sa postprocesor MO.

Kľúčovou stavovou premennou v tejto simulácii je „Dominant Atom“. Prejdite na posledný krok v databáze. Kliknutím na tlačidlo „State Variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})“ otvoríte dialógové okno stavových premenných. V časti „Diffusion“ vyberte premennú „Dominant Atom“ a zobrazenie tejto premennej ako tieňovanú kontúru. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (pozri obr. 2DHTML2.11.). Užívateľ by mal vidieť, že premenná má počiatočnú rovnomernú hodnotu 0,14. Hodnota sa zvyšuje na voľných hraniciach, čo naznačuje, že uhlík sa absorbuje a difunduje do zuba ozubeného kolesa.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0011.jpg' | relative_url }})

Graf atómov s prevládajúcou difúziou

Po dokončení následného spracovania uložte projekt a zatvorte sprievodcu MO kliknutím na tlačidlo „Quit ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }})“ alebo výberom možnosti „Quit“ v ponuke „File“. Ak chce používateľ pokračovať v nastavení, môže prejsť priamo do režimu „pre“ a pokračovať v nastavení pridaním operácie.

Súvisiace témy:

[2D HT Lab1 Heating]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab1_heating/' | relative_url }})

[2D HT Lab3 Diffusion]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab_3_diffusion/' | relative_url }})

[2D HT Lab4 Quenching ]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab4_quenching/' | relative_url }})
