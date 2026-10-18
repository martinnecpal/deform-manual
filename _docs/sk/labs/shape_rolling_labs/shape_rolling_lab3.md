---
lang: sk
title: "Laboratórium valcovania tvarov3"
---

# Tvarové valcovanie Lab3 (Lagrangián s použitím TET siete)

3.1. Vytvorenie nového problému

3.2. Operácia valcovania tvaru

3.3. Nastavenie procesných podmienok

3.4. Definujte obrobok

3.5. Definovanie drážok valcov

3.6. Definovanie nastavení roll passu v tabuľke Pass

3.7. Nastavenie 3D

3.8. Ovládacie prvky simulácie

3.9. Prevádzka Rolling Pass

3.10. Stojanový stôl

3.11. Definičné tabuľky

3.12. Objekt posunovača

3.13. Definovanie umiestnenia objektu

3.14. Definovanie kontaktných vzťahov

3.15. Stránka s ovládacími prvkami simulácie

3.16. Vytvoriť databázu

3.17. Simulácia chodu

3.18. Post Processing

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom * * Súbor * *******![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ** **Nový problém** alebo kliknutím na ikonu Nový problém. Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. L3.1. Pomocou prepínača vyberte prepínač „ * * Integrovaný výrobný proces * *“ a systém jednotiek ako „** SI * * “. Definujte názov problému ako „**SHR_LAG_LAB3 ** “ a uistite sa, že je zapnuté začiarkavacie políčko „** Zobraziť dialóg možností * *“ (ak nezapneme začiarkavacie políčko „Zobraziť dialóg možností“, nezobrazí sa dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0001.jpg' | relative_url }})

Okno výberu typu problému

  
Sprievodca viacnásobnou operáciou sa otvorí s dialógovým oknom Nový projekt, ako je znázornené na obr. L3.2., v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**SHR_LAG_LAB3 ** “. Operáciu 3D Shape Rolling je možné pridať aj v dialógu „New Project“ (pozri obr. L3.2.), v tomto laboratóriu pridáme operáciu valcovania tvaru zo zoznamu operácií prieskumníka, takže nezačiarknite políčko "Prvá operácia" a operáciu "Valcovanie tvaru" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0002.jpg' | relative_url }})

Otváracie okno sprievodcu MO v používateľskom rozhraní MO

## Operácia valcovania tvaru

Pridajte jednu operáciu valcovania tvaru zo zoznamu operácií prieskumníka. Operáciu možno pridať kliknutím na tlačidlo Operácia valcovania tvaru ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môže používateľ pridať aj presunutím myšou do editora operácií.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0003.jpg' | relative_url }})

Pridanie operácie valcovania tvaru

Procesné podmienky

Vyberte typ valcovania ako „**Lagrangeovský** “ a typ symetrie ako **Plný * *, pretože budeme nastavovať úplný objekt. Keďže nás zaujíma aj teplotný gradient v kotúčoch, vyberte možnosť „**Obrobok a kotúče (neizotermické)** “. Definujte hodnotu koeficientu trenia ako **0,7 * * a hodnotu koeficientu prestupu tepla ako **11 * *, ako je znázornené na obr. L3.4.

  
![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0004.jpg' | relative_url }})

Stránka procesu

## Definovať obrobok

V okne WP_CrossSection ponechajte typ objektu ako „**Plast**“ a zadajte teplotu obrobku ako **100** °C (pozri obr. L3.5.). Ďalšou možnosťou, ktorá je v tejto fáze k dispozícii, je „Importovať objekt“ z iného súboru kľúčových slov alebo databázy. Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0005.jpg' | relative_url }})

Definícia objektu obrobku

### Vytvoriť geometriu obrobku

Ak chcete vytvoriť obdĺžnikovú geometriu tyče pre obrobok, na stránke Geometria vyberte možnosť Definovať primitívne. Z okna primitívnej geometrie vyberte lištu a definujte parametre, ako je uvedené nižšie. Vytvorí sa obdĺžniková lišta, ako je znázornené na obr. L3.6.
**Východiskový bod** = (-50, -42,5)
**Šírka** Š = 100 mm
**Výška** H = 85 mm

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0006.jpg' | relative_url }})

Definícia geometrie obrobku v primitívnom okne Geometria

### Generovať pletivo obrobku

Vygenerujte povrchovú sieť obrobku s predvoleným počtom prvkov a nastavení.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0007.jpg' | relative_url }})

Generovanie pletiva obrobku

### Priradenie materiálu obrobku

Ak chcete priradiť materiál pre obrobok, vyberte materiál „**AISI****-1045** “ z okna materiálu. Dá sa to urobiť tak, ako je znázornené na obr. L3.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku zoznamu drážok.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0008.jpg' | relative_url }})

Priradenie materiálu pre obrobok

## Definovanie rolovacích drážok

Na stránke Groove List môžeme pridať drážky kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Kliknutím na „![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})“ raz pridáte jednu drážku, budeme používať rovnaký háj pre horný a spodný valec.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0009.jpg' | relative_url }})

Stránka zoznamu drážok

### Definovanie geometrie drážky 1

Vyberte prvú drážku a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Otvorí sa stránka Roll Groove Primitive, vyberte položku Flat rolls (Ploché kotúče). Pre valcovú geometriu definujte **šírku** ako **120** , **polomer**(r1) ako **5** a **valcový*** polomer * *** RR * * ako * * 100 * *, ako je znázornené na obr. L3.10.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0010.jpg' | relative_url }})

Definovanie geometrie drážky

## Definovanie nastavení roll passu v tabuľke Pass

V predvolenom nastavení môžeme pozorovať, ako sa Pass1 a First HT pridávajú do tabuľky Pass. Prvé nastavenia HT je potrebné definovať, ak simulujeme chladenie obrobku vzduchom pred prvým prechodom. V tomto laboratóriu budeme simulovať iba valivý priechod, preto definujeme nastavenia pre priechod 1.

Zapnite začiarkavacie políčko „Zobraziť všetky valce (pre asymetrické valcovanie)“.

V časti Pass1 vyberte položku Groove 1 zo zoznamu drážok pre horný aj dolný valec.

Definujte rýchlosť valenia (ot/min) ako 50, medzeru valenia (mm) ako 80 a teplotu valenia (C) ako 40. Ponechajte ostatné nastavenia ako predvolené a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku nastavenia 3D.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0011.jpg' | relative_url }})

Tabuľka preukazov

## Nastavenie 3D

Z DEFORMÁCIE v12 máme na stránke 3D Setup (Nastavenie 3D) možnosti Posúvač **objekt** pre Lagrangeovskú valcovaciu operáciu na stránke Stand table (Tabuľka podstavca). Teraz môžeme vytvoriť posunovač **objekt** pomocou možnosti Objekt alebo môžeme jednoducho priradiť * * Posunovač * *** BCC * * bez vytvorenia posunovacieho objektu, ako je znázornené na obr. L3.12.

  
**Objekt** : Keď vyberieme možnosť Objekt, vytvorí sa predvolená geometria objektu posunovača podobná prierezu obrobku a objekt posunovača sa pridá do zoznamu objektov.

**BCC** : Keď vyberieme možnosť BCC, pre posunovač obrobku sa BCC pridá na stránku BCC a stránka pohybu sa pridá pre obrobok na definovanie hodnoty pohybu rovnakej ako hodnota posunovača. V zozname objektov sa nepridá žiadny objekt posunovača.

**Žiadne** : Keď vyberieme možnosť Žiadne, objekt posunovača/BCC posunovača sa do operácie nepridá.

**Automatická poloha** : pri použití tejto možnosti bude obrobok umiestnený s horným valcom v smere pohybu a posunovač bude umiestnený s obrobkom v smere pohybu.

V tomto laboratóriu vyberte možnosť **Objekt * * pre **Posúvač**.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0012.jpg' | relative_url }})

Stránka nastavenia 3D

### Nastavenie geometrie 3D Roll

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) geometrie 3D valcov upravíte nastavenia generovania geometrie objektu 3D valcov, otvorí sa stránka nastavení geometrie 3D valcov. Na stránke nastavení geometrie 3D roliek definujte počet vrstiev ako 72 a vyberte „Generovanie jednotnej geometrie“. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno nastavení geometrie 3D rolls.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0013.jpg' | relative_url }})

Stránka nastavení 3D Roll Geometry

### Nastavenia 3D rolovacej siete

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) na povrchovej sieti 3D roliek upravíte nastavenia povrchovej siete rolky, otvorí sa okno povrchovej siete 3D rolky s nastaveniami pre povrchovú sieť 3D rolky. Definujte **počet otočných sekcií pre kotúče** ako **72** pomocou možnosti „**Uniform***mesh generation** “ a importujte materiál matrice „AISI-H-13“ z knižnice materiálov na priradenie k kotúčom, ako je znázornené na obr. L3.14. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vygenerujete povrchovú sieť pre kotúče s definovanými nastaveniami a materiálom. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno 3D rolovacej siete.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0014.jpg' | relative_url }})

Stránka nastavení povrchovej siete 3D Roll

### 3D nastavenie obrobku pomocou štvorstenného pletiva

V tomto laboratóriu použijeme pre obrobok tetraedrické pletivo. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) mriežky 3D obrobku, otvorí sa okno mriežky s nastaveniami mriežky 3D obrobku. Zvoľte užívateľské prepínacie tlačidlo pre Dĺžku obrobku a definujte dĺžku ako **600** mm, zvoľte prepínacie tlačidlo ** Tetrahedral ** ** mesh * *, definujte cieľový počet prvkov ako **20000** a pomer veľkosti ako **1** , ako je znázornené na obr. L3.15. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}) vygenerujete 3D povrchovú sieť obrobku. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno Mesh nastavenia povrchovej siete obrobku po vygenerovaní povrchovej siete.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0015.jpg' | relative_url }})

Stránka nastavení 3D povrchovej siete obrobku

  
  
Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button_2.jpg' | relative_url }}) na stránke 3D nastavenia a kliknite na tlačidlo „**Auto****pozícia** “, aby ste správne umiestnili posunovač, valce a obrobok, ako je znázornené na obrázku nižšie. L3.16. Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0016.jpg' | relative_url }})

Umiestnenie 3D objektov

## Ovládacie prvky simulácie

Prijmite predvolené nastavenia na stránke ovládacích prvkov simulácie.

Tu uložte projekt a vyberte operáciu Rolling Pass v editore operácií.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0017.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie

## Prevádzka valcovacej priepustky

V editore operácií vyberte operáciu Rolling Pass.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0018.jpg' | relative_url }})

Prevádzka Rolling Pass

## Stôl na stojan

Pri výbere operácie Rolling Pass sa zobrazí stránka stola Stand, ako je znázornené na obrázku [Fig. L3.18.]() V tomto laboratóriu budeme používať stoly na prednej a zadnej strane stojana, takže zapnite zaškrtávacie políčka **Table back** a * * Table ** *front**, ako je znázornené na obr. L3.19. Keď sa vygeneruje sieť a materiál je priradený k rolkám, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Tabuľka (Späť).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0019.jpg' | relative_url }})

Stránka tabuľky stojana

## Definovanie tabuliek

Musíme definovať stoly na prednej a zadnej strane valcového stojana. Stôl na zadnej strane sa nazýva **Stôl(zadný)** a stôl na prednej strane sa nazýva **Stôl(predný)**. Na stránke **Tabuľka(Späť)** potvrďte predvolenú teplotu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0020.jpg' | relative_url }})

Tabuľka (zadná) strana

### Definovanie geometrie tabuľky(zadnej)

Na stránke Geometria tabuľky(späť) vyberte položku „**Definovať primitívne“** a definujte parametre, ako je uvedené nižšie pre geometriu zadnej tabuľky.

**Východiskový bod** X= -50 mm

**Šírka** Š = 100 mm

**Výška** H = 5 mm

**Dĺžka** = 750

**Pass****Line** = 2,5 mm

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0021.jpg' | relative_url }})

Nastavenia geometrie pre tabuľku(späť)

### Generovanie sieťoviny pre stôl(späť)

Definujte počet vrstiev jednotnej hrúbky ako 5 a ostatné nastavenia ponechajte ako predvolené, ako je znázornené na obr. L3.22. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujete povrchovú sieť pre tabuľku.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0022.jpg' | relative_url }})

Nastavenia povrchovej siete pre stôl(späť)

### Priradenie materiálu k tabuľke(späť)

Ak chcete priradiť materiál pre tabuľku(späť), vyberte materiál „**AISI****-H-13** “ z okna materiálu. Dá sa to urobiť tak, ako je znázornené na obr. L3.23. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Tabuľka(predná strana).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0023.jpg' | relative_url }})

Priradenie materiálu k tabuľke(späť)

### Definičná tabuľka(predná strana)

Podobne ako pri tabuľke(zadná strana) definujte tabuľku(predná strana) s rovnakými nastaveniami pre geometriu, povrchovú sieť a materiál.

## Objekt posunovača

Objekt posunovača sa vytvorí automaticky pomocou rozmerov obrobku a na základe rýchlosti valenia sa priradí konštantná rýchlosť. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) skontrolujte vytvorenú geometriu a priradené ovládacie prvky pohybu.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0024.jpg' | relative_url }})

Stránka posunovača

### Geometria posunovača

Skontrolujte predvolenú geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), ako je znázornené na obr. L3.25. Kliknite na stránku pohybu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pusher.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0025.jpg' | relative_url }})

Definovanie geometrie posunovača

### Definovanie pohybu posunovača

Vyberte možnosť Rýchlosť. Rýchlosť posunovača by mala byť 50 až 60% relatívnej rýchlosti valcov, a preto by mala byť pre posunovač priradená konštantná rýchlosť * * 340 * * mm/s. (Pozri obr. L3.26.) Náhľad pohybu môžete vidieť kliknutím na možnosť „Náhľad pohybu“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) sa dostanete na stránku Umiestnenie objektu.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0026.jpg' | relative_url }})

Definovanie pohybu posunovača

## Definovanie umiestnenia objektu

Objekty sa automaticky umiestnia správne, keď klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}) na stránke nastavenia 3D a tabuľka(predná) a tabuľka(zadná) sa automaticky vytvoria na správnej pozícii, takže nie je potrebné polohu umiestniť.

Umiestnené predmety by sa mali objaviť tak, ako je znázornené na obr. L3.27.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0027.jpg' | relative_url }})

Poloha objektov

## Definovanie kontaktných vzťahov

Na stránke Contact relations sa automaticky pridajú vzťahy master-slave. Definujte **šmykové** trenie ako **0,7** a koeficient prestupu tepla rozhrania ako **11**(pozri obr. L3.28.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určíte inteligentnú toleranciu kontaktu a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujete kontakty medzi objektmi (prepnutím na model povrchovej záplaty zobrazíte kontakty vygenerované medzi objektmi). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0028.jpg' | relative_url }})

Nastavenia kontaktných vzťahov

## Stránka s ovládacími prvkami simulácie

Na stránke ovládacích prvkov simulácie nastavte Časové kroky ako * * 5000 * * pre túto simuláciu s krokom na uloženie ako **10** a Čas na krok ako **0,001** s. Pre kritériá zastavenia vyberte rovinu zastavenia a smer X (pozri obr. L3.29.). Kliknutím na voľnú koncovú hranu obrobku zastavíte ovládacie prvky zastavenia roviny (t.j. v smere +X) (pozri obr. L3.30.)

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0029.jpg' | relative_url }})

Definovanie počtu krokov a kritérií zastavenia

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0030.jpg' | relative_url }})

Údaje o rovine zastavenia (režim Expert)

Všeobecné

Vo fáze generovania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pristúpiť k generovaniu databázy (pozri obr. L3.31.). Pre prvú operáciu akýchkoľvek viacnásobných operácií je používateľ povinný vygenerovať databázu.

  
![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0031.jpg' | relative_url }})

Generovanie databázy

## Simulácia behu

Po vygenerovaní databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad operačným stromom. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. L3.32. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „* * Pokračovať ** * *z posledného kroku** “ a potom vyberte režim simulácie ako prepínač * * Interaktívne * *. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) pre spustenie simulácie.

Ak chcete definovať nastavenia MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}), okno Možnosti spustenia sa rozbalí a zobrazí možnosti definovania nastavení MPI pre simuláciu (maximálny počet procesorov, ktoré možno definovať v závislosti od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0032.jpg' | relative_url }})

Spustiť vyskakovacie okno simulácie

Postprocessing

V zozname krokov postprocesora nižšie sa v grafickej oblasti zobrazujú čísla krokov dostupné z rôznych simulovaných operácií. Na kontrolu odozvy modelu je možné použiť súbor premenných stavu, ktoré sú k dispozícii v ponuke „Post“.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0033.jpg' | relative_url }})

Sprievodca následným spracovaním

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0034.jpg' | relative_url }})

Kmeň Efektívny graf

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0035.jpg' | relative_url }})

Teplotný graf
