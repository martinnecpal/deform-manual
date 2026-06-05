---
lang: sk
title: "20. Definícia údajov medzi objektmi"
---

# 20. Definícia údajov medzi objektmi (Kontakt)

20.1. Kontaktný vzťah

20.2. Nástroje pre vzťahy medzi objektmi

Stránka s definíciou dát medzi objektmi je znázornená na obr. 20.1.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image001.jpg' | relative_url }})

(a) 2D stránka

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image004.jpg' | relative_url }})

b) 3D stránka

Okno definície dát medzi objektmi

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Tabuľka vzťahov zobrazuje aktuálne definované vzťahy medzi objektmi. Všetky objekty, ktoré môžu prísť do kontaktu v priebehu simulácie, musia mať definovaný kontaktný vzťah. To zahŕňa aj objekt, ktorý má vzťah sám so sebou, ak dochádza k vlastnému kontaktu. Je veľmi dôležité správne definovať tieto vzťahy, aby simulácia mohla presne modelovať proces formovania. Kľúčové premenné, ktoré je potrebné definovať medzi kontaktujúcimi sa objektmi, sú:

  * [Friction factor](20_1_friction_and_contact_criteria.htm#20_1_1_Friction_\(FRCFAC\))

  * [Interface heat transfer coefficient](20_2_interface_thermal_data.htm#20_2_1_Interface_heat_transfer_coefficient_\(IHTCOF\))

  * Kontaktný vzťah

  * [Separation criterion](20_1_friction_and_contact_criteria.htm#20_1_4_Separation_Type)

Súčasťou riadenia interakcií medzi objektmi je aj generovanie okrajových podmienok medzi objektmi.

Vzťahy medzi objektmi určujú, ktoré objekty môžu navzájom prichádzať do kontaktu a ako sa kontaktované objekty budú správať počas kontaktu. Pre každú dvojicu objektov sa tu nastavujú vzťahy kontaktu, okrajové podmienky medzi objektmi, trenie a prenos tepla (pozri obr. 20.1.). Zjednodušene povedané, postup definovania vzťahov medzi objektmi prebieha v nasledujúcich krokoch.

  * Určenie kombinácie hlavného a podriadeného objektu – Ak ide o jediný deformovaný objekt, tento objekt by mal byť vždy podriadeným objektom. Ak ide o viacero deformovaných telies, podriadeným objektom by mal byť ten objekt, ktorý má na rozhraní oboch objektov jemnejšiu sieť.

  * Nastavte parametre pre danú dvojicu master-slave – to môžete urobiť kliknutím na tlačidlo Upraviť a nastavením príslušných parametrov. (Pozri obr. 20.2 a obr. 20.3.)

  * Vytvorenie kontaktu pre všetky objekty – Najskôr kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}), čím sa vytvorí kontakt. Ak sa kontakt nevytvoril tam, kde ste očakávali, skontrolujte nasledujúce:

  * Orientácia geometrie tuhých objektov. Uistite sa, že geometria je vnútorná strana tuhých objektov vyplnená.

  * Rozloženie sietí v oblasti kontaktu. Ak je rozloženie sietí hrubé, v blízkosti miesta kontaktu sa nemusia nachádzať žiadne uzly.

  * Uistite sa, že sú tieto časti skutočne v tesnej blízkosti.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image002.jpg' | relative_url }})

Možnosti nastavenia konštanty šmykového trenia medzi objektmi v 2D

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image003.jpg' | relative_url }})

Možnosti nastavenia konštanty šmykového trenia medzi objektmi v 3D

## **Kontaktný vzťah (CNTACT)**

**[2D, 3D]:** Parameter vzťahu kontaktu ([CNTACT](/docs/sk/keyword_documentation/c/cntact/)) slúži na nastavenie vzťahu „hlavný/podriadený“ medzi obrobkom, formami a deformovateľnými telami. Podriadeným objektom by mal byť objekt s jemnejšou sieťou. V prípade dvoch objektov zložených z rovnakého materiálu môže byť podriadeným objektom ktorýkoľvek z nich, hoci objekt, u ktorého sa očakáva najväčšia elastická deformácia, by mal byť definovaný ako podriadený. Nastavenie vzťahu „Bez kontaktu“ spôsobí, že objekty budú pre seba navzájom neviditeľné a umožní im voľne sa navzájom prechádzať.

Pre každú dvojicu deformovateľných objektov, ktoré sa môžu počas simulácie dotýkať, je potrebné určiť vlastnosť CNTACT.

**Poznámka** :

Keď sa uzol jedného deformovateľného objektu dotkne povrchu iného deformovateľného objektu, je potrebné medzi týmito dvoma objektmi vytvoriť vzťah, aby sa zabránilo ich vzájomnému prenikaniu. Tento vzťah sa označuje ako vzťah „master-slave“ alebo „slave-master“. Keď sa dva objekty dotýkajú, kontaktné uzly sa pohybujú spolu s hlavným povrchom, pokiaľ sú oba objekty v kontakte. Podriadené uzly sa považujú za uzly v kontakte s hlavným objektom, pokiaľ uzlové sily indikujú tlakový stav. Keď v podriadenom uzle vznikne ťahová sila, uzol sa považuje za oddelený od hlavného objektu.

## Nástroje pre vzťahy medzi objektmi 

**Pridať predvolené vzťahy ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) **[2D, 3D]: Kliknutím na túto možnosť sa do zoznamu vzťahov kontaktov pridajú predvolené vzťahy kontaktov.

**Pridať vzťah**![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) [2D, 3D]: Kliknutím na túto možnosť sa do zoznamu pridá nový vzťah medzi kontaktmi

**Odstrániť**vzťah****![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) [2D, 3D]: Kliknutím na túto možnosť sa vybraný vzťah medzi kontaktmi odstráni zo zoznamu.

**Picking![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) [2D, 3D]: **Kliknutím na túto možnosť môže používateľ vybrať objekt, ktorý bude hlavným alebo podriadeným objektom.

****

**Použiť na všetky** ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) [2D, 3D]: Kliknutím na toto tlačidlo sa vybrané podmienky vzťahov, ako sú trenie a výmena tepla na rozhraní, uplatnia na všetky definované vzťahy medzi objektmi.

**Vymeniť**![]({{ '/assets/icons/pre_icons/mo_contact_swap_icon.jpg' | relative_url }}) [2D, 3D]: Kliknutím na toto tlačidlo sa vymenia pozície hlavného a podriadeného objektu. Hlavný objekt sa stane podriadeným a podriadený objekt sa stane hlavným.

**Vytvoriť** ![]({{ '/assets/icons/pre_icons/mo_generate_button.jpg' | relative_url }}) [2D, 3D]: Kliknutím na túto možnosť sa vytvorí kontakt len pre vybraný objektový vzťah.

**Podmienka priľnavosti** [2D, 3D]: Podmienky priľnavosti zabraňujú posuvu alebo oddeleniu medzi vybranou dvojicou objektov.

**Edit![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) **[2D, 3D]: Kliknutím na tlačidlo „Edit“ môže používateľ nastaviť koeficienty trenia a prenosu tepla cez rozhranie. 

**Vytvoriť všetko** ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) [2D, 3D]: Kliknutím na túto voľbu sa vytvoria kontakty pre všetky definované vzťahy medzi objektmi.

**Initialize![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}) **[2D, 3D]: Kliknutím na túto voľbu môže používateľ inicializovať definované kontakty.

**Obnoviť sieť**![]({{ '/assets/icons/pre_icons/mo_restore_mesh_button.jpg' | relative_url }}) [2D, 3D]: Obnoví sieť, ktorá existovala pred otvorením dialógového okna Inter-object

  
**Tolerancia**![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) [2D, 3D]: Kliknutím na toto tlačidlo systém použije predvolenú hodnotu tolerancie na vytvorenie kontaktov. Používateľ môže požadovanú hodnotu tolerancie na vytvorenie kontaktov nastaviť aj na karte „Tolerancia“.

**Preskúmať** ![]({{ '/assets/icons/pre_icons/mo_examine_button.jpg' | relative_url }}) [3D]: Od verzie V14.0 môže používateľ využiť možnosť Preskúmať na kontrolu kontaktov definovaných na stránke vzťahov medzi objektmi a na zobrazenie objektov v rozloženom pohľade. Kliknutím na toto tlačidlo sa otvorí okno, ako je znázornené na obr. 20.4. Na tejto stránke môžeme pozorovať kontaktné vzťahy každého objektu definovaného v tabuľke kontaktov. Ak nie sú kontaktné vzťahy definované v tabuľke, stránka Preskúmať bude vyzerať tak, ako je znázornené na obr. 20.5.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image005.jpg' | relative_url }})

Stránka na preskúmanie vzťahov medzi objektmi

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image006.jpg' | relative_url }})

Skontrolujte stránku, na ktorej nie je definovaný žiadny vzťah

Na stránke „Skúšky“ je definovaný stav vzťahu s kontaktom označený jednou z farieb: ![]({{ '/assets/icons/pre_icons/mo_good_object_color.jpg' | relative_url }}) (zelená), ![]({{ '/assets/icons/pre_icons/mo_candidate_object_color.jpg' | relative_url }}) (kandidát), ![]({{ '/assets/icons/pre_icons/mo_warning_object_color.jpg' | relative_url }}) (varovanie) a ![]({{ '/assets/icons/pre_icons/mo_floating_object_color.jpg' | relative_url }}) (neistý).

  * „![]({{ '/assets/icons/pre_icons/mo_good_object_color.jpg' | relative_url }})“ (Dobré) znamená, že bol definovaný vzťah so všetkými objektmi, s ktorými je v kontakte, a to v rámci objektov použitých v tabuľke medziobjektových vzťahov (pozri obr. 20.4.). 

  * „![]({{ '/assets/icons/pre_icons/mo_candidate_object_color.jpg' | relative_url }})“ (Kandidát) označuje, že objekt je v kontakte alebo môže prísť do kontaktu s niektorým z objektov definovaných v tabuľke vzťahov medzi objektmi, avšak vzťah kontaktu s príslušným objektom nie je definovaný (pozri obr. 20.6). Používateľ môže v prípade potreby pridať vzťah s príslušným objektom kliknutím pravým tlačidlom myši na podobjekt s farbou Kandidát, čím sa zobrazí tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_relationship_button.jpg' | relative_url }}) na pridanie vzťahu. 

  * „![]({{ '/assets/icons/pre_icons/mo_warning_object_color.jpg' | relative_url }})“ (Upozornenie) upozorňuje používateľa, že definovaný vzťah nemusí byť správny, keďže objekty sa nedotýkajú. Ak klikneme pravým tlačidlom myši na podobjekt označený farbou upozornenia, zobrazí sa tlačidlo ![]({{ '/assets/icons/pre_icons/mo_remove_relationship_button.jpg' | relative_url }}), ktorým môžeme tento vzťah odstrániť. 

  * „![]({{ '/assets/icons/pre_icons/mo_floating_object_color.jpg' | relative_url }})“ (voľný) – označuje, že objekt je voľný, pretože nemá žiadny vzťah s iným objektom, ale nachádza sa v strome objektov. Používateľ môže pridať vzťah v tabuľke medzi objektmi a potom použiť funkciu Preskúmať.

  
V nasledujúcom príklade sa snažíme pridať vzťah medzi položkami „Billet“ (objekt [1]) a „Bottom Die“ (objekt [3]) na stránke „Examine“.

  * Kliknite pravým tlačidlom na objekt „Bottom Die“ (object[3]) v zozname objektov pod objektom „Billet“ (object[1]).

  * Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_relationship_button.jpg' | relative_url }}).

  * V kontextovom okne „Pridať vzťah“ sa nachádzajú tlačidlá „Áno“, „Nie“ a „Zrušiť“. Ak klikneme na tlačidlo „**Áno**“, do tabuľky vzťahov medzi objektmi sa pridá nový vzťah s objektom 3 ako hlavným a objektom 1 ako podriadeným. Ak klikneme na tlačidlo „**Nie**“, do tabuľky vzťahov medzi objektmi sa pridá nový vzťah s objektom 3 ako podriadeným a objektom 1 ako nadradeným. Ak klikneme na tlačidlo „**Zrušiť**“, do tabuľky sa nepridá žiadny vzťah. (Pozri obr. 20.6.)

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image007.jpg' | relative_url }})

Pridanie možnosti vzťahu na stránke „Vyšetrenie“ 

V nasledujúcom príklade sme definovali kontaktný vzťah medzi „Podperou hornej matrice“ (Objekt[4]) ako hlavným objektom a „Sochárom“ (Objekt[1]) ako podriadeným objektom. Na stránke „Examine“ v zozname objektov „Billet“ pozorujeme objekt „Top die support“ s indikátorom „![]({{ '/assets/icons/pre_icons/mo_warning_object_color.jpg' | relative_url }})“, čo znamená, že objekty nie sú v kontakte a nemôžu prísť do kontaktu. Teraz sa pokúsime odstrániť tento vzťah zo stránky „Examination“.

  * Kliknite pravým tlačidlom myši na podobjekt „Top die support“ v zozname objektov polotovaru.

  * Potom kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_remove_relationship_button.jpg' | relative_url }})“.

  * V okienku „Odstrániť vzťah“ kliknite na tlačidlo „Áno“.

  * Vzťah medzi objektmi „Podpera hornej matrice“ a „Polotovar“ bol odstránený zo zoznamu vzťahov medzi objektmi. (Pozri obr. 20.7.)

  * Ak v okne „Odstrániť vzťah“ klikneme na tlačidlo „Nie“, v tabuľke vzťahov medzi objektmi nedôjde k žiadnej zmene. 

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image008.jpg' | relative_url }})

Odstránenie možnosti vzťahu zo stránky „Examination“

**Ovládací prvok rozloženého pohľadu [3D]**: Pomocou tejto možnosti môžeme zobraziť rozložený pohľad na objekty, ktoré sú momentálne zobrazené v zobrazovacej oblasti, a to posúvaním posuvníka pod ovládacím prvkom „Rozložený pohľad“, a tiež môžeme zmeniť vzťah hlavný-podriadený medzi objektmi. Keď potiahnete kurzor po posuvníku, objekty sa od seba vzdialia v smere rozloženia. Zapnutím tlačidla ![]({{ '/assets/icons/pre_icons/mo_contact_arrow_button.jpg' | relative_url }}) môžeme pozorovať šípku na objektoch v smere ich podriadených objektov, s ktorými majú kontaktný vzťah. Kliknutím na šípku v zobrazovacej oblasti môžeme zmeniť vzťah medzi objektmi.

V nasledujúcom príklade vidíme rozložený pohľad na 3D model „Spike“ so zobrazenými šípkami. Po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_contact_arrow_button.jpg' | relative_url }}) môžeme vidieť, že sa na hornej a spodnej matrici zobrazujú červené šípky, ktorých smer vedie k objektu „Billet“. Teraz kliknite na šípku hornej matrice, zobrazí sa okienko „Swap inter-Object Relationship“ (Vymeniť vzťah medzi objektmi), kliknite na tlačidlo „**Yes**“ (Áno), ako je znázornené na obr. 20.8.  

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image009.jpg' | relative_url }})

Kliknutím na šípku v hornej časti

  
Keď v kontextovom okne klikneme na tlačidlo „**Áno**“, smer šípky sa zmení z polotovaru smerom k hornej matrici a v tabuľke vzťahov sa vzťah „Horná matrica (Master) – Polotovar (slave)“ sa vzťah zmenil na „Polotovar (Master) – Horná matrica (slave)“, ako je znázornené na obr. 20.9.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_image010.png' | relative_url }})

Vzťah medzi objektmi po prepnutí pomocou šípky.  

**V oknách definície údajov medzi objektmi máme:**

  * **Karta Deformácia**: Na karte Deformácia môže používateľ nastaviť hodnoty trenia, kritériá kontaktu a kritériá oddelenia. Ďalšie informácie týkajúce sa možností na karte Deformácia nájdete v dokumente [20.1. Friction and Contact criteria](/docs/sk/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/).

  * **Karta „Thermal“**: Na karte „Thermal“ môže používateľ nastaviť údaje týkajúce sa koeficientu prenosu tepla a kritérií kontaktu (len pre 2D). Ďalšie informácie nájdete v [20.2. Interface Thermal Data.](/docs/sk/pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data/)

  * **Karta „Kúrenie“**: Na karte „Kúrenie“ môže používateľ zadať údaje o mernom odpore rozhrania. Ďalšie informácie nájdete v dokumente [20.3. Interface Resisitivity.](/docs/sk/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/)

  * **Karta „Friction Window“**: Karta „Friction Window“ umožňuje používateľovi nastaviť rôzne hodnoty koeficientu trenia pre rôzne kontaktné oblasti v rámci jednej dvojice objektov. Ďalšie informácie nájdete v dokumente [20.1. Friction and Contact criteria](/docs/sk/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/).

  * **Karta Opotrebenie nástroja******: Na karte Opotrebenie nástroja môže používateľ definovať model pre výpočet opotrebenia nástroja pri kontakte s iným objektom. Ďalšie informácie nájdete v [20.4. Tool Wear.](/docs/sk/pre_processor/20_inter-object_data_definition/20_4_tool_wear/)

  * **Karta „Rigid Contact“**: Na karte „Rigid Contact“ môže používateľ definovať referenčné body pre tuhé výsekové formy, aby sa zabránilo ich vzájomnému preniknutiu pri kontakte. Ďalšie informácie nájdete v dokumente [20.5. Rigid Contact.](/docs/sk/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/)

**Súvisiace témy:**

[20.1. Friction and Contact criteria](/docs/sk/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/)

[20.2. Interface Thermal Data](/docs/sk/pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data/)

[20.3. Interface Resisitivity](/docs/sk/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/)

[20.4. Tool Wear](/docs/sk/pre_processor/20_inter-object_data_definition/20_4_tool_wear/)

[20.5. Rigid Contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/)

([Simulation modes selection](../9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\))

[Environment process conditions settings](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)

[DEFORM object types](../11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type)

[Contact Boundary condition](../14_boundary_conditions/14_2_deformation_boundary_conditions.htm#14.2.6._Contact)

[2D Tool Wear Lab](/docs/sk/applications/55_applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/)

[2D Inertia weld simulation](/docs/sk/applications/55_applications/55_inertia_welding/2d_inertia_welding/)
