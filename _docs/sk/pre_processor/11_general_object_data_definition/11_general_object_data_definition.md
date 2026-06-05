---
lang: sk
title: "11. Definícia všeobecných údajov o objekte"
---

# 11\. Definícia všeobecných údajov o objekte

11.1. Stránka so zoznamom objektov

11.2. Názov objektu

11.3. Počiatočné podmienky objektu

11.4. Typ objektu

11.4.1. Plastové

11.4.2. Elastický

11.4.3. Elasto-plastické

11.4.4. Porézne

11.4.5. Pevná stránka

11.4.6. Hyper-elastické

11.4.7. Používateľom definované

11.4.8. Prostredie (Fluid(CFD))

11.4.9. Prostredie (vzduch (elektromagnetické))

11.5. Primárna matrica

11.6. Import objektu zo súboru

11.7. Import objektu z knižnice

11.8. Uloženie objektu do súboru

11.9. Uloženie objektu do knižnice

Strom objektov v Pre-procesore zobrazuje všetky aktuálne dostupné objekty. (Pozri obr. 11.1.) Údaje dostupných objektov možno ovládať výberom konkrétnej dátovej stránky pod objektom v Strome objektov. Po výbere dátovej stránky objektu, než v okne definície dát objektu obsahuje príslušné vybrané údaje, ako sú geometria, sieť, Materiál, okrajové podmienky, pohyb, počiatočné podmienky a numerické vlastnosti objektu špecifické pre daný objekt.

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image001.jpg' | relative_url }})

Preprocesor s oknom stromu objektov s červeným rámčekom

## Stránka zoznamu objektov

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image002.jpg' | relative_url }})

Stránka so zoznamom objektov

Ak chcete pridať objekt do stromu objektov, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}), ako je znázornené na obr. 11.2. Tým sa vloží nový objekt do prvého dostupného čísla objektu. Ak chcete odstrániť objekt, vyberte príslušný objekt a stlačte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}). Tým sa vymažú všetky položky súvisiace s vybraným objektom vrátane ovládacích prvkov pohybu, okrajových podmienok, medziobjektových okrajových podmienok atď.

Používateľ môže duplikovať existujúci objekt tak, že ho vyberie a klikne na ![]({{ '/assets/icons/pre_icons/mo_duplicate_object_button.jpg' | relative_url }}).

Pozíciu objektu v strome môžete zmeniť pomocou tlačidiel ![]({{ '/assets/icons/pre_icons/mo_move_object_down_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/mo_move_object_up_button.jpg' | relative_url }}).

Používateľ môže importovať objekt zo súboru s kľúčom alebo databázy pomocou ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), objekty sa pridajú do existujúceho zoznamu objektov.

Poznámka: Ak chcete nahradiť definíciu geometrie objektu bez odstránenia ovládacích prvkov pohybu a vzťahov medzi objektmi, je možné z okna geometrie odstrániť iba geometriu objektu. To je užitočné pri zmene geometrie výliskov pri vykonávaní dvoch alebo viacerých deformačných operácií na tom istom obrobku. Pri opätovnom definovaní objektu týmto spôsobom je mimoriadne dôležité inicializovať a regenerovať medziobjektové okrajové podmienky. Môže byť tiež potrebné vynulovať definíciu zdvihu v ovládacích prvkoch Pohyb na nulu.

## Názov objektu (OBJNAM)

Obrobok a každý kus nástroja musia byť identifikované ako jedinečný objekt a musí im byť pridelené číslo a názov objektu. (Pozri obr. 11.3.) Názov objektu ([OBJNAM](/docs/sk/keyword_documentation/o/objnam/)) je reťazec maximálne 64 znakov. Dôrazne sa odporúča, aby bol nastavený na niečo zmysluplné (napr. razník, matrica, obrobok).

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image003.jpg' | relative_url }})

Okno Definícia údajov 3D objektu

## Počiatočné podmienky objektu

Počiatočné podmienky je možné zadať pre akúkoľvek stavovú premennú súvisiacu s objektom v DEFORM. Najčastejšou špecifikáciou počiatočnej podmienky je teplota objektu, ktorú možno špecifikovať na príslušnej stránke objektu.

Pri problémoch tepelného spracovania s premenlivým obsahom uhlíka v obrobku sa môže špecifikovať aj dominantný obsah atómov. V prípade sieťovaných objektov sa počiatočná teplota objektu a počiatočný obsah dominantného atómu zadávajú priradením hodnôt všetkým uzlom výberom ikony Uzly objektu ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) (![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}))![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Difúzia na karte Objekt.  
Pri generovaní siete sa inicializujú hodnoty stavových premenných uzlov a prvkov na základe podmienok definovaných pre objekt.  
Jednotnú teplotu objektu je možné zadať v príslušnom okne objektu. Uzlové hodnoty možno zadať aj výberom ikony Objekt ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Uzly objektu (![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}))![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Teplotná karta. Hodnoty pre celý objekt možno nastaviť pomocou ikony inicializovať ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) vedľa príslušného dátového poľa.  
V prípade nemechanických pevných nástrojov je možné nastaviť konštantnú teplotu objektu pomocou referenčnej teploty ( [REFTMP](/docs/sk/keyword_documentation/r/reftmp/)) v rámci [Objects Properties.](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

Poznámka:
Použitie tejto aproximácie bude mať tendenciu nadhodnocovať teplotné straty, pretože povrch matrice sa počas simulácie nezahrieva. Tento efekt možno kompenzovať znížením koeficientu prestupu tepla medzi objektmi ([IHTCOF](/docs/sk/keyword_documentation/i/ihtcof/)).

  
Pre porézny objekt musí byť relatívna hustota zadaná tak, ako je popísané v type porézneho objektu pomocou tlačidla Priradiť hustotu. Tým sa inicializuje hodnota relatívnej hustoty pre všetky prvky definovanou hodnotou. Pomocou hodnôt údajov o prvku môžeme určiť objekty ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Objekt Ikona prvku (![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) ) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Deformácia ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Karta Všeobecné.  
Pre každý objekt definovaný ako zmes sa musí priradiť počiatočný objemový podiel ([VOLFC](/docs/sk/keyword_documentation/v/volfc/)) a maximálny transformovaný objemový podiel ([VOLFS](/docs/sk/keyword_documentation/v/volfs/)) pre všetky objemové podiely. Vo všeobecnosti by sa [VOLFC](/docs/sk/keyword_documentation/v/volfc/) a [VOLFS](/docs/sk/keyword_documentation/v/volfs/) mali inicializovať na rovnakú hodnotu. Objemový zlomok možno definovať výberom ikony Object ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Objects Element (![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }})) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Transformation (Transformácia) na karte Objekt.

## Typ objektu (OBJTYP)

Typ objektu ([OBJTYP](/docs/sk/keyword_documentation/o/objtyp/)) definuje, či a ako sa modeluje deformácia pre každý jednotlivý objekt v probléme DEFORM.

Nižšie sú uvedené rôzne typy objektov, ktoré sú k dispozícii v DEFORM:

11.4.1. Plastc

11.4.2. Elastický

11.4.3. Elasto-plastické

11.4.4. Porézne

11.4.5. Pevná stránka

11.4.6. Hyper-elastické

11.4.7. Používateľom definované

11.4.8. Prostredie (Fluid(CFD))

11.4.9. Prostredie (vzduch (elektromagnetické))

### Plast [2D, 3D]

Plastové objekty sa modelujú ako tuhý plastický alebo tuhý viskoplastický materiál v závislosti od vlastností materiálov. Formulácia predpokladá, že napätie v materiáli lineárne rastie s rýchlosťou deformácie až do prahovej rýchlosti deformácie, označovanej ako medzná rýchlosť deformácie ([LMTSTR](/docs/sk/keyword_documentation/l/lmtstr/)). Materiál sa plasticky deformuje nad medznou rýchlosťou deformácie. Plastické správanie sa materiálu objektu sa špecifikuje pomocou funkcie napätia toku materiálu alebo údajov o napätí toku ([FSTRES](/docs/sk/keyword_documentation/f/fstres/)).  
  
**Aplikácie:**
Pri použití na modelovanie obrobku poskytuje veľmi dobrú simuláciu skutočného správania materiálu. Presne zachytáva citlivosť na rýchlosť deformácie.  
  
**Omedzenia:**
Nemodeluje pružné zotavenie (spätné pruženie), a preto je nevhodný na ohýbanie alebo iné operácie, pri ktorých má spätné pruženie významný vplyv na konečnú geometriu dielu. Nemodeluje deformácie spôsobené tepelnou rozťažnosťou/zmrštením. Nemôže zachytiť zvyškové napätia.

### Elastické [2D, 3D]

Pružné správanie materiálu je špecifikované pomocou Youngovho modulu ([YOUNG](/docs/sk/keyword_documentation/y/young/)) a Poissonovho pomeru ([POISON](/docs/sk/keyword_documentation/p/poison/)). Elastické objekty sa používajú, ak sú dôležité znalosti o napätí a deformácii nástroja v priebehu procesu. Ak sú pre napätie v zápustke potrebné informácie o maximálnom napätí alebo deformácii, odporúča sa na simuláciu deformácie použiť tuhé zápustky, potom sa použije simulácia napätia v zápustke v jednom kroku.  
Ďalšie informácie nájdete v online pomocníkovi v časti Napätie v matrici 3D - [3D Die stress setup](/docs/sk/operation_templates/30_die_stress/30_2_3d_die_stress_setup/) , 2D- [2D Die Stress Analysis Theory](/docs/sk/operation_templates/30_die_stress/2d_die_stress_analysis_theory/) a [Die Stress study](/docs/sk/labs/die_stess_study_labs/die_stess_labs_across_single_steps_main_pg/) [ labs](/docs/sk/labs/die_stess_study_labs/die_stess_labs_across_single_steps_main_pg/). Pre 3D sa v súčasnosti vyžaduje plne prepojená analýza pružného nástroja s plastickým obrobkom, na odporúčanie je potrebné použiť prepojenú analýzu napätia v zápustke, ako je vysvetlené v [Coupled Die stress Analysis](/docs/sk/operation_templates/30_die_stress/coupled_die_stress_analysis/).  
  
**Aplikácie:**
Pri použití na modelovanie nástrojov môže elastický model poskytnúť informácie o napätí a deformácii nástroja. Užitočné v zriedkavých situáciách, keď môže mať priehyb nástroja významný vplyv na tvar súčiastky.  
**
Obmedzenia:**
Ak sa prekročí medza klzu nástroja, výsledky napätia a deformácie budú nesprávne. Vo väčšine prípadov však platí, že ak je prekročená medza klzu nástroja, predstavuje to neprijateľnú situáciu a deformácia nástroja nad medzu klzu nie je užitočná. Dobrou praxou je kontrolovať napätia v simuláciách s pružným náradím, aby sa zabezpečilo, že táto situácia nebude porušená.

### Elasto-plastické (Ela-Pla) [2D, 3D]

Elasto-plastické objekty sa považujú za elastické objekty až do dosiahnutia medze klzu.  
Potom sa všetky časti objektu, ktoré dosiahnu bod klzu, považujú za plastické, zatiaľ čo zvyšok objektu sa považuje za pružný. Pri elastoplastickej deformácii je celková deformácia v objekte kombináciou pružnej a nepružnej deformácie. Neelastická deformácia pozostáva z plastickej deformácie, deformácie tečením, tepelnej deformácie a transformačnej deformácie v závislosti od vlastností materiálov. Podrobnejšie informácie týkajúce sa materiálového modelu nájdete v kapitole [10\. Material Data](/docs/sk/pre_processor/10_material_data/10_material_data/). V prípade tehlových prvkov platí elastoplastický model pre všetky úrovne deformácie.

Pre elasto-plastický typ objektu sú k dispozícii tri formulácie prvkov.

  * Štandardné - predvolené nastavenie. Odporúčané pre väčšinu aplikácií.
  * Zmiešané (Tet mesh) - vhodné na simulácie tepelného spracovania s malou deformáciou.
  * Predpokladaná deformácia (tehlová sieť) - Vhodné pre modely s tehlovou sieťou, ktoré majú iba 1-2 vrstvy prvkov v celej hrúbke.

**Predpokladané napätie (tehlová sieť)**

Nastavenie "**Predpokladaná deformácia** " by sa malo aktivovať v modeloch elasto-plastického tvárnenia plechu, ktoré sú obmedzené len na 1-2 vrstvy tehlových prvkov, hoci hrúbka plechu je obmedzená. Toto nastavenie pomáha vyhnúť sa možnému numerickému zablokovaniu šmyku prijatím predpokladaného poľa priečnej šmykovej deformácie. Nastavenie "Predpokladaná deformácia" nie je potrebné, ak má objekt z plechu 3 alebo viac vrstiev tehlových prvkov cez hrúbku.

  
**Aplikácie:**
Poskytuje realistickú simuláciu pružného zotavenia (spätného pruženia) a deformácií spôsobených tepelnou rozťažnosťou. Užitočné pri problémoch, ako je ohýbanie, kde má spätná pružina významný vplyv na konečnú geometriu súčiastky. Užitočné aj na výpočty zvyškových napätí. Tento typ objektu dokáže spracovať aj materiály citlivé na rýchlosť deformácie. Typ objektu musí byť elasticko-plastický pre výpočty tečenia.  
  
**Omedzenia:**
Vo všeobecnosti trvá dlhý čas riešenia, konvergenčné správanie je výrazne ovplyvnené materiálovými údajmi definovanými pre počiatočné podmienky poddajnosti a kontaktné podmienky deformujúcich sa objektov.  
  
**Poznámka:** Ak je prietokové napätie definované pre viacero deformačných rýchlostí, prietokové napätie elastoplastického materiálu sa vyhodnotí pri hodnote deformačnej rýchlosti uvedenej v položke limiting strain rate v časti object->properties.

### Porézne [2D, 3D]

S poréznymi objektmi sa zaobchádza rovnako ako s plastickými objektmi (stlačiteľné tuhé-viskoplastické materiály) s tým rozdielom, že hustota materiálu sa počíta a aktualizuje ako súčasť simulácie. Správanie materiálu sa modeluje podobne ako pri plastických objektoch, ale model zahŕňa do formulácie stlačiteľnosť materiálu. V stave plnej hustoty sa musí určiť medzná miera deformácie ([LMTSTR](/docs/sk/keyword_documentation/l/lmtstr/)) a napätie pri prúdení ([FSTRES](/docs/sk/keyword_documentation/f/fstres/)). Hustota materiálu sa špecifikuje pri každom prvku ([DENSTY](/docs/sk/keyword_documentation/d/densty/)). Objekty s meniacou sa hustotou materiálu, ako sú napríklad materiály používané pri práškovom tvárnení, by sa mali modelovať ako porézne objekty. Jedinou iteračnou metódou, ktorá je v súčasnosti k dispozícii pre porézny materiál, je metóda priameho riešenia. Táto metóda nemá schopnosť rýchlej konvergencie, následne môže pórovitá simulácia trvať dlhšie ako porovnateľná plastická simulácia.

Modely spekaných materiálov dostupné v systéme DEFORM nájdete na adrese [10.12.7. Sintering Driving Force Model.](../10_material_data/10_12_miscellaneous_data/10_12_miscellaneous_data.htm#10.12.7._Sintering_Driving_Force_model)

Od verzie 14.0 môže používateľ modelovať pružné správanie poréznych materiálov výberom možnosti Elasto-plastic (Pružný a plastický) z možností typu Porézny objekt, ako je znázornené na obr. 11.4.

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image004.jpg' | relative_url }})

Možnosť typu porézneho objektu

  
  
  
**Aplikácie**
Vhodné pre zhutnené, spekané prášky, nad približne 70 /presne modeluje konsolidáciu a zhutňovanie počas kovania.  
  
**Obmedzenia**
Nie je určený na modelovanie procesov zhutňovania sypkých práškov.

### Rigid [2D, 3D]

Tuhé objekty sú modelované ako nedeformovateľné materiály. Pri deformačnej analýze je objekt reprezentovaný geometrickým profilom ([DIEGEO](/docs/sk/keyword_documentation/d/diegeo/)). Údaje o riešení deformácie dostupné pre tuhé objekty zahŕňajú zdvih objektu, zaťaženie a rýchlosť. Sieť pre tuhý objekt sa používa len na tepelné, transformačné a difúzne výpočty.  
  
**Aplikácie:**
Pri použití na modelovanie nástrojov zvyšuje rýchlosť simulácie (v porovnaní s pružnými nástrojmi) tým, že znižuje počet deformovateľných objektov, a tým aj počet rovníc, ktoré sa musia riešiť. Zanedbateľná strata presnosti pri typických simuláciách, pri ktorých majú nástroje oveľa vyššiu medzu klzu ako obrobok.  
  
**Omedzenia:**
Údaje o napätí a deformácii matríc počas deformácie nie sú k dispozícii. Tieto údaje je možné získať vo vybraných jednotlivých krokoch vykonaním analýzy napätia v jednom kroku zápustky.

### Hyperelastický [2D,3D]

Hyperelastické správanie materiálu sa špecifikuje pomocou typu objektu hyperelastic ([HYPREL](/docs/sk/keyword_documentation/h/hyprel/)). Hyperelastický materiál je typ konštitutívneho modelu pre ideálne pružný materiál, pre ktorý vzťah napätie-deformácia vyplýva z funkcie hustoty deformačnej energie. Hyperelastické objekty sa používajú v aplikáciách, ako je tvarovanie gumových podložiek a pri deformácii niektorých polymérnych objektov. Používateľ môže vybrať túto možnosť, ak je typ objektu hyperelastický. V programe DEFORM sú na simuláciu hyperelasticity k dispozícii dva hyperelastické konštitutívne modely Neo-Hookean a Mooney-Rivlin.  
  
**Aplikácie**
Tvarovanie gumových podložiek, deformácia určitých polymérových predmetov atď.  
  
**Obmedzenia**
Nie je k dispozícii pre 2D rovinné napätie

### Definované používateľom [2D] [3D]

Používateľ má možnosť prispôsobiť správanie materiálu. Používatelia môžu prispôsobiť správanie materiálu pomocou [usr_mat.f.](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_5_User_defined_material_models_\(USRMAT\)) definovaním jedinečného konštitutívneho modelu. Povolený je len jeden objekt s takouto definíciou, preto nie je potrebné odovzdávať žiadne číslo procedúry. Používatelia môžu modelovať elasto-plastické alebo tuho-plastické správanie a môžu vybrať príslušnú možnosť z možností typu objektu definovaného používateľom, ako je znázornené na obr. 11.5. , Elasto-plastic pre elasto-plastické a Plastic pre tuhoplastické. Pre používateľom definované elasto-plastické problémy sa navrhuje SP riešiteľ. Od verzie 12 táto implementácia nahrádza funkciu UMAT.DAT v predchádzajúcich verziách.

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image005.jpg' | relative_url }})

Typ objektu definovaný používateľom

### Prostredie [Fluid(CFD)] [2D, 3D]

Používatelia môžu definovať prostredie Fluid pomocou typu objektu Environment (Fluid(CFD)), ako je znázornené na obr. 11.6. Táto možnosť bude k dispozícii, keď používateľ zapne typ simulácie "CFD flow" (prúdenie CFD) na stránke Simulation controls (Ovládacie prvky simulácie).

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image006.jpg' | relative_url }})

Výber objektu typu prostredia Fluid(CFD)

### Prostredie [Vzduch (elektromagnetické)] [2D, 3D]

Vzduch v elektromagnetických problémoch typu Induction možno modelovať pomocou typu objektu Environment (Air(Electro-magnetic)), ako je znázornené na obr. 11.7. Táto možnosť je používateľom k dispozícii, keď je v časti Prenos tepla na stránke Simulation controls (Ovládacie prvky simulácie) vybraný typ Induction (Indukčný typ ohrevu).

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image007.jpg' | relative_url }})

Prostredie Výber objektu typu Air(Electro-magnetic)

### Definované používateľom (plast) [2D] [3D]

Používateľ má možnosť prispôsobiť správanie plastového materiálu. Používateľ môže prispôsobiť správanie materiálu pomocou [usr_mat.f.](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#User_Defined_\(Plastic\)) definovaním jedinečného konštitutívneho modelu. Povolený je len jeden objekt s takouto definíciou, preto nie je potrebné odovzdávať žiadne číslo procedúry. Tento typ objektu možno použiť na simuláciu tuhého plastického modelu materiálu. Od verzie 12 táto nová implementácia nahrádza funkciu UMAT.DAT v predchádzajúcich verziách. V aktuálnej verzii v12 DEFORM je pre problémy s elasto-plastickými objektmi definovanými používateľom navrhnutý riešiteľ SP.

## Primárna matrica (PDIE)

Primárna kocka ([PDIE](/docs/sk/keyword_documentation/p/pdie/)) určuje primárny objekt pre simuláciu. Primárny objekt sa zvyčajne priraďuje k objektu, ktorý je najtesnejšie ovládaný tvárniacim strojom.  
Napríklad matrica pripevnená k baranu mechanického lisu sa označuje ako primárna matrica. Charakteristiky primárnej lisovacej formy možno použiť na riadenie rôznych aspektov simulácie vrátane:

  * Veľkosť časového kroku simulácie ([DSMAX](/docs/sk/keyword_documentation/d/dsmax/))
  * Pohyb objektu ([MOVCTL](../../keyword_documentation/m/movctl_\(2d\).htm))
  * Kritériá ukončenia simulácie ([SMAX](/docs/sk/keyword_documentation/s/smax/), [VMIN](/docs/sk/keyword_documentation/v/vmin/) a [LMAX](/docs/sk/keyword_documentation/l/lmax/))

Primárna matrica sa definuje pomocou zaškrtávacieho políčka (pozri obr. 11.3.). Ako primárnu kocku je možné definovať iba jeden objekt.

## **Import objektu zo súboru**![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) :

Používateľ môže importovať objekt zo súboru s kľúčom alebo z databázy. Tým sa importujú všetky údaje o objekte dostupné v súbore s kľúčom alebo v DB, ako sú geometria, sieť, BCC, pohyb, materiál a uzlové a elementárne údaje.

## **Import objektu z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}):

Používateľ môže importovať objekt z používateľskej knižnice.

## **Uloženie objektu do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) :

Používateľ môže objekt uložiť vo formáte kľúčového súboru. Tento uložený súbor môže ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) importovať späť pomocou možnosti importovať objekt v ľubovoľnom inom nastavení problému deformácie.

## **Uloženie objektu do knižnice**![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) :

Používateľ môže uložiť údaje o objekte do knižnice a uložený súbor môže importovať späť pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) importovať objekt v akomkoľvek inom nastavení problému deformácie.

**Súvisiace témy:**

[9\. Simulation Controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

[10\. Material Properties](/docs/sk/pre_processor/10_material_data/10_material_data/)

[12\. Geometry Modelling](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[13\. Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[16\. Object Properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[17\. Object Data Initialize](/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[18\. Advanced Object Data Definition](/docs/sk/pre_processor/18_object_manipulation_tools/18_object_manipulation_tools/)

[19\. Object positioning](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/)

[20\. Inter-Object Definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[21\. Database Generation](/docs/sk/pre_processor/21_database_generation/21_database_generation/)

[22\. Convert 2D to 3D](/docs/sk/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/)
