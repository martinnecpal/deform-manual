---
lang: sk
title: "26.6.12. Sledovanie Flownet"
---

# 26.6.12. Sledovanie Flownet

  * 2D Flownet

  * Obdĺžniková mriežka

  * Vzor z mnohouholníkov

  * Vzor posunu

  * Užívateľsky definovaná sieť Flownet****

  * 3D Flownet

  * Kockový vzor

  * Mriežkový vzor

  * Vzor z mnohouholníkov

  * 2D posun

  * Posun

  * Vzor mriežky na povrchu

  * Užívateľsky definovaná sieť Flownet

  * Sledovanie potrubia

**[2D, 3D]** : Flownet je nástroj na následné spracovanie, ktorý používateľovi umožňuje umiestniť na objekt určitú formu (2D alebo 3D) mriežky a nechať simuláciu sledovať deformáciu mriežky počas celého procesu deformácie. Ako sa deformuje sieť, deformuje sa aj vzor, avšak na rozdiel od siete FEM zostáva vzor počas všetkých prepočítaní siete zachovaný. Flownet sa teda veľmi podobá fyzickému vyrytiu vzoru na priečnom reze obrobku.Je to vynikajúci spôsob, ako vizualizovať akékoľvek potenciálne nepravidelnosti v štruktúre zŕn alebo zobraziť potenciálne povrchové vady, ako sú záhyby. Treba poznamenať, že vzory Flownet je možné generovať iba pre deformujúce sa objekty. Zoznam počiatočných krokov bude obsahovať všetky kroky v zobrazenom okne, ktoré sú aktuálne načítané ako predvolené.

**2D Flownet** :

Oblasť toku siete sa definuje v grafickom okne. Je možné ju vybrať v rámci obrysu alebo hranice objektu. Na definovanie oblasti musí používateľ pridať aspoň tri body v rámci obrysu objektu. Následne je potrebné vybrať príslušné nastavenia vzoru a zobraziť jeho náhľad. Po definovaní vzoru vyberte možnosť „Generovať vzor“ v okne „Generovanie vzoru \ Sledovanie“.

**Druhy mriežkových vzorov dostupných v 2D** :

V 2D sú k dispozícii tieto typy mriežkových vzorov: Mriežka, Mnohouholník, Posun a Užívateľsky definovaný.

  * **Obdĺžniková mriežka [2D]**

Možnosť „obdĺžniková mriežka“ vytvorí mriežku zloženú z kolmých čiar v rámci požadovanej oblasti. Obdĺžnikové vzory sa zvyčajne používajú v prípadoch, keď je dôležitá textúra materiálu. Tento vzor je veľmi podobný smeru vlákien, ktorý by bol viditeľný, keby bol priečny rez dielom vyrytý. Ak je zvolený obdĺžnikový vzor, je potrebné určiť počiatok mriežky, uhol orientácie a rozstup čiar v osiach X a Y.

**Postup pri definovaní mriežkového vzoru:**

  1. Vyberte typ mriežky, ktorú chcete použiť (pozri obr. 26.6.12.1.). Je zvolená obdĺžniková mriežka. Definujte požadovaný počet ohraničujúcich bodov kliknutím na obrobok a potom kliknite na tlačidlo Ďalej. Používateľ môže tiež kliknúť na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) bez definovania ohraničujúcich bodov. Systém bude štandardne považovať ohraničenie obrobku za ohraničujúce body.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image001.jpg' | relative_url }})

Generovanie vzorov v programe Flownet

  1. V tejto fáze je potrebné určiť hustotu mriežky. V prípade mriežky je možné nastaviť počet bodov pre mriežku s pravidelnými rozstupmi. Výberom možnosti „náhľad“ si môžete mriežku prezrieť ešte pred výpočtom všetkých krokov. Po získaní požadovanej mriežky kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (Pozri obr. 26.6.12.2.)

Definíciu mriežky je možné nastaviť pomocou nasledujúcich parametrov:

**Údaje o sieti** :

**Počet mriežok**: používateľ môže nastaviť počet mriežok na osi X, resp. na osi Y.

**Rozstup**: Ide o vzdialenosť (DX a DY) medzi jednotlivými bodmi mriežky v smeroch X a Y.

**Počet sekcií**: používateľ môže určiť počet sekcií, ktoré sa majú zobraziť v 3D pohľade.

**Uhol otočenia**: Táto hodnota určuje uhol, pod ktorým sa mriežka nakreslí, vyjadrený v stupňoch.

**Posun**: Ide o počiatok súradnicovej sústavy.

**Pokročilé nastavenia** :

**Hranica**: Zahrnúť iba hranice mriežky.

**Paralelne s čiarou X**: Na zahrnutie čiar X mriežky.

**Paralelne s líniou Y**: Na zobrazenie línií Y mriežky.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image002.jpg' | relative_url }})

Okno definície mriežky Flownet

  1. V tejto fáze sú k dispozícii pokročilé možnosti, ako napríklad uloženie počiatočného alebo koncového vzoru (pozri obr. 26.6.12.3.). To je užitočné v prípade, ak sa má výstupom stať sieť z inej databázy. Po dokončení kliknite na ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) a letová sieť sa vypočíta. (Pozri obr. 26.6.12.4.) 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image003.jpg' | relative_url }})

Okno s pokročilými nastaveniami programu Flownet

Vzor je možné sledovať spätne tak, že ako počiatočný krok vyberiete neskorší krok v databáze a ako konečný krok vyberiete skorší krok.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image004.jpg' | relative_url }})

Príklad 2D mriežkového siete „flownet“

  * **Vzor mnohouholníka [2D]:**

Vytvorenie polygónového vzoru prebieha tak, ako je znázornené nižšie. Používateľ môže tiež vytvoriť sieť sústredných kruhov na sledovanie toku materiálu pomocou kruhového tvaru. Kruhová mriežka dokáže vytvoriť sústavu kruhov s daným polomerom a vzájomnou vzdialenosťou v rámci požadovanej oblasti. Kruhové vzory sa zvyčajne používajú na monitorovanie smerovej orientácie toku. Ak je zvolený polygónový vzor, používateľ musí určiť počiatok mriežky, priemer, vzdialenosť medzi stredmi polygónov, počet segmentov v polygónoch a či majú byť zahrnuté orezané kruhy.

**Postup pri definovaní vzoru mnohouholníka:**

  1. Vyberte typ mriežky s polygónmi (pozri obr. 26.6.12.5.). Definujte požadovaný počet hraničných bodov kliknutím na obrobok a následným kliknutím na tlačidlo Ďalej. Používateľ môže kliknúť na tlačidlo Ďalej aj bez definovania hraničných bodov. Systém štandardne považuje hranice obrobku za hraničné body.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image005.jpg' | relative_url }})

Definícia oblasti polygónu

  1. V tejto fáze je potrebné určiť hustotu mriežky. V prípade mriežky je možné nastaviť počet bodov pre mriežku s pravidelnými rozstupmi. Výberom možnosti „náhľad“ si môžete mriežku prezrieť ešte pred výpočtom všetkých krokov. Po získaní požadovanej mriežky kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (Pozri obr. 26.6.12.6.)

Definíciu mriežky je možné nastaviť pomocou nasledujúcich parametrov: ****

**Výška príspevku:**

  * **Počet mriežok v smere X**: Výberom tohto prepínača môže používateľ určiť počet mriežok, ktoré sa majú umiestniť v smere X.

  * **Vzdialenosť od stredu k stredu**: Určuje vertikálnu a horizontálnu vzdialenosť medzi jednotlivými stredu susedných mnohouholníkov.

  * **Počet sekcií**: Zobrazuje definovaný počet sekcií, keď si používateľ prezerá model v 3D režime.

**Priemer**: Určuje veľkosť každého mnohouholníka.

**Typ**: Používateľ si môže vybrať požadovaný typ polygónových vzorov (kruh, trojuholník, päťuholník, kosoštvorec, šesťuholník atď.) na vizualizáciu výsledkov.

**Zobraziť orezané**: Zahrňuje všetky čiastočné polygóny, ktoré boli orezané hranicami oblasti. (predvolené nastavenie je „áno“)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image006.jpg' | relative_url }})

Definícia polygónovej mriežky

  1. V tejto fáze sú k dispozícii pokročilé možnosti, ako napríklad uloženie počiatočného alebo koncového vzoru (pozri obr. 26.6.12.3.). To je užitočné v prípade, ak sa má výstupom stať sieť z inej databázy. Po dokončení kliknite na ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) a letová sieť sa vypočíta. (Pozri obr. 26.6.12.7.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image007.jpg' | relative_url }})

Príklad 2D polygónovej siete „flownet“

  * **Vzor posunu [2D]**

Posun nakreslí identickú plochu v určenej vzdialenosti od okraja objektu. Vzor posunu okraja sa zvyčajne používa na zachytenie tendencií k tvorbe prekrývaní. Ak je zvolený posun okraja, je potrebné určiť vzdialenosť, o ktorú sa má okraj posunúť.

**Postup definovania vzoru posunu:**

  1. Zvoľte typ mriežky „Offset“ (pozri obr. 26.6.12.8.). Definujte požadovaný počet hraničných bodov kliknutím na obrobok a následným kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Používateľ môže tiež kliknúť na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) bez definovania hraničných bodov. Systém štandardne považuje hranice obrobku za hraničné body.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image008.jpg' | relative_url }})

2D posun pre 2D úlohu

  1. Krivka posunu sa nastavuje pomocou nasledujúceho parametra.

**Vzdialenosť posunu**: Vzdialenosť posunu je kladná hodnota, ktorá určuje, ako ďaleko dovnútra oblasti by mal byť umiestnený identický okraj.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image009.jpg' | relative_url }})

Definícia hranice pomocou 2D posunu

  1. V tejto fáze sú k dispozícii pokročilé možnosti, ako napríklad uloženie počiatočného alebo koncového vzoru (pozri obr. 26.6.12.3). Toto je užitočné v prípade, ak sa má letová sieť exportovať do inej databázy. Po dokončení kliknite na ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) a letová sieť sa vypočíta. (Pozri obr. 26.6.12.10.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image010.jpg' | relative_url }})

Príklad vzoru 2D posunutej mriežky

**3D Flownet:**

V programe 3D Flownet musí používateľ v grafickom okne definovať hranice 3D oblasti pomocou 2D rovín alebo 2D rovinných hraníc v závislosti od typu siete toku. Tieto hranice musia ležať v rámci obrysu objektu. Následne je potrebné vybrať príslušné nastavenia vzoru a zobraziť jeho náhľad. Po definovaní vzoru stačí v okne „Generovanie vzoru \ Sledovanie“ vybrať možnosť „Generovať vzor“.

**Rôzne typy mriežkových vzorov dostupné v 3D** :

V 3D sú k dispozícii možnosti „Kocka“, „Mriežka“, „Mnohouholník“, „2D posun“, „Posun“, „Sieť povrchov“ a „Definované používateľom“.

  * **Kubický vzor [3D]**

Vytvorenie kubickej mriežky prebieha nasledovne. Najskôr je potrebné vymedziť oblasť mriežky, ako je znázornené na obr. 26.6.12.11. Potom je potrebné definovať mriežku tak, ako je znázornené na obr. 26.6.12.12. A nakoniec sa vygeneruje kubická mriežka tak, ako je znázornené na obr. 26.6.12.13.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image011.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image012.jpg' | relative_url }})

Definícia oblasti pre kubický mriežkový vzor

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image013.jpg' | relative_url }})

Definícia mriežky pre kubický mriežkový vzor

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image014.jpg' | relative_url }})

Príklad vzoru s kubickou mriežkou

  * **Mriežkový vzor [3D]**

  1. Vyberte typ **mriežky**, ktorý sa má použiť (pozri obr. 26.6.12.14.). Možno použiť buď 2D, alebo 3D mriežky. 2D mriežky sú pri rovnakej veľkosti mriežky menej časovo náročné, pretože v dvoch rozmeroch sa vyžaduje menej informácií. V tomto príklade sa vyberie mriežka a klikne sa na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image015.jpg' | relative_url }})

Generovanie vzorov v programe Flownet

  1. V prípade 2D mriežky je potrebné definovať rovinu pomocou rezacej roviny. Spôsob výberu roviny je podobný postupu používanému v dialógovom okne pre rezanie (pozri obr. 26.6.12.15.). Po určení roviny, ktorú chcete použiť, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

  1. V tejto fáze je potrebné určiť hustotu mriežky. V prípade mriežky je možné nastaviť počet bodov pre mriežku s pravidelnými rozstupmi. Výberom možnosti „náhľad“ si môžete mriežku prezrieť ešte pred výpočtom všetkých krokov. Po získaní požadovanej mriežky kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (Pozri obr. 26.6.12.15.)

Definíciu mriežky je možné nastaviť pomocou nasledujúcich parametrov:

Údaje o mriežke:

**Počet mriežok:** používateľ môže nastaviť počet mriežok na osi X, resp. na osi Y.

**Rozstup:** Ide o vzdialenosť (DX a DY) medzi jednotlivými bodmi mriežky v smeroch X a Y.

**Uhol otočenia:** Táto hodnota určuje uhol, pod ktorým sa mriežka nakreslí, vyjadrený v stupňoch.

  * **Posun**: Ide o počiatok súradnicovej sústavy.

**Pokročilé nastavenia:**

  * **Hranica**: Zahrnúť iba body hranice.

  * **Paralelne s čiarou X**: Na zahrnutie čiar X mriežky.

  * **Paralelne s čiarou Y**: Na zahrnutie čiar Y mriežky.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image016.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image017.jpg' | relative_url }})

Generovanie vzorov v programe Flownet

  1. 4\. V tomto momente sú k dispozícii pokročilé možnosti, ako napríklad uloženie počiatočného alebo koncového vzoru (pozri obr. 26.6.12.3.). To je užitočné v prípade, ak sa má výstupná sieť vygenerovať z inej databázy. Po dokončení kliknite na ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) a letová sieť sa vypočíta. (Pozri obr. 26.6.12.16.). 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image018.jpg' | relative_url }})

Príklad mriežky „flownet“ – 3D mriežkový vzor

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image019.jpg' | relative_url }})

Príklad mriežky Flownet – Vytvorenie vertikálnej mriežky

  * **Vzor z mnohouholníkov [3D]**

Vytvorenie vzoru polygónovej mriežky prebieha tak, ako je znázornené nižšie. Najskôr je potrebné vymedziť oblasť mriežky, ako je znázornené na obr. 26.6.12.18, potom je potrebné definovať mriežku, ako je znázornené na obr. 26.6.12.19, a nakoniec sa vygeneruje polygónová mriežka, ako je znázornené na obr. 26.6.12.20\. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image020.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image021.jpg' | relative_url }})

Definícia oblasti polygónu

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image022.jpg' | relative_url }})

Definícia polygónovej mriežky

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image023.jpg' | relative_url }})

Príklad 3D polygónovej siete „flownet“

**Sústredené kruhy**: Príklad znázorňujúci vytvorenie sústredených kruhov v programe Flownet je uvedený na obr. 26.6.12.21.

**Počet kruhov**: v tomto poli môže používateľ zadať počet kruhov.

**Maximálny polomer**: používateľ môže určiť maximálny polomer kruhu.

**Poloha stredu**: používateľ môže vybrať alebo zadať jeden bod na určenie polohy stredu.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image024.jpg' | relative_url }})

Vytvorenie vzoru z leteckých sietí v podobe sústredných kruhov

  * **2D posun [3D]**

Vytvorenie 2D posunutého vzoru prebieha tak, ako je znázornené nižšie. Najskôr je potrebné vymedziť oblasť, ako je znázornené na obr. 26.6.12.22, potom je potrebné definovať ohraničenie, ako je znázornené na obr. 26.6.12.23, a nakoniec sa ohraničenie vygeneruje, ako je znázornené na obr. 26.6.12.24.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image025.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image026.jpg' | relative_url }})

Definícia oblasti 2D posunu pre 3D úlohu

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image027.jpg' | relative_url }})

Definícia ohraničenia 2D posunu pre 3D úlohu

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image028.jpg' | relative_url }})

Vzor 2D posunutých hraníc pre 3D úlohu

  * **Posun [3D]**

Posun nakreslí identickú plochu v určenej vzdialenosti vnútri ohraničenia objektu. Vzor posunutia ohraničenia sa zvyčajne používa na zachytenie tendencií k tvorbe prekrývaní. Ak je zvolené posunutie ohraničenia, je potrebné určiť vzdialenosť, o ktorú sa ohraničenie posunie. Krivka posunutia sa riadi vzdialenosťou posunutia. Vzdialenosť posunu je kladná hodnota, ktorá určuje, ako ďaleko dovnútra oblasti by mal byť umiestnený identický okraj. Na definovanie vzdialenosti posunu možno použiť približnú hodnotu jednej štvrtiny vzdialenosti prekrývania. Vytvorenie vzoru posunu je znázornené nižšie.

Najskôr je potrebné vymedziť oblasť tak, ako je znázornené na obr. 26.6.12.25, potom je potrebné definovať hranice tak, ako je znázornené na obr. 26.6.12.26, a nakoniec sa hranica vygeneruje tak, ako je znázornené na obr. 26.6.12.27.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image029.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image030.jpg' | relative_url }})

Definícia oblasti s posunutými hranicami

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image031.jpg' | relative_url }})

Definícia posunutých hraníc

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image032.jpg' | relative_url }})

Príklad znázorňujúci vzor posunutých hraníc

  * **Vzor mriežky povrchu [3D]**

V tejto možnosti bola sieť povrchu rozdelená na dve možnosti: paralelnú a kruhovú. Výber režimu siete povrchu je znázornený na obr. 26.6.12.28. Vzor definície mriežky pre paralelný a kruhový tvar je znázornený nižšie na obr. 26.6.12.29., obr. 26.6.12.30. a obr. 26.6.12.31. pre príklady lineárneho a kruhového vzoru mriežky.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image033.jpg' | relative_url }})

Okno na výber režimu povrchovej siete

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image036.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image038.jpg' | relative_url }})

Definícia mriežky pre paralelnú a kruhovú sieť

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image037.jpg' | relative_url }})

Príklady vzorov paralelných mriežok pre povrchovú sieť

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image039.jpg' | relative_url }})

Príklady vzoru kruhovej mriežky na povrchu

  * ******Užívateľsky definovaná sieť Fl****ownet [2D, 3D]**

Ak si chcete vytvoriť vlastný počiatočný vzor alebo použiť už skôr vygenerovaný vzor, môžete tak urobiť načítaním súboru s tokovým vzorom. Súbor so vzorom sa skladá zo zoznamu súradníc bodov a zoznamu súborov prepojení. Body sú bodmi priesečníkov v rámci siete. Typ mriežky je určený zoznamom prepojení. Tento zoznam určuje každú krivku samostatne ako počet bodov v sekvenčnom vzore. Ak sú indexy počiatočného a koncového bodu rovnaké, krivka je uzavretá. 

Vzor definovaný používateľom sa musí načítať zo súboru vzorov. Vygenerovaný vzor je možné uložiť do tohto súboru nastavením možnosti uloženia na „yes“. Ak sa vzor ukladá, názov súboru je potrebné zadať do textového poľa „Súbor vzorov“.

Formát údajov o hmotnostných bodoch je nasledovný: 

Numpt

1 X(1) Y(1)

. . .

. . .

Numpt X (Numpt) Y (Numpt)

NumCv

1 CvSz(1) pt(1) pt(CvSz(1))

. . . .

. . . .

NumCv CvSz(NumCv) bod(NumCv) bod(CvSz(NumCv))

Kde

**Numpt** : Počet bodov materiálu 

**Y(i)** : súradnica Y i-teho bodu materiálu

**NumCv** : Počet kriviek

**CvSz(i)** : Počet bodov v i-tej krivke

**pt** : Index bodu krivky (odkazuje na indexy v prvom zozname)

**Príklad**  
Ak vezmeme kruhový výrez zo súboru SPIKE.KEY v adresári DATA a umiestnime naň obdĺžnikovú mriežku 3x3, dostaneme počiatočnú letovú sieť, ktorá pripomína obr. 26.6.12.32. Táto letová sieť je uložená ako súbor zobrazený na obr. 26.6.12.33. Ako je vidieť na obr. 26.6.12.32, najskôr sa uložia body mriežky a v druhej časti sa uloží prepojiteľnosť. Body mriežky sú označené tak, ako je to znázornené na obr. 26.6.12.32, a krivky prepojení sú označené podľa obr. 26.6.12.33.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image040.jpg' | relative_url }})

Výsledok umiestnenia siete typu „flownet“ s rozmermi 3×3 na guľatý predmet; (a) Body sú označené; (b) Krivky sú označené

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image041.jpg' | relative_url }})

Ukážkový súbor vzoru zodpovedajúci uvedenému príkladu. Porovnajte prepojenie bodov s obrázkom vyššie

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image042.jpg' | relative_url }})

Zlúčenie rôznych vzorov siete na lietanie

Používateľ môže tiež vytvárať kombinované (alebo zložité) vzory, ako sú kruhová mriežka, kruhová kocka a podobne. Tento typ kombinovaných mriežkových vzorov je možné získať pomocou možností definovaných používateľom v programe Flownet![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) a je znázornený na obr. 26.6.12.35., obr. 26.6.12.36 a obr. 26.6.12.37.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image043.jpg' | relative_url }})

Ukážka toho, ako vytvoriť kombinovaný mriežkový vzor

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image044.jpg' | relative_url }})

Zobrazuje zložitý vzor siete „flownet“

Kruhový mriežkový vzor na hornej strane obrobku sa vytvorí pomocou možnosti Flownet ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Polygon a vygenerovaná kruhová mriežka je znázornená nižšie na obr. 26.6.12.37.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image045.jpg' | relative_url }})

Kruhový mriežkový vzor na hornej strane obrobku

**Sledovanie potrubia** :

Funkcia sledovania tokových čiar bola vyvinutá na zobrazenie toku kovu v simuláciách ALE v okne Flownet (pozri obr. 26.6.12.38.). Táto možnosť je k dispozícii pre 2D štúdie ALE, 3D simulácie valcovania tvarov ALE a 3D simulácie extrudovania ALE.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image046.jpg' | relative_url }})

Okno sledovania zásielok Flownet

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image047.jpg' | relative_url }})

Možnosti sledovania zásielok v systéme Flownet

Výber hraničných bodov: V prípade 2D objektu je možné vzorkovacie body vybrať ručne pozdĺž hranice objektu obrobku (pozri obr. 26.6.12.40.) alebo môže používateľ použiť počiatočný a koncový bod hrany na ohraničení pomocou možnosti Definovať vzorkovací bod (pozri obr. 26.6.12.41.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image048.jpg' | relative_url }})

Ručne vybrané body pre sledovanie krivky v 2D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image049.jpg' | relative_url }})

Výber bodov pomocou počiatočného a koncového bodu v okne „Výber bodov“ pre 2D

V prípade 3D objektu je možné body odberu vzoriek vybrať ručne z objektu obrobku alebo ich definovať ako pravouhlú mriežku s rôznymi tvarmi, ako sú kruhy, mnohouholníky alebo body na počiatočnej ploche, pomocou možnosti „Definovať body odberu vzoriek“ (pozri obr. 26.6.12.42.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image050.jpg' | relative_url }})

Výber bodov na 3D objekte pomocou rôznych možností výberu

**Tabuľka vybraných bodov**: V tabuľke môžeme vidieť body vybrané na sledovanie priebehu.

**Ovládanie typu zobrazenia**: pomocou tejto možnosti môžeme nastaviť hrúbku čiary Flowline. Hrúbku čiary je možné meniť ťahaním kurzora po posuvníku v rozmedzí od 1 do 100.

**Ovládanie animácie**: Pomocou možnosti „Animate“ môžeme prehrať animáciu toku materiálu a zároveň môžeme regulovať rýchlosť animácie posúvaním kurzora na posuvníku „Animation Speed“ od pomalej po rýchlu.

**Automatická aktualizácia**: Ak je zaškrtnuté políčko „Automatická aktualizácia“, pre každý vybraný krok sa automaticky vygenerujú tokové čiary. Ak je táto funkcia vypnutá, používateľ musí pre každý vybraný krok použiť tlačidlo „Vygenerovať tokové čiary“, aby sa tokové čiary vygenerovali.

**Typ grafu stavovej premennej:** V časti „Stavová premenná“ má používateľ pri kreslení grafu stavovej premennej na výber, či ako os X použije čas alebo vzdialenosť (od začiatku po koniec plochy).

**Vytvoriť prietokovú čiaru**: Po nastavení požadovaných parametrov na vytvorenie prietokovej čiary môže používateľ kliknúť na toto tlačidlo a prietokové čiary sa vytvoria.

**Uloženie bodov do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}): Pomocou tejto možnosti môžeme uložiť body definované pre sledovanie Flowline pre budúce použitie.

**Načítať body zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Pomocou tejto možnosti je možné načítať definované body zo súboru.

**Odstránenie vybraného bodu**: Pomocou tejto možnosti môže používateľ odstrániť nepotrebné body z tabuľky tak, že vyberie príslušný riadok v tabuľke.

**Odstrániť všetky body** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ naraz odstrániť všetky body z tabuľky.

**Zobraziť/skryť body**: Pomocou tejto možnosti môžeme na displeji zobraziť alebo skryť body a čísla bodov pomocou tlačidiel „P“ a „T“.
