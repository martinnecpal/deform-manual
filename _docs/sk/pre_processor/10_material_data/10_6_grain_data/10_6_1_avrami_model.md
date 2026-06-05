---
lang: sk
title: "10.6.1 Avramiho model"
---

# 10.6.1. Avramiho model

  * Dynamická rekryštalizácia

  * Statická rekryštalizácia

  * Meta-dynamická rekryštalizácia

  * Rast obilia

  * NOMENKLATÚRA

Avramiho rovnica opisuje, ako sa pevné látky menia z jednej fázy (stavu hmoty) na druhú pri konštantnej teplote. Môže konkrétne opísať kinetiku kryštalizácie. (Pozri obr. 10.6.1.1.)

![]({{ '/assets/images/pre-processor/10_material_data/10_6_grain_data/10_6_image002.jpg' | relative_url }})

Okno modelu Avrami Grain Material

**Definície:**
**Dynamická rekryštalizácia:** prebiehajúca počas deformácie a pri prekročení kritickej deformácie. Hnacou silou je odstránenie dislokácií.  
  
**Statická rekryštalizácia:** nastáva po deformácii a keď je deformácia menšia ako kritická deformácia. Hnacou silou je odstránenie dislokácií. Rekryštalizácia začína v prostredí bez jadier.  
  
**Meta-dynamická rekryštalizácia:** nastáva po deformácii a pri deformácii väčšej ako kritická deformácia. Hnacou silou je odstránenie dislokácií. Keďže deformácia prekročila kritickú deformáciu, v materiáli sa vytvorili rekryštalizačné jadrá, takže správanie pri rekryštalizácii je odlišné od správania bez jadier (statická rekryštalizácia).

  
**Rast zrna:** vyskytujúci sa pred začiatkom rekryštalizácie alebo po ukončení rekryštalizácie. Hnacou silou je zníženie energie na hranici zŕn.

**Koeficient zachovania ťahu** : Koeficient zachovania deformácie sa používa len vtedy, keď:

  1. Aktuálny krok má deformáciu.

  2. V predchádzajúcom kroku nedochádza k deformácii, t. j. na začiatku kroku, keď sa operácia mení z prenosu tepla na deformáciu.

Rovnica je nasledovná:

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_17.jpg' | relative_url }}) |
---|---
  
**Dynamická rekryštalizácia**

Dynamická rekryštalizácia je funkciou deformácie, rýchlosti deformácie, teploty a počiatočnej veľkosti zŕn, ktoré sa menia v čase. Je veľmi ťažké modelovať dynamickú rekryštalizáciu súčasne počas tvárnenia. Namiesto toho sa dynamická rekryštalizácia vypočíta v kroku bezprostredne po ukončení deformácie. Ako vstupy do rovníc sa používajú priemerné teploty a rýchlosť deformácie počas obdobia deformácie.

  1. **Aktivizačné kritériá**

K nástupu DRX zvyčajne dochádza pri kritickej deformácii ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_c.jpg' | relative_url }}) .

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_1.jpg' | relative_url }}) |
---|---
  
  
Kde ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_p.jpg' | relative_url }}) označuje vrcholovú deformáciu zodpovedajúcu maximu napätia pri prúdení:

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_2.jpg' | relative_url }}) |
---|---
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.

  1. **Kinetika**

Na opis vzťahu medzi dynamicky rekryštalizovanou frakciou ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/x.jpg' | relative_url }}) a efektívnou deformáciou sa používa Avramiho rovnica.

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_3.jpg' | relative_url }}) |
---|---
  
  
Kde ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_0_5.jpg' | relative_url }}) označuje deformáciu pre 50 % rekryštalizáciu:

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_4.jpg' | relative_url }}) |
---|---
  
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.

  1. **Veľkosť zrna**

Veľkosť rekryštalizovaného zrna je vyjadrená ako funkcia počiatočnej veľkosti zrna, deformácie, rýchlosti deformácie a teploty,

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_5.jpg' | relative_url }}) |
---|---
  
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.

**Statická rekryštalizácia**

Keď sa deformácia zastaví, rýchlosť deformácie a kritická deformácia sa použijú na určenie, či sa má aktivovať statická alebo metadynamická rekryštalizácia. Statická a metadynamická rekryštalizácia sa ukončí, keď sa tento prvok začne opäť deformovať.

  1. **Aktivizačné kritériá**

Ak je rýchlosť deformácie menšia ako![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_dot_ss.jpg' | relative_url }}), po deformácii nastáva statická rekryštalizácia.

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_6.jpg' | relative_url }}) |
---|---
  
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.

  1. **Kinetika**

Model rekryštalizačnej kinetiky je založený na modifikovanej Avramiho rovnici.

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_7.jpg' | relative_url }}) |
---|---
  
Kde ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/t_0_5.jpg' | relative_url }}) je empirická kinetika založená na modifikovanej Avramiho rovnici.

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_8.jpg' | relative_url }}) |
---|---
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.

  1. **Veľkosť zrna**

Veľkosť rekryštalizovaného zrna je vyjadrená ako funkcia počiatočnej veľkosti zrna, deformácie, rýchlosti deformácie a teploty,

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_9.jpg' | relative_url }}) |
---|---
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.

**Meta-dynamická rekryštalizácia**

Meta-dynamická rekryštalizácia je podobná statickej rekryštalizácii, ale s odlišnými aktivačnými kritériami a materiálovými konštantami.

  1. **Aktivizačné kritériá**

Ak je rýchlosť deformácie väčšia ako ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_dot_ss.jpg' | relative_url }}) (pozri EQ(10.6.1.3.)), po deformácii dochádza k metadynamickej rekryštalizácii.

  1. **Kinetika**

Model rekryštalizačnej kinetiky je založený na modifikovanej Avramiho rovnici.

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_10.jpg' | relative_url }}) |
---|---
  
  
Kde ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/t_0_5.jpg' | relative_url }}) je empirická časová konštanta pre 50% rekryštalizáciu:

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_11.jpg' | relative_url }}) |
---|---
  
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.

  1. **Veľkosť zrna**

Veľkosť rekryštalizovaného zrna je vyjadrená ako funkcia počiatočnej veľkosti zrna, deformácie, rýchlosti deformácie a teploty,

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_12.jpg' | relative_url }}) |
---|---
  
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.

**Rast zrna**

Rast zŕn prebieha pred začiatkom rekryštalizácie alebo po jej skončení.  
Kinetika je opísaná rovnicou:

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_13.jpg' | relative_url }}) |
---|---
  
  
Vysvetlenie ďalších pojmov nájdete v nižšie uvedenej nomenklatúre.  
  
**Zachovaný kmeň a veľkosť zrna**
Pri viacnásobných deformačných procesoch sa môže deformácia počas obdobia medzi priechodmi znížiť v dôsledku obnovy.  
  
Na výpočet zachovanej deformácie na začiatku následnej deformácie sa používa nasledujúca rovnica.

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_14.jpg' | relative_url }}) |
---|---
  
  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.  
  
**Temperatúrny limit**
Teplotný limit je dolnou hranicou všetkých mechanizmov vývoja zrna. Pod touto teplotou nedochádza k žiadnemu vývoju zrna.  
  
**Priemerná veľkosť zrna**
Na výpočet veľkosti rekryštalizovaného zrna pri neukončenej rekryštalizácii sa použil zákon zmesi,

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_15.jpg' | relative_url }}) |
---|---
  
  
Okrem toho, ak je na začiatku deformácie celková hodnota ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/xrex.jpg' | relative_url }}) 1,0, program sa znovu inicializuje (napr. ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/xrex.jpg' | relative_url }}) = 0), aby sa vypočítalo nové kolo rekryštalizácie.  
Vysvetlenie pojmov nájdete v nižšie uvedenej nomenklatúre.  
  
**Závislosť modelu od teploty a rýchlosti deformácie**
DEFORM umožňuje rôzne konštanty a koeficienty pre rovnice pri rôznych teplotách alebo rýchlostiach deformácie. Údaje sú lineárne interpolované.  
**
****NOMENCLATURE**

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_16.jpg' | relative_url }})
