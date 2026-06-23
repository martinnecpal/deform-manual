---
lang: sk
title: "26.6.3. Premenné stavu"
---

# 26.6.3. Premenné stavu

  * Rôzne typy premenných typu State

  * Možnosti zobrazenia

  * Nastavenia stavových premenných 

  * Nastavenia ovládacích prvkov

  * Škálovanie

  * Farebná hranica

  * Nastavenia priehybu

  * Súradnice

  * Obdĺžnikové a valcové súradnice

  * Definované používateľom

  * Lokálna (os materiálu) 

  * Mapovanie****

  * Pomer prípustných hodnôt

  * Odkaz

  * Nastavenia opotrebenia nástrojov

  * Kmeň – celkom

  * Relatívna rýchlosť

Niektoré z najčastejšie používaných stavových premenných, ako sú celkový posun ![]({{ '/assets/icons/post_icons/mo_disp_sv_icon.jpg' | relative_url }}), celková rýchlosť ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}), efektívna deformácia ![]({{ '/assets/icons/post_icons/mo_strain_sv_icon.jpg' | relative_url }}), efektívna rýchlosť deformácie ![]({{ '/assets/icons/post_icons/mo_strain_rate_sv_icon.jpg' | relative_url }}), efektívne napätie ![]({{ '/assets/icons/post_icons/mo_eff_stress_sv_icon.jpg' | relative_url }}), teplota ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) a poškodenie ![]({{ '/assets/icons/post_icons/mo_damage_sv_icon.jpg' | relative_url }}), slúžia na zobrazenie kontúrového grafu pre objekty zobrazené v grafickom okne. Ikona ![]({{ '/assets/icons/post_icons/mo_clear_sv_icon.jpg' | relative_url }}) (Vymazať stavovú premennú) slúži na vymazanie vybranej stavovej premennej pre objekty.

K ďalším stavovým premenným sa dostanete pomocou ikony ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (Nastavenie stavových premenných) (pozri obr. 26.6.3.2.). Stavové premenné sú zoskupené do rôznych kategórií, a to: ![]({{ '/assets/icons/post_icons/mo_analysis_icon.jpg' | relative_url }}) (Analýza), ![]({{ '/assets/icons/post_icons/mo_deformation_icon.jpg' | relative_url }}) (Deformácia), ![]({{ '/assets/icons/post_icons/mo_thermal_sv_icon.jpg' | relative_url }}) (Tepelné vlastnosti), ![]({{ '/assets/icons/post_icons/mo_heating_sv_icon.jpg' | relative_url }}) (Ohrev), ![]({{ '/assets/icons/post_icons/mo_micro_sv_icon.jpg' | relative_url }}) (Mikrostruktúra), ![]({{ '/assets/icons/post_icons/mo_diffn_sv_icon.jpg' | relative_url }}) (Difúzia), ![]({{ '/assets/icons/post_icons/mo_prop_sv_icon.jpg' | relative_url }}) (Vlastnosti), ![]({{ '/assets/icons/post_icons/mo_user_sv_icon.jpg' | relative_url }}) (Používateľ) a ![]({{ '/assets/icons/post_icons/mo_postprocssing_sv_icon.jpg' | relative_url }}) (Termomechanické), ku ktorým sa dostanete pomocou ikon zobrazených na obr. 26.6.3.1.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image001.jpg' | relative_url }})

Skupiny stavových premenných

Na zobrazenie stavových premenných ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) je potrebné vybrať premennú a jej zložku (pozri obr. 26.6.3.2.). Tiež je potrebné vybrať jeden z typov škálovania: globálne (min/max všetkých objektov pre všetky kroky simulácie), lokálne (min/max všetkých objektov pre konkrétny krok) a užívateľsky definované (ktoré má predvolené globálne hodnoty). V prípade užívateľsky definovaného typu je možné zadávať min/max hodnoty do vstupných polí umiestnených v pravej časti okna. Následne je možné vybrať typ kontúry (čiara/tieňovanie/vektor) a triedu objektov, ktoré sa majú vykresliť, a nakoniec je možné vybrať konkrétne objekty ich zapnutím/vypnutím v stromovej štruktúre objektov. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vykreslí stavová premenná v aktuálnom zobrazení.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image002.jpg' | relative_url }})

Okno so stavovými premennými

**Rôzne typy premenných typu State**

V programe MO Post je možné vykresliť nasledujúce stavové premenné ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}):

**Analytické premenné**

**[2D]:**

  * Minimálna vzdialenosť

  * Hrúbka

**Opotrebenie náradia:**

  * Teplota rozhrania

  * Rýchlosť posuvu

  * Tlak v rozhraní

  * Miera opotrebenia

  * Hĺbka opotrebenia (celková)

  * Životnosť nástroja (počet dielov)

  
**[3D]:**

  * Minimálna vzdialenosť

  * Doba kontaktu

  * Uhol sklopenia

  * Miera rozťažnosti povrchu

  * Plocha povrchu

  * Hrúbka

  
**Opotrebenie náradia:**

  * Teplota rozhrania

  * Rýchlosť posuvu

  * Tlak v rozhraní

  * Miera opotrebenia

  * Hĺbka opotrebenia (celková)

  * Životnosť nástroja (počet dielov)

  * Opotrebovaná geometria

  
**Deformácia [2D, 3D]:**

  * Súradnice

  * Poškodenie

  * Poškodenie uzlov

  * Objem

  * Hustota

  * Účinný kmeň

  * Uzlový kmeň

  * Celkový počet kmeňov

  * Rýchlosť deformácie

  * Stres

  * Uzlový napätie

  * Rýchlosť

  * Relatívna rýchlosť

  * Napätie v chrbte

  * Normálny tlak

  * Uhol otáčania

  * Sila

  
**Tepelné [2D, 3D]:**

  * Teplota

  * Difúzne spájanie

  * Uzlové teplo

  * Tepelný tok

  
**Mikrostruktúra [2D, 3D]:**

  * Objemový podiel

  * Model zrna

  
**Tvrdosť**[2D, 3D]:****

  * Tvrdosť

  * Doba chladenia

  * Rýchlosť chladenia

**Difúzia [2D, 3D]:**

  * Dominantný atóm

  * Tok atómov

  
**Kúrenie [2D, 3D]:**

  * Napätie

  
**Vlastnosti [2D, 3D]:**

  * Materiál

  * Osy materiálu

  
**Používateľ [2D, 3D]:**

  * Uzlové premenné v programe FEM

  * Premenné užívateľských prvkov FEM

  * Zverejniť používateľské premenné

  * Vlastná premenná

  
**Termomechanické [2D, 3D]:**

  * Termomechanické premenné uzlov

  * Premenné termomechanických prvkov

**Aditívna výroba [3D]**

  * Normálna hustota

  * ID vrstvy

**Možnosti zobrazenia**

Pre príslušné stavové premenné sú k dispozícii rôzne možnosti zobrazenia kontúrových grafov, ako napríklad Čiara, Tieňované, Plná plocha, MinMax, Vektorový graf, Izoplocha a Elementárne kontúry. Nastavenia kontúrových grafov je možné tiež meniť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }}) (nastavenia) v dolnej časti okna stavových premenných.

  * **Kontúra čiary [2D, 3D]**: Zobrazí vybranú stavovú premennú vo forme kontúry čiary.

  * **Tienovaná kontúra [2D, 3D]**: Zobrazí vybranú stavovú premennú vo forme tienovanej kontúry.

  * **Solid Contour [2D, 3D]**: Zobrazuje stavovú premennú tak, že každý prvok je vyfarbený konštantnou farbou s veľmi diskrétnymi farebnými prechodmi farebnej škály. To uľahčuje získanie hodnôt z jednotlivých prvkov a vizualizáciu oblastí s nízkymi a vysokými hodnotami.

  * **Elemental Contour [2D, 3D]**: Zobrazuje stavovú premennú, pričom každý prvok je vyfarbený konštantnou farbou s veľmi plynulými farebnými prechodmi farebnej stupnice. Vďaka tomu je možné ľahko vizualizovať oblasti s nízkymi a vysokými hodnotami.

  * **Vektorový graf [2D, 3D]**: Táto funkcia znázorňuje premenné ako vektorové veličiny, t. j. s veľkosťou a smerom. Týmto spôsobom je možné znázorniť len určité premenné, ako napríklad rýchlosť a posun. Informácie o nastavení veľkosti, tvaru a hustoty vektorového grafu nájdete v časti Nastavenia stavových premenných – Vektor.

  * **Izo-povrch [3D]**: Izo-povrch je povrch, ktorý znázorňuje body s konštantnou hodnotou. Tento typ grafu znázorňuje rovinu, pozdĺž ktorej je konkrétna hodnota stavovej premennej v rámci objektu konštantná. Informácie o vlastnostiach izo-povrchu nájdete v časti Nastavenia stavových premenných – Izo-povrch.

  * **Graf minimálnych a maximálnych hodnôt [3D]**: Tento typ grafu zobrazuje iba minimálne a maximálne hodnoty definovanej premennej na obrobku.

**Nastavenia stavových premenných**

**[2D, 3D]**: Tu sú k dispozícii možnosti na úpravu nastavení typov zobrazenia stavových premenných – kontúry, vektory a izopovrchy. Toto tlačidlo (Nastavenia) sa nachádza v spodnej časti okna „Stavové premenné“.

  
**Nastavenia obrysov**: Nastavenia obrysov slúžia na úpravu nastavenia nadpisu, popisu, tieňovaných obrysov, čiarových obrysov a pomeru minimálnej a maximálnej veľkosti grafu. 

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image003.jpg' | relative_url }})

Contour – Okno nastavení typu nadpisu

  * **Názov**: Používateľ môže zmeniť názov aktivovaním možnosti „Názov definovaný používateľom“ a zmeniť farbu a písmo, ako je znázornené na obr. 26.6.3.3.

  * **Štítok**: Používateľ môže zmeniť formát čísla tak, aby obsahoval nastavený počet desatinných miest, zmeniť farbu obrysu čiary a písma. Môže tiež zapnúť alebo vypnúť zobrazenie minimálnej a maximálnej hodnoty. (Pozri obr. 26.6.3.4.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image004.jpg' | relative_url }})

Contour – Okno nastavení typu štítku

  * **Vytienené**: Používateľ si môže vybrať typ farebnej lišty a počet hodnôt. (Pozri obr. 26.6.3.5.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image005.jpg' | relative_url }})

Contour – Okno nastavení typu s tieňovaním

  * **Čiara:** Pomocou tohto nastavenia môžete ovládať farbu obrysu čiary, počet čiar, hrúbku a štýl (pozri obr. 26.6.3.6.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image006.jpg' | relative_url }})

Contour – Okno nastavení typu čiary

  * **Graf minimálnych a maximálnych hodnôt**: Používateľ môže nastaviť veľkosť grafu minimálnych a maximálnych hodnôt pomocou možnosti pomeru veľkostí, ako je znázornené na obrázku [Fig. 26.6.3.7.](26_6_3_state_variables.htm#Fig_26_6_3_7_Contour__Min/Max_plot_type_settings_window)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image007.jpg' | relative_url }})

Contour – Okno nastavení typu grafu „Min/Max“

**Nastavenia izoplochy [3D]**: Nastavenia izoplochy slúžia na zmenu počtu izoploch a hodnôt v grafe izoplochy. Po vykreslení izoplochy pre ľubovoľnú stavovú premennú môže používateľ kliknúť na tlačidlo nastavení a zmeniť počet izoploš, a dokonca aj hodnoty rovín izoploš pomocou posuvníka Hodnota, ako je znázornené na obr. 26.6.3.8. Upravené nastavenia je možné uložiť ako predvolené zaškrtnutím políčka Nastaviť ako predvolené.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image008.jpg' | relative_url }})

Okno nastavení typu zobrazenia premennej stavu izopovrchu

  
**Nastavenia vektorov**: Nastavenia vektorov slúžia na úpravu typu vektorov, pomeru vzorkovania, dĺžky tela, hrúbky, typu hlavy a mierky hlavy. 

  * **Všeobecné nastavenia:** Používateľ môže v časti „Všeobecné nastavenia“ zmeniť typ vektora na konštantnú alebo premennú veľkosť a môže tiež zmeniť pomer vzorkovania, ako je znázornené na obr. 26.6.3.9.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image009.jpg' | relative_url }})

Okno s všeobecnými vlastnosťami zobrazenia v programe Vector

  * **Telo**: Používateľ môže zmeniť hrúbku vektorového tela a tiež nastaviť minimálnu a maximálnu dĺžku v nastaveniach „Telo“, ako je znázornené na obr. 26.6.3.10.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image010.jpg' | relative_url }})

Okno vlastností zobrazenia vektorového telesa

  * **Hlava:** Používateľ môže zmeniť typ hlavy a v rámci možnosti „Hlava“ môže tiež nastaviť jej mierku, ako je znázornené na obr. 26.6.3.11.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image011.jpg' | relative_url }})

Okno vlastností zobrazenia vektorovej hlavy

**Nastavenia ovládacích prvkov**

  
**Zmenšovanie a zväčšovanie [2D, 3D]** :

  * **Lokálne (aktuálny krok)**: Pre každý krok platia odlišné minimálne a maximálne hodnoty. To zabezpečuje lepšie rozlíšenie v rámci jedného kroku, avšak v priebehu viacerých krokov dochádza k posunu farieb, čo sťažuje sledovanie vývoja premenných. (Pozri obr. 26.6.3.12.)

  * **G******lo** bal (všetky kroky)**: Pre každý krok sa použije rovnaká minimálna a maximálna hodnota. To uľahčuje sledovanie vývoja premennej v priebehu viacerých krokov, avšak na úkor rozlíšenia v rámci jedného kroku. (Pozri obr. 26.6.3.12.)

  * **Globálne (definované používateľom)**: Pre každý krok sa použije rovnaká minimálna a maximálna hodnota, ktorú môže definovať používateľ. Toto je obzvlášť užitočné pre stavové premenné, ktoré vykazujú malé oblasti s extrémnymi hodnotami. Rozlíšenie zostávajúcej oblasti sa môže stratiť v dôsledku automatického prispôsobenia mierky extrémnemu vrcholu. Nastavenie maximálnych a minimálnych hodnôt na rozumnejšie hodnoty síce zníži výraznosť vrcholových hodnôt, ale poskytne oveľa lepšie rozlíšenie pre medzihodnoty. (Pozri obr. 26.6.3.12.)

  * **Obmedzenia objektov**: Funkcia „Obmedzenia objektov“ umožňuje používateľovi nastaviť rôzne minimálne a maximálne hodnoty pre rôzne objekty. Táto funkcia je aktivovaná iba pre čiarové obrysy. (Pozri obr. 26.6.3.12.)

  * **Používateľské premenné**: Používateľské premenné umožňujú v postprocesore vykresliť ľubovoľnú používateľskú premennú. (Pozri obr. 26.6.3.12.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image012.jpg' | relative_url }})

Ovládanie stavových premenných – okno „Vlastnosti mierky“

  
**Hranica farieb** : 

**[2D, 3D]** Obmedzenie farieb je možné aktivovať zaškrtnutím políčok „Cutoff Min“ a „Cutoff Max“ a nastavením rozsahu. Oblasť rozsahu obmedzenia je možné zobraziť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a túto oblasť je možné uložiť ako vlastnú oblasť pomocou tlačidla „Uložiť ako vlastnú oblasť“ (pozri obr. 26.6.3.13.), aby si používateľ mohol zobraziť rozloženie ostatných stavových premenných v rámci tejto oblasti. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image013.jpg' | relative_url }})

Definovanie farebnej hranice

  
Na nižšie uvedenom obr. 26.6.3.14. V ľavom okne je stavová premenná Efektívne deformácie znázornená pomocou škálovania typu Užívateľ s hodnotami Min: 0,00 a Max: 2 bez definovania funkcie obmedzenia farieb a v pravom okne je stavová premenná Efektívne deformácie znázornená pomocou škálovania typu Užívateľ s hodnotami Min: 0,00 a Max: 2 a s funkciou obmedzenia farieb. Môžeme pozorovať, že v pravom okne, kde sa používa funkcia „Color cutoff“, systém zobrazuje iba tie oblasti objektu, ktoré sa nachádzajú v rozsahu ohraničenia.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image014.jpg' | relative_url }})

Funkcia obmedzenia farieb

  * **Ďalšie možnosti na karte „Control“ [2D, 3D]**: Histogram: Zobrazuje histogram rozdelenia stavovej premennej v danom kroku.

  * **Vylúčenie tuhej zóny**: Všeobecný riešenie rýchlosti môže byť kombináciou tuhých a deformujúcich sa rýchlostných polí. Pri modeloch, ako je valcovanie tvarov alebo valcovanie prstencov, sa väčšina obrobku nachádza v tuhej zóne s rýchlostným poľom. Ak chcete zobraziť čisto deformujúce sa rýchlostné pole v deformujúcej sa zóne, môžete použiť túto funkciu.

  * **Žiadne zníženie** : <Text, ktorý sa má pridať>

  * **Vlastná oblasť**: Slúži na výber konkrétnej oblasti na objekte, ktorú chcete skúmať. Po zaškrtnutí tohto políčka musí používateľ vybrať požadovanú oblasť štúdia kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Definovať) vedľa políčka. Následne sa v ľavej palete grafického okna zobrazia možnosti výberu uzlov v požadovanej oblasti. V programe DEFORM-V12 je funkcia „Iba vybraný uzol“ dostupná prostredníctvom možnosti „Vlastná oblasť“. V starších verziách mohol používateľ zobraziť vybranú oblasť iba vo forme tieňovaného zobrazenia, od verzie DEFORM-V12 sa zobrazenie vybranej oblasti rozšírilo aj na plné tieňovanie. 

**Nastavenia vychýlenia**

**[2D, 3D] :** Používateľ môže zmenu tvaru zväčšiť alebo zmenšiť pomocou posuvníka alebo zmenou hodnôt, ako je znázornené na obr. 26.6.3.15 a obr. 26.6.3.16.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image015.jpg' | relative_url }})

Okno deformácie pre 2D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image016.jpg' | relative_url }})

Okno deformácie pre 3D

Používateľ môže skryť alebo zobraziť ohraničenie referenčného objektu a môže tiež zmeniť jeho farbu, ako je znázornené na obr. 26.6.3.17.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image017.jpg' | relative_url }})

Deformácia – referenčná voľba pre 2D

**3D**: Používateľ môže tiež zmeniť priehľadnosť referenčného objektu tak, že aktivuje možnosť „Použiť priehľadnosť“ a posunie posuvník, ako je znázornené na obr. 26.6.3.18.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image018.jpg' | relative_url }})

Použiť okno „Transparentnosť – Odklon“

**Súradnice**

  * **Obdĺžnikové a valcové súradnice** : 

**[3D]** : V súčasnosti existujú dva typy súradnicových systémov, v ktorých je možné zobraziť zložky napätia, deformácie a rýchlosti deformácie: kartézske (pravoúhlé) a valcové. Dekartské súradnice sú predvolené nastavenie, avšak tlačidlo „Súradnice“ v okne vlastností zobrazenia umožňuje používateľovi prepnúť na valcové súradnice (len v 3D, pozri obr. 26.6.3.19.). Kliknutím na kartu „Súradnice“ sa otvorí okno, v ktorom môže používateľ vybrať valcové súradnice. Používateľ musí pre valcové súradnice definovať os z. Táto os sa definuje prostredníctvom jedného bodu na osi z a jedného smeru vektora. Používateľ môže použiť ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) na výpočet parametrov „Center“ a „Z 'direction value“. Toto funguje pre kontúrové grafy aj pre sledovanie bodov. Valcové súradnice sa nezobrazia, kým používateľ nevyberie zložky napätia, deformácie alebo rýchlosti deformácie.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image019.jpg' | relative_url }})

Okno vlastností valcových súradníc

**[2D]:** **Karteziánske alebo pravouhlé súradnice** sú predvoleným nastavením pre 2D databázu. Tá obsahuje zložky R,Z, Theta a RZ pre typy geometrie „Axi-symmetric“ a „Torsion“, zatiaľ čo pre typy „Plane strain“ a „Plane stress“ sú k dispozícii len zložky X, Y a XY. (Pozri obr. 26.6.3.20.)

  * **Definované používateľom [2D, 3D]** : 

Tento súradnicový systém možno použiť na znázornenie zložiek premennej v ľubovoľnom smere.

**[2D]** : (Iba pre rovinné deformácie a rovinné napätia) Pomocou tejto funkcie môže používateľ vybrať požadovaný uhol osi vzhľadom na aktuálnu os, aby mohol vyniesť premenné na túto os. (Pozri obr. 26.6.3.20.)

Ak používateľ vykreslí komponent „User defined axis1“, zadaním uhla 0, 180 alebo 360 sa vykreslí zložka X premennej; zmenou tohto uhla na 90 alebo 270 sa vykreslí zložka Y premennej.

Ak používateľ vykreslí os 1–2 definovanú používateľom, zadaním uhla 0, 180 alebo 360 sa vykreslí zložka XY premennej; zmenou tohto uhla na 90 alebo 270 sa vykreslí zložka -XY premennej.

**[3D]** : Pomocou tejto voľby môže používateľ vybrať os, na ktorej chce znázorniť premennú v dvoch poskytnutých riadkoch. (Pozri obr. 26.6.3.21.)

Ak používateľ vykreslí zložku „User defined axis1“, potom zadaním čísla 1 do bunky X v 1. riadku a čísla 1 do bunky X v 2. riadku vykreslí zložku X danej premennej; podobne to platí aj pre zložky Y a Z.

Ak používateľ vykreslí zložku „User defined axis1“, zadá hodnotu 1 do bunky Y v 1. riadku a hodnotu 1 do bunky Z v 2. riadku, vykreslí sa zložka YZ danej premennej; podobne to platí aj pre zložky XY a ZX.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image020.jpg' | relative_url }})

Okno vlastností užívateľsky definovaných súradníc pre 2D s oknom SV zvýrazneným s premennými stavu užívateľsky definovaných osí

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image021.jpg' | relative_url }})

Okno vlastností užívateľsky definovaných súradníc pre 3D s oknom SV zvýrazneným pomocou premenných stavu užívateľsky definovaných osí

  * **Lokálna (os materiálu)**

**[2D, 3D] :** Ak používateľ použije lokálnu os materiálu, premenné sa budú znázorňovať vzhľadom na lokálnu os materiálu každého prvku. K stavovým premenným, pre ktoré sú implementované lokálne osi materiálu, je možné pristupovať z okna stavových premenných, ako je znázornené na obr. 26.6.3.22 nižšie.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image022.jpg' | relative_url }})

Okno SV zvýraznené pomocou premenných stavu osí miestneho materiálu

**Mapovanie**

**[2D, 3D]:** Špeciálnu premennú následného spracovania je možné „**priradiť**“ zo stavovej premennej uloženej v databáze prostredníctvom vyhľadávacej tabuľky (pozri obr. 26.6.3.23.). Používateľ vyberie stavovú premennú v strome, potom definuje názov novej používateľsky definovanej stavovej premennej a zadá hodnoty krížových odkazov.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image023.jpg' | relative_url }})

Okno SV Mapping

**Postup definovania mapovania**:

  * Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

  * Vyberte premennú „State“

  * Kliknite na kartu „Mapovanie“

  * Zaškrtnite políčko „Použiť mapovanie SV“

  * Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte novú užívateľsky definovanú stavovú premennú

  * Zadajte názov pre užívateľskú stavovú premennú

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) a definujte vyhľadávaciu tabuľku.

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image024.jpg' | relative_url }})

Príklad mapovania stavových premenných

**Pomer prípustných hodnôt**  
Ide o akýsi bezpečnostný graf, v ktorom pomery udávajú, v ktorých oblastiach dochádza k prekročeniu bezpečnostného limitu podľa údajov v definovanej tabuľke pre danú premennú, napríklad pre maximálne hlavné napätie. Ak napríklad v tabuľke definujeme bezpečnú hodnotu maximálneho hlavného napätia pri rôznych teplotách, tento graf by mal znázorniť tento pomer na objekte, pričom oblasti/hodnoty nad 1,0 by označovali oblasti, v ktorých je prekročený bezpečnostný limit. (Pozri obr. 26.6.3.25.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image025.jpg' | relative_url }})

Pomer prípustných hodnôt

**Referencia**

**[3D]:** Používateľ môže teraz definovať referenčný rámec na výpočet minimálnej vzdialenosti. Keď používateľ vyberie stavovú premennú „Minimálna vzdialenosť“, na stránke „Stavové premenné“ sa zobrazí záložka „Referenčný rámec“ (pozri obr. 26.6.3.26.). Na karte „Referenčné“ môže používateľ kliknutím na tlačidlo zaškrtnúť políčko „Zapnúť referenčnú plochu“ a vybrať referenčný rámec; systém potom použije tento referenčný rámec na výpočet minimálnej vzdialenosti (pozri obr. 26.6.3.27.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image026.jpg' | relative_url }})

Premenná stavu – karta „Referencie“

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image027.jpg' | relative_url }})

Možnosť výberu referenčnej plochy

**Nastavenia opotrebenia nástrojov**  
Premenné týkajúce sa rýchlosti opotrebenia nástroja a analýzy životnosti nástroja je možné skontrolovať s použitím rôznych parametrov modelu opotrebenia nástroja a kritérií životnosti nástroja (pozri obr. 26.6.3.29 a obr. 26.6.3.30). Zmena parametrov rýchlosti opotrebenia nástroja sa okamžite prejaví vo výpočte rýchlosti opotrebenia. K týmto parametrom sa dostanete na karte Opotrebenie nástroja, aktivujú sa však až po výbere príslušných premenných stavu analýzy, ako je znázornené na obr. 26.6.3.28.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image028.jpg' | relative_url }})

Stavová premenná – možnosti opotrebenia nástroja

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image029.jpg' | relative_url }})

Nastavenia miery opotrebenia nástrojov

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image030.jpg' | relative_url }})

Nastavenia životnosti nástroja

**Kmeň – celkom**  
Používateľ si môže prispôsobiť zobrazenie premennej „Celková deformácia“ vypnutím príslušných komponentov na karte „Deformácia – Celková“, ako je znázornené na obr. 26.6.3.31 nižšie. Karta „Deformácia – Celková“ sa aktivuje, keď používateľ v dialógovom okne „Stavová premenná“ vyberie položku „Deformácia – Celková“.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image031.jpg' | relative_url }})

Okno s možnosťami výberu „Strain Total“

**Relatívna rýchlosť**  
Relatívna rýchlosť umožňuje používateľovi znázorniť relatívnu rýchlosť vo vzťahu k iným objektom. Používateľ si môže vybrať buď posun, alebo rotáciu, aby mohol sledovať príslušný relatívny pohyb, a z roletového menu „Referencia“ si môže vybrať referenčný objekt, vo vzťahu ku ktorému sa má znázorniť relatívna rýchlosť (pozri nižšie obr. 26.6.3.32).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_3_state_variables/image032.jpg' | relative_url }})

Okno s možnosťami výberu relatívnej rýchlosti
