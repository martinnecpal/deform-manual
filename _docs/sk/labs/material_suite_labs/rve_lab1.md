---
lang: sk
title: "RVE Lab1"
---

# RVE Lab1: Model RVE s hybridnou spodnou konštrukciou

  
1.1. Úvod do modelu RVE

1.2. Spustenie modelu RVE v Material Suite

1.3. Výber objektu a výber bodu

1.4. Nastavenie modelu RVE

1.4.1. Definovanie rozmeru modelu RVE

1.4.2. Definovanie materiálov pre model RVE

1.4.3. Definovanie modelu RVE

1.4.4. Generovanie povrchovej siete pre model RVE

1.4.5. Definovanie nastavení inklúzie

1.4.6. Generovanie databázy na simuláciu modelu RVE

1.5. Spustiť simuláciu modelu RVE

1.6. Výstup modelu RVE

## Úvod do modelu RVE

Modely reprezentatívnych objemových prvkov (RVE) v mikroúrovni prostredníctvom bodového sledovania danej databázy. Pomocou modelu RVE môžeme študovať podrobnú mikroúrovňovú odozvu (lokálne napätie a deformácia, defekty/interakcia matrice, uzavretie dutiny), hodnotenie mikroštruktúry (veľkosť častíc, objemová frakcia, orientácia tvaru atď.), hodnotenie textúr atď.

V tomto laboratóriu ukážeme, ako využiť možnosť RVE na modelovanie RVE s hybridnou spodnou konštrukciou s jednou prázdnou a dvoma inklúziami.

## Spustiť model RVE v Material suite

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI.
  
Požadujeme nominálnu DB na vykonanie modelu RVE v súbore materiálov, pre toto laboratórium použijeme Forging_2D_Nominal.key z priečinka **\2D\LABS\RVE_LABS** na generovanie nominálnej DB. Otvorte NG Pre (![]({{ '/assets/icons/pre_icons/2d_3d_pre_radio_button.jpg' | relative_url }})) Vytvorte nový problém buď výberom * *File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) * ***New Problem** alebo kliknutím na ikonu New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}), ako je znázornené na obr. RVEL1.1. Definujte názov problému ako "**Forging_2D_Nominal** " a "**System****International****(SI)** " unit System prepínač v okne New Problem, ako je znázornené na obr. RVEL1.1. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0001.jpg' | relative_url }})

Vytvorenie nového problému

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0002.jpg' | relative_url }})

NG Pre Nové okno problému

  
Ponechajte ID problému ako „**Forging_2D_Nomina** l“, zvoľte prepínač „**2D** “ Dimension a ponechajte prepínač „System International (SI)“ v okne New Problem (Nový problém), ako je znázornené na obr. RVEL1.2. Importujte „**Forging_2D_Nominal.key** “ z priečinka „**\2D\LABS\ RVE_LABS** “ pomocou „Import Keyfile“ z ponuky Súbor v NG Pre, ako je znázornené na obr. RVEL1.3.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0003.jpg' | relative_url }})

Importovanie súboru kľúčov Forging_2D_Nominal pomocou možnosti Importovať súbor kľúčov

Prejdite na stránku Generate DB (Vygenerovať databázu) a kliknite na „ Generate Database “ (Vygenerovať databázu), aby ste vygenerovali databázu a zatvorili NG Pre Spustite simuláciu z hlavného grafického rozhrania, uistite sa, že simulácia sa zastaví normálne bez akéhokoľvek problému. Teraz z hlavného grafického rozhrania kliknite na **Material Suite** v časti „Post Processor“ a otvorte modul Material Suite.

  
Po otvorení hlavného okna pre balík materiálov kliknite na ikonu "Otvoriť..." ( ![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }})) v hornom paneli nástrojov a importujte databázu simulovanú vyššie (**Forging_2D_Nominal.DB**). Do stromu úloh sa pridá predvolená položka úlohy „DEFORMOVAŤ“. Rozbaľte položku „**Mikroštruktúra** “, ako je znázornené na obr. RVEL1.4. a kliknutím na ikonu „Model RVE“ sa do stromu úloh pridá nová položka úlohy „Model RVE“.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0004.jpg' | relative_url }})

Spustenie modelu RVE v Material Suite

## Výber objektu a výber bodu

Prejdite na posledný krok a zakreslite premennú Efektívny stav deformácie, ako je znázornené na obr. RVEL1.5.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0005.jpg' | relative_url }})

Efektívna deformačná krivka v poslednom uloženom kroku

V strome úloh „DEFORMOVAŤ“ kliknite na položku „** Výber objektu ** “ a vyberte položku „obrobok“ (pozri obr. RVEL1.6.). Kliknite na položku „* * Výber bodu * * “, pretože sme už vybrali posledný krok, číslo kroku bude „100“ v poli číslo kroku (pozri obr. RVEL1.7.). Definujte dva body na obrobku, ako je znázornené na obr. RVEL1.7. Súradnica bodu 1 (P1) je (20.5721, 75.4728, 0, 1) a súradnica bodu 2 (P2) je (131.923, 142.717, 0, 1). Používatelia si môžu vybrať ľubovoľné číslo kroku, ktoré im vyhovuje.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0006.jpg' | relative_url }})

Object Selection

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0007.jpg' | relative_url }})

Výber bodu na obrobku

## Nastavenie modelu RVE

Kliknite na položku „**Config** “, zobrazí sa jej okno s údajmi. Musíme špecifikovať spustiteľný súbor pre simuláciu FEM a pracovný adresár pomocou tlačidla ![]({{ '/assets/icons/post_icons/mo_import_button.jpg' | relative_url }}) susediaceho s poľom. Predvolený spustiteľný súbor pre simuláciu modelu RVE je „DEF_SIMULATION.EXE“, ktorý je v inštalačnom adresári DEFORMAČNÉHO softvéru. Adresár obsahujúci nominálnu databázu je nastavený ako Pracovný adresár, ako je znázornené na obr. RVEL1.8.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0008.jpg' | relative_url }})

Nastavenia konfigurácie modelu RVE

### Definovanie rozmeru modelu RVE

Kliknite na položku „** Rozmer modelu RVE** “ pod stromom úloh modelu RVE, vyberte rozmer modelu RVE ako „2D“, ako je znázornené na obr. RVEL1.9. Pomocou možnosti „Importovať projekt“ môžeme importovať predtým uložený projekt modelu RVE a pomocou možnosti „Uložiť projekt“ môžeme uložiť projekt modelu RVE.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0009.jpg' | relative_url }})

Výber rozmeru modelu RVE

### Definovanie materiálov pre model RVE

Kliknite na položku "RVE model Materials" pod RVE model Task Tree, prvý materiál uvedený v zozname je materiál obrobku v nominálnej databáze. V tomto laboratóriu importujeme dva inkluzívne materiály, dvakrát kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (tlačidlo Pridať), do zoznamu sa pridajú dva „Nové materiály“, v zozname vyberte prvý „Nový materiál“ a importujte „* * Material_Al2O3.key * * “ z priečinka „2D\LABS\ RVE_LABS“ pomocou ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})option a vyberte materiál „Al2O3“. Podobne vyberte iný „Nový materiál“ v zozname a importujte „**Material_MnS.key ** “ z priečinka „2D\LABS\ RVE_LABS“ a vyberte materiál „MnS“. Po načítaní materiálov vyzerá stránka Modelové materiály RVE, ako je znázornené na obr. 10. Môžeme tiež importovať materiálové údaje z knižnice pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), uložiť materiál pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a môžeme tiež upraviť materiál pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0010.jpg' | relative_url }})

Načítanie materiálov potrebných pre model RVE

### Definovanie modelu RVE

Kliknite na položku „** Nastavenie modelu RVE** “ pod stromom úloh modelu RVE, tu môžeme vytvoriť geometriu modelu RVE pomocou primitívnej možnosti (2D kruhová vnútorná medzera, 2D vnútorná medzera elipsy a 2D polotuhá povrchová medzera) alebo pomocou možnosti modelu RVE definovanej používateľom 2D.

V rámci možnosti modelu RVE definovaného používateľom 2D môžeme importovať geometriu pre Matrix a pre Substructure zo súboru geometrie alebo zo súboru kľúčov pomocou tlačidla „Importovať model RVE integrovaný používateľom zo súboru“.

V časti Subštruktúra máme nasledujúce možnosti:

* **Importovať** tlačidlo geometrického súboru - pre import geometrie subštruktúry zo súboru.

* **Preklad** \- Preloží vybranú geometriu na hodnotu súradnice prekladu.

* **Rotácia** – Otočí vybranú geometriu na základe definovaných údajov osi rotácie a uhla rotácie (stupňov).

* **Mierka** \- Zmení mierku vybranej geometrie na základe faktora mierky v smere X a Y.

* **Duplikovať** \- Môžeme duplikovať vybranú geometriu a umiestniť duplikovanú geometriu na základe prekladu po duplicitných údajoch.

* **Odstrániť** \- Odstráni vybranú geometriu v zozname.

* **Submodel* * \- Môžeme definovať údaje roviny lomu RVE pre vybranú geometriu a vygenerovať mozaikovanie vo vybranej geometrii. Táto možnosť nebude aktívna pre neplatné položky.

V tomto laboratóriu vytvárame tri podštruktúry pomocou kruhu s polomerom 0,01mm z importovanej geometrie. Na stránke „Nastavenie modelu RVE“ vyberte „**2D model RVE definovaný používateľom ** “, zadajte veľkosť modelu RVE (L) ako 0,2 a importujte súbor „Rve_InclusionGeo_CR001.geo“ z priečinka 2D\LABS\ RVE_LABS pomocou možnosti Import, ako je znázornené na obr. RVEL1.11., bude to geometria **centrálnej spodnej konštrukcie**. Importovaná geometria centrálnej spodnej konštrukcie s modelom RVE bude vyzerať tak, ako je znázornené na obr. RVEL1.11.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0011.jpg' | relative_url }})

Model RVE s centrálnou spodnou konštrukciou

* Ak chcete vytvoriť**ľavú subštruktúru** , pomocou možnosti „* * Duplikovať * * “ duplikujte geometriu centrálnej subštruktúry a umiestnite ju na X=-0,05, Y=0 pomocou „Prekladu“, ako je znázornené na obr. RVEL1.12. Škálujte duplikovanú podkladovú štruktúru pomocou možnosti „**Scale** “ s FX=2 a FY=0,5 faktorov mierky, ako je znázornené na obr. RVEL1.12.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0012.jpg' | relative_url }})

Vytvorenie geometrie ľavej podštruktúry

* Podobne vytvoríme **pravú podštruktúru **. Pomocou možnosti „**Duplikovať** “ duplikujte geometriu centrálnej spodnej konštrukcie a umiestnite ju na X=0,05, Y=0 pomocou funkcie „Preklad“, ako je znázornené na obr. RVEL1.13 Mierka duplikovanej základnej štruktúry pomocou možnosti „**Mierka** “ s FX=0,5 a FY=2 faktory, ako je znázornené na obr. RVEL1.13

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0013.jpg' | relative_url }})

Vytvorenie správnej geometrie subštruktúry

* Materiál pre podštruktúry je možné definovať dvojitým kliknutím na bunku v stĺpci Materiál v tabuľke, ako je znázornené na obr. RVEL1.14. Nebudeme priraďovať materiál k centrálnej spodnej konštrukcii, preto sa bude považovať za „Žiadny (neplatný)“. Pre ľavú spodnú konštrukciu priraďte materiál „Al2O3“a pre pravú spodnú konštrukciu priraďte materiál „MnS“.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0014.jpg' | relative_url }})

Priradenie materiálu pre podštruktúry modelu RVE

### Generovanie povrchovej siete pre model RVE

Kliknite na položku „** povrchová sieť modelu RVE ** “ pod stromom úloh modelu RVE, budeme považovať podštruktúry za samostatné objekty, preto začiarknite políčko „Vytvoriť samostatné objekty inklúzií“. Pre **Maticu** definujte počet prvkov ako **2000** a pomer veľkosti ako **2** a pre **najmenšie zahrnutie** definujte počet prvkov ako 45 a pomer veľkosti ako 1. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujete povrchovú sieť, vygenerovanú sieť pre model RVE, ako je znázornené na obr. RVEL1.15.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0015.jpg' | relative_url }})

Nastavenia povrchovej siete pre inklúzie modelu RVE

### Definovanie nastavení inklúzie

Kliknite na položku „** Nastavenia zahrnutia ** “ pod stromom úloh modelu RVE. V tomto laboratóriu použijeme predvolené údaje o vzťahu kontaktu matice a inklúzie, typ kontaktu je "**Nelepivý ** " a typ trenia je "**Šmyk** " s koeficientom trenia **0,25 * *, ako je znázornené na obr. RVEL1.16.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0016.jpg' | relative_url }})

Definovanie nastavení inklúzie

### Generovanie databázy na simuláciu modelu RVE

Kliknite na položku „** generovanie modelu RVE DB ** “ pod stromom úloh modelu RVE, môžeme sledovať informácie o nastavení modelu RVE na stránke generovania modelu RVE DB. Kliknutím na tlačidlo **![]({{ '/assets/icons/post_icons/ms_generate_database_button.jpg' | relative_url }}) * * vygenerujete databázu na simuláciu modelu RVE. Po úspešnom vygenerovaní databázy môžeme pozorovať správu „Databázové súbory sú úspešne vygenerované pre všetky sledované body!“ v stavovom riadku (pozri obr. RVEL1.17.).

Po vygenerovaní databázy môžeme pozorovať, že v pracovnom adresári je vytvorený priečinok RVE_MODEL. Vo vnútri adresára RVE_MODEL sa vytvoria samostatné adresáre pre každý bod s „Bodom*“ obsahujúcim databázu modelu RVE spolu so súbormi .txt údajov sledovania bodu pre zložky napätia, strednú teplotu a premenné stavu gradientu rýchlosti.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0017.jpg' | relative_url }})

Stránka generovania databázy pre model RVE

## Simulácia modelu RVE

Kliknite na položku „* * Spustiť * * “ v strome úloh a kliknite na tlačidlo „* * Vypočítať * * “ v okne údajov na spustenie simulácie (pozri obr. RVEL1.18.).

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0018.jpg' | relative_url }})

Stránka spustenia modelu RVE

## RVE model Výstup

Po dokončení simulácie kliknite na položku „**Bod1** “ v časti „**Výstup** “ v strome úloh, prejdite na posledný krok a zakreslite premennú Efektívny stav deformácie (pozri obr. RVEL1.19). Môžeme prehrať animáciu, aby sme pozorovali správanie dutého uzavretia a inklúzie materiálu počas formovacej operácie. Na obr. RVEL1.20. je v prvom a poslednom kroku bodu 1 zobrazená prázdnota centrálnej spodnej konštrukcie.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0019.jpg' | relative_url }})

Point1 Výstup v poslednom kroku s premennou Effective Strain state

![]({{ '/assets/images/labs/material_suite_labs/rve_lab1/image0020.jpg' | relative_url }})

Centrálna spodná štruktúra bodu 1 je v prvom a poslednom kroku prázdna
