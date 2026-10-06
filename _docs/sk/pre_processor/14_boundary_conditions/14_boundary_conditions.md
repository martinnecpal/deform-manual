---
lang: sk
title: "14. Hraničné podmienky"
---

# 14\. Hraničné podmienky [BCC]

Hraničné podmienky určujú, ako hranica objektu interaguje s inými objektmi a s prostredím. Najčastejšie používanými okrajovými podmienkami sú výmena tepla s okolím pri simuláciách zahŕňajúcich prenos tepla, predpísaná rýchlosť na vynútenie symetrie alebo predpísanie pohybu v problémoch, ako je napríklad kreslenie, pri ktorom je diel pretiahnutý cez lisovací stroj, zmršťovacie prispôsobenie na modelovanie zmršťovacích krúžkov na nástrojoch, predpísaná sila na analýzu namáhania lisovacieho stroja a kontakt medzi objektmi v modeli. Niektoré definície okrajových podmienok boli zmenené z definície založenej na uzloch na definíciu založenú na hranách prvkov.

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_image001.jpg' | relative_url }})

(a)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_image002.jpg' | relative_url }})

(b)

Okno okrajovej podmienky objektu; (a) pre 2D (b) pre 3D

Účelom zmeny definície založenej na uzloch na definíciu založenú na hranách je znížiť nejednoznačnosť v rohoch. Ak je výmena tepla s prostredím definovaná na hrane a tepelný tok je na susednej hrane nastavený na nulu, v rohu vzniká nejednoznačnosť. Ak je rohový uzol nastavený na výmenu tepla s prostredím, potom definícia na hrane s jedným BC výmeny tepla a jedným BC tepelného toku nie je jednoznačne definovaná. Účelom definície na hrane je odstrániť tento problém vo všetkých prípadoch, keď okrajová podmienka pôsobí po celej dĺžke hrany prvku, ako je tlak, tepelný tok a difúzia atómov z prostredia.

**Definovanie okrajových podmienok objektu**

Hraničné podmienky sa zadávajú a vynucujú v uzloch alebo na okrajoch prvkov v sieti konečných prvkov. Základný postup nastavenia akejkoľvek okrajovej podmienky okrem podmienky Kontakt je rovnaký:

  1. Vyberte príslušný typ podmienky.
  2. Vyberte smer (ak je to vhodné).
  3. Vyberte uzly, na ktoré sa budú aplikovať okrajové podmienky, pomocou jedného z výberových nástrojov v ľavej dolnej lište tlačidiel (pozri obr. 14.1).
  4. Aplikujte okrajové podmienky

Vybrané uzly sa zvýraznia. Ak chcete použiť okrajové podmienky, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Farebnými značkami sa zvýraznia uzly, na ktoré boli aplikované okrajové podmienky. Ak chcete odstrániť konkrétne okrajové podmienky, vyberte počiatočné a koncové uzly a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}). Ak chcete odstrániť všetky okrajové podmienky zadaného typu a smeru, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}).

Poznámka :

Plochy povrchu môžete vybrať buď pomocou funkcie políčok povrchu, alebo pomocou tlačidla uzla vybrať jednotlivé uzly.

**Možnosti výberu pre 2D objekt sú:**

**Začiatočný a koncový bod **![]({{ '/assets/icons/pre_icons/mo_bcc_start_and_end_ico.jpg' | relative_url }}) : Výberom dvoch po sebe idúcich bodov, z ktorých prvý je začiatočný bod a druhý koncový bod, sa vyberie protichodná množina hraničných uzlov.

**By edge****![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }})** : Pomocou tejto možnosti sa na dvojrozmernom tvare vyberajú rôzne hrany. Ak je tvar dostatočne zakrivený, vyberie sa celá hrana.

**Po jednom**![]({{ '/assets/icons/pre_icons/mo_bcc_one_by_one_icon.jpg' | relative_url }}) : Kliknutím na túto ikonu vyberiete jednotlivé uzly.

**Okienko** : Nižšie sú uvedené možnosti 2D okien, ktoré sa používajú na výber oblasti definovaním okien.

Na výber oblasti BCC pre 2D sa používajú možnosti **Polygon**![]({{ '/assets/icons/pre_icons/mo_2d_polygon_window_icon.jpg' | relative_url }}) , **Obdĺžnik**![]({{ '/assets/icons/pre_icons/mo_2d_rectangle_window_icon.jpg' | relative_url }}) a **Kruh**![]({{ '/assets/icons/pre_icons/mo_2d_circle_window_icon.jpg' | relative_url }}) **[2D]**.

**Add****a****point**![]({{ '/assets/icons/pre_icons/mo_2d_add_point_button.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ pridať body na definovanie okna BCC.

**Delete****a****point**![]({{ '/assets/icons/pre_icons/mo_2d_delete_point_button.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ odstrániť body definovaného okna BCC.

**Premiestniť****bod**![]({{ '/assets/icons/pre_icons/mo_2d_relocate_point_button.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ premiestniť body definovaného okna BCC.

**Modify**![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ upraviť predtým definované okno BCC.

**Vybrať všetko**![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) : Kliknutím na túto ikonu sa vyberie každý uzol na hranici dielu.

**Zrušiť výber všetkých** :![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) Kliknutím na túto ikonu zrušíte výber každého uzla na hranici dielu.

**Možnosti výberu pre 3D objekt sú:**

**S******u** rface Patch **![]({{ '/assets/icons/pre_icons/mo_bcc_surface_patch_icon.jpg' | relative_url }}): Táto možnosť sa používa na výber povrchovej vrstvy objektu.

**Plane![]({{ '/assets/icons/pre_icons/mo_bcc_plane_icon.jpg' | relative_url }})** : Táto možnosť vyberá rovinu objektu.

**Po jednom** ![]({{ '/assets/icons/pre_icons/mo_bcc_one_by_one_icon.jpg' | relative_url }}): Kliknutím na túto ikonu vyberiete jednotlivé uzly.

**Okienko** : Nižšie uvedené možnosti Windows sa používajú na výber oblasti definovaním okien.

Na výber oblasti BCC pre 3D sa používajú možnosti **Box![]({{ '/assets/icons/pre_icons/mo_box_window_icon.jpg' | relative_url }})** , **Cylinder![]({{ '/assets/icons/pre_icons/mo_cylinder_window_icon.jpg' | relative_url }})** , **Ring![]({{ '/assets/icons/pre_icons/mo_hollow_cylinder_icon.jpg' | relative_url }}) **a **Polygon![]({{ '/assets/icons/pre_icons/mo_polygon_window_icon.jpg' | relative_url }}) [3D] **okno.

**Modify**![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ upraviť predtým definované okno BCC.

![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_toggle_button.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_assign_button.jpg' | relative_url }}) sú možnosti pridania, odstránenia, prepnutia a priradenia okna.

**Vybrať všetko**![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) : Kliknutím na túto ikonu sa vyberie každý uzol na hranici dielu.

**Zrušiť výber všetkých** :![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) Kliknutím na túto ikonu zrušíte výber každého uzla na hranici dielu.

Ak chcete použiť okrajové podmienky, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Farebné značky zvýraznia hrany, na ktoré boli aplikované okrajové podmienky. Ak chcete odstrániť konkrétne okrajové podmienky, vyberte počiatočné a koncové uzly a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}). Ak chcete odstrániť všetky okrajové podmienky zadaného typu a smeru, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}).

Poznámka:

Ak sa majú definovať rovnobežné roviny symetrie, okrajové podmienky rýchlosti sa môžu použiť len v jednej rovine. Na druhej rovine by mala byť definovaná pevná plocha.

**Hraničné podmienky** sú kategorizované ako**:

  * **Hraničné podmienky symetrie****[3D]** : kde sú pre 3D objekt k dispozícii možnosti Symmetry BCC. Ďalšie informácie týkajúce sa možností Symmetry Boundary conditions (Hraničné podmienky symetrie) nájdete v časti [14.1. Symmetry Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/' | relative_url }})
  * **Deformácia**Hraničné podmienky**[2D, 3D]**: kde sú k dispozícii možnosti Velocity BCC, Pressure BCC, Force BCC, Movement ****BCC, Contact BCC, Beginning surface****BCC, Free surface BCC, Rolling BCC a Advanced Deformation BCC. Ďalšie informácie týkajúce sa možností Deformation Boundary conditions******** nájdete v časti [14.2. Deformation Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/' | relative_url }})
  * **Termické** hraničné podmienky**[2D, 3D]**: kde sú k dispozícii možnosti výmeny tepla s prostredím BCC, teplota BCC, teplo BCC, tepelný tok BCC a rozšírené tepelné BCC. Ďalšie informácie týkajúce sa možností Thermal Boundary conditions (Tepelné okrajové podmienky) nájdete v časti [14.3. Thermal Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/' | relative_url }})
  * **Difúzia**Ohraničujúce podmienky**[2D, 3D]: **kde sú k dispozícii možnosti Difúzia s prostredím BCC, Obsah atómov BCC, Tok atómov BCC a Rozšírená difúzia BCC. Ďalšie informácie týkajúce sa možností Diffusion Boundary conditions (Hraničné podmienky difúzie) nájdete v časti [14.4. Diffusion Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/' | relative_url }})
  * **Vykurovanie** Hraničné podmienky** [2D, 3D]: **V tomto prípade sú k dispozícii možnosti Napätie BCC, Prúdový tok BCC, Obsah atómov BCC, Tok atómov BCC, Počiatočný povrch, Koncový povrch BCC a Vykurovací povrch BCC. Ďalšie informácie týkajúce sa možností Heating Boundary conditions (Hraničné podmienky ohrevu) nájdete v časti [14.5. Diffusion Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/' | relative_url }})

**Súvisiace témy:**

[14.1. Symmetry Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/' | relative_url }})

[14.2. Deformation Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/' | relative_url }})

[14.3. Thermal Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/' | relative_url }})

[14.4. Diffusion Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/' | relative_url }})

[14.5. Heating Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/' | relative_url }})

[2D-Geometry type selection from Simulation controls](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])
[Simulations modes selections from Simulation controls](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\))
[Process conditions selection from Simulation controls](../9_Simulation_Controls/9_6_Process_Conditions.htm#Process_Conditions)
[Object type selection from object data definition window](../11_General_Object_Data_Definition/11_General_Object_Data_Definition.htm#11.4._Object_type)
[Assigning movement to deformable objects with Movement BCC](14_2_deformation_boundary_conditions.htm#14.2.4._Movement_BCC)
[19\. Inter-object Data Definition]({{ '/docs/sk/pre_processor/20_Inter-object_Data_Definition/20_Inter-Object_Data_Definition/' | relative_url }})
[BCC- User routines -USRBCC](../../User_Routines/56_User_Routines_in_DEFORM/56_2_2D_User_Defined_FEM_Routines.htm#56_2_3_6_User_defined_nodal_boundary_conditions_\(USRBCC\))
[2D Labs]({{ '/docs/sk/Labs/Basic_labs/2D_Labs/2D_LABS/' | relative_url }})
[3D Labs]({{ '/docs/sk/Labs/Basic_labs/3D_Labs/3D_LABS/' | relative_url }})
