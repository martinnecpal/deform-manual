---
lang: sk
title: "12.1. Definovanie 2D geometrických údajov"
---

# 12.1. Definovanie 2D geometrických údajov

12.1.1. Pravidlá geometrie pre 2D

12.1.2. Nástroje 2D geometrie

12.1.3. Import a ukladanie 2D geometrických údajov

12.1.4 Nastavenia

Stránka 2D geometrie je znázornená na nasledujúcom obrázku 12.1.1.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image003.jpg' | relative_url }})

2D geometria stránka

## Pravidlá geometrie pre 2D

**Orientácia**
Koncové body úsečiek sú definované číselne. Pri všetkých definíciách výsekov by mali byť všetky objekty očíslované tak, aby sa blok výsekov nachádzal vľavo a voľný priestor (kontaktná zóna) vpravo, keď sa pohybujete po bodoch v poradí. Nedodržanie tejto orientácie môže spôsobiť niektorý z nasledujúcich problémov:

  * Objekt sa nespojí.
  * Sieť sa pri použití okrajových podmienok deformuje.
  * Chyba polohovania objektu pomocou interferenčného polohovania.

**Smerovanie**

Objekty musia byť definované proti smeru hodinových ručičiek (CCW). Smer orientácie možno skontrolovať pomocou tlačidla číslovania bodov v okne na úpravu geometrie.

Ak je aktuálne pripojenie v smere hodinových ručičiek (po nakreslení alebo po importovaní), je možné ho obrátiť. Funkcia obrátenej geometrie obráti aktuálnu konektivitu objektu kliknutím na tlačidlo Obrátiť.

**Hranice**
Počiatočný a koncový bod výseku musí byť mimo kontaktnej zóny, pokiaľ sa body nenachádzajú na osi symetrie. Nástroje, ktoré pretínajú os, by tak mali robiť pod uhlom 90 stupňov: iné uhly môžu viesť k nekonvergencii. V prípade špicatého razidla by sa mala v strede pridať veľmi krátka úsečka.

**Zmiešané filé**

Spojitosť medzi zmiešanými filamentmi je vo formáte IGES zle definovaná. Aby ste sa vyhli problémom, je užitočné definovať veľmi krátke úsečky medzi oblúkmi. Zmiešané filé môžu spôsobiť, že DEFORM-2D bude neustále vydávať hlásenie o nesprávnej geometrii, a to aj po kontrole a oprave geometrie. Ak to chcete opraviť, jednoducho pridajte medzi dva filé extrémne malú úsečku.

**Koncové body**

Polomer prvého a posledného bodu musí byť nulový.

**Výpoveď vyhovuje**

Nástroje s tesnou vôľou by sa mali ťahať tak, aby sa mierne prekrývali. Ak sa nástroje neprekrývajú, môže dôjsť k prekĺznutiu uzlov medzi razníkom a matricou a k problémom pri regenerácii oka. Výsledkom bude chyba "záporný jacobian" v súbore správ.

## Nástroje 2D geometrie

**Definovanie primitív** ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}): Na stránke všeobecnej geometrie je teraz k dispozícii päť primitívnych tvarov, ktoré možno použiť na generovanie geometrie, ako je vidieť na obr. 12.1.2 a obr. 12.1.3. V každom prípade musí používateľ definovaním rozmerov vhodne prispôsobiť mierku problému.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image004.jpg' | relative_url }})

Možnosti 2D osovo symetrických a torzných geoprimitívov

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image005.jpg' | relative_url }})

2D rovinná deformácia a napätie Geo Primitívne možnosti

**Škálovanie geometrie**![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }}) **:** Geometriu možno škálovať v Preprocesore zadaním faktora škálovania. (Pozri obr. 12.1.4.) Faktor škálovania možno vypočítať podľa teplotného rozdielu a údajov o materiáli závislých od teploty a škálovanú geometriu možno uložiť vo formátoch na ukladanie geometrie.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image001.jpg' | relative_url }})

Možnosti škálovania geometrie

**Rozhranie CAD** ![]({{ '/assets/icons/pre_icons/mo_cad_interface_label.jpg' | relative_url }})**:** Pomocou tejto možnosti môže používateľ importovať súbor CAD s geometriou priamo pre Soildworks.

**Konštrukcia odčítaním**![]({{ '/assets/icons/pre_icons/mo_construct_by_substraction_button.jpg' | relative_url }}) **:** Táto možnosť sa používa na vytvorenie geometrie odčítaním geometrie iných už prítomných objektov. Tu je potrebné zadať počiatočný bod, šírku a výšku geometrie objektu, od ktorej sa majú ostatné geometrie odčítať, ako je znázornené na obrázku (pozri obr. 12.1.5).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image006.jpg' | relative_url }})

Konštrukcia pomocou okna Odčítať

**Kontrola geometrie** ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})

Po vytvorení geometrie objektu sa aktivuje tlačidlo Check GEO. Je potrebné skontrolovať orientáciu geometrie. To možno vykonať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})objaví sa vyskakovacie okno, ako je znázornené na nasledujúcom obr. 12.1.6. Geometria sa opraví, keď klikneme na tlačidlo check & correct geometry (Skontrolovať a opraviť geometriu).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image002.jpg' | relative_url }})

Kontrola okna možností geometrie v režime 2D

Nižšie je uvedených niekoľko bežných geometrických chýb v programe DEFORM 2D a spôsob ich opravy v programe DEFORM.

**GEOMETRICKÁ CHYBA** | **ODPORÚČANÁ OPRAVA**
---|---
Duplicitné body | Odstránenie duplicitného bodu
Susedné body sú kolineárne | Odstrániť kolineárny bod (y)
Polomer rohu je taký veľký, že aspoň jeden zo styčných bodov leží mimo dotyčnice definovanej susednými bodmi | Znížte polomer rohu tak, aby oba styčné body ležali v úsečkách dotyčnice
Interferencia oblúkov v susedných bodoch: opačné orientácie oblúkov | Upravte polomery bodov tak, aby spoločný dotykový bod ležal na priamke spájajúcej body
Interferencia oblúkov v susedných bodoch: rovnaká orientácia oblúka | Upravte polomery tak, aby sa spoločný dotykový bod stal priesečníkom dvoch oblúkov premietnutých na spoločnú dotykovú čiaru
Riadková entita s nulovou dĺžkou | Odstrániť entitu
Oblúková entita s nulovým polomerom | Odstrániť entitu
Susediace entity sa pretínajú | Upravte entity tak, aby sa priesečník stal koncovým bodom jednej entity a počiatočným bodom druhej entity
Nespojené susediace entity | Pridanie úsečky na prepojenie entít
  
Nápravné opatrenia, ktoré sa majú prijať pre geometriu DEFORM 2D

**Závady systému:** keď používateľ kontroluje geometriu, ak je nejaká nesprávna orientácia, opraví sa bez ohľadu na to, či ide o uzavretú alebo otvorenú geometriu.

**Zatvorené:** Kontroluje orientáciu geometrie a uzatvára geometriu. Ak používateľ vytvorí otvorenú geometriu, uzavrie ju spojením počiatočných a koncových bodov výberom uzavretej geometrie.

**Otvorená geometria:** Ak používateľ vytvorí otvorenú geometriu, skontroluje sa orientácia a geometria zostane otvorená.

**Odstrániť kolineárne body:** Keď používateľ začiarkne políčko Odstrániť kolineárne body, odstránia sa kolineárne body prítomné v geometrii.

**Reverse**![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }}) : Táto funkcia mení orientáciu geometrie. Orientácia 2D geometrie musí byť v prípade geometrie s jednou slučkou vždy vnútri, v prípade geometrie s viacerými slučkami môže mať slučka, ktorá sa delí o dve oblasti, orientáciu na oboch stranách, ale musí byť definovaná topológia.

**Edit**![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) : Táto funkcia pomáha upravovať hranice 2D objektu. Okno na úpravu geometrie sa používa na vytvorenie, úpravu alebo zobrazenie geometrie daného objektu. Okno sa zobrazí po výbere ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) v okne Geometria. Pozri [Chapter 12.2. 2D Geometry Editing.]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})

**Extraktovať hranicu**![]({{ '/assets/icons/pre_icons/mo_extract_border_button.jpg' | relative_url }}) : Táto funkcia extrahuje geometrické údaje z aktuálnej databázy pre všetky typy objektov okrem tuhého objektu.

**Extract from Mesh**![]({{ '/assets/icons/pre_icons/mo_extract_from_mesh.jpg' | relative_url }}) : Táto funkcia extrahuje geometriu zo siete.

**Zobraziť geometriu vnútri značky** : Začiarknutím tejto možnosti sa zapne zobrazenie orientácie geometrie.

**Odstránenie geometrie :** Pomocou možnosti Odstrániť ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) sa odstráni geometria objektu.

## Načítanie a ukladanie údajov 2D geometrie

**Importovanie geometrie :** Geometriu možno importovať zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo Načítať geometriu z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), z natívneho grafického súboru DEFORM (AMGGEO), zo súboru s kľúčovými slovami, z databázového súboru alebo vytvoriť pomocou editora geometrie. Pri importovaní súborov IGES alebo dxf vyberte pomocou myši objekt, ktorý chcete importovať. Kliknite na ľubovoľnú úsečku v objekte. Všetky segmenty pripojené k tomuto objektu budú tiež vybrané a zvýraznené.

**Vstup vo formáte AMGGEO [2D]**

Formát AMGGEO je interný formát generátora sietí na spracovanie geometrií. Tento formát môže špecifikovať geometriu ako súbor spojovacích bodov, formát XYR, formát oblúkových čiar a ako súbor hraničných uzlov.

Poznámka:

Na výber objektu, ktorý sa má importovať, je potrebné použiť myš, aj keď je v súbore výkresu len jeden objekt.

**Priradenie názvu súboru k názvu objektu pri načítaní geometrie** : Keď používateľ začiarkne túto možnosť pri načítaní alebo importovaní súboru geometrie, priradí názov súboru geometrie k názvu objektu.

**Uloženie geometrie :** Uloží geometriu do súboru ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) alebo do knižnice ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). Ukladá geometriu vo formátoch IGES, DXF a DEFORM natívneho formátu GEO pre 2D.

## Nastavenia ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }})

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_1_2d_geometry_data_defining/12_1_image007.jpg' | relative_url }})

Okno nastavení 2D geometrie

**Tolerancia:** Tu sa nastavuje úroveň tolerancie pre spojenie dvoch hraničných bodov, ktoré sú blízko seba pri importe objektu vo formátoch geometrie IGS a DXF a pred prenosom údajov do programu DEFORM. ( Obr. 12.1.7.)

**Počet bodov diskretizácie:**

[12\. Geometry Modelling]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/' | relative_url }})

[12.2. 2D Geometry data Editing]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})

[12.3. 3D Geometry data Defining]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/' | relative_url }})

[12.4. 3D Geometry data Editing (GEO TOOL)]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_Editing_geo_toolL/' | relative_url }})
