---
lang: sk
title: "23.1. Spustenie, zastavenie a obnovenie simulácií"
---

# 23.1. Spustenie, zastavenie a obnovenie simulácií

Simuláciu spustíte kliknutím na ![]({{ '/assets/icons/simulator_icons/gui_run_button.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/simulator_icons/mo_run_icon.jpg' | relative_url }}) (pozri obr. 23.1.1.). Tým sa spustí séria operácií potrebných na vykonanie simulácie a v prípade potreby na vytvorenie nových sietí (pozri obr. 23.1.1.).

Informácie o behu programu sa zapíšu do súborov ProblemId.MSG a ProblemId.LOG.

  * Informácie o vykonaní, vrátane údajov o konvergencii pre každý krok a chybových hlásení simulácie, sa nachádzajú v súbore .MSG.

  * Informácie o simulácii a prepočítaní siete, časoch vykonania, fatálnych chybách a type spustenej úlohy FEM (32-bitová alebo 64-bitová simulácia) v prípade 3D úlohy nájdete v súbore .LOG alebo v príkazovom okne, z ktorého bol program DEFORM spustený.

  * Kliknutím na odkaz ![]({{ '/assets/icons/simulator_icons/open_simulation_graphics_label.jpg' | relative_url }}) v záložke „Náhľad“ si používateľ môže prezrieť grafické znázornenie simulácie v tejto záložke.

  * Funkcia „Poznámka“ umožňuje používateľovi zadávať a ukladať akékoľvek poznámky súvisiace s aktuálnou simuláciou.

![]({{ '/assets/images/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/image001.jpg' | relative_url }})

Hlavné okno grafického rozhrania DEFORM – Hlavné okno (počas spustenia modelu)

Na obr. 23.1.1.:

**1- Spustiť** – táto voľba slúži na spustenie úlohy.

**2 – Zastaviť** – táto voľba slúži na zastavenie bežiacej úlohy.

Možnosť **3 – Pokračovať** slúži na pokračovanie v obnovenej úlohe.

Simuláciu je možné zastaviť kliknutím na ![]({{ '/assets/icons/simulator_icons/gui_stop_button.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/simulator_icons/mo_stop_icon.jpg' | relative_url }}) v hlavičke (pozri obr. 23.1.1.). Simuláciu je možné zastaviť aj pomocou tlačidiel „Kill“ alebo „Stop“ v monitore procesu (pozri obr. 23.1.2.). V prípade voľby „Stop simulation“ sa simulácia zastaví po dokončení aktuálneho kroku. V prípade voľby „Kill Simulation“ sa simulácia zastaví pri aktuálnej iterácii.

**Ukončenie simulačného procesu**

Ďalším spôsobom, ako zastaviť simuláciu, je ukončenie súboru „DEFORM_RUNNING_JOB_STATUS.TXT“ v hlavnom okne grafického rozhrania. Keďže príkaz „Stop“ zastaví simuláciu až po dokončení aktuálneho kroku, môže trvať značnú dobu, kým sa simulácia zastaví. Ak chcete simuláciu ukončiť okamžite, je potrebné proces DEF_SIM.EXE ukončiť priamo z operačného systému.

![]({{ '/assets/images/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/image002.jpg' | relative_url }})

**Ukončenie úlohy z okna Process Monitor**

Simuláciu je možné pokračovať alebo obnoviť od miesta, kde sme ju zastavili, kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/gui_continue_button.jpg' | relative_url }}) (pozri obr. 23.1.1.) v palete Simulátor na pravej strane alebo na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_continue_icon.jpg' | relative_url }}) v hlavičke.

**Simulácia s viacerými procesormi**

Možnosť „Počet procesorov na úlohu“ umožňuje používateľovi definovať nastavenia viacerých procesorov používaných na riešenie úlohy, ako aj počet procesorov používaných na každom počítači. V poli „Názov počítača“ sa teraz zobrazí správny názov počítača. (Pozri obr. 23.1.3.)

Po výbere typu FEM a typu stroja kliknite na tlačidlo „Štart“, aby ste spustili simuláciu.

**Možnosť čiastočne paralelnej FEM** spúšťa v paralelnom režime iba časť simulácie zodpovednú za riešenie, zatiaľ čo ostatné operácie, ako je výpočet tuhostnej matice modelu, prečlenenie siete a interpolácia, prebiehajú na jednom procesore primárneho hostiteľského počítača. V prostredí PC to vedie k spusteniu jedného súboru DEF_SIM.EXE na každom z požadovaných procesorov.

**Plne paralelný FEM** spracováva celý model tak, aby sa spúšťal paralelne, vrátane matice tuhosti modelu, prečlenenia siete a interpolácie, okrem fázy riešenia. V prostredí PC vedie plne paralelný beh k spusteniu jedného súboru DEF_SIM.EXE na každom z požadovaných procesorov. Pokiaľ ide o celkový čas simulácie, väčšie modely zvyčajne ťažia z tohto multiprocesového nastavenia.

![]({{ '/assets/images/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/image003.jpg' | relative_url }})

Okno „Nastavenie viacerých procesorov“

Poznámka:

  1. Po výbere týchto možností systém uloží informácie do lokálnych súborov (DEF_MPIenv.DAT a DEF_MPI_p4penv.DAT). Program FEM vyhľadáva tieto súbory na spustenie paralelných výpočtov.

  2. Od tejto verzie bude Správca úloh zobrazovať iba viaceré inštancie programu DEF_SIM.EXE v režime MPI, a to namiesto programov DEF_SIM.EXE, DEF_SIM_P4P.EXE alebo DEF_SIM_P4P.EXE v závislosti od nastavenia MPI.

  3. Pokiaľ nie sú nainštalované staršie verzie MPICH, je teraz povinné nainštalovať 32-bitovú verziu MPICH1 v1.2.1 pre 32-bitové počítače a dodatočne 64-bitovú verziu MPICH2 v1.2.1 pre 64-bitové počítače.

**Súvisiace témy:**

[23\. Introduction to Simulator](/docs/en/simulator/23_deform_simulator/23_introduction_to_deform_simulator/)

[23.2. Interactive and batch modes using Run option](/docs/en/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/)

[23.3. Simulation Graphics](/docs/en/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/)

[23.5. Setting up MPICH](/docs/en/simulator/23_deform_simulator/23_5_setting_up_mpich/)

[23.6. Running Shared folder Simulations](/docs/en/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/)

[23.7. Trouble Shooting Simulation Running](/docs/en/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/)

[Post Processor](/docs/en/post_processor/post_processor_mainpg/)
