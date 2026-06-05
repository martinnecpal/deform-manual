---
lang: sk
title: "16.1. Deformation_Properties"
---

# 16.1. Deformačné vlastnosti

16.1.1. Výpočet tečenia

16.1.2. Elasto-plastický počiatočný odhad

16.1.3. Cieľový objem

16.1.4. Objemová penalizačná konštanta

16.1.5. Priemerná miera deformácie

16.1.6. Medzná miera deformácie

[16.1.7. Generalized plane strain control](/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/)

16.1.8. Aktualizácia ovládacích prvkov

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_Image001.jpg)

Okno Vlastnosti 2D objektu

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_Image002.jpg)

Okno Vlastnosti 3D objektu

## Výpočet plazivosti

Aktivuje výpočty tečenia ([CREEP](/docs/sk/Keyword_Documentation/C/CREEP/)) pre konkrétny objekt. Ďalšie informácie o dostupných modeloch creepu nájdete v časti [10.1.2. Creep](/docs/sk/pre_processor/10_Material_Data/10_1_Plastic_Data/10_1_2_Creep/10_1_2_Creep_Models/) (CREEP).

  
Ak by používateľ chcel v postprocesore vidieť napätie Creep, potom by sa malo aktivovať zaškrtávacie políčko Creep v ceste "Simulation controls![](../../../assets/Icons/Pre_icons/arrow_front.jpg) Advanced ![](../../../assets/Icons/Pre_icons/arrow_front.jpg) Output controls".

**Dodaný text týkajúci sa nových možností plazenia**

## Elasto-plastický počiatočný odhad (ELPSOL) [2D, 3D]

Konvergencia elasto-plastického riešenia ([ELPSOL](/docs/sk/Keyword_Documentation/E/ELPSOL/)) závisí od počiatočného odhadu stavu napätia a deformácie. K dispozícii sú tri počiatočné odhady riešení:

  * **Plastový roztok** : Na vytvorenie počiatočného odhadu používa čisto plastické údaje o deformácii.
  * **Elastické riešenie** : Na vytvorenie počiatočného odhadu sa používajú čisto elastické údaje o deformácii.
  * **Riešenie v predchádzajúcom kroku** : Na vytvorenie počiatočného odhadu použije elastoplastické riešenie z predchádzajúceho kroku.

Zdá sa, že riešenie predchádzajúceho kroku poskytuje vo väčšine prípadov najlepšiu konvergenciu. Ak je konvergencia
je pre konkrétny problém nedostatočná, možno použiť pružné alebo plastické riešenie.

## Cieľový objem (TRGVOL) [2D, 3D]

Zachovanie objemu deformujúceho sa objektu v simulácii je veľmi dôležité pre presné predpovede modelu. Samotná dobrá veľkosť siete a jemnejší časový krok nedokážu zabezpečiť konštantnosť objemu pre niektoré triedy simulácií. Používateľ teraz môže aktivovať kompenzáciu objemu v rámci možnosti "Properties" (Vlastnosti) (pozri obr. 16.1.1. a obr. 16.1.2.).

  
Môžete zapnúť "Aktivovať možnosti cieľového objemu" ([TRGVOL](/docs/sk/Keyword_Documentation/T/TRGVOL/)) a potom použiť ![](../../../assets/Icons/Pre_icons/MO_Target_volume_icon.jpg) na automatický výpočet objemu. Ak je kompenzácia objemu zapnutá, potom sa počas behu simulácie objem siete kompenzuje na uvedenú hodnotu.

  
Pri analýze metódou konečných prvkov existuje niekoľko príčin objemových strát.

  * Formulácia pokuty, ktorú používa DEFORM, prirodzene stratí zlomok objemu v každom kroku. Je to normálne a vo všeobecnosti to nepredstavuje významný dôvod na obavy.

  * Ak sa použije veľký časový krok a subkrokovanie je vypnuté, pri kontakte uzly preniknú do podriadených povrchov a na konci kroku sa premiestnia. Toto premiestnenie môže spôsobiť miernu stratu objemu. V priebehu simulácie sa môže stať významnou.

  * Keď sa prvky podriadených objektov roztiahnu okolo rohov hlavných objektov, prvky prerežú roh objektu. Objem, ktorý prechádza cez roh, sa pri opätovnom meraní stratí. Tento jav možno obmedziť použitím malých prvkov okolo rohov.

  
Systém poskytuje niekoľko ovládacích prvkov na minimalizáciu tejto straty objemu počas simulácie (pozri obr. 16.1.1 a obr. 16.1.2). Cieľový objem by mal byť nastavený na počiatočný objem súčiastky. Túto hodnotu možno získať z ikony objemu v okne Meshing/Remeshing (sieťovanie/remeshing).

  
V prípade poréznych materiálov sa očakáva, že objem sa bude počas simulácie meniť. Ak je aktivovaná kompenzácia objemu, aktuálny objem súčiastky sa zachová počas remeshovania.

Pri určitých geometriách s veľkými voľnými povrchmi môže kompenzácia objemu spôsobiť skreslenie.

Ak je toto skreslenie neprijateľné, najlepšou alternatívou je použitie jemnej siete a nastavenie podstupňovania dĺžky polygónov na malú hodnotu. Časté nútené remeshing môže byť užitočné, ak je problémom rozťahovanie prvkov okolo rohov.

## Objemová penalizačná konštanta (PENVOL) [2D, 3D]

Konštanta objemovej pokuty ([PENVOL](/docs/sk/Keyword_Documentation/P/PENVOL/)) udáva veľkú kladnú hodnotu, ktorá sa používa na vynútenie objemovej stálosti plastických objektov. Predvolená hodnota 106 je pre väčšinu simulácií dostatočná. Ak je hodnota príliš malá, môže dôjsť k neprijateľne veľkým objemovým stratám. Ak je hodnota príliš veľká, riešenie môže mať problémy s konvergenciou.

## Priemerná miera deformácie (AVGSTR) [2D, 3D]

Priemerná miera deformácie ([AVGSTR](/docs/sk/Keyword_Documentation/A/AVGSTR/)) je charakteristická priemerná hodnota efektívnej miery deformácie. Približná hodnota tejto hodnoty by sa mala uviesť na začiatku simulácie. Primeranú aproximáciu možno získať z:

![](../../../assets/Equations/Pre_Processor/16_Object_Properties/EQ_16_1_1.jpg) |
---|---
  
## Medzná miera deformácie (LMTSTR) [2D, 3D]

Medzná miera deformácie ([LMTSTR](/docs/sk/Keyword_Documentation/L/LMTSTR/)) definuje hraničnú hodnotu efektívnej miery deformácie, pod ktorou sa plastický alebo porézny materiál považuje za tuhý a správa sa ako newtonovská kvapalina. Vzťah medzi napätím a rýchlosťou deformácie v tuhej oblasti je aproximovaný vzťahom,

![](../../../assets/Equations/Pre_Processor/16_Object_Properties/EQ_16_1_2.jpg) |
---|---
  
DEFORM automaticky udržiava pomer medzi priemernou rýchlosťou deformácie a medznou rýchlosťou deformácie. Vo všeobecnosti by hodnota medznej rýchlosti deformácie mala byť 0,1 % až 1,0 % priemernej rýchlosti deformácie.

Ak je hraničná rýchlosť deformácie príliš malá, riešenie môže mať problémy s konvergenciou. Ak je príliš veľká, presnosť riešenia sa zhorší. Ak problém nekonverguje, hraničnú mieru deformácie možno zvýšiť na 2 alebo 3 kroky a potom ju vrátiť na pôvodnú hodnotu.

## Zovšeobecnená kontrola rovinnej deformácie (ZSTR) [2D]

Zovšeobecnené riadenie rovinnej deformácie ([ZSTR](/docs/sk/Keyword_Documentation/Z/ZSTR/)) umožňuje určitému objektu deformáciu v smere hrúbky pre rovinný deformačný prvok. Deformáciu v smere hrúbky možno riadiť buď predpísanou rýchlosťou, alebo ťahom v smere hrúbky. Táto možnosť je k dispozícii pre elasto-plastický materiál s riadením rýchlosti aj trakcie a pre tuhý plastický materiál len s riadením rýchlosti.

Objekt leží medzi dvoma ohraničujúcimi rovinami, ktoré sa môžu navzájom pohybovať ako tuhé telesá, čo spôsobuje deformáciu v smere hrúbky objektu. Nech P0(X0, Y0) je pevný bod vo vzťažných rovinách. Dĺžka medzi P0 a jeho obrazom v druhej rovine P1 je t0 + DuZ , kde t0 je počiatočná hrúbka a DuZ je zmena dĺžky v hrúbke.

![](../../../assets/Equations/Pre_Processor/16_Object_Properties/EQ_16_1_3.jpg) |
---|---
  
V tejto definícii sa rovina môže pohybovať len rovnobežne s referenčnou rovinou, preto budú mať všetky body v objekte rovnakú hrúbku deformácie.

**Z Rate [2D]** :

Tento postup sa zvyčajne uplatňuje pri problémoch s rovinným kmeňom a plechom. Rýchlosť deformácie z je rýchlosť toku materiálu mimo roviny.

Je definovaná ako pomer celkovej deformácie (prirodzený logaritmus zmenšenia prierezu) k času procesu. To určuje konštantnú rýchlosť deformácie v smeroch z.

## Aktualizácia ovládacích prvkov [3D]

**Súvisiace témy:**

[16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[16.2. Thermal properties](/docs/sk/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/sk/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/sk/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.5. Hardness Properties](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.6. Heating Properties](/docs/sk/pre_processor/16_object_properties/16_6_heating_properties/)

[16.7. Symmetry Properties](/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/sk/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/sk/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/sk/pre_processor/16_object_properties/16_10_user/)

[Selecting the Creep strain from simulation output controls](../9_Simulation_Controls/9_7_Advanced_Options.htm#9.7.4._Output_Control)

[Material Creep models](/docs/sk/pre_processor/10_Material_Data/10_1_Plastic_Data/10_1_2_Creep/10_1_2_Creep_Models/)

[Object type selection from object data definition window](../11_General_Object_Data_Definition/11_General_Object_Data_Definition.htm#11.4._Object_type)

[Remeshing-2D Settings](../13_Mesh_Generation/13_1_2D_Mesh_Generation.htm#13.1.8._Remeshing_criteria)
[Remeshing-3D Settings](../13_Mesh_Generation/13_2_3D_Tet_Mesh_Generation.htm#13.2.8._Remeshing_criteria)
