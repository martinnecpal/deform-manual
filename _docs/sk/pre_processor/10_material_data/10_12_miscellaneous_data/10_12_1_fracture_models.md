---
lang: sk
title: "10.12.1. Modely zlomov"
---

# 10.12.1. Modely zlomov

  * Normalizovaný model poškodenia C&L

  * Model poškodenia Cockcroft & Latham

  * McClintockov model poškodenia

  * Freudenthalov model poškodenia

  * Model poškodenia Rice & Tracy

  * Model poškodenia Oyane

  * Model poškodenia Oyane (negatívny)

  * Model poškodenia Ayada

  * Model poškodenia Osakada

  * Model poškodenia Brozzo

  * Model poškodenia Zhoa & Kuhn

  * [Maximum principal stress / ultimate tensile strength damage model](10_12_1_fracture_models.htm#Maximum_principal_stress_/_ultimate_tensile_strength)

  * Model poškodenia pri uzavretí prázdneho priestoru

  * Model poškodenia FLD

  * Používateľský model poškodenia

V programe DEFORM sú k dispozícii tieto modely zlomov (pozri obr. 10.12.1.1):

  * Normalizované C&L
  * Cockcroft & Latham
  * McClintock
  * Freudenthal
  * Rice & Tracy
  * Oyane
  * Oyane (negatívny)
  * Ayada
  * Osakada
  * Brozzo
  * Zhoa &Kuhn
  * Maximálne hlavné napätie / medza pevnosti v ťahu
  * Uzavretie prázdneho priestoru
  * FLD
  * Používateľská rutina

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image001.jpg' | relative_url }})

Modely zlomov v programe DEFORM

  * **Normalizovaný model poškodenia C & L**

Tento model je definovaný ako funkcia maximálneho hlavného napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_dash.jpg' | relative_url }})) normalizovaného efektívnym napätím (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }})).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_1.jpg' | relative_url }}) |
---|---
  
  * **Cockcroft & Latham model poškodenia**

Tento model je definovaný ako funkcia maximálneho hlavného napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_star.jpg' | relative_url }})).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_2.jpg' | relative_url }}) |
---|---
  
  * **McClintockov model poškodenia**

Tento model je definovaný ako funkcia maximálneho a minimálneho hlavného napätia ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_a.jpg' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_b.jpg' | relative_url }}) ) a efektívneho napätia. je koeficient modelu.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_3.jpg' | relative_url }}) |
---|---
  
  * **Freudenthalov model poškodenia**

Tento model je definovaný ako funkcia efektívneho napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }}) ).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_4.jpg' | relative_url }}) |
---|---
  
  * **Model poškodenia Ryža a Tracyho**

Tento model je definovaný ako funkcia stredného napätia ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_m.jpg' | relative_url }}) ) a efektívneho napätia ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }}) ). ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/alpha.jpg' | relative_url }}) je koeficient modelu.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_5.jpg' | relative_url }}) |
---|---
  
  * **Oyane model poškodenia**

Tento model je definovaný ako funkcia stredného napätia ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_m.jpg' | relative_url }}) ) a efektívneho napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }}) ). ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/a_not.jpg' | relative_url }}) je modelová konštanta.

Materiálová konštanta ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/a_not.jpg' | relative_url }}) sa v mnohých publikovaných prácach predpokladá na úrovni 0,424, ako ju určili Hambli a Reszka.

_Hambli, R.; Reszka, M. Identifikácia lomových kritérií pomocou metódy inverznej techniky a slepého experimentu. Int. J. Mech. Sci., 2002, 44, 1349-1361. https://doi.org/10.1016/S0020-7403(02)00049-8._

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_6.jpg' | relative_url }}) |
---|---
  
  * **Oyane (negatívny) model poškodenia**

Zohľadňuje záporné členy v integrále, aby sa hodnoty poškodenia mohli znižovať alebo zvyšovať v závislosti od stavu napätia. Zahrnutie záporného integračného člena do uvedenej rovnice EQ(10.12.1.6).

  * **Ajada model poškodenia**

Tento model je definovaný ako funkcia stredného napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_m.jpg' | relative_url }})) a efektívneho napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }})).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_7.jpg' | relative_url }}) |
---|---
  
  * **Ajada (negatívny) model poškodenia**

Zohľadňuje záporné členy v integrále, aby sa hodnoty poškodenia mohli znižovať alebo zvyšovať v závislosti od stavu napätia. Zahrnutie záporného integračného člena do uvedenej rovnice EQ(10.12.1.7).

  * **Osakada model poškodenia**

Tento model je definovaný ako funkcia stredného napätia a efektívnej deformácie ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/small_a.jpg' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/small_b.jpg' | relative_url }}) sú koeficienty modelu.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_8.jpg' | relative_url }}) |
---|---
  
  * **Brozzo model poškodenia**

Tento model je definovaný ako funkcia hlavného napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_star.jpg' | relative_url }}) ) a stredného napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_m.jpg' | relative_url }})).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_9.jpg' | relative_url }}) |
---|---
  
  * **Zhoa & Kuhn model poškodenia**

Tento model je definovaný ako funkcia hlavného napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_star.jpg' | relative_url }})) a efektívneho napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }})), ale závisí len od stavu napätia.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_10.jpg' | relative_url }}) |
---|---
  
  * **Poškodenie na základe maximálneho hlavného napätia / medze pevnosti v ťahu**

Tento model je definovaný ako funkcia maximálneho hlavného napätia a medze pevnosti v ťahu (UTS) a závisí len od stavu napätia. UTS môže byť aj funkciou teploty.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_11.jpg' | relative_url }}) |
---|---
  
  * **Voidný uzáver**

Model uzavretia prázdneho priestoru odhaduje "faktor hojenia", čo je pomer prázdneho priestoru definovaný vydelením aktuálneho objemu prázdneho priestoru počiatočným objemom prázdneho priestoru. Percento zmäkčenia napätia pri prúdení sa stáva 100 %, keďže ide o model hojenia, a nie o model lomu. Index hodnotenia uzavretia vnútornej dutiny (Q) sa počíta v simulácii MKP pomocou nasledujúcej definície. (kde 0,0 < Q < 1,0)

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_12.jpg' | relative_url }}) |
---|---
  
  
Používateľ musí zadať pomer objemu prázdneho priestoru ako funkciu indexu uzavretia prázdneho priestoru (Q), ako je znázornené na obr. 10.12.1.2.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image004.jpg' | relative_url }})

Okno funkcie prázdneho uzáveru

  * **FLD model poškodenia**

Model hraničného diagramu tvárnenia (FLD) sa zavádza ako indikátor poruchy pri simuláciách tvárnenia plechov. Vo FLD možno zohľadniť zmäkčenie toku. Tento model je k dispozícii len v prostredí MO. Faktor poškodenia je definovaný ako pomer veľkej deformácie (= aktuálna veľká deformácia / limitná veľká deformácia) pre daný stav veľkej a malej deformácie. (Pozri obr. 10.12.1.3.)

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_13.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image003.jpg' | relative_url }})

Faktor poškodenia Hlavný graf pomeru deformácií

  
Používatelia by mali poskytnúť diagram medze tvárnenia (t. j. diagram menšej deformácie v závislosti od väčšej deformácie). Používateľ môže upravovať údaje o funkcii FLD, ako je znázornené na obr. 10.12.1.4.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image005.jpg' | relative_url }})

Tvorba okna obmedzujúceho diagramu

  
Výberom tlačidla Definovať môže používateľ definovať FLD (Major strain, Minor strain), ako je znázornené na obr. 10.12.1.5.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image006.jpg' | relative_url }})

Formovanie okna funkcie obmedzujúceho diagramu

  * **Používateľská rutina poškodenia**

Ak sa zvolí model maximálneho efektívneho napätia/pevnosti v ťahu, musí sa pevnosť v ťahu ([UTSDAT](/docs/sk/keyword_documentation/u/utsdat/)) definovať ako konštanta alebo funkcia teploty. K základným modelom Oyane a Ayada sú k dispozícii aj ďalšie modely, ktoré zohľadňujú záporné členy v integrále, aby sa hodnoty poškodenia mohli znižovať alebo zvyšovať v závislosti od stavu napätia. Premenná stavu DAMAGE sa používa na spustenie modelovania lomu pomocou vymazania prvkov alebo zmäkčenia kontinuálneho poškodenia. Pri vymazávaní prvkov sa zo siete vymažú prvky, ktoré prekročia definovanú kritickú hodnotu poškodenia. Ide o efektívny spôsob modelovania šírenia trhlín. Vymazávanie prvkov sa musí aktivovať pre každý objekt v dialógovom okne Vlastnosti objektu. Pri zmäkčení kontinuálneho poškodenia sa hodnota prietokového napätia použitá na výpočet tuhosti prvku zníži na určené percento (zvyčajne 1 až 5 %) prietokového napätia vypočítaného pre daný prvok. Používateľ môže vytvoriť model poškodenia pomocou dostupných stavových premenných vo fortranovom súbore usr_dmg.f. Číslo užívateľskej procedúry usr_dmg.f musí byť uvedené tak, ako je znázornené na obr. 10.12.1.6., aby sa vybral užívateľsky definovaný model na výpočet poškodenia.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image002.jpg' | relative_url }})

Poškodenie Používateľské okno rutinného modelu
