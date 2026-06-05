---
lang: sk
title: "9.4. Kritériá pre generovanie novej siete"
---

# 9.4. Kritériá pre výpočet novej siete ![]({{ '/assets/icons/pre_icons/mo_remeshing_criteria.jpg' | relative_url }})

9.4.1. Maximálna hĺbka interferencie (RMDPTH)

9.4.2. Maximálny prírastok zdvihu (RMSTRK)

9.4.3. Maximálny časový krok (RMTIME)

9.4.4. Maximálny krok (RMSTEP)

9.4.5. Vzdialenosť prenikania (absolútna)

9.4.6. Vzdialenosť prenikania (relatívna)

9.4.7. Ďalšie kritériá pre tvorbu novej siete

9.4.8. Metóda prepočítania siete

**[2D, 3D]** : Kritériá pregenerovania siete (Autoremesh) predstavujú najpohodlnejší spôsob, ako riešiť pregenerovanie siete objektov, ktoré prechádzajú veľkou plastickou deformáciou. Okno Kritériá pre vytváranie novej siete (obr. 9.4.1.) obsahuje skupinu parametrov, ktoré riadia, kedy a ako často sa sieť na objektu so sieťou regeneruje na základe priradenia určitých spúšťačov.Existujú štyri kľúčové slová, ktoré riadia spustenie postupu premenovania ([RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/), [RMTIME](/docs/sk/keyword_documentation/r/rmtime/), [RMSTEP](/docs/sk/keyword_documentation/r/rmstep/) a [RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/)) pre objekt. Keď sú splnené kritériá pregenerovania siete pre ktorékoľvek z týchto kľúčových slov alebo sa sieť stane nepoužiteľnou (negatívna Jacobova matica), objekt bude pregenerovaný. Ak objekt počas simulácie spĺňa niektoré z kritérií pre vytváranie novej siete, vygeneruje sa nová sieť, informácie o riešení zo starej siete sa interpolujú na novú sieť a simulácia pokračuje.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_4_remesh_criteria/9_4_image001.jpg' | relative_url }})

a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_4_remesh_criteria/9_4_image002.jpg' | relative_url }})

b)

Okno kritérií pre výpočet novej siete; (a) pre 2D, (b) pre 3D

## Maximálna hĺbka interferencie (RMDPTH) [2D, 3D]

Hodnota maximálnej hĺbky zasahovania ([RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/)) slúži na spustenie procesu prepočítania sietí. Ak akákoľvek časť hlavného objektu zasahuje do podriadeného objektu hlbšie, ako je hĺbka špecifikovaná v parametri RMDPTH, spustí sa prepočítanie sietí. 

## Maximálny prírastok zdvihu (RMSTRK) [2D, 3D]

Vždy, keď prírastok zdvihu primárnej formy od posledného kroku vytvárania siete prekročí maximálny prírastok zdvihu ([RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/)), spustí sa nový krok vytvárania siete. 

## Maximálny časový krok (RMTIME) [2D, 3D]

Vždy, keď uplynie maximálny časový interval ([RMTIME](/docs/sk/keyword_documentation/r/rmtime/)) (hodnota uplynutého času) od posledného kroku vytvárania novej siete, spustí sa nový krok vytvárania novej siete. 

## Maximálny krok (RMSTEP) [2D, 3D]

Vždy, keď od posledného kroku prepočítania siete dôjde k dosiahnutiu maximálneho prírastku krokov (počet krokov), spustí sa nový krok prepočítania siete.

**Účel kritérií [2D, 3D]**

Keď ostrá hrana nástroja alebo formy narazí na obrobok, môže hlboko vniknúť do okraja prvku. Ak je táto hĺbka príliš veľká, prvky sa môžu natiahnuť a opätovné vytvorenie siete môže byť sťažené. Ešte pred dosiahnutím tejto hĺbky je potrebné opätovne vytvoriť sieť umiestnením uzlov okolo okraja, čím sa simulácia môže bez problémov pokračovať.

## Vzdialenosť prenikania (absolútna) [3D]:

Ak zadáte kladné číslo (v jednotkách dĺžky), program skontroluje každý okraj povrchu, ktorý má na oboch koncoch kontaktný uzol. Vypočíta sa vzdialenosť od stredu okraja k povrchu formy. Ak maximálna hĺbka vniknutia prekročí stanovený limit, spustí sa prepočítanie siete.

## Vzdialenosť prenikania (relatívna) [3D]:

Ak sa zadá záporné číslo (zlomok), program vykoná kontrolu každého okraja povrchu, ktorý má na oboch koncoch kontaktný uzol. Vypočíta sa vzdialenosť od stredu okraja k povrchu formy a vydelí sa pôvodnou dĺžkou okraja. Ak tento pomer prekročí veľkosť zadaného čísla, spustí sa prepočítanie siete.

**Predvolená hodnota [3D]:**

Predspracovateľ má teraz predvolenú hodnotu 0,7 s relatívnym nastavením.

## Ďalšie kritériá pre generovanie novej siete [3D]

  * **Limit rozťahovania**: Rozťahovanie hrany sa vypočíta ako „(aktuálna dĺžka – pôvodná dĺžka) / pôvodná dĺžka“. Ak táto hodnota prekročí stanovený limit, vykoná sa prepočet siete.

  * **Limit zmenšenia**: Zmenšenie hrany sa vypočíta ako „(aktuálna dĺžka – pôvodná dĺžka)/pôvodná dĺžka“. Ak táto hodnota prekročí stanovený limit, vykoná sa prepočet siete.

##  Metóda prepočítania siete [3D]

**Možnosti globálneho a lokálneho prekreslenia sietí [3D]**

V programe DEFORM-3D bola tvorba sietí vylepšená o funkciu lokálneho vytvárania sietí.

Predvolené nastavenia smerujú k existujúcim postupom globálneho prečlenenia, pri ktorých sa každý prvok starej siete nahradí novým prvkom siete, na čo nadväzuje interpolácia.

Nová funkcia lokálneho vytvárania sietí ponúka viacero možností na nastavenie veľkosti a kvality prvkov. Lokálne premeshovanie má tiež možnosti, ako zachovať skutočne lokálny charakter sietovania, aby sa minimalizovali chyby súvisiace s interpoláciou. (Pozri obr. 9.4.3.) V aktuálnej verzii sú všetky nastavenia súvisiace s lokálnym sietovaním uložené v lokálnych súboroch, nie v databáze.

To znamená, že ak používateľ skopíruje súbor databázy z jedného priečinka do druhého, lokálne nastavenia pre výpočet sietí sa neprenesú, pokiaľ sa do pracovného priečinka nezkopírujú všetky súbory.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_4_remesh_criteria/9_4_image003.jpg' | relative_url }})

Okno s kritériami globálneho prekreslenia siete

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_4_remesh_criteria/9_4_image004.jpg' | relative_url }})

Okno s kritériami pre lokálne prepočítanie sietí

**Vnútorné prvky:**

  * **Nastavenie veľkosti** :

  * **Priemer susedných prvkov**: Veľkosť prvku sa určuje na základe priemernej veľkosti okolitých prvkov deformovanej siete.
  * **Mierka**: Veľkosť prvku sa bude zmenšovať podľa mierky uvedenej pre každú vrstvu smerom dovnútra.

  * **Preskočiť prvky s dobrým tvarom**: Prvky s dobrým tvarom nebudú pri opätovnom vytváraní siete zohľadnené.

**Súvisiace témy:**

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)

[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)

[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)

[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)

[9.6. Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)

[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)

[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)

[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)

[13\. Mesh Data Definition](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)
