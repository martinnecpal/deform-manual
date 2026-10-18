---
lang: sk
title: "Spinning Lab"
---

# Spinning Lab

V tomto laboratóriu nastavíme jednoduchý proces odstreďovania s modelom ale a implicitným riešiteľom

  
1.1. Vytvorenie nového problému

1.2. Stránka procesu

1.3. Nastavenie simulácie

1.4. Predmety

1.5. Obrobok

1.6. Vreteno

1.7. Koniec

1.8. Roll

1.9. Priechodný stôl

1.10. Ovládacie prvky

1.11. Kontakt

1.12. Ovládacie prvky zastavenia

1.13. Ovládacie prvky simulácie

1.14. Generovať databázu

1.15. Simulácia chodu

1.16. Po spracovaní

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DSPL1.1. Pomocou prepínača vyberte prepínač „ * * Integrovaný výrobný proces * *“ a systém jednotiek ako „** SI * * “. Definujte názov problému ako "** SpinLab * * " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Nový problém

Sprievodca viacerými operáciami sa otvorí v dialógovom okne Nový projekt. V tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „SpinLab“. Operáciu 3D Spinning je možné pridať aj v dialógovom okne "Nový projekt", v tomto laboratóriu pridáme operáciu Spinning g zo zoznamu operácií Prieskumníka, takže nezačiarknite políčko "Prvá operácia" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pokračujte v otvorení operácie.

Pridajte operáciu 3D Spinning zo zoznamu Explorer Operations (Operácie prieskumníka). Pridajte operáciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré je k dispozícii vedľa 3D Spinning, alebo ho môžete pridať aj presunutím myšou do editora operácií (pozri obr. 3DSPL1.2). Keď pridáme operáciu odstreďovania, ak je aktuálny smer obrazovky smerom nahor smer "Z", dostaneme sa pod vyskakovacie okno. V kontextovom okne „Change screen upward axis“ (Zmeniť obrazovku smerom nahor) kliknite na „** YES-Change * *“ (Zmeniť).

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0002.jpg' | relative_url }})

Zobrazenie vyskakovacieho okna smeru nahor

Teraz sa predvolene otvorí okno nastavení procesu. Operáciu 3D Spinning je možné pridať aj z Prieskumníka operácií v MO.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0003.jpg' | relative_url }})

Otvorená operácia 3D odstreďovania

## Stránka procesu

Na stránke Proces vyberte "**Spinning** " a definujte rýchlosť vretena * * Rotational ** * * ako * * 90 * * rpm, ako je znázornené na obr. 3DSPL1.4. Táto rýchlosť sa vzťahuje aj na chvostovú aj hlavovú pažbu, ak sme ju použili. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku nastavenia simulácie.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0004.jpg' | relative_url }})

Stránka procesu

## Nastavenie simulácie

V nastavení simulácie vyberte metódu riešenia ako „** ale ** “ a typ riešiteľa ako „**Implicitný** “. Keďže nás teplotný profil nezaujíma, vyberieme typ „**Konštantná teplota (izotermická)** “ Tepelný výpočet a políčko Zapnúť **Aktívne v FEM** aktivujeme výpočet cieľového objemu (pozri obr. 3DSPL1.5.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na objekty.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0005.jpg' | relative_url }})

Stránka nastavenia simulácie

Predmety podnikania

V tomto spriadacom laboratóriu použijeme obrobok, tŕň, chvost a jednu rolku. V zozname objektov sa predvolene začiarkne políčko Mandrel, Tail stock a Head stock. Zrušte začiarknutie políčka Head stock a ponechajte počet valcov ako 1, ako je znázornené na obr. 3DSPL1.6. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na obrobok.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0006.jpg' | relative_url }})

Zoznam objektov

## Obrobok

Na stránke Obrobok ponechajte názov objektu ako * * Obrobok** , teplotu objektu 20 °C a typ objektu ako * * Plast * *, ako je znázornené na obr. 3DSPL1.7. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 2D Geometry.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0007.jpg' | relative_url }})

Všeobecná stránka obrobku

### Import 2D geometrie obrobku

Import 2D geometrie, „**SpinLab-blank.DXF** “ z priečinka „3D/Labs/Spinning“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a potom kliknite na Skontrolovať a opraviť geometriu vo vyskakovacom okne na overenie geometrie. Geometria bude opravená z hľadiska jej orientácie, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) vo vyskakovacom okne správy a potom na tlačidlo OK pre zatvorenie okna overenia geometrie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh.

### Generovanie sieťoviny

Na stránke povrchovej siete vyberte typ povrchovej siete ako povrchovú sieť z tehál a definujte **cieľový počet prvkov** ako **90** pre povrchovú sieť prierezu. Pre 3D povrchovú sieť definujte **Počet otočných sekcií** ako **100**. Keďže nastavenie je implicitné ale, potrebujeme jemnejšiu sieťku pri kontakte na zachytenie presného kontaktu, preto definujeme jemnejšiu sieťku v kontaktnej oblasti o 15 stupňov uhol a pomer veľkosti ako 4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2d_mesh_button.jpg' | relative_url }})a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}). Sieť by mala vyzerať tak, ako je znázornené na obr. 3DSPL1.8. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na materiál.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0008.jpg' | relative_url }})

Vygenerované 3D pletivo pre obrobok

Priradiť materiál ``+``

Na stránke Materiál kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a načítajte materiál * * Oceľ * * skupinový materiál "**AISI-1010,COLD[70F(20C)]** " z okna knižnice materiálov. Priraďte materiál „**AISI-1010,COLD[70F(20C)]** “ pre obrobok, ako je znázornené na obr. 3DSPL1.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) do stránky Mandrel.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0009.jpg' | relative_url }})

Priradenie materiálu pre obrobok

Priebojník

Na stránke Mandrel General ponechajte predvolené hodnoty pre názov * *Mandrel** a teplotu 200 °C. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

### Import 2D geometrie vretena - prierez

Import 2D geometrie, „**SpinLab-mandrel.DXF** “ z priečinka „3D/Labs/Spinning“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a potom kliknite na Skontrolovať a opraviť geometriu vo vyskakovacom okne na overenie geometrie. Geometria sa opraví z hľadiska jej orientácie, v kontextovom okne správy kliknite na tlačidlo OK a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na zatvorenie okna overenia geometrie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry.

### Generovať 3D geometriu vretena

Použitím predvolenej hodnoty 100 ako „Počet otočených sekcií“ vygenerujete 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DSPL1.10.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku nastavenia referenčného bodu.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0010.jpg' | relative_url }})

Vygenerovaná 3D geometria vretena

### Referenčná stránka vretena

Na tejto stránke môžeme definovať referenčný bod tŕňa, použijeme predvolenú vypočítanú hodnotu D "-63,5", ako je znázornené na obr. 3DSPL1.11. „D“ je vzdialenosť medzi začiatkom deformácie a začiatkom vretena pozdĺž osi X a použije sa na umiestnenie vretena. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Tail Stock.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0011.jpg' | relative_url }})

Stránka nastavenia referenčného bodu

## Chvostové zásoby

Na stránke Tail stock General ponechajte predvolené hodnoty pre name ako **Tail stock** a teplotu ako 200°C. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

### Importovanie 2D geometrie chvosta - prierez

Import 2D geometrie, „**SpinLab-tailstock.DXF** “ z priečinka „**3D/Labs/Spinning** “. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) vo vyskakovacom okne na overenie geometrie. Geometria sa opraví z hľadiska jej orientácie, kliknite na tlačidlo ok v kontextovom okne správy a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na zatvorenie okna overenia geometrie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry.

### Generovať 3D geometriu chvosta

Použitím predvolenej hodnoty 100 pre "**Počet otáčaných sekcií** " vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DSPL1.12.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Roll.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0012.jpg' | relative_url }})

Generovaná 3D geometria chvosta

Prevaľovať

Na stránke Roll General ponechajte predvolené hodnoty pre name ako Roll a teplotu ako 200 °C. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku 2D prierezu.

### Importovanie 2D geometrie rolky - prierez

Import 2D geometrie, „**SpinLab-roll.DXF** “ z priečinka „**3D/Labs/Spinning** “. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) vo vyskakovacom okne na overenie geometrie. Geometria sa opraví z hľadiska jej orientácie, kliknite na tlačidlo ok v kontextovom okne správy a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na zatvorenie okna overenia geometrie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry.

### Generovať 3D geometriu rolky

Použitím predvolenej hodnoty **100** pre "**Počet otočných sekcií** " vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DSPL1.13.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientáciu.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0013.jpg' | relative_url }})

Vygenerovaná 3D geometria rolky

Orientácia

V tomto laboratóriu je pohyb valca pozdĺž osi vretena definovaný pomocou pohybu dráhy, ktorý vyžaduje definovanie dátumu valca. Treba poznamenať, že valce vyžadujú jedinečný prístup k nastaveniu kvôli použitiu ovládania pohybu dráhy. Preklad kotúča bude definovaný dráhou, ktorá sa použije v lokálnom UV (axiálnom/radiálnom) súradnicovom systéme. Jediný bod na valci, referenčný bod (dátum), bude nasledovať túto cestu. Aktuálne umiestnenie referenčného bodu, a teda rolovania, je určené údajmi o ceste a aktuálnym časom. Každý kotúč sledujúci dráhu musí mať definovaný referenčný bod.

Používateľ môže zvoliť počiatočný bod Roll pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) vedľa poľa Roll Datum (pozri obr. 3DSPL1.15.), ktoré poskytne možnosti, ako je znázornené na obr. 3DSPL1.16. Používateľ môže tiež zadať súradnice dátumu manuálne. V tomto laboratóriu sa centrum rotácie vyberie v dialógovom okne Roll Datum, definícia cesty pre valec je už správne nakonfigurovaná podľa referenčného bodu pôvodu (0,0), preto ponecháme súradnice Roll Datum na predvolené (0,0).

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0014.jpg' | relative_url }})

orientácia strany

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0015.jpg' | relative_url }})

Sprievodca dátumom rolovania

Valček musí byť naklonený na správnu orientáciu otáčania, ktorá je v tomto prípade 45 stupňov. Ak to chcete urobiť, na stránke Orientácia definujte orientačný uhol ako 45, ako je znázornené na obr. 3DSPL1.16. a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_angle_button.jpg' | relative_url }}). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pass Table.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0016.jpg' | relative_url }})

Stránka orientácie rolovania

## Tabuľka preukazov

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) definujete Pohyb pre Roll 1 v Pass table (pozri obr. 3DSPL1.17.).

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0017.jpg' | relative_url }})

Okno tabuľky ciest

Keďže sa valček pohybuje po určitej ceste, vyberieme cestu a definíciu typu cesty ako **funkciu času * * typu cesty, ako je znázornené na obr. 3DSPL1.18.

Všimnite si, že údaje o krivkovitej dráhe G-kódu musia byť znížené na lineárne údaje, pretože deformácia nepodporuje krivkovité dráhy.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0018.jpg' | relative_url }})

Roll 1 Movement page

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button2.jpg' | relative_url }}) a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_load_button_2.jpg' | relative_url }}) otvorte priečinok **SpinLab-roll-path_table.dat **. z priečinka **/3D/Labs/Spinning**. Zmeňte typ grafu na **U-V**, aby ste videli grafické znázornenie axiálneho (U) a radiálneho (V) profilu pohybu valca (pozri obr. 3DSPL1.20). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) v okne Synchronizácia s pohybom cesty a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) zatvorte definíciu.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0019.jpg' | relative_url }})

Synchronizácia s vyskakovacím oknom pohybu cesty

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0020.jpg' | relative_url }})

U-V graf

Všimnite si, že stredový bod Rotácia 1 je už definovaný údajmi o prenose cesty.

Vyberte typ otáčania ako „**Krútiaci moment** “ pre valec 1 a ponechajte hodnotu na 0, pretože valec sa otáča na základe krútiaceho momentu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku pohybu. Pre toto laboratórium nedefinujeme žiadne iné hodnoty a klikneme na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na Polohovanie.

Príkazy

Všetky predmety, ktoré sú namontované pozdĺž osi stroja (vreteník, tŕň, obrobok, koník), boli dovezené na správne miesto.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0021.jpg' | relative_url }})

Problém s automatickým polohovaním

Prejdite na stránku **Ovládacie prvky * * a potom kliknite na **Automatické polohovanie**. **Počiatočná (t=0)** možnosť presunie valec do polohy dráhy času = 0. Pri možnosti kontaktu sa valček presunie na miesto dráhy času pri kontakte. Použite **At contac****t** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) v kontextovom okne. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku Kontakt.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0022.jpg' | relative_url }})

Okno automatického polohovania

Kontakt

Na stránke Kontakt vyberte typ „**User** “ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). V tabuľke budeme pozorovať pridávanie predvolených vzťahov, zapnite začiarkavacie políčko pre tŕň - Pracovný kus a chvost - Vzťahy obrobku. Teraz definujte **Šmykovú** hodnotu trenia **0,12** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) vypočítate predvolenú hodnotu tolerancie kontaktu a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vytvoríte kontakt. V kontextovom okne „STAV PRILEPENIA“ vyberte možnosť Áno. Vygenerovaný kontakt, ktorý vyzerá ako na obr. 3DSPL1.23. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Zastavenie ovládacích prvkov.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0023.jpg' | relative_url }})

stránka s kontaktnými informáciami

## Zastavenie ovládacích prvkov

Definujte ** Trvanie procesu ** ako **22** s, ako je znázornené na obr. 3DSPL1.24. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na ovládacie prvky simulácie.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0024.jpg' | relative_url }})

Stránka trvania procesu

## Ovládacie prvky simulácie

Zadajte**Počet krokov* * ako * * 999999 * *, * * Prírastok kroku, aby ste ušetrili** ako **50** a **Čas na krok* * ako * * 0,001 * * s na stránke ovládacích prvkov simulácie, ako je znázornené na obr. 3DSPL1.25. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete stránku DB.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0025.jpg' | relative_url }})

Stránka s ovládacími prvkami simulácie

Všeobecné

Na stránke Generate DB kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) a vygenerujte databázu. Sledujte správu na karte Správa, ktorá informuje o stave generovania databázy.

## Simulácia behu

Po vygenerovaní databázy prepnite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. 3DSPL1.26. Použite predvolenú možnosť **Pokračovať v točení * * a vyberte možnosť „* *Pokračovať z posledného kroku** “ a potom vyberte režim simulácie ako * * Interaktívny * * a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0026.jpg' | relative_url }})

Okno Spustiť simuláciu

Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces odstreďovania, keď simulácia pokračuje podľa zadaných kritérií zastavenia zo simulačnej grafiky.

Postprocessing

Po dokončení simulácie skontrolujte výsledky prepnutím do režimu Post pomocou tlačidla nad panelom nástrojov simulácie.

Prehrajte si kroky simulácie a pozrite sa, ako sa tvorí časť obrobku počas procesu odstreďovania.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0027.jpg' | relative_url }})

V kroku -1

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0028.jpg' | relative_url }})

V kroku 10000

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0029.jpg' | relative_url }})

V poslednom kroku

Graf **Kmeň - Efektívna** stavová premenná a sledujte rozdelenie napätia.

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0030.jpg' | relative_url }})

V kroku -1

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0031.jpg' | relative_url }})

V kroku 10000

![]({{ '/assets/images/labs/spinning_labs/spinning_lab/image0032.jpg' | relative_url }})

V poslednom kroku
