---
lang: sk
title: "50.1. 3D Geo Tool"
---

# 50.1.3 Nástroj pre 3D geometriu

50.1.1. Rozloženie nástrojov geometrie

50.1.2. Výkladná skriňa

50.1.3. Strom objektov

50.1.3.1. Počet objektov

50.1.3.2. Viditeľnosť

50.1.3.3. Farba objektu

50.1.3.4. Transparentnosť

50.1.4. Grafické nástroje

50.1.4.1. Ponuka „Súbor“

50.1.4.2. Ponuka „Upraviť“

50.1.4.3. Ponuka nástrojov

50.1.4.4. Ponuka „Vybrať“

50.1.4.5. Ponuka zobrazenia

50.1.4.6. Zobrazovacia oblasť

50.1.4.7. Ponuka „Okno“

50.1.4.8. Ponuka možností

50.1.4.9. Ponuka Pomocník

50.1.5. Editor vlastností

50.1.5.1. Analýza

50.1.5.2. Meranie

50.1.5.3. Krájanie

50.1.5.4. Upraviť

50.1.5.5. Overiť

50.1.5.6. Morfing

## Rozloženie geometrických nástrojov

Rozloženie nástrojov geometrie je rozdelené na okno zobrazenia, strom objektov, okno grafických nástrojov a editor projektu. (Pozri obr. 50.1.1.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0001.jpg' | relative_url }})

Rozloženie 3D Geo nástroja

## Výkladná skriňa

Okno zobrazenia slúži na grafické zobrazenie všetkých importovaných alebo vytvorených geometrií. V okne zobrazenia môžeme sledovať geometriu v reálnom čase, ako sa v nej prejavujú vykonané zmeny.

## Strom objektov

V strome objektov môžeme vidieť importované alebo vytvorené objekty a informácie o ich zobrazení, ako napríklad počet objektov, stav zobrazenia, farbu objektov a informácie o priehľadnosti, ktoré sú k dispozícii v tomto okne.

### Počet objektov

Počet importovaných alebo vytvorených objektov (geometrie) je možné vidieť v stromovej štruktúre objektov, kde budú uvedené v zozname.

###  Viditeľnosť

Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) môže používateľ zapnúť alebo vypnúť zobrazenie objektov v okne zobrazenia.

### Farba objektu

Pomocou tejto možnosti môže používateľ zmeniť farbu objektu. Ak používateľ klikne na políčko pod možnosťou „Farba objektu“ pre vybraný objekt, otvorí sa dialógové okno s paletou farieb, v ktorom si môže vybrať farbu, ktorá sa má použiť pre vybraný objekt.

### Transparentnosť

Pomocou tejto možnosti môže používateľ zapnúť alebo vypnúť priehľadnosť vybraného objektu. Ak používateľ klikne na túto možnosť, príslušný objekt sa stane priehľadným.

## Grafické nástroje

Okno grafických nástrojov ponúka funkcie na manipuláciu s pohľadom a ďalšie pomocné funkcie na ovládanie zobrazenia objektov v okne Zobrazenie. Medzi funkcie patrí priblíženie a posun, ako aj otočenie. Okno grafických nástrojov obsahuje aj možnosti na paneli nástrojov na vytváranie geometrie a jej úpravy, ako sú Geometrický primitív, Posun, Otáčanie, Zmenšenie/zväčšenie, Zrkadlenie, Posun, Vytiahnutie, Plynulý posun a Boolovské operácie, ako aj možnosti výberu, ako sú Výber plášťa, Výber plochy, „Vybrať mnohouholník“, „Vybrať mnohouholníky pomocou obdĺžnika“, „Vybrať mnohouholníky pomocou valca“, „Vybrať mnohouholníky pomocou okna“, „Vybrať mnohouholníky pomocou čiary“, „Vybrať slučku“, „Vybrať krivku“, „Vybrať rezovú rovinu“, „Vybrať bod“ a „Výber Inventu“.

### Ponuka „Súbor“

Na nižšie uvedenom obr. 50.1.2 sú zobrazené možnosti ponuky Súbor,

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0002.jpg' | relative_url }})

Možnosti ponuky Súbor

  * **Nová relácia ![]({{ '/assets/icons/pre_icons/geo_tool_new_session.jpg' | relative_url }})**: Otvorí novú reláciu na vytváranie a úpravu geometrií v nástroji pre 3D geometriu.

  * **Open![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) **: Otvára 3D geometriu v rôznych formátoch, ako sú *.STL, *.GEO, *.PDA, *.UNV, *.KEY a *.PBR.

  * **Save![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) **: Uloží geometriu aktuálnej relácie do súboru *.STL.

  * **Uložiť ako**: Funkcia „Uložiť ako“ uloží geometriu v aktuálnej relácii do vybraného formátu spomedzi dostupných formátov do vybranej cesty.

  * **Uložiť všetko:** Možnosť „Uložiť všetko“ slúži na uloženie všetkých geometrií jedným kliknutím.

  * **Import:** Pomocou tejto možnosti môže používateľ importovať geometrie vo formátoch *.IGS a *.STP.

  * **Export**: Exportujte geometriu v aktuálnej relácii do formátu *.IGS alebo *.STP.

  * **Ukončiť reláciu**: Možnosť „Ukončiť reláciu“ slúži na ukončenie aktuálne otvorenej relácie, neukončuje však aplikáciu 3D Geo Tool.

  * **Ukončiť**: Táto voľba slúži na zatvorenie sprievodcu nástrojom 3D Geo Tool.

### Ponuka „Upraviť“

  * **Vrátiť späť**: Táto voľba slúži na vrátenie poslednej akcie späť.

  * **Zopakovať:** Táto možnosť slúži na zopakovanie akcie, ktorá bola zrušená pomocou funkcie „vrátiť späť“.

### Ponuka nástrojov

  * **Geometrické primitívy ![]({{ '/assets/icons/pre_icons/geo_tool_geometry_primitive.jpg' | relative_url }}): **Po kliknutí na možnosť „Geometrické primitívy“ sa otvorí okno „Primitívy“ s možnosťami na vytvorenie novej geometrie. (Pozri obr. 50.1.3.) Ďalšie informácie o možnostiach Geometrický primitív nájdete v časti [12.3.2. 3D Geometry Tool](../../pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining.htm#12.3.2._3D_Geometry_Tools) – [Define Primitive.](../../pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining.htm#Define_Primitive)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0003.jpg' | relative_url }})

Okno geometrických primitív

  * **Posunúť objekt ![]({{ '/assets/icons/pre_icons/geo_tool_translate_icon.jpg' | relative_url }}) **: Možnosť „Posunúť objekt“ slúži na posunutie objektov o zadanú vzdialenosť v smeroch X, Y a Z. Ak po výbere objektu klikneme na túto možnosť, zobrazí sa vyskakovacie okno, v ktorom môžeme zadať hodnotu vzdialenosti v príslušnom smere, o ktorú sa má objekt v danom smere posunúť. (Pozri obr. 50.1.4.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0004.jpg' | relative_url }})

Dialógové okno „Preložiť objekt“

  * **Otočiť objekt ![]({{ '/assets/icons/pre_icons/geo_tool_rotate_icon.jpg' | relative_url }}) :** Táto voľba slúži na otočenie objektu v zadanom smere o zadaný uhol. Keď klikneme na túto možnosť po výbere objektu, zobrazí sa vyskakovacie okno, v ktorom môžeme určiť smer a uhol. Následne po kliknutí na tlačidlo „Použiť“ sa objekty otočia v zadanom smere. (Pozri obr. 50.1.5.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0005.jpg' | relative_url }})

Dialógové okno „Otočiť“

  * **Zmenšiť objekt** ![]({{ '/assets/icons/pre_icons/geo_tool_scale_icon.jpg' | relative_url }}): Táto voľba slúži na zmenšenie geometrie. Geometriu je možné zmenšiť v nástroji Geo zadaním mierky zmenšenia. Pri hodnote 0,5 sa geometria zmenší na polovicu pôvodnej veľkosti a pri hodnote 2 sa zväčší na dvojnásobok pôvodnej veľkosti. (Pozri obr. 50.1.6.) Toto zmenšovanie alebo zväčšovanie je možné obmedziť na určitý smer. V dialógovom okne Zmenšovanie/zväčšovanie môže používateľ zrušiť zaškrtnutie smeru, v ktorom sa zmenšovanie alebo zväčšovanie nevyžaduje.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0006.jpg' | relative_url }})

Dialógové okno „Mierka objektov“

  * **Zrkadlenie objektu ![]({{ '/assets/icons/pre_icons/geo_tool_mirror_icon.jpg' | relative_url }}): **Táto voľba zrkadlí objekty pozdĺž zadaných osí a pôvodné objekty nezachová. (Pozri obr. 50.1.7.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0007.jpg' | relative_url }})

Dialógové okno „Zrkadlové objekty“

  * **Offset![]({{ '/assets/icons/pre_icons/geo_tool_offset_icon.jpg' | relative_url }}) :** Táto voľba slúži na posunutie plochy o zadanú dĺžku. Posunutie plochy je možné vykonať nasledujúcimi krokmi:

  * Vyberte možnosť „Offset“ (otvorí sa dialógové okno „Offset“),

  * Zadajte dĺžku posunu alebo cieľový objem.

  * Zapnite možnosť „Zachovať pôvodný diel“, ak má byť upravená geometria vytvorená ako nový diel; geometria pôvodného dielu zostane nezmenená.

  * Vyberte plochu, ktorú chcete posunúť, kliknutím na ňu (plochu sa zvýrazní)

  * Kliknite na ![]({{ '/assets/icons/pre_icons/apply_button.jpg' | relative_url }}). Vybraná plocha sa posunie o zadanú dĺžku alebo na cieľový objem. (Pozri obr. 50.1.8.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0008.jpg' | relative_url }})

Vyrovnanie povrchu

  * **Extrude![]({{ '/assets/icons/pre_icons/geo_tool_extrude_icon.jpg' | relative_url }}) : **Táto voľba slúži na vytiahnutie plochy na zadanú dĺžku. Vytiahnutie plochy je možné vykonať nasledujúcimi krokmi:

  * Vyberte možnosť „Extrude“ (otvorí sa dialógové okno „Extrude“),

  * Zadajte dĺžku extrudovania alebo cieľový objem.

  * Zapnite možnosť „Zachovať pôvodný diel“, ak má byť upravená geometria vytvorená ako nový diel; geometria pôvodného dielu zostane nezmenená.

  * Vyberte plochu, ktorú chcete vytiahnuť, kliknutím na ňu (plochu sa zvýrazní)

  * Nastavte smer alebo vyberte možnosť „auto“, aby systém automaticky určil smer na základe zvolenej plochy.

  * Kliknite na ![]({{ '/assets/icons/pre_icons/apply_button.jpg' | relative_url }}). Vybraná plocha sa vytiahne na zadanú dĺžku alebo na cieľový objem. (Pozri obr. 50.1.9.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0009.jpg' | relative_url }})

Extrudovanie povrchu

  * **Jemné posunutie** ![]({{ '/assets/icons/pre_icons/geo_tool_soft_move_icon.jpg' | relative_url }}): Táto voľba slúži na úpravu profilu povrchu. Jemné posunutie povrchu je možné vykonať nasledujúcimi krokmi:

  * Zvoľte možnosť „Soft move“ (otvorí sa dialógové okno „Soft move“),

  * Vyberte plochu, ktorej profil sa má upraviť, kliknutím na túto plochu (pridá sa valec; upravte valec tak, aby ste vybrali požadovanú plochu)

  * Vyberte spôsob úpravy profilu: „Okolo bodu“ alebo „Pozdĺž krivky“

  * Potiahnite šípku na okienku valca, aby ste určili tvar profilu. (Pozri obr. 50.1.10.)

  * Tvar krivky profilu je možné nastaviť pomocou posuvného prúžku.

  * Kliknite na ![]({{ '/assets/icons/pre_icons/apply_button.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/ok_button.jpg' | relative_url }}). Vybraná plocha sa plynulo posunie na zadanú dĺžku. (Pozri obr. 50.1.11.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0010.jpg' | relative_url }})

Vytvorenie tvaru profilu pre plynulý pohyb

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0011.jpg' | relative_url }})

Jemné pohybovanie po povrchu

  * **Sprievodca boolovskými operáciami** ![]({{ '/assets/icons/pre_icons/geo_tool_boolean_icon.jpg' | relative_url }}): Sprievodca boolovskými operáciami poskytuje používateľovi pokyny týkajúce sa nastavení, ktoré je potrebné použiť pri vykonávaní boolovských operácií, ako je odčítanie nežiaducej oblasti z geometrie pomocou inej geometrie alebo zjednotenie dvoch geometrií. Dá sa použiť na vytvorenie obrobku ALE.

**Krok 1: Začnite**

Úvodná stránka slúži na spustenie boolovských operácií. (Pozri obr. 50.1.12.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0012.jpg' | relative_url }})

Úvodná stránka sprievodcu Booleovými operáciami

**Krok 2: Úprava objektov**

Na stránke „Úprava objektov“ môžeme objekty umiestniť pomocou posunutia, aby sme sa vyhli povrchu „Overwrap“. (Pozri obr. 50.1.13.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0013.jpg' | relative_url }})

Sprievodca booleovskými hodnotami – Úprava stránky

**Krok 3: Booleovská zjednotenie**

Po úprave objektov môže používateľ zlúčiť dve geometrie do jednej výberom možnosti „Union“ na karte „Modify“. (Pozri obr. 50.1.14.) Pozri tiež 50.1.5.2.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0014.jpg' | relative_url }})

Stránka „Boolean Wizard Union“

**Krok 4: Vytvorenie geometrie**

Na stránke „Vytvorenie geometrie“ môže používateľ vytvoriť novú geometriu valca zadaním hodnôt do polí Priemer, Výška a Poloha. (Pozri obr. 50.1.15.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0015.jpg' | relative_url }})

Stránka „Vytvorenie geometrie“ v sprievodcovi Boolean

**Krok 5: Booleovské odčítanie**

Na stránke „Slice“ môže používateľ rozrezať predtým vyčistenú geometriu na požadovanom mieste v požadovanom smere. Týmto rozrezaním vznikne z rozrezaného objektu nová geometria; používateľ má možnosť zachovať pôvodnú geometriu (pozri obr. 50.1.16.). Pozrite si tiež časť „Boolean“ v bode 50.1.5.2. Meranie

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0016.jpg' | relative_url }})

Sprievodca boolovskými operáciami – Stránka „Odčítanie“

**Krok 6: Upratovanie**

Na stránke „Clean up“ môže používateľ opraviť predtým zlúčenú alebo odpočítanú geometriu odstránením neplatných plášťov/mnohouholníkov, a to pomocou možností na karte „Analysis“. (Pozri obr. 50.1.17.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0017.jpg' | relative_url }})

Stránka „Vyčistenie“ v sprievodcovi Boolean

**Krok 7: Krájanie**

Na stránke „Slice“ môže používateľ rozrezať predtým vyčistenú geometriu na požadovaný tvar a vzdialenosť v definovanom smere. Týmto rozrezaním sa celá geometria rozdelí na dve samostatné geometrie. (Pozri obr. 50.1.18.) Ďalšie informácie o rozrezávaní nájdete v časti 50.1.5.3. Rozrezávanie

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0018.jpg' | relative_url }})

Stránka „Boolean Wizard Slice“

**Krok 8: Extrudovanie**

Na stránke „Extrúzia“ môže používateľ extrudovať požadovanú plochu na definovanú dĺžku a v definovanom smere. Tým sa plocha predĺži na definovanú dĺžku. (Pozri obr. 50.1.19.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0019.jpg' | relative_url }})

Stránka „Extrudovať“ v sprievodcovi Boolean

**Krok 9: Dokončenie**

Po vytvorení konečného geometrického tvaru môže používateľ geometriu uložiť kliknutím na tlačidlo „Dokončiť“ na stránke „Dokončiť“. (Pozri obr. 50.1.20.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0020.jpg' | relative_url }})

Stránka „Dokončenie“ sprievodcu Booleovými výrazmi

### Vyberte ponuku

  * **Vybrať plášť**![]({{ '/assets/icons/pre_icons/geo_tool_pick_shell.jpg' | relative_url }}): Táto voľba slúži na výber celého plášťa geometrie na účely úpravy.

  * **Vybrať plochu**![]({{ '/assets/icons/pre_icons/geo_tool_pick_face.jpg' | relative_url }}) : Táto voľba slúži na výber geometrickej plochy na úpravu.

  * **Výber mnohouholníka** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygon.jpg' | relative_url }}): Táto voľba slúži na výber mnohouholníka na úpravy.

  * **Výber polygónov pomocou obdĺžnika**![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygons_by_box.jpg' | relative_url }}) : Táto voľba slúži na výber polygónov pomocou obdĺžnikového okna. Zmenou dĺžky a šírky obdĺžnika sa vyberú na úpravu tie polygóny, ktoré sa úplne nachádzajú v tomto obdĺžniku.

  * **Výber polygónov pomocou valca ![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygos_by_cylinder.jpg' | relative_url }}): **Táto voľba slúži na výber polygónov pomocou valcového okna. Zmenou priemeru a výšky valca sa vyberú na úpravu tie polygóny, ktoré sa nachádzajú úplne vo vnútri valca.

  * **Výber polygónov pomocou okna**![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygons_by_window.jpg' | relative_url }}) : Táto voľba slúži na výber polygónov pomocou okna, ktoré sa nakreslí cez polygóny.

  * **Výber mnohouholníkov pomocou čiary** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygons_by_line.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ nakresliť čiaru cez mnohouholníky, ktoré sa majú vybrať na úpravu.

  * **Výber slučky** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_loop.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ vybrať otvorenú slučku, ktorú chce vyplniť.

  * **Výber krivky** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_curve_by_line.jpg' | relative_url }}): Táto voľba slúži na výber kriviek v geometrii.

  * **Výber roviny rezu** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_slicing_curve.jpg' | relative_url }}): Táto voľba slúži na výber definovanej roviny rezu.

  * **Pick Point** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_point.jpg' | relative_url }}): Funkcia „Pick Point“ slúži na výber bodov na geometrii.

  * **Obrátiť výber** ![]({{ '/assets/icons/pre_icons/geo_tool_invert_selection.jpg' | relative_url }}): Táto voľba slúži na prepínanie výberu medzi vybranými a nevybranými oblasťami geometrie.

### Ponuka zobrazenia

V okne „Display“ sú k dispozícii možnosti na zmenu režimu zobrazenia geometrie. Pozri obr. 50.1.21.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0021.jpg' | relative_url }})

Zobraziť možnosti ponuky

  * **Zobraziť body ![]({{ '/assets/icons/pre_icons/geo_tool_display_points.jpg' | relative_url }})**: Zobrazí geometrické body v okne Zobrazenie.

  * **Stínovanie zobrazenia** ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}): Plynulo stínuje geometriu v rámci zobrazenia.

  * **Zobraziť drôtený model** ![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}): Zobrazí línie polygónov geometrie v okne zobrazenia.

  * **Zobrazenie tieňovania a drôteného modelu** ![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}): Plynulo tieňuje a zobrazuje geometriu spolu s líniami polygónov v okne zobrazenia.

  * **Zobraziť hrany** ![]({{ '/assets/icons/pre_icons/geo_tool_display_edge_icon.jpg' | relative_url }}): Zobrazí povrchové hrany geometrie.

  * **+Hrany**![]({{ '/assets/icons/pre_icons/geo_tool_plus_surface patch_icon.jpg' | relative_url }}) : Táto funkcia zobrazí hrany povrchu spolu s ďalšími možnosťami režimov zobrazenia.

### Zobrazenie

Obr. 50.1.22. Ukazuje možnosti ponuky „Viewport“. Pomocou tejto možnosti môže používateľ umiestniť geometriu tak, aby bola lepšie viditeľná.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0022.jpg' | relative_url }})

Ponuka zobrazenia

  * **Obnoviť obrazovku**: Možnosť „Obnoviť obrazovku“ vygeneruje novú obrazovku a odstráni všetky meracie značky.

  * **Prispôsobiť zobrazenie**: Prispôsobí všetky zobrazené geometrie tak, aby sa zmestili do aktuálneho zobrazenia.

  * **Predchádzajúci pohľad**: Vráti objekty do polohy, v akej boli zobrazené predtým.

  * **Viacnásobné****zobrazenia**: Používateľ môže využiť viacnásobné zobrazenia na súčasnú vizualizáciu geometrie z rôznych uhlov pohľadu.

  * **Synchronizácia viacerých****zobrazení**: Ak zvolíme možnosť „Synchronizácia viacerých zobrazení“, dôjde k synchronizácii oboch okien; ak zmeníme vlastnosti v jednom zobrazení, táto zmena sa premietne aj do ostatných zobrazení.

  * **Vybrať**: Tlačidlo „Vybrať“ slúži na všeobecné označovanie bodov. Plní viacero funkcií, ktoré sa líšia v závislosti od kontextu. Môže sa použiť na nahlásenie súradníc ľubovoľného bodu, na výber uzla alebo prvku, na zmenu hlavného zobrazenia a na mnohé podobné úlohy. 

  * **Posun** (Shift+ĽPK): Funkcia „Posun“ upravuje oblasť vyplňujúcu aktívne zobrazenie bez zmeny veľkosti zobrazeného objektu.

  * **Dynamické priblíženie** (Alt+ľavé tlačidlo myši): Dynamické priblíženie dynamicky mení veľkosť oblasti objektu, ktorá vyplňuje aktívne zobrazenie. Veľkosť zobrazenia je možné zmeniť podržaním klávesy Alt a kliknutím ľavým tlačidlom myši v aktívnom okne zobrazenia, pričom posúvaním kolieska myši dopredu alebo dozadu zväčšíte alebo zmenšíte veľkosť objektu v okne zobrazenia.

  * **Okno zväčšenia** (Ctrl+Alt+ĽMB) : Funkcia okna zväčšenia umožňuje podrobné preskúmanie malej časti aktuálne zobrazeného objektu alebo grafu. Oblasť zväčšenia sa vyberie podržaním klávesov Ctrl + Alt a kliknutím ľavým tlačidlom myši, pričom ťahaním myši ohraničíte vybranú oblasť zobrazeným rámčekom. Po uvoľnení tlačidla myši sa vybraná oblasť vyplní celé zobrazovacie okno.

  * **Otočiť** (Ctrl+ĽAVÉ TLAČIDLO MYŠI): Táto funkcia umožňuje kurzoru myši otáčať geometrie v požadovanom smere.

  * **Otočiť okolo osi X**: Táto funkcia umožňuje kurzoru myši otáčať objekt v smere osi X.

  * **Otočenie okolo osi Y**: Táto funkcia umožňuje kurzoru myši otáčať objekt v smere osi Y.

  * **Otočenie okolo osi Z**: Táto funkcia umožňuje kurzoru myši otáčať objekt v smere osi Z. 

### Ponuka „Okno“

  * **Kaskáda**: Ak zvolíme typ „Kaskáda“, databáza sa vždy otvorí v novom okne.

  * **Dlaždica**: Databáza sa zmestí do okna na zobrazenie.

  * **Usporiadať dlaždice vodorovne**: Databáza sa v okne zobrazenia zobrazí vo vodorovnom smere.

### Ponuka možností

**Životné prostredie** : 

Používateľ môže prispôsobiť pracovné prostredie programu DEFORM pomocou možnosti „Prostredie“. Tu môže používateľ vykonávať zmeny v nastaveniach zobrazenia a grafických nastaveniach. Nastavenia sa uplatnia od nasledujúcej relácie.

Región: V položke „Jazyk“ si používateľ môže vybrať preferovaný jazyk a v položke „Jednotky“ nastaviť anglické alebo SI jednotky ako predvolený systém jednotiek pre novú reláciu. (Pozri obr. 50.1.23.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0023.jpg' | relative_url }})

Karta „Životné prostredie – Región“

**Adresáre**: Možnosť „Adresáre“ v okne „Nastavenia prostredia“ sa zobrazuje tak, ako je znázornené na obr. 50.1.24. Používateľ môže vyhľadať požadované umiestnenie a nastaviť ho ako pracovný adresár; tento adresár sa bude používať ako predvolené umiestnenie na ukladanie geometrií, pokiaľ používateľ neurčí iné umiestnenie. Dočasné súbory vytvorené počas spustenia nástroja Geo sa ukladajú do cesty uvedenej v položke Umiestnenie dočasných súborov.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0024.jpg' | relative_url }})

Karta „Zoznamy životného prostredia“

**Uhol prvku**: Táto voľba umožňuje používateľovi zmeniť rozsah výberu pri výbere mnohouholníkov na úpravu geometrie metódou povrchových úsekov. Zobrazuje povrchový úsek tak, že povrchy v rámci uhla prvku považuje za jeden povrch. Zakrivený povrch s menším uhlom prvku znamená, že sa naraz vyberie menej povrchových mnohouholníkov. Karta na zmenu uhla prvku je znázornená na obr. 50.1.25.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0025.jpg' | relative_url }})

Karta „Funkcie pre životné prostredie“

**Ikona/Písmo**: Používateľ môže podľa potreby zmeniť ikonu a veľkosť písma, ako je znázornené v [Fig. 50.1.26.](50_1_3d_geo_tool.htm#Fig_50_1_26_Icon/Font_options_under_Environment_Settings_window)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0026.jpg' | relative_url }})

Možnosti ikon a písma v okne Nastavenia prostredia

### Ponuka Pomoc

Možnosti ponuky Pomoc sú zobrazené na obr. 50.1.27. Tieto možnosti možno použiť na otvorenie príručky a zobrazenie stručných informácií o produkte.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0027.jpg' | relative_url }})

Možnosti ponuky Pomocník

**Poznámka**: Možnosti v ponuke „Pomoc“ zatiaľ nefungujú.

## Editor vlastností

Možnosti v editore vlastností (ako napríklad Analýza, Meranie, Rozdelenie, Úprava, Overovanie a Morfing) sú kľúčové funkcie na analýzu a úpravu geometrií.

### Analýza

Okno analýzy zobrazuje podrobnosti o importovanej/vytvorenej geometrii a umožňuje upravovať geometrie pomocou rôznych možností. (Pozri obr. 50.1.28.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0028.jpg' | relative_url }})

Možnosti na karte „Analýza“

**Automatická oprava** ![]({{ '/assets/icons/pre_icons/geo_tool_auto_fix.jpg' | relative_url }}): Táto voľba automaticky opraví neplatnú geometriu. Táto voľba odstráni neplatné plášte, voľné slučky, voľné hrany, plášte s nepravidelnosťami, voľné krivky, chybné hrany a zabezpečí, aby geometria bola vodotesná.

**Vytvoriť:** Táto voľba slúži na vytvorenie mnohoúhelníka výberom bodov.

**Odstrániť:** Táto voľba odstráni vybranú časť geometrie alebo celú vybranú geometriu.

**Otočiť:** Táto voľba otočí povrch vybranej geometrie.

**Normálne:**

  * **Jednotné orientovanie plášťov**: Toto akčné tlačidlo zabezpečí, že všetky vybrané polygóny geometrie budú súvislé tým, že ich orientuje v jednom smere. Ak si to chcete overiť, vytvorte primitívnu valcovú geometriu, vyberte ľubovoľný mnohouholník > kliknite na „Flip“ > teraz kliknite na „Orient shells consistently“; tým sa všetky mnohouholníky, ktoré sú nesúrodé, zosúladia so zvyškom mnohouholníkov. (Pozri obr. 50.1.29.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0029.jpg' | relative_url }})

Príklad použitia možnosti „Orient Shell consistently“

  * **Automatická korekcia orientácie:** Ak používateľ použije možnosť automatickej korekcie orientácie, systém opraví orientáciu polygónov proti smeru hodinových ručičiek a jednotne ich nasmeruje proti smeru hodinových ručičiek (pozri obr. 50.1.30).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0030.jpg' | relative_url }})

Príklad možnosti „Automatická oprava orientácie“

**Spojenie**: Táto voľba slúži na vyplnenie medzier medzi polygónmi, ktoré nie sú po povrchu prepojené. Po kliknutí na tlačidlo „Spojenie“ sa existujúce polygóny, ktoré nie sú po povrchu prepojené, upravia tak, aby sa spojili v rámci tolerancie spojenia. (Pozri obr. 50.1.31.)

  * **Odhad tolerancie spájania**: Po kliknutí na položku „Odhad tolerancie spájania“ sa vypočíta hodnota tolerancie pre spájanie mnohouholníkov v geometrii.

  * **Automatické spájanie**: Ak sa použije táto voľba, systém automaticky odhadne toleranciu spájania a spojí polygóny celej geometrie, ktoré sa nachádzajú v rámci tolerancie spájania.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0031.jpg' | relative_url }})

Možnosti záložiek pre stehy

**Vyplnenie**: Chýbajúce plochy alebo mnohouholníky v geometrii, kvôli ktorým nie je možné geometriu uzavrieť, sa považujú za otvory. (Pozri obr. 50.1.32.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0032.jpg' | relative_url }})

Karta „Možnosti“ v okne „Vyplniť“

  * **Vyplniť otvory**: Po kliknutí na položku „Vyplniť otvory“ sa vytvoria nové mnohouholníky, ktoré vyplnia chýbajúce plochy alebo mnohouholníky.

  * **Vyplniť všetky otvory**: Po kliknutí na tlačidlo „Vyplniť všetky otvory“ sa všetky otvory v geometrii vyplnia novými mnohouholníkmi.

.

  * **Spojiť dve slučky**: Táto možnosť slúži na spojenie dvoch rôznych slučiek. Po výbere dvoch slučiek a kliknutí na možnosť „Spojiť dve slučky“ sa slučky spoja.

  * **Automatické vyplnenie**: Keď používateľ využije funkciu automatického vyplnenia, systém automaticky identifikuje chýbajúce plochy/polygóny v geometrii a vyplní ich novými polygónmi.

**Plášť**: Na karte „Plášť“ sa v tabuľke zobrazia informácie o každom plášti týkajúce sa stavu, počtu polygónov v plášti, plochy povrchu plášťa a objemu. (Pozri obr. 50.1.33.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0033.jpg' | relative_url }})

Karta „Shell“ – Možnosti

  * **Označiť šumové obaly**: Keď používateľ klikne na tlačidlo „Označiť šumové obaly“, systém zvýrazní šumové obaly na základe kritérií uvedených v nastaveniach „Možnosti šumových obalov“.

  * **Možnosti „Noisy Shell“:** Pomocou tlačidla „Noisy Shell Options“ môže používateľ určiť kritériá, na základe ktorých sa rozhodne, či ide o „noisy shell“, alebo nie.

**Trojuholník** : 

  * **Nástroj**: Na karte Nástroj sa nachádza tlačidlo Kontrola, ktoré slúži na kontrolu geometrie a identifikáciu a zobrazenie počtu polygónov s dvojitou plochou, počtu polygónov, ktoré sa pretínajú, počtu polygónov pripojených k chybnej hrane a počtu duplicitných polygónov. Na tejto karte môže používateľ špecifikovať kritériá, ako sú vzdialenosť, uhol a smer normály, na identifikáciu polygónov s dvojitou plochou. (Pozri obr. 50.1.34.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0034.jpg' | relative_url }})

Možnosti trojuholníkových záložiek

**Bod**: Karta „Bod“ slúži na vytváranie nových bodov alebo na duplikovanie existujúcich bodov 3D geometrie. (Pozri obr. 50.1.35.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0035.jpg' | relative_url }})

Možnosti na karte „Bod“

  * **Nástroj**: Možnosti nástroja slúžia na vytváranie nových bodov alebo duplikovanie existujúcich bodov 3D geometrie.

  * **Vlastnosti**: V časti „Vlastnosti“ systém zobrazuje číslo bodu a súradnice vybraného bodu alebo bodu, ktorý sa má vytvoriť.

**Geometria**: Na tejto karte môže používateľ zadať kritériá, ako sú vzdialenosť, uhol a smer normály, na identifikáciu mnohouholníkov s dvojitou plochou. (Pozri obr. 50.1.36.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0036.jpg' | relative_url }})

Možnosti na karte „Geometria“

  * **Dvojitá plocha**: Možnosť „Kontrola dvojitej plochy“ slúži na overenie, či geometria obsahuje viac ako jednu plochu, a to na základe zadaných hodnôt vzdialenosti a uhla určených na kontrolu dvojitej plochy, keďže program DEFORM vyžaduje, aby geometria mala iba jednu plochu.

  * **Prekrývajúce sa trojuholníky**: Možnosť „Prekrývajúce sa trojuholníky“ slúži na kontrolu, či geometria obsahuje nejaké prekrývajúce sa mnohouholníky.

**Pokročilé** : 

  * **Nástroj:**

  * **Spresnenie (konformné):** Keď používateľ klikne na tlačidlo „Spresniť konformne“, systém spresní geometriu zmenšením veľkosti polygónov, čím sa zvýši ich počet. (Pozri obr. 50.1.37.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0037.jpg' | relative_url }})

Možnosti na karte „Pokročilé“

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0038.jpg' | relative_url }})

Príklad spresnenia plochy geometrie

  * **Rozdelenie (nekonformné):**

  * **Kapotáž** :

  * **Výber kontaktnej oblasti**: Táto voľba sa zvyčajne používa pri lagrangovskom vytláčaní. Pri vytláčaní, kde sa materiál vychádzajúci z rôznych vreciek navzájom dotýka, slúži na vyčistenie týchto polygónov s vnútornými kontaktmi a na zabezpečenie plynulého toku materiálu prostredníctvom importu kontaktných podmienok s kľúčovým slovom BCC.

  * **Pripojte jednu škrupinu** :

  * **Prepojte všetky plášte** :

### Miera

**Meranie**: V tejto časti sa zobrazuje typ merania – či ide o meranie vzdialenosti medzi dvoma bodmi alebo medzi dvoma mnohouholníkmi – spolu s vektorom, dĺžkou a popiskom nameranej vzdialenosti. (Pozri obr. 50.1.39.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0039.jpg' | relative_url }})

Možnosti na karte „Meranie“

**Smer**: Pomocou možností nastavenia smeru môže používateľ zvoliť smer, v ktorom sa má vykonať meranie medzi dvoma vybranými objektmi.

**Filter**: Táto sekcia slúži na meranie vzdialenosti medzi bodmi, hranami, trojuholníkmi a plochami; zaškrtnutím príslušných políčok môže používateľ túto vzdialenosť zmerať.

**Informácie**: V tejto časti sú uvedené informácie o mnohouholníku, na ktorom sa nachádza kurzor alebo ktorý bol vybraný. Tieto informácie zahŕňajú číslo mnohouholníka, súradnice, plochu a smer normály.

**Vymazať**: Pomocou tlačidla „Vymazať“ môže používateľ vymazať naposledy zmeranú vzdialenosť.

**Vymazať všetko**: Pomocou tlačidla „Vymazať všetko“ môže používateľ vymazať všetky namerané vzdialenosti.

### Krájanie

Karta „Rezanie“ slúži na rezanie geometrie a pohľadu. Geometriu je možné rezať v ľubovoľnom smere zaškrtnutím príslušných políčok. Polohu roviny rezu je možné nastaviť pomocou posuvníka. (Pozri obr. 50.1.40.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0040.jpg' | relative_url }})

Geometrické rozkrájanie

**Rozrezávanie objektov:** Keď používateľ klikne na tlačidlo „Rozrezávanie objektov“, vytvorí sa nový objekt rozrezaním geometrie existujúceho objektu v zadej rovine rezu. Pôvodný diel zostane zachovaný a otvory sa vyplnia podľa stavu príslušných začiarkavacích políčok.

**Vytlačenie objektov**: Pomocou možnosti „Vytlačenie“ môže používateľ vytlačiť geometriu jedného objektu na druhý, napríklad použitím možnosti „valec“ na vytvorenie kruhových drážok po rozdelení drážkovanej časti, pozri obr. 50.1.41.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0041.jpg' | relative_url }})

Príklad použitia možnosti „imprint“ na vytvorenie projekcií

### Upraviť

**Orezávanie**: Možnosti orezávania slúžia na odstránenie časti geometrie pomocou definovania orezávacej čiary. To je možné vykonať nasledujúcimi krokmi:

  1. Vymedzenie orezávacej línie na geometrii. (Pozri obr. 50.1.42.)

  2. Používateľ môže zobraziť náhľad geometrie oreza. (Pozri obr. 50.1.43.)

  3. Kliknite na tlačidlo „Trim“, aby ste geometriu orezať. (Pozri obr. 50.1.44.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0042.jpg' | relative_url }})

Určenie orezávacej čiary

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0043.jpg' | relative_url }})

Náhľad orezania

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0044.jpg' | relative_url }})

Geometria po orezaní

Používateľ si môže zachovať pôvodný objekt tak, že zaškrtne políčko „Zachovať pôvodnú časť“.

**Booleovské operácie:** Booleovské operácie sa používajú na zjednotenie, odčítanie a nájdenie spoločného množiny dvoch geometrických telies.

**Zjednotenie**: Funkcia „Zjednotenie“ slúži na zlúčenie dvoch geometrií do jednej. Zjednotenie je možné vykonať nasledujúcimi krokmi:

  1. Vytvorte dve geometrie alebo importujte dve geometrie.

  2. Umiestnite geometrie tak, aby sa prekrývali v súlade s novými požiadavkami na geometriu.

  3. Prejdite na stránku editora vlastností „Modify“. (Pozri obr. 50.1.45.)

  4. Kliknite na tlačidlo „Zjednotiť“, aby ste spojili obe geometrie; farebné odtiene geometrií, ktoré sa majú spojiť, sa zobrazia na stránke „Upraviť“. (Pozri obr. 50.1.46.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0045.jpg' | relative_url }})

Definovanie dvoch nových geometrií

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0046.jpg' | relative_url }})

Spojenie geometrických telies pomocou možnosti „Union“

**Odčítanie:** Funkcia odčítania slúži na odstránenie nežiaducej časti geometrie pomocou geometrie iného objektu. Odčítanie je možné vykonať nasledujúcimi krokmi:

  1. Vytvorte dve geometrie alebo importujte dve geometrie.

  2. Umiestnite geometrické telesa tak, aby sa navzájom prekrývali. (Pozri obr. 50.1.47.)

  3. Prejdite na stránku editora vlastností „Modify“.

  4. Vyberte možnosť „odpočítať“, aby ste jednu geometriu odpočítali od druhej; farebné odtiene odpočítanej geometrie a geometrie, od ktorej sa odpočítava, sa zobrazia na stránke „Modify“ (pozri obr. 50.1.48.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0047.jpg' | relative_url }})

Definovanie dvoch nových geometrií pre odčítanie

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0048.jpg' | relative_url }})

Geometria odčítania

**Intersect**: Táto voľba slúži na vyberanie spoločnej časti dvoch geometrických telies. To je možné vykonať pomocou nasledujúcich krokov:

  1. Vytvorte dve geometrie alebo importujte dve geometrie.

  2. Umiestnite geometrické telesa tak, aby sa navzájom prekrývali.

  3. Prejdite na stránku editora vlastností „Modify“. (Pozri obr. 50.1.49.)

  4. Vyberte možnosť tlačidla „Intersect“ (Priesečník), aby ste vytvorili spoločnú časť oboch geometrií; farebné odtiene geometrií, z ktorých sa bude spoločná geometria vytvárať, sú zobrazené na stránke „Modify“ (pozri obr. 50.1.50.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0049.jpg' | relative_url }})

Vytvorenie dvoch geometrických útvarov

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0050.jpg' | relative_url }})

Odstránenie prekrývajúcej sa časti

Používateľ si môže zachovať pôvodný objekt tak, že zaškrtne políčko „Zachovať pôvodnú časť“.

###  Overiť

**Kvalita**: V okne „Kvalita“ môže používateľ analyzovať ohyby v geometrii na základe zadaných kritérií a tiež tieto ohyby odstrániť. (Pozri obr. 50.1.51.)

**Porovnanie**: Pomocou možností porovnania môže používateľ porovnať dve geometrie z hľadiska počtu mnohouholníkov, počtu bodov, minimálnej dĺžky mnohouholníka, minimálnej plochy mnohouholníka, počtu plášťov, počtu plášťov s chybami, počtu chybných hrán, počtu voľných hrán, objemu a povrchovej plochy. (Pozri obr. 50.1.51.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0051.jpg' | relative_url }})

Overiť možnosti na karte

### Morfing

Používateľ môže využiť morfing na zmenu geometrie jedného objektu na geometriu iného objektu. Morfing sa najčastejšie používa pri nastavovaní optimalizačných úloh. (Pozri obr. 50.1.53.)

**Spojenie párov:** Na vykonanie morfingu sú potrebné dva objekty. Jeden objekt sa považuje za zdrojový, ktorého geometria sa má transformovať, a druhý objekt sa považuje za cieľový, ktorého geometria sa má dosiahnuť. Používateľ môže vybrať povrch na zdrojovom objekte, ktorý sa má transformovať, a zodpovedajúci povrch na cieľovom objekte a spárovať ich.

Na stránke „Prepojené páry“ môže používateľ pridávať, odstraňovať, importovať a exportovať prepojené páry. (Pozri obr. 50.1.52.)

Používateľ môže vypočítať výsledky kliknutím na tlačidlo „Vypočítať“.

Po vypočítaní výsledkov si môže používateľ prezrieť náhľad transformovanej geometrie.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0052.jpg' | relative_url }})

Okno „Spojiť páry“

**Náhľad výsledkov morfingového spracovania**: Po výpočte výsledkov si používateľ môže pomocou posuvníka prezrieť náhľad jednotlivých fáz morfingového spracovania. Náhľad výsledkov morfingového spracovania môže používateľ skryť pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}). (Pozri obr. 50.1.53.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0053.jpg' | relative_url }})

Okno s náhľadom výsledkov morfingového spracovania

**Uloženie výsledkov morfingového spracovania**: Používateľ môže výsledky morfingového spracovania uložiť tak, že vyberie umiestnenie, a výsledky sa uložia vo formáte *.GEO. (Pozri obr. 50.1.54.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0054.jpg' | relative_url }})

Uložiť okno s výsledkami morfingovania
