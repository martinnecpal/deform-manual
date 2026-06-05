---
lang: sk
title: "14.2. Hraničné podmienky deformácie"
---

# 14.2. Deformačné hraničné podmienky

14.2.1. Rýchlosť BCC

  * Bezplatné skreslenie BCC

14.2.2. Tlak BCC

14.2.3. Vynútiť BCC

14.2.4. Pohyb BCC

14.2.5. Zmenšenie BCC

14.2.6. Kontakt na spoločnosť BCC

14.2.7. Začiatok povrchu BCC

14.2.8. Voľný povrch BCC

14.2.9. Rolling BCC

14.2.10. Pokročilá deformácia BCC

## Rýchlosť BCC [2D, 3D]

[2D]: Rýchlosť každého uzla možno určiť nezávisle v smeroch X a Y. Okrajové podmienky rýchlosti sú zvyčajne nastavené na nulu pre podmienky symetrie, ale môžu byť nastavené aj na zadanú nenulovú hodnotu pre procesy, ako je napríklad ťahanie, pri ktorom sa obrobok ťahá cez matricu. (Pozri obr. 14.2.1.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image001.jpg)

2D okno rýchlosti BCC

[3D]: Rýchlosť každého uzla možno určiť nezávisle v smeroch X, Y a Z. Okrajové podmienky rýchlosti sú zvyčajne nastavené na nulu pre podmienky symetrie (Symmetry BCC [3D]), ale môžu byť nastavené aj na zadanú nenulovú hodnotu pre procesy, ako je kreslenie, pri ktorom sa obrobok ťahá cez matricu.

Dokonca môžeme definovať rýchlosť BCC pomocou možnosti Všetky smery pre 2D aj 3D, pomocou tejto možnosti môže používateľ priradiť BCC pre všetky smery naraz.

Poznámka:

Ak sa majú definovať rovnobežné roviny symetrie, okrajové podmienky rýchlosti sa môžu použiť len v jednej rovine. Na druhej rovine by mala byť definovaná pevná plocha.

**Voľné skreslenie BCC****[3D]**

Okno voľného skreslenia je prístupné z okna rýchlosti BCC. (Pozri obr. 14.2.2.) Okrajová podmienka voľného skreslenia sa aplikuje tam, kde existuje možnosť vzniku maximálneho skreslenia.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image002.jpg)

Okno BCC s voľným skreslením

**Postup pri použití okrajovej podmienky voľného skreslenia:**

  1. Upevnite jeden uzol v smere X, Y a Z. Tým sa odstránia tri stupne voľnosti pri translácii.
  2. Nájdite bod s rovnakou hodnotou X a Z, ale s rôznou hodnotou Y - zafixujte ho v smere Z - rotácia X.
  3. Nájdite bod s rovnakou hodnotou Y a X, ale s inou hodnotou Z - zafixujte ho v smere X - otočenie Y.
  4. Nájdite bod s rovnakou hodnotou Z a Y, ale s inou hodnotou X - zafixujte ho v smere Y - otočenie Z (pozri obr. 14.2.3.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image003.jpg)

Upevnenie uzlov v smere X, Y a Z

Typický príklad, ktorý ukazuje, ako definovať voľné skreslenie BCC:

  1. Používateľ vyberie uzol, ktorý sa má zafixovať v smeroch X, Y, Z, ako je znázornené na obr. 14.2.4.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image004.jpg)

Výber uzla, ktorý sa má upevniť v smere XYZ

  1. Systém navrhne uzol na fixáciu v smere Z. Navrhnutý uzol má minimálny uhol k osi Y a je najvzdialenejší od pevného uzla XYZ. (Pozri obr. 14.2.5.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image005.jpg)

Výber uzla, ktorý sa má upevniť v smere Z

  1. Systém navrhne uzol na fixáciu v smere X. Navrhnutý uzol má minimálny uhol k osi Z a je najvzdialenejší od pevného uzla XYZ. (Pozri obr. 14.2.6.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image006.jpg)

Výber uzla, ktorý sa má upevniť v smere X

  1. Systém navrhne uzol na fixáciu v smere Y. Navrhnutý uzol má minimálny uhol k osi X a je najvzdialenejší od pevného uzla XYZ. Pri fixácii uzlov X, Y, Z sa môže použiť aj vstup používateľa. (Pozri obr. 14.2.7.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image007.jpg)

Výber uzla, ktorý sa má zafixovať v smere Y

Definované voľné skreslenie BCC je znázornené na obr. 14.2.8,

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image008.jpg)

Definované voľné skreslenie BCC

## Tlak BCC [2D, 3D]

**[2D]** : Tlakové okrajové podmienky určujú rovnomernú alebo lineárne sa meniacu silu na jednotku plochy na plochách prvkov spájajúcich zadané hrany. Požadujú sa dve hodnoty normálového tlaku, prvá hodnota je počiatočná hodnota tlaku z počiatočného bodu, kde je tlak zadaný, druhá hodnota je hodnota na konci miesta, kde je tlak zadaný. Tlak sa lineárne interpoluje medzi začiatkom a koncom. Kľúčové slová pre tlak sú [ECCDEF](/docs/sk/Keyword_Documentation/E/ECCDEF/) a [ECPRES](/docs/sk/Keyword_Documentation/E/ECPRES/). Používateľ môže definovať okno Pressure (Tlak), ako je znázornené na obr. 14.2.9.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image009.jpg)

(a)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image010.jpg)

(b)

2D definícia tlakového okna; a) pre 2D b) tlakové okno

**[3D]** : Tlakové okrajové podmienky určujú rovnomernú alebo lineárne sa meniacu silu na jednotku plochy na plochách prvkov spájajúcich zadané uzly. Ďalšie informácie o tom, ako definovať BCC s voľnou deformáciou, nájdete v časti BCC s voľnou deformáciou [ 3D].

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image011.jpg)

Definícia 3D tlakového okna

## Force BCC [2D, 3D]

Silové okrajové podmienky určujú silu pôsobiacu na každý uzol. Sila je zadaná v predvolených jednotkách. Pri analýze namáhania matrice možno silu, ktorou matrica pôsobí na obrobok, obrátiť a interpolovať na matrice pomocou interpolačnej funkcie.

**Kroky na definovanie interpolácie sily:**

  1. Kliknutím na tlačidlo ![](../../../assets/Icons/Pre_icons/MO_Interpolate_button.jpg) sa zobrazí okno podľa obr. 14.2.11.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image012.jpg)

Interpolácia databázy Widow

  1. Kliknutím na ![](../../../assets/Icons/Pre_icons/MO_Browse_button.jpg) vyberte krok z načítanej DB, pri ktorom sa má vykonať interpolácia síl. (Pozri obr. 14.2.12.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image013.jpg)

Interpolácia databázy Widow zobrazujúca výber čísla kroku

  1. Vo vyskakovacom okne vyberte objekt obrobku. Systém automaticky definuje toleranciu potrebnú na interpoláciu, ak má pole tolerancie hodnotu 0,00. Používateľ môže požadovanú hodnotu tolerancie zadať na karte Tolerancia chyby, ako je znázornené na obr. 14.2.13. Kliknite na ![](../../../assets/Icons/Pre_icons/MO_Interpolate_button2.jpg).

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image014.jpg)

Okno Interpolácia databázy zobrazujúce Definovanie čísla objektu a tolerancie chyby

  1. Kliknite na tlačidlo ![](../../../assets/Icons/Pre_icons/MO_OK_button.jpg), keď sa zobrazí okno Vynútiť toleranciu interpolácie. (Pozri obr. 14.2.14)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image015.jpg)

Okno Interpolácia sily

Interpolované sily sa zobrazia na karte sily, ako je znázornené na obr. 14.2.15.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image016.jpg)

Interpolácia sily 2D hornej kocky

## Pohyb BCC [2D, 3D]

Pohyb konkrétnych uzlov na objekte je možné špecifikovať. Ak je zadaná okrajová podmienka pohybu, musia byť zadané aj ovládacie prvky pohybu objektu.

## Zmenšiť fit BCC [2D, 3D]

Pre každý uzol možno určiť posun v ľubovoľnom smere. To sa často používa na špecifikáciu podmienok zmršťovania medzi lisovacou vložkou a zmršťovacím krúžkom.

Shrink Fit BCC v 3D sa používa na analýzu napätia v zápustke, To možno definovať nasledujúcimi krokmi,

  * Zadanie hodnoty rušenia.
  * Výber smeru (smer kolmý na vnútorný povrch zmršťovacieho krúžku alebo vonkajší povrch lisovacej vložky)
  * Výber vnútorného povrchu zmršťovacieho krúžku alebo vonkajšieho povrchu lisovacej vložky (povrch, ktorý je v kontakte s lisovacou vložkou)

Ak sa na vnútorný objekt aplikuje zmrštenie, hodnota by mala byť záporná a ak sa na vonkajší objekt aplikuje zmrštenie, hodnota by mala byť kladná.

Ďalšie informácie o zmršťovaní nájdete v časti [2D Die Stress Analysis Theory](/docs/sk/Operation_Templates/30_Die_Stress/2D_Die_Stress_Analysis_Theory/).

## Kontakt BCC [2D, 3D]

Kontaktná okrajová podmienka zobrazuje medzipredmetové okrajové kontaktné podmienky na danom objekte. Pred použitím tejto možnosti by mal používateľ získať určité skúsenosti s programom DEFORM. Kontaktné podmienky sú uložené v troch zložkách, aby reprezentovali skutočnosť, že pre každý daný uzol existujú tri stupne voľnosti.

Kontaktné okrajové podmienky sa aplikujú na uzly podriadeného objektu a určujú kontakt medzi týmito uzlami a povrchom nadradeného objektu (pozri obr. 14.2.1.). Ak je zadaný uzol, ktorý má byť v kontakte s konkrétnym objektom, bude umiestnený na povrchu tohto objektu. Ak si to vyžaduje zmenu polohy tohto uzla, zmení sa podľa potreby. Kontaktné okrajové podmienky sa generujú v rámci sekcie Inter-object Contact relation ([CNTACT](/docs/sk/Keyword_Documentation/C/CNTACT/)).

Kontaktné okrajové podmienky možno pre daný objekt zobraziť pomocou ikony Objects, Boundary Conditions, Advanced Deformation BCC's.

## Začiatok povrchu BCC [3D]

V procese vytláčania určuje počiatočný povrch obrobku.

## Voľný povrch BCC [3D]

V procese vytláčania určuje koncový povrch obrobku.

## Rolling BCC [3D]

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image017.jpg)

Rolling Okno hraničných podmienok

**Text sa doplní**

## Pokročilá deformácia BCC [2D, 3D]

Rozšírená okrajová podmienka zobrazuje podmienky medziobjektového kontaktu na danom objekte. Ide o rovnaké informácie, ktoré sa zobrazujú v okne Inter-Object BCC's. Zložky kontaktu X alebo Y nemajú žiadny fyzikálny význam. Smery sú skôr diktované numerickou pohodlnosťou. Podmienky kontaktu sa najprv priradia k smeru Y. Ak je táto pozícia obsadená inou hodnotou, podmienky sa priradia v smere X. Ďalšie informácie nájdete v časti [Nodal data- Deform BCC](../17_Object_Data_Initialization/17_1_Node_Data_Window.htm#Deform_BCC) ([BCCDEF](/docs/sk/Keyword_Documentation/B/BCCDEF/)).

V závislosti od súboru BCC usr_bcc.f fortan musí používateľ zadať číslo User Routine. Popis implementácie používateľsky definovaných rutín BCC nájdete v časti [Chapter 56. User Routines](/docs/sk/User_Routines/56_User_Routines_in_DEFORM/56_User_Routines_in_DEFORM/). (Pozri obr. 14.2.17.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image018.jpg)

(a)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image019.jpg)

(b)

Okno s okrajovými podmienkami objektu Advanced Deformation; (a) pre 2D (b) pre 3D

**Súvisiace témy:**

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.3. Thermal Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)

[14.4. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)

[14.5. Heating Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)
