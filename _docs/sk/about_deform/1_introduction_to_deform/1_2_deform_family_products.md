---
lang: sk
title: "1.2. Produkty rodiny DEFORM"
---

# 1.2. Deformovať rodinu produktov

1.2.1. ZÁKLADNÉ PRODUKTY

1.2.2. EXPRESNÉ MODULY

1.2.3. DODATOČNÉ MODULY

Produkty DEFORM možno klasifikovať ako základné produkty, expresné moduly a doplnkové moduly. Základné produkty sa dodávajú spolu s podpornými modulmi, ktoré pomáhajú používateľovi pri nastavovaní problémov a interpretácii výsledkov. V nasledujúcej tabuľke sú uvedené rôzne dostupné produkty DEFORM,

**ZÁKLADNÝ MODEL** | **EXPRESNÉ MODULY** | **DOPLNKOVÉ MODULY**
---|---|---
PRE-PROCESSOR | FORMING EXPRESS - 2D | COGGING
POSTPROCESOR | FORMING EXPRESS - 3D | ANALÝZA DÁT
INTEGROVANÝ VÝROBNÝ PROCES (MO) | NAMÁHANIE MATRICE | DOE / OPTIMALIZÁCIA
NAPÄTIE V ZÁPUSTKE | | VYTLÁČANIE
DEFORMÁCIE PRI OBRÁBANÍ | | TEPELNÉ SPRACOVANIE
| HT FURNACE
| INVERSE HT
| MACHINING
| | SADA MATERIÁLOV
| VALCOVANIE KRÚŽKOV
| VALCOVANIE TVARU
| SPINNING
| KULIČKOVANIE
  
## ZÁKLADNÉ PRODUKTY

****

**DEFORM Pre-Processor**

DEFORM [Pre-Processor](/docs/sk/pre_processor/7_introduction_to_pre-processor/) je integrovaný produkt 2D a 3D produktov, dokáže modelovať 2D aj 3D modely a umožňuje konvertovať 2D model na 3D model.

**2D:** Dokáže modelovať rovinné deformácie alebo rovinné napätia alebo osovo symetrické alebo torzné časti pomocou jednoduchého dvojrozmerného modelu. Plnofunkčný balík obsahujúci najnovšie inovácie v oblasti modelovania metódou konečných prvkov, ktorý je rovnako vhodný pre výrobné alebo výskumné prostredie.

**3D:** Dokáže modelovať komplexné trojrozmerné vzory toku materiálu. Ideálne pre diely, ktoré nemožno zjednodušiť na dvojrozmerný model.

**DIE STRESS**

Modul [Die stress](/docs/sk/operation_templates/30_die_stress/30_introduction_to_die_stress/) umožňuje používateľovi jednoducho vytvárať simulácie namáhania nástrojov. (2D, 3D)

**integrovaný výrobný proces (MO)**

[Integrated Manufacturing Process ](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/)(MO) poskytuje používateľsky prívetivé rozhranie na zostavenie mnohých po sebe nasledujúcich operácií pri počiatočnom nastavení a ich postupnú simuláciu bez interakcie používateľa. (2D, 3D). Na obr. 1.2.1. je schematicky znázornené prostredie MO.

![]({{ '/assets/images/about_deform/1_2_deform_family_products/1_2_image001.jpg' | relative_url }})

Štruktúra MO ENVIRONMENT

**SKRESLENIE PRI OBRÁBANÍ**

Modul [Machining Distortion](/docs/sk/operation_templates/40_machining_distortion/40_introduction_to_machining_distortion/) umožňuje modelovanie priehybu súčiastky v dôsledku priechodov obrábania na súčiastke s históriou deformácií. (2D, 3D)

  
**Postprocesor**

[Post-Processor](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/) poskytuje používateľovi prostredie na generovanie 3D PDF správ o výsledkoch simulácie, extrakciu údajov o kupónoch, interpretáciu výsledkov v databáze pomocou PIP, vykreslenie výsledkov v oblasti záujmu spolu so všeobecnými funkciami následného spracovania.

## EXPRESNÉ MODULY

Moduly [Forming Express](/docs/sk/operation_templates/34_forming_express/34_introduction_to_forming_express/) sa používajú na nastavenie rôznych 2D a 3D tvárniacich operácií v režime rýchleho sprievodcu v prostredí DEFORM-MO.

**Forming Express-2D:** Dokáže modelovať dvojrozmerné osovo symetrické alebo rovinné deformačné problémy. Vhodný pre malé a stredne veľké dielne, ktoré začínajú s modelovaním metódou konečných prvkov.

**Forming Express-3D:** Dokáže modelovať komplexné trojrozmerné procesy kovania za studena, za tepla a za tepla v prispôsobenom prostredí.

## PRÍDAVNÉ MODULY

**COGGING**

Sprievodca [Cogging](/docs/sk/operation_templates/29_cogging/29_introduction_to_cogging/) umožňuje používateľovi nastaviť sériu operácií Cogging/GFM na polotovare, ktoré predstavujú súbor cyklov tepelno-mechanického spracovania na konečný tvar, veľkosť a metalurgické vlastnosti. (3D)

**DOE**

[DOE](/docs/sk/doe_and_optimization/52_doe_study/51_introduction_to_doe/) dokáže vykonať analýzu citlivosti na riešenie variability/neistôt v podmienkach spracovania, údajov o materiáloch a okrajových podmienok v určenom rozsahu a pri odbere vzoriek. Špeciálne navrhnutý príspevok DOE Post pomôže používateľovi interpretovať výstupy simulácií DOE. (2D, 3D)

**EXTRUSION**

Rozhranie [Extrusion](/docs/sk/operation_templates/31_extrusion/31_introduction_to_extrusion/) umožňuje používateľovi zostaviť modely vytlačovacích procesov na spustenie postupov ALE, ustáleného stavu a Lagrangea. (3D)

**HT FURNACE**

Modul [HT Furnace](/docs/sk/operation_templates/38_furnace_heating/38_introduction_to_3d_ht_furnace/) poskytuje používateľovi prispôsobené prostredie na definovanie podmienok pece a simuláciu rozloženia teploty v polotovaroch pri ich ukladaní v určitom usporiadaní v rámci pece. (3D)

  
**TEPELNÁ ÚPRAVA**

Modul [Heat Treatment](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/) umožňuje používateľovi vytvoriť mnoho po sebe nasledujúcich simulácií tepelného spracovania s minimálnym úsilím. (2D, 3D). Je k dispozícii ako doplnok k programom DEFORM-2D a 3D. Okrem možností modelovania deformácií dokáže DEFORM-HT modelovať účinky tepelného spracovania vrátane tvrdosti, objemového podielu kovovej štruktúry, deformácie, zvyškového napätia a obsahu uhlíka.

**INVERZNÝ PRENOS TEPLA**

Sprievodca [Inverse heat transfer](/docs/sk/inverse_heat/51_introduction_to_inverse_heat/) umožňuje používateľovi určiť koeficient prestupu tepla na hranici objektu pomocou skutočných údajov z termočlánkov v kombinácii s výsledkami iteratívnej simulácie. (2D, 3D)

**MACHINING**

Sprievodca [Machining](/docs/sk/operation_templates/39_cutting/39_introduction_to_cutting/) umožňuje používateľovi vykonávať dvojrozmerné a trojrozmerné simulácie rezania kovov pri sústružení, vyvrtávaní, frézovaní a vŕtaní. (2D, 3D)

**SÚBOR MATERIÁLOV**

[Material Suite](/docs/sk/52_material_suite/52_introduction_to_material_suite/) je integrovaný výpočtový model materiálu, ktorý spája proces, mikroštruktúru, mechanické vlastnosti a výkon. Uľahčuje aj vývoj konštánt z fyzikálnych experimentálnych údajov alebo virtuálnych experimentov s mikroštruktúrou.

**OPTIMALIZÁCIA**

Modul [OPTIMIZATION](/docs/sk/doe_and_optimization/53_optimization_study/53_introduction_to_optimization/) určuje vhodné podmienky procesu na základe pôvodne nastavenej účelovej funkcie (teplota, geometria formy, materiál atď.). Modul DOE Post je špeciálne navrhnutý tak, aby pomohol používateľovi interpretovať výstup optimalizácie a vybrať procesné podmienky. (2D, 3D)

**KRÚŽENIE**

Modul [Ring rolling](/docs/sk/operation_templates/42_ring_rolling/42_introduction_to_ring_rolling/) umožňuje používateľovi interaktívne generovať rôzne komponenty procesu valcovania krúžkov a definovať podmienky procesu.

**TVAROVÉ VALCOVANIE**

Rozhranie [Shape rolling](/docs/sk/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/) umožňuje používateľovi konštruovať modely valcovania tvaru izotermických a neizotermických modelov s viacerými priechodmi a stojanmi na vykonávanie Lagrangeových a ALE postupov. (3D)

  
**ŠPINKOVANIE:**

Rozhranie [Spinning](/docs/sk/operation_templates/48_spinning/48_introduction_to_spinning/) umožňuje používateľovi vytvárať operácie Flow forming a Spinning na spustenie ALE a Lagrangeových postupov (3D)

**Súvisiace témy:**

[PRE-PROCESSOR](/docs/sk/pre_processor/7_introduction_to_pre-processor/)

[POST-PROCESSOR](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[FORMING EXPRESS](/docs/sk/operation_templates/34_forming_express/34_introduction_to_forming_express/)

[COGGING](/docs/sk/operation_templates/29_cogging/29_introduction_to_cogging/)

[MACHINING](/docs/sk/operation_templates/39_cutting/39_introduction_to_cutting/)

[INV. HEAT TRANSFER](/docs/sk/inverse_heat/51_introduction_to_inverse_heat/)

[HEAT TREATMENT](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/)

[INTEGRATED MANUFACTURING PROCESS](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/) (MO)

[SHAPE ROLLING](/docs/sk/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/)

[RING ROLLING](/docs/sk/operation_templates/42_ring_rolling/42_introduction_to_ring_rolling/)

[DIE STRESS](/docs/sk/operation_templates/30_die_stress/30_introduction_to_die_stress/)

[MACHINING DISTORTION](/docs/sk/operation_templates/40_machining_distortion/40_introduction_to_machining_distortion/)

[EXTRUSION](/docs/sk/operation_templates/31_extrusion/31_introduction_to_extrusion/)

[DOE](/docs/sk/doe_and_optimization/52_doe_study/51_introduction_to_doe/)

[OPTIMIZATION](/docs/sk/doe_and_optimization/53_optimization_study/53_introduction_to_optimization/)

[MATERIAL SUITE](/docs/sk/52_material_suite/52_introduction_to_material_suite/)

[HT FURNACE](/docs/sk/operation_templates/38_furnace_heating/38_introduction_to_3d_ht_furnace/)

[DOE POST](/docs/sk/doe_and_optimization/54_doe_post_processor/54_introduction_to_doe_post/)
