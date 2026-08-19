---
lang: sk
title: "44.1. Konvertor z 2D do 3D"
---

# 44.1. Konvertor z 2D na 3D

44.1.1. Operátor „Previesť 2D na 3D“

44.1.2. Definovanie konfiguračných nastavení

44.1.3. Výber objektov na konverziu

44.1.4. Definovanie objektov

44.1.5. Nastavenie konverzie geometrie

44.1.6. Nastavenia konverzie siete

44.1.7. Definícia materiálu

44.1.8. Okno „Premena objektov“

44.1.9. Vytvorenie databázy

44.1.10. Pokračovať v nastavení 3D úlohy po spustení konvertora

44.1.11. Simulácia integrovaného 2D a 3D nastavenia

44.1.12. Následné spracovanie integrovaného 2D a 3D modelu v programe MO Post

##  Pridať operátor prevodníka z 2D na 3D

Po dokončení nastavenia 2D operácie môže používateľ pridať simulačný operátor „2D to 3D Converter“ z okna prehliadača, ako je znázornené na obr. 44.1.1. Aj ako prvú operáciu môžeme pridať operáciu „2D to 3D Converter“; v takom prípade je potrebné na konverziu importovať 2D databázu alebo 2D kľúčový súbor.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0001.jpg' | relative_url }})

Pridať konvertor z 2D do 3D

Ak chcete vyskúšať uvedený príklad, otvorte sprievodcu MO v anglickom systéme jednotiek > pridajte 2D operáciu tvárnenia > importujte súbor kľúčových slov HAMMER_LAB.KEY zo zložky 2D/LABS > prejdite do okna na generovanie databázy > vygenerujte databázu > následne z priečinka Explorer pridajte simulačný operátor na konverziu z 2D do 3D.

V editore operácií vyberte operátor „Prevodník z 2D do 3D“, aby sa otvoril tak, ako je znázornené na obrázku [Fig. 44.1.2.](44_1_2d_to_3d_converter.htm#Fig_44_1_2_Configuration_settings_of_converter_for_2D_axisymmetric/torsion_geometry_type)

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0002.jpg' | relative_url }})

Nastavenia konfigurácie prevodníka pre typ geometrie 2D osovo symetrickú/torznú

## Definovanie konfiguračných nastavení

Používateľ musí zvoliť smer nahor pre 3D modely pomocou prepínačov na výber súradnicového systému. Ako je uvedené, ak je zvolená možnosť „Z je hore“, smer Z bude smerom nahor, takže osovo symetrický smer nahor Z v 2D alebo smer nahor Y pri rovinnom deformovaní sa v 3D modeli stane smerom Z. Podobne v prípade voľby „Y je hore“ sa os Y stane smerom nahor v 3D konvertovanom modeli. Predvolene je ako smer nahor zvolený smer Z.

Používateľ môže ovládať počet otáčok a počiatočný uhol objektu pre typ 2D osovo symetrickej geometrie pomocou nastavenia 3D parametrov, ako je znázornené v [Fig. 44.1.2.](44_1_2d_to_3d_converter.htm#Fig_44_1_2_Configuration_settings_of_converter_for_2D_axisymmetric/torsion_geometry_type)

Pri konverzii 2D geometrie s rovinným deformovaním/rovinným napätím môže používateľ ovládať dĺžku extrudovania a počiatočnú polohu pomocou nastavení 3D parametrov, ako je znázornené v [Fig. 44.1.3.](44_1_2d_to_3d_converter.htm#Fig_44_1_3_Configuration_settings_of_converter_for_2D_plane_strain/plane_stress_geometry_type). To si možno vyskúšať importovaním príkladu Rib_web_SI.Príklad 2D kovania KEY do 2D operácie tvárnenia podobnej osovo symetrickému príkladu HAMMER_LAB uvedenému v tejto príručke v časti 44.1.1.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0003.jpg' | relative_url }})

Konfiguračné nastavenia konvertora pre typ geometrie 2D rovinného deformácie/rovinného napätia

## Vyberte objekty, ktoré chcete previesť

Všetky objekty z predchádzajúcej operácie sa automaticky prenesú do operácie konvertora; ak niektoré z týchto objektov nie sú potrebné pre ďalšiu 3D operáciu, je možné ich odstrániť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}), ako je znázornené na obr. 44.1.4. Keďže sa prenesú všetky objekty z predchádzajúcej operácie, všetky typy objektov sa načítajú z databázy.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0004.jpg' | relative_url }})

Okno na výber objektov

## Definovanie objektov

Na stránke objektov, ak je objekt načítaný z predchádzajúcej operácie, jeho typ sa prečíta z typu v databáze. Používateľ môže tiež pridať prevodný operátor ako prvú operáciu a importovať 2D objekty z databázy DEFORM alebo zo súboru kľúčových slov pomocou možnosti importu objektov, ako je znázornené na obr. 44.1.5. Ak používateľ importoval akýkoľvek 2D objekt na prevod, typ objektu bude taký, ako je v importovanom súbore, namiesto toho, aby bol načítaný z databázy.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0005.jpg' | relative_url }})

Okno všeobecných nastavení objektov

##  Nastavenie konverzie geometrie

Na konverziu geometrie je potrebné definovať počet rezov a zaškrtnúť políčko „Výstupná geometria“ (pozri obr. 44.1.7.). Keďže sa obrobok (deformovateľné typy objektov) mení pri každom kroku v dôsledku deformácie, jeho geometria sa zvyčajne nekonvertuje, preto je toto políčko pre obrobok štandardne odškrtnuté, ako je znázornené na obr. 44.1.6.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0006.jpg' | relative_url }})

Okno nastavení prevodu geometrie pre obrobok (osovo symetrický)

V prípade plných objektov musí byť typ geometrie nastavený na „Solid“ a v prípade dutých objektov musí používateľ zvoliť možnosť „Hollow“. V prípade konverzie 2D osovo symetrického nastavenia, ak je typ geometrie „Solid“ a súradnice uzlov symetrických hrán objektu sa nachádzajú v rámci tolerančného limitu od stredovej osi, systém túto medzeru ignoruje a vygeneruje 3D geometriu telesa; ak vzdialenosť prekročí tolerančný limit, systém túto medzeru zohľadní a v strede vygeneruje zakrivený povrch. Pri konverzii 3D modelov s uhlom otáčania menším ako 360° z 2D osovo symetrického modelu sa automaticky vygeneruje symetria typu BCC.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_preview_button.jpg' | relative_url }}), aby ste si prezreli náhľad geometrie, ako je znázornené na obr. 44.1.7.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0007.jpg' | relative_url }})

Nastavenia konverzie geometrie pre lisovacie formy (osovo symetrické)

V prípade 2D geometrie typu „rovinné deformácie/rovinné napätia“ bude používateľ mať k dispozícii iba možnosť geometrie s určitým počtom rezov v smere dĺžky extruzie, ako je znázornené na obrázku [Fig. 44.1.8.](44_1_2d_to_3d_converter.htm#Fig_44_1_8_Geometry_conversion_window_for_plane_strain/plane_stress)

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0008.jpg' | relative_url }})

Okno na prevod geometrických údajov pre rovinné deformácie/rovinné napätia

## Nastavenia konverzie siete

V prípade objektov so sieťou zapnite výstupnú sieť a vyberte typ siete. Zadajte počet 3D prvkov pre objekty so sieťou, ako je znázornené na obr. 44.1.9.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0009.jpg' | relative_url }})

Nastavenia konverzie mriežky

Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_advanced_button.jpg' | relative_url }}) slúži na priradenie rôznych parametrov 3D siete, ako je znázornené na obr. 44.1.10. Ďalšie informácie o všeobecných nastaveniach, váhových faktoroch, oknách siete, povrchovej úprave, kritériách pre vytvorenie novej siete a pokročilých nastaveniach tetraédrovej a tehličkovej/hexaédrovej siete nájdete v častiach [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) a [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/).

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0010.jpg' | relative_url }})

Pokročilé nastavenia sietí pre siete Tet a Brick

Ak používateľ nastaví prevod v interaktívnom režime po simulácii 2D operácie alebo samotný prevod ako prvú operáciu, tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) bude aktívne na prevod siete.

## Definícia materiálu

Používateľ môže vybrať nový materiál len pre obrobok a dokonca upraviť vlastnosti materiálu zaškrtnutím políčka „Vybrať nový materiál“, ako je znázornené na obr. 44.1.11.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0011.jpg' | relative_url }})

Nová možnosť výberu materiálu pre obrobok

## Okno „Prevod objektov“

V okne „Convert“ (Previesť) si môže používateľ overiť stav geometrie objektov, výber konverzie siete a samotný priebeh konverzie, ako je znázornené na obr. 44.1.12.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0012.jpg' | relative_url }})

Okno na konverziu objektov v hromadnom režime

V interaktívnom režime (po simulácii 2D operácie) alebo ak je samotný prevodník nastavený ako prvá operácia, budú aktívne ako začiarkavacie políčko „Vynútiť regeneráciu pre všetky objekty“, tak aj tlačidlo „Generovať“, takže používateľ môže začiarknutím tohto políčka vynútiť generovanie siete a geometrie všetkých objektov podľa výberu. Používateľ môže v interaktívnom režime previesť sieť a geometriu aj pre chýbajúci objekt pomocou tlačidla „Generovať“ bez zaškrtnutia tohto políčka.

Pri nastavení konvertora geometrie s 2D rovinným deformovaním v interaktívnom režime je stav okna konvertora taký, ako je znázornené na obr. 44.1.13. Na tomto obr. 44.1.13. sú siete obrobku a hornej matrice konvertované, ale sieť spodnej matrice nie je konvertovaná; ak chce používateľ konvertovať iba nekonvertované objekty, musí kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}). Všetky objekty je možné tiež vynútene previesť naraz zaškrtnutím políčka „Vynútiť regeneráciu pre všetky objekty“ a stlačením tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0013.jpg' | relative_url }})

Okno na konverziu objektov v interaktívnom režime

## Vytvoriť databázu

V dávkovom režime sa v okne na generovanie databázy zobrazí stav „Generovanie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu“, ako je znázornené na obr. 44.1.14.

V interaktívnom režime sa po simulácii 2D operácie alebo po samotnej prevádzke konvertora ako prvom prevádzkovom prípade aktivuje možnosť „Databáza“ a stav bude „Pripravené“. Ak v interaktívnom režime nie sú definované vstupné polia alebo objekty nie sú konvertované, stav bude „Chyba vstupu“.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0014.jpg' | relative_url }})

Okno na vytvorenie databázy pre prevodník pracujúci v dávkovom režime

## Pokračovať v nastavení 3D úlohy po spustení konvertora

Po nastavení operátora „2D to 3D Converter“ sú povolené iba 3D operácie, takže 3D operácia pridaná z prehliadača po operátore konvertora sa v editore operácií automaticky prepojí, ako je znázornené na obr. 44.1.15.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0015.jpg' | relative_url }})

Pridanie 3D operácie po prevode z 2D do 3D

V editore operácií vyberte 3D operáciu, aby ste mohli pokračovať v jej nastavení. Na základe tejto 3D operácie sa objekty automaticky prenesú z predchádzajúcej operácie. Keď vyberieme pridanú 3D formovaciu operáciu, všetky objekty sa prenesú z predchádzajúcej operácie, ako je znázornené na obr. 44.1.16.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0016.jpg' | relative_url }})

Pridali sme objekty do operácie 3D tvarovania

Funkcia „Convert“ neprevádza údaje objektov pohybu a vlastností ani údaje ovládacích prvkov simulácie, preto musí používateľ tieto údaje definovať v 3D operácii. V tomto príklade definujte pre hornú matricu rovnaké ovládacie prvky pohybu ako v prvej operácii, t. j. vyberte ovládacie prvky pohybu kladiva v smere -Z, ako je znázornené na obr. 44.1.17.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0017.jpg' | relative_url }})

Ovládacie prvky pohybu pre prácu s 3D objektom hornej matrice

Prejdite do okna naplánovaného umiestnenia, pridajte a definujte polohu kolízie obrobku voči spodnej matrici v smere -Z; podobne určte polohu kolízie hornej matrice voči obrobku v smere -Z, ako je znázornené na obr. 44.1.18. Ak používateľ nastavil konvertor v dávkovom režime, odporúča sa pridať naplánované polohovanie objektov po konverzii v 3D operácii. Rovnako ak používateľ pridal nové objekty v 3D operácii spolu s konvertovanými objektmi, je potrebné naplánované polohovanie.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0018.jpg' | relative_url }})

Plánovanie umiestnenia objektov

Nastavte predvolené vzťahy medzi kontaktmi a prejdite do časti „Simulačné ovládacie prvky“, kde nastavte ovládacie prvky krokov tak, ako v prvej operácii, ako je znázornené na obr. 44.1.19.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0019.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie

## Simulácia integrovaného 2D a 3D nastavenia

Po dokončení nastavenia úlohy odošlite projekt na spustenie v simulačnom režime MO a po dokončení 2D operácie sledujte kartu správ LOG, kde nájdete správy o konverzii z 2D do 3D. Obr. 44.1.20. znázorňuje správy o konverzii z 2D do 3D pre príklad vysvetlený v tejto príručke, ktorý sa týka konverzie jedného obrobku a dvoch tuhých objektov formy. Začiatok konverzie je označený riadkom správy „$BGN$“ a koniec procesu konverzie bude označený riadkom správy „$END$“. 

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0020.jpg' | relative_url }})

Správy protokolu o konverzii z 2D do 3D

## Uskutočnite následné spracovanie integrovaného 2D a 3D modelu v programe MO Post

V aplikácii MO Post môže používateľ prezerať integrovanú 2D a 3D databázu, výberom konkrétneho 2D alebo 3D pracovného kroku sa načítava príslušný krok v príslušnom režime a v konvertore z 2D na 3D bude k dispozícii iba negatívny krok, pri ktorom je k dispozícii konvertovaný 3D model, ako je znázornené na obr. 44.1.21.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0021.jpg' | relative_url }})

Pracovná pozícia operátora konvertora 2D na 3D v spoločnosti MO

Používateľ môže spustiť animáciu a vykresliť všetky stavové premenné a využiť ďalšie funkcie postprocesora dostupné v MO post. Ak chce mať viac možností, môže vybrať akčný štítok ![]({{ '/assets/icons/pre_icons/mo_post_label_link.jpg' | relative_url }}) a otvoriť databázu v postprocesore. Informácie o možnostiach postprocesora nájdete v [26\. Post Processor Features](/docs/en/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/).
