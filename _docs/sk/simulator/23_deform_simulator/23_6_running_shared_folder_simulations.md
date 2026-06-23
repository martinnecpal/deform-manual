---
lang: sk
title: "23.6. Spúšťanie simulácií zdieľaných priečinkov"
---

# 23.6. Spúšťanie simulácií zdieľaných priečinkov

Táto časť poskytuje používateľovi návod na nastavenie servera fronty úloh (Batch Queue Server) a simulačného servera (Simulation Server) v sieti. Pred vykonaním tohto nastavenia je potrebné nakonfigurovať sieťové disky. Tento postup vysvetlíme na príklade štyroch počítačov: lmwin11, emerald, tuscan a puce. Počítač lmwin11 slúži ako licenčný server, ktorý spravuje licenciu Deform, a zároveň ako server fronty dávok, ktorý riadi poradie spúšťania úloh. Ostatné tri počítače sú klientske stroje, z ktorých emerald slúži ako simulačný server na spúšťanie úloh FEM. 

  
Najskôr **vytvorte zdieľanú zložku na simulačnom serveri** nasledujúcim spôsobom (pozri obr. 23.6.1.).

  1. Prihláste sa do počítača, z ktorého chcete zdieľať, t. j. **Simulation****Server** emerald.

  2. Kliknite pravým tlačidlom myši na priečinok, ktorý chcete zdieľať, napr. priečinok TEST, prejdite do okna Vlastnosti a vyberte **Zdieľanie**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Zdieľať**.

  3. Nakoniec kliknite na tlačidlo „Hotovo“. 

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image001.jpg' | relative_url }})

Zdieľajte priečinok na simulačnom serveri. 

Nezabudnite, že pred vytvorením zdieľanej zložky je potrebné sa uistiť, že je na vašom simulačnom serveri povolené zdieľanie súborov a tlačiarní, a to podľa nasledujúcich krokov.

  1. Prejdite do Ovládacieho panela (alebo do Nastavení).

  2. Prejdite do Centra sietí a zdieľania ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) a vyberte možnosť Zmeniť pokročilé nastavenia zdieľania.

  3. Zapnite funkciu vyhľadávania sietí a zdieľania súborov a tlačiarní.

  
Po druhé, **otvorte zdieľanú zložku** nasledujúcim spôsobom.

  1. Otvorte počítač, v ktorom chcete **získať prístup k zdieľanej zložke**, t. j. **klientsky počítač**, napríklad tuscan.

  2. Otvorte Průzkumník súborov a do adresného riadka zadajte \\\<názov simulačného servera>, t. j. \\\emerald (alebo kliknite na kartu Sieť v ľavom bočnom paneli a dvakrát kliknite na počítač emerald). 

  3. **Kliknite pravým tlačidlom myši na zdieľanú zložku** TEST a vyberte možnosť **Priradiť sieťovú jednotku…**, ako je znázornené na obr. 23.6.2., aby ste vytvorili priradenú jednotku s jedinečným názvom, napríklad „S:“ (pozri obr. 23.6.3.)

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image002.jpg' | relative_url }})

Otvorte zdieľanú zložku z klientskeho počítača a priradte sieťovú jednotku.

  
![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image003.jpg' | relative_url }})

Pripojte sieťovú jednotku k zdieľanej zložke.

Teraz môžete vidieť pripojenú jednotku v okne **Tento počítač**, ako je znázornené na obr. 23.6.4. Upozorňujeme, že vytvorenú jednotku môžete odstrániť tak, že kliknete pravým tlačidlom myši na jej názov a vyberiete možnosť Odpojiť.

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image004.jpg' | relative_url }})

Pripojený disk v sekcii „Tento počítač“.

Po tretie, **nastavte pripojené disky v programe Deform Setup** podľa nasledujúcich krokov.

  1. Na každom klientskom počítači spustite program **Deform Setup** a synchronizujte sa s licenčným serverom; keď sa zobrazí správa, že licenčný server beží, kliknite na tlačidlo OK (pozri obr. 23.6.5).

  2. Ako je znázornené na obr. 23.6.6, na karte **Zdieľané priečinky** môžete vytvoriť **nový****priečinok**, ktorý bude priradený k priečinku \\\emerald\TEST na simulačnom serveri emerald.

  3. **Pridajte zdieľaný priečinok** z klientskych počítačov, aby ste mohli zdieľať priečinok s projektom a databázu (pozri obr. 23.6.7.). 

  4. Nakoniec nezabudnite **uložiť** posledné zmeny v nastaveniach deformácie. Obr. 23.6.8 znázorňuje uložené sieťové disky na klientskych počítačoch tuscan a puce (t. j. S: a R:), ktoré sú priradené k zdieľanej zložke na simulačnom počítači emerald.

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image005.jpg' | relative_url }})

V nastaveniach programu Deform vykonajte synchronizáciu s licenčným serverom.

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image006.jpg' | relative_url }})

Vytvorte nový adresár s názvom počítača a adresárom, v ktorom sa nachádza zdieľaná zložka (na simulačnom serveri).

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image007.jpg' | relative_url }})

Pridajte zdieľané priečinky zo simulačného servera a z klientskych počítačov pomocou písmena sieťovej jednotky. 

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image008.jpg' | relative_url }})

Uložte zdieľané disky v nastaveniach programu Deform.

Teraz majú obe sieťové jednotky S: a R: na klientskych počítačoch „tuscan“ a „puce“ prístup k zdieľanej zložke TEST na simulačnom serveri „emerald“, ako je vidieť na obr. 23.6.9. Užívatelia tak môžu pracovať na súboroch projektu MO a databázach na svojich lokálnych počítačoch a spúšťať ich na simulačnom serveri. 

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image009.jpg' | relative_url }})

Prístup k simulačnému serveru z pripojeného sieťového disku na klientskom počítači.

  
Používatelia môžu následne odosielať úlohy na simulačný server nasledovným spôsobom.

  1. Na klientskom počítači vyberte sieťovú jednotku, napríklad „tuscan“ (zobrazí sa umiestnenie na lokálnom počítači).

  2. Vyberte databázu, ktorú chcete spustiť (zobrazí sa databáza na vzdialenom počítači).

  3. Otvorte okno „Run options“ v programe tuscan, ako je znázornené na obr. 23.6.10.

  4. V časti „Batch mode“ vyberte simulačný server „emerald“ (zobrazí sa umiestnenie na vzdialenom počítači).

  5. Skontrolujte server (Zobrazí sa dialógové okno so stavom.)

  6. Odoslať do fronty (na zariadení „emerald“ sa spustí program DEF_SIM_64.exe.)

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image010.jpg' | relative_url }})

Odoslať úlohu do fronty dávkového spracovania.

Obr. 23.6.11. znázorňuje priebeh riadenia po odoslaní úlohy. Tento obrázok ukazuje, ako systémy získavajú licenciu zo servera na vykonanie danej úlohy. Vidíme, že klientske počítače tuscan a puce získavajú licencie z licenčného servera a zo servera fronty dávkových úloh lmwin11, aby mohli otvoriť aplikácie Deform, resp. pridať úlohy do fronty dávkových úloh. Simulačný server „emerald“ získava licenciu zo servera „lmwin11“ na spustenie simulácie a zároveň pristupuje k serveru fronty dávkových úloh, aby pridal databázy do zoznamu.   
Zatiaľ čo prebiehajú všetky tieto operácie, môžeme tento prebiehajúci proces sledovať prostredníctvom nástrojov Process Monitor a License Manager Administrator.

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image011.jpg' | relative_url }})

Postup po odoslaní úlohy.

Na záver je potrebné poznamenať, že používatelia môžu alternatívne odosielať úlohy na simuláciu pomocou vzdialených simulačných serverov v dávkovom režime prostredníctvom možností v ponuke „Spustiť“. Týmto spôsobom sa úlohy dočasne presunú na vzdialený simulačný server na účely simulácie, simulácia sa dokončí a projekt sa skopíruje späť, takže nie je potrebné mapovať zdieľanú zložku na vzdialenom počítači, čo znižuje zaťaženie lokálneho počítača. Bude to však jednoduchšie, ak všetky simulačné súbory zostanú na simulačnom počítači a budeme k nim pristupovať prostredníctvom sieťových diskov. Používatelia sa môžu stretnúť s ťažkosťami počas prenosu súborov a spúšťania simulácie v dôsledku sieťovej komunikácie, čo spôsobí, že spúšťanie simulácie na vzdialenom počítači bude náročnejšie ako spúšťanie simulácie zo zdieľaného priečinka. 

**Súvisiace témy:**

[23.1. Start, Stop and Resume Simulation](/docs/en/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)

[23.2. Interactive and batch modes using Run option](/docs/en/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/)

[23.3. Simulation Graphics](/docs/en/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/)

[23.5. Setting up MPICH](/docs/en/simulator/23_deform_simulator/23_5_setting_up_mpich/)

[23.8. Trouble Shooting Simulation Running](/docs/en/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/)

[Pre-Processor](/docs/en/post_processor/post_processor_mainpg/)

[Integrated Manufacturing Process (MO)](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_integrated_manufacturing_process_layout/)
