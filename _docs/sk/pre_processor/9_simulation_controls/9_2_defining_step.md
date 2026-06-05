---
lang: sk
title: "9.2. Definovanie kroku"
---

# 9.2. Definovanie kroku

9.2.1. Kroky simulácie

  * Počiatočné číslo kroku (NSTART)

  * Počet simulačných krokov (NSTEP)

  * Krok pri ukladaní (STPINC)

  * Primárny čip (PDIE)

9.2.2. Krok

  * [Step increment control (DSMAX/DTMAX)](9_2_defining_step.htm#Step_increment_control_\(DSMAX/DTMAX\))

  * Definícia kroku (STPDEF)

  * Výber časového kroku a počtu krokov

  * Ovládacie prvky pre nastavenie krokov

  * Pokročilé ovládacie prvky krokov

## Kroky simulácie ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }})

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií špecifikovaných v ponuke ovládacích prvkov krokov, ako je znázornené na obr. 9.2.1.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_2_defining_step/9_2_image001.jpg' | relative_url }})

Kroky simulácie

**Počiatočné číslo kroku (NSTART)****[2D, 3D]**

Ak sa zapisuje do novej databázy, zadané číslo kroku ([NSTART](/docs/sk/keyword_documentation/n/nstep/)) bude prvým krokom v tejto databáze. Ak sa údaje zapisujú do existujúcej databázy, údaje z predspracovania sa do nej pripíšu v správnom číselnom poradí a všetky kroky nasledujúce po zadanom kroku sa prepíšu.  
Znak mínus (-n) pri čísle kroku znamená, že tento krok do databázy zapísal predspracovateľ (buď ručným vytvorením databázového kroku, alebo automatickým prečlenením siete), a nie simulačný modul.

Poznámka:   
Všetky kroky vygenerované predspracovateľom by mali mať záporné číslo kroku.

**Počet simulačných krokov (NSTEP)** **[2D, 3D]**

Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú spustiť od počiatočného čísla kroku. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí príkaz na zastavenie simulácie alebo ak simulácia nenarazí na problém. Napríklad, ak je počiatočné číslo kroku -35 ([NSTART](/docs/sk/keyword_documentation/n/nstep/)) a je špecifikovaných 30 krokov ([NSTEP](/docs/sk/keyword_documentation/n/nstart/)), simulácia sa zastaví po 65. kroku, pokiaľ sa najskôr nespustí iná kontrola zastavenia.

**Krok pri ukladaní (STPINC) [2D, 3D]**

Krok prírastku ([STPINC](/docs/sk/keyword_documentation/s/stpinc/)), ktorý sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nemusí sa nutne uložiť do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať viac úložného priestoru.

**Primárny čip (PDIE) [2D, 3D]**

Primárny lis ([PDIE](/docs/sk/keyword_documentation/p/pdie/)) je objekt, pre ktorý je definovaných mnoho kritérií zastavenia a krokovania. Napríklad brzdná vzdialenosť založená na zdvihu primárneho lisu. Keď zdvih objektu definovaného ako primárny lis dosiahne hodnotu posunu primárneho lisu, simulácia sa zastaví bez ohľadu na to, či boli špecifikované ďalšie kroky. Funkcia Step By Stroke určuje veľkosť kroku na základe pohybu primárneho lisovacieho nástroja.  
Hlavná forma sa zvyčajne priraďuje k objektu, ktorý je najviac pod kontrolou kováčskeho stroja. Napríklad forma pripevnená k piestu mechanického lisu by bola označená ako hlavný objekt.

**Ovládacie prvky sekundárneho kroku (STPINC) [2D, 3D]**  
Možnosť „Sekundárne nastavenia krokov“ umožňuje zmeniť veľkosť kroku pri ukladaní pre určitú časť simulácie. Táto možnosť je užitočná v prípade, ak používatelia chcú pre určitú časť simulácie ukladať buď viac, alebo menej krokov. Akonáhle zvolená hodnota nastavenia zastavenia dosiahne definovanú hodnotu „Sekundárne nastavenia krokov“, bude sa pri ukladaní krokov do databázy zohľadňovať hodnota „Sekundárneho kroku“.  
Túto možnosť môžeme použiť v spojení s regulačnými prvkami „Čas“, „Posun primárnej matrice“, „Zaťaženie primárnej matrice“, „Pomer kontaktnej plochy“ a „Minimálna vzdialenosť matríc“.   
Po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) sa na základe zvoleného kritéria ukončenia odhadne posledných 10 % procesu. Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) bude aktívne len vtedy, ak sú definované príslušné údaje o kritériách ukončenia.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_2_defining_step/9_2_image006.jpg' | relative_url }})

Možnosť nastavenia sekundárneho kroku

## Krok prírastku ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})

Možnosti nastavenia kroku nájdete na obr. 9.2.3.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_2_defining_step/9_2_image002.jpg' | relative_url }})

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_2_defining_step/9_2_image003.jpg' | relative_url }})  
b) 

Ovládacie prvky krokov; (a) pre 2D (b) pre 3D

**Ovládanie krokovania (DSMAX/DTMAX)** **[2D, 3D]**

Používateľ môže definovať (maximálnu povolenú) veľkosť časového kroku ako funkciu „zdvihu“ ([DSMAX](/docs/sk/keyword_documentation/d/dsmax/)) alebo „času“ ([DTMAX](/docs/sk/keyword_documentation/d/dtmax/)).  
Veľkosť kroku riešenia je možné riadiť časovým krokom alebo posunom primárneho lisovacieho nástroja. Ak je zadaný zdvih na krok, primárny lisovací nástroj sa v každom časovom kroku posunie o zadanú vzdialenosť. Celkový pohyb primárneho lisovacieho nástroja bude predstavovať posun na krok vynásobený celkovým počtom krokov. Ak je špecifikovaný čas na krok, použije sa časový interval na krok. Posun lisovacieho nástroja na krok bude predstavovať časový krok vynásobený rýchlosťou lisovacieho nástroja.  
Od verzie 3DV61 bola definícia riadenia krokového prírastku vylepšená tak, aby zahŕňala krokové funkcie závislé od času aj od zdvihu. To znamená, že veľkosť kroku (či už ide o čas na krok alebo zdvih na krok) je teraz možné definovať ako funkciu času alebo zdvihu. Táto funkcia umožňuje v prípade potreby dosiahnuť jemnejšie rozlíšenie uložených informácií o modeli. (typicky smerom ku koncu zdvihu, kde môžu nastať prudké zmeny zaťaženia formy a plnenia dutiny alebo tvorby otrepu).  
Počet zdvihov na krok je často intuitívnejší. Čas na krok je však potrebné určiť pri každej úlohe, v ktorej nedochádza k pohybu lisovacej formy (napríklad pri prenose tepla), alebo pri každej úlohe, kde sa využíva regulácia sily. 

**Definícia kroku (STPDEF) [2D, 3D]**

Na definovanie krokov sú k dispozícii tri režimy ([STPDEF](/docs/sk/keyword_documentation/s/stpdef/)),

  * **Používateľ** V režime krokov definovaných používateľom zodpovedajú kroky hodnote [NSTEP](/docs/sk/keyword_documentation/n/nstep/). Ide o predvolené nastavenie, ktoré vo väčšine prípadov nie je potrebné meniť.
  * **Systém** V režime definovaných krokov systému sa každý čiastkový krok uloží do databázy a považuje sa za samostatný krok. Táto možnosť sa používa predovšetkým na účely ladenia.
  * **Teplota** Pri krokovaní založenom na teplote sa časové krokovanie riadi nastaveniami [DTPMAX](/docs/sk/keyword_documentation/d/dtpmax/). Účelom týchto nastavení je určiť časové krokovanie simulácie, ktorá je riadená deformáciou vyvolanou teplotou.

**Výber časového kroku a počtu krokov [2D, 3D]**

Správny výber časového kroku je dôležitý. Príliš veľký časový krok môže spôsobiť nepresnosť riešenia, rýchle deformácie siete alebo problémy s konvergenciou. Príliš malý časový krok môže viesť k zbytočne dlhým časom výpočtu. Nasledujúca časť obsahuje niekoľko odporúčaní pre výber časových krokov. Maximálny posun pre akýkoľvek uzol by nemal prekročiť približne 1/3 dĺžky hrany prvku v jednom kroku. V prípade prúdenia okolo ostrého rohu, formovania výstupkov alebo podobných vysoko lokalizovaných deformácií môže byť potrebné definovať časové kroky tak, aby pohyb uzla bol čo najmenší, napríklad 1/10 dĺžky hrany prvku. Pre jemnejšiu sieť sú teda potrebné menšie kroky ako pre hrubšiu sieť. Tým sa zabráni nadmernému skresleniu siete v jednom časovom kroku.  
  
Časový krok možno určiť nasledujúcou metódou:

  * Pomocou meracieho nástroja zmerajte jeden z menších prvkov deformovaného objektu (toto je potrebné urobiť až po vytvorení siete)
  * Odhadnite maximálnu rýchlosť v ľubovoľnej oblasti obrobku (v prípade väčšiny úloh to bude rýchlosť matrice. Pri úlohách s extrudovaním to bude rýchlosť matrice vynásobená pomerom extrudovania). Ak už boli vykonané niektoré kroky, zobrazte rýchlosť objektu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) (Dáta uzla) (použite ikonu ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) na zobrazenie grafu vektora rýchlosti a maximálnych a minimálnych hodnôt).
  * Výsledok z bodu 1 vydelíme výsledkom z bodu 2 a ako časový krok použijeme približne 1/3 tejto hodnoty. Ide o hrubý odhad, takže extrémna presnosť nie je rozhodujúca.
  * Počet krokov je daný vzťahom:

Pozrite si tiež funkciu „Dĺžka podkroku polygónu“ v časti „Pokročilé nastavenia krokov“. Ak nie je k dispozícii dostatok informácií na výpočet celkového počtu krokov, máte na výber tri možnosti:

  * Ako všeobecné pravidlo možno použiť zníženie výšky o 1 % až 3 % na jeden schod.
  * Zadajte ľubovoľne veľký počet krokov a použite alternatívny kritérium na ukončenie, napríklad čas alebo celkový počet zdvihov matrice.
  * Odhadnite počet krokov potrebných pre danú veľkosť kroku a potom zadajte približne 120 % tejto hodnoty. Nechajte simuláciu prekročiť cieľovú hodnotu a ako konečné riešenie použite hodnotu blízko konca, ale nie priamo na konci.

**Ovládacie prvky pre nastavenie krokov**

  * **Deformácia na krok (DEMAX) [2D, 3D]:**

Maximálny prírastok deformácie prvku obmedzuje veľkosť deformácie, ktorá sa môže nahromadiť v ktoromkoľvek jednotlivom prvku počas jedného časového kroku. Ak sa pre premennú [DEMAX](/docs/sk/keyword_documentation/d/demax/) priradí hodnota odlišná od nuly, spustí sa nový podkrok v okamihu, keď prírastok deformácie v ktoromkoľvek prvku dosiahne hodnotu [DEMAX](/docs/sk/keyword_documentation/d/demax/).

  * **Doba kontaktu (DTSUB) [2D, 3D]**

Po zadaní parametra DSMAX alebo DTMAX sa simulácia deformácie môže rozdeliť na menšie čiastkové kroky v závislosti od nastavenia parametra [DTSUB](/docs/sk/keyword_documentation/d/dtsub/).  
  
**[2D]** : Pri predvolenom nastavení [DTSUB](/docs/sk/keyword_documentation/d/dtsub/)= 0,0 systém aktivuje subkrokovanie kontaktov.  
Ak je hodnota [DTSUB](/docs/sk/keyword_documentation/d/dtsub/)= 1,0, nedôjde k žiadnemu subkrokovaniu.  
  
**[3D]** : Parameter „Contact time“ určuje, či sa pri kontakte uzlov s hlavnou plochou vykoná čiastkové rozdelenie kroku. V predvolenom nastavení ([DTSUB](/docs/sk/keyword_documentation/d/dtsub/)= 1), ak sa uzol dotkne hlavnej plochy v priebehu časového kroku, časový krok sa rozdelí a tento krok sa spustí znovu v priebehu časti časového prírastku. Tým sa uzol umiestni na plochu na konci časového kroku. Pri 3D úlohách s veľkým počtom uzlov, ktoré sa dotýkajú hlavných plôch, to môže spôsobiť výrazné predĺženie času spracovania.  
  
Ak je pre [DTSUB](/docs/sk/keyword_documentation/d/dtsub/) nastavená hodnota 1, je deaktivované subkrokovanie kontaktného času. Uzly budú môcť preniknúť cez hlavnú plochu, na konci časového kroku sa však umelo vrátia späť na plochu. Tým sa výrazne skráti čas spracovania. Ak je však definovaný časový krok príliš veľký, môže dôjsť k určitej strate objemu a deformácii siete.  
Všeobecne sa odporúča nastaviť parameter XLPHX0 na hodnotu 1 a dôsledne dodržiavať vyššie uvedené odporúčania týkajúce sa časového kroku. Použitie podkrokovania dĺžky polygónov (XLPHX1) tiež pomáha obmedziť stratu objemu a deformáciu siete bez výrazného predĺženia času výpočtu.

  * **Dĺžka podkroku mnohouholníka (DPLEN) [3D]**

Funkcia obmedzenia dĺžky kroku pri posúvaní hrany ([DPLEN](/docs/sk/keyword_documentation/d/dplen/)) stanovuje hornú hranicu absolútnej vzdialenosti, o ktorú sa môže uzol povrchu posunúť v danom časovom kroku.  

![]({{ '/assets/equations/pre_processor/9_simulation_controls/9_2_defining_step/eq_9_2_2.jpg' | relative_url }}) |   
---|---  
  
  
Povolené hodnoty pre [DPLEN](/docs/sk/keyword_documentation/d/dplen/) sú v rozmedzí od 0 do 1. Hodnota 0 deaktivuje subkrokovanie. Odporúčané hodnoty sú 0,2 až 0,5, pričom hodnota 0,2 je konzervatívnejšia, a teda spomaľuje výpočet, a hodnota 0,49 je agresívnejšia, rýchlejšia, ale menej presná. Hodnoty väčšie ako 0,5 je možné použiť, ale môžu spôsobiť neprijateľnú degeneráciu siete.

  * **Zaškrtávacie políčko „Adaptívne riadenie hĺbky vtlačenia“**

Táto voľba implicitne ovláda počty kontaktov pre modely EP a plastové modely. Od verzie 12.0 bola namiesto umiestňovania súboru **DEF_CNT.DAT** do pracovného adresára implementovaná voľba v grafickom rozhraní.

**Pokročilé ovládacie prvky krokov**

Toto menu ponúka ďalšie možnosti pre špeciálne simulácie, pri ktorých je potrebné presné nastavenie veľkosti časového kroku (pozri obr. 9.2.4.).

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_2_defining_step/9_2_image004.jpg' | relative_url }})

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_2_defining_step/9_2_image005.jpg' | relative_url }})

b)

Rozšírené krokové menu; (a) pre 2D (b) pre 3D

  * **Zmena teploty na jeden krok (DTPMAX) [2D, 3****D]:** Maximálny prírastok zmeny teploty obmedzuje rozsah, o ktorý sa môže teplota ktoréhokoľvek uzla zmeniť počas jedného časového kroku. Ak je priradená hodnota odlišná od nuly, spustí sa nový podkrok, keď zmena teploty v ktoromkoľvek uzle dosiahne hodnotu [DTPMAX](/docs/sk/keyword_documentation/d/dtpmax/). Maximálny/minimálny časový krok je najväčší a najmenší časový krok povolený pri podkrokoch založených na teplote.

  * **Doba deformácie na krok (DTPMAX) [2D]:** Ak sú v skupine „Riadenie krokov na základe deformácie“ pre polia „Min. časový krok“ a „Max. časový krok“ nastavené hodnoty odlišné od nuly, pri každom kroku sa určí nová veľkosť kroku v závislosti od rýchlosti konvergencie riešenia. Ak je rýchlosť konvergencie riešenia dobrá, veľkosť časového kroku sa zvýši. Ak je však rýchlosť konvergencie riešenia slabá, veľkosť časového kroku sa zníži. Minimálne/maximálne časové kroky sú najväčší a najmenší časový krok povolený pri určovaní veľkosti časového kroku. Ak je definované toto riadenie krokov, má vyššiu prioritu ako riadenie zmeny teploty na krok.

  * **Maximálna chyba posuvu [2D]:** Toto nastavenie krokovania sa vo všeobecnosti neodporúča. Pre viac informácií kontaktujte SFTC na čísle [support@deform.com](mailto:support@deform.com).

  * **Zmena objemu na jeden krok (DVMAX) [2D]:** Počas časového kroku deformácie dochádza u prvkov zvyčajne k zmene objemu ([DVMAX](/docs/sk/keyword_documentation/d/dvmax/)). V priebehu času táto zmena objemu zvyčajne vedie k strate objemu. Strata objemu sa zvyčajne zvyšuje s rastúcou veľkosťou krokov a rastúcim celkovým znížením výšky ![]({{ '/assets/equations/pre_processor/9_simulation_controls/9_2_defining_step/dh_h.jpg' | relative_url }}), kde ![]({{ '/assets/equations/pre_processor/9_simulation_controls/9_2_defining_step/dh.jpg' | relative_url }}) označuje zníženie výšky na jeden krok a ![]({{ '/assets/equations/pre_processor/9_simulation_controls/9_2_defining_step/h.jpg' | relative_url }}) označuje výšku objektu. Pri úlohách, kde je strata objemu významná, je možné stratu objemu regulovať aj stanovením maximálnej hodnoty zmeny objemu, ktorú môže jednotlivý prvok alebo objekt zaznamenať počas časového kroku. Ak je priradená hodnota odlišná od nuly, spustí sa nový podkrok, keď pomer zmeny objemu k pôvodnému objemu akéhokoľvek prvku prekročí stanovenú hodnotu.

Súvisiace témy:

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.6. Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)   
[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)
