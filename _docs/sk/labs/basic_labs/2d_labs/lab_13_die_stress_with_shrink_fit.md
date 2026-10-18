---
lang: sk
title: "Laboratórna úloha č. 13: Napätie v matrici pri montáži s tepelne zmrštiteľným spojom"
---

# Laboratórna úloha č. 13: Napätie v matrici pri montáži s tepelne zmrštiteľným spojom

V tomto laboratórnom cvičení vykonávame analýzu napätia v lisovacích formách pre projekt [Spike_Nonisothermal]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_05_spike_non-isothermal/' | relative_url }}) a pridávame dva ďalšie objekty s názvom „Holder“, ktoré slúžia na podoprenie spodnej lisovacej formy a upevnenie zúženého upínacieho zariadenia na hornej lisovacej forme.

13.1. Otvorenie súboru projektu

13.2. Pridať analýzu namáhania lisovacej formy

13.3. Výber kroku

13.4. Pridávanie objektov

13.5. Nastavenie hornej matrice

13.6. Nastavenie spodnej matrice

13.7. Nastavenie držiaka

13.8. Nastavenie prsteňa

13.9. Vytvorenie kontaktu

13.10. Ovládacie prvky simulácie

13.11. Vytvorenie databázy

13.12. Spustenie simulácie

13.13. Následné spracovanie výsledkov

## Otvorenie súboru projektu

Otvorte predtým simulovaný súbor **Spike_NoniSothermal.moproj** v programe DEFORM MO, ako je znázornené na obr. L13.1. Otvorí sa predspracovateľ programu MO.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0001.jpg' | relative_url }})

Okno grafického rozhrania programu DEFORM

## Pridať analýzu napätia v matrici

Ak sú už laboratórne testy napätia v matrici č. 6 a 12 vykonané, po otvorení projektu Spike_Nonisothermal si môžete všimnúť karty „Die Stress Study 1“ a „Die Stress Study 2“, ako je znázornené na obr. L13.2. V ľavom hornom rohu okna Display kliknite ľavým tlačidlom myši na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu Add Die stress Study, ako je znázornené na obr. L13.2.

V editore operácií bola k operácii „Napätie v lisovacej forme“ pridaná záložka „Štúdia napätia v lisovacej forme“, ako je znázornené na obr. L13.3.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0001.jpg' | relative_url }})

Pridanie operácie s napätím v matrici

## Výber kroku

Ak chcete vykonať operáciu „Die stress“, vyberte **krok** **50** na stránke výberu krokov, ako je znázornené na obr. L13.3. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0002.jpg' | relative_url }})

Zoznam výberu krokov

## Pridať objekty

Pridajte dva objekty kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) na stránke „Objekty“ (pozri obr. L13.4.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Horná forma“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0003.jpg' | relative_url }})

Zoznam objektov

## Nastavenie hornej matrice

### Definícia objektu „Top die“

V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Top Die“ ponechajte typ objektu ako pružný. Od verzie v13.1.1 boli na stránke objektov zavedené dve nové možnosti na umiestnenie matíc v budúcich krokoch pri analýze napätia matíc vo viacerých krokoch; pri analýze napätia matíc v jednom kroku tieto možnosti nie je potrebné používať, preto nechajte políčko „Need positioning“ (Potrebné umiestnenie) nezaškrtnuté. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka BCC, kde môžete priradiť okrajové podmienky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0023.jpg' | relative_url }})

Na začiatok stránky objektu

### Nastavenie okrajovej podmienky

Na hornú plochu hornej matrice nastavte okrajovú podmienku rýchlosti Vy = 0. Táto okrajová podmienka zabraňuje odletu matrice pri pôsobení síl, pozri obr. L13.6. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Interpolácia sily hornej matrice“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0004.jpg' | relative_url }})

Na začiatok stránky BCC

### Vynútená interpolácia

Na stránke „Interpolácia sily“ kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) a po vykonaní interpolácie sily sa v zozname správ zobrazí správa o interpolácii sily, ako je znázornené na obr. L13.7. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Spodná matrica“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0005.jpg' | relative_url }})

Okno interpolácie sily hornej matrice

## Nastavenie spodnej matrice

### Definícia objektu spodnej matrice

Pre spodnú formu ponecháme typ objektu „Elastic“ a zrušíme zaškrtnutie políčka „Potrebné polohovanie“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka BCC, kde priradíte okrajové podmienky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0024.jpg' | relative_url }})

Stránka objektu „Spodná matrica“

### Spodná matrica BCC

Na stránke BCC skontrolujte predvolene priradenú deformáciu BCC pre ľavú stranu obrobku v smere osi X; predvolené hodnoty BCC sa priradia automaticky na základe výberu typu úlohy ako osovo symetrickej (pozri obr. L13.9.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Force Interpolation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0006.jpg' | relative_url }})

Stránka „Spodná matrica BCC“

### Vynútená interpolácia

Kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) a po vykonaní interpolácie sily sa v zozname správ zobrazí správa o interpolácii sily, ako je znázornené na obr. L13.10. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Objekt 4.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0007.jpg' | relative_url }})

Vynútiť okno interpolácie

## Nastavenie držiaka

Pre objekt **HOLDER** zvolíme typ objektu **Elastic** a zrušíme zaškrtnutie políčka „Potrebné polohovanie“, ako je znázornené na obr. L13.11. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Geometria“, kde vytvoríte geometriu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0008.jpg' | relative_url }})

Stránka objektu „Holder“

### Vytvorenie geometrie pre držiak

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a vytvorte geometriu tak, že do tabuľky 1 zadáte nasledujúce hodnoty súradníc XYR (pozri obr. L13.12.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**X** |  **Y** |  **R**  
---|---|---  
4 |  -3 |  0  
4 |  -1 |  0  
1 |  -1 |  0  
1 |  -3 |  0  
  
Hodnota súradníc XYR v geometrii

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0009.jpg' | relative_url }})

Dialógové okno na úpravu geometrie

### Vytvorenie siete pre držiak

Nastavte **počet prvkov** na hodnotu **150** a vygenerujte sieť pomocou ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (pozri obr. L13.13.), potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“ (Materiál).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0010.jpg' | relative_url }})

Stránka „Holder Mesh“

### Priradenie materiálu pre držiteľa

Pre držiak zadajte materiál **AISI-H-13** výberom zo zoznamu materiálov (pozri obr. L13.14.) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0011.jpg' | relative_url }})

Priradenie materiálu držiaka

### Nastavenie okrajových podmienok pre Holdera

Nastavte okrajovú podmienku rýchlosti Vy = 0 na spodnej ploche držiaka, ako je znázornené na obr. L13.15, a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0012.jpg' | relative_url }})

Stránka držiteľa BCC

## Nastavenie prsteňa

Zmeňte **názov objektu** na **Ring**, nastavte počiatočnú **teplotu** na **250°** F, vyberte typ objektu **Elastic** a zrušte zaškrtnutie políčka „Need positioning“****(pozri obr. L13.16.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0013.jpg' | relative_url }})

Stránka objektu „Ring“

### Vytvorenie geometrie prsteňa

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a vytvorte geometriu tak, že do tabuľky 2 zadáte nasledujúce hodnoty súradníc XYR (pozri obr. L13.17) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**X** |  **Y** |  **R**  
---|---|---  
2,2 |  3,2 |  0  
2,2 |  1,2 |  0  
4 |  1,2 |  0  
4 |  3,2 |  0  
  
Hodnota súradníc XYR v geometrii

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0014.jpg' | relative_url }})

Dialógové okno „Upraviť geometriu“

### Vytvorenie siete pre prsteň

Nastavte **Počet prvkov** na hodnotu **150** a vygenerujte sieť pomocou ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (pozri obr. L13.18.), potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Materiál.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0015.jpg' | relative_url }})

Stránka „Ring Mesh“

### Priradenie materiálu pre prsteň

Pre krúžok nastavte materiál **AISI-H-13** výberom zo zoznamu materiálov a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Nastavenie okrajovej podmienky pre prstenec

Na hornú plochu prstena uplatnite okrajovú podmienku pre rýchlosť Vy = 0, ako je znázornené na obr. L13.19.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0016.jpg' | relative_url }})

Rýchlosť BCC pre prsteň

Nastavte zmršťovacie upevnenie v smere X = 0,008 pozdĺž vnútornej plochy a v rozbaľovacom okne „Presunúť uzlové súradnice objektu“ kliknite na „NIE“ (pozri obr. L13.20.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Kontakt“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0017.jpg' | relative_url }})

BCC s termoprídržným upevnením pre vnútorný povrch prstena

## Vytvorenie kontaktu

Na stránke Kontakt pridajte dva vzťahy kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Pre prvý vzťah vyberte ako **Hlavný objekt** položku **Prsteň** a ako **Podriadený objekt** položku **Horná matrica** a pre druhý vzťah vyberte ako **Hlavný objekt** **Držiak** a ako **Podriadený objekt** **Spodná matrica**; pre oba vzťahy nastavte hodnotu trenia na **0,12**. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určte vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,00136"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu, ako je znázornené na obr. L13.21. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky simulácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0018.jpg' | relative_url }})

Stránka na získavanie kontaktov

## Ovládacie prvky simulácie

V nastaveniach simulácie nastavte **Počet krokov simulácie** na hodnotu **5**, **krok pri ukladaní** na hodnotu **1**, **Maximálny uplynutý čas procesu na jeden krok** na **0,1** s a použite predvolený riešiteľ a metódu iterácie, ako je znázornené na obr. L13.22. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vytvorenie databázy.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0019.jpg' | relative_url }}).

Stránka s ovládacími prvkami simulácie

## Vytvorenie databázy

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Spustite simuláciu kliknutím na akčný štítok ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) a pomocou predvolenej možnosti **Pokračovať v behu** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak simulácia prebehne bez problémov, na koniec súboru so správami sa pridá nasledujúca správa: „NORMAL STOP: Simulácia bola dokončená a zastavená v časovom kroku určenom používateľom“.

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite do režimu zobrazenia výsledkov kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), ako je znázornené na obr. L13.23.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0020.jpg' | relative_url }})

Príspevok z Missouri

**Skontrolujte výsledné napätie u všetkých objektov**

Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}), vytvorte graf **efektívneho napätia** a **maximálneho hlavného napätia** a sledujte graf tak, ako je znázornené na obr. L13.24 a obr. L13.25. Tieto dve veličiny sú najdôležitejšími premennými pri simulácii napätia v lisovacej forme.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0021.jpg' | relative_url }})

Graf pôsobenia napätia v zobrazení s plným tieňovaním

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0022.jpg' | relative_url }})

Graf maximálneho hlavného napätia v líniovom zobrazení

****

**Súvisiace témy:**

[11\. General Object Data Definition]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }})

[14\. Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[6.2. Integrated Manufacturing Process Simulation layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
