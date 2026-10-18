---
lang: sk
title: "2D DOE – laboratórna úloha č. 1"
---

# 2D DOE – Laboratórna práca č. 1

V tomto laboratórnom cvičení naimportujeme konfiguračný súbor „Multi Stand Drawing“ z laboratórnych cvičení z oblasti 2D a následne budeme pokračovať v simulácii nominálneho projektu a nastavení DOE.

1.1. Nastavenie a simulácia nominálneho projektu

1.2. Skontrolujte a definujte nominálny projekt

1.3. Pridať projekt DOE

1.4. Pridať variáciu geometrie matrice ako premennú DOE

1.5. Pridajte koeficient trenia ako premennú DOE

1.6. Skontrolujte tabuľku premenných DOE

1.7. Definícia vzoriek DOE

1.8. Definícia operácie „Výstup DOE“

1.8.1. Výber operácie DOE a predmetu štúdie

1.8.2. Definovanie výstupných premenných

1.9. Simulácia projektu DOE

1.10. Preskúmať výsledky testu DOE

1.10.1. Kontrola premenných min/max prevádzky (všetky kroky)

1.10.2. Skontrolujte premenné „Súhrn min/max“ (posledný krok)

1.10.3. Skontrolujte premenné špecifické pre danú lokalitu (jedno krokové)

## Nastavenie a simulácia nominálneho projektu

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. DOEL1.1. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Anglický**“. Názov úlohy zadajte ako „**DoeMultiStandDraw**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezakliknete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0001.jpg' | relative_url }})

Stránka „Nový problém“

  
Otvorí sa okno „Integrated Manufacturing Process“; v tomto momente bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V okne Nový projekt zadajte Názov problému ako „**DoeMultiStandDraw**“, ako Prvú operáciu vyberte 2D tvarovanie a vyberte anglický systém jednotiek, ako je znázornené na obr. DOEL1.2. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pridajte projekt.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0002.jpg' | relative_url }})

Okno na vytvorenie nového projektu

  
  
Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Import DB/Keyfile) a naimportujte súbor **MultiStandDraw.key** zo zložky 2D/LABS v inštalačnom adresári, ako je znázornené na obr. DOEL1.3.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0003.jpg' | relative_url }})

Import súboru s nastaveniami projektu „Nominal“

  
Po importe súboru s kľúčom program MO zobrazí všetky objekty tak, ako je znázornené na obr. DOEL1.4.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0004.jpg' | relative_url }})

Rozloženie projektu MO po importe konfiguračného súboru s kľúčmi

## Skontrolujte a definujte nominálny projekt

Importovaný súbor kľúčov predstavuje nastavenie ťahania s viacerými stojanmi, ktoré obsahuje 2 stojany; matrice na každom stojane sú označené ako „Pass1 Die“ a „Pass2 Die“. Obrobok sa vťahuje do týchto matríc na vykonanie procesu ťahania, čo sa dosahuje pôsobením rýchlosti na obrobok.  
  
Z stromu operácií vyberte „Okrajové podmienky obrobku“, aby ste mohli sledovať okrajové podmienky rýchlosti obrobku definované na prednej strane, ktoré slúžia na ťahanie obrobku cez lisovacie formy, a pevnú rýchlosť na stredovej osi, ako je znázornené na obr. DOEL1.5.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0005.jpg' | relative_url }})

Okrajová podmienka rýchlosti na prednom konci obrobku

Podobne vyberte BCC s pevnou rýchlosťou X a sledujte pevnú rýchlosť stredovej čiary, ako je znázornené na obr. DOEL1.6.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0006.jpg' | relative_url }})

Okrajová podmienka rýchlosti osi obrobku

  
Keďže v rámci projektu DOE meníme priemer matrice Pass1, obrobok sa musí počas simulácií DOE polohovať vzhľadom na meniaci sa priemer geometrie matrice tak, aby dochádzalo k interferencii v smere –Y. Musíme teda naplánovať polohu obrobku vzhľadom na matricu.  
  
Kliknite na položku „Plánovaná poloha“ v prevádzkovom strome, aby ste definovali plánované umiestnenie obrobku vo vzťahu k forme Pass1. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), aby ste pridali definíciu naplánovaného polohovania (pozri obr. DOEL1.7.) a nastavili polohu obrobku vo vzťahu k forme Pass1 tak, aby nedošlo ku kolízii v smere –Y, ako je znázornené na obr. DOEL1.8.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0007.jpg' | relative_url }})

Plánované časové okno na polohovanie

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0008.jpg' | relative_url }})

Určenie polohy obrobku vzhľadom na formu Pass1

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte definíciu naplánovaného polohovania. V strome operácií vyberte položku „Kontakt“, aby ste si prezreli vzťah medzi objektmi „Matrice“ a „Obrobok“ a hodnotu koeficientu trenia. (Pozri obr. DOEL1.9.)

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0009.jpg' | relative_url }})

Okno vzťahov medzi objektmi

V strome operácií vyberte položku „Generate Database“ (Vygenerovať databázu). Keď otvoríte položku „Generate Database“, zobrazí sa vám v dôsledku naplánovaných údajov o polohovaní vyskakovacie okno s textom „**Apply scheduled Positioning**“ (Použiť naplánované polohovanie). V tomto okne kliknite na „**Yes**“ (Áno) a vygenerujte databázu. (Pozri obr. DOEL1.10.)

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0010.jpg' | relative_url }})

Okno na vytvorenie databázy

  
Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) MO Mode, aby ste spustili simuláciu. Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Run Options, ako je znázornené na obr. DOEL1.11. Použite predvolenú možnosť **Pokračovať v spustení**, vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0011.jpg' | relative_url }})

Spustiť okno simulácie

  
Po dokončení simulácie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) v režime MO, aby ste prehrali jednotlivé kroky a skontrolovali nominálnu simuláciu, ako je znázornené na obr. DOEL1.12.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0012.jpg' | relative_url }})

Režim nominálneho projektového príspevku DOE

## Pridať projekt DOE

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) v režime MO, aby ste pridali štúdiu DOE. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) (Pridať) v ľavom hornom rohu grafického okna a vyberte možnosť Pridať štúdiu DOE, ako je znázornené na obr. DOEL1.13.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0013.jpg' | relative_url }})

Pridanie projektu štúdie DOE

Projekt DOE bude pridaný spolu s operáciou spracovania výstupov DOE, ktorá je potrebná na analýzu výsledkov DOE, ako je znázornené na obr. DOEL1.14.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0014.jpg' | relative_url }})

Pridaný projekt štúdie Ministerstva energetiky (DOE)

## Pridať variáciu geometrie výlisku ako premennú DOE

Na pridanie premenných DOE vyberte operáciu „Tvarovanie“ v editore operácií. Ak chcete zmeniť priemer formy v prvom stánku, vyberte v strome operácií položku „Geometria formy Pass1“ a pridajte geometriu ako premennú DOE kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať premennú DOE), ako je znázornené na obr. DOEL1.15.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0015.jpg' | relative_url }})

Pridanie geometrie ako premennej DOE

Pomenujte premennú DOE ako „Dia“ a zvoľte počet vzoriek 2. Používateľ môže pridať popis definície premennej DOE. V tomto laboratórnom cvičení, keďže meníme vnútorný priemer v rozmedzí od 0,2 do 0,24, pridajte popis: „**Vnútorný****priemer sa mení od 0,2183 do 0,2 (dolná hranica) a 0,24 (horná hranica).**“, ako je znázornené na obr. DOEL1.16.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0016.jpg' | relative_url }})

Okno na definovanie premenných DOE

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_geometry_button.jpg' | relative_url }}), aby ste definovali geometriu dolnej a hornej hranice. V 2D geometrickom editore skontrolujte, či je typ DOE nastavený na **Dolná**. (Pozri obr. DOEL1.17.)

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0017.jpg' | relative_url }})

Okno editora geometrie 2D DOE

  
Kliknite na kartu **Geometria** a v stĺpci X tabuľky si všimnite vnútornú plochú oblasť s priemerom 0,2183. Vyberte bod s najmenším priemerom, kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_move.jpg' | relative_url }}) (Presunúť) a presuňte bod o (-0,0183; 0), ako je znázornené na obr. DOEL1.18.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0018.jpg' | relative_url }})

Posunutie bodov vnútorného priemeru pre geometriu s dolnou hranicou

Podobne posuňte druhý koniec plochého hrotu o 0,0183 in smerom k osi, ako je znázornené na obr. DOEL1.19.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0019.jpg' | relative_url }})

Posun 2. dia s plochou špičkou

Aby sa zachoval rovnaký uhol vstupu a výstupu matrice, posuňte koncové body horného a dolného zúženého okraja o rovnakú vzdialenosť smerom k stredovej osi. Geometria dolnej hranice a tabuľka geometrie nakoniec vyzerajú tak, ako je znázornené na obr. DOEL1.20.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0020.jpg' | relative_url }})

Geometria dolnej hranice

  
Vyberte kartu „Objekty“, aby ste definovali hornú hranicu geometrickej premennej DOE, a ako je znázornené na obr. DOEL1.21, ako typ DOE vyberte možnosť **Horná**.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0021.jpg' | relative_url }})

Výber premennej geometrie s hornou hranicou

Znovu vyberte kartu „Geometria“ a posuňte body vnútorného plochého priemeru o 0,0217 od stredovej osi, aby sa priemer zmenil z 0,2183 na 0,24, ako je znázornené na obr. DOEL1.22.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0022.jpg' | relative_url }})

Posúvanie bodov vnútornej plochého priemeru v hornej hranici

  
Podobne ako v prípade koncových bodov rovnej hrany posuňte horné a dolné koncové body zúženej hrany o rovnakú vzdialenosť od stredovej čiary, aby sa zachoval rovnaký uhol vstupu a výstupu z lisovacej formy. Geometria hornej hranice a tabuľka geometrie nakoniec vyzerajú tak, ako je znázornené na obr. DOEL1.23.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0023.jpg' | relative_url }})

Horná hranica konečných bodov geometrie

Kliknite na kartu „Objekty“ a posuňte posuvník „Morph“, aby ste mohli sledovať prechod zmeny geometrie od dolnej po hornú hranicu, ako je znázornené na obr. DOEL1.24.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0024.jpg' | relative_url }})

Premenená geometria medzi definovanými variantmi geometrie

  
Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili 2D geometrický editor, a opäť kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili definíciu premennej DOE geometrie pre matricu Pass1. Všimnite si zelené sfarbenie okolo tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (upraviť geometriu) (pozri obr. DOEL1.25.), ktoré označuje, že premenná DOE bola úspešne definovaná. Ak definícia obsahuje chyby, okolo poľa premenných DOE sa zobrazí červené sfarbenie.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0025.jpg' | relative_url }})

Okno „Geometria“ po definovaní premenných DOE

## Pridať koeficient trenia ako premennú DOE

V prevádzkovom strome vyberte položku **Kontakt**, aby ste ako druhú premennú DOE definovali koeficient trenia medzi matricou Pass2 a obrobkom. (Pozri obr. DOEL1.26.)

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0026.jpg' | relative_url }})

Okno definície objektu Inter

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) pre vzťah medzi formou Pass2 a obrobkom (pozri obr. DOEL1.26.). Kliknite pravým tlačidlom na pole s konštantou trenia a pridajte ho ako premennú DOE, ako je znázornené na obr. DOEL1.27.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0027.jpg' | relative_url }})

Vzťahy medzi objektmi – okno úprav – karta „Deformácia“

  
Otvorí sa okno na definovanie premennej DOE (pozri obr. DOEL1.28.). Pomenujte premennú DOE ako „**Trenie**“, počet vzoriek nastavte na 2, hornú hodnotu definujte ako 0,084 a dolnú hodnotu ako 0,076, ako je znázornené na obr. DOEL1.28. K tejto premennej pridáme popis: „**Koeficient trenia sa menil o 5 percent nad a pod nominálnou hodnotou.**“.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0028.jpg' | relative_url }})

Okno s definíciou premennej koeficientu trenia v programe DOE

Overte, či definícia premennej DOE neobsahuje žiadnu chybu – to spoznáte podľa zelenej farby okolo poľa s hodnotou koeficientu trenia, ako je znázornené na obr. DOEL1.29.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0029.jpg' | relative_url }})

Karta „Deformácia“ v okne úpravy objektu Inter po definovaní premenných DOE

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte okno „Edit Inter-Object definition“.

## Skontrolujte tabuľku premenných DOE

Vyberte tabuľku „Premenné DOE“, aby ste si prezreli zoznam definovaných premenných DOE (pozri obr. DOEL1.30.). Používateľ môže definíciu premenných DOE ľahko upravovať v tabuľke „Premenné DOE“ – v prípade konštantných hodnôt stačí na ne dvakrát kliknúť. Hodnoty funkcií je možné upravovať kliknutím na jediné tlačidlo „Upraviť“ pod stĺpcom „Horná hodnota“.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0030.jpg' | relative_url }})

Zoznam premenných DOE v okne premenných DOE

## Definícia vzoriek DOE

Vyberte kartu „DOE Sampling“ (Odber vzoriek DOE), ako metódu odberu vzoriek zvoľte **Full Factorial** a všimnite si celkový počet simulácií uvedený vedľa nej, ako je znázornené na obr. DOEL1.31. V tomto laboratórnom cvičení je počet vzoriek pre obe premenné DOE 2, takže celkový počet behov/simulácií DOE je 4 (2x2).

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0031.jpg' | relative_url }})

Okno na odber vzoriek DOE

## Definícia operácie „DOE Output“

### Vyberte prevádzku DOE a objekt, ktorý sa má skúmať

V editore operácií vyberte operáciu výstupu DOE a v okne výberu operácií zaškrtnite políčko „tvarovacia operácia“ (pozri obr. DOEL1.32.). Ak projekt „Nominal“ obsahuje viac ako jednu operáciu a premenné DOE sú definované pre viac ako jednu operáciu, používateľ môže na analýzu vybrať obe operácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte typy výstupov.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0032.jpg' | relative_url }})

Okno výberu operácie

### Definovanie výstupných premenných

Skontrolujte výstupné typy „Minimálna/maximálna hodnota operácie“, „Miestna minimálna/maximálna hodnota“ a „SV“ na všetkých uzloch/prvkoch (posledný krok vybranej operácie) (pozri obr. DOEL1.33.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali oblasť záujmu.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0033.jpg' | relative_url }})

Okno výberu výstupu DOE

  
Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), aby ste pridali región, a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) (pozri obr. DOEL1.34.).

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0034.jpg' | relative_url }})

Okno „Zaujímavá oblasť“

Vytvorte primitív **dutý valec** s **polomerom** 1,1 a **výškou** 1,5 (pozri obr. DOEL1.35..). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) uzavrite definíciu geometrie. Kliknite na **P******osi** tioning **a nastavte **Offset** na (-0,1; -1), ako je znázornené na obr. DOEL1.36, a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0035.jpg' | relative_url }})

Vytvorenie geometrie sledovanej oblasti

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0036.jpg' | relative_url }})

Určenie polohy oblasti záujmu 

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre funkciu Min/Max (všetky kroky v operácii) a pridajte stavové premenné **Efektívne napätie** a **Efektívne deformácia**, ako je znázornené na obr. DOEL1.37. Ako minimálnu hodnotu zložky vyberte v okne Min/max možnosť **Max**, ako objekt vyberte **obrobok** a kliknite na **![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})**.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0037.jpg' | relative_url }})

Okno na definovanie výstupných premenných operácie Min/Max

  
Dvakrát kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}), aby ste v poslednom kroku operácie pridali **minimálne efektívne napätie** a **deformáciu** ako súhrnné premenné a **obrobok** ako objekt, ako je znázornené na obrázku [Fig. DOEL1.38.]({{ '/docs/sk/labs/doe_labs/2d_doe_lab/2d_doe_lab1/' | relative_url }}#Fig_DOEL1_38_Summary_Min/Max_variables_definition_window)

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0038.jpg' | relative_url }})

Okno s prehľadom definícií premenných Min/Max

  
Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a trikrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}), aby ste definovali 3 stavové premenné špecifické pre danú polohu. Pridajte stavové premenné **Efektívna deformácia**, **Efektívne napätie** a **Efektívna rýchlosť deformácie** a v dolnej časti okna vyberte spoločnú oblasť siete **REGION001**, ako je znázornené na obr. DOEL1.39.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0039.jpg' | relative_url }})

Okno na definovanie premenných špecifických pre danú polohu (všetky uzly)

  
Po výbere definovanej oblasti záujmu (Region of Interest) ako spoločnej oblasti siete (Common Mesh Region) sa vedľa nej zobrazí okno „Mesh“. Kliknite teda na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), čím sa vygeneruje sieť pre túto oblasť, ako je znázornené na obr. DOEL1.40.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0040.jpg' | relative_url }})

Okno na generovanie siete oblasti záujmu

  
Keďže nedefinujeme žiadne obmedzenia pre premenné a výplň, kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) (Uložiť projekt). Ak chce používateľ obmedziť hodnotu akejkoľvek stavovej premennej, môže definovať obmedzenia pre premenné; ak potrebuje filtrovať deformácie spôsobené nedostatočnou výplňou a prekrývaním, môže zaškrtnúť obmedzenia pre výplň.

Stlačte tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) MO, aby ste odoslali projekt DOE na simuláciu.

## Simulácia projektu DOE

Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) na spustenie simulácie. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím sa otvorí vyskakovacie okno „Run DOE/OPT“ (pozri obr. DOEL1.41.), a vyberte simulačný server zo zoznamu dostupných simulačných serverov. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) (pozri obr. DOEL1.42.), čím spustíte generovanie databázy vzoriek DOE a simulácie. Systém vygeneruje databázu pre všetky behy a následne začne simulovať od **behu 1** po **beh N** (posledný beh) v poradí. Ak používateľ zvolil viac ako jednu **súbežnú simuláciu**, potom sa vybraný počet simulácií spustí súbežne.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0041.jpg' | relative_url }})

Simulácie DOE – Okno spustenia

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0042.jpg' | relative_url }})

Simulácie DOE – Okno spustenia

  
Sledujte kartu „Simulation Jobs“ (Simulačné úlohy), kde môžete sledovať stav prebiehajúcich úloh DOE, ako je znázornené na obr. DOEL1.43.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0043.jpg' | relative_url }})

DOE – stav simulačných úloh

  
Vyberte súbor protokolu DOE, aby ste mohli sledovať podrobnosti o úlohách spustených v DOE, ako je znázornené na obr. DOEL1.44.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0044.jpg' | relative_url }})

Podrobnosti o záznamoch úloh DOE

  
V hlavnom okne prehliadača grafického používateľského rozhrania programu DEFORM si používateľ môže prezrieť štruktúru súborov projektov DOE, ako je znázornené na obr. DOEL1.45.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0045.jpg' | relative_url }})

Štruktúra súborov projektu DOE

Overte, či sa simulácia DOE vykonala, podľa správy „Simulácia je dokončená“ na karte „Protokol DOE“, a potom kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) MO, aby sa otvoril výstup DOE.

## Prehľad výsledkov DOE

V programe MO Post kliknite na tlačidlo na otvorenie súboru databázy DOE SQL (SDB) v programe DOE Post, keďže program MO Post neposkytuje funkcie na štatistickú analýzu výsledkov DOE. Program DOE Post sa otvorí v samostatnom okne, ako je znázornené na obr. DOEL1.46.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0046.jpg' | relative_url }})

Príspevok DOE

  
V grafickom okne sa zobrazí tabuľkový pohľad. V oblasti okna vlastností môžeme zaškrtnúť príslušné políčka, ktoré sa majú v tabuľkovom pohľade zobraziť (Vstupy DOE a Výstupy DOE).

### Skontrolujte premenné min/max operácie (všetky kroky)

Vo výstupnom strome vyberte premennú „Operation Min/Max“ a kliknite na zobrazenie tabuľky ![]({{ '/assets/icons/post_icons/doe_post_table_view.jpg' | relative_url }}). Všetky behy DOE majú globálne minimálne hodnoty rovné nule, takže nie je potrebné vykresľovať ďalšie krivky.

V tabuľkovom zobrazení pre geometriu Diameter DOE hodnota Dia 0 označuje dolnú hranicu geometrie a hodnota 1 hornú hranicu geometrie. Keďže sme odobrali len 2 vzorky, medzi dolnou a hornou hranicou neexistuje žiadna geometrická odchýlka. V takomto prípade sa zobrazí hodnota podielu; ak je väčšia ako 0,5, znamená to, že hodnota sa nachádza medzi nominálnou hodnotou a hornou hranicou.

### Skontrolujte premenné „súhrn min/max“ (posledný krok)

Vyberte položku „Súhrnné efektívne napätie“ a kliknite na ikonu ![]({{ '/assets/icons/post_icons/doe_post_response surface_button.jpg' | relative_url }}) (3D graf odozvy), aby ste si prezreli 3D znázornenie tejto odozvy pre vstupné premenné DOE. (Pozri obr. DOEL1.47.)

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0047.jpg' | relative_url }})

Súhrnná odozva povrchu odozvy pre minimálne efektívne deformácie

Kliknite na ![]({{ '/assets/icons/post_icons/doe_post_response_contour_button.jpg' | relative_url }}) (2D povrch odozvy) a zobrazíte odozvu vybraných výstupných premenných v 2D rovine, ako je znázornené na obr. DOEL1.48. Z panela nástrojov vyberte tlačidlo ![]({{ '/assets/icons/post_icons/doe_post_change_layout_icon.jpg' | relative_url }}) Zmeniť rozloženie a vyberte „Grid4_1“, čím rozdelíte grafickú oblasť rovnomerne medzi všetky 4 okná, ako je znázornené na obr. DOEL1.48.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0048.jpg' | relative_url }})

2D kontúrová odozvová plocha pre minimálne efektívne napätie

Vyskúšajte tiež grafy typu „tornádo“, citlivosti, rozptylu a histogramu na analýzu výstupnej premennej „Minimálne efektívne napätie“. (Pozri obr. DOEL1.49.)

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0049.jpg' | relative_url }})

Grafy citlivosti premenných DOE pre súhrnnú premennú „Minimálne efektívne napätie“

  
**Tornádový graf** znázorňuje relatívnu veľkosť a smer vplyvu premenných DOE na vybranú výstupnú premennú. Na obr. DOEL1.49 je z tornádového grafu zrejmé, že v poslednom kroku má priemer väčší vplyv na minimálne efektívne napätie v porovnaní s trením a že oba faktory pôsobia opačne.

**Graf citlivosti** znázorňuje vplyv každej vstupnej premennej štúdie DOE na vybranú výstupnú premennú vo forme sklonu krivky. V prípade minimálneho efektívneho napätia majú obe zmeny vstupných premenných opačný vplyv.

**Bodový graf** znázorňuje koreláciu medzi vstupnou premennou štúdie DOE a vybranou výstupnou premennou prostredníctvom lineárnej regresie. Na vyššie uvedenom obr. DOEL1.49 môžeme pozorovať rovnicu lineárnej regresie spolu s bodmi odberu vzoriek.

**Graf histogramu** znázorňuje frekvenciu výstupných premenných v jednotlivých pokusoch DOE v rámci malých rozsahov. Ide teda o stĺpcový graf, v ktorom je na jednej osi počet pokusov DOE a na druhej osi vybraná výstupná premenná.

### Skontrolujte premenné špecifické pre danú lokalitu (jedno krokové)

V stromovej štruktúre „DOE Output“ vyberte hodnotu efektívneho deformácie pre konkrétnu polohu. Ako je vysvetlené v časti „Summary variables“, skontrolujte grafy 3D a 2D odozvových plôch a sledujte odozvu výstupnej premennej pre vybraný vstup, ako je znázornené na obr. DOEL1.50. V prípade výstupnej premennej špecifickej pre danú polohu sa informácie o stavovej premennej vykreslia iba pre definovanú oblasť záujmu, ak sa nachádzame na karte „Spoločná sieť“, ako je znázornené na obr. DOEL1.50.

![]({{ '/assets/images/labs/doe_labs/2d_doe_labs/2d_doe_lab1/image0050.jpg' | relative_url }})

3D a 2D graf odozvy povrchu pre efektívne deformácie v konkrétnych miestach

Ďalšie informácie o týchto funkciách na analýzu záznamov nájdete v kapitole [54\. DOE Post Processor]({{ '/docs/sk/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/' | relative_url }}).

  
**Súvisiace témy:**

****[52.1. DOE and DOE Output Operation Setup]({{ '/docs/sk/doe_and_optimization/52_doe_study/52_1_doe_and_doe_output_operation_setup/' | relative_url }})

[52.2. DOE Simulation Running and Monitoring]({{ '/docs/sk/doe_and_optimization/52_doe_study/52_2_doe_simulation_running_and_monitoring/' | relative_url }})

[54.1. DOE Post Processor]({{ '/docs/sk/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/' | relative_url }})
