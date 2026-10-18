---
lang: sk
title: "Sprievodca 2D tepelným spracovaním Lab2"
---

# Cvičenie 2: Sprievodca 2D tepelným spracovaním

2.1. Úvod

2.2. Začatie riešenia novej úlohy

2.3. Definovanie nastavení procesu

2.4. Definícia nakladaného materiálu

2.5. Definovanie obrobku

2.5.1. Všeobecný popis obrobku

2.5.2. Import geometrie obrobku

2.5.3. Priradenie materiálu

2.5.4. Vytvorenie siete

2.5.5. Priradenie okrajových podmienok

2.5.6. Inicializácia obrobku

2.6. Definícia pojmu „stredný“

2.7. Definícia plánu

2.8. Ovládacie prvky simulácie

2.9. Vytvorenie databázy

2.10. Spustenie simulácie

2.11. Následné spracovanie

## Úvod

Sprievodca tepelným spracovaním je praktický nástroj na nastavenie zložitých úloh tepelných procesov pozostávajúcich z viacerých operácií. V tomto laboratórnom cvičení si ukážeme, ako pomocou tohto sprievodcu pripraviť simuláciu nauhličovania, kalenia a popúšťania oceľového dielu. Toto laboratórne cvičenie môže používateľom pomôcť pochopiť možnosti schémy výpočtu fázových prechodov v programe DEFORM-HT.

## Vytvorenie novej úlohy

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

  
Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu **Nový problém** ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 2DHTWL2.1. V poli Jednotky vyberte prepínač „**2D tepelné spracovanie**“ a ako systém jednotiek vyberte prepínač „**SI**“. Názov úlohy zadajte ako „**Temperovanie**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0001.jpg' | relative_url }})

Definovanie nového problému.

  
Otvorí sa sprievodca viacerými operáciami, pričom ako prvá operácia bude nastavená operácia 2D HT, ako je znázornené na obr. 2DHTWL2.2.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0002.jpg' | relative_url }})

Nový projekt s 2D HT prevádzkou.

## Nastavenie parametrov procesu

Po otvorení sprievodcu viacerými operáciami sa v oblasti editora vlastností zobrazí stránka Nastavenia procesu, ako je znázornené na obr. 2DHTWL2.2. Používateľ môže nastaviť režim simulácie podľa požiadaviek simulácie spolu s ovládacími prvkami na definovanie krokov. V rámci tohto laboratórneho cvičenia zapneme „**Deformácia**“, „**Difúzia**“ a „**Fázová transformácia**“. Definícia krokov sa nastaví na stránke Ovládacie prvky simulácie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Zoznam materiálov, keďže na stránke Inicializácia nemusíme vykonávať žiadne zmeny.

## Načítavanie materiálu do zoznamu materiálov

Na stránke „Zoznam materiálov“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať materiál zo súboru) a importujte materiál „**Demo_Temper_Steel.KEY**“ z inštalačnej cesty \SFTC\DEFORM\v*_*\2d\LABS\HeatTreat (pozri obr. 2DHTWL2.3.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte vyskakovacie dialógové okno na výber materiálu, kde môžete vidieť, že materiál má definovaných viacero fáz, a môžete si prezrieť vlastnosti materiálu v jednotlivých fázach pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), ktorým prejdete na príslušnú fázu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostanete na stránku objektu obrobku.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0003.jpg' | relative_url }})

Import materiálu na stránku „Zoznam materiálov“.

## Definovanie obrobku

### Všeobecná definícia objektu obrobku

Na stránke „Obrobok“ zmeňte typ objektu na **Elastoplastický** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (pozri obr. 2DHTWL2.4.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0004.jpg' | relative_url }})

Všeobecná definícia obrobku.

### Import geometrie obrobku

Na stránke Geometria kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (import geometrie z knižnice) a importujte súbor „**TemperingPart.GEO**“ z inštalačnej cesty \SFTC\DEFORM\v*_*\2d\LABS\HeatTreat, ako je znázornené na obr. 2DHTWL2.5. Pomocou akcie ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte importovanú geometriu. Ak sa vyskytnú akékoľvek problémy s geometriou, táto sa opraví a zobrazí sa správa, ako je znázornené na obr. 2DHTWL2.6. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostanete na stránku Material.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0005.jpg' | relative_url }})

Import geometrie obrobku.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0006.jpg' | relative_url }})

Oprava geometrických chýb v importovanej geometrii.

### Priradenie materiálu k obrobku

Na stránke „Materiál“ vyberte zo zoznamu materiálov položku **Demo.Steel**, aby ste tento materiál priradili k obrobku, ako je znázornené na obr. 2DHTWL2.7. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) prejdite na stránku „Mriežka“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0009.jpg' | relative_url }})

Priradenie materiálu k obrobku.

### Vytvorenie siete pre obrobok

Na stránke „Mesh“ nastavte cieľový počet prvkov siete na **300**. Pre lepšiu predikciu fázového rozloženia a obsahu atómov na povrchu je potrebné definovať štruktúrovanú sieť, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), čím prepnete nastavenia siete do expertného režimu, vyberte Coating mesh a pridajte 2 vrstvy povlaku, ako je znázornené na obr. 2DHTWL2.9. Nastavte „**Režim hrúbky**“ na „**pomer k celkovému rozmeru objektu**“ a zadajte **500** **mikrónov** a **1000****mikrónov** ako hrúbku pre vrstvu 1, resp. 2, ako je znázornené na obr. 2DHTWL2.9. Ako materiál pre povlak ponecháme predvolený výber „**Demo.Ste****el**“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Sieť vygenerovaná pre obrobok spolu so štruktúrovanou sieťou vyzerá tak, ako je znázornené na obr. 2DHTWL2.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) pre prepnutie do režimu s návodom. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s okrajovými podmienkami.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0007.jpg' | relative_url }})

Určenie počtu prvkov siete obrobku.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0008.jpg' | relative_url }})

Nastavenia sieťoviny pre povrchovú úpravu obrobku.

### Priradenie okrajových podmienok k obrobku

Na stránke „Okrajové podmienky“ zafixujeme uzly v smere Y na spodnom okraji obrobku, ako je znázornené na obr. 2DHTWL2.10. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Inicializácia“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0010.jpg' | relative_url }})

Priradenie rýchlosti BCC k obrobku.

### Inicializácia rozloženia fáz a percentuálneho podielu atómov v obrobku

Na stránke „Inicializácia“ kliknite na kartu „**Mikrostruktúra**“ a v treťom stĺpci nastavte počiatočnú hodnotu „**Perlit + bainit**“ na „1“, ako je znázornené na obr. 2DHTWL2.11. Následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}), aby sa inicializovala hodnota pre celý obrobok.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0011.jpg' | relative_url }})

Inicializácia fázových objemových podielov obrobku.

Na inicializáciu obsahu atómov kliknite na **Node****Data![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }})** a vyberte kartu „**Diffusion**“, čím inicializujete hodnotu obsahu atómov, ako je znázornené na obr. 2DHTWL2.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}), otvorí sa vyskakovacie okno „Inicializovať uzlové údaje“, vyberte „Rozsah“ a nechajte rozsah uzlov ako predvolený výber všetkých uzlov v počiatočnom a koncovom uzle. Nastavte „Hodnotu“ na 0,2 a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) na inicializáciu hodnoty, pozri obr. 2DHTWL2.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}), aby ste zatvorili okno „Inicializovať údaje uzlov“, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili dialógové okno s údajmi uzlov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali podrobnosti o prostredí.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0012.jpg' | relative_url }})

Inicializácia obsahu atómu pre obrobok.

## Stredná definícia pre tepelné spracovanie

Na stránke „**Podrobnosti o médiách**“ definujeme rôzne médiá a s nimi súvisiace zóny prenosu tepla,

  
1\. Premenujte prvé médium na „**Furnace**“ a nastavte koeficient prenosu tepla (HTC) „**Default**“ na konštantu **0,1**. Zaškrtnite políčko „Radiation“, ako je znázornené na obr. 2DHTWL2.13.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0013.jpg' | relative_url }})

Definícia prostredia pece.

2\. Pridajte stredné prostredie „**Polymer********Solution**“, zrušte zaškrtnutie políčka „Radiation“ a nastavte jeho zónu HTC „**Default**“ ako funkciu teploty. Funkciu definujte pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}), ako je znázornené v tabuľke 1 a na obr. 2DHTWL2.14.

Teplota  |  HTC  
---|---  
20 |  3,5  
400 |  8,5  
700 |  15  
900 |  5,2  
  
Funkcia HTC v polymérnom roztoku.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0014.jpg' | relative_url }})

Definovanie funkcie HTC pre polymérny roztok.

3\. Pridajte zónu prenosu tepla do prostredia „**Polymer********Solution**“. Kliknutím na hranicu obrobku určite túto zónu pomocou výberového režimu ![]({{ '/assets/icons/pre_icons/mo_bcc_start_and_end_ico.jpg' | relative_url }}), ako je znázornené na obr. 2DHTWL2.15. Vyberte HTC ako funkciu teploty a definujte hodnoty funkcie pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}), ako je znázornené v tabuľke 2 a na obr. 2DHTWL2.16.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0015.jpg' | relative_url }})

Definícia zóny 1 polymérneho média.

Teplota  |  HTC  
---|---  
20 |  3,5  
200 | 4,5  
400 |  8,8  
700 |  3,5  
900 |  2,8  
  
Funkcia HTC v prostredí s polymérnym roztokom v zóne 1.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0016.jpg' | relative_url }})

Určenie funkcie HTC v prostredí polymérneho roztoku v zóne 1.

4\. Pre zónu 1 prostredia „Polymer Solution“ vyberte „Rýchlosť difúznej povrchovej reakcie“ ako funkciu teploty, ako je uvedené v tabuľke 3. Definujte túto funkciu podľa obrázkov 2DHTWL2.17 a 2DHTWL2.18.

Teplota  |  RRC  
---|---  
20 |  0,1  
500 | 0,2  
1000 |  0,6  
  
Funkcia rýchlosti difúznej povrchovej reakcie v prostredí polymérneho roztoku, zóna 1 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0017.jpg' | relative_url }})

Nastavenie vlastností žiarenia a difúzie v zóne 1.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0018.jpg' | relative_url }})

Určenie funkcie rýchlosti povrchovej reakcie v prostredí polymérneho roztoku v zóne 1

5\. Pridajte ešte jedno médium a premenujte ho na „Air“. Nastavte hodnotu „Default“ HTC na 0,02 a zaškrtnite políčko „Radiation“, ako je znázornené na obr. 2DHTWL2.19. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) naplánujte operácie tepelného spracovania.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0019.jpg' | relative_url }})

Definícia vzdušného prostredia.

## Plánovanie operácií tepelného spracovania

V tomto laboratórnom cvičení budeme vykonávať päťstupňový proces tepelného spracovania. Na tento účel zadajte na stránke „**Plán**“ päťstupňový plán podľa nižšie uvedeného postupu.  
  
1\. Jedna hodina (3600 s) ohrevu pece. Teplota pece je stanovená ako funkcia času. Túto funkciu je možné zadať kliknutím na príslušnú bunku „Definovať“ v stĺpci „Pokročilé“ (pozri tabuľku 4, obr. 2DHTWL2.20, obr. 2DHTWL2.21 a obr. 2DHTWL2.22).

Čas(y) |  Teplota  
---|---  
0 |  20  
600 |  660  
1200 |  880  
3600 |  880  
  
Nastavenie funkcie teploty v peci počas prevádzky ohrevu pece.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0020.jpg' | relative_url }})

Plánovanie procesov tepelného spracovania.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0021.jpg' | relative_url }})

Vopred nastavenie časového okna kúrenia v peci

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0022.jpg' | relative_url }})

Okno s podrobnosťami o definícii funkcie

2) Naplánujte druhú operáciu HT na 10 minút (600 s) ochladzovania v polymérnom roztoku. Nastavte obsah „Atom“ na hodnotu 0,8 pri teplote 30 °C, ako je znázornené na obr. 2DHTWL2.23.

3) Naplánujte tretiu operáciu temperovania HT ako ohrev pece po dobu 30 minút (1800 s) pri teplote 250 °C, ako je znázornené na obr. 2DHTWL2.23.

4) Naplánujte štvrtú operáciu temperovania HT ako ohrev pece po dobu 30 minút (1800 s) pri teplote 350 °C, ako je znázornené na obr. 2DHTWL2.23.

5) Naplánujte štvrtú operáciu HT – temperovanie – ako chladenie na vzduchu po dobu jednej hodiny (3600 s) pri teplote okolia 20 °C, ako je znázornené na obr. 2DHTWL2.23, a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Step“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0023.jpg' | relative_url }})

Harmonogram operácií tepelného spracovania.

## Definovanie ovládacích prvkov simulácie

Na stránke „**Krok**“ vyberte tlačidlo **Auto** a nastavte „**Zmena teploty zmena na krok**“ na hodnotu **5°** C, minimálny čas na krok ponechajte na hodnote **0,001** s a maximálny čas na krok na hodnote **10** s. Nastavte **Krok prírastku na uloženie** na hodnotu **10**. (Pozri obr. 2DHTWL2.24.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0024.jpg' | relative_url }})

Definovanie krokových pokynov pre simuláciu tepelného spracovania.

## Vytvoriť databázu

Kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali chyby a varovania, ktoré je potrebné vyriešiť pred vytvorením databázy. Ak neexistujú žiadne chyby ani varovania, ktoré by ovplyvnili výstup simulácie, vytvorte databázu kliknutím na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), pozri obr. 2DHTWL2.25. Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0025.jpg' | relative_url }})

Vytvorenie databázy

## Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DHTWL2.26. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0026.jpg' | relative_url }})

Spustiť okno simulácie

  
Priebeh simulácie je možné počas jej vykonávania sledovať prostredníctvom okien „Simulation Message“ a „Process Monitor“ v režime simulácie. Kliknutím na kartu „Simulation Message“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}), čo je predvolené nastavenie, súbor správ sa bude aktualizovať každých pár sekúnd.  
  
Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a poskytuje údaje o tom, ako dobre simulácia prebieha.  
Po dokončení simulácie všetkých operácií tepelného spracovania sa na koniec súboru správ pridá správa, ako je znázornené na obr. 2DHTWL2.27.  
  
Každá definovaná fáza sa vykoná ako samostatná operácia a používateľ musí počkať, kým sa simulácia všetkých fáz dokončí.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0027.jpg' | relative_url }})

Sledovanie priebehu simulácie tepelného spracovania.

## Následné spracovanie

Po ukončení simulácie kliknite na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky. Priebeh minimálnej a maximálnej teploty by mal vyzerať ako na grafe nižšie (pozri obr. 2DHTWL2.28.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0028.jpg' | relative_url }})

Priebeh minimálnych a maximálnych teplôt počas simulácie tepelného spracovania.

Zaznačte objemový podiel jednotlivých fáz na konci všetkých operácií (pozri obr. 2DHTWL2.29.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0029.jpg' | relative_url }})

Rozloženie objemového podielu po ukončení všetkých operácií.

  
Zaznačte dominantný atóm na základe difúzie a sledujte rozloženie dominantného atómu v rôznych fázach procesu temperovania (pozri obr. 2DHTWL2.30.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0030.jpg' | relative_url }})

Rozloženie dominantných atómov na konci každej operácie.
