---
lang: sk
title: "26.6.6. Zhrnutie"
---

# 26.6.6. Zhrnutie

[2D, 3D]: V okne s prehľadom simulácie je možné vybrať krok zo zoznamu krokov a následne vybrať objekt pomocou tlačidla s rozbaľovacou šípkou v poli objektu. Po zmene objektu sa v prípade, že sa zmení krok, objekt nezmení. Určité charakteristické údaje, ako sú zaťaženia lisu, rýchlosti primárnych foriem a maximálne a minimálne hodnoty stavových premenných, sa ukladajú pre každý simulačný krok, bez ohľadu na to, či sa údaje pre každý krok ukladajú do databázy alebo nie. Tieto grafy súhrnných údajov v závislosti od času pre všetky uložené kroky je možné zobraziť v grafickom okne výberom stavovej premennej zo zoznamu a kliknutím na tlačidlo v spodnej časti okna. (Pozri obr. 26.6.6.1. a [Fig. 26.6.6.2.](26_6_2_object_elements.htm#Fig_26_6_2_2_Object_Elements_window_for_3D)).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_6_summary/image001.jpg' | relative_url }})

Okno s prehľadom stavových premenných

Kliknutím na bod v grafe sa na obrazovku načíta najbližší uložený krok z databázy, ako je znázornené v [Fig. 26.6.6.2.](26_6_2_object_elements.htm#Fig_26_6_2_2_Object_Elements_window_for_3D)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_6_summary/image002.jpg' | relative_url }})

Súhrnný graf premenných teplotného stavu

Zoznam krokov v okne súhrnu slúži na výber kroku. Ak je zaškrtnuté políčko „Načítať krok“ a krok je vybraný zo zoznamu krokov, vybraný krok sa načíta do grafického okna a hodnoty stavových premenných v danom kroku sa zobrazia v okne súhrnu. Zobrazujú sa tu tiež informácie o simulácii, ako napríklad číslo simulácie, číslo kroku, čas, zdvih primárnej matrice, číslo siete (mení sa v prípade prepočítania siete), výskyt prehybov, rozmer operácie a číslo verzie.

Stavové premenné sú zoskupené do rôznych kategórií, a to ![]({{ '/assets/icons/post_icons/mo_analysis_icon.jpg' | relative_url }}) (Všeobecné), ![]({{ '/assets/icons/post_icons/mo_deformation_icon.jpg' | relative_url }}) (Deformácia), ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (Tepelné), ![]({{ '/assets/icons/post_icons/mo_heating_sv_icon.jpg' | relative_url }}) (Ohrev), ![]({{ '/assets/icons/post_icons/mo_prop_sv_icon.jpg' | relative_url }}) (Tepelné spracovanie) a ![]({{ '/assets/icons/post_icons/mo_user_sv_icon.jpg' | relative_url }}) (Používateľ). K týmto premenným je možné pristupovať pomocou ikon, ako je znázornené v [Fig. 26.6.6.2.](26_6_2_object_elements.htm#Fig_26_6_2_2_Object_Elements_window_for_3D)

Pomocou ikony ![]({{ '/assets/icons/post_icons/mo_show_all_sv_button.jpg' | relative_url }}) (Zobraziť všetko) je možné zobraziť všetky skupiny stavových premenných. Ikona ![]({{ '/assets/icons/post_icons/mo_clear_sv_icon.jpg' | relative_url }}) (Vymazať) slúži na zrušenie výberu všetkých skupín stavových premenných.

Dvojitým kliknutím na hodnotu stavovej premennej v okne súhrnu môže používateľ skopírovať minimálnu a maximálnu hodnotu v danom kroku; pomocou možnosti „Exportovať údaje grafu“ (prístupnej po kliknutí pravým tlačidlom myši) môže tiež exportovať údaje súhrnného grafu zobrazené v grafickom okne. Vlastnosti grafu, ako sú názvy a ich písmo, rozsah hodnôt, počet desatinných miest, štýl zobrazenia a zapnutie/vypnutie legendy, je možné zmeniť pomocou možnosti „Nastaviť vlastnosti grafu“, ktorá sa zobrazí po kliknutí pravým tlačidlom myši.

V prípade 3D úlohy, ak sa v nej nachádza nejaký ohyb, je možné ho lokalizovať pomocou tlačidla „Locate fold“ v dolnej časti okna; tým sa automaticky zapne zobrazenie ohybu vo grafickom okne pre vybraný objekt.
