---
lang: sk
title: "9.5. Nastavenia riešiteľa"
---

# 9\. 5. Nastavenia riešiteľa ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }})

9.5.1. Riešiteľ deformácií (SOLMTD)

Riešiteľ

Riešiteľ riedkych matíc

Riešiteľ iterácií

Špeciálny riešiteľ

Explicitný riešiteľ

Iteračné metódy (ITRMTH)

Priamo

Newton-Raphsonova metóda  
9.5.2. Riešiteľ teplotných rovníc (SOLMTT)

9.5.3. Riešiteľ indukčného ohrevu (SOLMTI)

9.5.4. Pokročilé

Limity konvergenčnej chyby (CVGERR)

Maximálny počet iterácií (ITRMXD, ITRMXT)

Optimalizácia šírky pásma (DEFBWD, TMPBWD)

Kritériá riešiteľa určujú podmienky, ktoré riešiteľ FEM používa na nájdenie riešenia v každom kroku simulácie úlohy. Pre väčšinu úloh by mali byť predvolené hodnoty postačujúce. V prípade, že nedôjde ku konvergencii, môže byť potrebné tieto hodnoty zmeniť (pozri obr. 9.5.1.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image001.jpg' | relative_url }})

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image002.jpg' | relative_url }})  
b) 

Nastavenia riešiteľa pre riešiteľ deformácií; (a) pre 2D (b) pre 3D

## Riešiteľ deformácií (SOLMTD) [2D, 3D]

**Riešiteľ**

  * **Riešiteľ riedkych matíc**

Riešiteľ pre riedke matice ([SOLMTD](/docs/sk/keyword_documentation/s/solmtd/)) pri riešení rovníc využíva vlastnosti maticových rovníc DEFORM. Je efektívny, najmä pri riešení rozsiahlych úloh.

  * **SPOOLES a MUMPS [2D, 3D] :**

Riešitelia riedkych matíc SPOOLES a MUMPS sú novšie a efektívnejšie, najmä pri riešení rozsiahlejších úloh. V nadchádzajúcej verzii V12.0 bude riešiteľ MUMPS s iteračnou metódou Newton-Raphson novým predvoleným riešiteľom pre všetky simulácie (plastické, elastoplastické, riadené silou atď.). V 3D sa musí používať na rotačne symetrických modeloch s mriežkou typu brick.

  * **MUMPS [3D] :**

****

  * **Skyline [2D] :**

Algoritmus Skyline je veľmi jednoduchý spôsob riešenia inverzie matíc. Ide o pôvodný algoritmus, ktorý sa používal v programe DEFORM, a je udržiavaný predovšetkým z dôvodu spätnej kompatibility. Je spoľahlivý, ale nie nevyhnutne efektívny.

  * **Riešiteľ iterácií**

  * **Konjugovaný gradient [3D]**

Riešiteľ pre riedke matice ([SOLMTD](/docs/sk/keyword_documentation/s/solmtd/)) je metóda priameho riešenia, ktorá využíva riedkosť formulácie FEM na zvýšenie rýchlosti výpočtu. Riešiteľ s konjugovanými gradientmi sa snaží vyriešiť problém FEM prostredníctvom iteratívneho približovania sa k riešeniu. 

Vo verzii 11.3 je predvoleným 3D riešiteľom pre simulácie s plastickými objektmi konjugovaný gradient (CG) s priamymi iteráciami. Konkrétne je predvoleným riešiteľom „starý a nový“ CG (úroveň vyplnenia = 4, metóda rozdelenia = 1), pričom riešiteľ MUMPS slúži ako záloha v prípade potreby konvergencie. Elasto-plastické (EP) simulácie nemôžu používať metódu priamych iterácií, preto sa pre EP odporúča riešiteľ MUMPS s Newton-Raphsonovými iteráciami.

  * **GMRES [3D]**

Pri riešení určitých úloh ponúka tento riešiteľ oproti riešiteľu pre riedke matice obrovské výhody.  
Medzi výhody iteratívneho riešiteľa patria:

  * Zkrácenie celkového času riešenia až o 5:1, najmä pri veľmi rozsiahlych úlohách 
  * Schopnosť spracovať veľmi veľký počet prvkov v primeranom čase a s primeranými nárokmi na pamäť. (Najväčší doterajší problém predstavuje 380 000 tetraedrických prvkov, ktoré na 32-bitovom počítači spotrebujú 1 GB pamäte RAM). Od verzie 3Dv10.0 bol FEM engine ďalej vylepšený, aby využíval výhody 64-bitových prostredí Linuxu, čím je schopný spracovať modely oveľa väčších rozmerov. 
  * Omnoho nižšie nároky na pamäť pri menších úlohách – vďaka čomu je 3D praktické aj na lacných počítačoch alebo notebookoch.

  
**Obmedzenia:**

  * V niektorých situáciách môže byť konvergencia pomalšia alebo simulácia nemusí vôbec konvergovať, hoci riešiteľ pre riedke matice by konvergoval. Ide najmä o problém pri simuláciách s výrazným „pohybom tuhého telesa“, ku ktorému dochádza napríklad vtedy, keď sa súčiastka usadzuje v forme, prechádza miernou deformáciou alebo sa ohýba.

  
Ak sa riešiteľ s konjugovaným gradientom nedokáže úspešne priblížiť k riešeniu, program DEFORM-3D prejde na riešiteľ pre riedke matice. Od verzie 3DV61 bol do ponuky riešiteľov pridaný nový riešiteľ GMRES, ktorý využíva výhody prostredí s viacerými procesormi. Možnosť GMRES je možné použiť iba v režime viacerých procesorov.

**Kedy použiť iteratívny riešiteľ**

****Tento riešiteľ sa vo všeobecnosti veľmi dobre hodí na úlohy s veľkým množstvom kontaktov s formami. Ak nie je obrobok v formách správne umiestnený alebo ak sa bude pred začiatkom deformácie trochu posúvať, mali by ste simuláciu spustiť s riešiteľom pre riedke matice. Akonáhle dôjde k podstatnej deformácii obrobku, zastavte simuláciu, načítajte posledný krok do preprocesora, prejdite na „Conjugate Gradient“ a „Direct“ a zapíšte databázu. Obr. 9.5.2 uvádza odporúčané metódy riešiteľa a iterácie pre 3D model.  
Pri prvých niekoľkých krokoch sledujte súbor s hláseniami. Konvergencia prvého kroku môže trvať trochu dlhšie. Ak sa druhý krok stále nedokáže zkonvergovať alebo ak sa simulácia zastaví, možno bude potrebné na niekoľko ďalších krokov prejsť späť na riešiteľ pre riedke matice.  
Všeobecne platí, že simulácie, pri ktorých by sa pri použití riešiteľa typu „Sparse“ mohli vyskytnúť problémy s konvergenciou, nie sú vhodné pre metódu konjugovaných gradientov. Väčšina úloh, najmä v prípade tenkých alebo prebytkových častí, dosiahne uspokojivé výsledky už po prvých 20 až 30 krokoch, ak nie skôr.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image003.jpg' | relative_url }})

Graf závislosti času od prvkov pre rôzne riešiče pri elastických objektoch

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image004.jpg' | relative_url }})

Graf závislosti pamäte od počtu prvkov pre rôzne riešiče pri elastických objektoch

  * **Špeciálny riešiteľ [3D]**

Kategória „Špeciálne riešiče“ obsahuje niekoľko novo vyvinutých možností, ktorých cieľom je urýchliť riešenie veľmi rozsiahlych 3D simulácií (s miliónmi prvkov). 

  * **Rozklad domén (DD)**

Dekompozícia domén (DD) rozdeľuje obrobok na niekoľko malých čiastkových domén, z ktorých každú je možné riešiť samostatne na rôznych jadrách. Nie je možné ju použiť s nástrojmi s mriežkou ani s kompenzáciou objemu založenou na metóde konečných prvkov (FEM). Dekompozícia domén (DD) je založená na riešiteľovi MUMPS.

Metódu rozkladu domén je možné použiť iba pre typy objektov „Rigid Plastic“ s tetrahedrálnou sieťou. 

Pri veľmi rozsiahlych úlohách môže byť rozklad na domény rýchlejší.

  * **Dual Mesh (DM)**

Metóda dvoch sietí (DM) využíva na obrobku súčasne jemnú aj hrubú sieť, pričom riešenie z hrubej siete slúži ako počiatočný odhad pre jemnú sieť. Týmto spôsobom je možné výrazne zvýšiť rýchlosť výpočtu metódou CG.

„Faktor dvojitej veľkosti siete“ N bude určovať veľkosť hrubej siete; počet prvkov v hrubej sieti bude predstavovať 1/N pôvodného obrobku.

V programe Gui-Pre je predvolená hodnota 8. Možné sú hodnoty v rozmedzí 5 až 10.

  * **DD+DM**

Tento prístup rozloží model tak, aby sa riešenie rozdelilo medzi viaceré procesory, čím sa dá skrátiť čas výpočtu pri veľkých elasto-plastických modeloch. Metóda DD+DM sa stále vyvíja, ale pokojne ju vyskúšajte a zistite, či by jej techniky mohli byť prínosom pre vašu aplikáciu.   
Túto funkciu nie je možné používať s mriežkovanými nástrojmi ani s kompenzáciou objemu založenou na metóde konečných prvkov.  
DD+DM je samostatný, jedinečný riešiteľ, ktorý vychádza z prvkov riešiteľov DD a DM.

  * **Riešiteľ s čiastočnou oblasťou**: „**Riešiteľ s čiastočnou oblasťou**“ je k dispozícii v sekcii Špeciálne riešitelia a momentálne je dostupný len pre typy simulácií „Lagrangeov inkrementálny“ a „ALE spinning“. Tento riešiteľ simuluje lokalizovanú deformáciu v rámci špecifikovanej aktívnej oblasti. V časti Čiastočná doména má používateľ možnosť použiť Rýchle vyhodnotenie. Rýchle vyhodnotenie umožňuje presunúť stred otáčania pozdĺž vybranej osi. Používateľ môže definovať aktívnu doménu pre objekty, ktoré sa majú zohľadniť pri výpočte, v tabuľke v časti Ovládacie prvky riešiteľa. Neaktívnu doménu nad obrobkom je možné definovať na stránke Vlastnosti obrobku.

    * **Rýchly výpočtový modul**: Rýchly výpočtový modul rieši jednokrokový model (na jednu otáčku) pre inkrementálne rotačné tvárnenie a momentálne je k dispozícii len pre technológiu ALE Spinning. Metóda rýchleho výpočtu s modulom pre čiastočnú oblasť môže zvýšiť výpočtovú efektívnosť a je vhodná na parametrické štúdie slúžiace na počiatočnú kontrolu návrhu spracovania.

    * **Rýchle vyhodnotenie s posuvným stredom otáčania**: Túto možnosť môžeme zvoliť, aby sa posuvný stred otáčania objektov aktualizoval podľa smeru vybraného z roletového zoznamu „Smer“.

    * **Celkový uhol aktívnej oblasti**: Pomocou tejto možnosti môžeme určiť celkový uhol aktívnej oblasti, v rámci ktorej sa vykonávajú výpočty. 

    * **Osa otáčania**: Táto voľba slúži na definovanie osi otáčania objektu. Pre vybranú os otáčania môžeme na stránke Vlastnosti – v záložke Čiastočná doména obrobku definovať neaktívnu doménu.

    * ![]({{ '/assets/icons/pre_icons/mo_preview_button.jpg' | relative_url }})**Náhľad** : Pomocou tohto tlačidla náhľadu môžeme na obrobku sledovať aktívnu oblasť pre zónu výpočtu čiastočnej domény. Aktívna oblasť bude v zobrazenom regióne zvýraznená bielou farbou, ako je znázornené na obr. 9.5.4.

    * **Pridať**![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) : Pomocou tohto tlačidla môžeme do zoznamu pridať objekty, pre ktoré sa definuje aktívna doména, ak nie sú pridané automaticky. V súčasnosti sa do tabuľky automaticky pridávajú objekty, ktoré obsahujú údaje o pohybe (rýchlosť, dráha). 

    * **Odstrániť**![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) : Pomocou tohto tlačidla môžeme pridané objekty zo zoznamu odstrániť.

    * **Obmedzenia hraníc** :

      1. **Metódy**: V roletovom zozname „Metódy“ sú k dispozícii metódy „Tuhosť prúžku“ alebo „Penalty spring“, ktoré je možné použiť na čiastkovú oblasť.

      2. **Mierka****:** pomocou tejto možnosti môžeme nastaviť hodnotu mierky pre okrajové obmedzenia.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image010.jpg' | relative_url }})

Možnosti riešiteľa čiastočných domén

  * **Explicitný riešiteľ** [3D]:

  * **Explicitné:**

Pre 3D simulácie je teraz k dispozícii explicitný riešiteľ. Explicitný riešiteľ nevyžaduje žiadne iterácie a rýchlosti v uzloch sa počítajú priamo. Explicitné riešitelia sa zvyčajne používajú na simuláciu procesov, ktoré trvajú veľmi krátko (napríklad automobilové nehody). Časový krok v explicitnej analýze musí byť veľmi malý – menší ako čas, ktorý potrebuje zvuková vlna na prekonanie prvku. Implicitné simulácie naopak nemajú žiadne vnútorné obmedzenie veľkosti časového kroku, takže implicitné časové kroky sú zvyčajne o niekoľko rádov väčšie ako explicitné časové kroky. Ak je modelovaný proces veľmi krátky alebo sa vyžadujú veľmi malé časové kroky, explicitný riešiteľ môže byť vhodnou voľbou. Ak chcete vyskúšať explicitný riešiteľ, kontaktujte technickú podporu DEFORM.

**Odporúčania riešiteľa:**

Keďže sme už opísali riešiče pre 2D a 3D, bolo by užitočné mať k dispozícii tabuľku s podrobným prehľadom odporúčaných riešičov pre rôzne nastavenia modelov.

**2D**  
---  
**Typ obrobku** | **Typ nástroja** | **Pohyb** | **Predvolený riešiteľ** | **Alternatívny riešiteľ**  
Všetko | Všetko | Všetko  | MUMPS/NR | Skyline/NR  
  
Ako vyplýva z tabuľky, vo všetkých prípadoch sa odporúča riešiteľ MUMPS. Pri malých úlohách majú všetky riešitelia v podstate rovnakú rýchlosť. S rastúcou veľkosťou úlohy sa riešiteľ MUMPS stáva najrýchlejšou voľbou.

**3D**  
---  
**Typ obrobku** | **Typ nástroja** | **Pohyb** | **Preferovaný riešiteľ** | **Alternatívny riešiteľ**  
Plast (jednoduchý) | Tuhý | Rýchlosť | Záloha CG/MUMPS | MUMPS/NR  
| Dual Mesh1  
Rozklad domén2  
Plast (jednoduchý) | Tuhý | Sila | MUMPS/NR | Rozklad domény 2  
Plast (jednoduchý) | Tuhý  | Hydraulický lis | Podpora CG/MUMPS | MUMPS/NR  
| Dual Mesh1  
Plastika (rotačná symetria) | Tuhý  | Rýchlosť  | Záloha CG/MUMPS | MUMPS/NR3  
Plastový  | Pružný | Akýkoľvek  | MUMPS/NR | CG bude fungovať, ale je výrazne pomalší  
Viac plastov | Akékoľvek  | Akékoľvek  | MUMPS/NR | Žiadne  
Elastoplastické  | Tuhé (bez siete) | Rýchlosť  | MUMPS/NR | Kombinované DM / DD pre veľmi veľké modely  
Elastoplastické  | Tuhé (bez siete) | Sila  | Kombinácia DM / DD pre veľmi veľké modely  
Elastoplastický | Žiadny  
(WP – Testy zmiešaných zložiek) | Tepelné zaťaženie | Kombinované DM / DD pre veľmi veľké modely  
Elastoplastický | Elastický/  
Tvrdý (so sieťovinou) | Rýchlosť | Žiadny  
Iba elastické | Tuhé alebo elastické | Rýchlosť / Žiadna | Záloha CG/MUMPS | MUMPS/NR4 je prijateľné, ale vo všeobecnosti pomalšie  
Iba pružné | Tuhé alebo pružné | Sila  | MUMPS/NR4 | Žiadne  
Porézny  | Tuhý  | Rýchlosť  | Záloha CG/MUMPS | MUMPS/NR  
Porézny  | Akákoľvek kombinácia okrem nástroja Rigid / riadenia rýchlosti | MUMPS/NR | Žiadne  
1 Pri metóde Dual Mesh je potrebné použiť tetraedrickú sieť. Metóda DM môže byť rýchlejšia pri riešení veľmi rozsiahlych úloh.  
2 Pri dekompozícii domén nie je možné použiť sieť na tuhých telesech a nie je možné využiť kompenzáciu objemu založenú na metóde konečných prvkov. Dekompozícia domén môže byť rýchlejšia pri riešení veľmi rozsiahlych úloh.  
3 Modely s rotačnou symetriou a mriežkou typu „brick“ MUSIA používať riešiteľ MUMPS.  
4 Ak sa vyskytnú problémy s konvergenciou, spustite program s MUMPS/NR a súborom „DEF_ELAON.DAT“ v pracovnom adresári (akceptuje „blízke“ riešenie s odchýlkou približne 10 % vo výsledkoch zaťaženia a napätia).  
  
Výber riešiteľa v 3D nie je taký jednoznačný ako v 2D. Väčšina 3D simulácií DEFORM zahŕňa jeden plastický obrobok a tuhé nástroje s riadenou rýchlosťou. Pre tieto simulácie by sa mal použiť riešiteľ CG. Pre elasto-plastické simulácie by sa mal použiť riešiteľ MUMPS. Odporúčaný riešiteľ pre všetky ostatné scenáre nájdete v tabuľke vyššie. 

**Iteračné metódy (ITRMTH)** **[2D, 3D]**

Iteračná metóda ([ITRMTH](/docs/sk/keyword_documentation/i/itrmth/)) je spôsob, akým sa aktualizuje (alebo iteruje) riešenie simulácie s cieľom priblížiť sa k konvergentnému riešeniu daného kroku.

  * **Priamy**

Priama metóda má väčšiu pravdepodobnosť konvergencie ako Newton-Raphsonova metóda, na dosiahnutie konvergencie však zvyčajne vyžaduje viac iterácií. V prípade poréznych materiálov je priama metóda v súčasnosti jedinou dostupnou metódou.

  * **Newton-Raphsonova metóda**

Metóda Newton-Raphson sa odporúča pre väčšinu úloh, pretože zvyčajne konverguje v menšom počte iterácií ako ostatné dostupné metódy. Je však pravdepodobnejšie, že riešenia pri tejto metóde nebudú konvergovať ako pri iných metódach.

  * **Metóda dĺžky oblúka**

  * **Zakázať iterácie medzi elastickými objektmi**

## Riešiteľ teplotných úloh ([SOLMTT](/docs/sk/keyword_documentation/s/solmtt/)) [2D, 3D]

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image005.jpg' | relative_url }})  
a) 

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image006.jpg' | relative_url }})  
b) 

Nastavenia iterácie teploty; (a) pre 2D (b) pre 3D

  * **Cievky**[2D, 3D]

  * **Skyline**[2D, 3D]

Zatiaľ čo riešiteľ typu Sparse je efektívny pri modeloch veľkých rozmerov, riešiteľ typu Skyline využíva metódu ukladania typu Skyline v kombinácii s Gaussovou elimináciou na ukladanie údajov teplotnej matice. Táto metóda sa odporúča pre väčšinu úloh.

  * **MUMPS** [2D, 3D]

  * **Konjugovaný gradient** [3D]

V porovnaní s inými typmi riešiteľov vyžaduje riešiteľ konjugovaných gradientov oveľa menej pamäte a pri rozsiahlych modeloch umožňuje rýchlejšie výpočty.

  * **Explicitné [3D]**

## Riešiteľ indukčného ohrevu ([SOLMTI](/docs/sk/keyword_documentation/s/solmti/)) [3D]

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image007.jpg' | relative_url }})

Nastavenia riešiteľa indukčného ohrevu

## Pokročilé

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image009.jpg' | relative_url }})

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_5_solver_settings/9_5_image008.jpg' | relative_url }})  
b) 

Pokročilé nastavenia riešiteľa; (a) pre 2D (b) pre 3D

**Limity konvergenčnej chyby (CVGERR) [2D, 3D]**

Iterácia deformácie sa považuje za konvergovalú, ak sú splnené limity chýb rýchlosti a sily ([CVGERR](/docs/sk/keyword_documentation/c/cvgerr/)). To znamená, že zmena normy uzlovej rýchlosti aj normy uzlovej sily je nižšia ako stanovená hodnota, ako je znázornené na obr. 9.5.7. Hodnoty normy chyby pre každý iteračný krok sa zobrazujú v súbore správ. Ak súbor správ ukazuje, že normy chyby sily alebo rýchlosti sa zmenšujú, ale neklesajú pod limity chyby, simulácia sa môže pokračovať zvýšením príslušného limitu chyby na najmenšiu hodnotu v súbore správ. Tým sa zníži presnosť riešenia, preto by sa simulácia mala nechať bežať niekoľko krokov a potom by sa hodnoty mali opäť znížiť. Pri tom je potrebné postupovať s mimoriadnou opatrnosťou.  
  
Pri výpočtoch napätia v lisovacej forme alebo zaťaženia lisu, kde sú potrebné mimoriadne presné hodnoty síl alebo zaťaženia, je možné zvýšiť presnosť zaťaženia znížením limitu chyby sily. Tým sa síce predĺži čas simulácie, ale výsledky budú presnejšie.

Poznámka:  
Je potrebné poznamenať, že presnosť údajov o prietokovom napätí bude mať veľký vplyv na presnosť predpovedí napätia v lisovacej forme a zaťaženia lisu.

**Maximálny počet iterácií (ITRMXD, ITRMXT)** **[2D, 3D]**

Pri použití Newton-Raphsonovej iterácie sa v každom iteračnom úseku vykoná zadaný počet iterácií ([ITRMXD](/docs/sk/keyword_documentation/i/itrmxd/) a [ITRMXT](/docs/sk/keyword_documentation/i/itrmxt/)), až kým riešenie nedosiahne konvergenciu. Počas segmentu Newton-Raphson sa vykoná maximálne 30 iterácií. Ak riešenie nekonverguje v zadanom počte iterácií a pri následnom automatickom znížení veľkosti kroku, simulácia sa ukončí a do súboru správ DEFORM sa zapíše správa.  
Ak je ako metóda iterácie špecifikovaná priama iterácia, vykoná sa stanovený počet iterácií. Ak riešenie nedosiahne konvergenciu, vykoná sa ďalšia séria iterácií. Ak riešenie stále nedosiahne konvergenciu, simulácia sa ukončí a do súboru správ DEFORM sa zapíše správa.

**Optimalizácia šírky pásma (DEFBWD, TMPBWD)****[2D, 3D]**

Optimalizácia šírky pásma ([DEFBWD](/docs/sk/keyword_documentation/d/defbwd/) a [TMPBWD](/docs/sk/keyword_documentation/t/tmpbwd/)) skracuje čas riešenia optimalizáciou štruktúry riešenej maticovej rovnice. Malo by sa používať takmer pri všetkých úlohách.

Súvisiace témy:

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.6. Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)   
[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)
