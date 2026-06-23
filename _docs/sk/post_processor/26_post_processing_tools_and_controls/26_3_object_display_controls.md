---
lang: sk
title: "26.3. Ovládacie prvky na zobrazenie objektov"
---

# 26.3. Ovládacie prvky na zobrazenie objektov

26.3.1. Ponuka zobrazenia

26.3.2. Ponuka myši

V časti „Okno zobrazenia objektu“ sa budeme venovať možnostiam v ponukách „Zobrazenie“ a „Myš“. 

## Ponuka zobrazenia

Na obr. 26.3.1 sú zobrazené možnosti ponuky zobrazenia. Pomocou týchto možností alebo ikon na paneli nástrojov môže používateľ vybrať rôzne typy vykresľovania objektov, ako napríklad tieňovanie, drôtený model, kombináciu tieňovania a drôteného modelu, charakteristickú čiaru (plochu) a pridať charakteristickú čiaru k akémukoľvek inému typu vykresľovania. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image017.jpg' | relative_url }})

Zobraziť možnosti ponuky

  * **Stínovanie (F6)** ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) : Plynulo stínuje objekty v zobrazení.

  * **Wireframe (F7)** ![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}) : Zobrazí sieť objektu v okne zobrazenia.

  * **Tienenie a drôtený model (F8)** ![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}) : Plynulo tieňuje a zobrazuje sieť objektov v okne zobrazenia.

  * **Línia prvku alebo plocha** ![]({{ '/assets/icons/pre_icons/mo_feature_line_mode_icon.jpg' | relative_url }}) : Zobrazuje okraje povrchu objektu. V 3D režime použite uhol prvku na zmenu zobrazenia plôch.

  * **Pridať riadok vlastnosti** ![]({{ '/assets/icons/pre_icons/mo_add_feature_line_icon.jpg' | relative_url }}): Táto vlastnosť kombinuje hrany povrchu s ďalšími možnosťami režimov zobrazenia. V 3D režime použite vlastnosť „uhol“ na zmenu zobrazenia plôch povrchu. 

## Ponuka myši

Na obr. 26.3.2 sú zobrazené možnosti ponuky „Myš“. Pomocou týchto možností alebo ikon na paneli nástrojov môže používateľ vybrať rôzne režimy myši na meranie lineárnej vzdialenosti objektov a na zmenu alebo posun pohľadu na objekty v grafickom okne, napríklad posúvanie, otáčanie (len v 3D), priblíženie a zväčšenie.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image018.jpg' | relative_url }})

Možnosti ponuky myši

  * **Meranie**![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}): Tento nástroj umožňuje používateľovi zmerať ľubovoľnú vzdialenosť medzi dvoma bodmi postupným kliknutím na oba body. Meranie je možné vykresliť buď v smere X, Y alebo XY; v 3D sa do obrazu dostane aj smer Z, a to pomocou dostupnej možnosti štýlu CAD, ktorá zobrazuje namerané hodnoty vo vybranom smere. Pre prístup k možnosti štýlu CAD musí používateľ v režime merania kliknúť pravým tlačidlom myši v zobrazovacom okne (pozri obr. 26.3.3.). Meracie značky sa nevymažú, kým sa zobrazenie neobnoví, a preto sú vhodné aj na označenie ľubovoľných referenčných bodov na obrazovke, ktoré si zachovajú svoju polohu aj pri zmenách zobrazenia.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image019.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image020.jpg' | relative_url }})

  
(a) (b)

Možnosti štýlu merania pomocou pravého tlačidla myši; (a) pre 3D, (b) pre 2D

  * **Select![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) : **Tlačidlo „Select“ slúži ako všeobecný nástroj na označovanie. Plní viacero funkcií, ktoré sa menia v závislosti od kontextu. Môže sa použiť na výber uzla alebo prvku, na výber BCC, na zastavenie kontrolných bodov na objektoch a na mnohé podobné funkcie. Z kontextového menu, ktoré sa otvorí po kliknutí pravým tlačidlom myši v grafickom okne, môže používateľ zmeniť zobrazenie vybraných uzlov na bod alebo mnohouholník, ako je znázornené na obr. 26.3.4.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image021.jpg' | relative_url }})

Zobrazenie možnosti pravého tlačidla myši pre vybraný uzol v grafickom okne

  * **Posun (Shift+ĽMB)** ![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) : Funkcia „Posun“ upravuje oblasť vyplňujúcu aktívne zobrazenie bez zmeny veľkosti zobrazeného objektu.

  * **Otočiť (Ctrl+ĽMB)** ![]({{ '/assets/icons/pre_icons/mo_rotate_icon.jpg' | relative_url }}) : Táto funkcia umožňuje pomocou kurzora myši otočiť geometrie v požadovanom smere. To isté je možné dosiahnuť aj tak, že podržíte kláves Ctrl, kliknete ľavým tlačidlom myši v aktívnom zobrazení a otočením kolieska myši dopredu alebo dozadu otočíte objekty.

  * **Otočiť okolo osi X** ![]({{ '/assets/icons/pre_icons/mo_rotate_x_icon.jpg' | relative_url }}) : Táto funkcia umožní kurzoru myši otočiť objekt v smere osi X.

  * **Otočiť okolo osi Y** ![]({{ '/assets/icons/pre_icons/mo_rotate_y_icon.jpg' | relative_url }}) : Táto funkcia umožní kurzoru myši otáčať objekt v smere osi Y.

  * **Otočiť okolo osi Z** ![]({{ '/assets/icons/pre_icons/mo_rotate_z_icon.jpg' | relative_url }}) : Táto funkcia umožňuje kurzoru myši otáčať objekt v smere osi Z. Táto možnosť nie je k dispozícii pre 2D systémy. Hoci sa táto ikona zobrazuje aj pri nastavovaní 2D úlohy, ak na ňu používateľ klikne, zobrazí sa upozornenie „Táto funkcia nie je k dispozícii v 2D zobrazení“.

  * **Dynamické priblíženie (Alt+ĽMB)** ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) : Dynamické priblíženie dynamicky mení veľkosť oblasti objektu, ktorá vyplňuje aktívne zobrazenie. Veľkosť zobrazenia je možné zmeniť tak, že podržíte kláves Alt, kliknete ľavým tlačidlom myši v aktívnom okne zobrazenia a otočením kolieska myši dopredu alebo dozadu zväčšíte alebo zmenšíte veľkosť objektu v okne zobrazenia.

  * **Zväčšenie rámčekom (Ctrl+Alt+ĽMB)**![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) : Funkcia zväčšenia rámčekom umožňuje podrobné preskúmanie malej oblasti aktuálne zobrazeného objektu alebo grafu. Oblasť zväčšenia sa vyberie podržaním klávesov Ctrl + Alt a kliknutím ľavým tlačidlom myši, pričom ťahaním myši ohraničíte vybranú oblasť zobrazeným rámčekom. Po uvoľnení tlačidla myši sa vybraná oblasť vyplní celé zobrazené okno. 

**Súvisiace témy:**

[26\. Post Processor Features](/docs/en/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/)

[26.2. Viewport and Windows menu](/docs/en/post_processor/26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor/)
