---
lang: sk
title: "Laboratórium 08 – Kladivový lis"
---

# Laboratórna úloha č. 08: Kladivový lis

Požiadavka: Na nastavenie tejto operácie musíme najskôr nastaviť [Lab 03 Spike Isothermal Lab.]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_03_spike_isothermal/' | relative_url }})

8.1. Vytvorenie nového problému

8.2. Pridanie operácie

8.3. Import databázy

8.4. Zoznam materiálov

8.5. Stanovenie teploty sochory

8.6. Nastavenie pohybu kladiva pre hornú matricu

8.7. Vytvorenie databázy prvých operácií

8.8. Simulácia prvej operácie

8.9. Následné spracovanie výsledkov prvej operácie

8.10. Pridanie druhej operácie

8.11. Pridávanie objektov

8.12. Nastavenie pohybu hornej matrice

8.13. Vytvorenie kontaktov medzi objektmi

8.14. Ovládacie prvky krokov

8.15. Vytvorenie databázy druhej operácie

8.16. Simulácia druhej operácie

8.17. Následné spracovanie výsledkov druhej operácie

8.18. Ukončenie sprievodcu MO

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „******Spike_Hammer**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa vám dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. L8.1.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tomto cvičení použijeme ako názov projektu „**Spike_Hammer**“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0001.jpg' | relative_url }})

Priradenie názvu projektu

Používateľ môže tiež zmeniť systém jednotiek, umiestnenie súboru na uloženie projektu a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. L8.1.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predchádzajúce uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

## Pridanie operácie

Otvorí sa sprievodca viacerými operáciami. Zo zoznamu operácií v prehliadači pridajte operáciu 2D tvárnenia. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) pre operáciu 2D tvárnenia alebo ju môžete pridať aj pretiahnutím do editora operácií.

## Importovanie databázy

Pomocou možnosti importu ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) načítajte databázu úlohy **Spike_Isothermal**, v okne výberu krokov vyberte krok **-1** (pozri obr. L8.2.) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0002.jpg' | relative_url }})

Výber kroku v okne „Výber kroku“

## Zoznam materiálov

V zozname materiálov odstráňte materiál AISI-1035, COLD [70–400 °F (20–200 °C)] tak, že ho označíte a kliknete na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) (pozri obr. L8.3.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0003.jpg' | relative_url }})

Odstránenie materiálu zo zoznamu materiálov

Načítajte materiál **AISI-1045_(20-1100C)** z knižnice materiálov DEFORM v kategórii **Oceľ** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Sochor“.

## Nastavenie teploty sochory

Nastavte **teplotu objektu** na hodnotu **2250** °F (pozri obr. L8.4.) a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die movement“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0004.jpg' | relative_url }})

Stránka objektu „Billet“

## Nastavenie pohybu kladiva pre hornú maticu

Na stránke **Pohyb hornej matrice** vyberte typ pohybu **Kladivo**, nastavte **Energiu** na hodnotu **250 Klb-in** a **Hmotnosť kladiva** na hodnotu **0,265e-3** **Klb-s^2/in** a **účinnosť úderu** na hodnotu **0,6** (pozri obr. L8.5.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Generate DB.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0005.jpg' | relative_url }})

Na začiatok stránky o pohybe matrice

## Vytvorenie databázy prvých operácií

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

## Simulácia prvej operácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), aby sa otvorilo dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Priebeh simulácie je možné počas jej vykonávania sledovať v režime Simulácia v častiach „Simulačné správy“ a „Simulačná grafika“. Kliknutím na kartu „Simulačné správy“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) (čo je predvolené nastavenie), súbor správ sa bude obnovovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru so správami pridá nasledujúca správa:

"PROGRAM SA ZASTAVIL!

***** „ENERGIA TLAČE BOLA ÚPLNE SPOTREBOVANÁ.“.

## Následné spracovanie výsledkov prvej operácie

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) – otvorí sa postprocesor MO.

#### Graf zdvihu zaťaženia

**Vytvorte graf závislosti medzi zaťažením a zdvihom na osi Y:**  
Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}), otvorí sa okno „Load Stroke Graph“ (Graf zaťaženia zdvihu). V zozname objektov „Plot“ vyberte položku „Top Die“, v roletovom menu osi X vyberte položku „Stroke“ a v roletovom menu osi Y vyberte položku „Y Load“. Kliknite na kartu „Možnosti“ a zaškrtnite políčko „Step tracer“, potom kliknite na ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}). V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) a spustite animáciu (pozri obr. L8.6.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0006.jpg' | relative_url }})

Graf zdvihu zaťaženia

**Graf rýchlosti na osi Y – zdvih:**  
V roletovom menu na osi Y vyberte položku „Y-Speed“, kliknite na ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) a pozrite si graf. (Pozri obr. L8.7.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0007.jpg' | relative_url }})

Graf rýchlosti a zdvihu

## Pridanie druhej operácie

Po dokončení následného spracovania kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) a pridajte ďalšiu operáciu 2D tvárnenia. V tejto operácii používame tie isté objekty a vykonávame druhú operáciu vyfukovania.

V editore operácií kliknite na druhú operáciu tvarovania, v rozbaľovacom menu „Typ nastavenia“ vyberte „Interaktívny režim“ a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekt“.

## Pridávanie objektov

V interaktívnom režime sa pridajú všetky objekty predchádzajúcej operácie a ich údaje sa automaticky načítajú z posledného kroku predchádzajúcej operácie, ako je znázornené na obr. L8.8. Keďže v druhej operácii nie sú potrebné žiadne nové objekty a všetky údaje o objektoch sa načítajú z posledného kroku predchádzajúcej operácie, vyberte z objektového stromu vetvu „Top die Movement“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0008.jpg' | relative_url }})

Interaktívna stránka s nastavením druhého operačného objektu

## Nastavenie pohybu hornej matrice

Na stránke „Pohyb“ nastavte hodnotu **Energie** na **250** **Klb-in**. V strome objektov kliknite na vetvu „Kontakt“.

## Vytvorenie prepojení medzi objektmi

Údaje o kontaktných vzťahoch už boli skopírované z predchádzajúcej operácie, ako je znázornené na obr. L8.9. Ak tomu tak nie je, vyberte typ používateľa, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) a vyberte príslušný koeficient trenia pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Upraviť). Po definovaní koeficientu trenia pre akýkoľvek vzťah je možné rovnaké hodnoty skopírovať do ostatných vzťahov pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) a pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určiť vhodnú toleranciu kontaktu, aby sa kontakty vygenerovali pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}).

V rámci tohto cvičenia sa údaje o vzťahoch medzi objektmi a kontakty načítajú z predchádzajúcej operácie, takže nie je potrebné generovať kontakty; kliknite teda na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí okno „Step controls“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0009.jpg' | relative_url }})

Stránka na generovanie kontaktov medzi objektmi

## Ovládacie prvky krokov

Na stránke „Step controls“ (Ovládacie prvky krokov) definujte definíciu kroku riešenia s konštantným **posunom matrice** nastaveným na hodnotu **0,015** a **počtom krokov** na **50** (pozri obr. L8.10.). Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0010.jpg' | relative_url }})

Ovládacie prvky simulácie

## Vytvorenie databázy druhej operácie

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

## Simulácia druhej operácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), aby sa otvorilo dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Priebeh simulácie je možné počas jej vykonávania sledovať v režime simulácie prostredníctvom okien „Simulation Message“ a „Simulation Graphics“. Kliknutím na kartu „Simulation Message“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}), čo je predvolené nastavenie, súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru so správami pridá nasledujúca správa:

"PROGRAM SA ZASTAVIL!

***** „ENERGIA TLAČE BOLA ÚPLNE SPOTREBENÁ.“.

## Následné spracovanie výsledkov druhej operácie

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) – otvorí sa postprocesor MO.

#### Graf zdvihu zaťaženia:

Prezrite si grafy ZÁŤAŽ-ZÁBER a RÝCHLOSŤ-ZÁBER pre druhý pracovný cyklus, ako je znázornené na obr. L8.11 a obr. L8.12.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0011.jpg' | relative_url }})

Graf závislosti zaťaženia od zdvihu

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0012.jpg' | relative_url }})

Graf rýchlosti v závislosti od zdvihu

## Ukončenie sprievodcu MO

Po dokončení následného spracovania uložte projekt a zatvorte sprievodcu MO kliknutím na tlačidlo „Close ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }})“ alebo výberom možnosti „Quit“ v ponuke „File“.

**Súvisiace témy:**

[15\. Movement Controls Settings]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[6.2. Integrated Manufacturing Process Simulation layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
