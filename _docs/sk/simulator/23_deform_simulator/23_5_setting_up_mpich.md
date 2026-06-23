---
lang: sk
title: "23.5. Nastavenie MPICH"
---

# 23.5. Registrácia MPICH (platí pre verziu v11.1.1 a staršie verzie)

## Registrácia 64-bitového 3D FEM enginu v počítači

V rámci inštalácie DEFORM v*_* (kde *_* je číslo verzie DEFORM) sa používateľovi zobrazí možnosť inštalácie „MPICH2 64bit“. Na 64-bitových počítačoch je táto inštalácia nevyhnutná na spustenie 64-bitového 3D FEM enginu. Táto časť inštalácie si tiež vyžaduje vykonanie nasledujúcich krokov po inštalácii, aby bolo zabezpečené 64-bitové runtime prostredie:

Od verzie DEFORM v11.0 sa nasledujúce požiadavky na nastavenie 64-bitovej verzie MPICH2 úplne riešia už počas samotnej inštalácie systému. Nasledujúce kroky je možné použiť aj na riešenie prípadných problémov súvisiacich s MPICH2, ak by sa neskôr z akéhokoľvek dôvodu vyskytli.

  1. Otvorte príkazové okno ako správca, prejdite do priečinka MPICH2 pomocou príkazu _'cd c:\Program Files\MPICH2\bin'_ a postupne spustite dva príkazy: _'mpd.exe -install' a 'smpd.exe -restart'_.

  2. Otvorte príkazové okno ako správca, prejdite do adresára MPICH2 pomocou príkazu '_cd c:\Program Files\MPICH2\bin'_ a spustite príkaz _'mpiexec.exe -register'_ s uvedením používateľského mena a hesla.

  3. V prípade služieb SimulationServer musí používateľ prejsť do systémových služieb, vybrať spustenú službu „_DeformSimServer_“, kliknúť pravým tlačidlom myši a zvoliť možnosť „Vlastnosti“ a na karte „Prihlásenie“ nastaviť meno používateľského účtu a heslo pre daného používateľa.

## Spustenie 64-bitového 3D FEM enginu v systéme Linux na PC

  * V grafickom rozhraní 3D / 2D3D vyberte úlohu, prejdite do časti „Run options“ a vyberte možnosť „64 bit“. Kliknutím na tlačidlo „Start“ spustíte 64-bitovú simuláciu.

  * Na spustenie 64-bitového behu FEM z hlavného okna grafického rozhrania je potrebný súbor „64bit.DAT“ v zložke s úlohou. Tento súbor „64bit.DAT“ sa vytvorí automaticky po výbere možnosti 64-bitového behu v nastaveniach spustenia. Bez tohto súboru sa uprednostní bežný 32-bitový kód FEM.

**Poznámka:**

  1. Táto 64-bitová verzia dokáže spracovať rozsiahle modely, ktoré vyžadujú viac ako 2 GB hlavnej pamäte.

  2. Podpora 64-bitovej verzie sa vzťahuje iba na 3D FEM engine.

  3. Pri vytváraní modulu FEM s užívateľskými rutinami použite prosím identifikátor operačného systému centos_linux64.

**Súvisiace témy:**

[23.1. Start, Stop and Resume Simulation](/docs/en/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)

[23.2. Interactive and batch modes using Run option](/docs/en/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/)

[23.3. Simulation Graphics](/docs/en/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/)
