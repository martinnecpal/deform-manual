---
lang: sk
title: "Modelové laboratórium MEDC"
---

# Laboratórium pre model MEDC (vývoj mikroštruktúry počas chladenia) pre zliatiny titánu

1.1 Celkový prehľad

1.2. Spustenie modelu MEDC v Material Suite

1.3 Výber objektu a výber bodu

1.4 Nastavenie modelu MEDC

1.5 Simulátor bodu točenia materiálu

1.6 Výstup

Prehľad

Model MEDC (** Vývoj mikroštruktúry počas chladenia**) v súbore materiálov je použiteľný pre zliatiny titánu. Cieľom je modelovať vývoj mikroštruktúry počas chladenia pre dvojfázovú zliatinu alfa a beta Ti 6-4 na predpovedanie štruktúry transformácie. Model MEDC predpovedá veľkosť primárneho alfa zrna, objemové frakcie primárneho alfa, beta a sekundárneho alfa a štruktúru sekundárneho alfa transformovaného z beta podľa pravidla výberu variantov. V DEFORMÁCII sú implementované dve pravidlá výberu variantov, a to náhodný výber variantov a preferované pravidlo výberu variantov, ktoré najlepšie zodpovedajú pólovým číslam primárnej alfa. Textúra môže byť reprezentovaná buď v Rodriguesovom priestore alebo v Eulerovom priestore. Vstupné údaje do modelu MEDC zahŕňajú kontrolné údaje simulácie MEDC, definíciu materiálu, údaje o fázovej transformácii z beta na primárnu alfa a z beta na sekundárnu alfa, počiatočnú textúru, počiatočné objemové frakcie alfa a beta fázy a počiatočnú veľkosť primárneho zrna alfa. Pre každý uložený krok v databáze deformácií obsahujú výstupné údaje vyššie uvedené vlastnosti mikroštruktúry. K dispozícii sú nástroje na analýzu textúr, ako sú pólové čísla, inverzné pólové čísla a Kearnsovo číslo kryštálu HCP, najmä pre celkový alfa kód.

Model MEDC je možné spustiť buď po dokončení modelu deformačnej textúry, alebo ako samostatný model transformačnej textúry s použitím známej alebo predpokladanej deformačnej textúry. Model MEDC je možné spustiť po dokončení modelu deformačnej textúry v Material Suite tak, aby sa predpovedaná deformačná textúra mohla použiť ako vstup do modelu MEDC ako počiatočná textúra. Ak sa MEDC používa ako samostatný model na predpovedanie transformačnej textúry bez predchádzajúcich výsledkov modelu deformačnej textúry, používateľ môže použiť typickú databázu deformácií tepelného spracovania spolu s nameranou deformačnou textúrou (EBSD) alebo predpokladanými údajmi deformačnej textúry ako počiatočnú počiatočnú textúru pre model MEDC.

V tomto laboratóriu je prezentovaný vývoj mikroštruktúry a textúry počas tepelného spracovania dvojitej kužeľovitej vzorky Ti 6-4 ako samostatného modelu MEDC. Toto laboratórium používa súbor kľúča DEFORMÁCIE na spustenie simulácie tepelného spracovania a demonštruje, ako používať model MEDC na spustenie simulácie bodového režimu pre transformačnú textúru pomocou databázy deformácií pre prípad dvojitého kužeľa Ti 6-4 tepelného spracovania s použitím predpokladanej deformačnej textúry ako počiatočnej počiatočnej textúry.

## Spustenie modelu MEDC v balíku materiálov

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v12.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI.

Požadujeme nominálnu DB na vykonanie analýzy textúry v materiáli, pre toto laboratórium použijeme * * * *** Double_Cone_Cooling_Nominal.key ** z * ***\PRÍRUČIEK\PDF\ DEFORM3D_MEDC_Lab**** na vygenerovanie nominálnej DB. Otvorte **NG Pre** pomocou prepojenia DEFORMÁCIE GUI Main a definujte ID problému ako " * ***Double_cone_Cooling* ** * ", vyberte prepínač "**3D** " Dimension a "**System International (SI)** " unit System prepínač v okne New Problem, potom importujte * * * ** Double_Cone_Cooling_Nominal.key * * *** z priečinka ****\MANUÁLY\PDF\DEFORM\ 3D_MEDC_Lab**** *. Prejdite na stránku Generate DB a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) pre vygenerovanie databázy. Zatvorte NG Pre a spustite simuláciu z GUI Main, uistite sa, že simulácia sa zastaví normálne bez akéhokoľvek problému. Teraz z hlavného GUI, bez výberu ********Double_CONE_Cooling** ** ** * *.DB súbor kliknite na **Material* ***Suite** v časti „Post Processor“ a otvorte modul Material Suite.

Po zobrazení hlavného okna pre sadu materiálov kliknite na ikonu "Otvoriť..." (![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }})) v hornom paneli nástrojov a importujte vzorovú databázu (**Double_cone_Cooling.DB**). Do stromu úloh sa pridá predvolená položka úlohy „DEFORMOVAŤ“. Rozbaľte položku „* * Mikroštruktúra * * “ a kliknite na ikonu „* * Model MEDC * * “, do stromu úloh sa pridá nová položka úlohy „* * Vývoj mikroštruktúry počas chladenia modelu zliatiny Ti * * “, ako je znázornené na obr. MEDCL.1, .

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0001.jpg' | relative_url }})

Spustite model MEDC v Material Suite.

## Výber objektu a výber bodu

Ako je znázornené na obr. MEDCL.2, v strome úloh „DEFORMOVAŤ“ kliknite na položku „** Výber objektu ** “ a vyberte položku „**Obrobok** “. Kliknite na „** Výber bodu ** “, definujte číslo kroku ako „-1“ a definujte dva body na obrobku (obr. MEDCL.3). Súradnica bodu 1 (P1) je (1,176, 0, 0,381, 1) a súradnica bodu 2 (P2) je (8,950, 0, 8,701, 1).

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0002.jpg' | relative_url }})

Výber objektu a výber bodu

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0003.jpg' | relative_url }})

Definícia bodov na obrobku

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0004.jpg' | relative_url }})

Konfigurácia

## Nastavenie modelu MEDC

Všetky údaje pre model MEDC sú pripravené položkami v "** Vývoj mikroštruktúry počas chladenia modelu zliatiny Ti ** ". Pozrite si obr. MEDCL.4, kliknite na položku „**Config** “, zobrazí sa jej okno s údajmi. Zadajte spustiteľný súbor pre simuláciu MEDC a pracovný adresár kliknutím na tlačidlá definície (![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }})). Predvolený spustiteľný súbor pre simuláciu MEDC jeDEF_MEDC.EXE ", ktorý sa nachádza v inštalačnom adresári softvéru Deform. Používatelia môžu tiež vytvoriť vlastný spustiteľný súbor pre simuláciu MEDC a tu zadať názov súboru. Pracovný adresár musí byť ten, v ktorom sa nachádza nominálna databáza.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0005.jpg' | relative_url }})

Simulačné riadenie MEDC

Kliknite na položku „** MEDC simulation control** “, jej okno s údajmi sa zobrazí ako obr. MEDCL.5\. Je potrebné špecifikovať nasledujúce údaje: metóda reprezentácie textúry (Eulerove uhly alebo Rodriguesov priestor), rozsah krokov na aplikáciu simulácie MEDC, zdroj údajov o textúre, zdroj spustiteľného súboru, faktor mierky pre primárnu veľkosť alfa. Predvolené hodnoty sú uvedené, ale používatelia môžu tieto hodnoty zmeniť. Ak v databáze existujú údaje o textúre (ODF), zistia sa automaticky a používateľ môže vybrať prepínač „**Extrahovať transformačnú textúru z existujúcej databázy ODF ** “. V tomto prípade len extrahujeme dáta a zobrazíme ich na nasledujúcich stránkach. Ak však chcú používatelia prepočítať textúru transformácie, vyberte prepínač „**Vypočítať textúru transformácie ** “ a vyberte prepínač „**Existujúca textúra deformácie v databáze** “.

Keď je zaškrtnuté prepínacie tlačidlo „* * Vypočítať transformačnú textúru * * “, existujú tri možnosti definovania zdroja deformačnej textúry ako počiatočných textúrnych údajov pre model MEDC: (1) Existujúca deformačná textúra v databáze deformácií; (2) Deformačná textúra v dôsledku spustenia simulátora DEFORMAČNÝCH bodov Material Suite; (3) Nová definícia počiatočnej textúry pre model MEDC. Pre použitie deformačnej textúry zo simulátora bodu DEFORMÁCIE Material suite musíme špecifikovať cestu priečinka výsledku simulácie deformačnej textúry. Ak tento priečinok s názvom „TEXTÚRA“ existuje v aktuálnom pracovnom adresári, automaticky sa zistí a zobrazí v editore riadkov. Koeficient mierky primárnej alfa konvertuje výsledok zobrazenia primárnej veľkosti alfa. V tomto laboratóriu vyberáme počiatočný zdroj textúry 3 (**Nová definícia deformačnej textúry**). Importujte údaje o materiáli zo súboru *** ***Double_Cone_Cooling_Nominal.key* * pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_button.jpg' | relative_url }}). Začiarknite políčko ** Materiál zmesi ** a kliknite na tlačidlo trice ![]({{ '/assets/icons/pre_icons/mo_add_phase_button.jpg' | relative_url }}) na tri fázy v zozname, potom premenujte fázy na „** PriAlpha ** “, „**Beta** “ a „** SecAlpha ** “, ako je znázornené na obr. MEDCL.6.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0006.jpg' | relative_url }})

Definícia materiálu

Kliknite na položku „* * Definícia materiálu * * “ a okno s údajmi sa zobrazí na obr. MEDCL.6\. Ak je na riadiacej stránke simulácie MEDC zvolené prepínač „Extrahovať transformačnú textúru z existujúcej databázy ODF“, čo znamená, že v databáze existujú údaje o textúre sekundárnej alfa, údaje o materiáli sa automaticky extrahujú z databázy a zobrazia sa. Vlastnosti materiálu si môžete prezrieť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button_2.jpg' | relative_url }}) (pozri obr. MEDCL.6). V tomto prípade by sa nemali meniť vlastnosti materiálu. Jedinými dotknutými vlastnosťami sú základné informácie o textúre (typ kryštálu, typ textúry a typ Rodriguesovej siete) pre údaje o fázovom materiáli a fázovej transformácii definované v materskom materiáli.

Ak je na ovládacej stránke simulácie MEDC zvolené prepínacie tlačidlo „Vypočítať textúru transformácie“, definícia materiálu je znázornená na obr. MEDCL.7 ~ 10, v závislosti od možnosti počiatočných zdrojových údajov textúry. Ak je zvolené prepínacie tlačidlo "existujúca deformačná textúra v databáze", z databázy sa extrahujú textúrne údaje primárnej alfa a beta. Ak boli v databáze definované textúrne dáta sekundárnych alfa a fázových transformácií, tieto dáta sa extrahujú automaticky; inak je potrebné tieto dáta definovať.

Ak je zvolené prepínacie tlačidlo „Deformation texture from material point simulator“ (Textúra deformácie zo simulátora materiálového bodu), údaje o textúre primárnych alfa a beta sú extrahované automaticky z posledného kroku výsledkov simulátora materiálového bodu pre priebeh deformačnej textúry; je potrebné definovať údaje o textúre sekundárnych údajov o alfa a fázovej transformácii.

Ak je zvolené prepínacie tlačidlo „**Nová definícia počiatočnej textúry** “, je potrebné definovať základné informácie o textúre všetkých fáz a údajov o transformácii fázy. Na obr. MEDCL.7 je znázornená definícia základných informácií o textúre primárneho alfa a beta. Základné informácie o textúre sekundárnej alfa (SecAlpha) sú definované rovnako ako primárna alfa (PriAlpha). Pre primárnu alfa a sekundárnu alfa je kryštálovým typom HCP; pre beta je kryštálovým typom BCC. Pre každú fázu je typ reprezentácie textúry Rodriguesov priestor a typ povrchovej siete textúry je typ 3.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0007.jpg' | relative_url }})

Základné informácie o textúre každej fázy

Ak chcete definovať údaje fázovej transformácie, vyberte nadradený materiál „* *Ti64-test** “ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button_2.jpg' | relative_url }}) (pozri obr. MEDCL.6). V okne vlastností kliknite na ikonu položky transformácie (![]({{ '/assets/icons/pre_icons/mo_transformation_icon.jpg' | relative_url }})), ako je znázornené na obr. MEDCL.8\. Pridajte dva modely fázovej transformácie: beta k primárnej alfa a beta k sekundárnej alfa. Pre transformáciu z beta na primárnu alfa, vyberte "MEDC" ako kinetický model. Model MEDC predpovedá vývoj primárnej veľkosti alfa a objemovej frakcie počas chladenia. Kinetika je riadená difúziou vanádu alebo hliníka.

Tu použitý difúzny koeficient je prevzatý z (S.L. Semiatin, S.L. Knisley, P.N. Fagin, F. Zhang a D.R. Barker, „Microstructure evolution during alpha-beta heat treatment of Ti-6Al-4V“, Metall. Mater. Trans. A34 (2003), 2377-2386).

  
Za predpokladu, že difúzia je riadená vanádom, A = 100000 ![]({{ '/assets/equations/keyword_documentation/p/meu.jpg' | relative_url }})m2/s a B=17460 pre jednotku SI. Kliknutím na tlačidlo (![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }})) definujete fázové zloženie prvku riadiaceho difúziu v rovnovážnom stave, ako je znázornené na obr. MEDCL.8\. Vstupné veličiny zahŕňajú: (1) priemernú koncentráciu prvku riadiaceho difúziu (V) C0: 0,042; (2) hodnoty teplôt; (3) chemické zloženie v rovnovážnom stave pri rôznych teplotách, ktoré sú definované kliknutím na tlačidlá „Cp“ a „Ci“. "Cp" predstavuje koncentráciu prvku riadiaceho difúziu v primárnej alfa a "Ci" označuje zodpovedajúcu koncentráciu v beta fáze.

Podrobné hodnoty pre Cp a Ci ako funkcie teploty sú uvedené v S.L. Semiatin, S.L. Knisley, P.N. Fagin, F. Zhang a D.R. Barker, „Microstructure evolution during alpha-beta heat treatment of Ti-6Al-4V“, Metall. Mater. Trans. A34 (2003), 2377-2386.

V tomto laboratóriu môžeme tiež kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button_2.jpg' | relative_url }}) a načítať dátový súbor „**Ti64_ChemicalComp****.**** dát ** “ na vyplnenie týchto funkčných údajov. (Pozri obr. MEDCL.9)

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0008.jpg' | relative_url }})

Údaje o fázovej transformácii z beta na primárnu alfa - výber modelu MEDC

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0009.jpg' | relative_url }})

načítané funkčné údaje MEDC z **Ti64_ChemicalComp****.**** dátového súboru**

  
Pre fázovú transformáciu z beta na sekundárnu alfa zvoľte ako kinetický model "Secondary alpha lath based on the critical cooling rate" (obr. MEDCL.10). Tento model vypočítava kritickú rýchlosť ochladzovania pre tvorbu sekundárnej alfa a vývoj objemových frakcií beta a sekundárnej alfa. Čiara na definovanie udávanej teploty (![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/t_s.jpg' | relative_url }})) a času (t) pre sekundárny rast alfa z teploty roztoku je definovaná ako,

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/eqn_1.jpg' | relative_url }})  
Kde ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/t_beta.jpg' | relative_url }}) je beta transus. Objemový podiel sekundárnej alfa sa vypočíta ako

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/eqn_2.jpg' | relative_url }})  
Kde ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/t_e.jpg' | relative_url }}) je koncová teplota pre transformáciu z beta na sekundárnu alfa a ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/v_r.jpg' | relative_url }}) je vyvážený objemový podiel primárnej alfa.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0010.jpg' | relative_url }})

Údaje o transformácii fázy z beta na sekundárnu alfa.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0011.jpg' | relative_url }})

Model výberu variantu pre textúru fázovej transformácie.

  
Ak chcete definovať model textúry fázovej transformácie z beta na sekundárnu alfa, kliknite na kartu „ostatné“ zobrazenú na obr. MEDCL.11 a vyberte "Náhodný výber" ako model výberu variácie. Podľa tohto pravidla sa predpokladá, že všetky varianty sú rovnako pravdepodobné.

  
Pre účely demonštrácie pre toto laboratórium predpokladáme nasledujúce hodnoty.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/t_beta.jpg' | relative_url }})=1000 °C, teplota roztoku = 955 °C
![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/a1.jpg' | relative_url }})=0,2, ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/a0.jpg' | relative_url }}) =150 °C
Teplotný rozsah nad a pod na výpočet rýchlosti chladenia: ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/delta_t.jpg' | relative_url }})= 50 °C
A=-4, D=3, ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/t_e.jpg' | relative_url }})= 500 °C
  
Treba spomenúť, že vyššie uvedené hodnoty ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/a1.jpg' | relative_url }}), ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/a0.jpg' | relative_url }}), ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/delta_t.jpg' | relative_url }}), A, D a ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/t_e.jpg' | relative_url }}) sú tvorené hodnotami kvôli demonštrácii. Používatelia musia naladiť svoje experimentálne údaje, aby našli vhodné hodnoty pre tieto parametre.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0012.jpg' | relative_url }})

Počiatočná textúra a mikroštruktúra (celkový pohľad)

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0013.jpg' | relative_url }})

Počiatočná štruktúra a mikroštruktúra: osi textúry

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0014.jpg' | relative_url }})

Počiatočná štruktúra a mikroštruktúra: ODF primárnej alfa

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0015.jpg' | relative_url }})

Počiatočná štruktúra a mikroštruktúra: ODF beta

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0016.jpg' | relative_url }})

Počiatočná štruktúra a mikroštruktúra: objemové frakcie a veľkosť zrna

Kliknutím na položku „**Počiatočná textúra a mikroštruktúra** “ otvoríte okno s údajmi (obr. MEDCL.12). Ak je na stránke kontroly simulácie MEDC vybraté prepínač „Extrahovať transformačnú textúru z existujúcej databázy ODF“, všetky údaje sa automaticky extrahujú a vyplnia na tejto stránke. Údaje je možné skontrolovať, ale nie je možné ich upraviť. Ak je vybraté prepínacie tlačidlo „Vypočítať textúru transformácie“, ak je počiatočná textúra z existujúceho ODF v databáze alebo z deformačnej textúry simulátora materiálového bodu, textúrne údaje primárneho alfa a beta sa automaticky extrahujú a zobrazia. Pri výbere prepínača „nová definícia počiatočnej textúry“ potrebujeme definovať osi textúry, počiatočnú textúru, počiatočný objemový zlomok a veľkosť zrna (pozri obr. MEDCL.12~16).

Pre toto laboratórium budeme predpokladať a definovať deformačnú textúru ako počiatočnú textúru pre model MEDC. Pozri obr. MEDCL.13, pre bod 1 kliknite na kartu „**Textúra****osi** “ a zadajte osi textúry ako osi globálnych súradníc, t. j. RD=(1,0,0), TD=(0,1,0) a ND=(0,0,1). Kliknutím na kartu „* * Orientácia ** *údaje * * “ inicializujete hodnoty ODF pre každú fázu (obr. MEDCL.14 ~ 15). Nastavte typ formátu údajov na 5 (WTD: TSL Bunge, Radians, Weights) a uhol vyhladenia ODF nastavte na 5 stupňov. Pre bod 1 sú počiatočné textúrne údaje pre primárne alfa a beta umiestnené v priečinku laboratória MEDC: **DEFORM_Sample_MEDC_PrimaryAlpha_P1.Dat** ,
**DEFORM_Sample_MEDC_Beta_P1.Dat**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) importujete dátový súbor a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) vypočítate hodnoty ODF. Pre sekundárnu alfa použite formát údajov typu 1 (náhodná textúra) na inicializáciu hodnôt ODF tak, aby ODF=1 pre každú zložku.

Na obr. MEDCL.16 je znázornená definícia počiatočného objemového zlomku každej fázy a počiatočná primárna veľkosť alfa (polomer). V tomto laboratóriu sú počiatočné objemové frakcie primárneho alfa, beta a sekundárneho alfa pri teplote roztoku 0,274, 0,726 a 0; primárna veľkosť alfa (polomer) je 4 mikróny.

Pre bod 2 použite rovnaký postup na špecifikovanie počiatočnej textúry a mikroštruktúry. Okrem počiatočnej štruktúry sú ostatné položky rovnaké ako v bode 1. Počiatočné údaje o textúre pre primárnu alfa a beta verziu pre bod 2 sa nachádzajú v priečinku laboratória MEDC: **DEFORM_Sample_MEDC_PrimaryAlpha_P2.Dat** , **DEFORM_Sample_MEDC_Beta_P2.Dat**.

## Spustiť simulátor materiálových bodov

Kliknite na položku „* * Spustiť * * “ v strome úloh a v okne údajov kliknite na tlačidlo „** Vypočítať * *“ (obr. MEDCL. 17). V pracovnom adresári sa vytvorí priečinok s názvom „MEDC_Model“ a pod ním sa vytvorí priečinok pre každý vybraný bod s názvom „Bod*“ (* označuje číslo bodu) na uloženie výsledkov simulácie.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0017.jpg' | relative_url }})

Spustiť simuláciu

Vo všeobecnosti sa pre každý vybraný bod vytvoria nasledujúce dátové súbory
(1) Vstupné súbory pre spustiteľný súbor simulácie MEDC:

**STEP.txt** : uložené čísla krokov v nominálnej databáze.
**temp_mean.*** *tx*** * * t ** **: * * Jednotkový systém a história teploty.
**StressStrain.txt** : História zložiek stresu a napätia.

**SIMCTRL_MEDC.DAT** : Kontrolné údaje simulácie MEDC
**MAT_MEDC.DAT** : materiálové parametre pre model MEDC
**TxrInfo.txt** : Základné informácie o textúre a počiatočné objemové zlomky pre všetky fázy

**RDTDND.txt** : Počiatočné osi textúry.
**ODF_S-1.txt** : Počiatočné hodnoty ODF
**EulerAng_S-1.txt** : Počiatočné Eulerove uhly a závažia

**InitGSize.txt* * : Počiatočná veľkosť zrna primárnej alfa

(2) Výstupné súbory zo spustiteľného súboru simulácie MEDC:

**ODF_FS.txt** : Konečné hodnoty ODF pre primárnu alfa, beta a sekundárnu alfa
**EulerAng_FS.txt** : Konečné Eulerove uhly a závažia pre primárnu alfa, beta a sekundárnu alfa

**HTRES.txt** : údaje o mikroštruktúre pre všetky uložené kroky v nominálnej databáze (číslo kroku, veľkosť primárnych alfa častíc, objemové frakcie primárnej alfa, beta, sekundárnej alfa a celkovej alfa, počiatočná teplota pre tvorbu sekundárnej alfa a kritická rýchlosť ochladzovania pre tvorbu sekundárnej alfa).

(3) Pre viacfázové zliatiny titánu sa poskytujú tieto údaje:

**PrimAlphaSize.Dat** : počiatočná a konečná primárna veľkosť alfa

**FinalTexture.Dat** : Konečné údaje o textúre pre primárnu alfa, beta a celkovú alfa v Bungeovej notácii v radiánoch.

vzoru.

Po dokončení simulácie sú všetky vybrané body uvedené v položke „**Výstup** “ v strome úloh. Zadajte číslo kroku v prehliadači krokov (malo by byť v rozsahu definovanom na stránke kontroly simulácie MEDC) a vyberte bod, výsledky simulácie je možné skontrolovať. Obr. MEDCL.18 zobrazuje hodnoty stavových premenných v poslednom kroku a môžeme vykresliť krivku každej stavovej premennej voči času alebo teplote. Tieto stavové premenné zahŕňajú (1) teplotu, (2) primárnu veľkosť alfa, (3) primárnu objemovú frakciu alfa, (4) objemovú frakciu beta, (5) sekundárnu objemovú frakciu alfa, (6) celkovú objemovú frakciu alfa, (7) sekundárnu počiatočnú teplotu alfa, (8) kritickú rýchlosť chladenia pre tvorbu sekundárnej alfa.

Obr. MEDCL.19 zobrazuje grafické používateľské rozhranie na zobrazenie údajov o textúre a nástrojov na analýzu textúry. Na vykonanie analýzy textúry je potrebné špecifikovať osi textúry v globálnom súradnicovom systéme. Ich hodnoty sa môžu líšiť od počiatočných osí textúry definovaných na stránke „Počiatočná textúra a mikroštruktúra“. Tu je RD zarovnaný v globálnom smere X, TD v globálnom smere Z a ND v globálnom zápornom smere Y. Obr. MEDCL.19 je tiež príkladom nastavenia na analýzu štruktúry celkovej alfa. Obr. MEDCL.20 vykresľuje pólové hodnoty primárnej alfa, beta, sekundárnej alfa a celkovej alfa v bode 1; Obr. MEDCL.21 vykresľuje pólové čísla v bode 2. Porovnaním pólových hodnôt sekundárnej alfa a beta sa pozoruje silný Burgersov vzťah medzi beta a sekundárnou alfa, t. j. (0001) ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/alpha.jpg' | relative_url }})// (110)![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/beta.jpg' | relative_url }}) a <11-20> ![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/alpha.jpg' | relative_url }})// <111>![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/beta.jpg' | relative_url }}).

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0018.jpg' | relative_url }})

Výstup: Stavová premenná a jej vývoj

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0019.jpg' | relative_url }})

Výstup: orientačné údaje a nástroje na analýzu textúry na vykreslenie obrysu ODF, čísla pólov, čísla inverzných pólov a výpočet čísla Kearns pre fázu HCP. Toto grafické používateľské rozhranie je tiež príkladom na vykreslenie pólových čísel celkovej alfa.

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0020.jpg' | relative_url }})

(a)

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0021.jpg' | relative_url }})

(b)

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0022.jpg' | relative_url }})

(c)

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0023.jpg' | relative_url }})

(d)

Výstup: pólové hodnoty pre bod 1: (a) primárna alfa; (b) beta; (c) sekundárna alfa; (d) celková alfa

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0024.jpg' | relative_url }})

(a)

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0025.jpg' | relative_url }})

(b)

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0026.jpg' | relative_url }})

(c)

![]({{ '/assets/images/labs/material_suite_labs/medc_model_lab/image0027.jpg' | relative_url }})

(d)

Výstup: pólové hodnoty pre bod 2: (a) primárna alfa; (b) beta; (c) sekundárna alfa; (d) celková alfa
