---
lang: sk
title: "26.6.19. Nastavenie animácie"
---

# 26.6.19. Nastavenie animácie ![]({{ '/assets/icons/post_icons/mo_animation_icon.jpg' | relative_url }})

Výsledky modelu je možné zobraziť ako súvislý rad obrázkov a animačných súborov v štandardných formátoch určených na prezentácie. K týmto funkciám sa dostanete cez ikonu ![]({{ '/assets/icons/post_icons/mo_animation_icon.jpg' | relative_url }}) (Nastavenie animácie). Dialógové okná nastavení animácie umožňujú používateľom ukladať obrázky do definovaného umiestnenia v konkrétnom formáte a rozlíšení (pozri obr. 26.6.19.1., obr. 26.6.19.2. a obr. 26.6.19.3.). Od verzie 12.xx je možné animáciu uložiť aj vo formátoch HTML, Movie a štandardnom formáte súborov programu PowerPoint (pozri obr. 26.6.19.3.).

Na karte **Všeobecné** môže používateľ v poli Názov súboru zadať názov súboru; pomocou tlačidla Prehľadávať môže vybrať adresár, do ktorého sa má animácia uložiť. Vybraná cesta sa zobrazí v poli Adresár (pozri obr. 26.6.19.1.).

Po vytvorení súboru prezentácie (.pre) sa aktivuje tlačidlo „Upraviť v editore prezentácií“ ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}). Kliknutím na toto tlačidlo spustíte editor prezentácií. Ďalšie informácie týkajúce sa editora prezentácií nájdete v [26.6.23. Presentation Editor](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_6_23_presentation_editor/)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_19_animation_setup/image001.jpg' | relative_url }})

Okno „Všeobecné nastavenia animácie“

Na karte **Nastavenia** môže používateľ nastaviť trvanie rámcov pre „Oneskorenie začiatku animácie“, „Oneskorenie konca animácie“, „Oneskorenie začiatku operácie“, „Oneskorenie konca operácie“ a „Interval medzi krokmi“. Trvanie sa uvádza v „msec“.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_19_animation_setup/image002.jpg' | relative_url }})

Okno nastavení animácie

Na karte **Export** môže používateľ nastaviť veľkosť a formát obrázku, ktorý sa má exportovať. Veľkosť obrázku je možné nastaviť pomocou možnosti „Nastavenie obrázku“. Veľkosť videa je možné zmeniť pomocou možnosti Veľkosť obrázku; teraz je k dispozícii aj možnosť Film s aktualizovanými formátmi videa, ako sú formáty WMV (verzia 9) a MP4 (H.264). Pomocou možnosti MS PowerPoint môže používateľ tiež exportovať animáciu do súboru .PPT.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_19_animation_setup/image003.jpg' | relative_url }})

Okno na export nastavení animácie so správou o riešení problémov

Pri vytváraní animácie môžeme vidieť, že sa v priečinku, do ktorého sa animácia ukladá, vytvorí súbor vo formáte *.pre. Používateľ môže súbor s príponou „.pre“ otvoriť pomocou prehrávača DEFORM Presentation.   
Animované súbory DEFORM (.pre) fungujú ako „flipbook“. Na nižšie uvedenom obrázku je znázornená štruktúra súboru .pre; používateľ môže súbor .pre upravovať ručne. Obrázky vo formáte PNG pre každý vybraný krok sa uložia do priečinka „Images“.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_19_animation_setup/image004.jpg' | relative_url }})

Formát súboru .pre

  
**Vytvorenie filmového súboru z formátu .pre pomocou príkazového riadku**  
Pomocou existujúceho súboru .pre môže používateľ znovu vygenerovať filmové súbory pomocou programu DEF_MOVIE.exe v príkazovom riadku. Keď sa súbor DEF_MOVIE.EXE otvorí v príkazovom riadku, používateľ uvidí formát, ako je znázornené nižšie. 

„Nástroj na vytváranie filmových súborov od spoločnosti DEFORM(TM)“  
Verzia 12.0

DEF_MOVIE formát názov_súboru1 názov_súboru2 {voľba} {rozlíšenie}

formát filmového súboru  
wmv – formát WMV (zastaraný)  
avi – formát AVI (zastaraný)  
adv – Rozšírené možnosti formátovania  
filename1 – názov vstupného súboru (*.pre)  
filename2 – názov výstupného súboru (*.wmv, *.avi, *.mp4)  
{option} ovládanie rozlíšenia  
pre formát WMV  
1 – nízke rozlíšenie (320×240)  
2 – vysoké rozlíšenie (640×480)  
pre formát AVI  
1 – bez kompresie  
2 – MPG4  
pre pokročilé nastavenia formátu  
1 – WMV (verzia 9)  
2 – MP4 (H.264)  
{rozlíšenie}  
pre rozlíšenie formátu Advanced  
1 – Použiť veľkosť obrázku  
2 – 320 × 240  
3 – 640 × 480  
4 – 800 × 600  
5 – 1024 × 768  
6 – 1280 × 720  
7 – 1600 × 1200  
8 – 1920 × 1080 

Príklad vytvorenia filmového súboru pomocou príkazového riadku:  
„<cesta k inštalácii programu Deform>\ DEF_MOVIE.exe adv spike.pre spike.wmv 1 1 “
