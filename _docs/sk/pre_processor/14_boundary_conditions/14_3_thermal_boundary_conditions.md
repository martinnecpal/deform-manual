---
lang: sk
title: "14.3. Tepelné okrajové podmienky"
---

# 14.3. Tepelné hraničné podmienky

14.3.1. Výmena tepla s okolím BCC
14.3.2. Teplota BCC
14.3.3. Tepelný tok BCC
14.3.4. Uzlové teplo BCC
14.3.5. Pokročilý tepelný BCC

## Výmena tepla s prostredím BCC [2D,3D]

Táto okrajová podmienka [ECCTMP](/docs/sk/Keyword_Documentation/E/ECCTMP/) určuje, že by malo dochádzať k výmene tepla medzi plochami prvkov ohraničenými týmito uzlami a ich okolím. Kontaktná okrajová podmienka určuje, či dôjde k výmene s okolitou atmosférou alebo s kontaktným objektom.

Štandardná výmena tepla s okolím prebieha s okolitým prostredím, ako je opísané vyššie. Okná výmeny tepla však možno zadať pomocou ikony okien výmeny tepla. Výmena tepla pre uzly v rámci týchto okien sa riadi parametrami nastavenými pre každé okno.

**Výmena okien**

Táto funkcia umožňuje používateľovi definovať podmienky výmeny tepla pre lokálne oblasti na telese pomocou trojrozmerného okna. Ak chcete použiť okná výmeny tepla, vykonajte nasledujúce činnosti:

  1. Prejdite do okna Okrajové podmienky.
  2. Vyberte kartu Thermal (Teplota).
  3. Vyberte tlačidlo Okná výmeny tepla.
  4. Všimnite si, že nástroje v ľavom hornom rohu okna displeja sa zmenia a objaví sa nové okno výmeny tepla.
  5. V tomto okne je možné definovať okná výmeny tepla pomocou nástrojov v ľavom hornom rohu zobrazovacieho okna. Každé okno má vlastnú lokálnu teplotu prostredia, koeficient konvekcie, tepelný tok a emisivitu. Pozri obr. 14.3.1. okna výmeny tepla.
  6. Touto metódou môžete definovať až 20 nezávislých okien. Ak dve oblasti zdieľajú rovnaký priestor, vyhráva okno s nižším číslom.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_3_Thermal_Boundary_Conditions/14_3_Image003.jpg)

(a)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_3_Thermal_Boundary_Conditions/14_3_Image001.jpg)

(b)

Výmena tepla s oknom prostredia; (a) pre 2D a (b) pre 3D

## Teplota BCC [2D, 3D]

Určuje pevnú teplotu v daných uzloch.

## Tepelný tok BCC [2D, 3D]

Toto ([ECHFLX](/docs/sk/Keyword_Documentation/E/ECHFLX/)) Určuje tok energie na jednotku plochy na ploche prvku ohraničenej uzlami. Jednotky sú energia/čas/plocha.

## Uzlové teplo BCC [2D, 3D]

Určuje zdroj tepla v daných uzloch. Jednotky sú energia/čas.

## Pokročilé tepelné BCC [2D, 3D]

Účelom tejto definície okrajových podmienok je umožniť používateľovi flexibilne špecifikovať všetky rôzne typy okrajových podmienok tepla na tej istej hrane. Používateľ môže zadať buď číslo používateľského podprogramu, alebo lokálnu definíciu prenosu tepla. (Pozri obr. 14.3.2.) Ak chce používateľ špecifikovať používateľskú rutinu, je potrebné zadať číslo používateľskej rutiny. Zadané číslo užívateľskej rutiny bude zodpovedať podrutine, ktorej bude zodpovedať okrajová podmienka. Ďalšie informácie o používaní týchto používateľských okrajových podmienok nájdete v časti User Routines (Používateľské rutiny). Ak číslo rutiny zostane nulové, používateľ potom môže definovať lokálne definovanú okrajovú podmienku, kde je potrebné určiť teplotu prostredia, koeficient konvekcie, emisivitu a tepelný tok okraj. Všetky tieto štyri premenné môžu byť definované ako konštanty alebo funkcie. Ak chcete použiť lokálnu okrajovú podmienku definovanú používateľom, nastavte požadované premenné, nastavte lokálne definované číslo na jedinečnú hodnotu a použite ju na sadu hrán prvkov. Nové kľúčové slová pre lokálne definovanie hrán sú [ECCDEF](/docs/sk/Keyword_Documentation/E/ECCDEF/), [ECTMFN](/docs/sk/Keyword_Documentation/E/ECTMFN/) a [LOCTMP](/docs/sk/Keyword_Documentation/L/LOCTMP/).

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_3_Thermal_Boundary_Conditions/14_3_Image002.jpg)

Pokročilé okno okrajovej podmienky tepelného objektu

**Súvisiace témy:**

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.2. Deformation Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)

[14.4. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)

[14.5. Heating Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)
