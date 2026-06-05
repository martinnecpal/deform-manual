---
lang: sk
title: "21. Vytvorenie databázy"
---

# 21. Vytvorenie databázy

**[2D, 3D]:** Sada simulačných údajov zadaná do predspracovateľa môže byť uložená ako nová databáza alebo pridaná na koniec existujúceho databázového súboru. Informácie budú uložené ako záporný krok, čo znamená, že boli uložené z predspracovateľa, a nie zo simulačného modulu. V existujúcej databáze budú v tomto momente prepísané všetky kroky vyššie ako aktuálny krok. Simulačná databáza bude kontrolovaná počas zapisovania.

Keď je stav „Pripravené na vytvorenie databázy“, môžeme vytvoriť súbor databázy. Ak je stav „Chyba zadávania“, môžeme si v súbore správ prečítať chybovú správu týkajúcu sa nastavenia (v ktorom nastavení chýbajú údaje alebo sú nesprávne). 

Od verzie 12.0.2 sa v okne „Generate DB file“ (Vytvoriť súbor DB) zobrazuje prehľad nastavení simulácie prevádzky, ako je znázornené na obr. 21.1. 

Databáza simulácie sa skontroluje po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), ako je znázornené na obr. 21.1.

![]({{ '/assets/images/pre-processor/21_database_generation/image001.jpg' | relative_url }})

Okno na vytvorenie databázy

**Chyby v údajoch**

Chyby sú závažné problémy v súbore údajov, ktoré bránia spusteniu simulácie. Tieto chyby sú pri kontrole údajov označené červenými vlajočkami a je potrebné ich odstrániť, aby bolo možné údaje zapísať do databázy.

**Upozornenia týkajúce sa údajov**

Upozornenia sú stavy, ktoré môžu spôsobiť nežiaduce správanie riešenia, ale nezabránia spusteniu simulácie. Upozornenia sú označené žltými vlajočkami. Ak sa vyskytnú upozornenia, každé z nich by sa malo dôkladne skontrolovať a mal by sa zistiť ich zdroj.

Niektoré varovania poukazujú na nezvyčajné, avšak platné situácie v údajoch. V takom prípade ich možno ignorovať a simuláciu spustiť.

**Výhody integrovanej databázy**  
V integrovanej databáze môžeme ukladať 2D a 3D simulácie a optimalizované animácie. Problémy s kompatibilitou verzií databázy už neexistujú. Obr. 21.2 znázorňuje štruktúru integrovanej databázy.

![]({{ '/assets/images/pre-processor/21_database_generation/image002.jpg' | relative_url }})

Okno výberu kroku v databáze

**Súvisiace témy:**

[DEFORM Basic file system](/docs/sk/about_deform/1_introduction_to_deform/1_10_basic_file_system/)

([Primary Die selection from simulation control](../9_simulation_controls/9_2_defining_step.htm#Primary_die_\(PDIE\))

[Primary Die selection from Object general definition window](../11_general_object_data_definition/11_general_object_data_definition.htm#11.5._Primary_Die)

[Step definition in the simulation control](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)

[Max. Interference depth for remesh settings](../13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.8._Remeshing_criteria)

([Volume compensation selection from Object properties window](../16_object_properties/16_1_deformation_properties.htm#16_1_3_Target_Volume_\(TRGVOL\))

[Inter-Object data definition window](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[23.1. Start, Stop and Resume Simulation](/docs/sk/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)

[23.2. Interactive and batch modes using Run option](/docs/sk/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/)

[23.3. Simulation Graphics](/docs/sk/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/sk/simulator/23_deform_simulator/23_4_process_monitor/)
