---
lang: sk
title: "Laboratórium valcovania tvarov1"
---

# Tvarové valcovanie Lab1(Lagrangian pomocou tehlovej siete)

  
1.1. Vytvorenie nového problému

1.2. Operácia valcovania tvaru

1.3. Nastavenie procesných podmienok

1.4. Definujte obrobok

1.5. Definovanie drážok

1.6. Priechodný stôl

1.7. Nastavenie 3D

1.8. Ovládacie prvky simulácie

1.9. Prevádzka Rolling Pass

1.10. Stojanový stôl

1.11. Zadná strana stola

1.12. Objekt posunovača

1.13. Definovanie umiestnenia objektu

1.14. Definovanie kontaktných vzťahov

1.15. Stránka s ovládacími prvkami simulácie

1.16. Generovať databázu

1.17. Simulácia chodu

1.18. Post Processing

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. L1.1. Pomocou prepínača vyberte prepínač „ * * Integrovaný výrobný proces * *“ a systém jednotiek ako „** SI * * “. Definujte názov problému ako „**Shape_Rolling_Lab1 ** “ a uistite sa, že je zapnuté začiarkavacie políčko „** Show option dialog * *“ (ak nezapneme začiarkavacie políčko „**Show option dialog * * “, nezobrazí sa dialógové okno New Project v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0001.jpg' | relative_url }})

Okno výberu typu problému

Sprievodca viacnásobnou operáciou sa otvorí s dialógovým oknom Nový projekt, ako je znázornené na obr. L1.2., v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Shape_Rolling_Lab1 ** “. Operáciu 3D Shape Rolling je možné pridať aj v dialógu „Nový projekt“ (pozri obr. L1.2.), v tomto laboratóriu pridáme operáciu valcovania tvaru zo zoznamu operácií prieskumníka, takže nezačiarknite políčko "Prvá operácia" a operáciu "Valcovanie tvaru" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0002.jpg' | relative_url }})

Otváracie okno sprievodcu MO v používateľskom rozhraní MO

## Operácia valcovania tvaru

Pridajte jednu operáciu valcovania tvaru zo zoznamu operácií prieskumníka. Operáciu možno pridať kliknutím na tlačidlo Operácia valcovania tvaru ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môže používateľ pridať aj presunutím myšou do editora operácií.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0003.jpg' | relative_url }})

Pridanie operácie valcovania tvaru

Procesné podmienky

Vyberte typ valcovania ako „**Lagrangeovský** “ a typ symetrie ako **Plný * *, pretože budeme nastavovať úplný objekt. Keďže nás zaujíma aj teplotný gradient v kotúčoch, vyberte možnosť „**Obrobok a kotúče (neizotermické)** “. Definujte hodnotu koeficientu trenia ako **0,7 * * a hodnotu koeficientu prestupu tepla ako **11 * *, ako je znázornené na obr. L1.4.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0004.jpg' | relative_url }})

Stránka procesu

## Definovať obrobok

V okne WP_CrossSection ponechajte typ objektu „**Plast**“ a zadajte teplotu obrobku 100 °C (pozri obr. L1.5.). Ďalšou možnosťou, ktorá je v tejto fáze k dispozícii, je „Importovať objekt“ z iného súboru kľúčových slov alebo databázy. Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0005.jpg' | relative_url }})

Definícia objektu obrobku

### Vytvoriť geometriu obrobku

Ak chcete vytvoriť obdĺžnikovú geometriu tyče pre obrobok, na stránke Geometria vyberte možnosť Definovať primitívne. Z okna primitívnej geometrie vyberte lištu a definujte parametre, ako je uvedené nižšie. Vytvorí sa obdĺžniková lišta, ako je znázornené na obr. L1.6.

**Východiskový bod** = (-50, -42,5)

**Šírka** Š = 100 mm

**Výška** H = 85 mm

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0006.jpg' | relative_url }})

Definovať primitívne

### Generovať pletivo obrobku

Vygenerujte povrchovú sieť obrobku s predvoleným počtom prvkov a nastavení.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0007.jpg' | relative_url }})

Generovanie pletiva obrobku

### Priradenie materiálu obrobku

Ak chcete priradiť materiál pre obrobok, vyberte materiál „AISI-1045“ z okna materiálu. Dá sa to urobiť tak, ako je znázornené na obr. L1.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku zoznamu drážok.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0008.jpg' | relative_url }})

Priradenie materiálu pre obrobok

## Definovanie drážok

Na stránke Groove List môžeme pridať drážky kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) raz pridáte jednu drážku, budeme používať rovnaký háj pre horný a spodný valec.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0009.jpg' | relative_url }})

Stránka zoznamu drážok

### Definovanie drážky1

Vyberte prvú drážku a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Otvorí sa stránka Roll Groove Primitive, vyberte položku Flat rolls (Ploché kotúče). Pre geometriu kotúča definujte šírku ako 120, polomer (r1) ako 5 a polomer kotúča RR ako 100, ako je znázornené na obr. L1.10.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0010.jpg' | relative_url }})

Definovanie geometrie drážky

## Tabuľka preukazov

V priechodnom stole priradíme geometrie drážok pre horný valec a spodný valec.

Zapnite začiarkavacie políčko „Zobraziť všetky valce (pre asymetrické valcovanie)“.

V časti Pass1 vyberte drážku 1 pre horný aj dolný valec v časti Pass 1.

Definujte rýchlosť valenia (ot/min) ako 50, medzeru valenia (mm) ako 80 a teplotu valenia (C) ako 40. Ostatné nastavenia ponechajte ako predvolené.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0011.jpg' | relative_url }})

Tabuľka preukazov

### 2,5d Valcovanie

V priechodnej tabuľke môže používateľ zobraziť náhľad procesu valcovania pomocou simulácie 2,5 D iba pre typ valcovania ale, takže pre toto laboratórium kliknite na stránku nastavenia ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku 3D.

## Nastavenie 3D

Z DEFORMÁCIE v12 máme na stránke 3D Setup (Nastavenie 3D) možnosti Posúvač **objekt** pre Lagrangeovskú valcovaciu operáciu na stránke Stand table (Tabuľka podstavca). Teraz môžeme vytvoriť objekt posunovača pomocou možnosti **Objekt** alebo môžeme jednoducho priradiť * * Posunovač * *** BCC * * bez vytvorenia objektu posunovača, ako je znázornené na obr. L1.12.

**Objekt** : Keď vyberieme možnosť Objekt, vytvorí sa predvolená geometria objektu posunovača podobná prierezu obrobku a objekt posunovača sa pridá do zoznamu objektov.

**BCC** : Keď vyberieme možnosť BCC, pre posunovač obrobku sa BCC pridá na stránku BCC a stránka pohybu sa pridá pre obrobok na definovanie hodnoty pohybu rovnakej ako hodnota posunovača. V zozname objektov sa nepridá žiadny objekt posunovača.

**Žiadne** : Keď vyberieme možnosť Žiadne, objekt posunovača/BCC posunovača sa do operácie nepridá.

**Automatická poloha:** pri použití tejto možnosti bude obrobok umiestnený s horným valcom v smere pohybu a posunovač bude umiestnený s obrobkom v smere pohybu.

V tomto laboratóriu vyberte možnosť **Objekt * * pre **Posúvač**.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0012.jpg' | relative_url }})

Stránka nastavenia 3D

### Nastavenie geometrie 3D Roll

Vyberte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) geometrie 3D Rolls. Otvorí sa stránka nastavení geometrie 3D Rolls, na stránke nastavení geometrie 3D Rolls definujte počet vrstiev ako 72 a vyberte „Generovanie jednotnej geometrie“. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno nastavení geometrie 3D rolls.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0013.jpg' | relative_url }})

Stránka nastavení 3D Roll Geometry

### Nastavenia 3D rolovacej siete

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) 3D rolovacej siete, otvorí sa okno 3D rolovacej siete s nastaveniami pre 3D rolovaciu sieť. Definujte **počet otočných profilov** pre kotúče ako **72** pomocou možnosti „**Uniform mesh generation** “ a importujte materiál matrice „* * AISI-H-13 * * “ z knižnice materiálov na priradenie k kotúčom, ako je znázornené na obr. L1.14\. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vygenerujete povrchovú sieť pre kotúče s definovanými nastaveniami a priradíte materiál. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno 3D rolovacej siete.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0038.jpg' | relative_url }})

Stránka nastavení povrchovej siete 3D Roll

### 3D nastavenie obrobku pomocou tehlovej siete

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) mriežky 3D obrobku, otvorí sa okno mriežky s nastaveniami mriežky 3D obrobku. Vyberte prepínač používateľa pre dĺžku obrobku a definujte dĺžku ako 600 mm, vyberte prepínač Birckovej siete a definujte počet vrstiev ako 120, ako je znázornené na obr. L1.15. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}) vygenerujete 3D povrchovú sieť obrobku. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno Mesh nastavenia povrchovej siete obrobku po vygenerovaní povrchovej siete.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0014.jpg' | relative_url }})

Stránka nastavení 3D povrchovej siete obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button_2.jpg' | relative_url }}) na stránke 3D nastavenia a kliknite na tlačidlo „Automatická poloha“, aby ste správne umiestnili posunovač, valce a obrobok, ako je znázornené na obrázku nižšie. L1.16. Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0015.jpg' | relative_url }})

Umiestnenie vygenerovaných objektov

## Ovládacie prvky simulácie

Prijmite predvolené nastavenia na stránke ovládacích prvkov simulácie.

Tu uložte projekt a vyberte operáciu Rolling Pass v editore operácií.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0016.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie

## Prevádzka valcovacej priepustky

V editore operácií vyberte operáciu Rolling Pass.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0017.jpg' | relative_url }})

Prevádzka Rolling Pass

## Stôl na stojan

Pri výbere stránky tabuľky operačného stojana Rolling Pass sa zobrazí, ako je znázornené na obrázku. V tomto laboratóriu musíme použiť zadnú a prednú časť stola, preto zapnite začiarkavacie políčko, ako je znázornené na obr. L1.19. Keďže sa vytvára povrchová sieť a materiál je priradený k valcom, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Tabuľka (späť)

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0018.jpg' | relative_url }})

Stránka tabuľky stojana

## Zadná strana stola

Na zadnej strane tabuľky potvrďte predvolenú teplotu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0022.jpg' | relative_url }})

Tabuľka (zadná) strana

### Definovanie zadnej geometrie stola

Na stránke geometrie zadnej strany tabuľky vyberte položku „Definovať primitívne“ a definujte parametre uvedené nižšie pre geometriu zadnej strany tabuľky.

**Východiskový bod** X= -50 mm

**Šírka** Š= 100 mm

**Výška** H= 5 mm

**Dĺžka** =750

**Pass****Line** = 2,5 mm

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0023.jpg' | relative_url }})

Vytvorenie geometrie zadnej tabuľky

### Stôl späť Mesh Generation

Definujte počet vrstiev jednotnej hrúbky ako 5 a ostatné nastavenia ponechajte ako predvolené, ako je znázornené na obr. L1.22. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujete povrchovú sieť pre tabuľku.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0024.jpg' | relative_url }})

Generovanie povrchovej siete zadnej tabuľky

### Priradenie materiálu spätného stola

Ak chcete priradiť materiál pre tabuľku späť, vyberte materiál „**AISI-H-13** “ z okna materiálu. Dá sa to urobiť tak, ako je znázornené na obr. L1.23. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po prednú stranu tabuľky.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0021.jpg' | relative_url }})

Priradenie materiálu hornej role

Podobne definujte prednú stranu stola ako zadnú stranu stola s rovnakými nastaveniami pre geometriu, povrchovú sieť a materiál.

## Objekt posunovača

Objekt posunovača sa vytvorí automaticky pomocou rozmerov obrobku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) skontrolujte vytvorenú geometriu a priradené ovládacie prvky pohybu.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0026.jpg' | relative_url }})

Stránka posunovača

### Geometria posunovača

Skontrolujte predvolenú geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), ako je znázornené na obr. L1.25. Kliknite na stránku pohybu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pusher.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0027.jpg' | relative_url }})

Definícia geometrie posunovača

### Definícia posunovacieho pohybu

Vyberte možnosť Rýchlosť. Rýchlosť posunovača by mala byť 50 až 60% relatívnej rýchlosti valcov, a preto by mala byť pre posunovač priradená konštantná rýchlosť 340 mm/s. (Pozri obr. L1.26.) Náhľad pohybu môžete vidieť kliknutím na možnosť „Náhľad pohybu“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) sa dostanete na stránku Umiestnenie objektu.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0028.jpg' | relative_url }})

Definovanie pohybu posunovača

## Definovanie umiestnenia objektu

Objekty sa automaticky umiestnia správne, keď klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}) na stránke 3D nastavenia a predná a zadná strana stola sa automaticky vytvoria na správnej pozícii, takže nie je potrebné ich umiestniť. Umiestnené predmety by sa mali objaviť tak, ako je znázornené na obr. L1.27.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0029.jpg' | relative_url }})

Poloha objektov

## Definovanie kontaktných vzťahov

Na stránke Contact relations sa automaticky pridajú vzťahy master-slave. Definujte šmykové trenie ako 0,7 a koeficient prestupu tepla rozhrania ako 11 (pozri obr. L1.28). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určíte inteligentnú toleranciu kontaktu a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujete kontakty medzi objektmi (prepnutím na model povrchovej záplaty zobrazíte kontakty vygenerované medzi objektmi). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0030.jpg' | relative_url }})

Generovanie kontaktných vzťahov

## Stránka s ovládacími prvkami simulácie

V ovládacích prvkoch simulácie nastavte stránku Časové kroky ako 5000 pre túto simuláciu s krokom na uloženie ako 10 a Čas na krok ako 0,001 s. Pre kritériá zastavenia vyberte rovinu zastavenia a smer X (pozri obr. L1.29.). Kliknutím na voľnú koncovú hranu obrobku zastavíte ovládacie prvky zastavenia roviny (t.j. v smere +X) (pozri obr. L1.30.)

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0031.jpg' | relative_url }})

Definovanie počtu krokov a kritérií zastavenia

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0032.jpg' | relative_url }})

Údaje o rovine zastavenia (režim Expert)

Všeobecné

Vo fáze generovania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pristúpiť k generovaniu databázy (pozri obr. L1.31.). Pre prvú operáciu akýchkoľvek viacnásobných operácií je používateľ povinný vygenerovať databázu.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0033.jpg' | relative_url }})

Generovanie databázy

## Simulácia behu

Po vygenerovaní databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad operačným stromom. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. L1.32. Použite predvolenú možnosť **Pokračovať*** * Spustiť * * a vyberte možnosť „**Pokračovať z posledného kroku** “ a potom vyberte režim simulácie ako prepínač * * Interaktívne * *. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) pre spustenie simulácie.

Ak chcete definovať nastavenia MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}), okno Možnosti spustenia sa rozbalí a zobrazí možnosti definovania nastavení MPI pre simuláciu (maximálny počet procesorov, ktoré možno definovať v závislosti od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0034.jpg' | relative_url }})

Spustiť vyskakovacie okno simulácie

Postprocessing

V zozname krokov postprocesora nižšie sa v grafickej oblasti zobrazujú čísla krokov dostupné z rôznych simulovaných operácií. Na kontrolu odozvy modelu je možné použiť súbor premenných stavu, ktoré sú k dispozícii v ponuke „Post“.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0035.jpg' | relative_url }})

Sprievodca následným spracovaním

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0037.jpg' | relative_url }})

Kmeň Efektívny graf

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0036.jpg' | relative_url }})

Teplotný graf
