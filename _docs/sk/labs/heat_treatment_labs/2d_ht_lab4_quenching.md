---
lang: sk
title: "2D HT Lab 4 – Kalenie"
---

# 2D HT Lab4: Modelovanie kalenia zubov ozubeného kolesa

  
4.1. Otvorenie súboru projektu

4.2. Pridávanie operácie

4.3. Nastavenie ovládacích prvkov simulácie

4.4. Nastavenie vlastností objektu

4.5. Vytvorenie databázy

4.6. Spustenie simulácie

4.7. Následné spracovanie výsledkov

## Otvorenie súboru projektu

Hlavné okno grafického rozhrania DEFORM by už malo byť otvorené. Keď je v zozname súborov zvýraznený súbor **Gear_Blank**.**moproj**, kliknite na ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}), ako je znázornené na obrázku [Fig. 2DHTML2.1.]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab2_carburization/' | relative_url }}#Fig_2DHTML2_1_DEFORM_GUI_Main_Window). Otvorí sa okno „Integrated Manufacturing Proc.“.

## Pridávanie operácie

V Průzkumníku pridajte operáciu 2D tvarovanie zo zoznamu operácií. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie **2D****Tvarovanie** alebo ju môžete pridať aj pretiahnutím do oblasti Editor operácií.

V editore operácií vyberte 4. operáciu, zobrazí sa roletové menu „Typ nastavenia“; kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Nastavenie ovládacích prvkov simulácie

Vyberte kartu **Main![]({{ '/assets/icons/pre_icons/mo_main_setting.jpg' | relative_url }})**, zmeňte názov operácie na **Quench**. Vypnite modul **Diffusion** a zapnite modul **Deformation**, ako je znázornené na obr. 2DHTML4.1.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0001.jpg' | relative_url }})

Ovládacie prvky simulácie – karta „Hlavné“ v režime „Expert“

Vyberte kartu **Krok****Prírastok![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})** a v časti Definícia kroku nastavte hodnotu na Konštantná **teplota**. Zadajte počiatočný/minimálny časový krok na 0,01 sekundy na krok a maximálnu zmenu teploty na krok nastavte na 5 °C. Maximálny časový krok pre zmenu teploty nastavte na 20 sekúnd na krok. (Pozri obr. 2DHTML4.2.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0002.jpg' | relative_url }})

Karta „Krok“ v režime Expert

Vyberte kartu **Zastavenie****Controls![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }})** a nastavte **Trvanie procesu****** na **13500** sekúnd, ako je znázornené na obr. 2DHTML4.3.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0003.jpg' | relative_url }})

Karta „Ovládacie prvky zastavenia“ v režime Expert

V časti „Process Conditions“ (Podmienky spracovania) nastavte **teplotu prostredia** na **20** °C a zmeňte **koeficient konvekcie** na **4,093**, ako je znázornené na obr. 2DHTML4.4. Tento koeficient konvekcie je podobný koeficientu konvekcie určitých druhov chladiacich olejov. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Vlastnosti obrobku.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0004.jpg' | relative_url }})

Okno „Podmienky procesu“

## Nastavenie vlastností objektu

V tejto fáze používateľ nastaví typ výpočtu tvrdosti na metódu objemových podielov. Kliknite na kartu Vlastnosti obrobku. Nastavte typ odhadu **Tvrdosti** na **Použitie****objemových****podielov**, ako je znázornené na obr. 2DHTML4.5.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0005.jpg' | relative_url }})

Okno vlastností objektu

## Vytvorenie databázy

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly červené správy označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). Ak sa nezobrazujú žiadne chyby, databázu je možné vygenerovať.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu (pozri obr. 2DHTML4.6.). Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0006.jpg' | relative_url }})

Vytvoriť databázu

## Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia.[]({{ '/docs/sk/labs/tool_life_study_lab/tool_life_study_lab1/' | relative_url }}#Fig_TLSL1_17_Run_Options_Popup) Použite predvolenú možnosť **Pokračovať v spúšťaní**, aby ste vybrali možnosť „**Pokračovať od posledného kroku** a potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) ****sa simulácia spustí.

Ak simulácia prebehne bez problémov, na koniec súboru Message sa pridá nasledujúca správa, ako je znázornené na obr. 2DHTML4.7.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0007.jpg' | relative_url }})

Karta „Simulačné správy“

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky; otvorí sa postprocesor MO.

Používateľa by mohli zaujímať stavové premenné „Fázové objemové podiely“. Prejdite na posledný krok v databáze. Kliknutím na tlačidlo „Stavové premenné ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})“ otvoríte dialógové okno so stavovými premennými. V časti „Mikrostruktúra“ vyberte premennú „Objemové podiely (perlit)“ a znázornite premenné ako tieňované kontúry. Tým získate predpoveď mikrostruktúry zubov ozubeného kolesa ako funkciu polohy. Na konci kalenia je materiál v blízkosti povrchu prevažne martenzit, zatiaľ čo v strede prevláda perlit. Okrem toho môže používateľa zaujímať deformácia spôsobená kalením a zvyškové napätie, ktoré sú spôsobené heterogénnymi objemovými zmenami pri transformácii a tepelnou kontrakciou. Ak chcete preskúmať deformáciu, vyberte premennú „Total Displacement“ (Celkový posun) v časti „Deformation“ (Deformácia) a znázornite premenné ako graf „Deflection“ (Ohyb). Ak chcete zväčšiť deformáciu, môžete potiahnuť lištu „Deflection Scale“ (Mierka deformácie). V prípade zvyškového napätia vyberte „Effective Stress“ (Efektívne napätie) a vyneste premennú ako tieňovaný kontúrový graf. (Pozri obr. 2DHTML4.8. až obr. 2DHTML4.10.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0008.jpg' | relative_url }})

Graf objemového podielu perlitov

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0009.jpg' | relative_url }})

Graf objemového podielu martenzitu

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0010.jpg' | relative_url }})

Objemový podiel austenitu

Ďalšou dôležitou stavovou premennou v tejto simulácii je premenná „Tvrdosť“. Vyberte premennú „Tvrdosť“ v časti „Mikrostruktúra“ a znázornite premenné ako tieňované kontúry. Vidíte, že tvrdosť (v jednotkách Rockwell C) je vysoká tam, kde je vysoký obsah martenzitu, a nízka tam, kde je vysoký obsah perlitov. (Obr. 2DHTML4.11.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0011.jpg' | relative_url }})

Graf tvrdosti

Po dokončení následného spracovania uložte projekt a zatvorte sprievodcu MO kliknutím na tlačidlo „Quit ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }})“ alebo výberom možnosti „Quit“ v ponuke „File“. Ak chce používateľ pokračovať v nastavení, môže priamo prejsť do režimu „pre“ a pokračovať v nastavení pridaním operácie.

Súvisiace témy:

[2D HT Lab1 Heating]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab1_heating/' | relative_url }})

[2D HT Lab2 Carburization]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab2_carburization/' | relative_url }})

[2D HT Lab3 Diffusion]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab_3_diffusion/' | relative_url }})
