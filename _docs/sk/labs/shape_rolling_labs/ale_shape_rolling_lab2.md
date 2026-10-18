---
lang: sk
title: "Ale Shape Rolling Lab2"
---

# ale Shape Rolling Lab2 (pomocou booleovskej siete)

  
2.1. Vytvorenie nového problému

2.2. Operácia valcovania tvaru

2.3. Nastavenie procesných podmienok

2.4. Definujte obrobok

2.5. Definovanie drážok

2.6. Priechodný stôl

2.7. Nastavenie 3D

2.8. Prevádzka Rolling Pass

2.9. Stojanový stôl

2.10. Definovanie kontaktných vzťahov

2.11. Ovládacie prvky simulácie

2.12. Vytvoriť databázu

2.13. Simulácia chodu

2.14. Post Processing

##  Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. ALEL2.1. Pomocou prepínača vyberte prepínač „ * * Integrovaný výrobný proces * *“ a systém jednotiek ako „** SI * * “. Definujte názov problému ako názov ako "**MO_ale_LAB2 ** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "Zobraziť dialóg možností", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0001.jpg' | relative_url }})

Okno výberu typu problému

Sprievodca viacerými operáciami sa otvorí s dialógovým oknom Nový projekt, ako je znázornené na (pozri obr. ALEL2.2.), v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**MO_ale_LAB2 ** “. Operáciu 3D Shape Rolling je možné pridať aj v dialógu „New Project“ (pozri obr. ALEL2.2.), v tomto laboratóriu pridáme operáciu valcovania tvaru zo zoznamu operácií prieskumníka, takže nezačiarknite políčko "Prvá operácia" a operáciu "Valcovanie tvaru" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

## Operácia valcovania tvaru

Pridajte jednu operáciu valcovania tvaru zo zoznamu operácií prieskumníka. Operáciu možno pridať kliknutím na tlačidlo Operácia valcovania tvaru ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môže používateľ pridať aj presunutím myšou do editora operácií (pozri obr. ALEL2.3.)).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0002.jpg' | relative_url }})

Sprievodca MO s novým otváracím oknom projektu

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0003.jpg' | relative_url }})

Pridanie operácie valcovania tvaru z prieskumníka

Procesné podmienky

Vyberte typ valcovania ako "Steady-State ale" a typ symetrie ako "Full", pretože budeme nastavovať kompletný objekt. Keďže nás teplotný gradient v kotúčoch nezaujíma, vyberte možnosť „** Len obrobok (neizotermický)** “. Definujte hodnotu koeficientu trenia ako **0,7 * * a hodnotu koeficientu prestupu tepla ako **11 * *, ako je znázornené na obr. ALEL2.4. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na WP_CrossSection.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0004.jpg' | relative_url }})

Stránka procesu

## Definovať obrobok

Na stránke WP_CrossSection ponechajte typ objektu ako „Plast“ a zadajte teplotu obrobku 100 °C (pozri obr. ALEL2.5.). Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0005.jpg' | relative_url }})

Definícia objektu obrobku

### Vytvoriť geometriu obrobku

Ak chcete vytvoriť obdĺžnikovú geometriu tyče pre obrobok, na stránke Geometria vyberte položku ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Z okna primitívnej geometrie vyberte **Bar** a definujte parametre

Východiskový bod = (-50, -42,5), šírka W = 100 mm a výška H = 85 mm a zatvorte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Vytvorí sa obdĺžniková lišta, ako je znázornené na obr. ALEL2.6. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0006.jpg' | relative_url }})

Definovať primitívne

### Generovať pletivo obrobku

Vygenerujte povrchovú sieť obrobku s predvoleným počtom prvkov a nastavení (pozri obr. ALEL2.7.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0007.jpg' | relative_url }})

Generovanie pletiva obrobku

### Priradenie materiálu obrobku

Ak chcete priradiť materiál pre obrobok, vyberte materiál „AISI-1045“ z okna materiálu. Dá sa to urobiť tak, ako je znázornené na obr. ALEL2.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku zoznamu drážok.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0008.jpg' | relative_url }})

Priradenie materiálu pre obrobok

## Definovanie drážok

Na stránke Groove List môžeme pridať drážky kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Jedným kliknutím na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte jednu drážku (pozri obr. ALEL2.9.), použijeme rovnakú drážku pre horný a dolný valec.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0009.jpg' | relative_url }})

Stránka zoznamu drážok

### Definovanie drážky1

Vyberte prvú drážku a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), otvorí sa stránka Roll Groove Primitive, vyberte Flat rolls. Pre geometriu kotúča definujte šírku (W) ako 120, polomer (r1) ako 5 a polomer kotúča (RR) ako 100 (pozri obr. ALEL2.10.). Kliknutím ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pass.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0010.jpg' | relative_url }})

Definovanie geometrie drážky

## Tabuľka preukazov

V priechodnom stole priradíme geometrie drážok pre horný valec.

V časti Pass1 vyberte možnosť Groove 1 for Top roll, systém skopíruje geometriu horného valca pre spodný valec spodného valca, ak nie je začiarknuté políčko asymetrického valcovania.

Definujte rýchlosť valenia (ot/min) ako 50, medzeru valenia (mm) ako 80 a teplotu prostredia ako 20° C. Ostatné nastavenia ponechajte ako predvolené. Použite predvolený počet sekcií ako 20. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) nastavíte 3D objekty pre obrobok a valce.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0011.jpg' | relative_url }})

Tabuľka preukazov

## Nastavenie 3D

Nastavenia geometrie a povrchovej siete 3D Rolls a obrobku sú k dispozícii na tejto stránke na nastavenie 3D modelov. (Pozri obr. ALEL2.12.).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0013.jpg' | relative_url }})

Stránka nastavenia 3D

### Nastavenie geometrie 3D roliek

Vyberte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) geometrie 3D valcov, otvorí sa okno nastavení geometrie 3D valcov. V okne nastavení geometrie 3D valcov definujte počet vrstiev pre valce ako 72 a vyberte možnosť „Jemnejšia geometria od“, ako je znázornené na obr. ALEL2.13. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vygenerujete kotúče s novými nastaveniami. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno nastavení geometrie 3D rolls.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0012.jpg' | relative_url }})

Stránka nastavení 3D Roll Geometry

### Nastavenie 3D obrobku pomocou metódy Boolean mesh

V tomto laboratóriu budeme používať booleovskú metódu na generovanie 3D siete pre obrobok, materiál z obrobku na priesečníku valca a obrobku bude odstránený.

Vyberte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) 3D obrobku, otvorí sa okno nastavení povrchovej siete 3D obrobku. Vyberte prepínač používateľa pre dĺžku obrobku a definujte dĺžku ako 100 mm, vyberte metódu povrchovej siete ako Boolean, definujte počet vrstiev ako 36 a vyberte jemnejšiu povrchovú sieť od 0,333 do 0,6667. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno nastavení povrchovej siete obrobku. Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0014.jpg' | relative_url }})

Stránka nastavení 3D povrchovej siete obrobku

Teraz uložte projekt a vyberte operáciu Rolling Pass v editore operácií.

## Prevádzka valcovacej priepustky

V editore operácií vyberte operáciu Rolling Pass.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0015.jpg' | relative_url }})

Prevádzka Rolling Pass

## Stôl na stojan

Pri výbere stránky tabuľky operačného stojana Rolling Pass sa zobrazí, ako je znázornené na obrázku. V tomto laboratóriu nebudeme používať tabuľky a udržiavať teplotu 20° C pre kotúče. Takže kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Kontakt.

## Definovanie kontaktných vzťahov

Na stránke Contact relations sa automaticky pridajú vzťahy master-slave. Definujte šmykové trenie ako 0,7 a koeficient prestupu tepla rozhrania ako 11 (pozri obr. ALEL2.16.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určíte inteligentnú toleranciu kontaktu a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vytvoríte kontakty medzi objektmi. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0016.jpg' | relative_url }})

Generovanie kontaktných vzťahov

## Ovládacie prvky simulácie

V ovládacích prvkoch simulácie nastavte stránku Časové kroky ako 5000 pre túto simuláciu s krokom na uloženie ako 10 a Čas na krok ako 0,001 s. Z DEFORMÁCIE v12 bola v krokových ovládacích prvkoch pridaná možnosť zastavenia konvergencie ale v ustálenom stave, používateľ môže definovať kritériá zastavenia ale v ustálenom stave pre valcovaciu prevádzku ale. V tomto laboratóriu použijeme predvolené hodnoty, ako je znázornené na obr. ALEL2.17. , kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre vygenerovanie DB.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0017.jpg' | relative_url }})

Ovládacie prvky simulácie

Všeobecné

Vo fáze generovania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pristúpiť k generovaniu databázy (pozri obr. ALEL2.18.).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0018.jpg' | relative_url }})

Generovanie databázy

## Simulácia behu

Po vygenerovaní databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad operačným stromom. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. ALEL2.19. Použite predvolenú možnosť **Pokračovať*** * Spustiť * * a vyberte možnosť „**Pokračovať z posledného kroku** “ (z kroku -1) a potom vyberte režim simulácie ako prepínač * * Interaktívne * *. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) pre spustenie simulácie.

Ak chcete definovať nastavenia MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}), okno Možnosti spustenia sa rozbalí a zobrazí možnosti definovania nastavení MPI pre simuláciu (maximálny počet procesorov, ktoré možno definovať v závislosti od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0019.jpg' | relative_url }})

Dialógové okno Spustiť možnosť

Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces, ako simulácia prebieha z grafiky simulácie

Simulácia sa zastaví po dosiahnutí stabilného stavu s nižšie uvedenou správou v súbore správy.

" PROGRAM ZASTAVENÝ!

AKTUÁLNY VALIVÝ PRIECHOD DOSIAHOL PODMIENKY USTÁLENÉHO STAVU “

Postprocessing

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), otvorí sa postprocesor MO (pozri obr. ALEL2.20.).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0020.jpg' | relative_url }})

Režim MO Post

Prejdite na posledný krok, Plot Strain - Effective a Stress Max principal state available a sledujte rozdelenie stavových premenných (pozri obr. ALEL2.21. a obr. ALEL2.22. ).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0021.jpg' | relative_url }})

Kmeň - efektívny graf

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0022.jpg' | relative_url }})

Stress Max Principal Plot
