---
lang: sk
title: "Laboratórna práca č. 11: Šnekový lis"
---

# Laboratórna práca č. 11: Šnekový lis

Požiadavka: Na nastavenie tejto operácie musíme najskôr nastaviť [Lab 03 Spike Isothermal Lab.]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_03_spike_isothermal/' | relative_url }})

11.1. Vytvorenie novej úlohy

11.2. Pridanie operácie

11.3. Import databázy

11.4. Zoznam materiálov

11.5. Stanovenie teploty sochoru

11.6. Nastavenie pohybu šnekového lisu pre hornú matricu

11.7. Vytvorenie databázy

11.8. Spustenie simulácie

11.9. Následné spracovanie výsledkov

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek zvoľte prepínač „**Anglický**“. Názov úlohy zadajte ako „******Spike_Screwpress**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“ (pozri obr. L11.1.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tomto cvičení použijeme ako názov projektu „**Spike_Screwpress**“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0001.jpg' | relative_url }})

Priradenie názvu projektu

Používateľ môže tiež zmeniť systém jednotiek, umiestnenie súboru na uloženie projektu a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. L11.1.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

## Pridanie operácie

Otvorí sa sprievodca viacerými operáciami. Zo zoznamu operácií v Průzkumníku pridajte operáciu 2D tvárnenie. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) pre operáciu 2D tvárnenie alebo ju môžete pridať aj pretiahnutím do editora operácií.

## Importovanie databázy

Pomocou možnosti Importu ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) načítajte databázu úlohy **Spike_Isothermal**, v okne Výber kroku vyberte krok **-1** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Materiál.

## Zoznam materiálov

V zozname materiálov odstráňte materiál AISI-1035, COLD [70–400 °F (20–200 °C)] tak, že ho označíte a kliknete na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) (pozri obr. L11.2.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0003.jpg' | relative_url }})

Odstránenie materiálu zo zoznamu materiálov

Načítajte materiál **AISI-1045_(20-1100C)** z knižnice materiálov DEFORM v kategórii **Oceľ** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). Následne klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Billet“.

## Nastavenie teploty sochory

Nastavte **teplotu objektu** na hodnotu **2250** °F (pozri obr. L11.3.) a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die movement“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0002.jpg' | relative_url }})

Stránka objektu „Billet“

## Nastavenie pohybu skrutkového lisu pre hornú matricu

Na stránke „Pohyb hornej matrice“ vyberte typ **Pohyb skrutkového lisu**, nastavte **Energiu** na **75 Klb-in**, **Účinnosť zdvihu** na **0,8**, **zotrvačnosť** na **0,25 Klb-in-s²** a **rozstup vodiacich skrutiek** na **5** **in/rev** (pozri obr. L11.4.). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Generate DB.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0003.jpg' | relative_url }})

Na začiatok stránky o pohybe matrice

## Vytvorenie databázy

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu, aby ste spustili simuláciu.

## Spustenie simulácie

Kliknite na ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“. Po kliknutí na možnosť „Spustiť“ sa otvorí dialógové okno „Spustiť simuláciu“. Použite predvolenú možnosť **Pokračovať v spúšťaní**, aby ste vybrali možnosť „**Pokračovať od posledného kroku** a potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

Priebeh simulácie je možné počas jej vykonávania sledovať v režime Simulácia v častiach „Simulačné správy“ a „Simulačná grafika“. Kliknutím na kartu „Simulačné správy“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) (čo je predvolené nastavenie), súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a tiež poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru „Message“ pridá nasledujúca správa:

"PROGRAM SA ZASTAVIL!

***** „ENERGIA PRE TLAČ BOLA ÚPLNE VYČERPANÁ.“.

## Následné spracovanie výsledkov

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) – otvorí sa postprocesor MO.

Vytvorte grafy **zaťaženie – zdvih** a **rýchlosť – zdvih** a sledujte ich, ako je znázornené na obr. L11.5 a obr. L11.6:

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0004.jpg' | relative_url }})

Graf závislosti zaťaženia Y od zdvihu

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0005.jpg' | relative_url }})

Rýchlosť Y – graf zdvihu

**Súvisiace témy:**

[15\. Movement Controls Settings]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[6.2. Integrated Manufacturing Process Simulation layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
