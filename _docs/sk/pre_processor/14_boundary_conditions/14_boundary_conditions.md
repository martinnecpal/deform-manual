---
lang: sk
title: "14. Hraničné podmienky"
---

# 14\. Hraničné podmienky [BCC]

Hraničné podmienky určujú, ako hranica objektu interaguje s inými objektmi a s prostredím. Najčastejšie používanými okrajovými podmienkami sú výmena tepla s okolím pri simuláciách zahŕňajúcich prenos tepla, predpísaná rýchlosť na vynútenie symetrie alebo predpísanie pohybu v problémoch, ako je napríklad kreslenie, pri ktorom je diel pretiahnutý cez lisovací stroj, zmršťovacie prispôsobenie na modelovanie zmršťovacích krúžkov na nástrojoch, predpísaná sila na analýzu namáhania lisovacieho stroja a kontakt medzi objektmi v modeli. Niektoré definície okrajových podmienok boli zmenené z definície založenej na uzloch na definíciu založenú na hranách prvkov.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_Image001.jpg)

(a)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_Image002.jpg)

(b)

Okno okrajovej podmienky objektu; (a) pre 2D (b) pre 3D

Účelom zmeny definície založenej na uzloch na definíciu založenú na hranách je znížiť nejednoznačnosť v rohoch. Ak je výmena tepla s prostredím definovaná na hrane a tepelný tok je na susednej hrane nastavený na nulu, v rohu vzniká nejednoznačnosť. Ak je rohový uzol nastavený na výmenu tepla s prostredím, potom definícia na hrane s jedným BC výmeny tepla a jedným BC tepelného toku nie je jednoznačne definovaná. Účelom definície na hrane je odstrániť tento problém vo všetkých prípadoch, keď okrajová podmienka pôsobí po celej dĺžke hrany prvku, ako je tlak, tepelný tok a difúzia atómov z prostredia.

**Definovanie okrajových podmienok objektu**

Hraničné podmienky sa zadávajú a vynucujú v uzloch alebo na okrajoch prvkov v sieti konečných prvkov. Základný postup nastavenia akejkoľvek okrajovej podmienky okrem podmienky Kontakt je rovnaký:

  1. Vyberte príslušný typ podmienky.
  2. Vyberte smer (ak je to vhodné).
  3. Vyberte uzly, na ktoré sa budú aplikovať okrajové podmienky, pomocou jedného z výberových nástrojov v ľavej dolnej lište tlačidiel (pozri obr. 14.1).
  4. Aplikujte okrajové podmienky

Vybrané uzly sa zvýraznia. Ak chcete použiť okrajové podmienky, kliknite na tlačidlo ![](../../../assets/Icons/Pre_icons/MO_Add_BCC_button.jpg). Farebnými značkami sa zvýraznia uzly, na ktoré boli aplikované okrajové podmienky. Ak chcete odstrániť konkrétne okrajové podmienky, vyberte počiatočné a koncové uzly a kliknite na tlačidlo ![](../../../assets/Icons/Pre_icons/MO_delete_BCC_button.jpg). Ak chcete odstrániť všetky okrajové podmienky zadaného typu a smeru, kliknite na tlačidlo ![](../../../assets/Icons/Pre_icons/MO_initialize_button.jpg).

Poznámka :

Plochy povrchu môžete vybrať buď pomocou funkcie políčok povrchu, alebo pomocou tlačidla uzla vybrať jednotlivé uzly.

**Možnosti výberu pre 2D objekt sú:**

**Začiatočný a koncový bod **![](../../../assets/Icons/Pre_icons/MO_Bcc_start_and_end_ico.jpg) : Výberom dvoch po sebe idúcich bodov, z ktorých prvý je začiatočný bod a druhý koncový bod, sa vyberie protichodná množina hraničných uzlov.

**By edge****![](../../../assets/Icons/Pre_icons/MO_Bcc_edge_icon.jpg)** : Pomocou tejto možnosti sa na dvojrozmernom tvare vyberajú rôzne hrany. Ak je tvar dostatočne zakrivený, vyberie sa celá hrana.

**Po jednom**![](../../../assets/Icons/Pre_icons/MO_Bcc_one_by_one_icon.jpg) : Kliknutím na túto ikonu vyberiete jednotlivé uzly.

**Okienko** : Nižšie sú uvedené možnosti 2D okien, ktoré sa používajú na výber oblasti definovaním okien.

Na výber oblasti BCC pre 2D sa používajú možnosti **Polygon**![](../../../assets/Icons/Pre_icons/MO_2D_Polygon_Window_icon.jpg) , **Obdĺžnik**![](../../../assets/Icons/Pre_icons/MO_2D_Rectangle_Window_icon.jpg) a **Kruh**![](../../../assets/Icons/Pre_icons/MO_2D_Circle_Window_icon.jpg) **[2D]**.

**Add****a****point**![](../../../assets/Icons/Pre_icons/MO_2D_Add_point_button.jpg) : Pomocou tejto možnosti môže používateľ pridať body na definovanie okna BCC.

**Delete****a****point**![](../../../assets/Icons/Pre_icons/MO_2D_Delete_point_button.jpg) : Pomocou tejto možnosti môže používateľ odstrániť body definovaného okna BCC.

**Premiestniť****bod**![](../../../assets/Icons/Pre_icons/MO_2D_Relocate_point_button.jpg) : Pomocou tejto možnosti môže používateľ premiestniť body definovaného okna BCC.

**Modify**![](../../../assets/Icons/Pre_icons/MO_Edit_window_icon.jpg) : Pomocou tejto možnosti môže používateľ upraviť predtým definované okno BCC.

**Vybrať všetko**![](../../../assets/Icons/Pre_icons/MO_Select_all_icon.jpg) : Kliknutím na túto ikonu sa vyberie každý uzol na hranici dielu.

**Zrušiť výber všetkých** :![](../../../assets/Icons/Pre_icons/MO_clear_icon.jpg) Kliknutím na túto ikonu zrušíte výber každého uzla na hranici dielu.

**Možnosti výberu pre 3D objekt sú:**

**S******u** rface Patch **![](../../../assets/Icons/Pre_icons/MO_Bcc_surface_patch_icon.jpg): Táto možnosť sa používa na výber povrchovej vrstvy objektu.

**Plane![](../../../assets/Icons/Pre_icons/MO_Bcc_plane_icon.jpg)** : Táto možnosť vyberá rovinu objektu.

**Po jednom** ![](../../../assets/Icons/Pre_icons/MO_Bcc_one_by_one_icon.jpg): Kliknutím na túto ikonu vyberiete jednotlivé uzly.

**Okienko** : Nižšie uvedené možnosti Windows sa používajú na výber oblasti definovaním okien.

Na výber oblasti BCC pre 3D sa používajú možnosti **Box![](../../../assets/Icons/Pre_icons/MO_Box_window_icon.jpg)** , **Cylinder![](../../../assets/Icons/Pre_icons/MO_Cylinder_window_icon.jpg)** , **Ring![](../../../assets/Icons/Pre_icons/MO_Hollow_Cylinder_icon.jpg) **a **Polygon![](../../../assets/Icons/Pre_icons/MO_Polygon_window_icon.jpg) [3D] **okno.

**Modify**![](../../../assets/Icons/Pre_icons/MO_Edit_window_icon.jpg) : Pomocou tejto možnosti môže používateľ upraviť predtým definované okno BCC.

![](../../../assets/Icons/Pre_icons/MO_Add_icon.jpg), ![](../../../assets/Icons/Pre_icons/MO_Delete_icon.jpg), ![](../../../assets/Icons/Pre_icons/MO_Toggle_button.jpg), ![](../../../assets/Icons/Pre_icons/MO_Assign_button.jpg) sú možnosti pridania, odstránenia, prepnutia a priradenia okna.

**Vybrať všetko**![](../../../assets/Icons/Pre_icons/MO_Select_all_icon.jpg) : Kliknutím na túto ikonu sa vyberie každý uzol na hranici dielu.

**Zrušiť výber všetkých** :![](../../../assets/Icons/Pre_icons/MO_clear_icon.jpg) Kliknutím na túto ikonu zrušíte výber každého uzla na hranici dielu.

Ak chcete použiť okrajové podmienky, kliknite na tlačidlo ![](../../../assets/Icons/Pre_icons/MO_Add_BCC_button.jpg). Farebné značky zvýraznia hrany, na ktoré boli aplikované okrajové podmienky. Ak chcete odstrániť konkrétne okrajové podmienky, vyberte počiatočné a koncové uzly a kliknite na tlačidlo ![](../../../assets/Icons/Pre_icons/MO_delete_BCC_button.jpg). Ak chcete odstrániť všetky okrajové podmienky zadaného typu a smeru, kliknite na tlačidlo ![](../../../assets/Icons/Pre_icons/MO_initialize_button.jpg).

Poznámka:

Ak sa majú definovať rovnobežné roviny symetrie, okrajové podmienky rýchlosti sa môžu použiť len v jednej rovine. Na druhej rovine by mala byť definovaná pevná plocha.

**Hraničné podmienky** sú kategorizované ako**:

  * **Hraničné podmienky symetrie****[3D]** : kde sú pre 3D objekt k dispozícii možnosti Symmetry BCC. Ďalšie informácie týkajúce sa možností Symmetry Boundary conditions (Hraničné podmienky symetrie) nájdete v časti [14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)
  * **Deformácia**Hraničné podmienky**[2D, 3D]**: kde sú k dispozícii možnosti Velocity BCC, Pressure BCC, Force BCC, Movement ****BCC, Contact BCC, Beginning surface****BCC, Free surface BCC, Rolling BCC a Advanced Deformation BCC. Ďalšie informácie týkajúce sa možností Deformation Boundary conditions******** nájdete v časti [14.2. Deformation Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)
  * **Termické** hraničné podmienky**[2D, 3D]**: kde sú k dispozícii možnosti výmeny tepla s prostredím BCC, teplota BCC, teplo BCC, tepelný tok BCC a rozšírené tepelné BCC. Ďalšie informácie týkajúce sa možností Thermal Boundary conditions (Tepelné okrajové podmienky) nájdete v časti [14.3. Thermal Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)
  * **Difúzia**Ohraničujúce podmienky**[2D, 3D]: **kde sú k dispozícii možnosti Difúzia s prostredím BCC, Obsah atómov BCC, Tok atómov BCC a Rozšírená difúzia BCC. Ďalšie informácie týkajúce sa možností Diffusion Boundary conditions (Hraničné podmienky difúzie) nájdete v časti [14.4. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)
  * **Vykurovanie** Hraničné podmienky** [2D, 3D]: **V tomto prípade sú k dispozícii možnosti Napätie BCC, Prúdový tok BCC, Obsah atómov BCC, Tok atómov BCC, Počiatočný povrch, Koncový povrch BCC a Vykurovací povrch BCC. Ďalšie informácie týkajúce sa možností Heating Boundary conditions (Hraničné podmienky ohrevu) nájdete v časti [14.5. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)

**Súvisiace témy:**

[14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.2. Deformation Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)

[14.3. Thermal Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)

[14.4. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)

[14.5. Heating Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)

[2D-Geometry type selection from Simulation controls](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])
[Simulations modes selections from Simulation controls](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\))
[Process conditions selection from Simulation controls](../9_Simulation_Controls/9_6_Process_Conditions.htm#Process_Conditions)
[Object type selection from object data definition window](../11_General_Object_Data_Definition/11_General_Object_Data_Definition.htm#11.4._Object_type)
[Assigning movement to deformable objects with Movement BCC](14_2_deformation_boundary_conditions.htm#14.2.4._Movement_BCC)
[19\. Inter-object Data Definition](/docs/sk/pre_processor/20_Inter-object_Data_Definition/20_Inter-Object_Data_Definition/)
[BCC- User routines -USRBCC](../../User_Routines/56_User_Routines_in_DEFORM/56_2_2D_User_Defined_FEM_Routines.htm#56_2_3_6_User_defined_nodal_boundary_conditions_\(USRBCC\))
[2D Labs](/docs/sk/Labs/Basic_labs/2D_Labs/2D_LABS/)
[3D Labs](/docs/sk/Labs/Basic_labs/3D_Labs/3D_LABS/)
