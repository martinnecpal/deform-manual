---
lang: sk
title: "26.6.24. Diagram formovacích limitov"
---

# 26.6.24 Diagram medzí tvárnosti (FLD)

Limity tvárnosti pri tvárnení plechov určujú mieru deformácie, ktorú je možné dosiahnuť bez porušenia v podobe zúženia, zlomu alebo zvlnenia. Používateľ môže vybrať ikonu diagramu limitov tvárnosti (FLD) z panela nástrojov, ako je znázornené na obr. 26.6.24.1., aby definoval nastavenia súvisiace s FLD a zobrazil krivku FLD. 

Keď používateľ klikne na ikonu FLD ![]({{ '/assets/icons/post_icons/mo_fld_icon.jpg' | relative_url }}), otvorí sa okno „Forming Limit Diagram“ (Diagram tvárnických medzí), ako je znázornené na obr. 26.6.24.2. V okne „Forming Limit Diagram“ môže používateľ definovať krivku tvárnických medzí spolu s bezpečnostnou bariérou, jednoduchou krivkou ťahu (faktor R) a jednoduchou krivkou šmyku. Používateľ môže vykresliť graf FLD s ľubovoľnou z týchto možností alebo s ľubovoľnou kombináciou týchto možností, ako je znázornené na obr. 26.6.24.9.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0001.jpg' | relative_url }})

Ikona FLD na paneli nástrojov

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0002.jpg' | relative_url }})

Okno „Diagram limitov tvárnenia“

## Krivka formovacích medzí

Nástup zúženia je najčastejšie používaným limitom tvárnosti pri tvárnení plechov a zvyčajne sa znázorňuje ako krivka v tvare písmena „V“, nazývaná tiež krivka medze tvárnosti (FLC), ako je znázornené na obr. 26.6.24.3. Krivka FLC udáva mieru deformácie, ktorú je možné vyvinúť na plechový diel, na základe čoho je možné predpovedať poškodenie. Po definovaní krivky formovateľnosti môže používateľ kliknúť na tlačidlo na vytvorenie grafu, ako je znázornené na obr. 26.6.24.3, následne sa vykreslí graf FLD s rozložením uzlov, ktorý znázorňuje uzly, kde môže dôjsť k zlomu, a uzly, ktoré sú bezpečné, a premenná FLD sa vykreslí na diele v zobrazovacej oblasti, ako je znázornené na obr. 26.6.24.4.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0003.jpg' | relative_url }})

Definícia krivky formovacej medze (FLC)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0004.jpg' | relative_url }})

Po aplikácii krivky FLC

## Bezpečnostná bariéra

Používateľ môže nastaviť bezpečnostnú rezervu pomocou bezpečnostnej bariéry; krivka bezpečnostnej bariéry je definovaná pod krivkou formovacej medze. Po definovaní bezpečnostnej bariéry, ako je znázornené na obr. 26.6.24.5, môže kliknúť na tlačidlo „Plot“ (Vykresliť), na čo sa vygeneruje graf FLD s uzlovým rozložením, ktorý znázorňuje uzly, ktoré sú v bezpečnej zóne, uzly, ktoré sa nachádzajú v bezpečnostnej rezervy (medzi bariérou a krivkou FLC), a uzly, v ktorých môže dôjsť k zlomu, ako je znázornené na obr. 26.6.24.6. Keď používateľ po definovaní bezpečnostnej bariéry klikne na tlačidlo „vykresliť“, vykreslí sa stavová premenná FLD, ktorá znázorňuje oblasti, ktoré sa nachádzajú v bezpečnej zóne, v bezpečnostnej rezervnej zóne a kde môže dôjsť k porušeniu. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0005.jpg' | relative_url }})

Definícia bezpečnostnej bariéry

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0006.jpg' | relative_url }})

FLD po definovaní FLC a bezpečnostnej bariéry

## Jednoduchá krivka napätia

Na odhad tendencie k zvlneniu je možné definovať jednoduchý faktor R založený na napätí. Po definovaní faktora R a FLC, ak používateľ klikne na tlačidlo „plot“, graf sa aktualizuje o jednoduchú krivku napätia, ktorá znázorňuje uzly, ktoré sú v bezpečí pred tvorbou vrások a zlomením, miesta, kde môže dôjsť k zlomeniu, a miesta, kde sa pozoruje tvorba vrások, ako je znázornené na obr. 26.6.24.7. Premenná FLD je vynesená na diele a znázorňuje oblasti na základe grafu FLD, pozri obr. 26.6.24.7.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0007.jpg' | relative_url }})

FLD po definovaní FLC a jednoduchej krivky napätia

## Jednoduchá krivka šmyku

Používateľ môže zaškrtnúť políčko „Jednoduchá krivka šmyku“ a „FLC“ a vykresliť graf podobný krivke jednoduchého ťahu, ktorý znázorňuje uzly, ktoré sú odolné voči zvlneniu a zlomeniu, ako je znázornené na obr. 26.6.24.8. Premenná FLD je vynesená na diele, pričom znázorňuje oblasti na základe grafu FLD, pozri obr. 26.6.24.8.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0008.jpg' | relative_url }})

FLD po definovaní FLC a krivky jednoduchého šmyku

Používateľ môže zaškrtnúť všetky políčka FLC, Bezpečnostná bariéra, Jednoduchá krivka ťahu a Jednoduchá krivka šmyku a vykresliť graf zobrazujúci uzly, ktoré sú v bezpečnej vzdialenosti od tendencie k zvlneniu, zvlnenia a zlomu, miesta, kde môže dôjsť k zlomu, miesta, kde dôjde k zvlneniu, a uzly vykazujúce tendenciu k zvlneniu, ako je znázornené na obr. 26.6.24.9. Premenná FLD je vynesená na diele, pričom znázorňuje oblasti na základe grafu FLD, pozri obr. 26.6.24.9.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0009.jpg' | relative_url }})

Krivka FLD

## Hrúbka

Keď v okne diagramu limitov tvárnenia vyberieme ikonu hrúbky, štandardne sa na zmenšenie použijú hodnoty premenných „Min.“ a „Max.“ hrúbky, ako je znázornené na obr. 26.6.24.10. Používateľ môže hodnoty mierky upraviť a graf stavových premenných nad tvárneným dielom sa podľa toho aktualizuje.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0010.jpg' | relative_url }})

Graf hrúbky

## Škody

Keď v okne diagramu limitov tvárnenia vyberieme ikonu poškodenia, štandardne sa na zmenšenie použijú hodnoty premenných „Min. poškodenie“ a „Max. poškodenie“, ako je znázornené na obr. 26.6.24.11. Používateľ môže hodnoty mierky upraviť a graf stavových premenných nad tvárneným dielom sa podľa toho aktualizuje.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_24_forming_limit_diagram/image0011.jpg' | relative_url }})

Graf poškodenia
