---
lang: sk
title: "26.6.17. Extrakcia údajov"
---

# 26.6.17. Extrakcia údajov ![]({{ '/assets/icons/post_icons/mo_data_extraction_icon.jpg' | relative_url }})

  
[2D, 3D]: Táto funkcia v postprocesore umožňuje používateľovi extrahovať ľubovoľnú premennú modelu pre daný objekt v danom kroku do textového súboru. (Pozri obr. 26.6.17.1.) Od verzie DEFORM -V12 môže používateľ extrahovať údaje o stavových premenných na základe súradnicového systému, ktorý sa používa na vykresľovanie stavových premenných na stránke „Stavové premenné“. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_17_data_extraction/image001.jpg' | relative_url }})

Okno na extrakciu údajov

**Typ údajov**: Informácie je možné zapísať vo formáte ASCII do výstupného súboru. Je možné extrahovať nižšie uvedené položky. V prípade objektov so sieťou ide o typické stavové premenné, zatiaľ čo v prípade objektov s tuhou matricou je možné extrahovať aj údaje o zdvihu zaťaženia.

**Údaje o objektoch**: Okrem toho je možné vybrať konkrétne kľúčové slová z údajov o objektoch, ako aj objekty, z ktorých sa majú údaje extrahovať. 

**Výstup**: Informácie je možné exportovať buď do jedného súboru, alebo ich rozdeliť do viacerých súborov. 

**Kroky**: Je možné vybrať jednotlivé kroky alebo všetky kroky. Ak chcete vybrať konkrétny krok, označte ho v roletovom menu krokov v pravej časti obrazovky. Ak potrebujete 5 alebo 6 krokov a nechcete všetky kroky v databáze, použite klávesy na klávesnici a vyberte požadované kroky v zozname krokov v okne extrakcie údajov.

**Súbory**: Informácie je možné uložiť do jedného alebo viacerých súborov. Túto možnosť je vhodné využiť v prípade, ak potrebujete informácie z viac ako jedného kroku. Dáta je možné uložiť do jedného súboru alebo do viacerých súborov s názvami typu name0001.DAT, name0002.DAT atď. 

**Dátový súbor**: Názov súboru, predvolene je to DEFORM.DAT. Tento súbor je možné premenovať alebo pomocou funkcie „Vyhľadať“ vyhľadať existujúci súbor.

**Extrahovať**: Po výbere požadovaných informácií stlačte tlačidlo „Extrahovať“, aby ste informácie extrahovali.
