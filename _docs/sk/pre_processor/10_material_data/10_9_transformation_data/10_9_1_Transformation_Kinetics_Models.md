---
lang: sk
title: "10.9.1. Modely kinetiky transformácie"
---

# 10.9.1. Modely kinetiky transformácie

  * Difúzia typu TTT tabuľka (Temp, Stress, Atom)

  * Martenzitický typ (Tms, Tms50 Tabuľková forma)

  * Typ difúzie (funkcia)

  * Typ difúzie (funkcia a tabuľka)

  * Martenzitický typ (funkcia)

  * Typ difúzie (zjednodušený)

  * MEDC

  * Sekundárna alfa lišta

  * Sekundárna alfa lišta - na základe kritickej rýchlosti chladenia

  * Ti-beta na hranici zrna alfa

  * Ti-beta na bočnú dosku alfa

  * [Solid/Liquid phase transformation](10_9_1_Transformation_Kinetics_Models.htm#Solid/Liquid_phase_transformation)

  * Difúzia (krivka rozpustnosti)

  * Ni gama primárny model zrážok

  * Model rozpúšťania Ni gama prime

  * Používateľská rutina

Nižšie sú uvedené modely transformačnej kinetiky dostupné v programe DEFORM (pozri obr. 10.9.1.1.),

  1. Difúzny typ tabuľky TTT (Temp, Stress, Atom)
  2. Martenzitický typ (Tms, Tms50 Tabuľková forma)
  3. Typ difúzie (funkcia)
  4. Typ difúzie (funkcia a tabuľka)
  5. Martenzitický typ (funkcia)
  6. Typ difúzie (zjednodušený)
  7. MEDC
  8. Sekundárna alfa lišta
  9. Sekundárna alfa lišta - na základe kritickej rýchlosti chladenia
  10. Ti-beta na hranici zrna alfa
  11. Ti-beta na bočnú dosku alfa
  12. Fázová transformácia tuhá/tekutá látka
  13. Difúzia (krivka rozpustnosti)
  14. Režim zrážania Ni gama prime
  15. Model rozpúšťania Ni gama prime
  16. Používateľská rutina

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image001.jpg' | relative_url }})

Modely kinetiky transformácie

  * **Tabuľka TTT typu difúzie (Temp, Stress, Atom)**

Tento typ definuje diagram TTT (pozri obr. 10.9.1.2 a obr. 10.9.1.3), ktorého nezávislými premennými sú priemerná teplota prvku, efektívne napätie a obsah dominantného atómu. V prípade ocele je dominantný obsah atómov hmotnostným percentom uhlíka v kove pri každom prvku. Pomocou tabuľkových údajov sa DEFORM snaží vyriešiť Avramiho rovnicu, ktorá má tvar,

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_1.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image002.jpg' | relative_url }})

Okno definície funkcie Log (Time) pre model difúznej kinetiky TTT

Pokiaľ ide o údaje TTT, na vyriešenie k a n sú potrebné dve krivky. Ak sa do programu DEFORM zadá len jedna krivka, používateľ musí zadať Avramiho číslo.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image003.jpg' | relative_url }})

Príklad krivky TTT

Na obr. 10.9.1.3 je uvedený príklad TTT diagramu v programe DEFORM. V uvedenom prípade sa na definovanie percenta transformácie pre daný obsah dominantného atómu používajú dve krivky. Každá krivka má hodnotu, pri ktorej je definované množstvo transformácie. Na krivke vľavo bolo definované počiatočné percento premeny z austenitu na bainit. Krivka vpravo je definovaná ako konečné percento premeny austenitu na bainit.

  * **Martenzitický typ (Tms, Tms50 Tabuľková forma)**

Počiatočná teplota transformácie a teplota 50 % úrovne sa zadávajú vo forme tabuľky v závislosti od obsahu uhlíka a úrovne napätia.  
Táto kinetika je založená na Koistinenovej-Marburgerovej rovnici [1]. V systéme DEFORM sa používa všeobecnejšia forma rovnice [2]:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_2.jpg' | relative_url }}) |
---|---
  
  
[1] D.P. Koistinen, R.E. Marburger, Acta Metall, 7 (1959), s. 59-60
[2] S. M. C. van Bohemen, J. Sietsma, Mater. Sci. Technol., 30(2014), s. 1024-1033
  
Okno pre definíciu funkcie martenzitického typu pozri nižšie na obr. 10.9.1.4.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image004.jpg' | relative_url }})

Tabuľka martenzitického začiatku a 50 % teploty tvorí okno definície kinetickej funkcie transformácie

  * **Typ difúzie (funkcia)**

Objemový podiel sa vyjadruje Avramiho rovnicou takto:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_3.jpg' | relative_url }}) |
---|---
  
  
Kde
![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/ft_t.jpg' | relative_url }}), ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/fs_m.jpg' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/fc_c.jpg' | relative_url }}) sú funkcie teploty (![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/t.jpg' | relative_url }})), stredného napätia (![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/sigma_m.jpg' | relative_url }})) a obsahu uhlíka (![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/c.jpg' | relative_url }}) ).

  
Výkon ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/small_n.jpg' | relative_url }}) závisí od druhov transformácie a ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/ft_t.jpg' | relative_url }}) možno vyjadriť nasledujúcim zjednodušeným vzorcom,

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_4.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/fs_sigma_m.jpg' | relative_url }}) okrem toho ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/fc_c.jpg' | relative_url }}) opisuje závislosť transformácie od napätia a obsahu uhlíka, resp:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_5.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_6.jpg' | relative_url }}) |
---|---
  
  
Koeficienty ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/as.jpg' | relative_url }}) sú určené podľa závislosti napätia od kriviek TTT, ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/ac1.jpg' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/ac2.jpg' | relative_url }}) sú určené podľa závislosti od obsahu uhlíka.  
  
Okno definície modelu typu difúznej funkcie nájdete na obr. 10.9.1.5.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image005.jpg' | relative_url }})

Okno definície modelu difúznej kinetickej transformácie

  * **Typ difúzie (funkcia a tabuľka)**

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_7.jpg' | relative_url }}) |
---|---
  
Spolu s rovnicou EQ(2.4.3) sa v tomto type difúzie používa tabuľka, ako je znázornené na obr. 10.9.1.6.

  
![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image006.jpg' | relative_url }})

Okno definície modelu difúznej funkcie a tabuľkovej kinetiky

  * **Martenzitický typ (funkcia)**

Objemový podiel bezdifúznej (martenzitovej) premeny v závislosti od teploty, napätia a obsahu uhlíka sa zavádza úpravou Mageeho rovnice takto:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_8.jpg' | relative_url }}) |
---|---
  
  
Ak sú dané teploty začiatku martenzitovej premeny za podmienok nauhličovania a aplikovaného napätia, možno určiť ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/phi2_by_phi1.jpg' | relative_url }}) , ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/phi31_by_phi1.jpg' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/phi32_byphi1.jpg' | relative_url }}), ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/phi1.jpg' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/phi4.jpg' | relative_url }}), ak sú uvedené teploty pre začiatok martenzitu TMS a pre 50 % martenzitu TM50 pri ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/zeta_m.jpg' | relative_url }}) = 0 a ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/zeta_m.jpg' | relative_url }}) = 0,5.  
  
Okno definície martenzitického modelu nájdete na obr. 10.9.1.7.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image007.jpg' | relative_url }})

Okno definície modelu kinetiky martenzitickej transformácie

  * **Difúzny typ (zjednodušený)**

Zjednodušená difúzna funkcia je definovaná funkciou nasledujúceho tvaru:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_9.jpg' | relative_url }}) |
---|---
  
  
Tento vzorec je dobrou prvou aproximáciou pre transformáciu založenú na difúzii.  
Koeficienty možno získať pomocou dilatačno-teplotných diagramov.  
Pozri nasledujúci obrázok 10.9.1.8. pre okno zjednodušenej definície funkcie Difúzia.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image008.jpg' | relative_url }})

Difúzia zjednodušená kinetická transformácia okno definície modelu kinetiky

  * **MEDC**

Model MEDC vyvinula AFRL v Spojených štátoch na predpovedanie vývoja mikroštruktúry počas kontinuálneho chladenia tvárnených alfa/beta titánových zliatin v dvojfázovom poli. Rast primárnej (guľovitej) alfa štruktúry počas chladnutia sa modeluje pomocou presného riešenia difúznej rovnice:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_10.jpg' | relative_url }}) |
---|---
  
  
Polomer častíc sa prepočíta na objemový podiel pomocou nasledujúceho výrazu:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_11.jpg' | relative_url }}) |
---|---
  
  
  
Vlastné koeficienty difúzie legujúcich prvkov v beta-titáne možno vyjadriť takto,

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_12.jpg' | relative_url }}) |
---|---
  
  
Parameter ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/lamda.jpg' | relative_url }}) v rovnici 1 súvisí s presýtením ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/omega_s.jpg' | relative_url }}) ) pomocou nasledujúceho výrazu:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_13.jpg' | relative_url }}) |
---|---
  
  
V každom kroku výpočtu sa presýtenie ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/omega_s.jpg' | relative_url }}) ) určí ako,

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_14.jpg' | relative_url }}) |
---|---
  
Tu ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/cm.jpg' | relative_url }}) , ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/ci.jpg' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/cp.jpg' | relative_url }}) predstavujú zloženie matrice vzdialenej od rozhrania matrica - častica, matrice na rozhraní matrica - častica a častice na rozhraní matrica - častica. V prípade reakcie riadenej difúziou zodpovedajú ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/ci.jpg' | relative_url }}) a ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/cp.jpg' | relative_url }}) rovnovážnemu zloženiu matrice, resp. častice a boli získané z fázového diagramu. ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/cm.jpg' | relative_url }}) zohľadňuje vplyv mäkkého nárazu na zloženie matrice vo "vzdialenom poli" a počíta sa pomocou obvyklej aproximácie odvodenej z hmotnostnej bilancie:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_15.jpg' | relative_url }}) |
---|---
  
  
Vstupné parametre modelu MEDC zahŕňajú krivky beta prístupu (zobrazujúce objemový podiel beta v závislosti od teploty), rovnovážne chemické zloženie fáz alfa a beta a difúznosť v závislosti od teploty, teplotu roztoku / počiatočný objemový podiel fázy alfa, počiatočný polomer častíc alfa a rýchlosť chladenia. Počiatočný objemový zlomok primárnej alfa (![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/fao.jpg' | relative_url }})) sa automaticky vypočíta na základe poskytnutej krivky prístupu beta v zmysle teploty roztoku (počiatočná teplota procesu chladenia). Počiatočnú veľkosť častíc (![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/rao.jpg' | relative_url }})) určuje používateľ, spravidla na základe experimentálnych údajov. Vývoj primárneho objemového zlomku alfa a veľkosti sa vypočíta na základe lokálnej rýchlosti chladenia počas simulácie prenosu tepla DEFORM.  
Ak je definovaný model zahusťovania sekundárnej alfa lamely, model MEDC sa automaticky spojí s modelom rastu sekundárnej alfa lamely. Rast primárneho alfa je ukončený začiatkom rastu sekundárneho alfa.  
  
Okno definície modelu MEDC nájdete na obr. 10.9.1.9.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image009.jpg' | relative_url }})

Okná definície modelu kinetickej transformácie MEDC

  * **Sekundárna alfa latka**

Na predpovedanie kinetiky zahusťovania sekundárnej alfa-lamely je vyvinutý rýchlo pôsobiaci model. Pri zohľadnení mäkkého nárazu medzi susednými postupujúcimi lamelami možno kinetiku zahusťovania sekundárnej alfy v štruktúre kolónie vyjadriť ako:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_16.jpg' | relative_url }}) |
---|---
  
  
Predpokladá sa, že teplota alfa rovnovážneho rozpúšťania je 980 °C.

Krivka CCT na opis počiatočných teplôt sekundárneho alfa pri rôznych rýchlostiach chladenia je prispôsobená polynomickej rovnici piateho rádu:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_17.jpg' | relative_url }}) |
---|---
  
  
Na nasledujúcom obr. 10.9.1.10. je zobrazené okno definície všeobecného modelu sekundárnej lišty alfa.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image010.jpg' | relative_url }})

Okno definície modelu všeobecnej kinetickej transformácie sekundárnej alfa latky

  * **Sekundárna alfa lišta - na základe kritickej rýchlosti chladenia**

  * **Ti-beta na hranici zrna alfa**

Na predpovedanie kinetiky zhrubnutia hranice zrna alfa v Ti-6Al-4V bol vyvinutý rýchlo pôsobiaci model. Predpokladá sa, že vrstva hranice zŕn alfa so zanedbateľnou hrúbkou sa vytvorí hneď po poklese teploty pod transus beta. Počas ďalšieho ochladzovania alebo izotermického udržiavania alfa na hranici zŕn pokračuje v raste, až kým sa nezačne vyvíjať alfa na bočnej doske. Preto sa tento typ transformácie vo všeobecnosti spája s typom 12 (prechod Ti-beta na bočnú dosku alfa). Kinetiku zhrubnutia hranice zŕn možno opísať takto,

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_18.jpg' | relative_url }}) |
---|---
  
  
Krivky CCT na opis počiatočnej teploty alfa na hranici zrna ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/tu.jpg' | relative_url }}) ) a počiatočnej teploty bočnej dosky (![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/tl.jpg' | relative_url }}) ) pri rôznych rýchlostiach chladenia sú prispôsobené polynomickej rovnici piateho rádu takto:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_19.jpg' | relative_url }}) |
---|---
  
  
Pozrite si nasledujúci obrázok 10.9.1.11. pre okno definície modelu Ti-beta na hranici zrna alfa.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image011.jpg' | relative_url }})

Okno definície modelu kinetickej transformácie Ti-beta na hranicu zrna alfa

  * **Ti-beta na bočnú dosku alfa**

Na predpovedanie kinetiky zhrubnutia bočnej dosky alfa v Ti-6Al-4V je vyvinutý rýchlo pôsobiaci model. Predpokladá sa, že bočná doska alfa sa začne vyvíjať, keď sa zastaví rast alfa na hranici zŕn. Preto je tento typ transformácie spojený s typom 11 (Ti-beta na hranicu zŕn alfa). Vzhľadom na mäkké narážanie medzi susednými postupujúcimi doskami možno kinetiku zhrubnutia a opísať nasledovne,

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_20.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_21.jpg' | relative_url }}) |
---|---
  
  
Dve krivky CCT opisujúce počiatočnú teplotu hranice zrna alfa (![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/tu.jpg' | relative_url }})) a bočnej dosky (![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/tl.jpg' | relative_url }})) pri rôznych rýchlostiach chladenia sú prispôsobené polynomickej rovnici piateho rádu takto:

![]({{ '/assets/equations/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/eq_10_9_1_19.jpg' | relative_url }}) |
---|---
  
Pozrite si nasledujúci obrázok 10.9.1.12. pre okno definície modelu Ti-beta na bočnú dosku alfa.

![]({{ '/assets/images/pre-processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinematic_models/10_9_1_image012.jpg' | relative_url }})

Okno definície modelu kinetickej transformácie Ti-beta na bočnú dosku alfa

  * **Transformácia tuhej a kvapalnej fázy**

  * **Difúzia (krivka rozpustnosti)**

  * **Ni gama model primárnych zrážok**

  * **Model rozpúšťania Ni gama prime**

  * **Používateľská rutina**

Tento model je nastavený na požadované číslo používateľskej rutiny. Pozrite si kapitolu 56. [USER ROUTINE]({{ '/docs/sk/User_Routines/User_routine_MainPg/' | relative_url }}), kde nájdete ďalšie podrobnosti.

**Súvisiace témy:**

[Assigning Material to Object in Pre-Processor](../../../Operation_Templates/33_Forming/33_1_2D_Forming_Setup.htm#Fig_33_1_5_Add_material_from_Material_List_window)

[Deform Units]({{ '/docs/sk/About_DEFORM/1_Introduction_to_DEFORM/1_9_Units/' | relative_url }})

[Material Editing in MO Lab]({{ '/docs/sk/Labs/Heat_Treatment_Labs/2D_HT_Lab5_Material_Input/' | relative_url }})

[TTT Calculation Lab]({{ '/docs/sk/Labs/Material_Suite_labs/Material_Parameters_Fitting_labs/TTT_Calculation_Lab/' | relative_url }})

[Material- Grain Models]({{ '/docs/sk/pre_processor/10_material_data/10_6_Grain_Data/10_6_Grain_Data/' | relative_url }})

[Material-Fracture models]({{ '/docs/sk/pre_processor/10_material_data/10_12_Miscellaneous_Data/10_12_1_Fracture_Models/' | relative_url }})

[Heat Treatment Labs]({{ '/docs/sk/Labs/Heat_Treatment_Labs/Heat_Treatment_Labs_Main_Pg/' | relative_url }})
