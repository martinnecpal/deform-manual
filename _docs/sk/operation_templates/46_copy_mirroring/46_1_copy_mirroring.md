---
lang: sk
title: "46.1. Zrkadlenie kópií"
---

# 46.1. Kopírovanie/zrkadlenie

46.1.1. Ako pridať operáciu kopírovania/zrkadlenia

46.1.2. Pridanie operácie kopírovania/zrkadlenia

46.1.3. Stránka „Objekty“

46.1.4. Stránka objektu

46.1.5. Stránka parametrov zrkadlenia

46.1.5.1. Pre režim hromadného spracovania

46.1.5.2. Zrkadlenie/kopírovanie v interaktívnom režime

46.1.6. Vytvorenie databázy

46.1.7. Pokračovať v ďalšej operácii

46.1.8. Výsledky následného spracovania pri operácii kopírovania/zrkadlenia

## Ako pridať operáciu kopírovania/zrkadlenia

Operácia kopírovania/zrkadlenia sa pridá ako nasledujúca operácia k operácii obsahujúcej symetrické modely v rámci viacerých operácií, aby sa symetrický objekt zrkadlil pozdĺž symetrickej roviny. Operáciu kopírovania/zrkadlenia je možné pridať aj ako prvú operáciu a importovať symetrické objekty, aby sa pokračovalo v nastavení viacerých operácií. Operácia Kopírovanie/Zrkadlenie je v tejto príručke vysvetlená na príklade súboru Spike_ForgingBlow1.key, ktorý obsahuje nastavenie symetrie. Tento súbor kľúčových slov obsahuje nastavenie 90-stupňovej symetrie, ktoré sa skopíruje na vytvorenie 180-stupňového modelu.

Pred pridaním operácie kopírovania/zrkadlenia musíme nastaviť operáciu tvárnenia pomocou súboru Sipke_ForgingBlow1.Key, preto otvoríme sprievodcu MO v jednotkách SI > pridáme 3D operáciu tvárnenia > naimportujeme súbor Sipke_ForgingBlow1.Key, ako je znázornené na obr. 46.1.1. > Pokračujte až po vygenerovanie databázy a spustite simuláciu.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0001.jpg' | relative_url }})

Import súboru 3D Spike Key

## Pridanie operácie kopírovania/zrkadlenia

Po spustení prvej simulácie operácie tvarovania môžeme pridať operáciu Kopírovanie/Zrkadlenie zo skupiny operátorov Simulácia v prehliadači, ako je znázornené na obrázku [Fig. 46.1.2.](46_1_copy_mirroring.htm#Fig_46_1_2_Adding_Copy/Mirroring_Operation). Po kliknutí na operáciu Kopírovanie/Zrkadlenie sa zobrazí vyskakovacie okno „Typ nastavenia“, ako je znázornené na obr. 46.1.3.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0002.jpg' | relative_url }})

Pridanie operácie kopírovania/zrkadlenia

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0003.jpg' | relative_url }})

Typ nastavenia: Vyskakovacie okno

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0004.jpg' | relative_url }})

Operácia kopírovania/zrkadlenia v dávkovom režime

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0005.jpg' | relative_url }})

Operácia kopírovania/zrkadlenia v interaktívnom režime

## Stránka „Objekty“

Objekty môžeme pridávať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a ak chceme nejaký objekt odstrániť, musíme vybrať príslušný objekt a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}), ako je znázornené na obr. 46.1.6. Môžeme zachovať objekty, ktoré sa majú zrkadliť, a ostatné objekty odstrániť; používateľ môže tiež pridávať nové objekty a importovať údaje z iných súborov kľúčových slov, databáz alebo geometrických súborov.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0006.jpg' | relative_url }})

Stránka objektov

## Stránka objektu

Ak je používateľ v nastavení dávkového režimu, všetky objekty budú mať typ „Načítanie z databázy“, s výnimkou novo pridaných objektov. Ak je nastavený typ „Interaktívny“, používateľ môže typ objektu zmeniť. (Pozri obr. 46.1.7.)

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0007.jpg' | relative_url }})

Stránka objektu obrobku

## Stránka parametrov zrkadlenia

### Pre režim hromadného spracovania 

Používateľ môže pridať zrkadlenie výberom možnosti ![]({{ '/assets/icons/pre_icons/mo_add_mirroring_radio_option.jpg' | relative_url }}) na karte „Režim úprav“ v časti „Parametre zrkadlenia“ a ak chceme pridané zrkadlenie odstrániť, musíme vybrať možnosť ![]({{ '/assets/icons/pre_icons/mo_delete_mirroring_radio_option.jpg' | relative_url }}) na karte „Režim úprav“ v časti „Parametre zrkadlenia“. Používateľ môže tiež definovať hodnotu tolerancie pre zrkadlený objekt, ako je znázornené na obr. 46.1.8. Údaje o zrkadlovej rovine sa aktualizujú počas generovania databázy.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0008.jpg' | relative_url }})

Stránka parametrov zrkadlenia (pre dávkový režim)

### Zrkadlenie/kopírovanie v interaktívnom režime 

Používateľ môže pridať zrkadlenie výberom možnosti ![]({{ '/assets/icons/pre_icons/mo_add_mirroring_radio_option.jpg' | relative_url }}) na karte „Režim úpravy“ v okne „Parametre zrkadlenia“ a ak chceme pridané zrkadlenie odstrániť, musíme vybrať možnosť ![]({{ '/assets/icons/pre_icons/mo_delete_mirroring_radio_option.jpg' | relative_url }}) na karte „Režim úpravy“ v okne „Parametre zrkadlenia“. Používateľ môže tiež definovať hodnotu tolerancie pre zrkadlený objekt. Po výbere požadovaného režimu úprav a definovaní hodnoty tolerancie musí používateľ kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_merge_button.jpg' | relative_url }}) na vytvorenie objektu, pozri obr. 46.1.9., ktorý zobrazuje zrkadlený objekt.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0009.jpg' | relative_url }})

Stránka parametrov zrkadlenia (pre interaktívny režim)

## Vytvoriť databázu

Ak je simulácia prvej operácie dokončená, počas vytvárania kópie/zrkadlenia databázy sa zrkadlené objekty automaticky aktualizujú, ako je znázornené na obr. 46.1.10. V prípade, že predchádzajúca operácia nebola simulovaná, zobrazí sa náhľad s objektmi bez výsledkov simulácie.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0010.jpg' | relative_url }})

Vytváranie databázy

## Pokračovať v ďalšej operácii

Po dokončení nastavenia kopírovania/zrkadlenia môžeme pridať operáciu 3D tvarovania z Průzkumníka, ako je znázornené na obr. 46.1.11.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0011.jpg' | relative_url }})

Pridanie operácie 3D tvarovania po operácii kopírovania/zrkadlenia

  
Teraz môžeme po zrkadlení objektov, ako je znázornené v [Fig. 46.1.12.](46_1_copy_mirroring.htm#Fig_46_1_12_3D_Forming_Operation_after_Copy/Mirroring_Operation_Batch_Mode) a na obr. 46.1.13, definovať údaje o nastavení druhej formovacej operácie.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0012.jpg' | relative_url }})

3D tvarovacia operácia po operácii kopírovania/zrkadlenia (dávkový režim)

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0013.jpg' | relative_url }})

3D tvarovanie po operácii kopírovania/zrkadlenia (interaktívny režim)

## Výsledky následného spracovania pri operácii kopírovania/zrkadlenia

V okne MO Post môže používateľ skontrolovať operáciu kopírovania/zrkadlenia. Výber kroku operácie kopírovania/zrkadlenia načíta príslušný krok so zrkadlovým objektom. Bude obsahovať iba jeden negatívny krok, v ktorom je k dispozícii zrkadlený model, ako je znázornené na obr. 46.1.14.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0014.jpg' | relative_url }})

Režim zverejňovania operácií kopírovania/zrkadlenia
