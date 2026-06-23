---
lang: sk
title: "26.1. Práce so súbormi v postprocesore"
---

# 26.1. Práce so súbormi v postprocesore

26.1.1. Práca s databázou v režime PIP

Na nižšie uvedenom obr. 26.1.1. sú zobrazené možnosti **ponuky Súbor**,

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/image001.jpg' | relative_url }})

Možnosť v ponuke „Súbor“ v postprocesore

**Nové** ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) (Ctrl + N): Načíta súbor databázy. Túto funkciu je možné spustiť aj z ponuky Súbor > Nástroje.

**Otvoriť**..![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}) (Ctrl + O): Načíta databázový súbor a uložený súbor relácie programu DEFORM. K tejto funkcii sa dostanete aj cez ponuku Súbor > Nástroje.

**Uložiť**![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) (Ctrl + S): Uloží súbor relácie. Túto funkciu je možné spustiť aj z ponuky Súbor > Nástroje.

**Uložiť ako...** : Uloží súbor relácie do vybraného adresára pod názvom zadaným používateľom.

**Import databázy (PIP)**![]({{ '/assets/icons/post_icons/mo_import_database_in_pip_icon.jpg' | relative_url }}) (Ctrl+Shift+D): Funkcia „obraz v obraze“ je užitočná na porovnávanie dvoch alebo viacerých databáz, alebo na porovnávanie rôznych fáz v rámci jednej databázy pri rôznych hodnotách stavových premenných. Pomocou tejto možnosti môže používateľ importovať viac ako jednu databázu v rámci jednej relácie pomocou ikony (Importovať databázu v PIP) na paneli nástrojov v hlavičke.

Ďalšie informácie nájdete 

**Export**: Uloží nastavenie úlohy vo formáte súboru .key. 

**Možnosť „Zložka“**: Otvorí pracovný adresár databázy v Průzkumníku Windows.

**Nastavenie obrázku** (Ctrl + M)**:** Slúži na nastavenie aktuálneho zobrazovacieho okna alebo pracovného priestoru na požadovanú veľkosť v pixeloch a na zachytenie obrázkov do požadovaného umiestnenia v požadovanom formáte. Túto funkciu je možné otvoriť aj z ponuky Súbor > Nástroje. (Pozri obr. 26.1.2.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/image002.jpg' | relative_url }})

Vyskakovacie okno „Nastavenie obrázku“

**Zachytiť obraz** ![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }}) (Ctrl + I): Uloží aktuálny obraz obrazovky do súboru v zadanom formáte.

**Uloženie obrázku do schránky**![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}) (Ctrl + Shift + I): Táto funkcia uloží aktuálny obrázok obrazovky do schránky. (V operačnom systéme Windows Vista na PC táto funkcia pri niektorých ovládačoch grafickej karty funguje iba v režime „Windows Vista Basic“ v nastaveniach personalizácie systému).

**Nedávne projekty**: Táto voľba slúži na otvorenie posledných desiatich predtým otvorených databáz.

**Zatvoriť** (Ctrl+W): Zatvorí aktuálny pracovný projekt, ale neukončí prevádzku preprocesora.

**Ukončiť** (Ctrl+Q): Slúži na ukončenie postprocesora.

Informácie o možnostiach v **ponuke Viewport** a **ponuke Windows****** nájdete v kapitole [26.2. Viewports and Windows Menu](/docs/en/post_processor/26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor/).

Informácie o možnostiach **Ponuka „Display“**** a **Ponuka „Mouse“**** nájdete v kapitole [26.3. Object Display Controls](/docs/en/post_processor/26_post_processing_tools_and_controls/26_3_object_display_controls/).

Informácie o možnostiach v **ponuke „Kroky“** nájdete v kapitole [ 26.4. Simulation Step Display Controls](/docs/en/post_processor/26_post_processing_tools_and_controls/26_4_simulation_step_display_controls/)

Informácie o možnostiach v **ponuke „Options“** nájdete v kapitole [26.5. PostProcessing Options Menu](/docs/en/post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options/)

Informácie o možnostiach v **ponuke Nástroje** nájdete v kapitole [26.6. Post Processing tools](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_post_processing_tools/)

Informácie o možnostiach v **ponuke „Sekcie“** a **ponuke „Správa“** nájdete v [27\. Introduction to Report Generation](/docs/en/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/)

Informácie o možnostiach v **Dock****Widgets****menu** nájdete v kapitole [25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/), v časti [25.5. Dock Widget menu](../25_post_processor_layout/25_post_processor_layout.htm#25_5_Dock_Widget_menu)

## Práca s databázou v režime PIP

Funkcia „obraz v obraze“ (PIP) je užitočná na porovnávanie dvoch alebo viacerých výsledkov z databázy alebo výsledkov tej istej databázy v rôznych krokoch pri rôznych stavových premenných. Pomocou tejto možnosti môže používateľ importovať viac ako jednu databázu v tej istej relácii pomocou ikony ![]({{ '/assets/icons/post_icons/mo_import_database_in_pip_icon.jpg' | relative_url }}) (Importovať databázu v PIP) z panela nástrojov v hlavičke, ako je znázornené na obr. 26.1.3.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image003.jpg' | relative_url }})

Možnosť „Importovať databázu do PIP“ na paneli nástrojov

Importovaná databáza sa otvorí v grafickom okne ako malý obrázok, ako je znázornené na obr. 26.1.4. Používateľ môže toto okno PIP zväčšiť, zmenšiť, pretiahnuť a presunúť pomocou ovládacích bodov.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image004.jpg' | relative_url }})

PIP v grafickom okne

Po výbere okna PIP sa okolo obrázka zobrazí rámček s bodkami; ak kurzor zostane v rámci tohto rámčeka, zobrazí sa ikona posúvania, a používateľ môže okno PIP presúvať ťahaním a púšťaním, ako je znázornené na obr. 26.1.6. Okno PIP je možné maximalizovať alebo minimalizovať ťahaním bodiek na okraji, keď sa zobrazí ikona šípky, ako je znázornené na obr. 26.1.5.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image005.jpg' | relative_url }})

Maximalizované okno PIP s možnosťou ťahania na maximalizáciu a minimalizáciu

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image006.jpg' | relative_url }})

Presunutý PIP s možnosťou posúvania

Okno PIP je možné tiež maximalizovať alebo minimalizovať tak, že kurzor ponecháte v rámci okraja a otočíte kolieskom myši.

Po výbere okna PIP môže používateľ prehrávať jednotlivé kroky, vykresľovať stavové premenné a grafy a porovnávať výsledky s hlavným grafickým oknom DB. (Pozri obr. 26.1.7. a obr. 26.1.8.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image007.jpg' | relative_url }})

Graf kontúrov stavových premenných v hlavnej aj v PIP databáze v rôznych krokoch pre 3D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image008.jpg' | relative_url }})

Graf obrysov stavových premenných v hlavnej aj v PIP databáze v rôznych krokoch pre 2D

**Objednávka** :

Používateľ môže usporiadať databázy PIP tak, aby sa lepšie zobrazovali, a to pomocou možnosti „Poradie“, ktorá je dostupná v kontextovom menu pravého tlačidla myši (RMB) pri položke PIP. Ponuka „Poradie“ obsahuje možnosti na posunutie vybranej databázy PIP dozadu alebo na jej presunutie do popredia atď. Možnosti dostupné v ponuke „Poradie“ sú znázornené na nižšie uvedenom obr. 26.1.9.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image009.jpg' | relative_url }})

Možnosť objednávky pre PIP DB

**Súvisiace témy:**

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

[26.2. Viewports and Windows Menu](/docs/en/post_processor/26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor/)

[26.3. Object Display Controls](/docs/en/post_processor/26_post_processing_tools_and_controls/26_3_object_display_controls/)

[26.4. Simulation Step Display Controls](/docs/en/post_processor/26_post_processing_tools_and_controls/26_4_simulation_step_display_controls/)

[26.5. PostProcessing Options Menu](/docs/en/post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options/)

[26.6. Post Processing tools](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_post_processing_tools/)
