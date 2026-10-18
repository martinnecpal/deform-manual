---
lang: sk
title: "Laboratórium valcovania tvaru ale3"
---

# ale Shape Rolling Lab3 ( s viacúčelovým stojanom a použitím booleovskej siete)

V tomto laboratóriu nastavíme jednoduchú ale viacnásobnú valcovaciu operáciu pomocou šablóny Shape Rolling, ktorá je k dispozícii v šablóne integrovaného výrobného procesu.

  
3.1. Vytvorenie nového problému

3.2. Operácia valcovania tvaru

3.3. Nastavenie procesných podmienok

3.4. Definovanie obrobku

3.4.1. Definovanie objektu obrobku

3.4.2. Vytvorenie geometrie obrobku

3.4.3. Generovanie pletiva obrobku

3.4.4. Priradenie materiálu obrobku

3.4.5. Definovanie okrajových podmienok obrobku

3.5. Definovanie drážok

3.5.1. Definovanie drážky pre geometriu kotúča

3.6. Definovanie viacnásobných pozícií pri prvom prechode

3.7. Generovanie 3D nastavenia

3.7.1. Nastavenia geometrie 3D Rolls

3.7.2. Stránka nastavení povrchovej siete 3D Roll

3.7.3. Nastavenie 3D obrobku pomocou metódy Boolean meshing

3.8. Úprava prevádzky Rolling Pass

3.8.1. Upravte tepelnú výmenu s prostredím BCC pre valce

3.8.2. Definovanie kontaktných vzťahov

3.8.3. Definovanie ovládacích prvkov simulácie

3.8.4. Generovanie databázy

3.9. Simulácia chodu

3.10. Post Processing

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. ALEL3.1. Pomocou prepínača vyberte prepínač „ * * Integrovaný výrobný proces * *“ a systém jednotiek ako „** SI * * “. Definujte názov problému ako „**SHR_ale_LAB3 ** “ a uistite sa, že je zapnuté začiarkavacie políčko „** Zobraziť dialóg možností * *“ (ak nezapneme začiarkavacie políčko „**Zobraziť dialóg možností * * “, nezobrazí sa dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0001.jpg' | relative_url }})

Okno výberu typu problému

  
Sprievodca viacnásobnou operáciou sa otvorí s dialógovým oknom Nový projekt, ako je znázornené na obr. ALEL3.2., v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**SHR_ale_LAB3 ** “. Operáciu 3D Shape Rolling je možné pridať aj v dialógu „New Project“ (pozri obr. ALEL3.2.), ale v tomto laboratóriu pridáme operáciu valcovania tvaru zo zoznamu operácií v Prieskumníkovi, takže nezačiarknite políčko "Prvá operácia" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

## Operácia valcovania tvaru

Pridajte jednu operáciu valcovania tvaru zo zoznamu operácií prieskumníka. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa Shape Rolling v Prieskumníkovi alebo ju používateľ môže pridať aj presunutím myšou do Editoru operácií (pozri obr. ALEL3.3.). Po pridaní operácie sa v oblasti vlastností otvorí stránka Proces.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0002.jpg' | relative_url }})

Pridanie operácie valcovania tvaru v sprievodcovi MO z nového okna projektu.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0003.jpg' | relative_url }})

Pridanie operácie valcovania tvaru z prieskumníka.

Procesné podmienky

Na stránke Proces vyberte typ valcovania ako „**Steady-State**** ale ** “ a typ symetrie ako „* * Quarter * * “, pretože budeme nastavovať objekt štvrťročnej symetrie. Keďže nás zaujíma teplotný gradient v kotúčoch, vyberte možnosť „**Obrobok a kotúče (neizotermické)** “.

Zmeňte koeficient rozhrania **Trenie* ** * na ** 0,5 * * a koeficient rozhrania **Teplo****prenos**** na ** 5 **(ide o globálne hodnoty platné pre všetky stojany a priechody), ako je znázornené na obr. ALEL3.4., budeme ďalej aktualizovať podmienky trenia v medziobjektových vzťahoch počas 3D nastavenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})na stránku WP_CrossSection.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0004.jpg' | relative_url }})

Definovanie podmienok valivého procesu na stránke Proces.

## Definovanie obrobku

### Definovanie objektu obrobku

V okne **WP_CrossSection ** ponechajte typ objektu ako „**Plastic**“ a zadajte teplotu obrobku ako **100°** C (pozri obr. ALEL3.5.). Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0005.jpg' | relative_url }})

Definícia objektu obrobku.

### Vytváranie geometrie obrobku

Keďže nastavujeme model štvrťročnej symetrie, musíme vytvoriť 1/4th dutú geometriu valca pre obrobok. Ak to chcete urobiť, na stránke Geometria vyberte možnosť Definovať primitívne, z okna primitívnej geometrie vyberte dutý valec a definujte parametre pre stredový bod ako (0, 0), polomer R1 ako **30** mm a polomer R2 ako **50** mm, ako je znázornené na obr. ALEL3.6. Zatvorte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0006.jpg' | relative_url }})

Definovať primitívne

### Generovanie pletiva obrobku

Vygenerujte povrchovú sieť obrobku s cieľovým počtom prvkov ako **100** a ponechajte ostatné možnosti v ich predvolených nastaveniach (pozri obr. ALEL3.7.). Ak je to potrebné, expertný režim je prístupný po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), čím získate prístup k ďalším nastaveniam na ovládanie 2D povrchovej siete. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0007.jpg' | relative_url }})

Generovanie pletiva obrobku

### Priradenie materiálu obrobku

Ak chcete priradiť materiál k obrobku, vyberte materiál kategórie ocele „**AISI* ***-1055** “ z knižnice materiálov a priraďte ho k obrobku. Dá sa to urobiť tak, ako je znázornené na obr. ALEL3.8. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na BCC.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0008.jpg' | relative_url }})

Priradenie materiálu pre obrobok.

### Definovanie hraničných podmienok obrobku

Počas generovania povrchovej siete je rýchlosť BCC pozdĺž okrajov symetrie priradená obrobku, keď sme generovali geometriu štvrťročnej symetrie, ako je znázornené na obr. ALEL3.9. Kliknite na stránku zoznamu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Groove.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0009.jpg' | relative_url }})

Stránka hraničných podmienok obrobku.

## Definovanie drážok

Na stránke Groove List môžeme definovať 2D prierez valcov kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Jedným kliknutím na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte jednu drážku (pozri obr. ALEL3.10.), budeme používať rovnakú drážku na všetkých valcovacích stojanoch.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0010.jpg' | relative_url }})

Stránka zoznamu drážok.

### Definovanie drážky pre geometriu kotúča

Vyberte prvú drážku a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) vyberte drážku z jedného z existujúcich základných drážok Roll.

Otvorí sa stránka Roll Groove Primitive, vyberte **Flat** rolls. Definujte geometriu 2D prierezu valcových drážok so šírkou (W) ako 200, polomerom (r1) ako 10 a polomerom valca (RR) ako 100, ako je znázornené na obr. ALEL3.11. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku Roll Groove Primitive. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pass.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0011.jpg' | relative_url }})

Definovanie geometrie drážky.

## Definovanie viacnásobných pozícií v prvom prechode

V priechodnom stole vyberte priechod 1 a kliknite na tlačidlo stojanového stola, ako je znázornené na obr. ALEL3.12.

V stolíku pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte 4 stojany. Na všetkých štyroch stánkoch,

* Ponechajte typ Rollset ako vertikálny pre všetky 4 stojany.

* Vyberte Groove1 ako geometriu drážky pre horný valec na všetkých štyroch stojanoch.

* Definujte rýchlosť valenia (ot/min) ako **55 otáčok za minútu **.

* Nastavte teplotu valca na **40C** na všetkých štyroch stojanoch.

Definujte medzeru medzi valcami (mm) ako **88 mm ** , **86 mm** , **84 mm ** a **82 mm** pre 1., 2., 3. a 4. stojan a pozíciu X ako 0, 200, 400 a 600 pre 1., 2., 3. a 4. stojan, ako je znázornené na obr. ALEL3.13. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku nastavení stola. Ponechajte ostatné nastavenia v tabuľke Pass ako predvolené a kliknite na stránku nastavenia ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku 3D.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0012.jpg' | relative_url }})

Pass Table.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0013.jpg' | relative_url }})

Nastavenia viacerých stojanov definované v tabuľke stojanov pre prvý priechod.

## Generovanie nastavenia 3D

Po definovaní multi stojanov zadaním polohy X a pri vstupe na stránku 3D nastavenia dostaneme vyskakovacie okno Dĺžka obrobku, ktoré definuje dĺžku obrobku väčšiu ako vzdialenosť medzi prvým a posledným valcom (600), ako je znázornené na obr. ALEL3.14. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) zatvorte vyskakovacie okno. Na stránke 3D nastavenia máme možnosti nastavenia geometrie a povrchovej siete pre nastavenie obrobku a geometrie 3D valcov. Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) priliehajúce k príslušným objektom je možné použiť na úpravu nastavení, pozri obr. ALEL3.15.)

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0014.jpg' | relative_url }})

Vyskakovacie okno s dĺžkou obrobku zo stránky nastavenia 3D.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0015.jpg' | relative_url }})

Stránka 3D Setup (Nastavenie 3D).

### Nastavenia geometrie 3D Rolls

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) geometrie 3D valcov, otvorí sa okno geometrie 3D valcov s nastaveniami geometrie 3D valcov. Definujte **počet vrstiev** pre valce ako **108** a vyberte možnosť „Jemnejšia geometria od“, aby ste vytvorili jemné polygóny bližšie ku kontaktnej oblasti s obrobkom, používame 300° ako začiatok a 360° ako koncový uhol, ako je znázornené na obr. ALEL3.16. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vygenerujete kotúče s novými nastaveniami. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno geometrie 3D rolovania.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0016.jpg' | relative_url }})

Stránka nastavení 3D Roll Geometry.

### Stránka nastavení 3D rolovacej povrchovej siete.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) v okne 3D Rolls mesh, okno 3D roll mesh sa otvorí s nastaveniami pre 3D roll mesh. Definujte počet otočných sekcií pre valce ako 72 a vyberte možnosť „Jemnejšia sieť od“, aby ste vytvorili jemné polygóny bližšie ku kontaktnej oblasti s obrobkom, nastavíme 330° ako začiatok a 360° ako koncový uhol pre jemnejšiu oblasť siete. Ak chcete priradiť materiál pre valce, načítajte materiál matrice „AISI-D3“ z knižnice materiálov a vyberte tento materiál v rozbaľovacej ponuke, ako je znázornené na obr. ALEL3.17. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vygenerujete povrchovú sieť roliek a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte okno 3D povrchovej siete roliek.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0029.jpg' | relative_url }})

Stránka nastavení povrchovej siete 3D Roll.

### Nastavenie 3D obrobku pomocou metódy Boolean meshing

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) 3D obrobku, otvorí sa okno Mesh s nastaveniami siete 3D obrobku. Vyberte užívateľské prepínacie tlačidlo pre Dĺžku obrobku a definujte dĺžku ako 1000 mm, definujte **Počet vrstiev** ako **120** a vyberte jemnejšiu mriežku z možnosti generovať jemnú mriežku od 0,33 do 0,67 (0 ako začiatok a 1 ako koniec dĺžky obrobku), ako je znázornené na obr. ALEL3.18. Metódu mriežkovania ponecháme ako Booleovskú. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}) vygenerujete 3D povrchovú sieť obrobku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno Mesh v nastaveniach povrchovej siete obrobku. Kliknutím na tlačidlo Generovať všetko vygenerujete 3D valce a obrobok pre všetky stojany. Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0017.jpg' | relative_url }})

Stránka nastavení 3D povrchovej siete obrobku.

  
Teraz uložte projekt a vyberte operáciu Rolling Pass v editore operácií kliknutím na dlaždicu operácie, aby ste upravili nastavenia Pass.

## Úprava prevádzky Rolling pass

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0018.jpg' | relative_url }})

Prevádzka Rolling Pass.

Pri výbere operácie Rolling Pass sa zobrazí stránka stola, ako je znázornené na obr. ALEL3.19. ktorý zobrazuje všetky údaje o 4 stojanoch. Keďže sme už tieto nastavenia definovali, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku RollStand1 Top Roll BCC.

### Upravte tepelnú výmenu s prostredím BCC pre valce

Počas vytvárania siete bola k celému kotúču priradená výmena tepla s prostredím BCC. Výmena tepla s prostredím BCC musí byť upravená tak, aby zohľadňovala polosymetrickú geometriu valca. Vyberte vetvu **Defined** v časti Heat Exchange with Environment a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}) z ponuky BCC, aby ste odstránili existujúcu hraničnú podmienku. Vyberte všetky hraničné uzly na kotúči kliknutím okrem uzlov na symetrickom povrchu kotúča pomocou vychystávacích nástrojov pozdĺž ľavej strany obrazovky. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) v ponuke BCC pridajte novú hraničnú podmienku, ako je znázornené na obr. ALEL3.20. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Top Roll BCC na RollStand2.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0028.jpg' | relative_url }})

Modifikovaná výmena tepla s prostredím BCC pre kotúč.

Podobne aktualizujte BCC pre stojan 2, stojan 3 a stojan 4 kotúče. Po aktualizácii kotúčov vo všetkých stojanoch kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Kontakt.

### Definovanie kontaktných vzťahov

Na stránke Kontakt sa automaticky pridajú vzťahy master-slave medzi valcami a obrobkom. Vyberte prvý vzťah a definujte * * Coulombovo * * trenie ako **0,5** a **Rozhranie** ** koeficient prestupu tepla ** ako **5** (pozri obr. ALEL3.21.) pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) budeme aplikovať rovnaké trecie podmienky medzi všetkými stojanmi Top Rolls a obrobkom. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určíte inteligentnú toleranciu kontaktu a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujete kontakty medzi objektmi. Kliknite na stránku ovládacích prvkov simulácie ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0021.jpg' | relative_url }})

Generovanie kontaktov.

### Definovanie ovládacích prvkov simulácie

V súbore strán ovládacích prvkov simulácie **Počet krokov** ako **5000** pre túto simuláciu s krokom ** na uloženie** ako **25** a **Čas za krok** ako **0,001** s. Z DEFORMÁCIE v12 bola v krokových ovládacích prvkoch pridaná možnosť zastavenia konvergencie ale v ustálenom stave, používateľ môže definovať kritériá zastavenia ale v ustálenom stave pre valcovaciu prevádzku ale. V tomto laboratóriu použijeme predvolené hodnoty, kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujeme databázu.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0022.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie.

### Generovanie databázy

Na stránke generovania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pristúpiť k generovaniu databázy (pozri obr. ALEL3.23.).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0023.jpg' | relative_url }})

Generovanie databázy.

## Simulácia behu

Po vygenerovaní databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad operačným stromom. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. ALEL3.24. Použite predvolenú možnosť **Pokračovať*** * Spustiť * * a vyberte možnosť „**Pokračovať z posledného kroku** “ a potom vyberte režim simulácie ako prepínač * * Interaktívne * *. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) pre spustenie simulácie.

Ak chcete definovať nastavenia MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}), okno Možnosti spustenia sa rozbalí a zobrazí možnosti definovania nastavení MPI pre simuláciu (maximálny počet procesorov, ktoré možno definovať v závislosti od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0024.jpg' | relative_url }})

Spustiť vyskakovacie okno simulácie.

  
Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces valcovania, pretože simulácia prebieha z grafiky simulácie
  
Simulácia sa zastaví po dosiahnutí stabilného stavu s nižšie uvedenou správou v súbore správy.
"
PROGRAM ZASTAVENÝ!
AKTUÁLNY VALIVÝ PRIECHOD DOSIAHOL PODMIENKY USTÁLENÉHO STAVU ".

Postprocessing

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), otvorí sa postprocesor MO (ako je znázornené na obr. ALEL3.25.).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0025.jpg' | relative_url }})

Režim MO Post po dokončení simulácie.

Prejdite na posledný krok, zakreslite premenné Efektívne napätie a Efektívny stav napätia a sledujte rozdelenie stavových premenných.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0026.jpg' | relative_url }})

Efektívna distribúcia napätia v rovnovážnom stave.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab3/image0027.jpg' | relative_url }})

Efektívne rozloženie napätia v rovnovážnom stave.
