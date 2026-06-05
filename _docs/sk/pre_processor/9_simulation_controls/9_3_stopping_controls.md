---
lang: sk
title: "9.3. Ovládacie prvky na zastavenie"
---

# 9.3. Ovládacie prvky zastavenia ![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }})

9.3.1. Dĺžka spracovania (TMAX) [2D, 3D]

9.3.2. Posun primárneho lisovacieho nástroja (SMAX)

9.3.3. Minimálna rýchlosť primárneho valca (VMIN)

9.3.4. Maximálne zaťaženie primárnej matrice (LMAX)

9.3.5. Maximálne napätie v ktoromkoľvek prvku (EMAX)

9.3.6. Meranie priemeru prstena

9.3.7. Maximálny vonkajší priemer (ODMAX)

9.3.8. Minimálny vnútorný priemer (IDMIN)

9.3.9. Pomer kontaktnej plochy

9.3.10. Zastaviť simuláciu pri skladaní

9.3.11. Okno zastavenia

9.3.12. Vzdialenosť medzi maticami

9.3.13. Zastavovacia rovina (REFPOS)

9.3.14. Regulácia zastavenia na základe teploty

9.3.15. ALE v ustálenom stave (ALECON)

Parametre ukončenia určujú čas priebehu, po ktorom sa simulácia ukončí. Simuláciu je možné ukončiť na základe maximálneho počtu simulovaných časových krokov, maximálneho kumulovaného elementárneho deformácie, maximálneho času priebehu, maximálneho zdvihu, minimálnej rýchlosti alebo maximálneho zaťaženia primárneho objektu. Simulácia sa zastaví, keď je splnená podmienka ktoréhokoľvek z parametrov ukončenia. Ak je niektorému z parametrov ukončenia okrem počtu krokov ([NSTEP](/docs/sk/keyword_documentation/n/nstep/)) priradená nulová hodnota, parameter sa nepoužije. Ak nie sú špecifikované žiadne iné parametre ukončenia, simulácia bude prebiehať, kým nevyčerpá všetky špecifikované kroky. (Pozri obr. 9.3.1. a  obr. 9.3.2.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image001.jpg' | relative_url }})

Parametre 3D procesu na zastavenie simulácie

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image007.jpg' | relative_url }})

Ovládacie prvky na zastavenie v 3D v režime s navádzaním

## Dĺžka spracovania (TMAX) [2D, 3D]

Ukončí simuláciu, keď celková dĺžka procesu ([TMAX](/docs/sk/keyword_documentation/t/tmax/)) dosiahne zadanú hodnotu.

## Posun primárneho výlisku (SMAX) [2D, 3D]

Simulácia sa ukončí, keď celkový posun ([SMAX](/docs/sk/keyword_documentation/s/smax/)) hlavnej matrice dosiahne zadanú hodnotu. Hodnota zdvihu pre objekt sa zadáva na karte Pohyb objektu.

## Minimálna rýchlosť primárnej matrice (VMIN) [2D, 3D]

Simuláciu ukončí, keď zložka rýchlosti primárnej matice v smere X, Y alebo Z dosiahne príslušné hodnoty X, Y alebo Z parametra [VMIN](/docs/sk/keyword_documentation/v/vmin/).

Tento parameter sa zvyčajne používa v prípadoch, keď je pohyb hlavného objektu riadený zaťažením, alebo keď sa pri hydraulickom lise uplatňuje parameter obmedzenia výkonu ([SPDLMT](/docs/sk/keyword_documentation/s/spdlmt/)).

## Maximálne zaťaženie primárneho výlisku (LMAX) [2D, 3D]

Ukončí simuláciu, keď zložka zaťaženia X, Y alebo Z primárneho telesa dosiahne príslušnú hodnotu X, Y alebo Z nastavenú v [LMAX](/docs/sk/keyword_documentation/l/lmax/). Zvyčajne sa používa v prípadoch, keď je riadenie pohybu primárneho objektu založené na rýchlosti alebo je určené používateľom.

## Maximálne napätie v ktoromkoľvek prvku (EMAX) [2D, 3D]

Táto voľba ([EMAX](/docs/sk/keyword_documentation/e/emax/)) ukončí simuláciu, keď kumulované deformácie ktoréhokoľvek prvku dosiahnu zadanú hodnotu.

## Meranie priemeru prsteňa [3D]

Táto možnosť bude k dispozícii iba pre typ simulácie valcovania prstencov. Po zaškrtnutí políčka „Meranie priemeru prstenca“ môžeme vybrať možnosť „OD“ alebo „ID“, čím určíme, či sa ako kritérium zastavenia použije vonkajší alebo vnútorný priemer prstenca. V poli Z môžeme definovať miesto merania pozdĺž osi Z, v ktorom sa má priemer merať na účely riadenia zastavenia.

Ak zvolíme možnosť „OD“, môžeme využiť možnosť „Max. vonkajší priemer“ na definovanie vonkajšieho priemeru krúžku ako obmedzujúceho parametra počas simulácie. Podobne, keď zvolíme možnosť „ID“, môžeme vidieť možnosť „Min. vnútorný priemer“, ktorou môžeme počas simulácie definovať vnútorný priemer krúžku ako obmedzovač. Pozri obr. 9.3.3. Používateľ musí z roletového menu vybrať symbol „>“, aby definoval hodnotu priemeru obmedzovača.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image011.jpg' | relative_url }})

Možnosť merania priemeru prsteňa pri valcovaní prsteňov

## Maximálny vonkajší priemer (ODMAX) [2D, 3D]

Táto voľba ukončí simuláciu v prípade, že vonkajší priemer obrobku prekročí definovanú maximálnu hodnotu vonkajšieho priemeru. V 2D je táto voľba k dispozícii iba pre typ geometrie „Axisymmetric“. 

Možnosť:

  * „**vypnuté**“: ak je zvolená možnosť „vypnuté“, počas simulácie sa nebude počítať kontrola zastavenia na základe maximálneho vonkajšieho priemeru.

  * „**< **“: ak je zvolená možnosť „<“, simulácia sa ukončí v okamihu, keď vonkajší priemer obrobku klesne pod hodnotu maximálneho vonkajšieho priemeru.

  * „**>** “: ak je zvolená možnosť „ > “, simulácia sa ukončí v okamihu, keď vonkajší priemer obrobku prekročí hodnotu maximálneho vonkajšieho priemeru.

## Minimálny vnútorný priemer (IDMIN)[2D3D]: 

Táto voľba ukončí simuláciu, keď vnútorný priemer obrobku prekročí definovanú minimálnu hodnotu vnútorného priemeru. V 2D je táto voľba k dispozícii iba pre typ geometrie „Axisymmetric“. 

Možnosť:

  * „**vypnuté**“: Ak je zvolená možnosť „vypnuté“, počas simulácie sa nebude počítať regulácia zastavenia na základe minimálneho vnútorného priemeru.

  * „ **<** “ : Ak je zvolená možnosť „ < “, simulácia sa ukončí v okamihu, keď vnútorný priemer obrobku klesne pod hodnotu minimálneho vnútorného priemeru.

  * „ **>** “ : Ak je zvolená možnosť „ > “, simulácia sa ukončí v okamihu, keď vnútorný priemer obrobku prekročí hodnotu minimálneho vnútorného priemeru.

## Pomer kontaktnej plochy [2D, 3D]

Táto voľba ukončí simuláciu, keď pomer kontaktnej plochy prekročí zadanú hodnotu pomeru kontaktnej plochy.  
Pomer kontaktnej plochy sa pohybuje v rozmedzí 0–1, pričom hodnota 0 znamená žiadny kontakt a hodnota 1 znamená úplný kontakt. Pri výpočte pomeru kontaktnej plochy sa nezohľadňuje stredová čiara v 2D a symetrické roviny v 3D.

## Zastaviť simuláciu pri skladaní [2D, 3D] 

Táto voľba ukončí simuláciu, keď sa v sieti deformovaného objektu zistí prehnutie.

## Zastavovacie okno [2D, 3D]:

Používateľ môže pomocou možnosti „Zastavovacie okno“ určiť miesto na obrobku, kde sa má skontrolovať pomer vyplnenia formy a kontaktu alebo ohyb. Možnosti „Pomer kontaktnej plochy“ a „Ohyb“ sú k dispozícii v roletovom zozname „Zastaviť pri“ (pozri obr. 9.3.4.).

Ak je zvolená možnosť „Pomer kontaktnej plochy“ a plocha povrchu obrobku vnútri oblasti okna dosiahne definované kritériá pomeru kontaktnej plochy, simulácia FEM sa zastaví.  
  
Ak je zvolená možnosť „Fold“ a na povrchu obrobku v oblasti okna sa zistí prehyb, simulácia FEM sa zastaví.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image009.jpg' | relative_url }})

Okno lietadla

## Vzdialenosť medzi formami [2D, 3D]

Ukončí simuláciu, keď vzdialenosť medzi referenčnými bodmi ([MDSOBJ](/docs/sk/keyword_documentation/m/mdsobj/)) na dvoch objektoch dosiahne zadanú hodnotu. Vzdialenosť zastavenia je potrebné nastaviť v okne „Die Distance“ pri definovaní referenčného bodu ([REFPOS](/docs/sk/keyword_documentation/r/refpos/)). 

Od verzie V12.0.2 platí, že v prípade referenčných objektov, ak sú definované referenčné body (v vlastnostiach objektu), môžeme sledovať stav ![]({{ '/assets/icons/pre_icons/mo_dis_bw_dies_check_mark_icon.jpg' | relative_url }}) a v prípade referenčného objektu, ak nie je definovaný referenčný objekt, môžeme sledovať stav ![]({{ '/assets/icons/pre_icons/mo_dis_bw_dies_question_mark_icon.jpg' | relative_url }}) na karte Die-Distance, ako je znázornené na obr. 9.3.5.

Pri čítaní z referenčného objektu databázy (v rámci nasledujúcej operácie) môžeme v prípade, že sú definované referenčné body, sledovať stav ![]({{ '/assets/icons/pre_icons/mo_dis_bw_dies_read_from_db_check_mark_icon.jpg' | relative_url }}), a ak referenčný objekt nie je definovaný, môžeme sledovať stav ![]({{ '/assets/icons/pre_icons/mo_dis_bw_dies_read_from_db_question_mark_icon.jpg' | relative_url }}) na karte „Die-Distance“, ako je znázornené na obr. 9.3.6.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image002.jpg' | relative_url }})

a)

  
![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image003.jpg' | relative_url }})

b)

Brzdná dráha na základe vzdialenosti medzi maticami; (a) Určenie prvého referenčného bodu (b) Určenie druhého referenčného bodu

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image008.jpg' | relative_url }})

Okno režimu Expert pre ovládacie prvky zastavenia vzdialenosti pri čítaní z databázového objektu.

Určenie brzdnej dráhy,

  1. Vyberte objekt, ktorý sa má použiť ako Referencia 1.
  2. Vyberte buď uzol, alebo súradnice objektu Referencia 1 a potom vyberte príslušný bod na objekte Referencia 1, ako je znázornené na obr. 9.3.5.(a).
  3. Vyberte objekt, ktorý sa má použiť ako Referencia 2.
  4. Vyberte buď uzol, alebo súradnicu objektu Referencia 2 a potom vyberte príslušný bod na objekte Referencia 2, ako je znázornené na obr. 9.3.5.(b).
  5. Nastavte metódu merania vzdialenosti a vzdialenosť, pri ktorej sa má simulácia zastaviť.

**Skontrolovať až po spotrebovaní energie**: Táto možnosť bola pridaná vo verzii 12.1.1. Možnosť „Skontrolovať až po spotrebovaní energie“ sa aktivuje iba pri typoch pohybu založených na spotrebe energie (pohyb kladivom a skrutkovacím lisom). Ak používateľ zaškrtne políčko „Skontrolovať až po spotrebovaní energie“, počas simulácie sa kritériá zastavenia vzdialenosti matrice vypočítajú až po úplnom spotrebovaní energie, a nie na konci každého kroku.

##  Zastavujúce sa lietadlo (REFPOS) [2D, 3D]

Táto funkcia sa zvyčajne používa v modeloch, ako je napríklad proces prechodného valcovania. Používateľ môže v priestore definovať rovinu a nastaviť ukončenie simulácie v okamihu, keď obrobok túto rovinu úplne prekročí. (Pozri obr. 9.3.7.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image004.jpg' | relative_url }})

Brzdná dráha na základe brzdnej roviny

Od verzie 13.0 môžeme údaje o referenčnej rovine definovať samostatne pre každý deformovateľný objekt. 

  
Ak chcete nastaviť ovládacie prvky pre referenčnú rovinu, najprv vyberte referenčný objekt z roletového zoznamu a zaškrtnite políčko „Definované“, potom zadajte hodnotu „Počiatok“ (na určenie polohy roviny) a údaje o vektore (na určenie normály roviny).  
Musíme definovať hodnotu vektora vzhľadom na smer pohybu referenčného objektu.  
Používateľ môže tiež kliknúť na objekt v zobrazovacej oblasti, aby vybral deformovateľný objekt a údaje o jeho počiatku. 

Ak sa počas simulácie celá oblasť referenčného objektu dostane do definovanej roviny, simulácia sa ukončí s nasledujúcou správou.  
" PROGRAM SA ZASTAVIL!  
Zastavenie lietadla: Všetky uzly objektu 1 opustili hraciu plochu. 

_**Poznámka**: V zozname objektov pre ovládacie prvky zastavovacej roviny budú uvedené iba plastické a elastoplastické objekty._

  
**Napríklad:**

****  
Pri valcovaní v 2D režime,

  1. Definujte údaje o zastavovacej rovine tak, že v zozname vyberiete objekt „Obrobok“ a zaškrtnete políčko „Definované“.

  2. Potom určte počiatok ako 0, 0, aby ste určili polohu roviny. 

  3. Teraz nastavte vektora v poli X na hodnotu „-1“ (aby ste definovali normálu voči zastavovacej rovine), ako je znázornené na obr. 9.3.8 nižšie. 

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image010.jpg' | relative_url }})

Definovanie 2D zastavovacej roviny pri valcovacom procese 

## Regulácia zastavenia na základe teploty [2D, 3D]

Toto tepelné zastavovacie kritérium slúži na reguláciu teploty objektov v procese. Používateľ môže na úrovni objektov definovať minimálnu a maximálnu teplotu ako zastavovacie kritérium (pozri obr. 9.3.9.). K tejto funkcii sa dostanete z okna definície údajov objektu v časti Vlastnosti objektu – karta Teplota. 

**Predmet**

Referenčný objekt pre ovládacie prvky tepelnej izolácie sa vyberie v zozname objektov.

**Spôsob zastavenia**  
**Žiadne** : Neaplikuje žiadne opatrenia na obmedzenie prehrievania

**Ľubovoľný uzol**: Simulácia sa zastaví, keď ktorýkoľvek uzol v sochore dosiahne zadanú hodnotu.

**Všetky uzly**: Simulácia sa zastaví, keď všetky uzly v polotovare dosiahnu zadanú hodnotu.

**Vybraný bod**: Simulácia sa zastaví, keď určený bod v polotovare dosiahne zadanú hodnotu.

**Priemer všetkých uzlov**: Simulácia sa zastaví, keď priemerná teplota všetkých uzlov v sochore dosiahne zadanú hodnotu.

**Priemerná povrchová teplota + maximálna teplota**: Simulácia sa zastaví, keď priemerná teplota všetkých uzlov

na povrchu sochoru + Maximálna teplota v sochore dosiahne stanovenú hodnotu.

  
**Teplotný rozsah**  
Okrem konkrétnej hodnoty je možné na ukončenie simulácie použiť aj teplotný rozsah.

**Zastaviť, ak teplota prekročí stanovený rozsah**: Simulácia sa zastaví, ak hodnota teploty prekročí stanovený rozsah.

**Zastaviť, keď je teplota v rozsahu**: Simulácia sa zastaví, keď sa hodnota teploty nachádza v zadanom rozsahu.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image005.jpg' | relative_url }})

Regulácia zastavenia na základe teploty

## ALE v ustálenom stave (ALECON) [3D]

V programe DEFORM V12 môže používateľ definovať kritériá zastavenia pre ustálený stav ALE ([ALECON](/docs/sk/keyword_documentation/a/alecon/)) pri valcovom procese ALE na karte „Ovládanie zastavenia – Ovládanie zastavenia v ustálenom stave ALE“. (Pozri obr. 9.3.10.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_3_stopping_controls/9_3_image006.jpg' | relative_url }})

ALE Kritériá zastavenia v ustálenom stave

**Súvisiace témy:**

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.6. Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)   
[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)
