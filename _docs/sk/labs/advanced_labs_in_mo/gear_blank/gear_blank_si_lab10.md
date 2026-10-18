---
lang: sk
title: "Polotovar na ozubené kolesá SI Lab 10"
---

# Laboratórna práca č. 10. Operácia s využitím symetrie polotovaru ozubeného kolesa

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_sym**, v ktorom nastavíte izotermické symetrické tvárnenie polotovaru ozubeného kolesa.

### Pridať operáciu a objekty

V editore operácií z prehliadača pridajte **3D tvarovaciu operáciu**.

V vetve **Ovládacie prvky simulácie** v strome operácií **zrušte zaškrtnutie** **režimu** **prenosu tepla** na hlavnej karte ovládacích prvkov simulácie, keďže ide o izotermickú simuláciu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Načítajte materiál **AISI-8620[1550–2200 °F (850–1200 °C)]** z knižnice **Steel_at_Extended_Temperatures**.

Kliknite na vetvu **Objekty** v strome operácií, aby ste pridali objekty a pokračovali v nastavení. Pridajte tri objekty (ak ešte neexistujú) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali obrobok.

### Definovanie symetrie obrobku

Nastavte teplotu na **1232,22°****C** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vytvorte geometriu.

**Vytvorenie geometrie obrobku**

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), aby ste vytvorili obrobok z primitívu **valca** s priemerom **127****mm**, **2,54****mm**, výškou **207,01****mm** a uhlom otáčania **30°** s **30** rezmi. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte ponuku.

Keďže smer výstupu z lisovacej formy je po osi Y, obrobok je potrebné otočiť tak, aby bol zarovnaný so smerom výstupu z lisovacej formy. Kliknite teda na vetvu **Polohovanie** v strome operácií a otočte obrobok o 90° okolo osi –X a stredu (0,0,0) pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}), tak ako v Lab5.

Vráťte sa do okna „Geometria obrobku“ kliknutím na vetvu **Geometria** v strome operácií, aby ste mohli definovať symetrické roviny.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}). Vyberte vetvu **Planárna****symetria** a pomocou panela nástrojov na ľavej strane (pod prehliadačom) vyberte v grafickom okne symetrické roviny, ako je znázornené na obrázku [Fig. L10.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab10/' | relative_url }}#Fig_L10_1_Symmetry_surfaces), vždy po jednej.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab10_image0001.jpg' | relative_url }})

Symetrické plochy

Po výbere roviny kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), aby ste pridali rovinné symetrické roviny.

**Poznámka**:

Symetria pomôže generátoru sietí pri určovaní hrán, ktoré je potrebné chrániť počas vytvárania siete.

Pridané symetrické plochy sa zobrazujú v časti „Rovinná symetria“, ako je znázornené na obrázku [Fig. L10.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab10/' | relative_url }}#Fig_L10_2_Added_symmetry_planes). Overte symetrické roviny tak, že v časti „Rovinná symetria“ vyberiete pridané vetvy a v grafickom okne si všimnete zvýraznenú rovinu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab10_image0002.jpg' | relative_url }})

Pridané symetrické roviny

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vygenerujte sieť s **10000** prvkami. Program Deform sa vás opýta, či chcete v sieti BCC použiť symetrickú definíciu geometrie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). (Pozrite [Fig. L10.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab10/' | relative_url }}#Fig_L10_3_Generating_Mesh_BCC_from_Geometry_BCC_popup))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab10_image0003.jpg' | relative_url }})

Vytvorenie siete BCC z geometrie – kontextové menu BCC

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a v zozname materiálov vyberte materiál **AISI-8620**.

Prejdite v stromovej štruktúre operácií do okna **Okrajové podmienky obrobku** a overte 2 roviny symetrie. (Pozri [Fig. L10.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab10/' | relative_url }}#Fig_l10_4_Generated_mesh_symmetry_BCC_from_geometry_symmetry_BCC))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab10_image0004.jpg' | relative_url }})

Symetria generovanej siete BCC odvodená zo symetrie geometrie BCC

Kliknite na položku **Horná matrica** v prevádzkovom strome, aby ste importovali matrice.

### Importovanie foriem

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }}), aby ste naimportovali objekt **top****die** z prvého kroku operácie **Forge** (op 2) súboru „**Gear_t.DB**“.

Kliknite na položku **Spodná forma** v strome operácií.

Podobne na prvom kroku operácie 2 načítajte objekt pre **bottom****die** (z **Gear_t.****DB**).

### Umiestňovanie objektov

Na presun nástrojov k obrobku použite polohovanie s ohľadom na kolízie.

### Vytvorenie vzťahov medzi objektmi

Na stránke „Kontakt“ pridajte tri vzťahy pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Pre prvý vzťah vyberte „Obrobok“ ako hlavný prvok a „Obrobok“ ako podriadený prvok, aby ste modelovali vlastný kontakt; pre druhý vzťah vyberte „Horná matrica“ ako hlavný prvok a „Obrobok“ ako podriadený prvok; a pre posledný vzťah vyberte „Spodná matrica“ ako hlavný prvok a „Obrobok“ ako podriadený prvok. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) a nastavte hodnotu trenia pri šmyku na 0,3. Ak chcete priradiť rovnakú hodnotu trenia všetkým vzťahom, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) na výpočet hodnoty tolerancie a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali ovládacie prvky **zastavenia** a **simulácie**.

### Definovanie ovládacích prvkov zastavenia a simulácie

Nastavte kritériá zastavenia tak, aby sa dosiahla hrúbka výplne **5,08** mm.

Keďže sa vo okne „Zastavovacie ovládacie prvky“ spolu s objektmi importujú aj vzdialenosti medzi objektmi, zaškrtnite políčko „Vzdialenosť medzi objektmi“ a vyberte objekt 1 ako hornú matricu a objekt 2 ako spodnú matricu. Tým sa načítajú importované referenčné body hornej a spodnej matrice a zobrazia sa v grafickom okne. V dátovom poli zadajte hodnotu **5,08** mm a ako smer vzdialenosti vyberte Y.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky simulácie.

Nastavte ovládacie prvky krokov v časti „Simulation Controls“. Pre túto operáciu použite **300** krokov. Zmerajte vzdialenosť medzi nástrojmi, aby ste určili vhodnú hodnotu posunu matrice. Celkovú vzdialenosť (203,2) vydelíte počtom krokov (**300**), čím získate posun formy (**0,67733**). Ukladajte každých **10** krokov.

### Vytvorte databázu a spustite simuláciu

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo „Režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})“ (nad stromom operácií), aby ste spustili simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore MO použite nástroj na zrkadlenie ![]({{ '/assets/icons/pre_icons/mo_mirror_merge_icon.jpg' | relative_url }}) z nástrojov postprocesora na vytvorenie kompletného obrobku s rozsahom 360 stupňov. V režime zrkadlenia môžete kliknúť na jednu zo symetrických rovín obrobku, aby ste ho zrkadlili. Na vytvorenie kompletného obrobku bude potrebných 11 kliknutí. Môžete prejsť do režimu mazania a kliknutím na zrkadlené objekty ich odstrániť z obrazovky. (Pozri [Fig. L10.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab10/' | relative_url }}#Flg_L10_5_Mirrored_symmetry_object_with_pointer_mirroring_on_symmetry_plane))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab10_image0005.jpg' | relative_url }})

Objekt so zrkadlovou symetriou so zrkadlením ukazovateľa v rovine symetrie
