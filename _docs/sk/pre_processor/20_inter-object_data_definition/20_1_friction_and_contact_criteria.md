---
lang: sk
title: "20.1. Kritériá trenia a kontaktu"
---

# 20.1. Kritériá trenia a kontaktu

20.1.1. Trenie (FRCFAC)

  * Konštantné šmykové napätie (prilepenie)

  * Coulomb (posuvný)

  * Hybridný

  * Tau (šmykové napätie)

20.1.2. Anizotropný

20.1.3. Kritériá pre kontakt

20.1.4. Typ oddelenia

  * Hustota separácie

  * Oddeliteľný

  * Neoddeliteľný

  * Možnosť adaptívneho kontaktu BCC

20.1.5. Kritériá oddelenia

20.1.6. Okno „Trenie“

## Trenie (FRCFAC) [2D, 3D]

Koeficient trenia ([FRCFAC](/docs/sk/keyword_documentation/f/frcfac/)) určuje trenie na rozhraní medzi dvoma objektmi. Koeficient trenia môže byť špecifikovaný ako konštanta, funkcia času, teploty, tlaku, teploty povrchu pri tlaku, závislá od tlaku, rýchlosti deformácie a rýchlosti kĺzania alebo užívateľská rutina (pozri obr. 20.1.1.).

Povolené typy trenia sú šmykové, Coulombovo, hybridné a s konštantným tau. Typ s konštantným tau je k dispozícii iba v 2D.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image001.jpg' | relative_url }})

Možnosti funkcie šmykového trenia medzi objektmi

**Konštantné šmykové napätie (prilepenie)** [2D, 3D]  
Trieštivé trenie s konštantným šmykom sa používa najmä pri simuláciách tvarovania objemových materiálov. Trieštivá sila v definícii konštantného šmyku je daná vzťahom:

![]({{ '/assets/equations/pre_processor/20_inter-object_data_definition/eq_20_1_1.jpg' | relative_url }}) |   
---|---  
  
Z toho vyplýva, že trenie je funkciou medze tečnosti deformovaného telesa.

**Coulomb (kĺzavý)** [2D, 3D]  
Coulombovo trenie sa uplatňuje v prípade kontaktu dvoch elasticky sa deformujúcich telies (môže zahŕňať aj elasticko-plastické teleso, ak sa deformuje elasticky) alebo medzi elastickým a tuhým telesom. Všeobecne sa používa na modelovanie procesov tvárnenia plechov. Trenie v modeli podľa Coulombovho zákona je definované takto:

![]({{ '/assets/equations/pre_processor/20_inter-object_data_definition/eq_20_1_2.jpg' | relative_url }}) |   
---|---  
  
Aby vznikla trecia sila, musí medzi dvoma telami pôsobiť tlak na rozhraní. Ak sa dve telesa dotýkajú, ale nepôsobí na ne žiadna sila, ktorá by ich tlačila k sebe, nedôjde k žiadnemu treniu.

V prípade kontaktu medzi dvoma plastickými alebo poréznymi objektmi sa trecie napätie vypočíta na základe tokového napätia podriadeného objektu.

**Hybridný** [2D, 3D]  
Hybridný model je kombináciou dvoch modelov trenia, ktoré možno uplatniť na dva objekty, ktoré sú v kontakte v dôsledku trenia (pozri obr. 20.1.2.).

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image002.jpg' | relative_url }})

Okno s hybridným trením medzi objektmi

**Tau (šmykové napätie)** [2D]  
Model trenia Tau umožňuje používateľovi nastaviť šmykové napätie medzi dvoma objektmi, ktoré sú v kontakte, spôsobené trením. Používateľ môže nastaviť konštantnú hodnotu.

**Častá otázka**: Aká je vhodná hodnota koeficientu trenia?

**Odpoveď**: Mazivo použité na nástrojoch má veľký vplyv na mieru trenia medzi nástrojmi a obrobkom. Toto trenie zase ovplyvňuje tok kovu na kontaktných plochách.

Typické hodnoty (len pri konštantnom šmyku):

(0,08–0,1) pre procesy tvárnenia za studena

(0,2) pre procesy tepelného tvárnenia

(0,2 až 0,3) pre procesy tvárnenia za tepla s mazáním

(0,7–0,9) pre suché povrchy

Väčšina procesov nie je mimoriadne citlivá na trenie a uvedené typické hodnoty sú úplne postačujúce. V prípade procesov, ktoré sú veľmi citlivé na podmienky mazania, je možné hodnoty trenia určiť experimentálnou cestou.

Poznámka:

  * Trenie s konštantným šmykom (adhézne trenie) sa používa najmä pri simuláciách formovania sypkých materiálov.

  * Pri operáciách tvárnenia plechov sa využíva Coulombovo (kĺzavé) trenie, pretože sa najviac podobá typu trenia, s ktorým sa pri tomto procese stretávame.

  * Trenie typu Tau je možné použiť v prípade, ak používateľ potrebuje určiť šmykové napätie na povrchu.

**Poznámky**: Dva jednoduché spôsoby, ako zistiť citlivosť procesu na trenie:

  1. Očakávali by ste výrazné rozdiely v správaní dielu v závislosti od toho, či je mazivo pri výrobe nanesené správne alebo nesprávne? Ak nie, mali by stačiť typické hodnoty trenia uvedené vyššie.

  2. Ak si stále nie ste istí, spustite dve simulácie v programe DEFORM s, povedzme, 20 % odchýlkou podmienok trenia od typických hodnôt. (V prípade tvárnenia za studena s mazáním môžete spustiť jednu simuláciu s hodnotou 0,08 a druhú s hodnotou 0,12). Porovnajte výsledky, napríklad zaťaženie v porovnaní so zdvihom alebo konečnou geometriou, najmä parametre, ktoré ste identifikovali ako kritické. Ak existuje podstatná odchýlka, je potrebné dôkladnejšie preskúmať trenie. Ak je odchýlka malá, typické hodnoty sú postačujúce.

DEFORM ponúka celý rad definícií na modelovanie presnej interakcie deformovaného obrobku s ostatnými fyzikálnymi komponentmi systému za meniacich sa podmienok spracovania. Patria sem definície hodnôt trenia ako funkcie času, tlaku na rozhraní, teploty na rozhraní a povrchového napätia deformovaného obrobku alebo ich kombinácie. Ďalšie definície zahŕňajú aj explicitné modely, ktoré definujú hodnoty trenia ako funkciu tlaku, rýchlosti deformácie a rýchlosti kĺzania, ako je uvedené na obr. 20.1.3. až obr. 20.1.8.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image003.jpg' | relative_url }})

Koeficient šmykového trenia závislý od tlaku

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image004.jpg' | relative_url }})

Koeficient šmykového trenia závislý od rýchlosti deformácie

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image005.jpg' | relative_url }})

Koeficient šmykového trenia závislý od rýchlosti posuvu

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image006.jpg' | relative_url }})

Koeficient Coulombovho trenia závislý od tlaku

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image007.jpg' | relative_url }})

Koeficient Coulombovho trenia závislý od rýchlosti deformácie

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image008.jpg' | relative_url }})

Koeficient Coulombovho trenia závislý od rýchlosti kĺzania

  
**Upozornenie** :

Pri použití podmienky samokontaktu buďte opatrní. Ak sa to nebude sledovať, môže sa počas simulácie vytvoriť záhyb, ktorý zakryje sám seba. Postprocesor umožní používateľovi tieto záhyby ľahko nájsť.

Rovnice modelov šmykového, Coulombovho a hybridného koeficientu trenia sú uvedené na obr. 20.1.9 nižšie.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image009.jpg' | relative_url }})

Rovnice Coulombovho, šmykového a hybridného modelu trenia

_Modely trenia je možné vybrať na základe nasledujúcich podmienok_ :

  * **Šmyk:**

  * Trenie pri prilepení

  * Väčšina prípadov hromadného formovania

  * Najlepšia konvergencia

  * **Coulomb:**

  * Kĺzavé trenie

  * Obrobky s ľahkou oporou pri hromadnom tvárnení

  * Tvarovanie plechov

  * **Hybridný:**

  * Coulombov zákon pri nízkom tlaku

  * Zákony šmyku pri vysokom tlaku

  * V programe Forming Express nie je k dispozícii

  
Hodnoty koeficientov šmykového a Coulombovho trenia pre niekoľko prípadov použitia sú uvedené v nasledujúcej tabuľke.

**Použitie** | **Koeficient šmykového trenia** | **Koeficient Coulombovho trenia**  
---|---|---  
Tvarovanie plechu | 0,08–0,12 | 0,05–0,10  
Tvarovanie za studena  | 0,08–0,12 | 0,05–0,10  
Tepelné kovanie | 0,2–0,3 |   
Kovanie za tepla s mazáním sklom | 0,1–0,2 |   
Kovanie za tepla s mazáním grafitom/olejom  | 0,3–0,4 |   
Kovanie za tepla bez mazania | 0,7–1,0 |   
Extrúzia bez mazania | 0,7–1,0 |   
Valcovanie | 0,7–1,0 |   
  
## Anizotropný [3D]

Možnosť „Anizotropný“ ([FRCFAI](/docs/sk/keyword_documentation/f/frcfai/)) umožňuje používateľovi definovať rôzne hodnoty koeficientov mierky trenia pre každú os. Ak sú pre jednotlivé osi definované rôzne koeficienty mierky, definovaná hodnota trenia sa prispôsobí podľa príslušného koeficientu mierky a uplatní sa na danú os. (Pozri obr. 20.1.10.)

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image010.jpg' | relative_url }})

Anizotropný model 

**Karta Kontakt:**

V časti DEFORM - V12 boli na karte Deformácia – Kontakt pridané možnosti kritérií oddelenia; boli implementované ďalšie kritériá kontaktu a oddelenia založené na vzdialenosti a geometrii (pozri obr. 20.1.11. (2D) a obr. 20.1.12. (3D)). Možnosti metódy kontaktu boli presunuté na kartu Simulačné ovládacie prvky ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Advanced ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})[Contact](../9_simulation_controls/9_7_advanced_options.htm#9.7.5._Contact_).

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image011.jpg' | relative_url }})

Okno karty „2D kontakt“ 

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image012.jpg' | relative_url }})

Okno karty „3D Kontakt“

## **Kritériá pre kontakt**

V rámci kritérií kontaktu sú k dispozícii nasledujúce možnosti, pomocou ktorých je možné určiť, kedy by mal byť uzol považovaný za kontaktný uzol.

  * **Predvolené nastavenie systému**: Ak použijeme predvolenú metódu systému pre uzlový kontakt, systém sám určí, či ide o kontaktný uzol, alebo nie.

  * **Absolútna vzdialenosť**: Ak sa uzol nachádza v rámci vzdialenosti uvedenej v tomto poli od hlavného objektu, považuje sa za kontaktný uzol.

  * **(%) veľkosti prvku** : Ak sa uzol nachádza vo vzdialenosti, ktorá predstavuje definované percento veľkosti prvku najbližšieho podriadeného objektu od hlavného objektu, považuje sa tento uzol za kontaktný uzol.

  * **Vyhľadávanie kontaktov v okne trenia**: Ak používatelia využijú túto možnosť, systém bude vyhľadávať kontaktné body iba v rámci okna trenia. Na použitie tejto možnosti je potrebné najprv definovať okno trenia, potom túto možnosť vybrať a koeficient trenia by mal byť definovaný na stránke okna trenia, nie na stránke globálneho trenia.

  * **Vybrať všetky uzly povrchu v okne trenia (len pre 3D)**: Táto možnosť je k dispozícii len v 3D a je prepojená s možnosťou „Neaktualizovať“ v rámci aktualizácie súradníc uzlov. Všetkým uzlom povrchu v okne trenia bude priradený kontakt BCC. Uzol sa oddelí, akonáhle opustí okno. Koeficient trenia by mal byť definovaný na stránke okna trenia, nie na stránke globálneho trenia.

V zozname aktualizácií súradníc uzlov máme:

  * **Aktualizácia systému**: Ak pri použití možnosti „Aktualizácia systému“ systém na základe kontaktných kritérií určí určitý uzol za kontaktný uzol, automaticky aktualizuje jeho súradnice, aby sa vytvoril kontakt s hlavným objektom.

  * **Neaktualizovať**: Ak použijeme možnosť „Neaktualizovať“, súradnice uzla sa neaktualizujú, hoci je uzol na základe kontaktných kritérií určený ako kontaktný uzol na vytvorenie kontaktu s hlavným objektom.

## Typ oddelenia

  * **Hustota oddelenia****[2D**]: Hustota oddelenia ([SEPDEN](/docs/sk/keyword_documentation/s/sepden/)) sa používa na modelovanie správania poréznych objektov, ktoré neboli úplne zhutnené. Definuje kritérium oddelenia kontaktných uzlov zahŕňajúcich porézne objekty. Pokiaľ hustota materiálu nie je väčšia ako hustota, oddelenie uzlov sa nezohľadňuje.

  * **Oddeliteľné [3D]:** Kritériá oddelenia ([SEPRES](/docs/sk/keyword_documentation/s/sepres/)) určujú, ako sa budú uzly na rozhraní medzi objektmi správať pri pôsobení ťahovej sily. Existujú tri spôsoby definovania kritérií oddelenia.

  * **Neoddeliteľné [3D]:** Vztah oddelenia ([SEPRES](/docs/sk/keyword_documentation/s/sepres/)) umožňuje definovať kontakt uzlov ako neoddeliteľný za akýchkoľvek podmienok. Táto podmienka by sa vo všeobecnosti mala používať len na pripojenie uzlov k tuhej symetrickej rovine pri definovaní symetrie na rovine inej ako XY, YZ alebo ZX.

  * **Možnosť adaptívneho kontaktu BCC [3D]**: Táto možnosť sa používa pri špeciálnom kontaktnom vzťahu medzi dvoma viacerými deformujúcimi sa maticami. Rozhranie dvoch deformujúcich sa matíc je mechanicky oddeliteľné, avšak zachováva kontakt BCC, takže žiadny uzol sa nesmie dostať do medzery medzi nimi.

## Kritérium oddelenia

V rámci kritérií založených na tlaku máme:

  * **Predvolené nastavenie systému**: Toto nastavenie spôsobí bežné oddelenie, ak na kontaktný uzol pôsobí ťahová sila alebo tlak väčší ako 0,1.

  * **(%) medze tečenia**: Toto nastavenie spôsobí oddelenie uzlov, ak je napätie na kontaktnom uzle väčšie ako zadané percento medze tečenia podriadeného objektu. Toto percento musí používateľ zadať v poli Kritériá oddelenia.

  * **Absolútny tlak:** Toto nastavenie spôsobí oddelenie uzla v prípade, že napätie pôsobiace na uzol je väčšie ako zadaný tlak. Tento tlak je potrebné uviesť v poli označenom ako „kritériá oddelenia“.

Medzi kritériá založené na geometrii patria:

  * **Absolútna vzdialenosť**: Ak je vzdialenosť medzi hlavnou plochou a uzlom väčšia ako vzdialenosť definovaná v absolútnej vzdialenosti, kontakt s týmto uzlom sa zruší.

  * **(%) veľkosti prvku** : Ak je vzdialenosť medzi hlavnou plochou a uzlom väčšia ako % veľkosti najbližšieho podriadeného prvku, kontakt s týmto uzlom sa zruší.

  * **Na základe roviny:** Poloha a smer roviny sú určené bodom a normálovým vektorom. Kontakt nebude povolený na strane roviny, ktorá smeruje v smere normály. Kontakt bude povolený na strane roviny, ktorá smeruje opačne ako smer normály.

## Okno trenia

**[2D, 3D]** : Okná trenia ([FRCWIN](/docs/sk/keyword_documentation/f/frcwin/)) je možné použiť v simulácii, ako je znázornené na obr. 20.1.13 a obr. 20.1.14. Jedným z účelov tejto funkcie je umožniť používateľovi použiť rôzne podmienky trenia v určitých oblastiach objektu, aby sa simulovali rozdiely v podmienkach mazania. Použitie okna sa vykonáva rovnakým spôsobom ako pri akejkoľvek inej funkcii okna. V prípade dvoch prekrývajúcich sa okien má prednosť okno s nižším poradovým číslom.

Okná trenia umožňujú používateľovi nastaviť rôzne hodnoty koeficientu trenia pre rôzne kontaktné oblasti v rámci jednej dvojice objektov. Okno trenia definuje koeficient trenia pre konkrétnu oblasť, ktorá je vyznačená v okne zobrazenia. Koeficient trenia určuje trenie, ktorému podlieha akýkoľvek objekt prichádzajúci do kontaktu s obrobkom.

V okne pre nastavenie trenia je možné využiť všetky definície modelov trenia dostupné v systéme, ako je vysvetlené v časti „Definícia údajov medzi objektmi“. Okno pre nastavenie trenia je možné nakonfigurovať tak, aby sledovalo pohyb iného objektu, alebo mu možno priradiť vlastnú rýchlosť.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image013.jpg' | relative_url }})

Okno definície medziobjektového trenia pre 2D 

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image014.jpg' | relative_url }})

Okno definície trenia medzi objektmi pre 3D

Poznámka:

Ak pre časti objektov, ktoré sú v kontakte, nie je priradené okno trenia, použije sa globálny koeficient trenia priradený v rozhraní medzi objektmi.

**Súvisiace témy:**

[20\. Inter-Object Data Definition]()

[20.2. Interface Thermal Data](/docs/sk/pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data/)

[20.3. Interface Resisitivity](/docs/sk/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/)

[20.4. Tool Wear](/docs/sk/pre_processor/20_inter-object_data_definition/20_4_tool_wear/)

[20.5. Rigid Contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/)
