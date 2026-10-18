---
lang: sk
title: "Sprievodca 2D tepelným spracovaním – Lab1"
---

# Sprievodca 2D tepelným spracovaním – Laboratórna práca č. 1

1.1. Úvod

1.2. Začatie riešenia novej úlohy

1.3. Nastavenia procesu

1.4. Definícia pojmov

1.5. Typ objektu obrobku

1.5.1. Definovanie údajov o obrobku

1.5.2. Import geometrie

1.5.3. Vytvorenie siete

1.5.4. Priradenie materiálu

1.5.5. Vytvorenie mriežky povlaku

1.5.6. Nastavenie okrajových podmienok

1.5.7. Inicializácia úrovní fáz obrobku

1.6. Definícia pojmu „stredný“

1.7. Definícia pojmu „plánovaný“

1.8. Ovládacie prvky simulácie

1.9. Vytvorenie databázy

1.10. Spustenie simulácie

1.11. Následné spracovanie

## Úvod

Sprievodca tepelným spracovaním je praktický nástroj na nastavenie zložitých úloh tepelných procesov pozostávajúcich z viacerých operácií. V tomto laboratórnom cvičení si ukážeme, ako pomocou tohto sprievodcu pripraviť simuláciu nauhličovania, kalenia a popúšťania oceľového dielu. Toto laboratórne cvičenie môže používateľom pomôcť pochopiť možnosti schémy výpočtu fázových prechodov v programe DEFORM-HT.

##  Vytvorenie novej úlohy

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main

Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obrázku [Fig. 2DHTWL1.1.](). Vyberte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek vyberte „**SI**“ pomocou prepínača. Názov úlohy zadajte ako „**QUENCH**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

Okno na výber typu problému

  
Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“, ako je znázornené na obr. 2DHTWL1.2. V tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a nadpis. V tomto laboratórnom cvičení použijeme ako názov projektu „**QUENCH**“. 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0002.jpg' | relative_url }})

Sprievodca MO – Nový projekt

Používateľ môže tiež zmeniť systém jednotiek (systém jednotiek vybraný v ponuke Súbor sa nastaví ako predvolený) a pridať operáciu HT tak, že ju vyberie z roletového zoznamu Prvá operácia a zaškrtne príslušné políčko (pozri obr. 2DHTWL1.3.). Pomocou možnosti Kopírovať existujúci projekt môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.  
  
Otvorí sa sprievodca viacerými operáciami. Zo zoznamu operácií v Průzkumníku pridajte operáciu „2D HT Wizard“. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „2D HT Wizard“ alebo ju môžete pridať aj pretiahnutím do Editoru operácií (pozri obr. 2DHTWL1.3..). 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0003.jpg' | relative_url }})

Pridanie sprievodcu 2D HT do editora operácií

## Nastavenia procesu

Po pridaní operácie sa otvorí stránka „Nastavenia procesu“, ako je znázornené na obr. 2DHTWL1.4. Používateľ môže nastaviť režim simulácie podľa požiadaviek simulácie spolu s ovládacími prvkami na definovanie krokov.

Zapnite možnosti „**Deformácia**“ a „**Fázová transformácia**“, keďže chceme počas procesu predpovedať zvyškové napätia a vypočítať fázové premeny. Definícia kroku sa nastaví na stránke „Ovládacie prvky simulácie“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (pozri obr. 2DHTWL1.4.). 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0004.jpg' | relative_url }})

Nastavenie parametrov procesu v sprievodcovi 2D HT

Otvorí sa stránka inicializácie, kde vidíme, že sú zaškrtnuté políčka „Fázová transformácia“ a „Deformácia“ (pozri obr. 2DHTWL1.5.). Nastavenia na stránke inicializácie ponecháme bez zmien a klikneme na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

  
  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0005.jpg' | relative_url }})

Okno nastavení inicializácie

## Definícia materiálu

V okne „Material“ načítajte materiál (JIS-S45C (tepelné spracovanie)) z knižnice materiálov DEFORM v kategórii „Steel“ pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 2DHTWL1.6, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v Průzkumníku. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka Obrobok. 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0006.jpg' | relative_url }})

Stránka „Import materiálu“

## Definovanie obrobku

### Definovanie údajov o obrobku

Na stránke „Workpiece“ (Obrobok) zmeňte typ objektu na **Elasto-plastic**, keďže potrebujeme predpovedať zvyškové napätia (pozri obr. 2DHTWL1.7.). Nastavte teplotu objektu na **900** °C. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0007.jpg' | relative_url }})

Definícia objektu obrobku

### Import geometrie

Na stránke Geometria kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (importovať geometriu z knižnice) a importujte súbor **QUENCH_PART.IGS** z inštalačnej cesty \SFTC\DEFORM\v*_*\2d\LABS, ako je znázornené na obr. 2DHTWL1.8. Pomocou akcie ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Pri správnej geometrii by sa mala zobraziť správa, ako je znázornené na obr. 2DHTWL1.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

  
  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0008.jpg' | relative_url }})

Import geometrie obrobku

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0009.jpg' | relative_url }})

Výstup kontroly importovanej geometrie

### Vytvoriť sieť

Na stránke „Mesh“ zadajte **Cieľový počet prvkov** ako **500** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Po dokončení generovania siete kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste obrobku priradili materiál. 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0010.jpg' | relative_url }})

Nastavenia siete a vygenerovaná sieť

### Priradenie materiálu

Vyberte a priraďte materiál **S45C-JAPAN**, ako je znázornené na obr. 2DHTWL1.11. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) vygenerujte sieť povlaku.

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0011.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Vytváranie mriežky povlaku

Prepnite do expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Budeme pridávať vrstvy povlaku, aby sme získali lepšie informácie o fázových premenách na povrchoch. Vyberte kartu „Coating“ a pridajte 2 vrstvy kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}). Nastavte hrúbku vrstvy 1 na 500 a vrstvy 2 na 1000, ako je znázornené na obr. 2DHTWL1.12., vyberte rovnaký materiál **S45C-JAPAN** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), aby ste prešli do režimu s navádzaním. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s okrajovými podmienkami.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0012.jpg' | relative_url }})

Nastavenia siete povrchovej úpravy použité pri generovaní siete obrobku

### Nastavenie okrajových podmienok

  1. Vyberte smer X a nastavte rýchlosť na 0, vyberte uzly pozdĺž osi tak, ako je znázornené na obr. 2DHTWL1.13, aby ste obmedzili rýchlosť uzlov v smere X, keďže ide o osovo symetrické usporiadanie.

  2. Vyberte smer Y a nastavte rýchlosť na 0, vyberte uzly pozdĺž spodnej plochy obrobku, ako je znázornené na obr. 2DHTWL1.13, aby ste obmedzili rýchlosť uzlov v smere Y obrobku počas kalenia.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0013.jpg' | relative_url }})

Priradenie rýchlosti BCC

### Inicializácia úrovní fáz obrobku

Keďže musíme vypočítať fázovú transformáciu, musíme nastaviť počiatočnú úroveň každej fázy; nezabudnite, že súčet všetkých fáz v každom prvku by mal byť rovný 1. Keďže teplota objektu je 900 °C a materiálom je oceľ, materiál by sa úplne premenil na austenitovú fázu, preto inicializujeme celý obrobok na austenitovú fázu. Na to kliknite na údaje prvku objektu ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) a v časti Mikrostruktúra vyberte kartu Fázová transformácia. Inicializujte austenit na hodnotu 1 a ostatné fázy na nulu výberom fázy a použitím ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) (pozri obr. 2DHTWL1.14.). V okne „Inicializovať údaje prvku“ priraďte hodnotu pomocou možnosti „Rozsah“ tak, že zadáte hodnotu 1, ako je znázornené na obr. 2DHTWL1.15, a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}), aby ste zatvorili okno „Inicializovať údaje prvkov“, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili dialógové okno „Údaje prvkov“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali podrobnosti o prostredí.

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0014.jpg' | relative_url }})

Inicializácia úrovne fázy v objekte „Element Data“

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0015.jpg' | relative_url }})

Okno na inicializáciu údajov prvkov

## Definícia pojmu „stredný“

Simulácia pozostáva z rýchleho ochladzovania; pre túto operáciu je potrebné definovať požadované médiá, v tomto prípade ide o vodu a vzduch. Na stránke „Podrobnosti o médiách“ definujete rôzne médiá a s nimi súvisiace zóny prenosu tepla, ako je znázornené na obr. 2DHTWL1.16.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0016.jpg' | relative_url }})

Okno „Podrobnosti o médiu“

  1. Premenujte prvé prostredie na „Air“ a nastavte koeficient prenosu tepla (HTC) a koeficient konvekcie v položke „Default“ na konštantu 0,05, ako je znázornené na obr. 2DHTWL1.16.

  2. Pridajte médium „Voda“. V prípade „štandardného“ modelu HTC načítajte údaje o konvekčnom koeficiente zo súboru „WATER_HTC1_si.DAT“.

  3. Pridajte ešte jednu zónu prenosu tepla pod médium „Voda“. Kliknutím na ohraničenie objektu určite počiatočný a koncový bod zóny. Zóna je priradená k spodnej časti obrobku, ako je znázornené na obr. 2DHTWL1.17. Pre zónu č. 1 HTC načítajte koeficient konvekcie zo súboru „WATER_HTC2_si.DAT“ a kliknite na funkciu „Definovať“, aby ste si prezreli údaje o funkcii, ako je znázornené na obr. 2DHTWL1.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali stránku plánu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0017.jpg' | relative_url }})

Okno so strednou úrovňou detailov zobrazujúce priradenie zón

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0018.jpg' | relative_url }})

Okno definície funkcie

## Definícia plánu

Na stránke „Plán“ zadajte päťstupňový plán kalenia, ako je znázornené na obr. 2DHTWL1.19, kliknutím na tlačidlo „Pridať“. Takýto postup sa niekedy označuje ako „intenzívne kalenie“, ktoré je navrhnuté tak, aby na diele vytvorilo veľmi tenkú „kôru“ martenzitu. Takýmto procesom je možné dosiahnuť vysokú povrchovú tvrdosť pri relatívne nízkom deformovaní dielu. 

1) 20 sekúnd (20 s) chladenie na vzduchu pri teplote 20 °C

2) 10 sekúnd (10 s) chladenie vo vode s teplotou 70 °C

3) 60 sekúnd (60 s) chladenie na vzduchu pri teplote 20 °C

4) 5 sekúnd (10 s) chladenie vo vode s teplotou 70 °C

5) 20 minút (1200 s) chladenie na vzduchu pri teplote 20 °C

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0019.jpg' | relative_url }})

Okno „Plán tepelného spracovania“

Nastavenia pre každú fázu je možné nastaviť alebo upraviť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define.._button.jpg' | relative_url }}) v stĺpci „Pokročilé“. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ovládacie prvky simulácie“.

## Ovládacie prvky simulácie

V časti „Definícia kroku“ vyberte prepínač „Auto“, nastavte hodnotu „Zmena teploty na krok“ na 5 °C a ostatné predvolené nastavenia ponechajte bez zmeny. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku generovania databázy. (Pozri obr. 2DHTWL1.20.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0020.jpg' | relative_url }})

Okno ovládacích prvkov simulácie

## Vytvoriť databázu

Kliknite na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) (pozri obr. 2DHTWL1.21.). Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0021.jpg' | relative_url }})

Okno na vytvorenie databázy

## Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DHTWL1.22. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0022.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie je možné počas jej vykonávania sledovať prostredníctvom okien „Simulation Message“ a „Process Monitor“ v režime simulácie. Kliknutím na kartu „Simulation Message“ zobrazíte súbor správ. Ak je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}), čo je predvolené nastavenie, súbor správ sa bude aktualizovať každých pár sekúnd.  
  
Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a poskytuje údaje o tom, ako dobre simulácia prebieha.  
Po ukončení simulácie sa správa pridá na koniec súboru správ. (Pozri obr. 2DHTWL1.23.)  
  
Každá definovaná fáza sa vykoná ako samostatná operácia a používateľ musí počkať, kým sa simulácia všetkých fáz dokončí.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0023.jpg' | relative_url }})

Karta „Simulačné správy“

## Následné spracovanie

Po ukončení simulácie kliknite na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky. Zobrazte stavovú premennú „Teplota“ a sledujte rozloženie teploty v rôznych fázach procesu kalenia (pozri obr. 2DHTWL1.24.). Zobrazte tiež objemový podiel jednotlivých fáz na konci procesu kalenia pomocou stavovej premennej „Objemový podiel“ v časti „Mikroštruktúra“ (pozri obr. 2DHTWL1.25.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0024.jpg' | relative_url }})

Rozloženie teploty v rôznych fázach procesu kalenia.

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0025.jpg' | relative_url }})

Objemový podiel jednotlivých fáz na konci procesu kalenia.
