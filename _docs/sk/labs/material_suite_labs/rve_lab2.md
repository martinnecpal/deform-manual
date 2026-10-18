---
lang: sk
title: "RVE Lab2"
---

# RVE Lab2 : Model RVE pre zlomeninu tvrdej inklúzie

2.1. Úvod do modelu RVE

2.2. Spustenie modelu RVE v Material suite

2.3. Výber objektu a výber bodu

2.4. Nastavenie modelu RVE

2.4.1. Definovanie rozmeru modelu RVE

2.4.2. Definovanie materiálov pre model RVE

2.4.3. Definovanie modelu RVE

2.4.4. Generovanie povrchovej siete pre model RVE

2.4.5. Definovanie nastavení inklúzie

2.4.6. Generovanie databázy na simuláciu modelu RVE

2.5. Simulácia modelu RVE

2.6. Výstup modelu RVE

## Úvod do modelu RVE

Modely reprezentatívnych objemových prvkov (RVE) v mikroúrovni prostredníctvom bodového sledovania danej databázy. Pomocou modelu RVE môžeme študovať podrobnú reakciu mikroúrovne (lokálne napätie a deformácia, defekty/interakcia matrice, uzavretie dutiny), hodnotenie mikroštruktúry (veľkosť častíc, objemová frakcia, orientácia tvaru atď.), hodnotenie textúr atď.

V tomto laboratóriu ukážeme, ako používať RVE na modelovanie zlomeniny tvrdej inklúzie.

## Spustiť model RVE v Material suite

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI.

Požadujeme nominálnu DB na vykonanie modelu RVE v súbore materiálov, pre toto laboratórium použijeme Forging_2D_Uniform.key zo zložky **\2D\LABS\RVE_LABS** na vygenerovanie nominálnej DB. Otvorte **NG Pre** (![]({{ '/assets/icons/pre_icons/2d_3d_pre_radio_button.jpg' | relative_url }})) a vytvorte nový problém buď výberom * * File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ** * ** New Problem * * alebo kliknutím na ikonu New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}), ako je znázornené na [Fig. RVEL2.1.]() Definujte názov problému ako „**Forging_2D_Uniform* *“ a „* * System ** * ** International ** * **(SI)* ** “ unit Systémové prepínacie tlačidlo v okne New Problem, ako je znázornené na [Fig. RVEL2.1.]() Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0001.jpg' | relative_url }})

Vytvorenie nového problému

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0002.jpg' | relative_url }})

NG Pre Nové okno problému

  
NG Pre GUI sa otvorí, ponechá ID problému ako tlačidlo „**Forging_2D_Uniform** “ a tlačidlo „**System International (SI) * * “ Unit System , zvoľte prepínač „* * 2D ** “ Dimension (Rozmer) v okne New Problem (Nový problém), ako je znázornené na obr. RVEL2.2. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) zatvorte dialógové okno Nový problém. Importujte „**Forging_2D_Uniform.ke** y“ z priečinka „**\2D\LABS\ RVE_LABS** “ pomocou „**Import Keyfile ** “ z ponuky Súbor v NG Pre, ako je znázornené na obr. RVEL2.3.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0003.jpg' | relative_url }})

Importovanie súboru kľúča Forging_2D_Uniform pomocou možnosti Importovať súbor kľúča

Prejdite na stránku Generate DB a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) pre vygenerovanie databázy. Zatvorte NG Pre a spustite simuláciu z GUI Main, uistite sa, že simulácia sa zastaví normálne bez akéhokoľvek problému. Teraz z hlavného grafického rozhrania bez výberu **Forging_2D_Uniform**.DB súbor kliknite na **Material* *** Suite * * v časti „Post Processor“ a otvorte modul Material Suite, ako je znázornené na obr. RVEL2.4.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0004.jpg' | relative_url }})

Otváracia sada materiálov z hlavného grafického rozhrania

  
Po otvorení hlavného okna pre balík materiálov kliknite na ikonu "Otvoriť..." **(![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}))** v hornom paneli nástrojov pre import databázy simulovanej vyššie (**Kovanie_2D_Uniform* ***.DB**). Do stromu úloh SA pridá predvolená položka úlohy „** deformácia * *“. Rozbaľte položku „**Mikroštruktúra** “ a kliknite na ikonu „**Model RVE** “ zo zoznamu Mikroštruktúra, ako je znázornené na obr. RVEL2.5., do stromu úloh sa pridá nová položka úlohy „RVE model“.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0005.jpg' | relative_url }})

Spustenie modelu RVE v Material Suite

## Výber objektu a výber bodu

V strome úloh „deformácia“ kliknite na položku „**O**** výber objektu ** “ a vyberte položku „**obrobok** “ (pozri obr. RVEL2.6.). Kliknite na položku „* * Bod ** ** výber * * “, pretože sme v prvom kroku pri načítaní DB, číslo kroku bude „-1“ v poli číslo kroku ( obr. RVEL2.7.). Definujte jeden bod na obrobku, ako je znázornené na obr. RVEL2.7. Súradnica bodu1 (* * P1 * *) je (61.6289, 129.55, 0, 1). Používatelia si môžu vybrať ľubovoľné číslo kroku, ktoré im vyhovuje.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0006.jpg' | relative_url }})

Výber objektu, ktorý sa má použiť na modelovanie RVE

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0007.jpg' | relative_url }})

Výber bodu na obrobku

## Nastavenie modelu RVE

Kliknite na položku „**Config** “ zo stromu úloh modelu RVE, zobrazí sa okno Configuration (Konfigurácia). Musíme špecifikovať spustiteľný súbor pre simuláciu FEM a pracovný adresár pomocou tlačidla ![]({{ '/assets/icons/post_icons/mo_import_button.jpg' | relative_url }}) susediaceho s poľom. Predvolený spustiteľný súbor pre simuláciu modelu RVE je „DEF_SIMULATION.EXE“, ktorý je v inštalačnom adresári DEFORMAČNÉHO softvéru. Adresár obsahujúci nominálnu databázu je nastavený ako Pracovný adresár, ako je znázornené na obr. RVEL2.8.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0008.jpg' | relative_url }})

Nastavenia konfigurácie modelu RVE

### Definovanie rozmeru modelu RVE

Kliknite na položku „** Rozmer modelu RVE** “ pod stromom úloh modelu RVE, vyberte rozmer modelu RVE ako „**2D** “, ako je znázornené na obr. RVEL2.9. Pomocou možnosti „* * Importovať projekt * * “ môžeme importovať predtým uložený projekt modelu RVE a pomocou možnosti „* * Uložiť projekt * * “ môžeme uložiť projekt modelu RVE.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0009.jpg' | relative_url }})

Výber rozmeru modelu RVE

### Definovanie materiálov pre model RVE

Kliknite na položku "** RVE model Materials * * " pod RVE model Task Tree, prvý materiál uvedený v zozname je materiál obrobku v nominálnej databáze. V tomto laboratóriu importujeme jeden inkluzívny materiál, kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (tlačidlo Pridať), do zoznamu sa pridá jeden „Nový materiál“, v zozname vyberte „Nový materiál“ a importujte „* * Hard_Inclusion_Material.key ** “ z priečinka „2D\LABS\ RVE_LABS“ pomocou možnosti Import ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}). V Matrix material (Steel) flow stress model z nominálneho DB je ![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/matrix_material_eq.jpg' | relative_url }}) a importovaný Hard inclusion material stress model je ![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/hard_inclusion_eq.jpg' | relative_url }}) . Po načítaní materiálov vyzerá stránka Modelové materiály RVE tak, ako je znázornené na obr. RVEL2.10. Môžeme tiež importovať materiálové údaje z knižnice pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), uložiť materiál pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a môžeme tiež upraviť materiál pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0010.jpg' | relative_url }})

Načítanie materiálu potrebného pre model RVE

### Definovanie modelu RVE

Kliknite na položku „** Nastavenie modelu RVE** “ pod stromom úloh modelu RVE, tu môžeme vytvoriť geometriu modelu RVE pomocou primitívnej možnosti (2D kruhová vnútorná medzera, 2D vnútorná medzera elipsy a 2D polotuhá povrchová medzera) alebo pomocou možnosti modelu RVE definovanej používateľom 2D.

V rámci možnosti modelu RVE definovaného používateľom 2D môžeme importovať geometriu pre Matrix a pre Substructure ako súbor geometrie alebo súbor kľúča pomocou tlačidla „Importovať model RVE integrovaný používateľom zo súboru“.

V časti Subštruktúra máme nasledujúce možnosti:

* **Importovať** tlačidlo geometrického súboru - pre import geometrie subštruktúry zo súboru.

* **Preklad** \- Preloží vybranú geometriu na súradnice prekladu.

* **Rotácia** – Otočí vybranú geometriu na základe definovaných údajov osi rotácie a uhla rotácie (stupňov).

* **Mierka** \- Zmení mierku vybranej geometrie na základe faktora mierky v smere X a Y.

* **Duplikovať** \- Môžeme duplikovať vybranú geometriu a umiestniť duplikovanú geometriu na základe prekladu.

* **Odstrániť** \- Odstráni vybranú geometriu v zozname.

* **Submodel* * \- Môžeme definovať údaje roviny lomu RVE pre vybranú geometriu a vygenerovať mozaikovanie vo vybranej geometrii. Táto možnosť nebude aktívna pre neplatné položky.

V tomto laboratóriu vytvárame tri podštruktúry pomocou možnosti Submodely. Na stránke „* * RVE *** * model * ** * Setup * * “ zvoľte „**2D****kruhový****vnútorný****prázdny** “, uveďte ** RVE *** *model*** *veľkosť** (**L * *) ako * * 1,5 * * a * *polomer(R)* * ako * * 0,1 * * to bude geometria centrálnej spodnej konštrukcie. Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/ms_rve_generate_geo_button.jpg' | relative_url }}), vytvorený model RVE bude vyzerať tak, ako je znázornené na obr. RVEL2.11.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0011.jpg' | relative_url }})

Geometria modelu RVE

Ak chcete vytvoriť submodely, vyberte Substructure Material ako „**Hard****Inclusion** “ pomocou rozbaľovacej ponuky, ako je znázornené na obr. RVEL2.11. a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button2.jpg' | relative_url }}), otvorí sa okno definície rovín zlomenín RVE. V rovinách zlomenín RVE máme dve možnosti na vytvorenie podštruktúr,

* **Podľa individuálnej roviny (čiary)** : pomocou tejto možnosti môžeme rozdeliť spodnú štruktúru na čiastkový model pomocou definovaných údajov o individuálnej rovine.

* ** Náhodnými semenami** : pomocou tejto možnosti môžeme vytvoriť pod model podľa definovaných údajov Seeds #.

Po definovaní údajov o rovine, keď používateľ klikne na tlačidlo ![]({{ '/assets/icons/post_icons/ms_tessellation_button.jpg' | relative_url }}), sa vytvorí geometria podštruktúry.

V tomto laboratóriu použijeme možnosť „**Podľa individuálnej roviny(čiary)** “ na vytvorenie submodelov. Vyberte prepínač „**Podľa individuálnej roviny(čiary)** “, dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a pridajte dve roviny. Pre **FP1** definujte bod 1 ako -0,04 (X), -0,2 (Y) a bod 2 ako -0,04 (X), 0,2 (Y). Podobne definujte bod 1 ako 0,04 (X), -0,2 (Y) a bod 2 ako 0,04 (X), 0,2 (Y) pre **FP2** a kliknutím na ![]({{ '/assets/icons/post_icons/ms_tessellation_button.jpg' | relative_url }}) vytvorte submodely. Vytvorené submodely budú tak, ako je znázornené na obr. RVEL2.12. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku Roviny zlomenín RVE.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0012.jpg' | relative_url }})

Vytvorenie geometrie podštruktúry RVE

### Generovanie povrchovej siete pre model RVE

Kliknite na položku „** Mriežka modelu RVE ** “ pod stromom úloh modelu RVE, budeme považovať podštruktúry za samostatné objekty, preto zapnite začiarkavacie políčko „**Vytvárať samostatné objekty inklúzií ** “. Pre **Maticu** definujte**počet* ** prvkov * * ako * * 5000 * * a ** pomer veľkosti*** * ako * * 2 * * a pre **najmenšie* ***začlenenie** definujte **počet prvkov* * ako * * 100 * * a pomer veľkosti ako **1**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujete povrchovú sieť, vygenerovanú sieť pre model RVE, ako je znázornené na obr. RVEL2.13.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0013.jpg' | relative_url }})

Nastavenia povrchovej siete pre inklúzie modelu RVE

### Definovanie nastavení inklúzie

Kliknite na položku „** Nastavenia zahrnutia ** “ pod stromom úloh modelu RVE. V **Matrix****-***zahrnutie** kontaktného vzťahu vyberte typ kontaktu ako „* * Nelepivý * * “ a typ trenia ako „* * Šmyk * * “ s koeficientom trenia * * 0,25 ** , potom vyberte kritériá separácie na základe tlaku ako „**Absolútna* ** hodnota * * “ a definujte absolútnu hodnotu ako* * 250 * *, ako je znázornené na obr. RVEL2.14. Podobne v **Zahrnutie-zahrnutie * * kontaktnom vzťahu vyberte typ trenia ako „* * Šmyk * * “ s koeficientom trenia * * 0,25 ** , vyberte kritériá separácie na základe tlaku ako „**Absolútna * ***hodnota * * “ a definujte absolútnu hodnotu ako **60 * *, ako je znázornené na obr. RVEL2.14.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0014.jpg' | relative_url }})

Definovanie nastavení inklúzie

### Generovanie databázy na simuláciu modelu RVE

Kliknite na položku „** generovanie modelu RVE DB ** “ pod stromom úloh modelu RVE, môžeme sledovať informácie o nastavení modelu RVE na stránke generovania modelu RVE DB. Kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/ms_generate_database_button.jpg' | relative_url }}) vygenerujete databázu na simuláciu modelu RVE. Po úspešnom vygenerovaní databázy môžeme pozorovať správu „Databázové súbory sú úspešne vygenerované pre všetky sledované body!“ v stavovom riadku (pozri obr. RVEL2.15).

Po vygenerovaní databázy môžeme pozorovať, že v pracovnom adresári je vytvorený priečinok RVE_MODEL. Vo vnútri adresára RVE_MODEL sa vytvoria samostatné adresáre pre každý bod s „Bodom *“ obsahujúcim databázu modelu RVE spolu so súbormi .txt údajov sledovania bodu pre zložky napätia, strednú teplotu a premenné stavu gradientu rýchlosti.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0015.jpg' | relative_url }})

Stránka generovania databázy pre model RVE

## Simulácia modelu RVE

Kliknite na položku „* * Spustiť * * “ v strome úloh a kliknite na tlačidlo „* * Vypočítať * * “ v okne údajov na spustenie simulácie (pozri obr. RVEL2.16.).

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0016.jpg' | relative_url }})

Stránka spustenia modelu RVE

## RVE model Výstup

Po dokončení simulácie kliknite na položku „**Bod1** “ v časti „**Výstup** “ v strome úloh, prejdite na posledný krok a zakreslite premennú Efektívny stav deformácie (pozri obr. RVEL2.17.). Animáciu môžeme prehrať a pozorovať lomové správanie materiálu počas tvárniacej operácie. Na obr. RVEL2.18. je znázornená lom submodelov v rôznych krokoch.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0017.jpg' | relative_url }})

Point1 Výstup v poslednom kroku s premennou Effective Strain state

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0018.jpg' | relative_url }})

Zlomenina bodu 1 s tvrdým začlenením v rôznych krokoch
