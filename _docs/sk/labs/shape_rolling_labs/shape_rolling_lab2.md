---
lang: sk
title: "Tvarové valcovanie Lab2"
---

# Tvarové valcovanie Lab2 (Lagrangian pomocou tehlovej siete)

V tomto laboratóriu nastavíme jednoduchú lagrangeovskú viaccestnú valcovaciu operáciu pomocou šablóny Shape Rolling, ktorá je k dispozícii v šablóne integrovaného výrobného procesu.

2.1. Vytvorenie nového problému

2.2. Operácia valcovania tvaru

2.3. Nastavenie procesných podmienok

2.4. Definovanie obrobku

2.4.1. Definovanie objektu obrobku

2.4.2. Vytvorenie geometrie obrobku

2.4.3. Generovanie pletiva obrobku

2.4.4. Priradenie materiálu obrobku

2.4.5. Definovanie okrajových podmienok obrobku

2.5. Definovanie drážok

2.5.1. Definovanie drážok pre geometriu kotúča

2.6. Definovanie 4 priechodov s 2 stojanmi v 3. a 4. priechode

2.7. Generovanie 3D nastavenia

2.7.1. Nastavenia geometrie 3D Roll

2.7.2. Nastavenia povrchovej siete 3D Roll

2.7.3. 3D nastavenie obrobku pomocou tehlovej siete

2.7.4. Definícia posunovača

2.8. Ovládacie prvky simulácie na úrovni valivej skupiny

2.9. Úprava operácie Rolling pass 1 (Pass 1)

2.9.1. Stojan na priechod 1

2.9.2. Zadná strana stola

2.9.2.1. Definovanie zadnej geometrie stola

2.9.2.2. Stôl späť Mesh Generation

2.9.2.3. Priradenie materiálu spätného stola

2.9.3. Objekt posunovača

2.9.3.1. Definícia pohybu posunovacieho objektu

2.9.4. Umiestnenie objektu

2.9.5. Definovanie kontaktných vzťahov

2.9.6. Definovanie ovládacích prvkov simulácie

2.9.7. Generovanie databázy

2.10. Úprava operácie Rolling pass 2 (Pass 2)

2.10.1. Vytvorenie geometrie stola a vytvorenie povrchovej siete

2.10.2. Definícia pohybu posunovacieho objektu

2.10.3. Definícia polohovania harmonogramu

2.10.4. Stránka s ovládacími prvkami simulácie

2.11. Úprava operácie Rolling pass 3 (Pass 3)

2.11.1. Vytvorenie geometrie stola a vytvorenie povrchovej siete

2.11.2. Definovanie pohybu valcov stojana 2

2.11.3. Definícia pohybu posunovacieho objektu

2.11.4. Definícia polohovania harmonogramu

2.11.5. Stránka s ovládacími prvkami simulácie

2.12. Úprava operácie Rolling pass 4 (Pass 4)

2.12.1. Vytvorenie geometrie stola a vytvorenie povrchovej siete

2.12.2. Definovanie pohybu valcov stojana 2

2.12.3. Definícia pohybu posunovacieho objektu

2.12.4. Definícia polohovania harmonogramu

2.12.5. Stránka s ovládacími prvkami simulácie

2.13. Simulácia chodu

2.14. Post Processing

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. L2.1. Pomocou prepínača vyberte prepínač „* * Integrovaný výrobný proces * *“ a systém jednotiek ako „** SI * * “. Definujte názov problému ako „**SHR_LAG_LAB2 ** “ a uistite sa, že je zapnuté začiarkavacie políčko „** Zobraziť dialóg možností * *“ (ak nezapneme začiarkavacie políčko „**Zobraziť dialóg možností * * “, nezobrazí sa dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0001.jpg' | relative_url }})

Okno výberu typu problému

Sprievodca viacnásobnou operáciou sa otvorí s dialógovým oknom Nový projekt, ako je znázornené na obr. L2.2., v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „** * *SHR_LAG_LAB2** * * “. Operáciu 3D Shape Rolling je možné pridať aj v dialógu „New Project“ (pozri obr. L2.2.), v tomto laboratóriu pridáme operáciu valcovania tvaru zo zoznamu operácií prieskumníka, takže nezačiarknite políčko "Prvá operácia" a operáciu "Valcovanie tvaru" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0002.jpg' | relative_url }})

Pridanie operácie valcovania tvaru v používateľskom rozhraní MO z nového okna projektu.

## Operácia valcovania tvaru

Pridajte jednu operáciu valcovania tvaru zo zoznamu operácií prieskumníka. Operáciu možno pridať kliknutím na tlačidlo Operácia valcovania tvaru ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môže používateľ pridať aj presunutím myšou do editora operácií. (Pozri obr. L2.3.). Po pridaní operácie sa v oblasti vlastností otvorí stránka Proces.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0003.jpg' | relative_url }})

Pridanie operácie valcovania tvaru z prieskumníka

Procesné podmienky

Na stránke Proces vyberte typ valcovania ako „**Lagrangeovský** “ a typ symetrie ako „* * Plný * * “, pretože budeme nastavovať štvrťročný objekt symetrie. Keďže nás zaujíma teplotný gradient v kotúčoch, vyberte možnosť „**Obrobok a kotúče (neizotermické)** “. Definujte hodnotu koeficientu trenia ako **0,7 * * a hodnotu koeficientu prestupu tepla ako **11 * *, ako je znázornené na obr. L2.4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku WP_CrossSection.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0004.jpg' | relative_url }})

Definovanie podmienok valivého procesu na stránke Proces.

## Definovanie obrobku

### Definovanie objektu obrobku

V okne WP_CrossSection ponechajte typ objektu ako „Plast“ a zadajte teplotu obrobku 100 °C (pozri obr. L2.5.). Pokračujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0005.jpg' | relative_url }})

Definícia objektu obrobku.

### Vytváranie geometrie obrobku

Musíme vytvoriť geometriu tyče pre obrobok. Ak to chcete urobiť, na stránke Geometria vyberte ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), z okna primitívnej geometrie vyberte lištu a definujte parametre pre východiskový bod ako (-50, -42,5), šírku (W) ako 100 mm a výšku (H) ako 85 mm, ako je znázornené na obr. L2.6. Zatvorte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0006.jpg' | relative_url }})

Definujte primitívne.

### Generovanie pletiva obrobku

Vygenerujte povrchovú sieť obrobku s počtom prvkov 100 a ponechajte ďalšie možnosti v ich predvolených nastaveniach (pozri obr. L2.7.). Ak je to potrebné, expertný režim je prístupný po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), čím získate prístup k ďalším nastaveniam na ovládanie 2D povrchovej siete. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0007.jpg' | relative_url }})

Generovanie pletiva obrobku.

### Priradenie materiálu obrobku

Ak chcete priradiť materiál pre obrobok, vyberte materiál kategórie ocele „**AISI-1045** “ z knižnice materiálov a priraďte ho k obrobku. Dá sa to urobiť tak, ako je znázornené na obr. L2.8. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na BCC.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0008.jpg' | relative_url }})

Priradenie materiálu k obrobku.

### Definovanie hraničných podmienok obrobku

Počas generovania siete je výmena tepla s prostredím BCC priradená k obrobku, ako je znázornené na obr. L2.9. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Groove list.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0009.jpg' | relative_url }})

Stránka hraničných podmienok obrobku.

## Definovanie drážok

Na stránke Groove List môžeme definovať 2D prierez valcov kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) trikrát pridáte 3 drážky (pozri obr. L2.10.), použijeme drážku 1 pre priechod 1 a priechod 2 a drážku 2 a drážku 3 pre priechod 3 a priechod 4 (2 stojany).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0010.jpg' | relative_url }})

Stránka zoznamu drážok.

### Definovanie drážok pre geometriu kotúča

Vyberte prvú drážku a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) vyberte drážku z jedného z existujúcich základných drážok Roll.

Otvorí sa stránka Roll Groove Primitive, vyberte položku Flat rolls (Ploché kotúče). Definujte geometriu 2D prierezu valcových drážok so šírkou (W) ako 120, polomerom (r1) ako 5 a polomerom valca (RR) ako 100, ako je znázornené na obr. L2.11. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku Roll Groove Primitive.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0011.jpg' | relative_url }})

Definovanie geometrie drážky 1

Podobne vyberte druhú drážku a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), potom vyberte Ploché valce. Definujte geometriu 2D prierezu valcových drážok so šírkou (W) ako 60, polomerom (r1) ako 5 a polomerom valca (RR) ako 100, ako je znázornené na obr. L2.12. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku Roll Groove Primitive.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0012.jpg' | relative_url }})

Definovanie geometrie drážky 2

Podobne vyberte tretiu drážku a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), potom vyberte Ploché valce. Definujte geometriu 2D prierezu valcových drážok so šírkou (W) ako 120, polomerom (r1) ako 5 a polomerom valca (RR) ako 50, ako je znázornené na obr. L2.13. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku Roll Groove Primitive. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pass.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0013.jpg' | relative_url }})

Geometria Defininig Groove 3

## Definovanie 4 priechodov s 2 stojanmi v 3. a 4. priechode

V tabuľke priechodov pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte 4 priechody. Na všetkých štyroch priechodoch dodržujte

* Typ rollsetu ako vertikálny pre všetky 4 priechody.

* Nastavte teplotu valca na **40C** pre všetky prihrávky.

* Definujte rýchlosť valenia ako **50 otáčok za minútu pre** všetky štyri priechody.

Definujte **drážku1** ako geometriu drážky horného valca pre 1. a 2. priechod a **drážku2** ako geometriu drážky horného valca pre 3. a 4. priechod. Definujte medzeru medzi valcami (mm) ako **80 mm ** , **75 mm** , **65 mm** a **60 mm** pre 1., 2., 3r d a 4. priechod. Zapnite začiarkavacie políčko **Reverse*** * Rolling * * pre 2. a 4. priechod, ako je znázornené na obr. L2.14.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0014.jpg' | relative_url }})

Tabuľka preukazov

Vyberte Pass 3 a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_stand_table_button.jpg' | relative_url }}), ako je znázornené na obr. L2.14. na zobrazenie stojanového stola. V tabuľke stojanov pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte 2. stojan a definujte parametre 2. stojanu, ako je znázornené na obr. L2.15.

* Typ rollsetu definujte ako **vodorovný** pre 2. stojan.

* Vyberte Groove3 ako geometriu drážky pre horný valec na 2. stojane.

* Definujte rýchlosť valenia (ot/min) ako **0 otáčok za minútu **.

* Definujte medzeru medzi valcami (mm) ako **90 mm**.

* Nastavte teplotu kotúča na **40C** na 2. podstavci.

* Definujte polohu X (mm) ako **0 mm**.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku nastavení stola.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0015.jpg' | relative_url }})

Definovanie 2 stánkov v stánku pre tretí priechod

Podobne vyberte **Pass 4** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_stand_table_button.jpg' | relative_url }}).

V stolíku pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte 2. stojan a definujte 2. stojan, ako je znázornené na obr. L2.16.

* Typ rollsetu definujte ako **vodorovný** pre 2. stojan.

* Vyberte **Groove3** ako geometriu drážky pre horný valec na 2. stojane.

* Definujte rýchlosť rolovania (ot/min) ako **0 otáčok za minútu.**

* Definujte medzeru medzi valcami (mm) ako **90 mm**.

* Nastavte teplotu kotúča na **40C** na 2. podstavci.

* Definujte polohu X (mm) ako **0 mm**.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku nastavení stola. Ponechajte ostatné nastavenia v tabuľke Pass ako predvolené a kliknite na stránku nastavenia ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku 3D.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0016.jpg' | relative_url }})

Definovanie 2 stojanov v stánku pre štvrtý priechod

## Generovanie nastavenia 3D

Na stránke 3D nastavenia máme možnosti nastavenia geometrie a povrchovej siete pre obrobok, rolky a posunovač, ktoré sa vzťahujú na všetky priechody a stojany. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) vedľa príslušných objektov môžeme upraviť nastavenia. V tomto laboratóriu zaškrtnite políčko „**Zabrániť krúteniu** “, ak nie je predvolene zaškrtnuté, ako je znázornené na obr. L2.17.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0017.jpg' | relative_url }})

Stránka 3D Setup (Nastavenie 3D).

### Nastavenia geometrie 3D rolky

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) geometrie 3D valcov, otvorí sa okno geometrie 3D valcov s nastaveniami geometrie 3D valcov. Definujte **počet vrstiev** pre kotúče ako **72** pomocou možnosti „**Uniform****geometry generation** “, ako je znázornené na obr. L2.18. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vygenerujete kotúče s definovanými nastaveniami pre všetky prihrávky a stojany. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno geometrie 3D rolovania.

  
![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0018.jpg' | relative_url }})

Stránka nastavení 3D Roll Geometry

### Nastavenia 3D rolovacej siete

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) 3D rolovacej siete, otvorí sa okno 3D rolovacej siete s nastaveniami pre 3D rolovaciu sieť. Definujte **počet otočných profilov** pre kotúče ako **72** pomocou možnosti „**Uniform mesh generation** “ a importujte materiál matrice „AISI-H-13“ z knižnice materiálov na priradenie k kotúčom, ako je znázornené na obr. L2.19. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vygenerujete povrchovú sieť pre kotúče s definovanými nastaveniami pre všetky priechody a stojany a priradíte materiál. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno 3D rolovacej siete.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0048.jpg' | relative_url }})

Stránka nastavení povrchovej siete 3D Roll

### 3D nastavenie obrobku pomocou tehlovej siete

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) 3D obrobku, otvorí sa okno Mesh s nastaveniami siete 3D obrobku. Vyberte prepínač používateľa pre ** Dĺžka obrobku ** a definujte dĺžku ako **600 mm** , definujte **Počet vrstiev** ako **120** pomocou možnosti „**Jednotná *** *hrúbka vrstiev** “ na vytvorenie rovnomernej siete, ako je znázornené na obr. L2.20. Pre nastavenie lagrangian budeme mať k dispozícii iba metódu boolean meshing. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}) vygenerujete 3D povrchovú sieť obrobku. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno Mesh nastavenia povrchovej siete obrobku po vygenerovaní povrchovej siete.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0019.jpg' | relative_url }})

Stránka nastavení 3D povrchovej siete obrobku

### Definícia posunovača

Na stránke 3D nastavenia môžeme vybrať posunovač ako objekt alebo BCC. V tomto laboratórnom nastavení budeme používať posunovač ako objekt, takže zvoľte prepínač „**Objekt** “ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}), ako je znázornené na obr. L2.21. na umiestnenie obrobku vo vzťahu k valcom v závislosti od smeru pohybu valcov a posunovača k obrobku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku ovládacích prvkov simulácie.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0020.jpg' | relative_url }})

Definícia objektu posunovača na stránke nastavenia 3D.

## Ovládacie prvky simulácie na úrovni valcovacej skupiny

Na tejto stránke s ovládacími prvkami simulácie musíme vybrať riešiteľa ako **PRÍUŠNICE**, pretože používame horizontálne valce s torzným pohybom v 3. a 4. priechode. Po výbere riešiteľa kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_passes_button.jpg' | relative_url }}). Teraz uložte projekt a vyberte operáciu Rolling Pass 1 v editore operácií kliknutím na dlaždicu operácie a upravte nastavenia funkcie Pass 1.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0021.jpg' | relative_url }})

Ovládacie prvky simulácie na úrovni valivej skupiny

## Úprava operácie Rolling pass 1 (Pass 1)

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0022.jpg' | relative_url }})

Prevádzka Rolling Pass

Pri výbere operácie Rolling Pass 1 sa zobrazí stránka tabuľky Stand, ako je znázornené na obr. L2.23. ktorý zobrazuje údaje Pass 1.

### Stôl na stojan pre priechod 1

V tomto laboratóriu musíme použiť **stôl *** * zadný * * a ** stôl ** ** predný * *, takže zapnite začiarkavacie políčko, ako je znázornené na obr. L2.24. Keď sa vygeneruje povrchová sieť a priradí sa materiál pre kotúče, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Tabuľka (Späť).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0023.jpg' | relative_url }})

Stôl stojana pre Pass 1

### Stôl (chrbát)

Na stránke Tabuľka (Späť) potvrďte predvolenú teplotu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0026.jpg' | relative_url }})

Tabuľka (zadná) strana

#### Definovanie zadnej geometrie stola

Na stránke geometrie zadnej strany tabuľky vyberte položku „Definovať primitívne“ a definujte parametre uvedené nižšie pre geometriu zadnej strany tabuľky.
Východiskový bod X = -50 mm
Šírka W = 100 mm
Výška H = 5 mm
Dĺžka = 750

Začiarknite políčko „Zarovnať k hornej časti spodného valca pre valcovanie pásov“
Pass Line = 2,5 mm.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) pre vytvorenie tabuľky a ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie geometrie tabuľky/vodiacej lišty Primitívna stránka a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre povrchovú sieť.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0027.jpg' | relative_url }})

Vytvorenie geometrie zadnej tabuľky

#### Stôl späť Mesh Generation

Prepnite do Expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), potom definujte **Uniform Thickness number of layers** as * * 5 * * a ponechajte zvyšok nastavení ako predvolené. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujete povrchovú sieť pre tabuľku.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0028.jpg' | relative_url }})

Generovanie povrchovej siete zadnej tabuľky

#### Priradenie materiálu zadného stola

Ak chcete priradiť materiál pre zadný stôl, vyberte materiál „**AISI-H-13** “ z okna materiálu. Dá sa to urobiť tak, ako je znázornené na obr. L2.28. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po prednú stranu tabuľky.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0029.jpg' | relative_url }})

Priradenie materiálu zadnej časti stola

  
Prednú stranu stola definujte ako zadnú stranu stola s rovnakými nastaveniami pre geometriu, povrchovú sieť a materiál.

### Objekt posunovača

Objekt posunovača sa vytvorí automaticky pomocou rozmerov obrobku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) skontrolujte vytvorenú geometriu a priradené ovládacie prvky pohybu.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0030.jpg' | relative_url }})

Stránka objektu posunovača

#### Definícia pohybu posunovacieho objektu

Vyberte možnosť Rýchlosť. Rýchlosť posunovača by mala byť 50 až 60% relatívnej rýchlosti valcov, a preto priradiť **konštantnú rýchlosť** 340 ** mm/s pre posunovač, ako je znázornené na obr. L2.30. Náhľad pohybu môžete vidieť kliknutím na možnosť „Náhľad pohybu“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Umiestnenie objektu.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0031.jpg' | relative_url }})

Definícia pohybu posunovacieho objektu

### Umiestnenie objektu

Objekty sa automaticky umiestnia správne, keď klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) na stránke 3D nastavenia a predná a zadná strana stola sa automaticky vytvoria na správnej pozícii, takže teraz nemusíme robiť žiadne polohovanie. Umiestnené predmety by sa mali objaviť tak, ako je znázornené na obr. L2.31.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0032.jpg' | relative_url }})

Poloha objektov

### Definovanie kontaktných vzťahov

Na stránke Kontakt sa automaticky pridajú vzťahy master-slave medzi valcami a obrobkom. Vyberte prvý vzťah a definujte * * šmykové * * trenie ako **0,7** a súčiniteľ prestupu tepla rozhraním ako **11**(pozri obr. L2.32.) pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) budeme aplikovať rovnaké trecie podmienky medzi všetkými stojanmi Top Rolls a obrobkom. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určíte inteligentnú toleranciu kontaktu a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujete kontakty medzi objektmi. Kliknite na stránku ovládacích prvkov simulácie ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0033.jpg' | relative_url }})

Generovanie kontaktov.

### Definovanie ovládacích prvkov simulácie

Na stránke ovládacích prvkov simulácie prepnite do režimu vedenia kliknutím na položku ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) a potom nastavte **Počet krokov** ako **5000** pre túto simuláciu s krokom ** na uloženie* * ako * *10** a **Čas na krok** ako **0,001** s. Pre kritériá zastavenia použite predvolený bod roviny zastavenia a vyberte ** smer X **. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete databázu.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0034.jpg' | relative_url }})

Ovládacie prvky simulácie.

### Generovanie databázy

Na stránke generovania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pristúpiť k generovaniu databázy (pozri obr. L2.34.).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0035.jpg' | relative_url }})

Generovanie databázy

## Úprava operácie Rolling pass 2 (Pass 2)

Teraz uložte projekt a vyberte operáciu Rolling Pass 2 v editore operácií kliknutím na dlaždicu operácie, aby ste upravili nastavenia Pass 2. Potrebujeme použiť stoly vzadu a vpredu v priechode 2, takže zapnite zaškrtávacie políčka Table back a Table front v stolíku pass2, ako je znázornené na obr. L2.24. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Top Roll mesh.

### Vytvorenie geometrie stola a vytvorenie povrchovej siete

Podobne vytvorte geometriu stola, vygenerujte povrchovú sieť a priraďte materiál pre zadnú aj prednú stranu stola, ako je uvedené v 2.9.2

### Definícia pohybu posunovacieho objektu

Na stránke pohybu posunovača definujte smer objektu posunovača ako* * -X * * smer a konštantnú rýchlosť ako **340 mm/s**, ako je znázornené na obr. L2.35.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0036.jpg' | relative_url }})

Definícia pohybu posunovača

### Definícia plánovaného polohovania

Na stránke plánovania polohy vyberte prvý vzťah a kliknite na tlačidlo upraviť, potom zmeňte **referenčný objekt** ako **Top* ** roll * * od prvého stretnutia a použite predvolený smer priblíženia ako * * -X. * * kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), ako je znázornené na obr. L2.36.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0037.jpg' | relative_url }})

Definícia polohovania harmonogramu

### Stránka ovládacích prvkov simulácie

V ovládacích prvkoch simulácie prepnite do režimu vedenia kliknutím na ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) , po kliknutí na tlačidlo Použiť na všetky prechody v ovládacích prvkoch simulácie valivej skupiny, pre každý prechod bude predvolene definovaný normálny smer v závislosti od stavu začiarkavacieho políčka spätného valenia. Pre tento prechod by mal byť normálny smer **-X smer**, ako je znázornené na obr. L2.37. Vyberte operáciu Rolling Pass 3 v editore operácií kliknutím na dlaždicu operácie a upravte nastavenia funkcie Pass 3.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0038.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie

## Úprava operácie Rolling pass 3 (Pass 3)

V priechode 3 máme dva stojany. Budeme používať stoly vpredu a vzadu pre stojan 1, takže zapnite začiarkavacie políčka * * Table back * * a * * Table * ***front** stojana 1, ako je znázornené na obr. L2.38. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku RollStand1 Top Roll Mesh.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0039.jpg' | relative_url }})

Stôl stojana pre preukaz 3

### Vytvorenie geometrie stola a vytvorenie povrchovej siete

Na zadnej strane tabuľky akceptujte predvolenú teplotu 20C a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku geometrie. Na stránke geometrie zadnej strany stola vyberte ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a definujte parametre uvedené nižšie pre geometriu zadnej strany stola.
Východiskový bod X = -30 mm
Šírka W = 60 mm
Výška H = 5 mm
Dĺžka = 750 mm

Začiarknite políčko „Zarovnať k hornej časti spodného valca pre valcovanie pásov“
Pass Line = 5 mm.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vytvoríte tabuľku a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte primitívnu stránku Tabuľka/Vodiaca geometria a kliknete na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Sieť.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0040.jpg' | relative_url }})

Vytvorenie geometrie zadnej tabuľky

  
Na stránke povrchovej siete prepnite do expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), potom definujte počet vrstiev s jednotnou hrúbkou ako * * 5 * * a ponechajte zvyšok nastavení tehlovej siete ako predvolené. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujete povrchovú sieť pre tabuľku, ako je znázornené na obr. L2.27.
  
Priraďte materiál „**AISI-H-13* * “ pre zadný objekt stola z okna materiálu. Dá sa to urobiť tak, ako je znázornené na obr. L2.28. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po prednú stranu tabuľky.
  
Podobne definujte prednú stranu stola ako zadnú stranu stola s rovnakými nastaveniami pre geometriu, povrchovú sieť a materiál.

### Definovanie ovládacích prvkov pohybu pre kotúče stand2

V prípade kotúčov je sieťka už vygenerovaná a materiál je priradený tak, že kliknete na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránke pohybu. Prepnite do riadeného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), potom definujte typ otáčania ako „* * Krútiaci moment * * “ s konštantou **0** **N-mm**, ako je znázornené na obr. L2.40.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0041.jpg' | relative_url }})

Stránka pohybu horného kotúča stojana 2

Podobne definujte ovládacie prvky pohybu aj pre spodný valec.

### Definícia pohybu posunovacieho objektu

Na stránke pohybu posunovača prepnite do expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), potom definujte smer objektu posunovača ako * * X ** * smer * * a konštantnú ** rýchlosť ** ako ** 340 mm * ***/s**, ako je znázornené na obr. L2.41.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0042.jpg' | relative_url }})

Stránka pohybu objektu posunovača pre prechod 3

### Definícia plánovaného polohovania

Na stránke plánovania umiestnenia vyberte prvú reláciu a kliknite na tlačidlo upraviť, potom zmeňte **referenčný objekt** ako **2 - Top roll** stojana rolky 1 od prvého stretnutia a použite predvolený smer priblíženia ako **X**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), ako je znázornené na obr. L2.42.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0043.jpg' | relative_url }})

Definícia polohovania harmonogramu

### Stránka ovládacích prvkov simulácie

V ovládacích prvkoch simulácie prepnite do režimu vedenia kliknutím na ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), v predvolenom nastavení, keď klikneme na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_passes_button.jpg' | relative_url }}) v ovládacích prvkoch simulácie valivých skupín pre každý prechod, normálny smer bude predvolene definovaný v závislosti od smeru valenia. Pri prechode by normálny smer mal byť **X smer**. Vyberte operáciu Rolling Pass 4 v editore operácií kliknutím na dlaždicu operácie a upravte nastavenia funkcie Pass 4.

## Úprava operácie Rolling pass 4 (Pass 4)

V Pass 4 máme dva stojany. Budeme používať tabuľky vpredu a vzadu pre stojan 1, takže zapnite začiarkavacie políčka Tabuľka vzadu a Tabuľka pred stojanom 1 podobne, ako je znázornené na obr. L2.39. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Tabuľka (späť).

### Vytvorenie geometrie stola a vytvorenie povrchovej siete

Podobne vytvorte geometriu stola, vygenerujte povrchovú sieť a priraďte materiál pre zadnú aj prednú stranu stola, ako je uvedené v 2.11.1.

### Definovanie ovládacích prvkov pohybu pre kotúče stand2

Keďže sieť je už vygenerovaná a materiál je priradený pre kotúče, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku pohybu. Typ otáčania definujte ako „**Krútiaci moment** “ s konštantou **0N-mm* * podobne ako 2.11.3. pre horný aj dolný valec.

### Definícia pohybu posunovacieho objektu

Na stránke pohybu posunovača, podobne ako v bode 2.10.2., definujte smer objektu posunovača ako **-X smer** a konštantnú rýchlosť ako **340 mm****/s**.

### Definícia plánovaného polohovania

Podobne ako v bode 2.10.3 na stránke plánovania polohy vyberte prvú reláciu a kliknite na tlačidlo upraviť, potom zmeňte **referenčný objekt** ako **2 - Top roll** stojana rolky 1 od prvého stretnutia a použite predvolený smer priblíženia ako **-X**.

### Stránka ovládacích prvkov simulácie

V ovládacích prvkoch simulácie prepnite do režimu vedenia kliknutím na ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), v predvolenom nastavení, keď klikneme na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_passes_button.jpg' | relative_url }}) v ovládacích prvkoch simulácie valivých skupín pre každý prechod, normálny smer bude predvolene definovaný v závislosti od smeru valenia. Pri tomto prechode by mal byť * * normálny * * smer **-X smer** a mal by sa použiť predvolený bod zastavenia roviny.

## Simulácia behu

Po vygenerovaní databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad operačným stromom. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. L2.43. Použite predvolenú možnosť **Pokračovať*** * Spustiť * * a vyberte možnosť „**Pokračovať z posledného kroku** “ (z kroku -1) a potom vyberte režim simulácie ako prepínač * * Interaktívne * *. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) pre spustenie simulácie.

Ak chcete definovať nastavenia MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}), okno Možnosti spustenia sa rozbalí a zobrazí možnosti definovania nastavení MPI pre simuláciu (maximálny počet procesorov, ktoré možno definovať v závislosti od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0044.jpg' | relative_url }})

Spustiť vyskakovacie okno simulácie.

  
Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces valcovania, pretože simulácia prebieha z grafiky simulácie
  
Simulácia sa zastaví po dosiahnutí stabilného stavu s nižšie uvedenou správou v súbore správy.

„PROGRAM ZASTAVENÝ!
Rovina zastavenia: Všetky uzly objektu 1 opustili matricu/valcovanie.“

Postprocessing

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), otvorí sa postprocesor MO (ako je znázornené na obr. L2.44.).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0045.jpg' | relative_url }})

Režim MO Post po dokončení simulácie.

Prejdite na posledný krok, zakreslite **Efektívne napätie** a **Teplota** stavové premenné a sledujte rozdelenie stavových premenných.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0046.jpg' | relative_url }})

Efektívne rozloženie napätia

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab2/image0047.jpg' | relative_url }})

Rozloženie teploty
