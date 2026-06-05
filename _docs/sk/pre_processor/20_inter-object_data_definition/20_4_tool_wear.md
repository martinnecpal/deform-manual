---
lang: sk
title: "20.4. Opotrebenie nástrojov"
---

# 20.4. Opotrebenie nástrojov

20.4.1. Archardov model

20.4.2. Usuiho model

**[2D, 3D]** : Opotrebenie nástrojov, ktoré prichádzajú do styku s inými objektmi, je možné vypočítať pomocou modelov opotrebenia v záložke „Opotrebenie nástrojov“. Na predpovedanie opotrebenia sú k dispozícii dva preddefinované modely: Archardov model a Usuiho model. Okrem modelov Archarda a Usuiho je k dispozícii aj funkcia užívateľskej rutiny, v ktorej môže užívateľ vyhodnotiť akýkoľvek iný model pomocou základných údajov modelu, ako sú rýchlosť kĺzania, tlak na rozhraní a teplota na rozhraní. (Pozri obr. 20.4.1.).

Pre každý pár objektov, ktoré sa počas procesu dotýkajú, je možné definovať modely opotrebenia; tieto sa nastavujú v časti „Inter-Object Data“. Miera opotrebenia sa vypočítava pre hlavný objekt vo vzťahu, pričom tento objekt musí mať sieť (preto musia byť v časti „Simulation Controls“ aktivované výpočty prenosu tepla).****

Koeficienty používané v týchto modeloch by mali zvyčajne pochádzať zo série kalibračných experimentov. Ak nie sú k dispozícii kalibrované údaje, na stanovenie relatívnych rýchlostí opotrebenia pri podobných procesoch možno použiť štandardné hodnoty. Správna technika modelovania povlakov a povrchových úprav (napríklad nitridácie) je stále predmetom veľmi aktívneho výskumu. Preto je porovnanie účinkov rôznych povrchových úprav bez dodatočných údajov náročné. Kontaktujte podporu DEFORM na adrese [support@deform.com](mailto:support@deform.com), ak potrebujete pomoc pri hľadaní najnovších výskumov v tejto oblasti. Napriek tomu je možné ponúknuť nasledujúce usmernenia:

Na použitie opotrebenia nástroja musia byť splnené nasledujúce podmienky:

  * Musia byť zapnuté tepelné výpočty.

  * Nástroj by mal byť pokrytý sieťou.

  * Nástroj by mal mať hodnotu tvrdosti definovanú v položke Elements Data![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }})![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Hardness.

  * V dialógovom okne pre vzťahy medzi objektmi je potrebné zapnúť model opotrebenia nástroja a pre koeficienty tohto modelu nastaviť hodnoty odlišné od nuly.

_**Poznámka:**_

_Od verzie DEFORM v11.0 je potrebné údaje o tvrdosti materiálu zadávať na úrovni materiálu._

_To znamená, že tvrdosť možno definovať ako konštantu alebo ako funkciu teploty._

V postprocesore môže používateľ vypočítať celkovú (integrálnu) hĺbku opotrebenia až po stanovený krok procesu, ako aj prírastkovú hĺbku opotrebenia za časový interval posledného kroku. Okrem toho môže používateľ v postprocesore získať údaje o rýchlostiach kĺzania, kontaktnom tlaku a teplotách na rozhraní na kontaktnej ploche matrice.

To znamená, že pre daný model, pre ktorý boli vypočítané údaje o deformácii, môže používateľ vyhodnotiť rôzne modely opotrebenia nástroja bez toho, aby musel simuláciu spúšťať nanovo. Všetky premenné opotrebenia nástroja sú uložené tak pre hlavný objekt, ako aj pre podriadené objekty so sieťou.

**Aktualizácia geometrie opotrebovania:** Používateľ môže zaškrtnúť toto políčko, aby sa geometria a sieťová štruktúra sieťovaných foriem aktualizovali na základe výpočtu opotrebovania nástroja. Geometria sa vyhladí a aktualizuje s vyhladzovacím faktorom 5.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_4_tool_wear/image001.jpg' | relative_url }})

Okno opotrebenia nástrojov medzi objektmi

## Archardov model 

Archard navrhol základné modely opotrebenia založené na adhéznom opotrebení medzi trenými pármi. Tento model sa vo všeobecnosti lepšie hodí pre diskrétne procesy, ako je studené alebo tepelné kovanie. V týchto prípadoch prevláda abrazívne opotrebenie.

![]({{ '/assets/equations/pre_processor/20_inter-object_data_definition/eq_20_4_1.jpg' | relative_url }}) |   
---|---  
  
V Archardovej rovnici opotrebenia sú exponenty a, b a c bezrozmerné. Ak sa predpokladá, že ich hodnota je 1 a že K je bezrozmerné, potom musí byť tvrdosť [H] vyjadrená v jednotkách MPa alebo KSI (v závislosti od jednotkového systému).

Hodnoty tvrdosti podľa Brinella a Vickersa možno previesť na jednotky MPa vynásobením týchto hodnôt hodnotou metrickej štandardnej gravitačnej konštanty (9,80665 m/s²). Ak potrebujete jednotky KSI, vykonajte dodatočný prevod z MPa na KSI.

V programe DEFORM je možné použiť ľubovoľnú jednotku tvrdosti, ak sa používa v spojení s koeficientmi, ktoré boli kalibrované pre danú jednotku tvrdosti. Ak boli napríklad koeficienty stanovené na základe experimentálnych údajov v jednotkách HRC, v simulácii programu DEFORM, ktorá tieto koeficienty využíva, sa musí použiť jednotka tvrdosti HRC.

Medzi jednotkou tvrdosti a jednotkou koeficientu K existuje špecifický vzájomný vzťah. Jednotky koeficientu K závisia od jednotiek tvrdosti, ktoré sa použili pri kalibrácii koeficientu. Jednotky tvrdosti a koeficientu K musia vyjadrovať konečnú rýchlosť opotrebenia vo vzťahu dĺžka/čas.

V prípade **Archardovho** **modelu** poskytnú nasledujúce koeficienty primerané výsledky pre bežné nástrojové ocele:

**a = 1**

**b = 1**

**c = 2**

**K = 1e-02 ~ 1e-03**

Ak sa použije hodnota K = 1e-02 ~ 1e-03, hodnoty tvrdosti by sa mali zadávať podľa Rockwellovej stupnice tvrdosti typu C. 

Je potrebné poznamenať, že tieto hodnoty slúžia výlučne na kvalitatívne porovnanie podobných procesov a neposkytujú kvantitatívne odhady skutočnej životnosti nástroja.

## Usuiho model

Tento model sa vo všeobecnosti lepšie hodí pre kontinuálne procesy, ako je rezanie kovov, kde difúzia významne prispieva k opotrebeniu.

![]({{ '/assets/equations/pre_processor/20_inter-object_data_definition/eq_20_4_2.jpg' | relative_url }}) |   
---|---  
  
  
Pre **Usuiho model** sú typické hodnoty pre obrábacie procesy nasledovné:

**A = 1,0E-5** (alebo rýchlosť kĺzania na rozhraní * tlak na rozhraní) – 1

**B = 1000** (rádu veľkosti absolútnej teploty na rozhraní)

Je potrebné poznamenať, že tieto hodnoty slúžia iba na kvalitatívne porovnanie podobných procesov a neposkytujú kvantitatívne odhady skutočnej životnosti nástroja.

**Súvisiace témy:**

[20\. Inter-Object Data Definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/)

[20.1. Friction and Contact criteria](/docs/sk/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/)

[20.2. Interface Thermal Data](/docs/sk/pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data/)

[20.3. Interface Resisitivity](/docs/sk/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/)

[20.5. Rigid Contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/)
