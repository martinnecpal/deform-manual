---
lang: sk
title: "Laboratórium 07 – Mechanický lis"
---

# Laboratórna práca č. 07 Mechanický lis

Požiadavka: Na nastavenie tejto operácie musíme najprv nastaviť [Lab 03 Spike Isothermal Lab]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_03_spike_isothermal/' | relative_url }}).

7.1. Vytvorenie nového problému

7.2. Pridanie operácie

7.3. Import databázy

7.4. Nastavenie pohybu hornej matrice

7.5. Vytvorenie databázy

7.6. Spustenie simulácie

7.7. Následné spracovanie výsledkov

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte tlačidlo „**Integrated Manufacturing Process**“ a v poli jednotiek zvoľte tlačidlo „**English**“. Názov úlohy zadajte ako „******Spike_Mechanical**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“ (pozri obr. L7.1.). V tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tomto cvičení použijeme ako názov projektu „**Spike_Mechanical**“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_07_mechanical_press/2d_mobl7_image0001.jpg' | relative_url }})

Priradenie názvu úlohy

Používateľ môže tiež zmeniť systém jednotiek, umiestnenie súboru na uloženie projektu a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. L7.1.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na tlačidlo pokračujte v otváraní operácie.

## Pridanie operácie

Otvorí sa sprievodca viacerými operáciami. Zo zoznamu operácií v Průzkumníku pridajte operáciu 2D tvarovania. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) pre operáciu 2D tvarovania alebo ju môžete pridať aj pretiahnutím do Editoru operácií. (Pozri obr. L7.2.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_07_mechanical_press/2d_mobl7_image0002.jpg' | relative_url }})

Pridať operáciu 2D tvárnenia do editora operácií

## Importovať databázu

Pomocou možnosti importu ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) načítajte databázu úlohy **Spike_Isothermal**, v okne výberu krokov (pozri obr. L7.3.) vyberte krok -1 a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_07_mechanical_press/2d_mobl7_image0003.jpg' | relative_url }})

Výber kroku v okne „Výber kroku“

V tomto laboratórnom cvičení nastavíme mechanický pohyb pre hornú matricu; kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s nastavením pohybu hornej matrice.

## Nastavenie pohybu hornej matrice

Vyberte typ mechanického pohybu, nastavte **Celkový zdvih** na hodnotu **22,5** palcov, **Zdvih kovania** na hodnotu **12** palcov a **Cyklus/s** na hodnotu **1** (pozri obr. L7.4.). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Generovať databázu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_07_mechanical_press/2d_mobl7_image0004.jpg' | relative_url }})

Hlavná stránka – Pohyb matrice

## Vytvoriť databázu

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). 

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

## Spustenie simulácie

Kliknite na ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. L7.5.). Po kliknutí na možnosť „Spustiť“ sa otvorí dialógové okno „Spustiť simuláciu“ (pozri obr. L7.6.). Použite predvolenú možnosť **Pokračovať v spúšťaní** na výber možnosti „**Pokračovať od posledného kroku**“ a potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_07_mechanical_press/2d_mobl7_image0007.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať v režime Simulácia v častiach „Simulačné správy“ a „Simulačná grafika“. Kliknutím na kartu „Simulačné správy“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) (čo je predvolené nastavenie), súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a tiež informácie o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru so správami pridá nasledujúca správa: „NORMAL STOP: Simulácia bola dokončená a zastavená v časovom kroku určenom používateľom“.

## Následné spracovanie výsledkov

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) – otvorí sa postprocesor MO.

### Graf závislosti zaťaženia od zdvihu:

Vytvorte graf rýchlosti na osi Y v závislosti od zdvihu pre hornú maticu.

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) – otvorí sa okno „Load Stroke Graph“ (Načítať graf zdvihu). V zozname objektov „Plot“ vyberte položku „Top Die“ (Horná matrica), v roletovom menu osi X vyberte položku **Stroke** (Zdvih) a v roletovom menu osi Y vyberte položku **Y Speed** (Rýchlosť na osi Y). Kliknite na kartu „Options“ a zaškrtnite políčko „Step tracer“, potom kliknite na ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}). Graf zaťaženia a zdvihu sa zobrazí na pravej strane okna (pozri obr. L7.7.). Pri výbere iného kroku sa v krivke zaťaženia a zdvihu zvýrazní príslušný krok a v grafe sa zobrazí zodpovedajúce zaťaženie pre tento krok. Okrem toho je možné myšou vybrať bod na grafe a zobrazený krok sa automaticky zmení na ten, ktorý zodpovedá danému bodu na grafe.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_07_mechanical_press/2d_mobl7_image0005.jpg' | relative_url }})

Graf priebehu rýchlosti Y-Speed

Podobne nakreslite graf **zaťaženia Y** v závislosti od **zdvihu** pre hornú maticu a graf si prezrite. (Pozri obr. L7.8.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_07_mechanical_press/2d_mobl7_image0006.jpg' | relative_url }})

Graf zdvihu s zaťažením Y

Po dokončení následného spracovania uložte projekt a zatvorte sprievodcu MO kliknutím na tlačidlo „Close ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }})“ alebo výberom možnosti „Quit“ v ponuke „File“.

**Súvisiace témy:**

[Movement Controls]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[Simulation]({{ '/docs/sk/simulator/simulator_mainpg/' | relative_url }})

[Post processor]({{ '/docs/sk/post_processor/post_processor_mainpg/' | relative_url }})
