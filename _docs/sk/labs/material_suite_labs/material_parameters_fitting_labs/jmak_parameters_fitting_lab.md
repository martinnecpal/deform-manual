---
lang: sk
title: "Laboratórium JMAK Parameters Fitting"
---

# Material Suite Lab pre montáž parametrov materiálu v modeli JMAK

1.1. Abstrakt

1.2. Spustenie modelu JMAK v Material Suite

1.3. Definujte kontroly testovania a teplotné skupiny

1.4. Prispôsobte parametre materiálu kinetike DRX

[1.5. Fit material parameters in MRX/SRX kinetics]({{ '/docs/sk/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/' | relative_url }}#1_5_Fit_material_parameters_in_MRX/SRX_kinetics_The_procedure_to_imp)

1.6. Parametre vhodného materiálu v kinetike rastu zrna

1.7. Výstup výsledkov montáže do súboru kľúčových slov

Abstrakt

Model JMAK (Johnson-Mehl-Avrami-Kolmogorov) opisuje rekryštalizačnú kinetiku (vývoj veľkosti zrna a objemového podielu rekryštalizovaných zŕn) kovov počas termomechanického spracovania. V závislosti od špecifických tepelno-mechanických podmienok spracovania môžu prebiehať rôzne rekryštalizačné mechanizmy, vrátane dynamickej rekryštalizácie (DRX) vyskytujúcej sa počas deformácie, meta-dynamickej rekryštalizácie (MRX) alebo statickej rekryštalizácie (SRX) vyskytujúcej sa po deformácii a statického rastu zŕn po dokončení rekryštalizácie. JMAK model vo všeobecnosti pozostáva zo súboru fenomenologických alebo empirických rovníc, ktoré sú funkciami deformácie, rýchlosti deformácie, teploty, času a počiatočnej veľkosti zrna. V JMAK modeli je zavedených veľa materiálových parametrov a je únavnou a časovo náročnou úlohou určiť tieto materiálové parametre z experimentálne nameraných dát. Model JMAK v DEFORM Material Suite poskytuje pohodlný nástroj na prispôsobenie parametrov materiálu v modeli JMAK.

V tomto laboratóriu sú automaticky demonštrované postupy na import experimentálne nameraných údajov do modulu JMAK v DEFORM Material Suite a prispôsobenie parametrov materiálu v modeli JMAK.

## Spustenie modelu JMAK v balíku materiálov

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v12.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI.

Z hlavného GUI kliknite na Material Suite v časti „Post Processor“ a otvorte modul Material Suite. Používateľ môže tiež dvakrát kliknúť na "DEF_GUI_MAT.exe" v inštalačnom adresári DEFORMAČNÉHO softvéru a spustiť sadu materiálov. Po zobrazení hlavného okna pre balík materiálov rozbaľte položku „vlastnosti“ a kliknite na ikonu „** JMAK Model * * “, do stromu úloh sa pridá nová položka úlohy „JMAK“ (pozri obr. JMAKL1.1.). Postupujte podľa každej položky stromu a pripravte údaje modelu JMAK v okne s údajmi o vlastnostiach (pravé dolné okno).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0001.jpg' | relative_url }})

Spustenie modelu JMAK v Material Suite.

Kliknutím na „**Config** “ otvoríte okno a zadáte pracovné adresáre, ako je znázornené na obrázku nižšie. JMAKL1.2. Zadajte pracovný adresár, do ktorého sa budú ukladať vypočítané údaje JMAK.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0017.jpg' | relative_url }})

Konfiguračné okno na definovanie pracovného adresára

## Definujte kontroly testovania a teplotné skupiny

V strome úloh „** JMAK Model** “ kliknite na položku „Testovanie ovládacích prvkov“, ako je znázornené na obr. JMAKL1.3. V okne nehnuteľnosti máme dva rôzne spôsoby, ako začať projekt JMAK. Ak bol predtým uložený existujúci projekt, môžeme kliknutím na tlačidlo „Importovať projekt“ importovať údaje o projekte a definované údaje pre každú položku stromu sa automaticky vyplnia. Používateľ môže tiež pripraviť údaje o projekte od začiatku. Po definovaní údajov na ľubovoľnej stránke položky stromu sa môžeme vrátiť na túto stránku „Testovanie ovládacích prvkov“ a kliknutím na tlačidlo „Uložiť projekt“ uložiť všetky definované údaje.

V tomto laboratóriu definujte systém jednotiek, ktoré predstavujú experimentálne výsledky (napríklad „SI“ v tomto laboratóriu). Kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/material_suite_add_button.jpg' | relative_url }})“ alebo „![]({{ '/assets/icons/pre_icons/material_suite_delete_button.jpg' | relative_url }})“ pridáte alebo odstránite každú testovaciu podmienku. Zadajte nasledujúce údaje pre počiatočnú veľkosť zrna (v mikrónoch): 40 a 100. Zadajte tri skúšobné teploty (v °C) : 900, 1200 a 1400 a dve skúšobné rýchlosti deformácie (v mm/mm/s) : 0,2 a 0,5. Každá mechanická skúška sa vykonáva pri konštantnej rýchlosti deformácie a konštantnej teplote (ako je jednoosová jednotná kompresná skúška).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0002.jpg' | relative_url }})

Definícia kontrol mechanického testovania

V strome úloh „JMAK Model“ kliknite na položku „**Teplotné skupiny** “. V okne s údajmi o vlastnostiach kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/material_suite_add_button.jpg' | relative_url }})“ alebo „![]({{ '/assets/icons/pre_icons/material_suite_delete_button.jpg' | relative_url }})“ a definujte názov skupiny teplôt (pozri obr. JMAKL1.4.). Pre každú skupinu teplôt vyberte zahrnuté teploty. V každej teplotnej skupine sa predpokladajú konštantné materiálové parametre pre rekryštalizačnú kinetiku. Parametre materiálu sa môžu meniť v rôznych teplotných skupinách. V dôsledku toho sú parametre materiálu definované ako funkcia teploty. V tomto laboratóriu definujte teplotnú skupinu ako „AA“ a priraďte do skupiny dve teploty 900 °C a 1200 °C ich výberom, ako je znázornené na obr. JMAKL1.4.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0003.jpg' | relative_url }})

Definícia teplotných skupín

## Prispôsobte parametre materiálu v kinetike DRX

Rozbaľte položku „Dynamická rekryštalizácia (DRX)“ v strome úloh a kliknite na prvú podpoložku „**DRX peak strain** “. V dátovom okne zadajte teplotnú skupinu. Pre každú počiatočnú veľkosť zrna definujte krivky napätia prietoku pre všetky teploty v skupine a všetky rýchlosti deformácie. Každá bunka v testovacej tabuľke zvýraznená červeným obdĺžnikom na obr. JMAKL1.5. definuje krivku napätia prietoku pri konštantnej teplote pri konštantnej rýchlosti deformácie.

Ikona prázdneho súboru („![]({{ '/assets/icons/pre_icons/material_suite_empty_file_icon.jpg' | relative_url }})“) označuje, že údaje bunky ešte neboli definované. Po kliknutí na nedefinovanú bunku sa obrázok bunky zmení na ikonu načítavacieho súboru („![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }})“) a v okne zobrazenia sa zobrazí okno na definovanie funkcie. Údaje o napätí a deformácii je možné manuálne zadať, skopírovať a prilepiť alebo načítať z existujúceho súboru údajov o funkcii. Po dokončení zadávania údajov kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) zatvorte okno definície funkcie. Obrázok bunky sa zmení na definovanú ikonu súboru („![]({{ '/assets/icons/pre_icons/material_suite_defined_file_icon.jpg' | relative_url }})“) a vrcholové napätie sa automaticky extrahuje a zobrazí v editore riadkov. Hodnotu špičkového napätia v editore riadkov je možné manuálne upraviť. Môžeme dvakrát kliknúť na ikonu zobrazenia v hlavičke („![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }})“), aby sme vykreslili krivky napätia prietoku pri pevnej rýchlosti deformácie alebo pevnej teplote. Treba poznamenať, že nie je potrebné definovať údaje pre všetky bunky, ale musí byť splnená minimálna požiadavka na osadenie zainteresovaných parametrov. Rovnaká metóda sa používa na definovanie údajov bunky v testovacej tabuľke pre každú položku alebo podpoložku v strome úloh. V tomto laboratóriu importujeme údaje pre každú bunku skupiny AA z priečinka „3D\LABS\MAK_Parameter_fitting_Lab_DATA\DRX_Peak_strain_DATA“.

Pre veľkosť zrna 40 - miera škvŕn 0,2 - teplota 900 buniek načítajte súbor „ 40_0.2_900.dat“.

Pre veľkosť zrna 40 - miera škvŕn 0,2 - teplota 1200 buniek načítajte súbor „ 40_0.2_1200.dat“.

Pre veľkosť zrna 40 - rýchlosť škvŕn 0,5 - teplota 900 buniek, načítajte súbor " 40_0.5_900.dat".

Pre veľkosť zrna 40 - miera škvŕn 0,5 - teplota 1200 buniek, načítajte súbor " 40_0.5_1200.dat".

Pre veľkosť zrna 100 - miera škvŕn 0,2 - teplota 900 buniek načítajte súbor „ 100_0.2_900.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,2 - teplota 1200 buniek načítajte súbor „ 100_0.2_1200.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,5 - teplota 900 buniek načítajte súbor „ 100_0.5_900.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,5 - teplota 1200 buniek, načítajte súbor " 100_0.5_1200.dat".

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0004.jpg' | relative_url }})

Importujte údaje o napätí prietoku a extrahujte špičkové napätie

Pre teplotnú skupinu po definovaní údajov o napätí prietoku pre všetky počiatočné veľkosti zrna kliknite na tlačidlo „**Fit**“, aby sa parametre materiálu prispôsobili rovnici maximálneho napätia (pozri obr. JMAKL1.6.). Namontované parametre sú zobrazené v tabuľke armatúr a grafické porovnanie medzi nameranými údajmi a predpokladanými údajmi podľa parametrov montovaného materiálu je zobrazené v okne displeja. Pre akýkoľvek známy parameter je možné priamo zadať hodnotu a skontrolovať jej príznak „Fixed“ (Pevná). Po nasadení je možné parametrickú štúdiu vykonať potiahnutím horizontálneho posúvača parametra a graficky preskúmať namerané a predpovedané údaje.

Pre každú ďalšiu teplotnú skupinu, ak existuje, zopakujte tento postup, aby ste importovali jej experimentálne údaje a prispôsobili parametre materiálu.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0005.jpg' | relative_url }})

Prispôsobiť parametre materiálu v rovnici špičkového napätia

Kliknite na podpoložku „**DRX volume fraction** “. V dátovom okne definujte dostupné bunkové údaje (experimentálne namerané) testovacej tabuľky. V tomto laboratóriu importujte údaje každej bunky z priečinka „3D\LABS\JMAK_Parameter_fitting_Lab_Data\DRX_Volume_fraction“.

Pre veľkosť zrna 40 - miera škvŕn 0,2 - teplota 900 buniek načítajte súbor „ 40_0.2_900.dat“.

Pre veľkosť zrna 40 - miera škvŕn 0,2 - teplota 1200 buniek načítajte súbor „ 40_0.2_1200.dat“.

Pre veľkosť zrna 40 - rýchlosť škvŕn 0,5 - teplota 900 buniek, načítajte súbor " 40_0.5_900.dat".

Pre veľkosť zrna 40 - miera škvŕn 0,5 - teplota 1200 buniek, načítajte súbor " 40_0.5_1200.dat".

Pre veľkosť zrna 100 - miera škvŕn 0,2 - teplota 900 buniek načítajte súbor „ 100_0.2_900.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,2 - teplota 1200 buniek načítajte súbor „ 100_0.2_1200.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,5 - teplota 900 buniek načítajte súbor „ 100_0.5_900.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,5 - teplota 1200 buniek, načítajte súbor " 100_0.5_1200.dat".

Každá bunka definuje krivku napätia DRX Vf~ pre konštantnú teplotu a konštantnú rýchlosť napätia. Pre každú krivku deformácie DRX Vf~ sa odporúča zmerať mikroštruktúry pre najmenej 3 hodnoty deformácie, ktoré zodpovedajú nízkym, stredným a vysokým objemovým frakciám DRX, aby bolo možné dobre opísať základný tvar krivky deformácie DRX Vf~. Pre každú definovanú krivku sa deformácia pre 50% DRX automaticky extrahuje a zobrazí v editore riadkov jej bunky. Ak extrahovaný kmeň pre 50% DRX nie je primeraný alebo žiaduci, môže byť manuálne upravený. V okne displeja po montáži sa pre každú mechanickú skúšobnú podmienku experimentálne údaje zobrazujú pevnými bodkami a predpovedané údaje podľa namontovaných parametrov sa zobrazujú ako plná čiara s rovnakou farbou (ako je znázornené na obr. JMAKL1.7.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0006.jpg' | relative_url }})

Prispôsobte parametre materiálu objemovej frakcii DRX

Kliknite na podpoložku „**DRX grain size * * “ v strome úloh. Pre každú dostupnú bunku testovacej tabuľky definujte krivku veľkosti zrna DRX v porovnaní s deformáciou. Importujte údaje každej bunky z priečinka „3D\LABS\ JMAK_Parameter_fitting_Lab_Data\DRX_Grain_size“.

Pre veľkosť zrna 40 - miera škvŕn 0,2 - teplota 900 buniek načítajte súbor „ 40_0.2_900.dat“.

Pre veľkosť zrna 40 - miera škvŕn 0,2 - teplota 1200 buniek načítajte súbor „ 40_0.2_1200.dat“.

Pre veľkosť zrna 40 - rýchlosť škvŕn 0,5 - teplota 900 buniek, načítajte súbor " 40_0.5_900.dat".

Pre veľkosť zrna 40 - miera škvŕn 0,5 - teplota 1200 buniek, načítajte súbor " 40_0.5_1200.dat".

Pre veľkosť zrna 100 - miera škvŕn 0,2 - teplota 900 buniek načítajte súbor „ 100_0.2_900.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,2 - teplota 1200 buniek načítajte súbor „ 100_0.2_1200.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,5 - teplota 900 buniek načítajte súbor „ 100_0.5_900.dat“.

Pre veľkosť zrna 100 - miera škvŕn 0,5 - teplota 1200 buniek, načítajte súbor " 100_0.5_1200.dat".

Po dokončení definície údajov pre vybranú skupinu teplôt kliknite na tlačidlo „**Fit** “, aby sa parametre materiálu prispôsobili rovnici veľkosti zrna DRX, ako je znázornené na obr. JMAKL1.8.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0007.jpg' | relative_url }})

Prispôsobte parametre materiálu veľkosti zrna DRX

Na obr. JMAKL1.9. je znázornená definícia hranice rýchlosti deformácie. Jeho definícia je založená

o empirickom pravidle používateľa na pracovnom materiáli. Nezodpovedáme parametrom v rovnici pre hranicu rýchlosti deformácie. Túto stránku uvádzame preto, aby sme po dokončení montáže parametrov materiálu mohli vygenerovať súbor kľúčových slov pre kompletný model JMAK. Importujte súbor Strain_rate_boundary.dat z priečinka „3D\LABS\ JMAK_Parameter_fitting_Lab_Data“.

Hranica rýchlosti deformácie spolu s priemernou rýchlosťou deformácie a kritickou deformáciou sa používa na určenie, či by sa pri zastavení deformácie mala aktivovať statická alebo meta-dynamická rekryštalizácia.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0008.jpg' | relative_url }})

Definícia materiálových parametrov v hraničnej rovnici rýchlosti deformácie

## Prispôsobte parametre materiálu v kinetike MRX/SRX

Postup importu experimentálnych údajov MRX a prispôsobenia ich materiálových parametrov je rovnaký ako postup pre SRX. Zavádza sa tu len postup prispôsobenia parametrov materiálu v kinetike MRX.

Preddeformovaný kmeň je dôležitým kontrolným faktorom v experimentálnom teste MRX/SRX. Mechanické skúšky sa ukončia na preddeformovaných napätiach, potom sa skúšobné telesá udržiavajú pri rovnakej teplote počas rôznych časov, po ktorých nasleduje kalenie na meranie mikroštruktúry. Mali by sa použiť aspoň dva preddeformované kmene. Pri testoch MRX sú preddeformované kmene veľké ako kritický kmeň, ale menšie ako 100% kmeň DRX. Pri testoch SRX by preddeformované kmene mali byť menšie ako kritické kmene (preto sa DRX ešte nevyskytlo). Definícia preddeformovaných kmeňov je znázornená na obr. JMAKL1.10.

V strome úloh kliknite na položku „** Meta-dynamická rekryštalizácia (MRX)** “. V okne s údajmi zadajte dve preddeformované deformácie, 0,1 a 0,2.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0009.jpg' | relative_url }})

Definícia preddeformovaného kmeňa pre kinetiku MRX

Kliknite na podpoložku „**MRX volume fraction** “ v strome úloh. V dátovom okne zadajte teplotnú skupinu. Pre každú počiatočnú veľkosť zrna a vopred deformovanú deformáciu pre každú dostupnú bunku v testovacej tabuľke definujte krivku objemového podielu MRX v závislosti od času. Importujte údaje každej bunky z priečinka „ 3D\LABS\ JMAK_Parameter_fitting_Lab_Data\MRX_Volume_fraction“.

Pre veľkosť zrna 40 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.1_0.2_900.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.1_0.5_900.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.1_0.2_1200.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.1_0.5_1200.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.2_0.2_900.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.2_0.5_900.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.2_0.2_1200.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.2_0.5_1200.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.1_0.2_900.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0,1 - Stain rate 0,5 - Temperature 900 cell, load " 100_0.1_0.5_900.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.1_0.2_1200.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0,1 - Stain rate 0,5 - Temperature 1200 cell, load " 100_0.1_0.5_1200.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.2_0.2_900.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.2_0.5_900.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.2_0.2_1200.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.2_0.5_1200.dat " file.

Po definovaní krivky bunky sa automaticky extrahuje čas pre 50% MRX a vyplní sa v editore riadkov. Tentoraz pre 50% MRX je možné manuálne upraviť. Po dokončení definície údajov kliknite na tlačidlo „**Fit** “, aby ste prispôsobili parametre materiálu do rovnice objemového zlomku MRX (pozri obr. JMAKL1.11.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0010.jpg' | relative_url }})

Prispôsobiť parametre materiálu pre rovnicu objemového zlomku MRX

Kliknite na podpoložku „** Veľkosť zrna MRX ** “ v strome úloh. Montáž parametrov materiálu pre rovnicu veľkosti zrna MRX je znázornená na obr. JMAKL1.12. Pre každú dostupnú bunku v testovacej tabuľke sa zadá nameraná veľkosť zrna MRX. Predpokladá sa, že veľkosť zrna MRX závisí od počiatočnej veľkosti zrna a podmienok preddeformácie, ale nemení sa s časom procesu MRX. V tomto laboratóriu definujte hodnoty pomocou nižšie uvedených údajov tabuľky 1 a tabuľky 2. Po dokončení definície údajov kliknite na tlačidlo „**Fit** “, aby ste prispôsobili parametre materiálu v rovnici veľkosti zrna MRX.

**Teplota** |  **Počiatočná veľkosť zrna 40** |  **Počiatočná veľkosť zrna 100**
---|---|---
Rýchlosť deformácie 0,2 | Rýchlosť deformácie 0,5 | Rýchlosť deformácie 0,2 | Rýchlosť deformácie 0,5
900 |  68,0606 |  65,1158 |  100,715 |  96,3075
1200 |  93.952 |  89.8477 |  139.463 |  133.32
  
Pre hodnotu predformovaného napätia 0,1

**Teplota** |  **Počiatočná veľkosť zrna 40** |  **Počiatočná veľkosť zrna 100**
---|---|---
Rýchlosť deformácie 0,2 | Rýchlosť deformácie 0,5 | Rýchlosť deformácie 0,2 | Rýchlosť deformácie 0,5
900 |  44,208 |  42,313 |  65,0177 |  62,2092
1200 |  60,708 |  58,0924 |  89,711 |  85,7966
  
Pre hodnotu predformovaného napätia 0,2

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0011.jpg' | relative_url }})

Parametre vhodného materiálu pre rovnicu veľkosti zrna MRX

V strome úloh kliknite na položku „**Statická kryštalizácia (SRX)** “. V okne s údajmi zadajte dve preddeformované deformácie, 0,1 a 0,2, ako je znázornené na obr. JMAKL1.13.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0012.jpg' | relative_url }})

Definícia preddeformovanej deformácie pre kinetiku SRX

Kliknite na podpoložku „**SRX volume fraction** “ v strome úloh. V dátovom okne zadajte teplotnú skupinu. Pre každú počiatočnú veľkosť zrna a vopred deformovanú deformáciu pre každú dostupnú bunku v testovacej tabuľke definujte krivku objemového podielu SRX v závislosti od času. Importujte údaje každej bunky z priečinka „ 3D\LABS\\\ JMAK_Parameter_fitting_Lab_Data\SRX_Volume_fraction“.

Pre veľkosť zrna 40 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.1_0.2_900.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.1_0.5_900.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.1_0.2_1200.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.1_0.5_1200.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.2_0.2_900.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.2_0.5_900.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.2_0.2_1200.dat " file.

Pre veľkosť zrna 40 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.2_0.5_1200.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.1_0.2_900.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0,1 - Stain rate 0,5 - Temperature 900 cell, load " 100_0.1_0.5_900.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.1_0.2_1200.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0,1 - Stain rate 0,5 - Temperature 1200 cell, load " 100_0.1_0.5_1200.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.2_0.2_900.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.2_0.5_900.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.2_0.2_1200.dat " file.

Pre veľkosť zrna 100 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.2_0.5_1200.dat " file.

Po definovaní krivky bunky sa automaticky extrahuje čas pre 50% SRX a vyplní sa v editore riadkov. Tento čas pre 50% SRX je možné manuálne upraviť. Po dokončení definície údajov kliknite na tlačidlo „**Fit** “, aby sa parametre materiálu prispôsobili rovnici objemového zlomku SRX (pozri obr. JMAKL1.14.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0013.jpg' | relative_url }})

Prispôsobiť materiálové parametre pre rovnicu objemového zlomku SRX

Kliknite na podpoložku „** Veľkosť zrna SRX ** “ v strome úloh. Montáž parametrov materiálu pre rovnicu veľkosti zrna SRX je znázornená na obr. JMAKL1.15. Pre každú dostupnú bunku v testovacej tabuľke sa zadá nameraná veľkosť zrna SRX. Predpokladá sa, že veľkosť zrna SRX závisí od počiatočnej veľkosti zrna a podmienok preddeformácie, ale nemení sa s časom procesu SRX. V tomto laboratóriu definujte hodnoty pomocou rovnakých údajov tabuľky 1 a tabuľky 2. Po dokončení definície údajov kliknite na tlačidlo „**Fit** “, aby ste prispôsobili parametre materiálu rovnici veľkosti zrna SRX.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0014.jpg' | relative_url }})

Parametre vhodného materiálu pre rovnicu veľkosti zrna SRX

## Prispôsobte parametre materiálu kinetike rastu zrna

V strome úloh kliknite na položku „** Rast zrna ** “. Pre každú skupinu teplôt definujte dostupné údaje o bunkách v testovacej tabuľke. Každá bunka definuje krivku veľkosti zrna v porovnaní s časom meraným z testov rastu zrna. Importujte údaje každej bunky z priečinka „ 3D\LABS\ JMAK_Parameter_fitting_Lab_Data\Grain Growth“.

Pre veľkosť zrna 40 - teplota 900 vložte súbor " 40_900.dat".

Pre veľkosť zrna 40 - teplota 1200 buniek načítajte súbor " 40_1200.dat".

Pre veľkosť zrna 100 - teplota 900 načítajte súbor " 100_900.dat".

Pre veľkosť zrna 100 - teplota 1200 buniek načítajte súbor " 100_1200.dat".

Po dokončení zadávania údajov kliknite na tlačidlo „**Fit** “, aby sa parametre materiálu prispôsobili rovnici rastu zrna.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0015.jpg' | relative_url }})

Vhodné parametre materiálu pre kinetiku rastu zrna

## Výstup výsledkov montáže do súboru kľúčových slov

Po dokončení parametrov materiálu pre model JMAK kliknite na „**Uložiť súbor kľúčových slov ** “ v strome úloh a zadajte potrebné údaje, ako je znázornené na obr. JMAKL1.17. dokončiť definíciu modelu JMAK. Kliknutím na tlačidlo „* * Uložiť kľúčové slovo * * “ uložíte súbor kľúčových slov do adresára určeného cestou k súboru. Názov súboru kľúčového slova v tomto laboratóriu je „JMAK.key“, údaje je možné zobraziť pod deformačným kľúčovým slovom „GRNDAT“ v uloženom súbore kľúčových slov. V definícii modelu FEM môžeme importovať tento súbor kľúčových slov pre definíciu modelu JMAK.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0016.jpg' | relative_url }})

Uložiť súbor kľúčových slov pre model JMAK
