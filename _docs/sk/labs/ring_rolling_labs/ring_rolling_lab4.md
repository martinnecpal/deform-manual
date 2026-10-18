---
lang: sk
title: "Krúžok valcovania Lab4"
---

# Ring Rolling Lab4

V tomto laboratóriu nastavíme jednoduchú operáciu valcovania krúžku.

4.1. Vytvorenie nového problému

4.2. Stránka procesu

4.3. Nastavenie simulácie

4.4. Výber objektu

4.5. Definovanie objektu krúžku obrobku

4.5.1 Definovanie nastavení objektu krúžku obrobku

4.5.2 Definovanie 2D prierezu krúžku obrobku

4.5.3 Generovanie 2D siete prierezu krúžku obrobku

4.5.4 Generovanie 3D geometrie krúžku obrobku

4.5.5 Generovanie 3D krúžku obrobku

4.5.6 Priradenie materiálu krúžku obrobku

4.6. Definovanie objektu hnacieho valca

4.6.1. Nastavenia predmetu hnacieho valca

4.6.2. Definovanie 2D prierezu hnacieho valca

4.6.3. Generovanie 3D geometrie hnacieho valca

4.6.4. Definovanie orientácie hnacieho valca

4.6.5. Definovanie pohybu hnacieho valca

4.7. Definovanie objektu tlakového valca

4.7.1. Definovanie objektu tlakového valca

4.7.2. Definovanie 2D prierezu valca tlaku Strana

4.7.3. Stránka Generovanie 3D geometrie tlakového kotúča

4.7.4. Definovanie orientácie tlakového valca

4.7.5. Definovanie pohybu tlakového valca

4.8. Kontaktná stránka

4.9. Definovanie ovládacích prvkov zastavenia

4.10. Definovanie krokov a prepracovanie ovládacích prvkov Strana

4.11. Vytvoriť databázu

4.12. Simulácia chodu

4.13. Post Processing

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Okno Nastavenie problému sa zobrazí, ako je znázornené na prepínači [Fig. RRL4.1.]() Select " * * Integrated Manufacturing Process * * " a Unit system ako "**English** " pomocou prepínača. Definujte názov problému ako "**RING_ROLL_LAB4 ** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0001.jpg' | relative_url }})

Vymedzenie problému

V dialógovom okne Nový projekt sa otvorí sprievodca viacerými operáciami, v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**RING_ROLLING_LAB4 ** “. Operáciu 3D Ring Rolling je možné pridať v dialógovom okne "New Project" zapnutím First operation check band výberom operácie Ring Rolling z rozbaľovacej ponuky (pozri obr. RRL4.2.) V tomto laboratóriu pridáme operáciu valcovania krúžku zo zoznamu operácií prieskumníka, takže nezačiarknite políčko "Prvá operácia" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v pridávaní operácie.

  
Pridajte operáciu valcovania 3D prstenca zo zoznamu operácií prieskumníka. Pridajte operáciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré je k dispozícii vedľa položky **3D Ring Rolling * *, alebo ho môžete pridať aj presunutím myšou do editora operácií. Keď pridáme operáciu valcovania krúžku, predvolene sa otvorí stránka Nastavenia procesu (pozri obr. RRL4.3).

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0002.jpg' | relative_url }})

Pridanie operácie valcovania krúžku z okna Nový projekt

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0003.jpg' | relative_url }})

Pridanie operácie valcovania krúžku z Prieskumníka

## Stránka procesu

Na stránke Proces sa predvolene vyberie prepínač „* * Valcovanie krúžku (predvolené) * * “ (pozri obr. RRL4.4.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na nastavenie simulácie.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0004.jpg' | relative_url }})

Stránka procesu

## Nastavenie simulácie

Vyberte prepínač „**Celá časť** “ typu 3D modelu a ponechajte predvolený typ tepelného výpočtu ako „**Konštantná teplota (izotermická)** “ na stránke nastavenia simulácie, ako je znázornené na obr. RRL4.5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Objekty.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0005.jpg' | relative_url }})

Nastavenia simulačného modelu na stránke Nastavenia simulácie

Object Selection

Na stránke „* * Objekty * * “ použijeme aktuálne predvolené objekty, ako je znázornené na obr. RRL4.6. Na nastavenie jednoduchej operácie valcovania krúžku sú potrebné minimálne 3 predmety obrobku (krúžok), tlakový valec (tŕň) a hnací valec. V tomto laboratóriu nebudeme používať žiadny axiálny valec. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Obrobok - krúžok definujete objekt krúžku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0006.jpg' | relative_url }})

Objekty pre nastavenie simulácie valcovania krúžku

## Definovanie krúžkového objektu obrobku

### Definovanie nastavení objektu krúžku obrobku

Na stránke Obrobok-krúžok definujte * * Objekt * *** teplotu * * ako * * 70 * * ° F, ako je znázornené na obr. RRL4.7., Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 2D prierez.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0007.jpg' | relative_url }})

Obrobok - Nastavenie prstencového objektu

### Definovanie 2D prierezu krúžku obrobku

Ak chcete definovať počiatočný tvar krúžku, kliknite na odkaz ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) na stránke 2D prierezu obrobku a vyberte * * H ** * * primitívny, definujte * * vonkajší polomer ** ako „* * 8 **“, * * vnútorný polomer * * ako „* * 6 * * “, * * H * *** osem * * ako „**2* *****“ a****a**rohy****polomer** ako**"**0,25"** vo všetkých rohoch, ako je znázornené na obr. RRL4.8. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte primitívnu stránku Geometria a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 2D povrchovú sieť.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0008.jpg' | relative_url }})

Obrobok – Nastavenie geometrie 2D prierezu krúžku

### Generovanie 2D siete prierezu obrobku

Ak chcete vygenerovať povrchovú sieť pre 2D prierez, v nastaveniach 2D povrchovej siete definujte **Cieľový počet prvkov** ako * *100 * * a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a pozorujte vygenerovanú povrchovú sieť v okne displeja (pozri obr. RRL4.9.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0009.jpg' | relative_url }})

Nastavenia 2D povrchovej siete obrobku

### Generovanie 3D geometrie krúžku obrobku

Na stránke 3D Geometry kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_revolve_from_2d_label.jpg' | relative_url }}), použite predvolené hodnoty v Revolve from 2D page a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie (pozri obr. RRL4.10.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D povrchovú sieť.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0010.jpg' | relative_url }})

Geometria a nastavenia 3D obrobku

### Generovanie 3D krúžku obrobku

Na stránke 3D povrchová sieť s predvolenou hodnotou **200** pre „**Počet otočných sekcií** “ vytvorte 3D povrchovú sieť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Sledujte vygenerovanú 3D sieť pre obrobok, ako je znázornené na obr. RRL4.11. Ak má krúžok nerovnomerný tvar, používateľ môže importovať geometriu a vybrať položku Otočiť tak, aby sa prispôsobil 3D tvaru, aby sa vygenerovala nerovnomerná 3D krúžková sieť. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Materiál.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0011.jpg' | relative_url }})

Nastavenia 3D siete krúžku obrobku a vygenerovanej siete

###  Priradiť materiál krúžku obrobku

Na stránke Materiál kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a načítajte * * oceľ * * skupinový materiál "**AISI-1035,COLD[70-400F (20-200C)]** " z okna knižnice materiálov. Priraďte materiál „**AISI-1035,COLD[70-400F(20-200C)]** “ pre obrobok, ako je znázornené na obr. RRL4.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až do stránky objektu Driving Roll.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0012.jpg' | relative_url }})

Definícia materiálu obrobku a krúžku

## Definovanie objektu Driving Roll

### Nastavenia objektu hnacieho valca

Meno „* * Driving ** * ***** Roll ** “ ponechajte nezmenené a teplotu * * 68 ** ° F, ako je znázornené na obr. RRL4.13., kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku geometrie prierezu 2D.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0013.jpg' | relative_url }})

Nastavenia objektu Driving Roll

### Definovanie 2D prierezu hnacieho valca

Na stránke 2D prierezu jazdy kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a vyberte * * Dutý * * ** valec * * primitívny, definujte * * Vonkajší polomer * * ako „* * 19 **“, * * Vnútorný polomer * * ako „* * 14 * *“ a * * H * *** osem * * ako „* * 10 * * “, ako je znázornené na obr. RRL4.14. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte primitívnu stránku Geometria a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0014.jpg' | relative_url }})

Definícia 2D prierezu hnacieho valca

### Generovanie 3D geometrie jazdného valca

Na stránke 3D Geometria kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_revolve_from_2d_label.jpg' | relative_url }}), použite predvolenú hodnotu **100** pre „**Počet vrstiev v smere obruče ** “ na stránke Otočiť z 2D (pozri obr. RRL4.15.) a zatvorte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Orientation.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0015.jpg' | relative_url }})

3D geometria a nastavenia hnacieho valca

### Definovanie orientácie jazdného valca

Na stránke orientácie Driving Roll zvoľte možnosť „**Nastavte relatívnu vzdialenosť medzi stredom objektu ** “ a definujte „**Vertikálna vzdialenosť (d)** “ ako * * 4 * * v a „Relatívna poloha stredu objektu ako „**-Z** “ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}), aby ste posunuli Driving Roll o ** 2.25 * * pozdĺž osi Z vzhľadom na stred objektu Ring (pozri obr. RRL4.16.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Pohyb.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0016.jpg' | relative_url }})

Nastavenia orientácie jazdného valca

### Definovanie pohybu hnacieho valca

Vyberte **Uhlová rýchlosť** v ovládacích prvkoch rotačného pohybu pre hnací valec a definujte konštantnú hodnotu **2** rad/s. Všimnite si zelenú šípku otáčania zobrazujúcu smer otáčania v okne displeja (pozri obr. RRL4.17.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Objekt v tlakovom valci.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0017.jpg' | relative_url }})

Ovládacie prvky pohybu hnacieho valca

## Definovanie objektu tlakového valca

### Definovanie objektu tlakového valca

Ponechajte názov „* * Tlakový valec * * “ a teplotu ako * * 68 * * ° * * F * *, ako je znázornené na obr. RRL4.18. a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku prierezu 2D.

  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0018.jpg' | relative_url }})

Stránka objektu Pressure Roll

### Definovanie 2D prierezu valca tlaku Strana

Na stránke Pressure Roll 2D Geometry kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a definujte údaje súradníc, ako je znázornené nižšie v tabuľke a na obr. RRL4.19. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

**X** |  **Y** |  **R**
---|---|---
0 |  0 |  0
2 0
2 (4,5 %)
2,25 |  4,75 |  0,25
2,25 |  5,25 |  0,25
2 |  5,5 |  0
2/ 10
0-10
0 |  0 |  0
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0020.jpg' | relative_url }})

Definícia geometrie valca tlaku

### Stránka Generovanie 3D geometrie tlakového kotúča

Na stránke 3D Geometria kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_revolve_from_2d_label.jpg' | relative_url }}), Použite predvolenú hodnotu **100** pre „**Počet vrstiev v smere obruče ** “ na stránke Otočiť z 2D (pozri obr. RRL4.20.) a zatvorte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Orientation.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0021.jpg' | relative_url }})

3D geometria a nastavenia tlakového valca

### Definovanie orientácie tlakového valca

Vyberte možnosť „**Nastaviť relatívnu vzdialenosť medzi stredmi objektov ** “ a definujte „ **Vertikálna vzdialenosť (d)* *“ ako * * 4 * * v a „* * Relatívna poloha stredu aktuálneho objektu ** “ ako „** -Z * * “, kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) posuniete rolovanie tlaku nadol pozdĺž osi ** Z * * o *4,5** v (pozri obr. RRL4.21.) na stránke Orientácia tlakového kotúča. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0022.jpg' | relative_url }})

Nastavenia orientácie tlakového valca

### Definovanie pohybu tlakového valca

Pohyb tlakového valca definujeme ako „konštantný“ „* * rýchlosť * * “ „* * 0,01 * * v/s“, ako je znázornené na obr. RRL4.22. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Kontakt.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0023.jpg' | relative_url }})

Ovládacie prvky pohybu tlakového valca

Kontakty

Na stránke Kontakt použite predvolenú hodnotu šmykového trenia **0,7** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vytvorte kontakty medzi hnacím valcom a obrobkom, ako aj medzi tlakovým valcom a obrobkom (pozri obr. RRL4.23.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Zastavenie ovládacích prvkov.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0024.jpg' | relative_url }})

Nastavenia vzťahu medzi objektmi

## Definovanie ovládacích prvkov zastavenia

Definujte **proces****trvanie** ako **10** s, ako je znázornené na obr. RRL4.24. Kliknite na ovládaciu stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step and remeshing.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0025.jpg' | relative_url }})

Ovládacie prvky zastavenia

## Definovanie krokov a prepracovanie ovládacích prvkov Strana

Ponechajte **Počet krokov** ako **10000** a definujte prírastok **Rotácie** na uloženie ako **90** a maximálny povolený časový krok ako 0,01. Ponechajte „Remeshing control“ ako „5 otáčok“, ako je znázornené na obr. RRL4.25. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým nevytvoríte DB.

  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0026.jpg' | relative_url }})

Ovládacie prvky kroku a úpravy

Všeobecné

Na stránke Generate DB kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) a vygenerujte databázu. Sledujte správu na karte Správa, ktorá informuje o stave generovania databázy.

## Simulácia behu

Po vygenerovaní databázy prepnite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. RRL4.26. Pomocou predvolenej možnosti **Pokračovať v spustení * * vyberte možnosť „**Pokračovať z posledného kroku** “ a potom vyberte režim simulácie ako **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0027.jpg' | relative_url }})

Spustiť nastavenia simulácie

  
Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulačná správa a Simulačný protokol, uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces valcovania krúžku, keď simulácia pokračuje podľa zadaných kritérií zastavenia z grafiky simulácie.

Postprocessing

Po dokončení simulácie s „normálnym zastavením“ skontrolujte výsledky prepnutím do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov simulácie.
Prehrajte si kroky simulácie a pozrite sa, ako sa tvorí krúžok obrobku.
  
Kliknite na ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) Režim jedného objektu výberom krúžku obrobku a vykreslením efektívneho namáhania krúžku obrobku. Pri prehrávaní krokov môžeme pozorovať nárast hodnoty napätia. Hodnota efektívneho napätia na konci simulácie by mala vyzerať tak, ako je znázornené na obr. RRL4.27.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0028.jpg' | relative_url }})

Efektívne namáhanie na konci simulácie
