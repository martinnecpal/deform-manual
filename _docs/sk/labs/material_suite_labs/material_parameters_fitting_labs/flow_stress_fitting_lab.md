---
lang: sk
title: "Laboratórium namáhania prietoku"
---

# Material Suite Lab pre montáž parametrov materiálu v modeli prietokového napätia

## Zavedenie zariadenia na montáž údajov o napätí prietoku

V Material Suite poskytujeme pohodlný nástroj na konverziu experimentálnych údajov (krivky zaťaženia a zdvihu alebo krivky napätia a deformácie) na tabuľkové údaje o prietoku a napätí v DEFORMÁCII. Program môže zvážiť adiabatickú korekciu experimentálnych údajov. Program poskytne parametre namontovaného materiálu v modeli prietokového napätia, grafické porovnanie medzi pôvodnými experimentálnymi údajmi a údajmi modelu. Používateľ môže ľahko uložiť namontované údaje o napätí prietoku do súboru kľúčových slov pre simuláciu MKP.

## Spustiť model napätia prietoku v súbore materiálov

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v12.xxx (.xxx označuje číslo verzie Napr. V14.0.2 a z ponuky vyberte Deform GUI Main v1x.xx. Zobrazí SA hlavné okno Deform GUI. Z hlavného grafického rozhrania kliknite na **Material Suite** v časti „Post Processor“ a otvorte modul Material Suite. Používateľ môže tiež dvakrát kliknúť na „**DEF_GUI_MAT.exe* * “ v inštalačnom adresári DEFORMAČNÉHO softvéru a spustiť sadu materiálov. Po zobrazení hlavného okna pre balík materiálov rozbaľte položku „vlastnosti“ a kliknite na ikonu „Model napätia prietoku“, do stromu úloh sa pridá nová položka úlohy „Napätie prietoku“ (pozri obr. FSL1.1.). Postupujte podľa každej položky stromu a pripravte údaje modelu napätia prietoku v okne s údajmi o vlastnostiach (pravé dolné okno).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0001.jpg' | relative_url }})

Spustite model Flow Stress v balíku materiálov.

Kliknutím na „**Config** “ otvoríte okno a zadáte pracovné adresáre, ako je znázornené na obrázku nižšie. FSL1.2\. Zadajte pracovný adresár, do ktorého sa budú ukladať vypočítané údaje o napätí prietoku.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0010.jpg' | relative_url }})

Konfiguračné okno na definovanie pracovného adresára

## Definujte jednotky a počiatočnú geometriu vzorky

V strome úloh „Stres prietoku“ kliknite na položku „**jednotky a počiatočná geometria vzorky ** “. V časti „jednotky A počiatočná geometria vzorky“ vyberte jednotku **SI * *. Počiatočná výška a počiatočná plocha prierezu sa používajú na konverziu údajov medzi údajmi o zdvihu zaťaženia a údajmi o namáhaní, jednotka je mm pre jednotku SI a palec pre anglickú jednotku. Ak chcete importovať údaje o projekte, môžeme kliknúť na tlačidlo „** Importovať projekt * * “, po importovaní sa automaticky vyplnia definované údaje pre každú položku stromu. Používateľ môže tiež pripraviť údaje o projekte od začiatku. Po definovaní údajov na ľubovoľnej stránke položky stromu sa môžeme vrátiť na túto stránku „jednotky a počiatočná geometria vzorky“ a kliknutím na tlačidlo „**Uložiť projekt * * “ uložiť všetky definované údaje. V tomto laboratóriu vyberáme 100 pre počiatočnú výšku a 10 pre počiatočnú plochu prierezu (pozri obr. FSL1.3.) .

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0002.jpg' | relative_url }})

Jednotky a úvodná geometria vzorky strana

## Definujte typ a podmienky testovania

V strome úloh „Stres prietoku“ kliknite na položku „** Typ testovania a podmienky** “. Vyberte "**Napätie** " ako typ testovania, "**Konštantná rýchlosť deformácie ** " ako typ kontroly frekvencie, ako je znázornené na obr. FSL1.4.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0003.jpg' | relative_url }})

Stránka Typ a podmienky testovania

## Definujte teplotu a sadzby testovania

V strome úloh „Tekuté napätie“ kliknite na stránku „**T******e** teplota a rýchlosti deformácie**“. Zadajte tri testovacie teploty: 200, 500 a 700 a tri testovacie rýchlosti deformácie: 0,1, 0,5 a 1, ako je znázornené na obr. FSL1.5. Na ďalšej stránke zadáme 9 sád údajov o tečení ako funkciu deformácie pre každú kombináciu teploty a rýchlosti deformácie.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0004.jpg' | relative_url }})

Testovacia stránka Teplota a sadzby

## Definujte experimentálne údaje

V strome úloh „Flow stress“ kliknite na stránku „**Experimentálne údaje** “. Vyberte prepínač Flow stress data (údaje o napätí prietoku) v časti Raw data type (typ údajov Raw) ( pozri obr. FSL1.6.) a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/material_suite_delete_button.jpg' | relative_url }}) a zadajte údaje o napätí prietoku pre každú bunku. Ikona prázdneho súboru („![]({{ '/assets/icons/pre_icons/material_suite_empty_file_icon.jpg' | relative_url }}) “) označuje, že údaje bunky ešte neboli definované. Po kliknutí na nedefinovanú bunku sa obrázok bunky zmení na ikonu načítavacieho súboru („![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }})“) a v okne zobrazenia sa zobrazí okno na definovanie funkcie. Údaje o napätí a deformácii je možné manuálne zadať, skopírovať a prilepiť alebo načítať z existujúceho súboru údajov o funkcii. Po dokončení zadávania údajov kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) zatvorte okno definície funkcie. Obrázok bunky sa zmení na definovanú ikonu súboru („![]({{ '/assets/icons/pre_icons/material_suite_defined_file_icon.jpg' | relative_url }})“). Pre toto laboratórium importujte údaje každej bunky z priečinka "3D\LABS\Material_Suite_Flow_stress_data" do inštalačnej cesty,

Pre teplotu 200 - rýchlosť deformácie 0,1 bunky načítajte súbor „ Temp_200_Strain_rate_0.1.dat“.

Pre teplotu 200 - rýchlosť deformácie 0,5 bunky načítajte súbor „ Temp_200_Strain_rate_0.5.dat“.

Pre teplotu 200 - rýchlosť deformácie 1 bunka, vložte súbor " Temp_200_Strain_rate_1.dat".

Pre teplotu 500 - rýchlosť deformácie 0,1 bunky načítajte súbor „ Temp_500_Strain_rate_0.1.dat“.

Pre teplotu 500 - rýchlosť deformácie 0,5 bunky, vložte súbor " Temp_500_Strain_rate_0.5.dat".

Pre teplotu 500 - rýchlosť deformácie 1 bunka, vložte súbor " Temp_500_Strain_rate_1.dat".

Pre teplotu 700 - rýchlosť deformácie 0,1 bunky načítajte súbor „ Temp_700_Strain_rate_0.1.dat“.

Pre teplotu 700 - rýchlosť deformácie 0,5 bunky, vložte súbor " Temp_700_Strain_rate_0.5.dat".

Pre Temperature 700 - Strain rate 1 cell, load " Temp_700_Strain_rate_1.dat " file, after defining data click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to Close.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0005.jpg' | relative_url }})

Stránka experimentálnych údajov

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0006.jpg' | relative_url }})

Po definovaní údajov o napätí prietoku pre každú bunku

## Definujte korekciu tepelnej kapacity

V strome úloh „Flow stress“ kliknite na stránku „**Experimentálne údaje** “. Ak zvážime účinok tepelnej kapacity výberom možnosti „**Áno** “ na tejto stránke, údaje o napätí prietoku sa opravia na základe adiabatického vykurovacieho účinku. Teplota sa nastaví pomocou ![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/eq_1.jpg' | relative_url }}) a príslušné údaje o napätí prietoku sa upravia. Pre toto laboratórium nebudeme používať korekciu tepelnej kapacity, preto zvoľte prepínač „**NO * * “.

## Definujte údaje o odbere vzoriek

V strome úloh „Flow stress“ kliknite na „**Sampling** “. input„ * * 10 * * “as number of strain, **0.1** as **Minimum* ***strain** , **1** as **Maximum****strain** a **0** as **Zero*** *strain***offset**. Vyberte„ ** Krivky napätia vzorkovaného prietoku ** “a potom kliknite na tlačidlo„ **Odber vzoriek** “. Program zobrazí krivku napätia prietoku v definovanom rozsahu deformácie.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0007.jpg' | relative_url }})

Stránka kontroly odberu vzoriek

## Konverzia modelu prietokového napätia

V strome úloh „Flow stress“ kliknite na stránku „**Conversion of flow stress model** “. Na stránke „**Konverzia modelu prietokového napätia ** “ si používateľ môže vybrať, ktorý model prietokového napätia chce prispôsobiť, v tomto laboratóriu vyberieme rovnicu **Johnson-Cook**:

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/eq_2.jpg' | relative_url }})

Pre metódu montáže zvoľte „** metóda kvázi najmenšieho štvorca ** “, zadajte počiatočný parameter guess, kliknutím na „* * Fit * * “ vygenerujte namontované parametre, ako aj krivku napätia prietoku pomocou namontovaných parametrov. Pre každý parameter sa používateľ môže rozhodnúť, či ho prispôsobí alebo opraví bez montáže. Pre každý parameter je k dispozícii aj posuvná lišta, ktorá umožňuje používateľovi upraviť hodnoty parametrov a zobraziť výsledky parametrickej štúdie. Na nasledujúcom grafickom zobrazení sú pôvodné experimentálne údaje reprezentované bodmi a údaje modelu sú reprezentované plnými čiarami (pozri obr. FSL1.9.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0008.jpg' | relative_url }})

Konverzia stránky modelu napätia prietoku

vzoru.

Kliknite na „**Výstup** “ v strome úloh, definujte „**Materiál NO** “ a „** Názov materiálu ** “, ako je znázornené na obr. FSL1.10. uložiť výstup do súboru s kľúčom a použiť ho v MKP. Kliknutím na tlačidlo „**Save keyword for flow stress** “ uložíte súbory kľúčových slov do adresára určeného cestou k súboru. Do zadaného adresára sa uložia dva súbory kľúčov, súbory **FSTRES.KEY* * a **FSTRES_SAMPLED_TABULATE.KEY* *.

**FSTRES.KEY** bude mať vybrané údaje modelu napätia prietoku.

**FSTRES_SAMPLED_TABULATE.KEY** bude mať údaje o odbere vzoriek (model napätia toku tabuľkového formátu údajov).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0009.jpg' | relative_url }})

Výstupná stránka napätia prietoku
