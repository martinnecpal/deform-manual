---
lang: sk
title: "3.1. Nastavenie licencie Deform"
---

# 3.1. Nastavenie licencie DEFORM

Pre verziu DEFORM-Integrated 2D3D bol implementovaný nový správca licencií DEFORM. Tento nový správca licencií sa označuje ako server správcu licencií, čo znamená, že tento server sa môže nachádzať na centrálnom mieste v sieti a poskytovať licencie viacerým klientským počítačom. Dávková fronta beží na tom istom počítači ako správca licencií a posiela úlohy na simulačný server (ktorý môže byť na rýchlejšom počítači s dostatočnými zdrojmi na spracovanie úloh FEM). Potrebné podrobnosti nastavenia sú stručne vysvetlené v tejto časti. V jednoduchej konfigurácii môžu byť všetky servery na tom istom počítači.

3.1.1. Požiadavky na konfiguráciu počítača

3.1.2. Umiestnenie počítačov v nastavení DEFORM

3.1.3. Ako nastaviť novú konfiguráciu licencie

## Požiadavky na konfiguráciu počítača

**Simulačný server:** Centrálny počítač - pravdepodobne vysoko výkonný - na vykonávanie výpočtov MKP.

**Licenčný server** : Centrálny počítač - nie nevyhnutne výkonný - na správu licencií.

**Server s frontom dávok** : Centrálny počítač na správu postupnosti úloh. Dávkové, licenčné a simulačné servery môžu byť spustené na tom istom počítači alebo simulačný server môže byť spustený na inom počítači.

**Pre / Post klient(y)** - Počítač, na ktorom budú používatelia pred a po spracovaní simulácií. Na tomto počítači sa vykonávajú programy pred a po spracovaní.

## Umiestnenie počítača v nastavení DEFORM

**Spustenie nastavenia DEFORM**

Na karte Simulačný server musí používateľ pridať systém simulačného servera, na ktorom sa budú spúšťať úlohy odoslané v dávkovom režime. Systém simulačného servera môže byť lokálny systém alebo akýkoľvek vzdialený vysokovýkonný systém, používateľ môže pridať simulačný server kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), pozri obr. 3.1.13. Ak ide o viacprocesorový alebo viacjadrový stroj, zadajte počet dostupných a licencovaných procesorov (jadier) v DEFORM (Číslo procesora) a maximálny počet úloh, ktoré by používateľ chcel spustiť súčasne na tomto kĺbovom systéme na základe výkonu systému (predvolené nastavenie je 1) tlačidlo. Ak ide o viacprocesorový alebo viacjadrový stroj, zadajte počet procesorov (jadier) dostupných a licencovaných v DEFORM (Číslo procesora) a maximálny počet úloh (predvolená hodnota je 1).

**V porovnaní s predchádzajúcimi verziami sú tu uvedené dôležité zmeny:**

**Umiestnenie priečinka správcu licencií, v ktorom sa má nachádzať súbor s heslom (DEFORM.PWD)**

  * Staré verzie (do 2DV91 alebo 3DV61) C:\Program Files\DEFORM License Manager 3.1
  * Aktuálne vydanie C:\Program Files\SFTC\Licence Manager

**Umiestnenie simulačného servera a spustiteľného súboru registrácie MPICH**

  * Staré verzie do 2DV91 alebo 3DV61 C:\Program Files\DEFORM License Manager 2.1 a do v10.2.1 v C:\Program Files\SFTC\Licence Manager
  * Aktuálne vydanie C:\Program Files\SFTC\DEFORM\Konfigurácia

Po inštalácii ovládača ochrany Sentinel sa spustí inštalácia správcu licencií a používateľ bude vyzvaný na zadanie súboru s heslom. Inštalátor skopíruje súbor s heslom na príslušné miesto a s hardvérovým kľúčom na mieste program servera License Manager overí kombináciu hesla a hardvérového kľúča. Počas tohto procesu je dôležité najprv odinštalovať predchádzajúcu kópiu programov s rovnakým číslom verzie.

**Nastavenie simulačného servera:**

(inštalácia týchto služieb je súčasťou predvoleného procesu inštalácie a tu uvedené údaje sú len záložné možnosti, ak má daný systém nejaké problémy/obmedzenia s obsluhou služieb)

Ako správca spustite súbor "InstallBatchQueueServer.bat" v počítači so serverom dávkovej fronty. (pri použití predvolenej inštalačnej cesty je typické umiestnenie tohto dávkového súboru C:\Program Files\SFTC\License Manager\\)

Od verzie 14.0 sa skript "InstallBatchQueueServer.bat" považuje za starší, namiesto toho sa na pridanie služieb Licenčný server a Dávkový server fronty používa skript "InstallServers.bat".

Počas vykonávania skriptu môže používateľ pozorovať nasledujúce hlásenia označujúce použitie súboru:

_"Použitie:_

"InstallServers.bat Y" - Nastavte licenčný server a server dávkovej fronty.

"InstallServers.bat N" - Nastavte iba licenčný server.

"InstallServers.bat" - Zobrazí výzvu, či sa má nastaviť server dávkovej fronty alebo nie.

Tým sa nainštaluje služba licenčného servera DEFORM.

Chcete nainštalovať aj službu Batch Queue Server? (Áno, Nie, Ukončiť) [Y,N,Q]?

Ak zadáme "Y", nainštaluje sa licenčný server aj server dávkovej fronty, ak zadáme "N", nainštaluje sa len licenčný server a ak zadáme "Quit", ukončí sa časť vykonávania skriptu.

Od verzie 11.2 sa služba systému Windows "DeformSimServer" nevyžaduje.

  1. Službu Windows "DeformSimServer" nemusíme inštalovať.
  2. Ak je služba Windows "DeformSimServer" už nainštalovaná, nemusíme ju spúšťať. Je **normálne**, ak je služba systému Windows "DeformSimServer" **zastavená**.

Používatelia programu DEFORM by mali použiť DEFORMSetup (v záložke "Služby DEFORM") na kontrolu stavu simulačného servera DEFORM a ostatných služieb DEFORM.

**Ako spustiť staršie verzie pomocou nového správcu licencií**

**Podľa 2D V9.1 a 3D V6.1**

Spustite DLConfig.exe z C:\Program Files (x86)\DEFORM License Manager 2.1 (v 64-bitových počítačoch) a C:\Program Files\DEFORM License Manager 2.1 (v 32-bitových počítačoch) a zadajte názov nového servera a číslo portu 34445.

**Nad verziou Deform 10.X a pod verziou Deform v11.1**

Nainštalujte program Deform Service Control z inštalačného programu Deform. Spustite program DeformSetup z C:\Program Files\SFTC\DEFORM\V10.X. V záložke Simulation Server pridajte systém simulačného servera. Vyberte možnosť Versions (Verzie) zo stromu Simulačný server a pridajte verziu. Vyberte pridanú verziu a zmeňte ju na starú verziu výberom čísla starej verzie z rozbaľovacej ponuky a jej umiestnenia inštalácie. Po dokončení kliknite na kartu Deform Services (Deformovacie služby) a vyberte položku Open DEFORM service for Local Computer (Otvoriť službu DEFORM pre lokálny počítač). Kliknutím na tlačidlo Update (Aktualizovať) aktualizujte súbory v priečinku Configuration (Konfigurácia) pomocou tlačidla Update (Aktualizovať) vedľa systému Simulation Server (Simulačný server) v časti Deform Computer (Počítač Deform). Teraz je systém pripravený na spustenie starších verzií programu DEFORM.

## Ako nastaviť novú konfiguráciu licencie

  
**Krok 1**

Keďže správcu licencií inštalujeme do serverového počítača, spustite inštaláciu systému DEFORM a pokračujte až na stránku s výberom komponentov a z rozbaľovacej ponuky vyberte možnosť "Inštalácia servera", ako je znázornené na obr. 3.1.1. Inštalátor DEFORM teda nainštaluje podporné kódy (Python a ovládač ochrany Sentinel) a potom spustí inštaláciu správcu licencií.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image023.jpg' | relative_url }})

Deformovať okno Vybrať komponenty (nie je povinný krok pre oficiálnu verziu v11.0.2)

Ak stará verzia správcu licencií nie je odinštalovaná, inštalátor odporúča odinštalovať starého správcu licencií pred inštaláciou nového správcu licencií, ako je znázornené na obr. 3.1.2.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image022.jpg' | relative_url }})

Upozornenie na inštaláciu správcu licencií (nie je povinným krokom pre oficiálnu verziu v11.0.2)

Zapnite možnosť Konfigurácia brány firewall systému Windows. Brána firewall systému Windows musí byť nakonfigurovaná tak, aby povolila službu License and Batch queue cez bránu firewall systému Windows, ako je znázornené na obr. 3.1.3., a potom kliknite na tlačidlo **Next**.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image025.jpg' | relative_url }})

Konfigurácia stránky brány Windows Firewall

Počas inštalácie programu DEFORM License Manager systém vyzve používateľa na zadanie hesla DEFORM (pozri obr. 3.1.4), používateľ môže vyhľadať umiestnenie súboru DEFORM.PWD pomocou tlačidla Browse. Keď používateľ klikne na tlačidlo Next (Ďalej), heslo sa skopíruje do priečinka License Manager (Správca licencií) z vyhľadaného umiestnenia. Súčasťou inštalácie je automatické spustenie servera DeformLicenseServer.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image024.jpg' | relative_url }})

DEFORM okno na zadávanie hesla

_**Poznámka:**_

_Ak používateľ nemá heslo v čase inštalácie, musí heslo ručne vložiť do priečinka Správca licencií a musí spustiť dávkový súbor správcu licencií, aby aktivoval službu DeformLicenseServer._

Zapnite server Inštalácia dávkovej fronty. Dávkový front je potrebný na zoraďovanie simulácií do frontu, ako je znázornené na obr. 3.1.5., a potom kliknite na tlačidlo **Ďalej**.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image028.jpg' | relative_url }})

Dodatočné okno výberu úlohy DEFORM License Manager

Skontrolujte výbery nastavení aplikácie License Manager a kliknutím na tlačidlo **Install** spustite inštaláciu. V opačnom prípade sa vráťte späť a zmeňte nastavenia. (Pozri obr. 3.1.6.)

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image026.jpg' | relative_url }})

Okno potvrdenia inštalácie programu DEFORM License Manager

Ak má daný systém nejaké problémy/obmedzenia s obsluhou služby DeformLicenseServer, potom ako správca spustite súbor "InstallServer.bat" na počítači s licenčným serverom (dostupný v inštalačnej ceste, typické umiestnenie tohto dávkového súboru je C:\Program Files\SFTC\License Manager) pomocou príkazového riadku, ako je znázornené na obr. 3.1.7. Ako možnosť zadajte "N", ak chcete nainštalovať iba licenčný server Deform License Server.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image001.jpg' | relative_url }})

Registrácia a spustenie servera správcu licencií pomocou dávkového súboru

Ak má daný systém nejaké problémy/obmedzenia s obsluhou služby DeformBatchQueue, potom ako správca spustite súbor "InstallServer.bat" s voľbou "Y" na počítači licenčného servera (dostupný v predvolenej inštalačnej ceste, typické umiestnenie tohto dávkového súboru je C:\Program Files\SFTC\License Manager) pomocou príkazového riadku, ako je znázornené na obr. 3.1.8.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image002.jpg' | relative_url }})

Registrácia a spustenie správcu licencií a serverov dávkového frontu pomocou dávkového súboru s možnosťou "Y"

**Krok 2:**

Pri akýchkoľvek následných zmenách môže používateľ otvoriť dialógové okno DEFORMSetup (pozri obr. 3.1.9.), kde uvedie názov servera, názov počítača a číslo portu (34445). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_syncronize_button.jpg' | relative_url }}), aby ste sa uistili, že sa vráti správa Success (Úspech), čo je údaj o tom, že teraz bola nastavovacím programom identifikovaná platná kombinácia License key (Licenčný kľúč), password file (Súbor hesiel). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) na vyskakovacie hlásenie, čím sa aktivujú ďalšie následné karty údajov (Simulation (Simulácia) a Shared folder (Zdieľaný priečinok)) a uložte nastavenia pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}). (Pozri obr. 3.1.10.). Po kliknutí používateľa na tlačidlo Save (Uložiť) sa aktivuje karta Deform Services (Deformačné služby), pre následné otvorenie dialógového okna DEFORMSetup zostane karta Deform Services (Deformačné služby) aktivovaná.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image003.jpg' | relative_url }})

Zástupca ponuky Štart DEFORM Setup

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image004.jpg' | relative_url }})

Povinné vstupné polia na aktiváciu konfigurácie licencie

Po kliknutí na tlačidlo synchronizovať, ak aktuálny počítač nebol nastavený ako simulačný server s aktuálnou verziou a cestou, program DEFORM Setup ponúkne jeho pridanie. (Pozri obr. 3.1.11.)

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image009.jpg' | relative_url }})

Okno DEFORM Setup License Server

Ak kliknutím na tlačidlo **Ano** pridáte simulačný server, program DEFORM Setup automaticky neuloží zmenu licenčného servera, ale vyzve na uloženie zmien. (Pozri obr. 3.1.12.) Pred uložením nastavení skontrolujte, či je zmena správna na karte Simulation Server (Simulačný server).

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image029.jpg' | relative_url }})

DEFORM Pripomienka nastavenia na uloženie

**Krok 3:**

Karta Simulačný server umožňuje používateľom spravovať simulačné servery pripojené k licenčnému serveru. Ako je znázornené na obr. 3.1.13., v hornej oblasti karty sú zobrazené definované simulačné servery. Ak miestny počítač nie je definovaný ako simulačný server, kliknite na tlačidlo "Pridať simulačný server", aby ste ho definovali.

Pri pridávaní simulačného servera sa v predvolenom nastavení zachytí a pridá názov miestneho počítača spolu s niektorými predvolenými hodnotami pre typ procesora, počet procesorov, maximálny počet úloh a najnovšia verzia dostupná v miestnom systéme sa automaticky nastaví na aktuálnu cestu.

Ak je server Správcu licencií na tom istom počítači, na ktorom sa spúšťa program DEFORM Setup, je možné definovať toľko simulačných serverov, koľko je potrebné. Ak sa však server License Manager nachádza na inom počítači, je možné definovať a upravovať iba miestny simulačný server.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image007.jpg' | relative_url }})

Okno DEFORM Setup Simulation Server

Na karte Simulácie,

  * Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) možno použiť na pridanie simulačného servera.

  * Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) možno použiť na odstránenie lokálneho simulačného servera.

  * Adresa zobrazuje názov počítača pripojeného k aktuálnemu správcovi licencií, na ktorom je spustený simulačný server.

  * Stĺpec Verzie zobrazuje zoznam všetkých verzií definovaných pre daný simulačný server.

  * Možnosť Maximum Jobs umožňuje nastaviť počet úloh vo fronte, ktoré môžu byť spustené súčasne na príslušnom simulačnom serveri.

  * Maximálny počet procesorov, ktoré možno použiť, by mal byť rovnaký alebo menší ako licencovaný.

  * Port TCP, na ktorom je spustený licenčný server.

  * Verzie DEFORM aktuálne nainštalované v príslušných systémoch.

V dolnej časti sa zobrazujú podrobnosti o aktuálne vybranom simulačnom serveri. (Pozri obr. 3.1.14.) Na karte Verzie je možné pridať umiestnenie disku pre viacero verzií pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) alebo odstrániť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}), pričom pre jednu verziu je povolená len jedna cesta.

Ak je typ procesora definovaný ako Klaster, karta Klastery sa aktivuje a je možné definovať podrobnosti o uzloch klastra. Po vykonaní zmien na karte Simulation Server (Simulačný server) kliknite na tlačidlo Save (Uložiť), čím uložíte nastavenia.

V systéme Windows môže používateľ určiť umiestnenie inštalácie viacerých verzií (V12.1, V12.0, V11.3, v11.2, v11.1,v11.0 a v10) pre každý simulačný server, ak chce používateľ používať staršie verzie (pozri obr. 3.1.14.). Rôzne verzie môže používateľ pridať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), vybrať číslo verzie z rozbaľovacej ponuky a potom zadať informácie o inštalačnej ceste pre každú verziu, ktorá sa použije na spustenie úloh z príslušnej verzie pri odoslaní v dávkovej fronte. V systéme Linux/UNIX však môže používateľ zadať len jednu verziu.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image006.jpg' | relative_url }})

Okno DEFORM Setup Simulation Server

Používateľ by sa mal uistiť, že služba Simulation Server je spustená, ak nie je spustená, môže navštíviť kartu DEFORM Services a spustiť miestny simulačný server kliknutím na tlačidlo [Start], ktoré je k dispozícii vedľa simulačného servera v zozname Deform Computers. Simulačné servery, ktoré možno použiť na spustenie vybranej úlohy, sú uvedené v dialógovom okne Možnosti spustenia, ako je znázornené na obr. 3.1.15.

**Poznámka** : Informácie o inštalačnej ceste pre každú verziu je potrebné definovať tak, aby DB rôznych verzií zaradené do frontu pomocou Dávkového frontu mohli simulovať používanie príslušnej verzie.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image008.jpg' | relative_url }})

Okno Možnosti spustenia

**Krok 4:**

Prejdite na kartu Zdieľané priečinky. Každý zdieľaný priečinok je reprezentovaný stromom, ktorý identifikuje jeho zdieľané názvy na každom počítači, kde je prístupný (pozri obr. 3.1.16.).

Kliknite na tlačidlo "New Dir" (pozri 1 na obr. 3.1.16.) a zadajte názov počítača a miestnu cestu, kde sa zdieľaný priečinok fyzicky nachádza. Napríklad zdieľaný priečinok je C:\Deform\Problem na počítači s názvom "FastServer". Ako názov počítača uveďte "Fast Server" a ako cestu "C:\Deform\Problem". Skontrolujte, či ste písali. V súčasnosti neexistuje žiadna automatická kontrola, ktorá by zabezpečila, že zadaná cesta skutočne existuje.

Teraz kliknite na tlačidlo "Pridať zdieľaný bod" (pozri 2 Obr. 3.1.16.). Zadajte názov klientského počítača a názov cesty v tomto počítači. Predpokladajme, že cesta je definovaná na počítači "Klient1" ako mapovaná sieťová jednotka "Z:". Potom zadajte názov iného klientskeho (Pozri 3 na obr. 3.1.16. . )počítača ako "Client2" a názov priečinka ako "Q:" Nezabudnite uviesť dvojbodku (:).

Teraz kliknite na tlačidlo "Uložiť" (pozri 4 na obr. 3.1.16). Všetky tieto informácie sú uložené v počítači klienta a licenčného servera.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image027.jpg' | relative_url }})

Informácie o zdieľaných priečinkoch v okne nastavenia DEFORM

**Služby DEFORM:**

Ovládací program Deform Services sa inštaluje spolu s novou inštaláciou alebo sa môže nainštalovať nezávisle od inštalačného súboru DEFORM_Service_Control_vx.x.exe, ak chce používateľ komunikovať s novým správcom licencií. Používateľ si môže všimnúť kartu Deform Services pridanú v programe DEFORMSetup po inštalácii riadiaceho programu Deform Services. Servisný obslužný program DEFORM (DEC_SC.EXE) bude na počítači so systémom Windows spustený ako "služba". Riadiaci program Deform Service komunikuje so správcom licencií a možno ho použiť na monitorovanie nasledujúcich služieb,

Pre serverový počítač

Licenčný server

Dávkový server frontu

Webové riadenie služieb (nie je k dispozícii v systéme Linux)

Pre klientsky počítač

Simulačný klient

Simulačný server

Webové monitorovanie simulácie (nie je k dispozícii v systéme Linux)

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image016.jpg' | relative_url }})

Služby DEFORM v okne Nastavenie DEFORM

Na karte Služby DEFORM máme dve možnosti prístupu k počítačom so službami DEFORM (pozri obr. 3.1.17. ). Používateľ môže služby zobraziť v samostatnom okne kliknutím na tlačidlo **Otvoriť v novom okne**.

**Otvorenie služby DEFORM pre miestny počítač DEFORM** : Pomocou tejto možnosti môžeme monitorovať a ovládať služby len na lokálnom počítači. Ak je miestny počítač počítačom servera, potom môžeme vidieť zoznam servera DEFORM aj zoznam počítačov DEFORM (pozri obr. 3.1.18.), ale v klientskom počítači môžeme vidieť len zoznam počítačov DEFORM (pozri obr. 3.1.19.).

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image011.jpg' | relative_url }})

Služba DEFORM pre miestne okno počítača DEFORM v počítači Server

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image012.jpg' | relative_url }})

Služba DEFORM pre miestne okno počítača DEFORM v klientskom počítači

**Otvorenie služby DEFORM pre všetky počítače DEFORM** : Pomocou tejto možnosti bude môcť používateľ zobraziť všetkých klientov, ktorí sú pripojení k serveru, ku ktorému je miestny systém pripojený spolu so systémom servera. Používateľ musí mať prístupový kód alebo musí byť oprávneným používateľom, aby mohol sledovať a ovládať služby iných počítačov ako miestneho počítača. Služby možno spustiť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/run_action_icon.jpg' | relative_url }}) a zastaviť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/stop_action_icon.jpg' | relative_url }}), ktoré je k dispozícii vedľa služby, pozri obr. 3.1.20. Od verzie 14 sa informácie všetkých počítačov pripojených k licenčnému serveru nebudú štandardne synchronizovať, aby sa zlepšil výkon DEFROM Setup, synchronizovať sa budú len informácie o miestnom počítači a počítači servera. Na synchronizáciu informácií príslušného počítača použite tlačidlo ![]({{ '/assets/icons/pre_icons/mo_deformsetup_sync_button.jpg' | relative_url }}) a na synchronizáciu všetkých počítačov použite tlačidlo ![]({{ '/assets/icons/pre_icons/mo_deformsetup_sync_all_computers_button.jpg' | relative_url }}). (Pozri obr. 3.1.21.)

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image013.jpg' | relative_url }})

DEFORM Service pre všetky počítače DEFORM

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image030.jpg' | relative_url }})

DEFORM Service pre všetky počítače DEFORM po synchronizácii

**Pasový kód :** Autorizovaný používateľ DEFORM (pozri) môže vytvoriť alebo zmeniť prístupový kód (pozri obr. 3.1.22.). Pomocou prístupového kódu,

  * Používateľ môže spúšťať a zastavovať služby počítača Server. (Používateľ musí mať prístupový kód, ak chce zastaviť služby serverového počítača v PC, zatiaľ čo v Linuxe potrebujete prístupový kód na spustenie aj zastavenie služieb serverového počítača)
  * Zobrazenie služieb akéhokoľvek počítača DEFORM (iného ako autorizovaného počítača)
  * Zobrazenie služieb akéhokoľvek počítača s webovým prehliadačom (nie je potrebné inštalovať DEFORM)
  * Aktualizácia súboru hesiel pre serverový počítač
  * Aktualizácia zastaraných služieb v ktoromkoľvek počítači DEFORM

**Poznámka:** Prístupový kód musí byť zdieľaný len medzi tými používateľmi, ktorí budú ovládať služby všetkých počítačov DEFORM pri spúšťaní a zastavovaní akejkoľvek služby.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image014.jpg' | relative_url }})

Vytvorenie prístupového kódu v oknách DEFORM Services autorizovaným používateľom

**Oprávnený používateľ DEFORM:**

Ak je vaše používateľské meno a názov počítača uvedené v textovom súbore s názvom**authorized_users.txt**, potom sa používateľ DEFORM nazýva autorizovaný používateľ DEFORM.

Ako autorizovaný používateľ DEFORM máte plnú kontrolu nad službami DEFORM. Môžete:

  1. Prístup k službám DEFORM na všetkých počítačoch DEFORM.
  2. Nastavenie alebo zmena prístupového kódu služby DEFORM
  3. Aktualizujte súbor s licenčným heslom DEFORM (DEFORM.PWD)

Súbor authorized_users.txt sa nachádza v licenčnom priečinku DEFORM na počítači servera DEFORM.

Má tento formát:

  * meno_používateľa1@názov_počítača1
  * meno_používateľa2@názov_počítača2

Ak súbor**authorized_users.txt** neexistuje, môžete ho vytvoriť pomocou textového editora

Pri konfigurácii autorizovaných používateľov DEFORM postupujte podľa vyššie uvedeného formátu. Pri vytváraní autorizovaných používateľov môžete použiť nasledujúce pokyny,

  * Použite skutočné meno používateľa a názov počítača v systéme
  * Uveďte len používateľov, ktorí spravujú systém DEFORM ako oprávnení používatelia DEFORM
  * Ak nemáte oprávnenie upravovať súbor authorized_users.txt, požiadajte o pomoc správcu IT.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image015.jpg' | relative_url }})

a. Hlavné okno autorizovaného používateľa DEFORM Services.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image016.jpg' | relative_url }})

b. Hlavné okno služby DEFORM pre neautorizovaných používateľov

Zobrazenie hlavného okna služieb DEFORM pre autorizovaného používateľa a neautorizovaného používateľa

**Aktualizácia modulov simulačných služieb:**

Ak po inštalácii služieb DEFORM pozorujeme stav ![]({{ '/assets/icons/pre_icons/error_status_icon.jpg' | relative_url }}), môže to byť spôsobené tým, že súbory simulačných služieb nie sú k dispozícii alebo dostupné súbory sú zastarané, potom musíme aktualizovať súbory pomocou tlačidla aktualizácie, ktoré je k dispozícii vedľa počítača DEFORM, ktorý zobrazuje chybu. Používateľ potrebuje na aktualizáciu služieb prístupový kód. Keď klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_deform_setup_update_icon.jpg' | relative_url }}) Update (Aktualizovať), potom sa súbory Simulation Server (SS), Simulation Client (SC) a Web-based Simulation Monitoring server (RS) skopírujú do zložky Configuration (Konfigurácia) a môžeme vidieť správu

"Aktualizácia sim_modules na TESTING1 ...

SUCCESS", TESTING1 je počítač, ktorý vykazoval chybu (pozri obr. 3.1.24.).

Po úspešnej aktualizácii simulačných služieb môžeme služby spustiť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/run_action_icon.jpg' | relative_url }}). Ak je systém DEFORM iný ako lokálny, musíme zadať meno používateľa a heslo systému, inak nemusíme. Služby sa spustia pod používateľským menom, ktoré je zadané pri spúšťaní služby. V prípade, že lokálny systém je Windows, služba sa spustí automaticky pod aktuálnym aktívnym prihláseným používateľským menom, keď klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/run_action_icon.jpg' | relative_url }}) (pozri obr. 3.1.26.), zatiaľ čo lokálny systém je Linux Používateľské meno (zobrazí sa predvolené používateľské meno zo súboru deformscd) a heslo je potrebné zadať na spustenie služby.

Pred aktualizáciou súborov služieb Simulation musíme zastaviť spustené služby a potom aktualizovať súbory.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image017.jpg' | relative_url }})

a. Ak sú simulačné služby zastarané alebo nie sú k dispozícii

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image018.jpg' | relative_url }})

b. Po aktualizácii simulačných služieb

Aktualizácia súborov simulačných služieb v okne DEFORM Services

**Rôzny stav simulačného servera**

\-- | Simulačný server nie je pridaný na karte Simulačný server
---|---
STOPPED | Simulačný server je pridaný, ale nie je spustený
zastarané | Simulačný server bol pridaný skôr, ale teraz je odpojený
RUNNING | Simulačný server pridaný a spustený
  
**Aktualizácia súboru s licenčným heslom:**

Pomocou tlačidla Aktualizovať súbor s licenčným heslom môže oprávnený používateľ aktualizovať súbor s heslom, keď dostane nový súbor s licenčným heslom (pozri obr. 3.1.25.). Po aktualizácii súboru s heslom je potrebné reštartovať licenčný server.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image019.jpg' | relative_url }})

Aktualizácia súboru hesla licencie zo služby DEFORM Services

**Ovládanie služieb v serverovom počítači**

V systéme Windows potrebujeme prístupový kód na zastavenie služieb Licenčný server, Server dávkovej fronty a Webové riadenie služieb na serverovom počítači, zatiaľ čo v systéme Linux potrebujeme prístupový kód aj na spustenie týchto služieb. Ak zastavíme službu Licenčný server, zastaví sa aj služba Dávkový frontový server spolu so všetkými službami Simulačný server a Simulačný klient na všetkých systémoch DEFORM pripojených k tomuto serveru, pozri obr. 3.1.26.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image021.jpg' | relative_url }})

Výzva na zadanie prístupového kódu na zastavenie služby servera Dávkový front

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image020.jpg' | relative_url }})

Výzva na zadanie mena používateľa a hesla na spustenie ďalších používateľských služieb

**Súvisiace témy:**

[3.2. License Monitoring](/docs/sk/starting_up_deform/3_license_manager/3_2_license_monitoring/)

[3.3. Services Monitoring](/docs/sk/starting_up_deform/3_license_manager/3_3_services_monitoring/)

[3.4. Trouble Shooting License Issues](/docs/sk/starting_up_deform/3_license_manager/3_4_trouble_shooting_license_issues/)
