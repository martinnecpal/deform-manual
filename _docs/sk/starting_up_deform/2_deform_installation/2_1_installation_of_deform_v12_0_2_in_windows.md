---
lang: sk
title: "2.1. Inštalácia DEFORM V14.0.2. v systéme Windows"
---

# 2.1. Inštalácia DEFORM V14.0.2 v systéme Windows

2.1.1. ÚVOD

2.1.2. POŽIADAVKY NA INŠTALÁCIU

2.1.3. INŠTALÁCIA ZARIADENIA S BEZPEČNOSTNÝM KĽÚČOM

2.1.4. INŠTALÁCIA DEFORM v14.0.2 V SYSTÉME WINDOWS

2.1.5. AKTUALIZÁCIA SÚBORU S LICENČNÝM HESLOM DEFORMÁCIE

2.1.6. OTÁZKY / PROBLÉMY

2.1.7. MOŽNOSTI INŠTALAČNÉHO PRÍKAZOVÉHO RIADKU

2.1.8. PONUKA ŠTART SYSTÉMU WINDOWS

## ÚVOD

Nasledujúce kroky je potrebné vykonať, aby ste nainštalovali DEFORM v14.0.2 (nasledujúce servisné balíky tiež postupujú podobne, ale inštalujú sa do iného priečinka a vytvárajú nové skratky).   
Tieto kroky zahŕňajú:

  * Splnenie minimálnych systémových požiadaviek.

  * Inštalácia programových súborov DEFORM v14.0.2.

  * Správca licencií (inštalácia ovládača bezpečnostného kľúča v7.6.9).

  * Podpora kódov ( MPICH2 v1.2 64-bit a MiKTeX v21.4)

  * súbory v14.0.2

  * Riešenie problémov, ak sa vyskytnú.

Inštalácia programu DEFORM sa spustí spustením **DEFORM_System_Installer_v14.0.2.exe.**
Po spustení tohto inštalačného programu bude mať používateľ možnosť vybrať si, ktoré časti programu DEFORM sa majú nainštalovať.Viac informácií nájdete v časti 2.1.4.

**DEFORM_License_Manager_Installer_v14.0.2.exe** nainštaluje správcu licencií DEFORM a dávkovú frontu.  
**DEFORM_Core_Installer_v14.0.2.exe** nainštaluje systém DEFORM.  
**DEFORM_Service_Control_Installer_v14.0.2.exe** nainštaluje program DEFORM Service Control. Je to novinka od verzie 11.2 a umožňuje spravovať služby DEFORM prostredníctvom karty Služby DEFORM v aplikácii DEFORM Setup.

Ak vám podpora SFTC neoznámi inak, inštalácia akejkoľvek časti DEFORM by sa mala vykonať spustením nástroja **DEFORM_System_Installer_v14.0.2.exe**.

## POŽIADAVKY NA INŠTALÁCIU

  * Operačný systém: (Serverové verzie nie sú podporované.)

  * Navrhovaná pamäť RAM: 16+ GB

  * Miesto na pevnom disku potrebné na inštaláciu: ~ 12 GB.

## INŠTALÁCIA ZARIADENIA S BEZPEČNOSTNÝM KĽÚČOM

Bezpečnostný kľúč umožňuje, aby bol systém DEFORM v14.0.2 vysoko prenosný a zároveň aby bol ako licenčný server s platným heslom kedykoľvek použiteľný len jeden systém. Skutočný softvér môžete nainštalovať na ľubovoľný počet počítačov, ale každý systém DEFORM bude funkčný len s pripojeným bezpečnostným kľúčom alebo bude nakonfigurovaný ako klient pripojený k platnému licenčnému serveru DEFORM. Bezpečnostný kľúč je kľúč USB. Hardvérový bezpečnostný kľúč USB zapojte do portu USB.

  
**UPOZORNENIE** :  
Bezpečnostný kľúč sleduje dátum v počítači. Pred prvým spustením programu DEFORM v14.0.2 sa uistite, že je dátum správny. Zmena dátumu dozadu alebo dopredu môže spôsobiť nefunkčnosť systému DEFORM v14.0.2.

  
Pri odinštalovaní staršej verzie programu DEFORM v14.0.2. (alfa alebo beta verzie) musí byť hardvérový kľúč Sentinel Security počas odinštalovania odpojený a po odinštalovaní opäť pripojený.

## INŠTALÁCIA DEFORM v14.0.2 V SYSTÉME WINDOWS

Inštalačný program DEFORM v14.0.2 je k dispozícii na stiahnutie z webovej stránky DEFORM User Area (<https://support.deform.com>). Všetok podporný (povinný a voliteľný) kód je zahrnutý v podpriečinkoch.

  
**Pred inštaláciou:**

  1. ****Odinštalujte predchádzajúcu verziu Správcu licencií a ovládačov kľúča Sentinel (Ak používateľ odinštaluje staršiu verziu DEFORM v14.0.2 (alfa alebo beta), odpojte hardvérový kľúč počas odinštalovania ovládača kľúča Sentinel a po odinštalovaní ho opäť pripojte.

  2. Pred začatím inštalácie DEFORM v14.0.2 v systéme Windows je potrebné, aby bol používateľ prihlásený ako správca.

  3. Antivírusové programy by mali byť počas inštalácie dočasne vypnuté. Môžu spôsobiť značné oneskorenie a/alebo problémy s inštaláciou.

**Postup:**

****

  1. Spustite systém Windows (prihláste sa ako správca alebo s oprávneniami správcu).

  2. Obsah stiahnutého súboru zip rozbaľte na vhodné miesto s minimálne 3,5 GB voľného miesta.

  3. Otvorte okno Prieskumníka, prejdite do rozbaleného priečinka a dvakrát kliknite na súbor **DEFORM_System_Installer_v14.0.2.exe**.

  4. Vyberte jazyk nastavenia, napríklad angličtinu, japončinu, taliančinu, nemčinu atď., a kliknite na **OK**, ako je znázornené na obr. 2.1.1.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0001.jpg' | relative_url }})

DEFORM Okno výberu jazyka nastavenia

  1. Zobrazí sa uvítacie okno inštalátora Deform System v14.0.2, ako je znázornené na obr. 2.1.2. Kliknite na tlačidlo **Ďalej**.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0002.jpg' | relative_url }})

Uvítacie okno inštalátora deformovaného systému

  1. Prijmite licenciu DEFORM (pozri obr. 2.1.3.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0003.jpg' | relative_url }})

Okno licenčnej zmluvy DEFORM

  1. Ak je potrebné zmeniť predvolené umiestnenie inštalácie programu DEFORM Setup, vyhľadajte ho a kliknite na tlačidlo **Ďalej**. (Pozri obr. 2.1.4.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0004.jpg' | relative_url }})

Okno výberu miesta inštalácie DEFORM

Ak sa v rovnakej ceste nachádzajú aj iné verzie programu DEFORM, zobrazí sa vyskakovacie okno "Priečinok existuje" s otázkou, či sa má nainštalovať do rovnakého priečinka, alebo nie, preto kliknite na tlačidlo **Ano**. (Pozri obr. 2.1.5.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0005.jpg' | relative_url }})

Vyskakovacie okno Existujúci priečinok

  1. Vyberte funkcie inštalačného programu systému DEFORM, ktoré chcete nainštalovať, zo zoznamu v okne Vybrať komponenty, ako je znázornené na obr. 2.1.6. V hornej časti okna je možné pomocou ponuky vybrať medzi rôznymi typmi inštalácií, vrátane Client only (Len klient) a Server only (Len server). Touto voľbou sa aktualizujú komponenty vybrané na inštaláciu. (Pozri obr. 2.1.7.) Kliknutím na tlačidlo **Ďalej** pokračujte.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0006.jpg' | relative_url }})

DEFORM vyberte komponenty

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0007.jpg' | relative_url }})

DEFORM vyberte komponenty okna combo box

Pri počiatočnom nastavení by sa mali vybrať všetky možnosti, aby sa nainštaloval celý systém DEFORM v14.0.2 a podporný kód. Označte časti, ktoré zodpovedajú vašej licencii, a v ponuke Štart systému Windows sa vytvoria príslušní zástupcovia. Správca licencií je povinnou súčasťou inštalačného balíka a ak je už nainštalovaná predchádzajúca verzia správcu licencií, odinštalujte ju pred inštaláciou nového správcu licencií. Ak je verzia správcu licencií rovnaká, potom nie je potrebné inštalovať. Možnosť Support Code (Podporný kód) spustí inštalačné programy pre MPICH, MiKTeX a redistribuovateľné súbory Microsoft C++, ktoré však možno (de)vybrať jednotlivo.

Počnúc verziou DEFORM v11.2 umožňuje riadenie služieb DEFORM spúšťanie a zastavovanie služieb DEFORM na serveri a tiež aktualizáciu programov služieb na klientských počítačoch DEFORM. Preto je potrebné nainštalovať ho na všetky počítače, na ktorých je nainštalovaný systém DEFORM bez ohľadu na verzie.

Počnúc verziou DEFORM v12.0 je inštalačný program MiKTeX súčasťou podporného kódu.MiKTeX sa používa pri generovaní zostáv.  
Počnúc verziou DEFORM v13.0 bol odstránený 32-bitový inštalačný program MPICH.  
Počnúc verziou DEFORM v13.0 je Redistributable Microsoft C++ 2015 64-bit súčasťou podporného kódu.  
Počnúc verziou DEFORM v13.1.1 boli 32-bitové a 64-bitové redistribučné súbory Microsoft C++ 2008 aktualizované na verziu 9.0.3.30729.6161.  
Počnúc verziou DEFORM v13.1.1 je Python 3.12.2 voliteľnou inštaláciou.  
Python sa používa v (v súčasnosti beta verzii) systému DEFORM API. Rozhranie DEFORM API umožňuje používateľom prístup k funkciám DEFORM zo skriptov Python.  
Python je potrebný aj pre voliteľné webové riadenie služieb. Webové ovládanie služieb umožňuje prístup k službám DEFORM (ako je vidieť na karte "Služby DEFORM" v nástroji DEFORM Setup) z webového prehliadača.

Počnúc verziou DEFORM v14.0.1 bol inštalátor MiKTeXu aktualizovaný na verziu 24.1.

Po výbere produktov, ktoré zodpovedajú vašej licencii, kliknite na tlačidlo **Dalšie**.

_**DEFORM v14.0.2 a Správca licencií v14.0.2 Možnosti inštalácie**_

  1. Začiarknite políčko "Konfigurovať bránu firewall systému Windows", aby ste povolili prístup programom DEFORM a službám License a batch queue cez bránu firewall systému Windows, ako je znázornené na obr. 2.1.8., a potom kliknite na tlačidlo **Next**.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0008.jpg' | relative_url }})

DEFORM Okno konfigurácie brány Windows Firewall

_** Možnosti inštalácie aplikácie DEFORM License Manager v14.0.2**_

  2. Ak je vybraná súčasť License Manager v14.0.2, inštalačný program DEFORM zobrazí možnosti týkajúce sa License Manager. Ak je počítač systémom licenčného servera (kde je zapojený hardvérový kľúč), musí sa vybrať súbor s licenčným heslom DEFORM, ktorý dodáva spoločnosť SFTC. Vyhľadajte súbor s heslom a vyberte ho. V opačnom prípade súbor s heslom nevyberajte. Kliknutím na tlačidlo **Ďalej** pokračujte v práci. (Pozri obr. 2.1.9.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0009.jpg' | relative_url }})

DEFORM Prehľadávanie okna Správca licencií Heslo

  1. Začiarknite políčko "Install Batch Queue Server" (Inštalovať server dávkových front), ktoré je potrebné pre simulácie frontu, ako je znázornené na obr. 2.1.10., a potom kliknite na tlačidlo **Next** (Ďalej).

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0010.jpg' | relative_url }})

Dodatočné okno výberu úlohy DEFORM License Manager

_**DEFORM v14.0.2 Možnosti inštalácie**_

  1. Ak je vybraná zložka DEFORM v14.0.2, inštalačný program DEFORM zobrazí možnosti týkajúce sa DEFORM. Od verzie DEFORM v13.1 je k dispozícii nová možnosť výberu motora konečných prvkov. SFTC odporúča použiť možnosť Intel® Fortran, pokiaľ sa nepoužíva kompilátor Absoft Fortran alebo ak sa DEFORM neinštaluje na počítač so starším (nemoderným) procesorom. Upozorňujeme, že možnosť Intel Fortran je kompatibilná s procesormi Intel Core aj AMD Ryzen. Urobte výber motora FEM podľa obrázka 2.1.11. a kliknite na tlačidlo **Next** (Ďalej). Upozorňujeme, že od verzie DEFORM v14.0.2 už nie je k dispozícii motor Absoft Legacy FEM.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0011.jpg' | relative_url }})

Okno DEFORM Setup FEM Engine

  1. Potvrďte nastavenia DEFORM Setup a kliknutím na tlačidlo **Install** nainštalujte súbory DEFORM. V opačnom prípade kliknite na tlačidlo **Zadné**, ak chcete zmeniť akékoľvek nastavenia. (Pozri obr. 2.1.12.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0012.jpg' | relative_url }})

Okno potvrdenia nastavení DEFORM Setup

  1. Nastavenie DEFORM bude pokračovať v inštalácii všetkých vybraných komponentov a inštalácia bude trvať niekoľko minút, ako je znázornené na obr. 2.1.13.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0013.jpg' | relative_url }})

DEFORM Stavové okno inštalácie systému

Všimnite si, že sa zobrazí inštalačný program MiKTeX, ale nie je potrebná žiadna interakcia, ako je znázornené na obr. 2.1.14.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0014.jpg' | relative_url }})

Stavové okno inštalačného programu MiKTeX

  1. Za určitých podmienok, konkrétne ak je vybraný inštalačný program Sentinel Key Driver, DEFORM bude vyžadovať reštartovanie počítača pred spustením programu DEFORM Setup. Ak je zobrazené okno na obr. 2.1.15., DEFORM Setup sa spustí pri prihlásení do systému Windows pri ďalšom reštarte systému Windows. Kliknutím na tlačidlo **Next** (Ďalej)** pokračujte v nastavovaní, ako je znázornené na obr. 2.1.15.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0015.jpg' | relative_url }})

DEFORM vyžaduje reštartovanie okna

  1. Kliknutím na tlačidlo **Ukončiť** ukončite inštaláciu, ako je znázornené na obr. 2.1.16.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0016.jpg' | relative_url }})

Okno dokončenia inštalácie DEFORM System Installer

  1. Ak inštalačný program DEFORM odporúča reštartovanie počítača, vyberte prepínač "Áno, reštartujte počítač teraz" a kliknutím na tlačidlo **Ukončiť** reštartujte počítač, ako je znázornené na obr. 2.1.17.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0017.jpg' | relative_url }})

Okno opätovného spustenia inštalátora systému DEFORM

Po dokončení inštalácie sa spustí DEC_SC.EXE, ktorý sa nachádza na adrese "<Inštalačná cesta>\DEFORM\Konfigurácia\DEF_SC.EXE".  
Tento obslužný program DEFORM (DEC_SC.EXE) sa spustí ako "služba" na počítačoch so systémom Windows.  
Táto služba komunikuje s licenčným serverom a v programe DEFORM Setup môže používateľ sledovať stav simulačného servera (SS), simulačného klienta (SC) a webového servera na monitorovanie simulácie (RS) na ktoromkoľvek počítači DEFORM. Ako sa uvádza v nasledujúcej časti, na ich aktualizáciu podľa potreby možno použiť kartu Služby DEFORM.

  1. Následne sa spustí aplikácia DEFORM Setup. Tu môžete nakonfigurovať umiestnenie licenčného servera a tieto zmeny uložiť.

Ak licenčný server beží na vzdialenom počítači, vyberte prepínač "Na vzdialenom licenčnom serveri" a zadajte názov počítača vzdialeného servera alebo IP adresu. Kliknite na tlačidlo **Synchronizovať**. Ak je licenčný server spustený na vzdialenom stroji, používateľovi sa zobrazí stav spusteného licenčného servera, ako je znázornené na obr. 2.1.18. V opačnom prípade sa zobrazí vyskakovacie okno s chybovým hlásením "Can not connect to license server" (Nemožno sa pripojiť k licenčnému serveru).

Ak je licenčný server spustený na tomto lokálnom počítači, vyberte prepínač "Na lokálnom počítači" a kliknite na tlačidlo **Synchronizovať**.

Po úspešnej synchronizácii, bez ohľadu na to, či je licenčný server spustený na miestnom alebo vzdialenom počítači, kliknite na tlačidlo **Uložiť**, aby ste uložili nastavenia. (Pozri obr. 2.1.18.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0018.jpg' | relative_url }})

Okno DEFORM Setup License Server

  
Po kliknutí na tlačidlo synchronizácie, ak aktuálny počítač nebol nastavený ako simulačný server pre aktuálnu verziu a cestu, program DEFORM Setup ponúkne jeho pridanie (obr. 2.1.19.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0019.jpg' | relative_url }})

Okno DEFORM Setup Simulation Server

Ak kliknutím na tlačidlo Áno pridáte simulačný server, program DEFORM Setup automaticky neuloží zmenu licenčného servera, ale vyzve na uloženie zmien. (Pozri obr. 2.1.20.) Pred uložením nastavení skontrolujte, či je zmena správna na karte Simulation Server (Simulačný server).

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0020.jpg' | relative_url }})

DEFORM Pripomienka nastavenia na uloženie

Karta Simulačný server umožňuje spravovať počítače pripojené k licenčnému serveru. Ako je znázornené na obr. 2.1.21., v hornej časti karty sú zobrazené definované Simulačné servery. Ak miestny počítač nie je definovaný ako Simulation Server (Simulačný server), kliknite na tlačidlo "Add Simulation Server" (Pridať simulačný server), aby ste ho definovali.  
Pri pridávaní simulačného servera sa predvolene definuje miestny počítač a niektoré hodnoty sa nastavia automaticky. Tieto predvolené hodnoty zahŕňajú typ procesora, počet procesorov, maximálny počet úloh a najnovšia verzia bude nastavená na aktuálnu cestu.  
Ak je Správca licencií na tom istom počítači, na ktorom sa spúšťa program DEFORM Setup, je možné definovať toľko simulačných serverov, koľko je potrebné. Ak sa však Správca licencií nachádza na inom počítači, je možné definovať a upravovať iba miestny simulačný server.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0021.jpg' | relative_url }})

Okno DEFORM Setup Simulation Server

V stĺpci **Verzie** sa zobrazuje zoznam všetkých verzií definovaných pre daný simulačný server.  
Možnosť **Maximum** Jobs umožňuje nastaviť počet úloh vo fronte, ktoré môžu byť spustené súčasne na príslušnom simulačnom serveri.  
V dolnej časti sa zobrazujú podrobnosti o aktuálne vybranom simulačnom serveri. (Pozri obr. 2.1.22.)
Na karte **Verzie** môžete definovať umiestnenie na disku pre viacero verzií. Pre každú verziu je povolená len jedna cesta.  
Ak je typ procesora definovaný ako **Cluster** , karta Clusters (Klastre) bude povolená a bude možné definovať podrobnosti o uzloch klastra.  
Po vykonaní zmien na karte Simulačný server kliknite na tlačidlo Uložiť, čím uložíte nastavenia.  
_**Poznámka** : ___Informácie o inštalačnej ceste pre každú verziu je potrebné definovať, aby dávkový front fungoval správne._

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0022.jpg' | relative_url }})

Okno DEFORM Setup Simulation Server

Spúšťanie úloh na vzdialených počítačoch možno vykonávať pomocou karty Zdieľané priečinky. (Pozri obr. 2.1.23.)
Podrobnejšie informácie nájdete v kapitole [23.6. Running Shared folder Simulations.](/docs/sk/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0023.jpg' | relative_url }})

DEFORM Nastavenie zdieľaných priečinkov

Karta Služby DEFORM umožňuje spravovať služby DEFORM, ako je znázornené na obr. 2.1.24. K dispozícii máte
dve možnosti:

  1. Otvorte služby DEFORM pre miestny počítač DEFORM.

  2. Otvorte služby DEFORM pre všetky počítače DEFORM.

Prvá možnosť je dostupná pre všetkých používateľov DEFORM, zatiaľ čo druhá možnosť je dostupná len pre "oprávnených používateľov" alebo používateľov, ktorí poznajú "prístupový kód" vytvorený oprávnenými používateľmi.  
"Oprávnení používatelia" a "prístupový kód" sa zaviedli s cieľom zabrániť zneužitiu nových možností, ktoré poskytuje karta služieb DEFORM. Ďalšie informácie získate podľa pokynov uvedených v používateľskom rozhraní DEFORM Setup.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0024.jpg' | relative_url }})

Okno DEFORM Setup DEFORM Services

Karta Služby DEFORM umožňuje spúšťať a zastavovať služby DEFORM na počítači licenčného servera a počítačoch DEFORM, ako aj aktualizovať aplikácie služieb na počítačoch DEFORM. Ak je niektorá zo služieb zastavená, kliknutím na príslušné tlačidlo spustenia spustite službu, ako je znázornené na obr. 2.1.25.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0025.jpg' | relative_url }})

Okno DEFORM Setup DEFORM Services

Keď sú všetky služby DEFORM označené ako "spustené", kliknite na tlačidlo Zatvoriť, ako je znázornené na obr. 2.1.26.   
Služby Simulation Client a Simulation Server by mali byť spustené na počítačoch DEFORM.   
Webové monitorovanie simulácie a server GeoCAD sú voliteľné.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0026.jpg' | relative_url }})

Okno DEFORM Setup DEFORM Services

## AKTUALIZÁCIA SÚBORU S LICENČNÝM HESLOM DEFORMÁCIE

Ak chcete aktualizovať licenčný súbor DEFORM pomocou programu DEFORM Setup, prepnite na kartu Služby DEFORM. Kliknite na tlačidlo "aktualizovať súbor s licenčným heslom" vedľa názvu servera, ako je znázornené na obr. 2.1.27.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0027.jpg' | relative_url }})

Tlačidlo DEFORM Nastavenie aktualizácie súboru s licenčným heslom

Na stránke Aktualizovať súbor hesla licencie DEFORM kliknite na ikonu priečinka a prejdite na súbor hesla. Potom kliknite na tlačidlo "**Aktualizovať súbor hesla "**, ako je znázornené na obrázku 2.1.28.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0028.jpg' | relative_url }})

DEFORM Nastavenie vyberte súbor s heslom

Kliknutím zastavte licenčný server a kliknite na áno vo výstražnom hlásení, ako je znázornené na obr. 2.1.29.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0029.jpg' | relative_url }})

DEFORM Setup zastaví licenčný server

Potom spustite všetky zastavené služby servera, ako je znázornené na obrázku 2.1.30.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0030.jpg' | relative_url }})

DEFORM Nastavenie spustenia služieb servera

  
Potom spustite všetky zastavené služby klienta, ako je znázornené na obrázku 2.1.31.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0031.jpg' | relative_url }})

DEFORM Spustenie nastavenia Služby klienta

## OTÁZKY / PROBLÉMY

Ak máte akékoľvek otázky, pripomienky alebo problémy s inštaláciou DEFORM v14.0.2, kontaktujte:

**Scientific Forming Technologies Corporation**

**2545 Farmers Drive, Suite 200**

**Columbus, OH 43235 USA**

**Telefón: (614) 451-8330**

**E-mail: support@deform.com**

**alebo**

**Navštívte našu webovú stránku na adrese**

**[http://www.deform.com](http://www.deform.com)**

## MOŽNOSTI PRÍKAZOVÉHO RIADKU INŠTALÁTORA

Od verzie 12.1 umožňuje inštalačný program systému DEFORM odovzdávať parametre príkazového riadka. To je užitočné pre správcov systému na vykonávanie automatizovaných inštalácií. Pri automatizovaných inštaláciách sú všetky možnosti voliteľné okrem /CPUType; musí byť zadaný buď moderný, alebo starší typ.

**/LANG** =jazyk

Táto možnosť určuje jazyk, ktorý bude inštalačný program používať. Ak sa použije platný parameter /LANG, dialógové okno Výber jazyka sa potlačí. To ovplyvňuje dialógové okno **Vyberte jazyk inštalácie**, ako je znázornené na obr. 2.1.1.

Platné možnosti:  
angličtina, francúzština, nemčina, japončina, ruština, španielčina, taliančina, kórejčina, čínština zjednodušená, čínština tradičná

  
**/DIR** ="cesta, do ktorej sa má DEFORM nainštalovať"

Táto možnosť určuje miesto, kam sa má nainštalovať DEFORM. Ovplyvňuje cestu v okne Select Destination Location (Vybrať cieľové umiestnenie), ako je znázornené na obr. 2.1.4.

Predvolená možnosť: Predvolené umiestnenie inštalácie je C:\Program Files\SFTC.

  
/ **COMPONENTS** ="zoznam názvov komponentov oddelených čiarkou"

Táto možnosť určuje, ktoré súčasti programu DEFORM budú nainštalované. Použitie tohto parametra príkazového riadka spôsobí, že program Setup automaticky vyberie vlastný typ, čo znamená, že všetky komponenty okrem tých, ktoré sú odovzdané tomuto parametru, nebudú vybrané. To ovplyvňuje vybrané komponenty v okne **Výber komponentov**, ako je znázornené na obr. 2.1.6.

Platné možnosti:

  * LicenseManager

  * Nainštaluje správcu licencií DEFORM, ale nie ovládač kľúča Sentinel.

  * *LicenseManager

  * Inštaluje správcu licencií DEFORM a ovládač kľúča Sentinel. Všimnite si hviezdičku pred LicenseManager.

  * LicenseManager\Sentinel

  * Inštaluje ovládač kľúča Sentinel a správcu licencií DEFORM.

  * *SupportCode

  * Nainštaluje všetky podporné kódy. Všimnite si hviezdičku pred SupportCode.

  * SupportCode\MPICH64

  * Nainštaluje 64-bitový MPICH.

  * SupportCode\MiKTeX

  * Nainštaluje MiKTeX.

  * SupportCode\vc32

  * Nainštaluje 32-bitový redistributable Microsoft C++ 2008.

  * SupportCode\vc64

  * Nainštaluje 64-bitový redistributable Microsoft C++ 2008.

  * SupportCode\vc2015x64

  * Inštaluje 64-bitový redistributable Microsoft C++ 2015

  * VoliteľnýKódP\Python

  * Inštaluje Python. (Vyžaduje sa len pre DEFORM API a webové riadenie služieb)

  * DEFORMComponent

  * Inštaluje systém DEFORM.

  * ServiceControl

  * Nainštaluje ovládací prvok služby DEFORM.

Predvolená možnosť: Predvolená možnosť je nainštalovať všetky komponenty okrem voliteľných komponentov.

/**PasswordFile** ="cesta k súboru DEFORM.PWD"

Táto možnosť určuje umiestnenie súboru s heslom DEFORM. Ak sa správca licencií neinštaluje, táto možnosť sa ignoruje. Ovplyvňuje to cestu v okne **DEFORM Password** (Heslo DEFORM**), ako je znázornené na obr. 2.1.9.

Predvolená možnosť: nie je zadaný žiadny súbor s heslom.

/**BatchQueue** =možnosť dávkovej fronty

Táto možnosť určuje, či sa má nainštalovať server dávkových front alebo nie. Ovplyvňuje to možnosť Inštalovať **Batch Queue Server** v okne **DEFORM License Manager**, ako je znázornené na obr. 2.1.10.

Platné možnosti:

áno, nie

Predvolená možnosť: áno

  
/ **Firewall** = možnosť firewall

Táto možnosť určuje, či sa má programom DEFORM povoliť prístup cez bránu firewall systému Windows.

To ovplyvňuje možnosť **Konfigurovať bránu firewall systému Windows** v okne Brána firewall systému Windows, ako je znázornené na obr. 2.1.8.

Platné možnosti:

áno, nie

Predvolená možnosť: áno

/**FEMType** =FEM Fortran type option

Nová možnosť od verzie DEFORM v13.1. Nahrádza možnosť CPUType

Táto možnosť určuje, či sa má nainštalovať motor Intel Fortran alebo Absoft Fortran FEM. To ovplyvňuje možnosti **Intel Fortran (Default)** a **Absoft Fortran** v okne **FEM Engine**, ako je znázornené na obr. 2.1.11.
Platné možnosti:  
intel, absoft

Predvolená možnosť: intel

  
/ **TICHÝ**

Prikazuje inštalačnému programu, aby sa spustil v tichom režime. Keď je inštalácia v tichom režime, okno sprievodcu sa nezobrazí, ale zobrazí sa okno priebehu inštalácie.

Pre tento parameter neexistujú žiadne možnosti.

**/DEFORMSetup** =Možnosť nastavenia DEFORM

Nová možnosť od verzie DEFORM v13.0.1.

Táto možnosť prikazuje inštalačnému programu spustiť program DEFORM Setup na konfiguráciu licenčného servera.

Platné možnosti:

áno, nie

Predvolená možnosť: áno

  
**/ConfigurationFile** ="cesta k súboru DEFORM_NLM_CONF"

Nová možnosť od verzie DEFORM v13.0.1.

Táto možnosť určuje umiestnenie konfiguračného súboru licenčného servera, ktorý sa má použiť. Tento súbor je vytvorený programom DEFORM Setup a nachádza sa v priečinku Configuration (Konfigurácia), preto najskôr spustite program DEFORM Setup aspoň na jednom počítači a použite ho pri ďalších inštaláciách.

Je to užitočné pri používaní rovnakého konfiguračného súboru na viacerých počítačoch a funguje to aj pri nastavení možnosti DEFORMSetup na nie.  
Ak v priečinku Configuration existuje existujúci súbor DEFORM_NLM_CONF, prepíše sa.

Ak inštalujete Správcu licencií (samostatne alebo ako súčasť licencie uzamknutej uzlom), ako zdrojový súbor môžete použiť DEFORM_NLM_CONF alebo DEFORM_NLM_CONF_SERVER. V tomto prípade sa súbor skopíruje aj do priečinka Configuration (ako DEFORM_NLM_CONF) aj do priečinka License Manager (ako DEFORM_NLM_CONF_LMSERVER).

Táto možnosť je nadradená možnosti LicenseServerName.

Predvolená možnosť: nie je zadaný žiadny konfiguračný súbor licenčného servera.

**/****LicenseServerName** ="Názov licenčného servera"

Nová možnosť od verzie DEFORM v13.0.1.

Táto možnosť určuje názov servera, ako je znázornené na obr. 2.1.18.

Je to užitočné pri používaní rovnakého konfiguračného súboru na viacerých počítačoch a funguje to aj pri nastavení možnosti DEFORMSetup na nie.

Ak v priečinku Configuration existuje existujúci súbor DEFORM_NLM_CONF, prepíše sa.

Toto sa ignoruje, ak je nastavená možnosť ConfigurationFile.

Predvolená možnosť: nie je zadaný názov servera

**Príklady**

Inštalácia uzla uzamknutá
DEFORM_System_Installer_v14.0.2.exe /LANG=english /SILENT

Inštalácia Inštalácia klienta
DEFORM_System_Installer_v14.0.2.exe /LANG=angličtina /COMPONENTS="*SupportCode,DEFORMComponent,ServiceControl" /SILENT

Inštalácia servera Inštalácia so súborom hesla

DEFORM_System_Installer_v14.0.2.exe /LANG=angličtina /COMPONENTS="*LicenseManager, SupportCode\vc32,ServiceControl" /PasswordFile="C:\DEFORM.PWD" /SILENT

****

**Odstránené možnosti**

**zápis v /FEMType**
Táto možnosť bola zrušená od verzie DEFORM v14.0.2. Starší motor Absoft FEM bol vyradený.

**Poznámky k vydaniu v /COMPONENTS**
Táto možnosť bola zrušená od verzie DEFORM v14.0.

**/NodeLocked**
Táto možnosť bola zrušená od verzie DEFORM v14.0.

**/CAD**
Táto možnosť bola zrušená od verzie DEFORM v14.0. Možnosť GeoCAD Server bola presunutá do nastavenia DEFORM.

**/CPUType**
Táto možnosť bola zrušená od verzie DEFORM v13.1. Nahradila ju možnosť FEMType.

## PONUKA ŠTART SYSTÉMU WINDOWS

Počnúc verziou DEFORM v14.0.2 umožňuje DEFORM Setup vybrať, ktoré skratky DEFORM sa zobrazia v ponuke Štart systému Windows, ako je znázornené na obr. 2.1.32. Inštalačný program zahrnie výber aplikácií do ponuky Štart. Ak ich chcete zmeniť, aplikácie môžete vybrať v stĺpci Nová **ponuka Štart****menu**. Kliknutím na tlačidlo **Aktualizovať ponuku Štart** sa ponuka Štart aktualizuje o vybrané aplikácie. Tlačidlá **Vybrať všetko** a **Zrušiť výber****all** slúžia na výber, resp. zrušenie výberu všetkých voliteľných aplikácií. Tlačidlo **Obnoviť** aktualizuje stĺpec Aktuálna ponuka Štart, v ktorom sa zobrazujú aplikácie, ktoré sú aktuálne v ponuke Štart.

_Poznamenajte, že karta ponuky Štart sa nezobrazí, ak je program DEFORM Setup spustený z položky ponuky Štart**DEFORM Setup for License Manager**._

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0032.jpg' | relative_url }})

DEFORM Setup Karta ponuky Štart

**Súvisiace témy:**

[3\. License Manager](/docs/sk/starting_up_deform/3_license_manager/3_introduction_to_license_manager/)

[3.4. Trouble Shooting License Issues](/docs/sk/starting_up_deform/3_license_manager/3_4_trouble_shooting_license_issues/)

[23.6. Running simulations remotely](../../../assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations)

[23.8. Trouble Shooting Simulation Running](../../../assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running)
