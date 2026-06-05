---
lang: sk
title: "9.1. Nastavenia typu simulácie"
---

# 9.1. Nastavenia typu simulácie

9.1.1. Informácie o simulácii

9.1.2. Typ geometrie

9.1.3. Jednotky

9.1.4. Typ

9.1.5. Simulačné režimy

Hlavné nastavenia pre 2D a 3D sú zobrazené na obr. 9.1.1.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_simulation_controls/9_image001.jpg' | relative_url }})

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_simulation_controls/9_image002.jpg' | relative_url }})

b)

Okno hlavných nastavení; (a) pre 2D a (b) pre 3D

## Informácie o simulácii

  * **Názov simulácie (TITLE) [2D, 3D]** : Pole „Názov simulácie“ ([TITLE](/docs/sk/keyword_documentation/t/title/)) slúži na zadanie názvu úlohy (max. 80 znakov) pre referenčné účely.

  * **Názov operácie (OPRNAM) [2D, 3D]** : Názov operácie (OPRNAM) slúži na označenie konkrétnej operácie (max. 64 znakov) pre účely referencie.

  * **Názov simulácie (SIMNAM) [2D, 3D]** : Názov simulácie ([SIMNAM](/docs/sk/keyword_documentation/s/simnam/)) slúži na označenie konkrétnej operácie (max. 64 znakov) pre účely referencie.

  * **Číslo operácie (CURSIM) [2D, 3D]** : Umožňuje zadať nové číslo operácie ([SIMNAM](/docs/sk/keyword_documentation/s/simnam/)) pre každú operáciu v databáze. Ak sú špecifikované čísla operácií, postprocesor zobrazí každú operáciu s jej číslom v zozname krokov.

  * **Číslo simulácie (CURSIM) [2D, 3D]**: Umožňuje zadať nové číslo simulácie ([SIMNAM](/docs/sk/keyword_documentation/s/simnam/)) pre každú simuláciu v databáze. Ak sú čísla simulácií zadané, postprocesor zobrazí každú simuláciu spolu s jej číslom v zozname krokov.

  * **Číslo siete (MESHNO) [2D, 3D] :** Táto premenná zaznamenáva aktuálnu sieť na základe počtu prepočítaní siete ([MESHNO](/docs/sk/keyword_documentation/m/meshno/)), ku ktorým došlo medzi počiatočnou sieťou a aktuálnou sieťou. Túto premennú by sa nemalo meniť.

##  Typ geometrie (GEOTYP) [2D]

V programe DEFORM je v súčasnosti možné nastaviť sedem typov geometrických modelov ([GEOTYP](/docs/sk/keyword_documentation/g/geotyp/)):

  * **Osovo symetrické**: Osovo symetrické modely sa modelujú ako priečny rez vzhľadom na stredovú os. Preto model vyžaduje, aby deformovaná geometria bola osovo symetrická a nachádzala sa v prvom a štvrtom kvadrante (t. j. X > 0). Okrem toho systém predpokladá, že prúdenie v každej radiálnej rovine je identické. (Pozri obr. 9.1.2.)

  * **Rovinné deformácie:** Pri rovinných deformáciách sa predpokladá, že geometria má jednotkovú hĺbku a že predná aj zadná plocha sú fixované. Simulácia vychádza z predpokladu, že objekty sa budú správať rovnako v akomkoľvek priereze v smere šírky aj výšky objektu. (Pozri obr. 9.1.2.)

  * **Krútenie:** Modely krútenia sú osovo symetrické modely. Pojem torzie je spôsob charakterizovania skrútenia alebo závitu. (Pozri obr. 9.1.2.). Typickou aplikáciou je modelovanie inercionného zvárania, kde je jedna časť s torzným pohybom a axiálnou silou pritlačená proti nehybnej časti, pričom výpočty sa vzťahujú aj na obvodový smer.

  * **Rovinné napätie**: Model rovinného napätia predpokladá, že hrúbka v smere z má jednotkové rozmery. Simulácia vychádza z predpokladu, že objekty sa budú správať rovnako v akomkoľvek priereze v smere šírky aj výšky objektu. Model rovinného napätia podporuje plastické, elastické a elasto-plastické objekty. (Pozri obr. 9.1.2.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_1_simulation_type_settings/9_1_image001.jpg' | relative_url }})

Príklad typov geometrických modelov

  * **2,5D trenie**: V programe DEFORM-V12 bola pridaná voľba typu geometrie pre 2,5D trenie; pomocou tejto voľby môže používateľ nastaviť operáciu 2,5D lineárneho trenia.

  * **2,5D valcovanie**: V programe DEFORM-V12 bola pridaná možnosť typu geometrie „2,5D valcovanie“. Pomocou tejto možnosti môže používateľ nastaviť operáciu 2,5D valcovania s údajmi o počte profilov.

  * **2,5D valcovanie**: V programe DEFORM-V12 bola pridaná možnosť typu geometrie pre 2,5D valcovanie. Pomocou tejto možnosti môže používateľ nastaviť operáciu 2,5D valcovania na základe údajov o prierezoch.

## Jednotky (UNIT) [2D, 3D]

Systém jednotiek v programe DEFORM ([UNIT](/docs/sk/keyword_documentation/u/unit/)) je možné nastaviť na anglický alebo metrický (SI). (Pozri obr. 9.1.1.) Všetky informácie v DEFORM by mali byť vyjadrené v jednotných jednotkách. Systém jednotiek by mal byť zvolený na začiatku postupu nastavenia problému a nemal by sa meniť počas simulácie ani po operácii. (Viac informácií o jednotkách premenných v DEFORM nájdete v [Table 1.9.1](../../about_deform/1_introduction_to_deform/1_9_units.htm#Table_DEFORM_unit_system))

##  Typ (STYPE)

Medzi rôzne typy simulácií ([STYPE](/docs/sk/keyword_documentation/s/stype/)), ktoré je možné spustiť, patria:

  * **Lagrangeov inkrementálny prístup [2D, 3D**]: Určený pre všetky bežné aplikácie [forming](/docs/sk/operation_templates/33_forming/33_introduction_to_forming/), [ heat transfer](/docs/sk/operation_templates/35_heat_transfer/35_introduction_to_heat_transfer_operations/) a [heat-treat](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/) (pozri obr. 9.1.1.). V tomto všeobecnom rámci je možné modelovať aj prechodnú fázu procesov, ako je valcovanie, [machining](/docs/sk/operation_templates/39_cutting/39_introduction_to_cutting/), [extrusion](/docs/sk/operation_templates/31_extrusion/31_introduction_to_extrusion/), ťahanie, [cogging](/docs/sk/operation_templates/29_cogging/29_introduction_to_cogging/) atď.

  * **ALE valcovanie [3D]**: Model ALE pre proces valcovania je možné vytvoriť pomocou šablóny „[Shape](/docs/sk/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/)[ Rolling template](/docs/sk/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/)“ (pozri obr. 9.1.1b.). Pri generovaní modelu pomocou tejto šablóny sa automaticky vygenerujú potrebné okrajové podmienky pre vstupnú plochu sochoru (v rozhraní označenú ako Počiatočná plocha, uzlom je priradené [BCCDEF](/docs/sk/keyword_documentation/b/bccdef/)=4) a výstupnej ploche (v rozhraní označenej ako Voľná plocha, uzlom sú priradené [BCCDEF](/docs/sk/keyword_documentation/b/bccdef/)=5). Šablóna automaticky nastaví typ analýzy na „ALE Rolling“. Pri nastavení modelu valcovania pomocou bežného preprocesora musí používateľ nastaviť tento typ analýzy a správne okrajové podmienky, aby mohol spustiť model ALE pre valcovanie. Od verzie 3DV6.1 bola táto funkcia vylepšená o automatické kritériá zastavenia po detekcii podmienok ustáleného stavu.

  * **Obrábanie v ustálenom stave [2D, 3D]** : Model 2D/3D obrábania pre sústruženie je možné vygenerovať pomocou „[Machining](/docs/sk/operation_templates/39_cutting/39_introduction_to_cutting/)[ ](/docs/sk/operation_templates/39_cutting/39_introduction_to_cutting/) [Template](/docs/sk/operation_templates/39_cutting/39_introduction_to_cutting/)“, pričom počiatočný model je možné nastaviť pre Lagrangeov inkrementálny beh. (Pozri obr. 9.1.1.) Keď sa vytvorí dostatočné množstvo triesok, šablónu možno použiť na generovanie dodatočnej operácie na prepnutie režimu analýzy do ustáleného stavu. V tejto fáze sa šablóna môže použiť na generovanie požadovaných okrajových podmienok pre beh v ustálenom stave, čo zahŕňa definovanie koncovej plochy špony (označenej ako voľná plocha, s kódom [BCCDEF](/docs/sk/keyword_documentation/b/bccdef/) nastaveným na 5 pre tieto uzly). Šablóna automaticky nastaví typ analýzy na „Steady-State Machining“. Keď je model obrábania nastavený pomocou bežného preprocesora, používateľ musí nastaviť tento typ analýzy a správne podmienky voľnej hladiny a tepelné okrajové podmienky, aby mohol spustiť model ustáleného stavu pre obrábanie.

  * **Válcovanie prstencov [3D]**: Od verzie 3D-V6.1 bol simulačný engine vylepšený tak, aby zvládal neizotermické modelovanie procesu [ring rolling](/docs/sk/operation_templates/42_ring_rolling/42_introduction_to_ring_rolling/). (Pozri obr. 9.1.1b.) Tento vývoj zahŕňa špeciálnu techniku ALE, ktorá nie je závislá od žiadnych nákladných výpočtových zdrojov a nevyžaduje veľmi dlhé časy modelovania. Od verzie 3D-v10.0 bol tento špeciálny riešiteľ ALE ďalej vylepšený, aby využíval výhody paralelných prostredí (časť riešiteľa).

  * **Extrúzia v ustálenom stave [3D]**: Ak chce používateľ zistiť posun a ďalšie stavové veličiny po dosiahnutí ustáleného stavu pri extrúzii, môže zvoliť túto možnosť. Táto možnosť je k dispozícii aj v rámci operácie [Extrusion](/docs/sk/operation_templates/31_extrusion/31_introduction_to_extrusion/) v prostredí DEFORM MO v sekcii Explorer. Používateľ môže simulovať len 5 až 10 krokov v závislosti od zložitosti geometrie extruzie.

  * **Extrúzia ALE [3D]**: Ak chce používateľ nastaviť model extrúzie ALE v predspracovateľovi, musí vybrať prepínač „Extrúzia ALE“, ako je znázornené na obr. 9.1.1b. Operáciu ALE Extrusion je možné nastaviť aj pomocou operácie Extrusion v prehliadači v grafickom rozhraní DEFORM MO.

  * **Zváranie ALE Stir [3D]**: Ak chce používateľ v programe DEFORM-V12 v predspracovateľovi nastaviť model zvárania ALE Stir, musí zaškrtnúť príslušné políčko.

  * **ALE Spinning [3D]**: V programe DEFORM-V12 musí používateľ, ak chce v predspracovateľovi nastaviť model ALE Spinning, vybrať prepínač ALE Spinning. Operáciu ALE [spinning](/docs/sk/operation_templates/48_spinning/48_introduction_to_spinning/) je možné nastaviť aj pomocou operácie 3D Spinning, ktorá je k dispozícii v prehliadači v grafickom rozhraní DEFORM MO.

  * **Elektromagnetické tvárnenie****[3D]**: Ak chce používateľ v programe DEFORM-V12 v predspracovateľovi nastaviť model elektromagnetického tvárnenia, musí zaškrtnúť políčko „Elektromagnetické tvárnenie“.

  * **ALE Spinning (express) [3D]** : V programe DEFORM-v12.1 si môže používateľ vybrať riešiteľ ALE express, čím urýchli simuláciu ALE spinningu.  
Ak je zvolený tento riešiteľ, valec musí mať v strede otvor a medzi vretenom a koníkom a obrobkom musia byť definované kritériá neoddelenia.

  * **ALE Tube piercing [3D]:** V programe DEFORMv12.1.1, ak chce používateľ v predspracovateľovi nastaviť model pre dierovanie rúr, mal by vybrať prepínač „ALE Tube piercing model“. Operáciu ALE Tube piercing je možné nastaviť aj pomocou operácie 3D Spinning, ktorá je k dispozícii v prehliadači v grafickom rozhraní Deform MO.

## Simulačné režimy (SMODE, TRANS)

[2D, 3D]: Program DEFORM ponúka skupinu simulačných režimov, ktoré je možné zapínať alebo vypínať jednotlivo, alebo používať v rôznych kombináciách. (Pozri obr. 9.1.3.) Z dôvodu spätnej kompatibility so starými kľúčovými slovami a databázami pred verziou 3.0 sa načíta kľúčové slovo [SMODE](/docs/sk/keyword_documentation/s/smode/) (starý štýl izotermický, neizotermický, prenos tepla) a v preprocesore sa nastavia príslušné prepínače režimu kľúčového slova TRANS. 

  * **Deformácia:** Simuluje deformáciu spôsobenú mechanickými, tepelnými vplyvmi alebo fázovými premenami. 

  * **Prenos tepla:** Simuluje tepelné javy v rámci simulácie, vrátane prenosu tepla medzi objektmi a okolím, ako aj tvorby tepla v dôsledku deformácie alebo fázovej premeny, ak je to relevantné.

  * **CFD prúdenie**: Pomocou tejto možnosti môže používateľ simulovať javy prúdenia tekutín na základe zákonov zachovania, ktoré riadia pohyb tekutín. V prípade 2D bude podporovaný iba typ geometrie „Rovinné deformácie“.

  * **Transformácia**: Simuluje transformáciu medzi fázami v dôsledku termomechanických a časových vplyvov.

  * **Difúzia**: Simuluje difúziu atómov uhlíka v materiáli v dôsledku gradientov obsahu uhlíka.

  * **Zrno**: Simuluje výpočet veľkosti zŕn a výpočty rekryštalizácie.

  * **Ohrev**: Simuluje tvorbu tepla v dôsledku odporového alebo indukčného ohrevu. Na simuláciu rôznych ohrevných procesov je možné použiť indukčný ohrev, indukčný ohrev metódou BEM (metóda hraničných prvkov) a odporový ohrev (k dispozícii od verzie DEFORM v11.0). 3D FEM engine z DEFORM v11.0 teraz dokáže spracovať modely indukčného ohrevu s dvojfrekvenčnými vstupnými údajmi pre frekvenciu prúdu. Príklady prípadov ohrevu nájdete v priečinku DATA v časti Príklady ohrevu.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_1_simulation_type_settings/9_1_image002.jpg' | relative_url }})

Okno Ovládacie prvky simulácie – Kúrenie

**Súvisiace témy:**

[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.6. Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)   
[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)

[9.10. Output controls](/docs/sk/pre_processor/9_simulation_controls/9_10_output_controls/)
