---
lang: sk
title: "10. Údaje o materiáloch"
---

# 10\. Údaje o materiáli

Okno s vlastnosťami materiálu je prístupné po kliknutí na zoznam materiálov (pozri obr. 10.1.).

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image001.jpg' | relative_url }})

Stránka so zoznamom materiálov v operačnom strome

Dialógové okno vlastností materiálu je znázornené na obr. 10.2. Aby simulácia dosiahla vysokú úroveň presnosti, je dôležité mať prehľad o vlastnostiach materiálu potrebných na špecifikáciu materiálu použitého v programe DEFORM. Požadované vlastnosti závisia od fyzikálnych javov, ktoré sa v programe DEFORM simulujú. Vlastnosti materiálu, ktoré musí používateľ špecifikovať, sú funkciou typov materiálov, ktoré používateľ využíva v simulácii. V tejto časti sú opísané údaje o materiáli, ktoré možno špecifikovať pre simuláciu v programe DEFORM.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image002.jpg' | relative_url }})

Stránka Vlastnosti materiálu

**Rôzne súbory údajov sú:**

  * [Plastic Data Definition](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_plastic_data/)
  * [Elastic Data Definition](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data/)
  * [Thermal Data Definition](/docs/sk/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/)
  * [Diffusion Data Definition](/docs/sk/pre_processor/10_material_data/10_4_diffusion_data/10_4_diffusion_data/)
  * Definícia údajov o dislokácii
  * [Grain Data Definition](/docs/sk/pre_processor/10_material_data/10_6_grain_data/10_6_grain_data/)
  * [Hardness Data Definition](/docs/sk/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/)
  * [Elec/ Mag Data Definition](/docs/sk/pre_processor/10_material_data/10_8_elec_mag_data/10_8_elec_mag_data/)
  * [Transformation Definition](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/)
  * Hrubšie definovanie údajov
  * Definícia údajov o textúre
  * [Miscellaneous Data Definition](/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_miscellaneous_data/)

V tejto kapitole je opísaný spôsob definovania jednotlivých súborov údajov a typ simulácie, pre ktorú je každý z nich potrebný.

Knižnica materiálov DEFORM obsahuje niekoľko stoviek súborov údajov. Takmer všetky materiály obsahujú plastické (napätie pri prúdení), elastické a tepelné údaje. V závislosti od zamýšľanej aplikácie môžu materiálové údaje obsahovať aj údaje týkajúce sa mikroštruktúry.

Používateľ by mal potvrdiť, že materiál vybraný z knižnice je vhodný pre proces, ktorý má v úmysle modelovať.

**Fázy a zmesi (MSTMTR) [MIC]**
Skupiny materiálov možno rozdeliť do dvoch kategórií: bežné a zmiešané. "Bežné" materiály sú vhodné na modelovanie väčšiny operácií spracovania kovov vrátane väčšiny problémov tvárnenia, rezania alebo analýzy napätia. "Zmesové" materiály ([MSTMTR](/docs/sk/keyword_documentation/m/mstmtr/)) sa používajú, ak sa má pri simulácii modelovať fázová premena. Transformujúci sa materiál sa modeluje ako "zmes" svojich zložiek - fáz. Napríklad uhlíková oceľ sa môže modelovať ako zmes austenitu, perlitu, bainitu a martenzitu. Ak je definovaný materiál zmesi, mali by sa definovať transformačné pravidlá, ktorými sa riadi transformácia jednej fázy na druhú.

**Viacfázové:** Ak chceme pridať viac fáz, musíme zaškrtnúť políčko Mixture material check (Kontrola materiálu zmesi), ako je znázornené na nasledujúcom obrázku 10.3. Pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_add_phase_button.jpg' | relative_url }}) môžeme pridať nové fázy a pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_remove_phase_button.jpg' | relative_url }}) môžeme pridané fázy z materiálu odstrániť.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image005.jpg' | relative_url }})

Pridanie fázy pre materiál zmesi

**Vytvoriť nový materiál** ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})**** slúži na definovanie nového materiálu, po výbere tohto tlačidla sa nový materiál pridá do zoznamu materiálov. Dvojklikom ľavého tlačidla myši v zozname materiálov je možné názov materiálu premenovať a jeho vlastnosti je potrebné definovať v príslušných záložkách (popísané v ďalších častiach ako Plastic data (Plastické údaje), Elastic data (Pružné údaje) atď.

**Delete Current Materia****l**![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }})** **vymaže aktuálny materiál vybraný v zozname materiálov.

**Import materiálu zo súboru** ****![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})**** sa používa na import údajov o materiáli z DB alebo súboru s kľúčom do problémového nastavenia.

**Načítať materiál z knižnice** **![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})** Pomocou tejto funkcie môže používateľ načítať materiál z databázy materiálov DEFORM. (Pozri obr. 10.4.) Na základe aplikácie môže používateľ vybrať zaškrtávacie políčka Tvarovanie za studena, Tvarovanie za tepla, Tepelné spracovanie a Obrábacie operácie. Výber materiálu uľahčia aj ďalšie filtre, ako je norma materiálu, systém jednotiek a knižnica používateľa/systému.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image003.jpg' | relative_url }})

Načítanie materiálu z okna knižnice

**Uloženie údajov o materiáli do súboru**![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }})****slúži na uloženie údajov o materiáli z nastavenia problému DEFORM vo formáte kľúčového súboru. Tieto údaje o materiáli možno použiť pri spätnom importe do iných nastavení problému.

**S****ave Material data to library![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }})** sa používa na uloženie používateľom definovaného materiálu do používateľskej knižnice deformácií. Pri ukladaní do používateľ musí uložiť pod niektorú kategóriu a môže tiež uviesť filtre založené na aplikácii a komentáre (pozri obr. 10.5.).

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image004.jpg' | relative_url }})

Uloženie materiálu v okne Knižnica používateľských materiálov

**Kopírovanie vlastností** ![]({{ '/assets/icons/pre_icons/mo_copy_properties.jpg' | relative_url }}) sa používa na kopírovanie bežných materiálových vlastností, ako sú plastické, elastické, tepelné atď., z jedného materiálu do druhého pri vytváraní/definovaní materiálových údajov. (Pozri obr. 10.6.) V tomto dialógovom okne sa musí vybrať zdroj a cieľ kopírovania vlastností a ktoré vlastnosti sa majú kopírovať.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image006.jpg' | relative_url }})

Kopírovanie okna vlastností

**Konvertovať jednotky** ![]({{ '/assets/icons/pre_icons/mo_convert_units_button.jpg' | relative_url }}) sa používa na konverziu aktuálne vybraného materiálu zo zoznamu materiálov zo SI na angličtinu alebo z angličtiny na SI alebo používateľ môže použiť akýkoľvek iný násobiaci faktor. (Pozri obr. 10.7.) Výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) sa zobrazia násobiace koeficienty pre prevod zo SI na angličtinu, podobne pre ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}), výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_convert_button.jpg' | relative_url }}) sa vykoná prevod a zatvorí sa okno prevodu. Túto konverznú tabuľku možno uložiť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save.._button.jpg' | relative_url }}) a možno ju tiež upraviť pomocou wordpadu/notepadu a načítať späť súbor **UNITCONV.DAT** pomocou tlačidla.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image007.jpg' | relative_url }})

Okno konvertora materiálových jednotiek

**Priradenie materiálu pre objekt**

Na nasledujúcom obr. 10.8 je zobrazené okno materiálu. Používateľ môže priradiť požadovaný materiál zo zoznamu alebo ho môže importovať a uložiť zo súboru alebo knižnice. Používateľ môže tiež pridať nový materiál, dokonca môže upravovať a odstraňovať materiál v zozname z okna materiálu objektu.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image008.jpg' | relative_url }})

Okno materiálu

Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}), otvorí sa okno materiálu, ako je znázornené na obr. 10.9.

![]({{ '/assets/images/pre-processor/10_material_data/10_material_data/10_image009.jpg' | relative_url }})

Okno Úprava materiálu

Súvisiace témy:

[10.1. Plastic Data Definition](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_plastic_data/)

[10.2. Elastic Data Definition](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data/)

[10.3. Thermal Data Definition](/docs/sk/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/)

[10.4. Diffusion Data Definition](/docs/sk/pre_processor/10_material_data/10_4_diffusion_data/10_4_diffusion_data/)

10.5. Definícia údajov o dislokácii

[10.6. Grain Data Definition](/docs/sk/pre_processor/10_material_data/10_6_grain_data/10_6_grain_data/)

[10.7. Hardness Data Definition](/docs/sk/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/)

[10.8. Elec/ Mag Data Definition](/docs/sk/pre_processor/10_material_data/10_8_elec_mag_data/10_8_elec_mag_data/)

[10.9 Transformation Data Definition](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/)

10.10. Definícia hrubých údajov

10.11. Definícia údajov o textúre

[10.12. Miscellaneous Data Definition](/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_miscellaneous_data/)
