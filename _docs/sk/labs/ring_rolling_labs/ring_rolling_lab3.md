---
lang: sk
title: "Laboratórium valcovania krúžkov3"
---

# Ring Rolling Lab3

V tomto laboratóriu nastavíme jednoduchú operáciu valcovania izotermického krúžku.

  
3.1. Vytvorenie nového problému

3.2. Stránka procesu

3.3. Nastavenie simulácie

3.4.Výber predmetu

3.5. Definovanie obrobku - krúžok

3.5.1. Definovanie obrobku - prstencový objekt

3.5.2. Definovanie obrobku - prsteň 2D prierez

3.5.3. Definovanie obrobku - prstencové 2D pletivo

3.5.4. Generovanie 3D geometrie pre obrobok - krúžok

3.5.5. Generovanie 3D pletiva pre obrobok - krúžok

3.5.6. Priradenie materiálu krúžku obrobku

3.6. Definovanie hnacieho valca

3.6.1. Definovanie predmetu hnacieho valca

3.6.2. 2D prierez hnacieho valca Strana

3.6.3. 3D geometrická stránka Driving Roll

3.6.4. Orientácia hnacieho valca

3.6.5. Pohyb hnacieho valca

3.7. Definovanie tlakového valca

3.7.1. Definovanie objektu tlakového valca

3.7.2. Tlakový valec 2D prierez Strana

3.7.3. Stránka 3D geometrie tlakového valca

3.7.4. Orientácia tlakového valca

3.7.5. Pohyb tlakového valca

3.8. Kontaktná stránka

3.9. Ovládacie prvky zastavenia

3.10. Ovládacie prvky Step a Remeshing Strana

3.11. Vytvoriť databázu

3.12. Simulácia chodu

3.13. Po spracovaní

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. RRL3.1. Pomocou prepínača vyberte prepínač „ * * Integrated Manufacturing Process * *“ a systém jednotiek ako „** English * * “. Definujte názov problému ako "**RING_ROLL_LAB3 ** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0001.jpg' | relative_url }})

Nový problém

V dialógovom okne Nový projekt sa otvorí sprievodca viacerými operáciami, v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**RING_ROLLING_LAB3 ** “. Operáciu 3D Ring Rolling je možné pridať v dialógovom okne "New Project" zapnutím First operation check band výberom operácie Ring Rolling z rozbaľovacej ponuky (pozri obr. RRL3.2.) V tomto laboratóriu pridáme operáciu valcovania krúžku zo zoznamu operácií prieskumníka, takže nezačiarknite políčko "Prvá operácia" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v pridávaní operácie.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0002.jpg' | relative_url }})

Pridanie operácie valcovania krúžku z nového projektu

  
Pridajte operáciu valcovania 3D prstenca zo zoznamu operácií prieskumníka. Pridajte operáciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré je k dispozícii vedľa položky **3D Ring Rolling * *, alebo ho môžete pridať aj presunutím myšou do editora operácií. Keď pridáme operáciu valcovania krúžku, predvolene sa otvorí stránka nastavení procesu (pozri obr. RRL3.3.).

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0003.jpg' | relative_url }})

Pridanie operácie valcovania krúžku z Prieskum

## Stránka procesu

Šablónu operácie valcovania krúžkov možno použiť na nastavenie valcovania krúžkov a valcovania kolies koľajníc, stránka V procese, v predvolenom nastavení sa vyberie prepínač ** "Valcovanie krúžkov (predvolené) * *" (pozri obr. RRL3.4.), tento výber predáme a klikneme na stránku nastavenia simulácie ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0004.jpg' | relative_url }})

Stránka procesu

## Nastavenie simulácie

Vyberte prepínač „* * Celý * * “ typu 3D modelu a ponechajte predvolený typ tepelného výpočtu ako „**C***** o * * konštantná teplota (izotermická)**“ na stránke nastavenia simulácie, ako je znázornené na obr. RRL3.5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Objekty.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0005.jpg' | relative_url }})

Stránka nastavenia simulácie

Object Selection

Na stránke „* * Objekty * * “ použijeme aktuálne predvolené objekty, ako je znázornené na obr. RRL3.6., na nastavenie procesu valcovania krúžku sú potrebné minimálne 3 objekty, sú to obrobok (krúžok), tlakový valec (tŕň) a hnací valec. V tomto laboratóriu nebudeme používať žiadny axiálny valec. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Obrobok - krúžok definujete objekt krúžku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0006.jpg' | relative_url }})

Zoznam objektov pre celý typ modelu

## Definovanie obrobku - krúžok

### Definovanie obrobku - prstencový objekt

Na stránke Obrobok - krúžok definujte teplotu objektu ako * * 70 * * ° F, ako je znázornené na obr. RRL3.7., kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 2D prierez.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0007.jpg' | relative_url }})

Obrobok - stránka Objekt krúžku

### Definovanie obrobku - prsteň 2D prierez

Na stránke prierezu 2D obrobku kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a vyberte**H* ***** ollo ** w** **valec** primitívny, definujte **vonkajší polomer** ako „**8** “, **vnútorný polomer** ako „6 “, **H****osem** ako „**2** “ a **rohy****polomer** ako**** 0,25 * * vo všetkých rohoch, ako je znázornené na obr. RRL3.8. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte primitívnu stránku Geometria a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 2D povrchovú sieť.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0008.jpg' | relative_url }})

Obrobok – definícia geometrie 2D prierezu krúžku

### Definovanie obrobku - prstencové 2D pletivo

V nastaveniach 2D povrchovej siete definujte cieľový počet prvkov ako **100** , kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a sledujte vygenerovanú povrchovú sieť v okne displeja (pozri obr. RRL3.9.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0009.jpg' | relative_url }})

Generovanie 2D sieťoviny obrobku - krúžok

### Generovanie 3D geometrie obrobku - krúžok

Na stránke 3D Geometria kliknite na možnosť „** Otočiť z 2D** “, použite predvolené hodnoty na stránke Otočiť z 2D, ako je znázornené na obr. RRL3.10., a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D povrchovú sieť.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0010.jpg' | relative_url }})

Nastavenia 3D geometrie krúžku obrobku

### Generovanie 3D sieťoviny pre obrobok - krúžok

Na stránke 3D povrchovej siete vyberte možnosť ** Otočiť s prepínačom s konštantným prierezom** a s predvolenou hodnotou **120** pre „**Počet otočných sekcií** “, vygenerujte 3D povrchovú sieť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Sledujte vygenerovanú 3D sieť pre obrobok, ako je znázornené na obr. RRL3.11. Ak má krúžok nerovnomerný tvar, používateľ môže importovať geometriu a vybrať položku Otočiť tak, aby sa prispôsobil 3D tvaru, aby sa vygenerovala nerovnomerná 3D krúžková sieť. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Materiál.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0011.jpg' | relative_url }})

Nastavenia 3D sieťoviny krúžku obrobku

### Priradiť materiál krúžku obrobku

Na stránke Materiál kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})(Načítať materiál z knižnice) a z okna knižnice materiálov načítajte materiál oceľovej skupiny „** AISI-1035,COLD[70-400F (20-200C)]** “. Priraďte materiál „**AISI-1035,COLD[70-400F(20-200C)]** “ pre obrobok, ako je znázornené na obr. RRL3.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku BCC obrobku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0012.jpg' | relative_url }})

Materiál obrobku a krúžku Strana

## Definovanie jazdného valca

### Definovanie objektu Driving Roll

Meno ponechajte ako „**Driving Roll** “ a teplotu ako**68°F * * nezmenenú, ako je znázornené na obr. RRL3.13. a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku geometrie prierezu 2D.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0013.jpg' | relative_url }})

Stránka objektu Driving Roll

### Prierez 2D riadiaceho valca Strana

Na stránke 2D prierezu jazdného valca kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a vyberte **H* **** o * * Llow valec **primitívny, definujte * * Vonkajší polomer * * ako „* * 19 * *“, * * Vnútorný polomer * * ako „* * 14 * *“ * * a * ** * výšku * * ako „* * 10 * * “, ako je znázornené na obr. RRL3.14. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte primitívnu stránku Geometria a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0014.jpg' | relative_url }})

Definovanie 2D prierezu hnacieho valca

### Driving Roll 3D Geometry Page

Na stránke 3D geometrie kliknite na možnosť „** Otočiť z 2D** “, ako je znázornené na obr. RRL3.15., použite predvolenú hodnotu * * 100 * * ako „**Počet vrstiev v smere obruče ** “ na stránke Otočiť z 2D, ako je znázornené na obr. RRL3.15.. a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) vygenerujete 3D geometriu, ako je znázornené na obr. RRL3.15.. a zatvorte. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientáciu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0015.jpg' | relative_url }})

Nastavenia 3D geometrie hnacieho valca

### Orientácia na šoférovanie

Na stránke orientácie Driving Roll zvoľte možnosť „**Nastavte relatívnu vzdialenosť medzi stredom objektu ** “ a definujte „ **Vertikálna vzdialenosť (d)* *“ ako ** 4 * * v s „* * Relatívna poloha stredu objektu * *“ ako „** -Z * * “, kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) posuniete Driving Roll o ** 2.25 * * pozdĺž osi * * Z * * vzhľadom na stred objektu Ring (pozri obr. RRL3.16.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Pohyb.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0016.jpg' | relative_url }})

Definovanie orientácie hnacieho valca

### Pohyb hnacieho valca

Vyberte **Uhlová rýchlosť** v ovládacích prvkoch rotačného pohybu pre hnací valec a definujte konštantnú hodnotu**2** rad/s. Všimnite si zelenú šípku otáčania zobrazujúcu smer otáčania v okne displeja (pozri obr. RRL3.17.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Objekt v tlakovom valci.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0017.jpg' | relative_url }})

Definícia pohybu hnacieho valca

## Definovanie tlakového valca

### Definovanie objektu tlakového valca

Ponechajte názov „* * Tlak * ***Valček** “ a teplotu * * 68°F * *, ako je znázornené na obr. RRL3.18. a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku prierezu 2D.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0018.jpg' | relative_url }})

Stránka objektu Pressure Roll

### 2D prierez valca tlaku Strana

Na stránke 2D prierezu tlakového valca kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a vyberte **valec** primitívne definujte * * R * ***** a * * dius **a **Height** ako **2** ” a **10** ”, ako je znázornené na obr. RRL3.19. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte primitívnu stránku Geometry a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D Geometry.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0019.jpg' | relative_url }})

Definovanie 2D geometrie prierezu valca tlaku

### Stránka 3D geometrie tlakového valca

Na stránke 3D geometrie kliknite na možnosť „** Otočiť z 2D** “, ako je znázornené na obr. RRL3.20., použite predvolenú hodnotu * * 100 * * pre "**Počet vrstiev v smere obruče ** " v Otočiť z 2D strany, ako je znázornené na obr. RRL3.20. a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) vygenerujete 3D geometriu pre tlakový valec, ako je znázornené na obr. RRL3.20. a zatvorte. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientáciu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0020.jpg' | relative_url }})

Nastavenia 3D geometrie tlakového valca

### Orientácia tlakového valca

Vyberte možnosť „**Nastaviť relatívnu vzdialenosť medzi stredmi objektov ** “ a definujte „ **Vertikálna vzdialenosť (d)** “ ako * * 4,5 * * v s „** Relatívna poloha stredu aktuálneho objektu ** “ ako „* * -Z * * “, kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) pre posunutie valca tlaku nadol pozdĺž osi ** Z * * o *4,5** v (pozri obr. RRL3.21.) na stránke Orientácia tlakového kotúča. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0021.jpg' | relative_url }})

Nastavenia orientácie tlakového valca

### Pohyb tlakového valca

Pohyb tlakového valca * * Otáčky ** definujeme ako „* * konštantný * * “ ako „* * 0,01 * * v/s“ pri zachovaní * * krútiaceho momentu * * na „**0 * * “, ako je znázornené na obr. RRL3.22. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Kontakt.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0022.jpg' | relative_url }})

Stránka pohybu tlakového valca

Kontakty

Na stránke Kontakt použijeme predvolenú hodnotu šmykového trenia * * 0,7 **, ako je znázornené na obr. RRL3.23. a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vytvoríte kontakty medzi hnacím valcom a obrobkom, ako aj medzi tlakovým valcom a obrobkom (pozri obr. RRL3.23.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Zastavenie ovládacích prvkov.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0023.jpg' | relative_url }})

stránka s kontaktnými informáciami

## Zastavenie ovládacích prvkov

Definujte **proces****trvanie** ako **10** s, ako je znázornené na obr. RRL3.24. Kliknite na ovládaciu stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step and remeshing.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0024.jpg' | relative_url }})

Zastavenie kontrolnej stránky

## Ovládacie prvky Step a Remeshing Strana

Ponechajte predvolené ***** z * * ** krokov * * z * * 10000 * *, nastavte * * Rotácia * * ** prírastok * * ** na * ** * uložiť * * ako * * 90 * * a * * Max * *** povolené * *** čas * ****krok** ako **0,01**. Ponechajte predvolené „**Ovládanieremeshingu* * “ ako „* * 5 * * otáčok“, ako je znázornené na obr. RRL3.25. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým nevytvoríte DB.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0025.jpg' | relative_url }})

Ovládacia stránka kroku a opätovného zostavenia

Všeobecné

Na stránke Generate DB kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) a vygenerujte databázu. Sledujte správu na karte Správa, ktorá informuje o stave generovania databázy.

## Simulácia behu

Po vygenerovaní databázy prepnite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. RRL3.26. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať z posledného kroku** “ (z kroku -1) a potom vyberte režim simulácie ako **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0026.jpg' | relative_url }})

Okno Spustiť simuláciu

  
Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces valcovania krúžku, keď simulácia pokračuje podľa zadaných kritérií zastavenia z grafiky simulácie.

Postprocessing

Po dokončení simulácie s „normálnym zastavením“ skontrolujte výsledky prepnutím do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov simulácie.
Prehrajte si kroky simulácie a pozrite sa, ako sa tvorí krúžok obrobku.
  
Kliknite na ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) Režim jedného objektu výberom obrobku-krúžok a vykreslenie efektívneho napätia obrobku-krúžok. Pri prehrávaní krokov môžeme pozorovať nárast hodnoty napätia. Efektívne rozloženie napätia v kroku 163 simulácie by malo vyzerať tak, ako je znázornené na obr. RRL3.27. Rozmer krúžku v poslednom kroku je znázornený na obr. RRL3.28.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0027.jpg' | relative_url }})

Preukázanie efektívneho stresu

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0028.jpg' | relative_url }})

Rozmery krúžku na konci simulácie
