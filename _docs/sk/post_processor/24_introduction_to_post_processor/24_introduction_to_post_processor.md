---
lang: sk
title: "24. Úvod do postprocesora"
---

# 24\. Úvod do postprocesora

Postprocesor DEFORM slúži na vyhodnocovanie výsledkov simulácie. Ide o integrovaný postprocesor vybavený novým užívateľsky prívetivým grafickým rozhraním, ktorý ponúka väčšinu existujúcich funkcií na spracovanie výsledkov simulácie, ako aj nové funkcie.

Postprocesor DEFORM poskytuje prostredie s novými funkciami, ktoré používateľovi umožňujú generovať 3D PDF správy s výsledkami simulácií, [ coupon data extraction](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/), interpretovať výsledky v rámci databázy pomocou [PIP](../26_post_processing_tools_and_controls/26_1_file_operations_in_post_processor.htm#26_1_1_Working_with_DB_in_PIP_mode), znázorniť výsledky v oblasti záujmu, [CA microstructure modelling](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_10_ca_model_setup/) a vykonávať následné spracovanie [report generation](/docs/en/post_processor/28_report_generation/28_report_generation/) (formáty súborov .pdf a .ppt) s vopred definovanými užívateľskými nastaveniami.

Postprocesor s celou radou funkcií a grafických prvkov umožňuje inžinierom overovať výsledky modelovania a prezentovať ich spôsobom, ktorý umožňuje efektívne porozumieť týmto výsledkom. V tejto časti sú uvedené stručné informácie o systéme a dostupných funkciách.

S každou novou verziou sa systém vylepšuje tak, aby spĺňal požiadavky odvetvia a špecifické požiadavky používateľov.

Informácie, ktoré sú k dispozícii z postprocesora, zahŕňajú:

  * Deformovaná geometria, vrátane pohybov nástroja a deformovanej siete v každom uloženom kroku.

  * [Contour plots](../26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables.htm#Display_options): Čiarové a tieňované kontúry znázorňujú rozloženie akýchkoľvek stavových veličín, vrátane napätia, deformácie, teploty, poškodenia a ďalších.

  * [Vector plots](../26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables.htm#Display_options): Vektory posunutia a rýchlosti udávajú veľkosť a smer posunutia alebo rýchlosti pre každý uzol v každom kroku počas celého procesu.

  * Grafy kľúčových premenných, ako sú tlakové zaťaženia, objemy, teplota, obsah atómov, tvrdosť a bodovo sledované stavové premenné.

  * [Point tracking](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_9_point_tracking/) na znázornenie pohybu materiálu a vykreslenie grafov správania stavových premenných v týchto bodoch.

  * [Flow net](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/) znázorňuje vzory toku materiálu na rovnomernej mriežke. Vo všeobecnosti ide o veľmi dobrý prediktor vzorov toku zŕn v hotovom diele.

  * Pre akúkoľvek stavovú premennú je možné vytvoriť graf typu [histogram](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables/), aby bolo možné zobraziť rozloženie danej stavovej premennej v celom telese.

  * Funkcia [3D View Mode](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_20_3d_setup/) slúži na vizualizáciu 2D objektov v 3D prostredí, a to buď otáčaním, alebo vytláčaním.

  * Interaktívne rozrezávanie 3D objektu s cieľom pochopiť vnútorné vlastnosti a rozloženie stavových premenných.

  * [Coupon data extraction](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/) na vyhodnotenie rezov v kritických miestach z hľadiska mikrostruktúry a reakcie mechanických vlastností.

  * Výsledky je možné znázorniť v oblasti záujmu definovaním ľubovoľného tvaru, čo slúži na získanie minimálnych a maximálnych hodnôt stavových premenných z konkrétnej časti objektu.

  * Výsledky interaktívneho následného spracovania je možné preniesť do súborov správ (vo formátoch .pdf a .ppt) s vopred definovanými užívateľskými nastaveniami.

  * Modely bunkových automatov (CA) sú synchronné algoritmy, ktoré opisujú diskrétny priestorový a časový vývoj komplexných systémov prostredníctvom uplatňovania lokálnych (alebo mezoskopických, strednodobých) deterministických alebo pravdepodobnostných transformačných pravidiel na bunky mriežky s lokálnou prepojenosťou s cieľom predpovedať veľkosť zŕn.

  * Nové možnosti [Multi viewports](../26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor.htm#Multi_Viewports), [Database comparison](../26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor.htm#Fig_26_2_3_DB_comparison) a „Prepojiť/Synchronizovať“ pre zobrazenie viacerých okien boli pridané a tieto možnosti je možné využiť na súčasné prezeranie viacerých databáz v programe NG Post.

Stavové premenné, geometrické údaje a obrazové údaje je možné tiež exportovať v rôznych neutrálnych formátoch na použitie v iných programoch.

## Otvorenie databázy na účely následného spracovania

Ak zložka s problémom obsahuje databázu, v hlavnom okne grafického rozhrania sa zobrazí možnosť ![]({{ '/assets/icons/pre_icons/2d_3d_post_label.jpg' | relative_url }}). Ak chcete otvoriť simulovanú databázu v postprocesore z hlavného okna grafického rozhrania, kliknite na ![]({{ '/assets/icons/pre_icons/2d_3d_post_label.jpg' | relative_url }}) v časti Post-Processor alebo na ![]({{ '/assets/icons/pre_icons/2d_3d_post_icon.jpg' | relative_url }}) v zozname na paneli nástrojov, ako je znázornené na obr. 24.1.

![]({{ '/assets/images/post_processor/24_introduction_to_post_processor/image001.jpg' | relative_url }})

Spustenie postprocesora z hlavného okna grafického rozhrania

**Súvisiace témy:**

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

[26\. Post Processor Features](/docs/en/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/)

[28\. Report Generation](/docs/en/post_processor/28_report_generation/28_report_generation/)
