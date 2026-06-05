---
lang: sk
title: "10.3. Tepelné údaje"
---

# 10.3. Tepelné údaje

10.3.1. Tepelná vodivosť
10.3.2. Tepelná kapacita
10.3.3. Emisivita
10.3.4. Hmotnostná hustota

Tepelné údaje sú potrebné pre každý objekt v režime prenosu tepla, ako je znázornené na obr. 10.3.1.

![]({{ '/assets/images/pre-processor/10_material_data/10_3_thermal_data/10_3_image001.jpg' | relative_url }})

Okno s údajmi o tepelnom materiáli

## Tepelná vodivosť (THRCND)

Vedenie je proces, pri ktorom teplo prúdi z oblasti s vyššou teplotou do oblasti s nižšou teplotou v prostredí. Tepelná vodivosť ([THRCND](/docs/sk/keyword_documentation/t/thrcnd/)) je v tomto prípade schopnosť daného materiálu viesť teplo v rámci objektu.  
Hodnota môže byť konštantná alebo funkcia teploty, funkcia obsahu atómov alebo funkcia teploty a obsahu atómov.

## Tepelná kapacita (HEATCP)

Tepelná kapacita je vo všeobecnosti definovaná ako množstvo tepla, ktoré musí objekt absorbovať, aby došlo k jednotkovej zmene jeho teploty.Zvyčajne sa dokumentuje presnejšie ako tepelná kapacita vydelená množstvom materiálu. Množstvo materiálu je zvyčajne hmotnosť alebo objem.

Väčšina referenčných hodnôt tepelnej kapacity uvádza špecifickú tepelnú kapacitu ![]({{ '/assets/equations/pre_processor/10_material_data/10_3_thermal_data/rcp.jpg' | relative_url }}), čo je tepelná kapacita na jednotku hmotnosti. Definuje teplo potrebné na zvýšenie jednotkovej hmotnosti látky o jednotkový teplotný interval pri konštantnom tlaku. Inými slovami, je to tepelná energia na jednotku hmotnosti potrebná na dosiahnutie zvýšenia teploty o jeden stupeň.

Predvolený termín tepelnej kapacity ([HEATCP](/docs/sk/keyword_documentation/h/heatcp/)) používaný v programe DEFORM je objemová tepelná kapacita, ρcp, čo je tepelná kapacita na jednotku objemu. Definuje teplo potrebné na zvýšenie jednotkového objemu látky o jednotkový teplotný interval pri konštantnom tlaku. Inými slovami, je to tepelná energia na jednotku objemu potrebná na dosiahnutie zvýšenia teploty o jeden stupeň.

Objemová tepelná kapacita sa získa vynásobením mernej tepelnej kapacity (tepelná kapacita na jednotku hmotnosti) hustotou (hmotnosť na jednotku objemu).

![]({{ '/assets/equations/pre_processor/10_material_data/10_3_thermal_data/eqn_10_3_1.jpg' | relative_url }}) |
---|---
  
Ďalším výrazom tepelnej kapacity ([HEATCP](/docs/sk/keyword_documentation/h/heatcp/)), ktorý je k dispozícii v programe DEFORM, je hmotnostná merná tepelná kapacita. Je to špecifická tepelná kapacita, ale označená ako "hmotnostné špecifické teplo", aby sa zdôraznil jej vzťah k vstupným údajom o hmotnostnej hustote, ktoré sú k dispozícii v ponuke tepelných vlastností. Hmotnostná hustota sa musí definovať, ak bola definovaná hmotnostná merná tepelná kapacita. Hodnoty pre hmotnostnú hustotu a hmotnostnú špecifickú tepelnú kapacitu musia používať konzistentné jednotky hmotnosti. Ďalšie podrobnosti nájdete v časti [1.9. Units](/docs/sk/about_deform/1_introduction_to_deform/1_9_units/).

DEFORM využíva objemovú tepelnú kapacitu na výpočty MKP. Ak bola definovaná hmotnostná merná tepelná kapacita, DEFORM vypočíta objemovú tepelnú kapacitu z hmotnostnej hustoty a hmotnostnej mernej tepelnej kapacity počas výpočtov MKP.

Objemová alebo hmotnostná merná tepelná kapacita môže byť do programu DEFORM zadaná ako konštanta, funkcia teploty, funkcia obsahu atómov alebo funkcia teploty a obsahu atómov.

## Emisivita (EMSVTY)

Emisný výkon telesa je celkové množstvo žiarenia vyžiarené telesom za jednotku plochy a času. Emisivita ([EMSVTY](/docs/sk/keyword_documentation/e/emsvty/)) telesa je pomer E/Eb, kde Eb je emisný výkon dokonalého čierneho telesa. Úplnejší opis vlastností emisivity nájdete v akomkoľvek zdroji zaoberajúcom sa prenosom tepla. Hodnota môže byť konštantná alebo funkcia teploty.

## Hmotnostná hustota (DENSTY)

Hmotnostná hustota ([DENSTY](/docs/sk/keyword_documentation/d/densty/)) materiálu je jeho hmotnosť na jednotku objemu. Hmotnostná hustota môže byť definovaná ako konštanta alebo ako funkcia teploty. Hmotnostná hustota sa musí definovať v modeloch, ktoré zahŕňajú gravitáciu, silu telesa, odstredivú silu alebo explicitný riešiteľ.

Hodnoty hustoty pre rôzne materiály sú ľahko dostupné v online a tlačenej literatúre. Je potrebné poznamenať, že typ hustoty uvedený v týchto referenciách sa vo všeobecnosti líši na základe špecifikovanej jednotkovej sústavy, ako je opísané nižšie.

  * Hodnoty hustoty uverejnené v sústave jednotiek SI zvyčajne predstavujú hmotnostnú hustotu materiálu v jednotkách kg/m3 alebo ekvivalentných jednotkách.

  * Hodnoty hustoty uverejnené v anglickom systéme jednotiek zvyčajne predstavujú hmotnostnú hustotu materiálu v jednotkách lbf/in3 alebo ekvivalentných jednotkách.

Pri práci v anglických jednotkách sa musí hmotnostná hustota pred použitím v programe DEFORM prepočítať na hmotnostnú hustotu. Na získanie hmotnostnej hustoty si najprv pripomeňte nasledujúci základný fyzikálny vzťah:

sila = hmotnosť * zrýchlenie

Rovnicu možno zmeniť tak, aby zohľadňovala vzťah medzi hmotnosťou (silou), hmotnosťou a gravitáciou (zrýchlením):

hmotnosť = hmotnosť * gravitácia

Nasledujúci vzťah sa získa tak, že sa predpokladá štandardná gravitácia, každá strana rovnice sa vydelí objemom (aby sa získali hustoty) a rovnica sa usporiada:

hmotnostná hustota = hustota hmotnosti / štandardná hmotnosť

Štandardná gravitácia sa rovná 32,17 ft/s2 (386,1 in/s2) v anglickej jednotkovej sústave.

Uvažujte o nasledujúcom príklade, kde je potrebné definovať hmotnostnú hustotu ocele buď v anglických jednotkách, alebo v jednotkách SI. Uverejnené hodnoty hustoty pre všeobecnú oceľ sú:

Anglické jednotky: 0,282 lbf/in3 (hustota hmotnosti)

Jednotky SI: 7800 kg/m3 (hmotnostná hustota)

Ak pracujete v anglických jednotkách, hustota hmotnosti sa najprv prepočíta na hustotu hmotnosti, ako je uvedené nižšie:

hmotnostná hustota = (0,282 lbf/in3) / (386,1 in/s2) = 0,730x10-3 lbf*s2/in4

Hmotnostná hustota sa potom musí upraviť na správny formát jednotky tak, že sa výraz lbf prevedie na klbf:

0,730x10-3 lbf*s2/in4 * (1 klbf / 1000 lbf) = 0,730x10-6 klbf*s2/in4

Hodnota hustoty hmotnosti, ktorá by mala byť definovaná v modeli DEFORM v anglickej jednotke, je teda 0,730x10-6 klbf*s2/in4.

Ak pracujete v jednotkách SI, potom je hustota hmotnosti už známa. Predtým, ako sa použije ako vstup pre DEFORM, sa však musí previesť do správneho formátu jednotiek. To si vyžaduje nasledujúci prevod:

1000 kg = 1 tona

7800 kg/m3 * (1 tona / 1000 kg) * (1 m / 1000 mm)3 = 7,80x10-9 tona/mm3

Hodnota hmotnostnej hustoty, ktorá by mala byť definovaná v modeli DEFORM v jednotkách SI, je teda 7,80x10-9 tona/mm3.
