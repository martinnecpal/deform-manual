---
lang: sk
title: "26.5. Možnosti následného spracovania"
---

# 26.5. Možnosti následného spracovania

26.5.1. Životné prostredie

26.5.2. Preferencia

26.5.3. Vlastnosti zobrazenia

26.5.4. Nastavenie vlastnosti zobrazenia

26.5.5. Farebná lišta

26.5.6. Prepočet jednotiek

V ponuke „Option Menu“ máme k dispozícii možnosti „Environment“, „Preference“, „Display Properties“, „Set Viewport property“, „Color bar“ a „Unit conversion“, ako je znázornené na obr. 26.5.1.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_5_postprocessing_options_menu/image001.jpg' | relative_url }})

Ponuka možností postprocesora

## **Životné prostredie**

Používateľ môže prispôsobiť pracovné prostredie programu DEFORM pomocou možnosti „Prostredie“. Tu môže používateľ vykonávať zmeny v nastaveniach zobrazenia a grafických nastaveniach a môže si tieto nastavenia uložiť podľa vlastných potrieb. Nastavenia sa uplatnia od nasledujúcej relácie. Ďalšie informácie týkajúce sa prostredia nájdete v kapitole [8\. Pre-Processor Layout](/docs/en/pre_processor/8_pre_processor_layout/8_pre-processor_layout/), v časti [Environment](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#Environment).

## Nastavenia

Poskytuje informácie o zobrazení a typoch objektov v geometriách. V tejto možnosti môže používateľ upraviť zobrazenie objektov v grafickom okne. Ďalšie informácie týkajúce sa prostredia nájdete v kapitole [8\. Pre-Processor Layout](/docs/en/pre_processor/8_pre_processor_layout/8_pre-processor_layout/), v časti [Preference](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#Preferences).

## Vlastnosti zobrazenia ![]({{ '/assets/icons/post_icons/mo_display_properties_icon.jpg' | relative_url }})

Táto voľba umožňuje používateľovi nastaviť zobrazenie informácií o databáze a názvu buď samostatne, alebo v kombinácii s názvom databázy, cestou k databáze, priečinkom databázy, názvom operácie, simuláciou a názvom. Tu môže používateľ nastaviť veľkosť a farbu písma pre názov a informácie o databáze (pozri obr. 26.5.2.).

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_5_postprocessing_options_menu/image002.jpg' | relative_url }})

Vlastnosti zobrazenia

## Nastavenie vlastnosti zobrazenia ![]({{ '/assets/icons/post_icons/mo_set_viewport_properties_icon.jpg' | relative_url }})

**[2D, 3D]** : Používateľ môže pomocou dostupných možností nastaviť zobrazovaciu oblasť všetkých štyroch zobrazení v okne zobrazenia. Tieto možnosti sa uplatnia iba na aktuálne alebo vybrané zobrazenie v okne zobrazenia.

Možnosti pre viacero zobrazení sú k dispozícii v grafických nástrojoch a tiež v ponuke „Multi“ v menu zobrazenia. Ďalšie informácie týkajúce sa viacerých zobrazení nájdete v kapitole XLPHX0, v časti XLPHX1.

**[2D]** : Používateľ môže na karte „Translation“ nastaviť minimálne a maximálne hranice osí X a Y pre všetky štyri zobrazenia kliknutím na roletové menu v hornej časti okna. Po výbere zobrazenia v okne zobrazenia musí používateľ otvoriť dialógové okno vlastností zobrazenia, aby vybral, ktoré zo štyroch nastavení zobrazenia sa má použiť. (Pozri obr. 26.5.3.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_5_postprocessing_options_menu/image003.jpg' | relative_url }})

Okno vlastností posunu zobrazenia

  
**[3D]** : Okrem výberu dvoch smerov obmedzenia zobrazenia na karte „Translation“ môže používateľ na karte „Rotation“ zvoliť tretí smer zobrazenia pomocou osi a uhla otáčania. (Pozri obr. 26.5.4.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_5_postprocessing_options_menu/image004.jpg' | relative_url }})

Okno vlastností „Rotácia zobrazenia“

**Nastavenie kvaternionov** :

**Inicializovať**: Inicializuje definované nastavenie kvaternionu.

**Priradiť**: Používateľ môže priradiť nastavenie kvaternionu výberom osi a zadaním uhla.

**Pridať**: Nastavenie definovaných kvaternionov môže byť priradené k zobrazeniu.

**Kvaterniony**: Poskytujú praktický matematický zápis na vyjadrenie orientácie a rotácie objektov v 3D priestore. Pomocou nastavenia kvaternionov môže používateľ ľahko zadávať zmysluplné kvaterniony.

## Farebná lišta ![]({{ '/assets/icons/post_icons/mo_color_bar_icon.jpg' | relative_url }})

Používateľ môže vytvárať nové farebné pruhy pridávaním, odstraňovaním alebo úpravou farieb. Farbu je možné zmeniť tak, že používateľ vyberie farebný pruh a pomocou tlačidla „Zmeniť farbu“ vyberie novú farbu; po výbere novej farby klikne v okne výberu farieb na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Farebné pruhy je možné posúvať nahor a nadol pomocou tlačidiel. Nové farby je možné pridať pomocou tlačidla a farby je možné odstrániť pomocou tlačidla (pozri obr. 26.5.5.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_5_postprocessing_options_menu/image005.jpg' | relative_url }})

Farebný pruh

## Prepočet jednotiek ![]({{ '/assets/icons/post_icons/mo_unit_conversion_icon.jpg' | relative_url }})

Toto umožňuje používateľovi previesť predvolený systém jednotiek premenných na iný štandardný systém jednotiek alebo na používateľom definovaný prevodný koeficient na účely následného spracovania.

  
K dispozícii sú v podstate tri možnosti: „Predvolené“ (systém jednotiek použitý pri nastavení úlohy), „Z aktuálneho do iného štandardného systému jednotiek“ alebo „Užívateľský“. Dva štandardné systémy jednotiek dostupné v programe Deform sú SI a anglický. (Pozri obr. 26.5.6.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_5_postprocessing_options_menu/image006.jpg' | relative_url }})

Prevádzanie jednotiek

**Súvisiace témy:**

[8\. Pre-Processor Layout](/docs/en/pre_processor/8_pre_processor_layout/8_pre-processor_layout/)

[26.2. Viewports and Windows menu](/docs/en/post_processor/26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor/)
