---
lang: sk
title: "Polotovar na ozubené kolesá EN Lab 10"
---

# Cvičenie č. 10: Operácia symetrie s polotovarom ozubeného kolesa

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_sym**, aby ste mohli nastaviť izotermické symetrické tvárnenie polotovaru ozubeného kolesa.

### Pridať operáciu a objekty

V editore operácií pridajte **3D tvarovaciu operáciu** z **priečinka**.

V vetve „Simulačné ovládacie prvky“ v strome operácií zrušte zaškrtnutie políčka „Režim prenosu tepla“ na hlavnej karte „Simulačné ovládacie prvky“, keďže ide o izotermickú simuláciu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Načítajte materiál **AISI-8620[1550–2200 °F (850–1200 °C)]** z knižnice **Steel_at_Extended_Temperatures**.

Kliknite na vetvu **Objekty** v strome operácií, aby ste pridali objekty a pokračovali v nastavení. Pridajte tri objekty (ak ešte neexistujú) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali obrobok.

### Definovanie symetrie obrobku

Nastavte teplotu na **2250** °F a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vytvorte geometriu.

**Vytvorenie geometrie obrobku**  
Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), aby ste vytvorili obrobok z primitívu **valca** s priemerom **5** ”, **0,1** ” **polomermi** rohov, výškou **8,15** “ a uhlom otáčania **30** ° s **30** rezmi. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte ponuku.

Keďže smer hornej časti formy je Y, obrobok je potrebné otočiť tak, aby bol zarovnaný so smerom hornej časti formy. Kliknite teda na vetvu **Polohovanie** v strome operácií a otočte obrobok o 90° okolo osi –X a stredu (0,0,0) pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}), rovnako ako v prípade [Lab5]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab5/' | relative_url }}).

Vráťte sa do okna „Geometria obrobku“ kliknutím na vetvu **Geometria** v strome operácií, aby ste mohli definovať symetrické roviny.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}). Vyberte vetvu „Planárna symetria“ a pomocou panela nástrojov na ľavej strane (pod prehliadačom) vyberte v grafickom okne symetrické roviny, ako je znázornené na obr. L10.1., vždy po jednej.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0001.jpg' | relative_url }})

Symetrické plochy

Po výbere roviny kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), aby ste pridali rovinné symetrické roviny.

Poznámka:

Symetria pomôže generátoru sietí pri určovaní hrán, ktoré je potrebné chrániť počas vytvárania siete.

Pridané symetrické plochy sa zobrazia v časti „Rovinná symetria“, ako je znázornené na obr. L10.2. Overte symetrické roviny tak, že v časti „Rovinná symetria“ vyberiete pridané vetvy a v grafickom okne si všimnete zvýraznenú rovinu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0002.jpg' | relative_url }})

Pridané symetrické roviny

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vygenerujte sieť s **10 000** prvkami. Program Deform sa vás opýta, či chcete v sieti BCC použiť symetrickú definíciu geometrie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). (Pozri obr. L10.3.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0003.jpg' | relative_url }})

Vytvorenie siete BCC z geometrie – kontextové menu BCC

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a v zozname materiálov vyberte materiál **AISI-8620**.

Prejdite v stromovej štruktúre operácií do okna **Okrajové podmienky obrobku** a overte 2 roviny symetrie. (Pozri obr. L10.4.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0004.jpg' | relative_url }})

Symetria generovanej siete BCC na základe symetrie geometrie BCC

Kliknite na položku **Top****die** v prevádzkovom strome, aby ste naimportovali matrice.

### Importovanie foriem

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), aby ste naimportovali objekt hornej matrice z prvého kroku operácie kovania (op 2) súboru „**Gear_t.DB**“.

Kliknite na položku **Spodná forma** v strome operácií.

Podobne naimportujte objekt spodnej matrice v prvom kroku operácie 2 (zo súboru **Gear_t****.DB**).

### Vytvorenie vzťahov medzi objektmi

Na stránke „Kontakt“ pridajte tri vzťahy pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Pre prvý vzťah vyberte „Obrobok“ ako hlavný prvok a „Obrobok“ ako podriadený prvok, čím modelujete vlastný kontakt; pre druhý vzťah vyberte „Horná forma“ ako hlavný prvok a „Obrobok“ ako podriadený prvok; a pre posledný vzťah vyberte „Spodná forma“ ako hlavný prvok a „Obrobok“ ako podriadený prvok. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) a nastavte hodnotu trenia pri šmyku na 0,3. Ak chcete priradiť rovnakú hodnotu trenia všetkým vzťahom, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) na výpočet hodnoty tolerancie a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali ovládacie prvky **zastavenia** a **simulácie**.

### Nastavenie ovládacích prvkov zastavenia a simulácie

Nastavte **kritériá zastavenia** tak, aby sa dosiahla hrúbka blesku **0,20** palca.

Keďže sa vzdialenosť medzi objektmi v zastavovacích kontrolách importuje spolu s objektmi do okna zastavovacích kontrol, zaškrtnite políčko „Vzdialenosť medzi objektmi“ a vyberte objekt 1 ako hornú maticu a objekt 2 ako spodnú maticu. Tým sa načítajú importované referenčné body hornej a spodnej matice a zobrazia sa v grafickom okne. V dátovom poli zadajte hodnotu **0,2** palca a ako smer vzdialenosti vyberte Y.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky simulácie.

Nastavte ovládacie prvky krokov v časti „Simulation Controls“ (Ovládacie prvky simulácie). Pre túto operáciu použite **300** krokov. Zmerajte vzdialenosť medzi nástrojmi, aby ste určili vhodnú hodnotu posunu formy. Celkovú vzdialenosť (8,0) vydelite počtom krokov (300), čím získate posun formy (**0,02667**). Ukladajte každých **10** krokov.

### Vytvorte databázu a spustite simuláciu

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) (nad stromom operácií), aby ste spustili simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore MO použite nástroj na zrkadlenie ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) z nástrojov postprocesora na vytvorenie kompletného obrobku s rozsahom 360 stupňov. V režime zrkadlenia môžete kliknúť na jednu z rovín symetrie obrobku, aby ste ho zrkadlili. Na vytvorenie kompletného obrobku bude potrebných 11 kliknutí. Môžete prejsť do režimu mazania a kliknutím na zrkadlené objekty ich odstrániť z obrazovky. (Pozri obr. L10.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0005.jpg' | relative_url }})

Objekt so zrkadlovou symetriou so zrkadlením ukazovateľa v rovine symetrie
