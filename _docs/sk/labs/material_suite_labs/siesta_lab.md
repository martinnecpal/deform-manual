---
lang: sk
title: "SIESTA LAB"
---

# SIESTA GENEROVANIE SÚBOROV

1.1. Úvod do SIESTY

1.2. Spustite výstup SIESTY v Material suite

1.3. Export do SIESTY

## Úvod do SIESTY

DEFORM vyvinul zariadenie na export údajov z databázy do súboru SIESTA, čo je formát súboru požadovaný softvérom DARWIN vyvinutým Juhozápadným výskumným ústavom. Viac podrobností o DARWINOVI nájdete tu:

  
<http://www.darwin.swri.org/html_files/background/summary.html>

## Spustite výstup SIESTY v Material suite

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte databázu importovaním 2D_Example/SI/HeatTreat/ MRX_SRX_2D_SI.KEY s ID problému ako **MRX_SRX_2D_SI** v NG Pre, potom ju simulujte z hlavného GUI pomocou Run. Pripravte si ho, na tomto príklade ukážeme, ako exportovať výstupný súbor SIEST v Material suite.

  
Teraz z hlavného grafického rozhrania výberom súboru **MRX_SRX_2D_SI.DB** kliknite na Material Suite v časti „Post Processor“ a otvorte modul Material Suite, ako je znázornené na obr. SIESTAL1.1.

![]({{ '/assets/images/labs/material_suite_labs/siesta_lab/image0001.jpg' | relative_url }})

Otváracia sada materiálov z hlavného grafického rozhrania

  
Po otvorení hlavného okna pre balík materiálov rozbaľte položku „* * Výkon * * “ a kliknite na ikonu „**SIESTA** “ zo zoznamu Výkonov, ako je znázornené na obr. SIESTAL1.2., do stromu úloh sa pridá nová položka úlohy „SIESTA Output“.

  
  
![]({{ '/assets/images/labs/material_suite_labs/siesta_lab/image0002.jpg' | relative_url }})

Spustenie výstupu SIESTY v materiáli

## Exportovať do SIESTY

Kliknite na kartu „* * Výstup * * “, vyberte objekt v zozname objektov a vyberte stavové premenné, ktoré sa majú exportovať (Stres, Teplota, Efektívne napätie a Veľkosť zrna) zo zoznamu stavových premenných, potom vyberte krok v databáze, ktorý sa má exportovať (tu vyberáme posledný krok). Kliknite na „**Export to SIESTA** “ a vyberte umiestnenie na uloženie súboru a názov súboru. V predvolenom nastavení sa súbor SIESTA uloží s názvom „Database+step number.ISO“. Napríklad názov databázy je MRX_SRX_2D_SI a krok, ktorý sme vybrali, je **717** , generovaný súbor SIESTA bude * *MRX_SRX_2D_SI_Step717.sio * *, ako je znázornené na obr. SIESTAL1.3.

![]({{ '/assets/images/labs/material_suite_labs/siesta_lab/image0003.jpg' | relative_url }})

Exportovanie súboru SIESTA v súbore materiálov
