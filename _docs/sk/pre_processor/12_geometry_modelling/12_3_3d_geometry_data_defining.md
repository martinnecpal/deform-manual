---
lang: sk
title: "12.3. Definovanie údajov 3D geometrie"
---

# 12.3. Definícia údajov 3D geometrie

12.3.1. Pravidlá geometrie pre 3D

12.3.2. Nástroje 3D geometrie

12.3.3. Import a ukladanie 2D geometrických údajov

12.3.4. Nastavenia

Okno 3D geometria sa používa na definovanie geometrie objektu, ako je znázornené na obr. 12.3.1. V aktívnom režime budú iba polia Definovať primitívum, CAD rozhranie, Upraviť a Predtvarovať, ostatné možnosti budú v sivej farbe, keď nie je definovaná žiadna geometria. Po vytvorení geometrie sa aktivujú všetky možnosti.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image001.jpg' | relative_url }})

Okno 3D geometrie

## Pravidlá geometrie pre 3D

Pri definovaní povrchov objektov v programe DEFORM je potrebné dodržiavať niekoľko konvencií.

**Orientácia normál povrchu****Normály :** ****In DEFORM normály povrchu uzavretých geometrií by mali smerovať von z geometrie. Takto DEFORM definuje vonkajšiu stranu objektu. V prípade povrchu, ktorý nie je uzavretý, by normály povrchu mali smerovať k deformovateľným objektom a treba dávať veľký pozor na to, aby žiadny uzol nevidel zadnú stranu objektu. V prípade, že sa na obmedzenie obrobku používa tuhá rovina, odporúča sa, aby bola rovina dostatočne veľká, aby uzly nevideli okolo roviny. V okne Geometry (Geometria) možno smer normál povrchu zobraziť kliknutím na tlačidlo Normály povrchu v ľavej dolnej časti obrazovky. Nedodržanie tejto konvencie môže spôsobiť niektorý z nasledujúcich problémov:

  * Objekt nebude [mesh]({{ '/docs/sk/pre_processor/13_Mesh_Generation/13_Mesh_Generation/' | relative_url }})
  * Sieť sa skreslí, keď sa použije[ boundary conditions]({{ '/docs/sk/pre_processor/14_Boundary_Conditions/14_boundary_conditions/' | relative_url }})
  * Chyba [Object positioning]({{ '/docs/sk/pre_processor/19_Object_Positioning/19_Object_Positioning/' | relative_url }}) pri použití interferenčného polohovania

**Povrchové škvrny :** V programe DEFORM je povrchová škvrna definovaná časťou povrchu, ktorá je oddelená od ostatných častí toho istého povrchu ohybom povrchu o 30 stupňov alebo viac. Napríklad kocka bude mať šesť povrchových políčok, pretože hrany medzi jednotlivými stranami majú 90-stupňový ohyb povrchu. Na zobrazenie povrchových políčok v programe DEFORM môže používateľ kliknúť na tlačidlo povrchových políčok v okne geometrie v ľavej dolnej časti obrazovky. Každý ohyb povrchu väčší ako 30 stupňov sa zobrazí ako hrubá červená čiara. Výhodou tejto funkcie je, že záhyby na povrchu sa zobrazia ako červené plôšky v strede geometrie. To poskytuje metódu na zistenie, kde sa môžu vyskytovať záhyby.

**Výber z hraníc** : Extrakcia hraníc je proces identifikácie geometrie povrchu deformovanej časti z povrchu siete konečných prvkov. Geometrické uvažovanie sa používa na identifikáciu kritických prvkov, ako sú hrany, rohy a roviny symetrie, ktoré by sa mali zachovať počas remeshingu.  
Extrakcia hraníc môže zlyhať z týchto dôvodov:

  * **Zložené alebo prekrížené prvky** [3D]

Ak sa v procese vytvorí uzavretý tvárniaci okraj, geometria povrchu bude zle definovaná. Ak sa použije príliš veľký časový krok bez [polygon length sub stepping](../9_Simulation_Controls/9_2_Defining_Step.htm#Polygon_length_sub_step_\(DPLEN\)), plochy prvkov sa môžu skrížiť, čo tiež spôsobí zle definovaný povrch. Oba tieto prípady sa dajú často identifikovať pomocou zobrazenia povrchových políčok v okne geometrie. ak vzniká legitímny tvarovací okraj, proces by sa mal prepracovať tak, aby sa okraj odstránil. Ak sa preliačina nachádza v oblasti, kde je prijateľná, môže byť potrebné použiť systém CAD na úpravu geometrie, potom znovu zosieťovať diel a interpolovať údaje. ak sa plochy prvkov krížia, je vo všeobecnosti potrebné vrátiť sa k poslednému dobrému kroku v databáze. Tejto situácii možno predísť použitím menšieho časového kroku, použitím [polygon length sub stepping](../9_Simulation_Controls/9_2_Defining_Step.htm#Polygon_length_sub_step_\(DPLEN\)), použitím menších prvkov v tesných rohoch a vynúteným remeshovaním na pevnom kroku alebo intervale zdvihu (podľa kritérií remeshovania).

**Rovnobežné roviny symetrie** : Pri použití symetrie by používateľ nemal zadávať paralelné okrajové podmienky pevnej rýchlosti. (komplexnú diskusiu o rovinách symetrie nájdete v dokumente [Appendix VIII]({{ '/docs/sk/Appendices/Appendix_VIII_Preventing_leakage_of_nodes/' | relative_url }}) o používaní rovín symetrie v 3D) V prípade, že sú potrebné dve paralelné roviny symetrie, používateľ môže zadať jednu pevnú okrajovú podmienku rýchlosti a jednu pevnú rovinu bez trenia a nerozdeliteľnú kontaktnú podmienku (informácie o tom, ako to realizovať, nájdete v dokumente [Appendix VIII]({{ '/docs/sk/Appendices/Appendix_VIII_Preventing_leakage_of_nodes/' | relative_url }}) o používaní rovín symetrie v 3D). Ak sú dve pevné okrajové podmienky rýchlosti nastavené rovnobežne vedľa seba, extrakcia hraníc určite zlyhá, čo spôsobí, že akékoľvek remeselnícke spracovanie zlyhá.

Ak rovina symetrie nie je dostatočne veľká, aby pokryla celú oblasť, v ktorej je potrebné definovať symetriu, je možné, že uzly sa môžu pohybovať okolo roviny symetrie, čo tiež spôsobí zlyhanie extrakcie hraníc. Keďže tuhé roviny, keď sa používajú na definovanie rovín symetrie, nemusia mať vzťah k žiadnym iným objektom ako k obrobku, môžu byť ľubovoľne veľké. Z dôvodov zobrazenia sa používateľovi neodporúča, aby rigidné roviny boli neprimerane veľké.

## Nástroje 3D geometrie

**Define Primitive** ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) : Máme tri rôzne typy geometrických primitív, ako sú Box, Cylinder a Hollow Cylinder, ako je znázornené na obr. 12.3.2. Extrude a Revolve možno použiť na prevod 2D prierezu na 3D.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image002.jpg' | relative_url }})

Primitívne okno geometrie

**Rozhranie CAD** ![]({{ '/assets/icons/pre_icons/mo_cad_interface_label.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ priamo importovať súbor geometrie CAD pre Soildworks.

**Vykonajte**![]({{ '/assets/icons/pre_icons/mo_preform_label.jpg' | relative_url }}) :

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image020.jpg' | relative_url }})

3D okno preformy

**Upraviť**![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) : Pomocou možnosti Upraviť môžeme upraviť existujúcu geometriu v sprievodcovi 3D GEO TOOL. Pozrite si kapitolu [12.4. 3D Geometry Editing.]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_Editing_geo_toolL/' | relative_url }})

**Extraktovať hranicu** ![]({{ '/assets/icons/pre_icons/mo_extract_border_button.jpg' | relative_url }}) : Táto funkcia extrahuje údaje o geometrii z aktuálneho sieťovaného objektu databázy pre všetky typy objektov okrem tuhého objektu.

**Extraktovanie z mriežky** ![]({{ '/assets/icons/pre_icons/mo_extract_from_mesh.jpg' | relative_url }}) : Táto funkcia extrahuje geometriu z 3D siete objektu.

**Kontrola**![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) : Vždy skontrolujte geometriu. DEFORM má kontrolný algoritmus, ktorý kontroluje počet neplatných hrán, neplatnú orientáciu, polygóny s malou plochou a počet povrchov. Každý typ chyby nie je možné odhaliť.

Použitím tejto možnosti Kontrola geometrie sa otvorí okno Výsledky kontroly geometrie, v ktorom sa zobrazí súhrn geometrie objektu (pozri obr. 12.3.4.). Pre objekt, ktorý má uzavretý objem, by mal existovať 1 povrch, 0 voľných hrán a 0 neplatných entít (ako je zakrúžkované nižšie na obr. 12.3.4.). Objekty, ktoré sú importované ako povrchy a nie telesá, budú mať voľné hrany, ale stále by mali mať len 1 povrch.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image004.jpg' | relative_url }})

Výsledky kontroly geometrie

**GEOMETRICKÁ CHYBA** | **ODPORÚČANÁ OPRAVA**
---|---
Poly s nesprávnou orientáciou | Buď opravte súbor STL v balíku na modelovanie telies alebo vyhľadajte problematický poly v Preprocesore a súbor STL opravte ručne.  
Poly s malou plochou | Mierne zvýšte toleranciu chyby
Poly s neplatnou hranou | Oprava geometrie v balíku na modelovanie telies
  
Nápravné opatrenia, ktoré sa majú prijať pre geometriu DEFORM 3D

  
Poznámka: Správna orientácia normál povrchu sa pri kontrole geometrie NEKONTROLUJE, ak všetky normály smerujú rovnakým smerom.

**Oprava**![]({{ '/assets/icons/pre_icons/mo_fix_label.jpg' | relative_url }}) : Táto funkcia rieši geometrické problémy, pri ktorých existuje buď viacero povrchov, alebo otvorené oblasti (diery), a to odstránením všetkých ďalších povrchov a vyplnením dier. V prípade menších alebo lokalizovaných problémov to funguje dobre. V prípade problematickejších súborov, ako je tento, nemusí oprava priniesť želaný výsledok (pozri obr. 12.3.5).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image005.jpg' | relative_url }})

Upevňovacia geometria kľukového hriadeľa

**Škála**![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }}) :Geometriu možno pri tvárnení zmenšiť, aby sa prispôsobila tepelnej rozťažnosti, zadaním faktora mierky. (Pozri obr. 12.3.6.) Faktor škálovania možno vypočítať na základe teplotného rozdielu a údajov o materiáli závislých od teploty. Škálovanú geometriu možno uložiť do rôznych formátov na ukladanie geometrie.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image001.jpg' | relative_url }})

Okno Geometria mierky

**Reverzný**![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }}) : Táto funkcia obráti povrch/normálu geometrie. Povrch/normál geometrie by mal byť vždy smerom von.

**Vyhľadanie osi** ![]({{ '/assets/icons/pre_icons/mo_find_axis_label.jpg' | relative_url }}) : Táto funkcia automaticky určí os geometrie na základe definície geometrie a zobrazí ju.

**Nastavenie siete Brick** ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) : Na definovanie siete Brick musí používateľ definovať počiatočný povrch a koncový povrch pre vytvorenú geometriu, ako je znázornené na obr. 12.3.7. Brick mesh sa používa pre geometrie s pravidelným alebo rovnakým prierezom.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image007.jpg' | relative_url }})

Nastavenie okna Brick Mesh pre vytláčanie

Tehlovú sieť možno vytvoriť výberom možností Extrude alebo Revolve na základe geometrie. Ak používateľ vyberie prepínač Extrude (Vytlačiť), tehlová sieť sa vytlačí vzhľadom na počiatočný a koncový bod, ako je znázornené na obr. 12.3.8.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image008.jpg' | relative_url }})

Tehlová sieť z vytlačeného objektu

Ak používateľ vyberie prepínač Revolve, sieť tehál sa bude otáčať v smere Z, ako je znázornené na obr. 12.3.9 a obr. 12.3.1.10.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image009.jpg' | relative_url }})

Nastavenie okna z tehlovej siete pre otáčanie

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image010.jpg' | relative_url }})

Tehlová sieť otáčajúceho sa objektu

**Roviny symetrie** ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}): Možno definovať rovinnú aj rotačnú symetriu. V prípade rovinnej symetrie bude mať simulácia dodatočné informácie, ktoré jej umožnia zabrániť tomu, aby sa okolo nej materiál blysol. V prípade rotačnej symetrie sieťovanie automaticky umiestni na plochy správne okrajové podmienky. To je myslené ako jednotné miesto na uplatnenie okrajových podmienok symetrie pre všetky objekty.

  * **Určenie rovinnej symetrie** : Ak chcete zadať rovinnú symetriu, vyberte rovinu symetrie na geometrii a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Podmienka rovinnej symetrie sa pridá do zoznamu aktuálne zadaných symetrií. (Pozri obr. 12.3.11.) Keď je definovaná rovina symetrie, počas generovania siete sa zobrazí vyskakovacie okno so správou, ako je znázornené na obr. 12.3.12., s požiadavkou, či sa má vytvoriť predvolená okrajová podmienka, používateľ môže vybrať možnosť "No" (Nie), ak nechce použiť predvolenú BCC pridelenú systémom na základe definovaných podmienok symetrie.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image011.jpg' | relative_url }})

Priradenie symetrických plôch

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image012.jpg' | relative_url }})

Predvolené okná Okrajové podmienky

Poznámka: Správa Symmetry Popup sa zobrazí len vtedy, keď nastavíme problém v režime Expert.

  * **Určenie rotačnej symetrie** : Ak chcete špecifikovať rotačnú symetriu, zadajte bod a vektor osi otáčania, ako aj dostupný stupeň symetrie, ako je znázornené na obr. 12.3.13. Potom kliknite na počiatočnú rovinu a koncovú rovinu geometrie v smere otáčania, aby sa uplatnila rotačná symetria. Podmienka symetrie sa pridá do zoznamu aktuálne zadaných symetrií. Ďalšie informácie o možnosti rotačnej symetrie nájdete v časti [16.7. ]({{ '/docs/sk/pre_processor/16_Object_Properties/16_7_symmetry_properties/' | relative_url }})[Rotational Symmetry]({{ '/docs/sk/pre_processor/16_Object_Properties/16_7_symmetry_properties/' | relative_url }}).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image013.jpg' | relative_url }})

Okno rotačnej symetrie

**Examine**![]({{ '/assets/icons/pre_icons/mo_examine_label.jpg' | relative_url }}) : Táto funkcia pomáha preskúmať body a polygóny 3D geometrie. Súradnice geometrického bodu možno upravovať aj pomocou polí súradníc bodov a tlačidla použiť po zmene týchto súradníc. Aktuálny výber zobrazenia bodov a polygónov je zvýraznený tvarmi gule alebo kocky pomocou zaškrtávacích polí v spodnej časti okna (pozri obr. 12.3.14).

V programe DEFORM V12 môžeme pomocou ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) ("Detekcia zón") vedľa možnosti Pole povrchu vypočítať počet zón existujúcich v geometrii a každej zóne môžeme priradiť iný materiál alebo ID vrstvy pomocou možnosti Priradenie. Táto možnosť pomáha používateľovi modelovať viacvrstvové kompozity, dutiny, inklúzie,aditívnu výrobu,...atď.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image006.jpg' | relative_url }})

Nastavenia geometrie okna Examine

**Konverzia z 2D do 3D** ![]({{ '/assets/icons/pre_icons/mo_2d_to_3d_conversion.jpg' | relative_url }}) : Používateľ môže definovať geometriu 2D prierezu, ktorú možno použiť na generovanie 3D geometrie začiarknutím políčka Use Cross Section (Použiť prierez).

**Define Primitive** ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) : Máme tri rôzne typy geometrických primitív, ako sú Bar, Cylinder a Hollow Cylinder, ako je znázornené na obr. 12.3.15. Toto okno geometrie sa zobrazí pre rovinný typ geometrie deformačného typu.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image005.jpg' | relative_url }})

Primitívne okno 2D geometrie pre rovinnú deformáciu a rovinné napätie

Okno geometrie sa zobrazí pre osovo súmerný typ geometrie, ako je znázornené na obr. 12.3.16.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image004.jpg' | relative_url }})

Primitívne okno 2D geometrie pre osovú symetriu a torziu

**Kontrola**![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) : Po vytvorení geometrie objektu sa aktivuje tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Je potrebné skontrolovať orientáciu geometrie. To možno vykonať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) Zobrazí sa vyskakovacie okno, ako je znázornené na nasledujúcom obr. 12.3.17. Geometria sa opraví, ak sú v nej nejaké chyby, keď klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Správa "Geometry is legal" (Geometria je legálna) sa zobrazí, keď je geometria opravená alebo nemá žiadne chyby, a potom klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Ďalšie informácie nájdete v časti [Check Geometry](12_1_2d_geometry_data_defining.htm#Check_Geometry)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image014.jpg' | relative_url }})

Vyskakovacie okno Kontrola geometrie

**Edit**![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) : Možnosť úpravy geometrie sa používa na vytvorenie geometrie pre objekt alebo na úpravu existujúcej geometrie. Importovanú geometriu možno upraviť v okne Edit Geometry (Úprava geometrie).

Ďalšie informácie o 2D geometrii úprav nájdete v časti [12.2. 2D Geometry Data Editing]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})

**Zobraziť geometriu vnútri značky** : Začiarknutím tejto možnosti sa zapne zobrazenie orientácie geometrie.

**Nastavenia**![]({{ '/assets/icons/pre_icons/mo_settings..._button.jpg' | relative_url }}) : Po vytvorení 2D geometrie pomocou týchto nastavení môže používateľ vytvoriť 3D geometriu z 2D geometrie.

**Extrude** : Používateľ môže importovať 2d prierez alebo použiť definovaný 2D prierez geometrie a vytlačiť ho v požadovanom smere. Toto je možné vykonať aj počas importu súborov 2d prierezov z DB alebo kľúčového súboru (pozri obr. 12.3.18).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image015.jpg' | relative_url }})

Nastavenia okna 2d prierezu pre vytláčanie

**Revolve** : Používateľ môže importovať 2d prierez geometrie a na základe symetrie ho otočiť, aby získal 3d prierez. (Pozri obr. 12.3.19.)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image016.jpg' | relative_url }})

Nastavenia okna 2D prierezu pre Revolving

**Generovať 3D** ![]({{ '/assets/icons/pre_icons/mo_generate_3d_button.jpg' | relative_url }}): Kliknutím na toto tlačidlo alebo na stránke Nastavenia na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d__label.jpg' | relative_url }}) možno vytvorenú 2D geometriu extrudovať alebo otočiť na 3D geometriu.

**Zobraziť normálové vektory geometrie** : Táto funkcia zobrazuje normálové vektory povrchu geometrie. Ak je geometria uzavretý objem, správna orientácia je definovaná vtedy, keď normály povrchu smerujú von z objektu. Ak geometria nie je uzavretý objem, ale je to len povrch, správna orientácia je definovaná, keď normály smerujú k obrobku (pozri obr. 12.3.20).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image017.jpg' | relative_url }})

Zobraziť normálové vektory geometrie

**Transparentný** : Zaškrtnutím tohto políčka sa zapne priehľadnosť objektu. (Pozri obr. 12.3.21.)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image018.jpg' | relative_url }})

Možnosť priehľadného zaškrtávacieho políčka

**Odstrániť geometriu**![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) : Odstráni vytvorenú geometriu.

## Import a ukladanie údajov 3D geometrie

**Import geometrie :** Geometriu možno importovať zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo Načítať geometriu z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), z natívneho grafického súboru DEFORM (AMGGEO), zo súboru s kľúčovými slovami, z databázového súboru alebo vytvoriť pomocou editora geometrie. Pri importovaní súborov STL alebo súborov PATRAN vyberte pomocou myši objekt, ktorý chcete importovať. Kliknite na ľubovoľnú úsečku v objekte. Všetky segmenty pripojené k tomuto objektu budú tiež vybrané a zvýraznené.

Geometrické formáty :

  * Vstup formátu STL (DIEGEO)
  * Vstup formátu AMGGEO
  * Vstupný formát PATRAN
  * Vstupný formát IDEAS
  * Vstupný formát NASTRAN
  * 2D vstup vo formáte IGES

**Vstup formátu STL (DIEGEO)**

Formát STL ([DIEGEO]({{ '/docs/sk/Keyword_Documentation/D/DIEGEO/' | relative_url }})) reprezentuje povrch sériou trojstranných faziet. Tento formát možno vytvoriť takmer vo všetkých komerčných balíkoch na modelovanie telies z modelu telesa alebo z modelu povrchu. V prípade veľmi jednoduchých tvarov, ako je napríklad kocka, sa môže použiť len veľmi málo faziet, ktoré poskytujú vynikajúcu reprezentáciu tvaru. V prípade lisovacej formy, kde sa fazety používajú na modelovanie zakriveného povrchu, môže byť potrebných veľa faziet, aby sa objektu poskytla hladká reprezentácia alebo aby sa vykreslili malé detaily geometrie. Odporúča sa šetriť počtom faziet použitých na reprezentáciu geometrie, aby sa minimalizovala veľkosť databázového súboru. Keď sa použije viac faziet, veľkosť každého kroku v databázovom súbore sa zvýši. Nárast času na výpočet kontaktov je zanedbateľný s nárastom počtu faziet v geometriách matríc.

Po vložení súboru STL do nástroja Pre-processor sa používateľovi okamžite zobrazí výzva na zadanie hodnoty tolerancie chyby. Táto hodnota predstavuje vzdialenosť prichytenia medzi bodmi v súbore STL. Keďže fazety nie sú na sebe závislé, body, ktoré majú susedné fazety spoločné, nemusia byť v súbore STL reprezentované presne rovnakým spôsobom. Keďže mali byť tým istým bodom, preprocesor predpokladá určitú toleranciu chyby, pri ktorej sú body zlúčené do reprezentácie toho istého bodu. Predvolená hodnota 1e-005 je zvyčajne dobrá východisková hodnota. Ak sú v geometrii matrice malé trhliny, môžu sa uzavrieť zvýšením hodnoty tolerancie chyby a dúfaním, že sa trhliny uzavrú. Toto nie je veľmi kontrolovaný spôsob, ktorým sa dajú uzavrieť akékoľvek trhliny, a mal by sa používať s mimoriadnou opatrnosťou. Po použití tejto metódy by sa mala geometria starostlivo skontrolovať, aby sa zabezpečilo, že sa do nej nedostanú žiadne diery alebo sa nestratia dôležité prvky.

Formát súborov STL môže byť ASCII alebo binárny formát. DEFORM dokáže čítať aj zapisovať ASCII aj binárne verzie STL súborov. Všetky fazety sú definované nezávisle od seba, takže hrozí nebezpečenstvo, že sa vyskytnú záhyby, diery, prekrývajúce sa fazety alebo neplatná orientácia faziet. Po načítaní súboru STL sa dôrazne odporúča skontrolovať geometriu, aby ste sa uistili, že sa v nej nenachádzajú žiadne záhyby, diery alebo iné problémy. Ak sa v deformujúcom sa telese vyskytnú problémy s geometriou, pri vytváraní siete objektu sa môžu vyskytnúť problémy. Ak sú problémy s geometriou v tuhej matrici, môžu sa vyskytnúť problémy počas simulácie, keď sa uzly zachytia a vážne narušia integritu deformujúceho sa telesa. To môže byť veľmi problematické, pretože problémy v geometrii výlisku sa môžu objaviť až v priebehu simulácie. Spôsob, ako najlepšie určiť, či je geometria výlisku dobre definovaná alebo nie, je pokúsiť sa na ňu aplikovať sieť. Ak je možné na geometrii vygenerovať sieť, potom ide o dobre definovanú geometriu, ak však sieťovanie zlyhá, je možné, že je problém s definíciou geometrie.

**Vstup vo formáte AMGGEO**

Formát AMGGEO je interný formát DEFORM na spracovanie geometrie. Tento formát môže špecifikovať povrch ako súbor spojovacích trojuholníkov alebo štvoruholníkov. Ak sa používajú štvoruholníky, degenerované prvky (t. j. trojuholníky) nie sú povolené. Normály políčka musia byť mimo prvku. To znamená, že body by mali byť číslované proti smeru hodinových ručičiek pri pohľade zvonku objektu. Súbor je možné vytvoriť a upraviť pomocou textového editora, ako je vi, emacs alebo Notepad.

Formát súboru je
POČET VRCHOLOVÝCH BODOV

1 X1 Y1 Z1

2 X2 Y2 Z2

...... N

XN YN ZN

POČET

POVRCHOVÉ ZÁPLATY

1 prvé prepojenie záplat 1 2 3 (1/4)

2 Druhé prepojenie záplat 1 2 3 (1/4)

......

N N-tá spojitosť záplat 1 2 3 (1/4)

kde (1/4) v spojitosti znamená, že bod 1 sa opakuje na 4. pozícii v trojuholníkovom políčku. Pri štvoruholníkovej záplate sa používajú všetky 4 body.

Štvorcová škvrna s rozmermi 1'' x 1'' v rovine xy s normálou smerujúcou pozdĺž osi z by bola definovaná takto:

4

1 0. 0. 0.

2 1. 0. 0.

3 1. 1. 0.

4 0. 1. 0.

1

1 1 2 3 4

Štvorec by sa definoval pomocou dvoch trojuholníkov takto:

4

1 0. 0. 0.

2 1. 0. 0.

3 1. 1. 0.

4 0. 1. 0.

2

1 1 2 3 1

2 1 3 4 1

  
**Vstupný formát PATRAN [3D]**

Neutrálny formát súboru PATRAN je výstupný formát systému PATRAN. Tento formát špecifikuje buď povrchovú sieť, alebo sieť telesa, ktorá sa môže použiť na reprezentáciu geometrie. Po načítaní neutrálneho súboru PATRAN sa používateľovi najprv zobrazí výzva, či je neutrálny súbor buď povrchová sieť, alebo plná sieť. Po tom, ako používateľ poskytne informáciu o tom, či je súbor povrchová alebo plná sieť, je vyzvaný, aby zadal konverzný faktor. Ide len o škálovaciu premennú a používateľovi sa odporúča použiť len predvolenú hodnotu 1.

DEFORM®-3D importuje geometrické súbory vo formátoch .PDA a .PAT 3d.

**Vstup formátu IDEAS [3D]**

Neutrálny formát súboru IDEAS je výstupný formát systému IDEAS. Tento formát špecifikuje povrchovú sieť, ktorá sa môže použiť buď na reprezentáciu geometrie v programe DEFORM, alebo ako základ pre pevnú sieť. Po načítaní univerzálneho súboru IDEAS sa používateľ najprv vyzve, aby zadal konverzný faktor. Ide len o škálovaciu premennú a používateľovi sa odporúča použiť len predvolenú hodnotu 1.

**Vstup vo formáte NASTRAN [3D]**

****DEFORM- 3D importuje formát 3D geometrie NAS. Pri importe je možné škálovanie vykonať pomocou faktora škálovania v záložke Možnosti gemetrie.

**2D Vstup vo formáte IGES [3D]**
3D geometriu možno vytvoriť aj extrudovaním 2D súboru geometrie IGS pomocou možnosti Import Geometry zadaním dĺžky a smeru extrudovania. Na obr. 12.3.22. je zobrazené okno s nastaveniami extrudovania 2d IGES geometrie, ktoré sa zobrazí počas importu geometrie pomocou možnosti Import geometrie.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image003.jpg' | relative_url }})

Okno Extrude Direction and Length pre 2D import IGES v 3D režime

**Priradenie názvu súboru k názvu objektu pri načítaní geometrie :** Keď používateľ zaškrtne túto možnosť pri načítaní alebo importovaní súboru geometrie, priradí názov súboru geometrie k názvu objektu.

**Uložiť geometriu** : Uloží geometriu do súboru ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) alebo do knižnice ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). Geometriu môžeme uložiť vo formátoch STL, PATRAN, UNV a DEFORM natívneho formátu GEO pre 3D.

## Nastavenia ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }})

**2D Import** :

**Tolerancia:** Tu sa definuje úroveň tolerancie pre spojenie dvoch hraničných bodov, ktoré sú blízko seba pri importe objektu vo formátoch geometrie IGS a DXF, pred prenosom údajov do programu DEFORM. (Pozri obr. 12.3.23.)

**Počet bodov diskretizácie:**

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_3_3d_geometry_data_definition/12_3_image019.jpg' | relative_url }})

Okno nastavení tolerancie 3D geometrie

**3D import** :

**Tolerancia:** tu sa definuje úroveň pre spojenie dvoch hraničných bodov, ktoré sú blízko seba pri importe objektu z formátov geometrie STL a pred prenosom údajov do DEFORM. (Pozri obr. 12.3.23.)

**Faktor škálovania:** Pri načítaní importovanej geometrie sa nastaví mierka 3D geometrie. Požadovaný faktor mierky musí byť zadaný pred importom geometrie, aby sa importovaná geometria zmenšila. V predvolenom nastavení bude hodnota 1 znamenať žiadne škálovanie, pre 0,5 sa škáluje na polovicu pôvodnej geometrie a pre 2 sa zdvojnásobí pôvodná geometria. (Pozri obr. 12.3.23.)

Súvisiace témy:

[12\. Geometry Modelling]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/' | relative_url }})

[12.1. 2D Geometry data Defining]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/' | relative_url }})

[12.2. 2D Geometry data Editing]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})

[12.4. 3D Geometry data Editing (GEO TOOL)]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_Editing_geo_toolL/' | relative_url }})

[13\. Mesh Generation]({{ '/docs/sk/pre_processor/13_Mesh_Generation/13_Mesh_Generation/' | relative_url }})
