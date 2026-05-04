---
lang: sk
title: "2.2. Inštalácia DEFORM V14.0.2. v systéme Unix alebo Linux"
---

# 2.2. Inštalácia DEFORM V14.0.2 v systéme Unix alebo Linux

****

2.2.1. Úvod

2.2.2. Požiadavky na inštaláciu

2.2.3. Zariadenie bezpečnostného kľúča

2.2.4. Získanie softvéru DEFORM

2.2.5. Poznámky k inštalácii

2.2.6. Inštalácia LZMA / XZ Utilities

2.2.7. Inštalácia Pythonu

2.2.8. Inštalácia ovládača kľúča Sentinel

2.2.9. Inštalácia správcu licencií

2.2.10. Inštalácia DEFORM

2.2.11. Dodatočná inštalácia

2.2.12. Nastavenie používateľského účtu

2.2.13. Nastavenie DEFORM

2.2.14. Vykonávanie systému

2.2.15. Otázky / problémy

2.2.16. Typy CPU

## ÚVOD

Na inštaláciu programu DEFORM v14.0.2 je potrebné vykonať nasledujúce kroky. (Aj nasledujúce servisné balíky postupujú podobne, ale inštalujú sa do iného priečinka). Tieto kroky zahŕňajú:

  * Splnenie minimálnych systémových požiadaviek.

  * Inštalácia programových súborov DEFORM v14.0.2.

  * Správca licencií (inštalácia ovládača bezpečnostného kľúča v7.6.3).

  * súbory v14.0.2

  * Podpora kódov (lzma/xz utils, tar, MPICH2 v1.3.1 64-bit, Python, openSCAD a TeX Live)

  * Riešenie problémov, ak sa vyskytnú.

## POŽIADAVKY NA INŠTALÁCIU

  * Operačný systém:

  * CentOS (Red Hat Enterprise Linux) 6.10+ Linux (x86_64)

  * CentOS (Red Hat Enterprise Linux) 7.7+ Linux (x86_64)

  * Red Hat Enterprise Linux (RHEL) 8.8+ (x86_64)

    * Podpora Red Hat 8 je v súčasnosti v beta verzii

  * Navrhovaná pamäť RAM: 16+ GB

  * Miesto na pevnom disku potrebné na inštaláciu: ~8 GB

  * Podporný softvér:

  * Nástroje LZMA/XZ

  * GNU Tar

## Zariadenie bezpečnostného kľúča

Bezpečnostný kľúč umožňuje, aby bol systém DEFORM v14.0.2 vysoko prenosný a zároveň aby bol ako licenčný server s platným heslom kedykoľvek použiteľný len jeden systém. Skutočný softvér môžete nainštalovať na ľubovoľný počet počítačov, ale každý systém DEFORM bude funkčný len s pripojeným bezpečnostným kľúčom alebo bude nakonfigurovaný ako klient pripojený k platnému licenčnému serveru DEFORM. Bezpečnostný kľúč je kľúč USB. Hardvérový bezpečnostný kľúč USB zapojte do portu USB.

**UPOZORNENIE** :

Bezpečnostný kľúč sleduje dátum v počítači. Pred prvým spustením programu DEFORM v14.0.2 sa uistite, že je dátum správny. Zmena dátumu dozadu alebo dopredu môže spôsobiť nefunkčnosť systému DEFORM v14.0.2.

## Získanie softvéru DEFORM

Balík DEFORM v14.0.2 je k dispozícii na stiahnutie na webovej stránke DEFORM User Area na adrese <https://support.deform.com>.

Súbor s heslom DEFORM (DEFORM.PWD) je k dispozícii na stiahnutie na webovej stránke používateľskej oblasti DEFORM na adrese <https://support.deform.com>. alebo kontaktujte pani Engelbrechtovú na telefónnom čísle [mengelbrecht@deform.com](http://mengelbrecht@deform.com).

Ovládač hardvérového kľúča Sentinel je k dispozícii na prevzatie na adrese <https://www.deform.com/redirects/sentinel.html>. Inštalačný program ovládača v7.6.2 je k dispozícii na stiahnutie aj z webovej lokality DEFORM User Area na adrese <https://support.deform.com>.

## Poznámky k inštalácii

  1. Aby ste mohli nainštalovať DEFORM v14.0.2, musíte mať v systéme, do ktorého chcete softvér nainštalovať, prístup root. Pokyny vyžadujúce prístup root sú označené začiatkom [root].

  2. Systém používateľa musí mať podporný softvér potrebný na inštaláciu softvéru DEFORM.

  3. Ak nie je uvedené inak, uvedené príklady predpokladajú inštaláciu v systéme CentOS Linux.

## Inštalácia LZMA / XZ Utilities

DEFORM je v systéme Linux distribuovaný ako súbor GNU tar komprimovaný pomocou LZMA. Inštalačné súbory sa musia rozkomprimovať pomocou dekompresného nástroja LZMA; výsledný súbor sa potom musí rozbaliť pomocou GNU tar. Na vykonanie inštalácie je potrebné priame prihlásenie ako root.

  
Skontrolujte, či je LZMA/XZ vo vašom systéme už nainštalovaný, a to zadaním nasledujúceho príkazu:  
V systémoch CentOS 7 a Red Hat (RHEL)8:

xz --version

V systéme CentOS 6:

lzma --version

Ak je nainštalovaný systém XZ, odpoveď bude podobná:

xz (XZ Utils) 5.5.2

liblzma 5.2.2

Ak je nainštalovaný LZMA, odpoveď bude podobná:

Nástroj príkazového riadka LZMA 4.32.7

LZMA SDK 4.43

Ak sa vám pri vyššie uvedenom príkaze zobrazí chyba, ale viete, že LZMA/XZ je vo vašom systéme nainštalovaný, upravte systémovú cestu tak, aby obsahovala cestu k binárnym súborom LZMA/XZ. Ak je LZMA/XZ nainštalovaný, spustenie príkazu 'which lzma' alebo 'which xz' vráti cestu.

Ak v systéme nie sú nainštalované nástroje LZMA/XZ, najjednoduchší spôsob inštalácie LZMA/XZ je prostredníctvom správcu balíkov systému.

CentOS 7 a Red Hat (RHEL)8:

yum install xz

CentOS 6:

yum install lzma

LZMA je k dispozícii aj v používateľskej oblasti DEFORM na manuálnu inštaláciu. Stiahnite si príslušné rpms pre váš systém do adresára, do ktorého je možné zapisovať. Vyžadujú sa rpm lzma-4* aj lzma-libs-4*. Najjednoduchšou metódou je získanie súborov z oblasti pre používateľov. Predkompilované súbory rpm pre systém CentOS (Red Hat Enterprise Linux Compatible) Linux sú k dispozícii na adrese <https://tukaani.org/lzma>.

Keď sú rpm v adresári, do ktorého je možné zapisovať, je potrebné najprv nainštalovať rpm lzma-libs-4*. Niektoré varianty systému Linux (novšie verzie systému Centos Linux) umožňujú inštaláciu súborov dvojitým kliknutím na ne v prehliadači súborov. Ak je táto metóda k dispozícii, vyžiada sa heslo roota a potom sa súbor nainštaluje. Uistite sa, že ste nainštalovali oba súbory lzma.

Súbory môžete nainštalovať aj pomocou nasledujúceho príkazu (vydaného ako root) z adresára, ktorý obsahuje tieto súbory:

rpm -Uvh lzma-4.32.7-1.el4.rf.x86_64.rpm lzma-libs-4.32.7-1.el4.rf.x86_64.rpm

## Inštalácia Pythonu

  1. Počnúc verziou DEFORM v13.1 je potrebné nainštalovať Python len v prípade, že používate webové ovládanie služieb alebo e-mailové oznámenia.

  2. [root] V niektorých verziách Linuxu môže byť dodaná verzia Pythonu príliš stará na to, aby sa dal nástroj DEFORM Services spustiť. Ak novšia verzia nie je dostupná prostredníctvom repozitára *yum, zipper), postupujte podľa týchto pokynov na aktualizáciu na Python 2.7.

wget http://www.python.org/ftp/python/2.7.2/Python-2.7.2.tgz

tar -xzvf Python-2.7.2.tgz

cd Python-2.7.2

./configure

vykonať inštaláciu

Ak sa vyskytnú problémy s inštaláciou Pythonu, možno bude potrebné najprv nainštalovať gcc. V systéme CentOS zadajte _yum install gcc_ .

## Inštalácia ovládača kľúča Sentinel

  1. Ovládač 7.6.2 vo formáte zip (sentinel_protection_installer_7.6.2_linux.zip) je k dispozícii v
nainštalovaného správcu licencií v adresári /usr/local/SFTC/LicenseManager/UTILS/. Podrobnosti o inštalácii správcu licencií nájdete v časti 2.2.9.

  2. Skopírujte komprimovaný archívny súbor ovládača kľúča Sentinel do adresára, do ktorého je možné zapisovať, v systéme, v ktorom ho chcete nainštalovať.

  3. [root] Spustite nasledujúce príkazy na inštaláciu ovládača.

cd /path_to_zip

Rozbaliť sentinel_protection_installer_7.6.2_linux.zip

cd sentinel_protection_installer_7.6.2

chmod +x protection_install.sh

./protection_install.sh

  1. Vložte kľúč USB do počítača. V prípade použitia klastra vložte kľúč do hlavného uzla.

  2. [root] Spustite démona ovládača.

cd /opt/safenet_sentinel/common_files/sentinel_usb_daemon

./load_daemon.sh start

./load_daemon.sh podpora

  1. [root] Druhé opakovanie príkazu ./load_daemon.sh start by malo znamenať, že démon už beží. Každé ďalšie reštartovanie systému spustí túto službu, čím umožní správcovi licencií DEFORM komunikovať s hardvérovým kľúčom a súborom hesiel.

  2. Používanie niektorých verzií tohto ovládača (napríklad v7.4 a vyšších) vyžaduje, aby používateľ manuálne zachoval kompatibilitu s predchádzajúcimi verziami pre reštart/reštart počítača. ('./load_daemon.sh support' sa musí vykonať ručne pri každom reštarte systému).

  3. DEFORM vyžaduje ovládač v7.1 alebo novší. S ovládačom v7.1 je predvolené umiestnenie spúšťacieho skriptu démona /opt/sentinel/sud/usb.

## Inštalácia správcu licencií

Správca licencií DEFORM môže byť spustený na tom istom počítači so systémom Linux, na ktorom je nainštalovaný DEFORM, alebo na akomkoľvek inom podporovanom počítači so systémom Linux alebo počítači v sieti.

  1. Ak je nainštalovaná staršia verzia programu DEFORM alebo licenčného servera, spustite nasledujúci príkaz na zastavenie existujúcich služieb DEFORM.

_/etc/init.d/deformscd cleanstop_

  1. Skopírujte komprimovaný archívny súbor Správcu licencií do adresára, do ktorého je možné zapisovať, v systéme, v ktorom ho chcete nainštalovať.

  2. Dekomprimujte súbor tar.lzma.

  1. V systéme CentOS 6 použite unlzma.

unlzma DEFORM_LicenseManager_v14_0_2_CentOS_v6.x_x86_64.tar.lzma

  1. V systéme CentOS 7 použite unxz.

unxz DEFORM_LicenseManager_v14_0_2_CentOS_v7.x_x86_64.tar.lzma

  1. [root] Vytvorte inštalačný adresár pre DEFORM.

mkdir /usr/local/SFTC

  1. [root] Prejdite do inštalačného adresára.

cd /usr/local/SFTC

  1. [root] Rozbalte rozbalený inštalačný súbor.

tar -xvf /path_to_file/DEFORM_LicenseManager_v14_0_2_CentOS_v6.x_x86_64.tar

  1. [root] Požadované systémové knižnice. V závislosti od spôsobu inštalácie operačného systému môžu niektorým 64-bitovým systémom chýbať niektoré požadované 32-bitové systémové knižnice, ktoré DEFORM vyžaduje. Spustite nižšie uvedené príkazy na inštaláciu najpravdepodobnejších chýbajúcich knižníc. To si vyžaduje prístup k platnému softvérovému úložisku.  
_cd /usr/local/SFTC/LicenseManager/UTILS
./DEF_INSTALL_LIBS.sh _

  2. [root] Spustite nasledujúci skript na nastavenie služieb DEFORM. Tým sa nastavia služby deformlmd, deformbqd a deformcd, ktoré sú potrebné na spustenie služieb pre správcu licencií, servera dávkovej fronty a riadenia služieb.

cd /usr/local/SFTC/LicenseManager/UTILS

./DEF_INSTALL_SERVERS.sh

  1. [root] Ak je Správca licencií nainštalovaný v predvolenom umiestnení (/usr/local/SFTC), tento krok môžete preskočiť.

Skripty deform* v /etc/init.d musia obsahovať správne cesty. Upravte každý súbor deform* a aktualizujte v ňom obsiahnuté cesty tak, aby ukazovali na použité umiestnenie inštalácie.

  1. Kontrola služieb sa nedá spustiť ako root. Skript v /etc/init.d/deformscd predpokladá, že existuje používateľ s menom "deform", ktorý nie je root. Ak neexistuje používateľ bez roota s menom "deform", upravte nasledujúci riadok tak, aby odkazoval na existujúceho používateľa bez roota.

export DEFORM_SIM_USER=deform

Pred spustením programu DEFORM Setup je potrebné spustiť program Services Control. Nespúšťajte službu pomocou príkazu "service deformscd start"; spôsobí to problémy s generovaním zostáv. Namiesto toho ju spustite podľa nasledujúceho postupu.

  
_/etc/init.d/deformscd start_

  1. [root] Ak DEFORM.PWD ešte nebol stiahnutý, pozrite si časť 2.2.4. Získanie softvéru DEFORM teraz. Skopírujte súbor DEFORM.PWD do adresára, v ktorom bol nainštalovaný program DEFORM License Manager. Predvolené umiestnenie inštalácie je /usr/local/SFTC/LicenseManager. Uistite sa, že tento súbor má povolené práva na čítanie pre všetkých používateľov (môžete použiť príkaz chmod).

cd /usr/local/SFTC/LicenseManager

cp /path_to_file/DEFORM.PWD

chmod +r DEFORM.PWD

  
POZNÁMKA: Pri reštarte systému by sa mali automaticky spustiť služby správcu licencií, dávkového frontu a riadenia služieb a každý prihlásený používateľ by mal mať možnosť tieto služby používať.

POZNÁMKA: Spustenie Správcu licencií vyžaduje, aby bol nainštalovaný ovládač kľúča Sentinel. Po nainštalovaní ovládača (podľa vyššie uvedených krokov) sa Správca licencií spustí automaticky po reštarte vo väčšine systémov Linux.

POZNÁMKA: Ak chce používateľ reštartovať správcu licencií DEFORM bez reštartovania počítača (napr. ak je potrebné nainštalovať nový súbor DEFORM.PWD), môže sa prihlásiť ako root a spustiť nasledujúce príkazy.

  
/etc/init.d/deformlmd reštart

/etc/init.d/deformbqd reštart

  1. [root] Spustite služby DEFORM.

 _/etc/init.d/deformbqd start
/etc/init.d/deformlmd start
/etc/init.d/deformscd start_

  1. Ak sa má DEFORM nainštalovať na ten istý počítač, prejdite na nasledujúcu časť 2.2.10. Inštalácia programu DEFORM. V opačnom prípade prejdite na časť 2.2.11. Dodatočná inštalácia.

## DEFORM Inštalácia

  1. Ak je nainštalovaná staršia verzia programu DEFORM alebo licenčného servera, spustite nasledujúci príkaz na zastavenie existujúcich služieb DEFORM.  
_/etc/init.d/deformscd cleanstop_

  2. Skopírujte komprimovaný archívny súbor Správcu licencií do adresára, do ktorého je možné zapisovať, v systéme, v ktorom ho chcete nainštalovať.

  3. Dekomprimujte súbor tar.lzma.

  1. V systéme CentOS 6 použite unlzma.

unlzma DEFORM _v14_0_2_CentOS_v6.x_x86_64.tar.lzma

  1. V systéme CentOS 7 použite unxz.

unxz DEFORM_ v14_0_2_CentOS_v7.x_x86_64.tar.lzma

  1. [root] Vytvorte inštalačný adresár pre DEFORM.

mkdir /usr/local/SFTC

  1. [root] Prejdite do inštalačného adresára.

cd /usr/local/SFTC

  1. [root] Rozbalte rozbalený inštalačný súbor

tar -xvf /path_to_file/DEFORM _v14_0_2_CentOS_v6.x_x86_64.tar

  1. [root] **Potrebné systémové knižnice**. V závislosti od spôsobu inštalácie operačného systému môžu niektorým 64-bitovým systémom chýbať niektoré požadované 32-bitové systémové knižnice, ktoré DEFORM vyžaduje. Spustite nižšie uvedené príkazy na inštaláciu najpravdepodobnejších chýbajúcich knižníc. To si vyžaduje prístup k platnému softvérovému úložisku.

cd /usr/local/SFTC/DEFORM/v14.0.2/UTILS
./DEF_INSTALL_LIBS.sh

  1. [root] Spustite nasledujúci skript na nastavenie služieb DEFORM. Tým sa nastavia služby deformlmd, deformbqd a deformcd, ktoré sú potrebné na spustenie služieb pre správcu licencií, servera dávkovej fronty a riadenia služieb.

_cd /usr/local/SFTC/DEFORM/v14.0.2/UTILS
./DEF_INSTALL_SERVERS.sh _

__

  2. [root] Ak je Správca licencií nainštalovaný v predvolenom umiestnení (/usr/local/SFTC), tento krok môžete preskočiť.

Skripty deform* v /etc/init.d musia obsahovať správne cesty. Upravte každý súbor deform* a aktualizujte v ňom obsiahnuté cesty tak, aby ukazovali na použité umiestnenie inštalácie.

  1. [root] Kontrola služieb sa nedá spustiť ako root. Skript v /etc/init.d/deformscd predpokladá, že existuje používateľ s menom "deform", ktorý nie je root. Ak neexistuje používateľ bez roota s menom "deform", upravte nasledujúci riadok tak, aby odkazoval na existujúceho používateľa bez roota.

export DEFORM_SIM_USER=deform

Pred spustením programu DEFORM Setup je potrebné spustiť program Services Control. Nespúšťajte službu pomocou príkazu "service deformscd start"; spôsobí to problémy s generovaním zostáv. Namiesto toho ju spustite podľa nasledujúceho postupu.

/etc/init.d/deformscd start

  1. [root] **Knižnice na generovanie správ**. Od verzie DEFORM v12.0.1 vyžaduje generovanie zostáv knižnicu Latex PDF. Spustite nižšie uvedené príkazy na inštaláciu knižníc Latex.

cd /usr/local/SFTC/DEFORM/v14.0.2/UTILS

./DEF_INSTALL_LATEX.sh

  1. **3D obrábanie**. Počnúc verziou DEFORM v11.1 je modul 3D obrábania rozšírený o vytváranie geometrie vrtákov, čo si vyžaduje nasledujúce dodatočné kroky.

  1. Skopírujte súbor openscad-2014.03.x86-32.tar.gz zo stránky

/usr/local/SFTC/DEFORM/v14.0.2/UTILS do priečinka, do ktorého je možné zapisovať

  1. rozbaľte to pomocou príkazu tar "_tar -xzvf openscad-2014.03.x86-32.tar.gz_ "

  2. Prejdite do výsledného priečinka "_cd openscad-2014.03_ "

  3. [root] Nainštalujte balík "_./install.sh_ ".

  1. [root] **64-bitová inštalácia FEM Engine**. Počnúc verziou DEFORM v10.2 bola podpora 64-bitového 3D FEM enginu rozšírená na Linux. V týchto 64-bitových operačných systémoch zahŕňa podpora 64-bitového 3D FEM aj podporu používateľských rutín. V GUI Main (Hlavné grafické rozhranie) v dialógovom okne Run Options (Možnosti spustenia) si teraz používateľ môže vybrať, či chce model spustiť v 32-bitovom alebo 64-bitovom režime. Súvisiace pokyny týkajúce sa kompilácie používateľských rutín v 64-bitovom režime sú k dispozícii v systémovej dokumentácii (pozrite si kapitolu Systémová dokumentácia [56.3. 3D User Defined FEM Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_3_3d_user_defined_fem_routines/)). Počnúc verziou DEFORM v10.2.1 pre 64-bitovú podporu MPI bola knižnica mpich1 aktualizovaná na mpich2 pre 64-bitovú podporu MPI (žiadna zmena pre 32-bitovú podporu MPI, ktorá stále používa mpich1). Od verzie DEFORM v11.1 bola aktualizovaná knižnica mpich2.

Spustite nasledujúce príkazy na inštaláciu mpich2 pre 64-bitový DEFORM.

_cd /usr/local_

_tar -xvf /usr/local/SFTC/DEFORM/v14.0.2/UTILS/mpich2-1.3.1.tar_

Do súboru používateľa .cshrc pridajte tieto 2 premenné prostredia.

_setenv DEFORM_MPI MPICH2_

_setenv MPI_ROOT /usr/local/mpich2-1.3.1_

POZNÁMKA: Definícia MPI_ROOT je potrebná len vtedy, ak inštalácia mpich2 nie je vykonaná v ceste /usr/local.

POZNÁMKA: Počnúc verziou DEFORM v11.1 bola podpora 64-bitov rozšírená aj na 2D FEM, ale nemá podporu MPI.

  1. [root] **64-bitové nastavenie FEM Engine**. Od verzie DEFORM v13.1.1 je k dispozícii nová možnosť výberu FEM Engine. Pre systém Centos 7 bol pridaný kompilátor Intel® Fortran, ktorý je predvolene nainštalovaný. SFTC odporúča používať túto možnosť, pokiaľ sa nepoužíva kompilátor Absoft Fortran alebo ak sa DEFORM neinštaluje na počítači so starším (nemoderným) procesorom. V prípade systému Centos 6 nie je možnosť Intel Fortran k dispozícii, preto je predvolene nainštalovaný moderný kompilátor Absoft. SFTC odporúča použiť modernú možnosť kompilátora Absoft Fortran, pokiaľ nie je DEFORM nainštalovaný na počítači, ktorý používa starší (nemoderný) procesor. Upozorňujeme, že možnosť Intel Fortran je kompatibilná s procesormi Intel Core aj AMD Ryzen. Upozorňujeme, že od verzie DEFORM v14.0.2 už nie je k dispozícii engine Absoft Legact.

a. Ak chcete zmeniť motor FEM, spustite nižšie uvedené príkazy a postupujte podľa pokynov.

cd /usr/local/SFTC/DEFORM/v14.0.2/UTILS

./DEF_SETUP_FEM.sh

## Dodatočná inštalácia

  1. **Povolenia**. V prípade simulácií, ktoré spúšťa iný používateľ ako definovaný používateľ simulačného servera, musia byť splnené nasledujúce minimálne požiadavky na oprávnenia.

  1. Používateľ DEFORM a používatelia simulačného servera musia byť vo vzájomných primárnych skupinách.

  2. Používateľ DEFORM a používateľ simulačného servera musia mať umask, ktorý umožňuje úplné oprávnenia pre používateľa a skupinu, t. j. umask 007

  3. Domovský adresár používateľa DEFORM musí byť čitateľný skupinou.

  4. Spustite _/usr/local/SFTC/DEFORM/v14.0.2/UTILS/DEF_CHECK_CONFIG.sh_ z problémového adresára, aby ste skontrolovali tieto a akékoľvek iné súvisiace problémy s oprávneniami. Pred kontaktovaním podpory SFTC požiadajte správcu systému, aby skontroloval výstup tejto kontroly. Upozorňujeme, že niektoré chyby sa môžu objaviť v závislosti od toho, kedy sa tento krok spustí (napríklad ak ešte nebolo nastavené používateľské konto).

  1. Nastavte prostredie root tak, aby obsahovalo DEF_CFG_DIR pridaním nasledujúceho príkazu do konfiguračného súboru shell (_~/.cshrc_):

_setenv DEF_CFG_DIR '/usr/local/SFTC/DEFORM/Configuration'_

  
POZNÁMKA: Toto bude potrebné definovať aj v prostredí používateľa, ako je vysvetlené v časti. 2.2.12. Nastavenie používateľského konta.

  1. **Funkcia príspevku definovaného užívateľom** **v 64-bitovom režime**. Ak chcete používať funkciu príspevku definovaného používateľom v 64-bitovom režime.

  1. V systéme musí byť nainštalovaný kompilátor Absoft v11.0 (64-bitový).

  2. Konfiguračný súbor používateľského shellu (~/.cshrc) musí obsahovať nasledujúci riadok.

setenv LD_LIBRARY_PATH /opt/absoft11.0/shlib64

  
Ak vyššie uvedené nastavenia neboli vykonané, pri načítaní 64-bitového súboru .SL na aktiváciu funkcie používateľom definovaného príspevku sa môže vyskytnúť nasledujúca chyba.  
"libaf77math.so: nemožno otvoriť súbor zdieľaného objektu : No such file or directory."

  1. [root] Kontrola služieb sa nedá spustiť ako root. Skript v /etc/init.d/deformscd predpokladá, že existuje používateľ s menom "deform", ktorý nie je root. Ak neexistuje používateľ bez roota s menom "deform", upravte nasledujúci riadok tak, aby odkazoval na existujúceho používateľa bez roota.

export DEFORM_SIM_USER=deform

Pred spustením programu DEFORM Setup je potrebné spustiť program Services Control. Nespúšťajte
službu pomocou príkazu "service deformscd start"; spôsobí to problémy s generovaním hlásení. Namiesto toho ju spustite, ako je uvedené nižšie.

/etc/init.d/deformscd start

## Nastavenie používateľského konta

Niektoré distribúcie Linuxu nemajú csh, ale namiesto toho majú tcsh, ako napríklad RHEL 8. V takom prípade je použitie tcsh v poriadku; stačí nahradiť .cshrc nižšie uvedeným .tcshrc.

Uistite sa, že predvolený prihlasovací shell je shell "C" (csh). Používatelia môžu určiť svoj predvolený prihlasovací shell pomocou

  
cat /etc/passwd | grep 'meno používateľa'

  
a pozorovanie posledného segmentu odozvy systému. Ak csh nie je predvolený prihlasovací shell, môžete to zmeniť pomocou príkazu chsh. Ak chcete zistiť formát tohto príkazu, zadajte príkaz 'man chsh'. Budeme predpokladať, že meno používateľa DEFORM je "user1" a prihlasovací adresár je "/home/user1".

  
Prihláste sa do používateľského konta a upravte súbor príkazov na prihlásenie do shellu "C", ".cshrc", tak, aby obsahoval nasledujúce príkazové riadky (podľa typického umiestnenia inštalácie):

  
setenv DEF_CFG_DIR '/usr/local/SFTC/DEFORM/Configuration'

setenv DEFORM23_DIR '/usr/local/SFTC/DEFORM/v14.0.2'

setenv DEFORM_DIR $DEFORM23_DIR/2d

setenv DEFORM3_DIR $DEFORM23_DIR/3d

setenv DEFORM_MPI MPICH2

setenv MPI_ROOT /usr/local/mpich2-1.3.1

zdroj $DEFORM23_DIR/CONFIG.COM

maska 007

  
Prvé štyri riadky príkazu definujú globálne symboly "DEF_CFG_DIR", "DEFORM23_DIR", "DEFORM_DIR" a "DEFORM3_DIR" ako umiestnenie konfigurácie produktu DEFORM a licencie. Na piatom a šiestom riadku sa nastavuje 64-bitový DEFORM mpich2. Riadok "source" spustí konfiguračný súbor DEFORM "CONFIG.COM", aby sa nastavili všetky symboly potrebné (alias) na spustenie systému DEFORM. V prípade symbolov nastavených v konfiguračnom súbore CONFIG.COM by používateľ nemal tieto symboly prepisovať alebo definovať inak ako v pôvodnom texte.

  
**Poznámka** : Nastavenia by mali byť aktívne pre všetky shelly, nielen pre interaktívne shelly.

  
Používateľ sa môže v tomto okamihu odhlásiť zo systému. Pri ďalšom prihlásení do systému sa automaticky vykonajú vyššie uvedené príkazové riadky.

  
Ak sa v tomto čase rozhodnete zostať v systéme, musíte súbor ".cshrc" spustiť ručne, pretože jeho obsah sa zmenil. Ak to chcete urobiť, zadajte "source .cshrc".

  
Spustením nasledujúcich príkazov overte, či sú premenné prostredia správne nastavené.

_echo $DEFORM_DIR_ (výsledkom by mala byť inštalačná cesta 2d)

_echo $DEFORM3_DIR_ (výsledkom by mala byť 3d inštalačná cesta)

_echo $DEFORM23_DIR_ (výsledkom by mala byť cesta k inštalácii integrovaného systému)

_echo $DEF_CFG_DIR_ (výsledkom by mala byť cesta ku konfiguračnému priečinku licencie)

## DEFORM Nastavenie

Pred spustením programu DEFORM Setup je potrebné spustiť program Services Control. Nespúšťajte službu pomocou príkazu "service deformscd start"; spôsobí to problémy s generovaním zostáv. Namiesto toho ju spustite podľa nasledujúceho postupu.

_/etc/init.d/deformscd start_

Spustite inštalačný program, v ktorom uvediete cestu inštalácie a údaje o serveri pre servery Správca licencií a Dávkové fronty.  
(na základe predvolenej inštalačnej cesty prejdite na priečinok v14.0.2 a spustite inštaláciu)

_cd /usr/local/SFTC/DEFORM/v14.0.2_

_./DEFORMSetup.EXE_

(Pri vykonávaní tejto akcie zo vzdialeného počítača je potrebné nastaviť príslušné nastavenia servera X)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_2_installation_of_deform_v12_0_1_in_linux/2_2_image001.jpg' | relative_url }})

Okno nastavenia DEFORM

Po otvorení dialógového okna DEFORMSetup je potrebné zadať nasledujúce základné informácie:

  * Názov stroja alebo IP adresa miesta, kde je správca licencií spustený, ako je identifikované v sieti.

  * Port servera správcu licencií má byť definovaný ako 34445. Upozorňujeme, že toto číslo nie je možné zmeniť.

  * Po kliknutí na "Synchronizovať" by sa mal v Správcovi licencií vrátiť pozitívny stav. Ak sa tak nestane, skontrolujte požadované komponenty, ako je stav démona ovládača kľúča Sentinel, hardvérový kľúč, stav behu démona správcu licencií a súbor s heslom.

  * Po úspešnej synchronizácii, bez ohľadu na to, či je licenčný server spustený na miestnom alebo vzdialenom počítači, kliknite na tlačidlo "Uložiť", aby ste uložili nastavenia.

  * Nastavenie simulačného servera vyžaduje aj názov stroja, na ktorom je služba umiestnená, a číslo portu. V prípade viacerých definícií simulačného servera sa odporúča najprv načítať/synchronizovať existujúce informácie zo servera správcu licencií, opraviť alebo doplniť informácie a uložiť na server správcu licencií. Opäť platí, že tieto informácie sú potrebné len v prípade, ak je licencovaná dávková fronta. Upozorňujeme, že nastavenie dávkového frontu a simulačného servera je povinné na spustenie úloh DOE a OPT. Simulačné servery môžete spustiť na karte Simulation Server (Simulačný server).

  * Upozorňujeme, že pri zmene akýchkoľvek informácií a ich uložení v nástroji DEFORMSetup môže dôjsť k prerušeniu služieb pri používaní toho istého servera.

  * Nakonfigurujte systémový firewall tak, aby boli prístupné porty používané pre služby DEFORM (34444 a 34445 (správca licencií), 34446 (server dávkovej fronty), 34447 (simulačný server) a 34448 (služby DEFORM, s TCP).

  * Systémové porty pre 34449+ musia byť tiež prístupné. Počet portov, ktoré je potrebné otvoriť v danom rozsahu, závisí od počtu súbežných úloh DOE/OPT, ktoré môžu byť spustené v danom čase.

Karta Služby DEFORM umožňuje správu služieb DEFORM a je nová od verzie 11.2.

Máte dve možnosti:

  1. Spravujte službu DEFORM spustenú v miestnom počítači.
  2. Spravujte služby DEFORM spustené vo všetkých počítačoch.

Prvá možnosť je k dispozícii pre každého používateľa programu DEFORM. Druhá možnosť je dostupná len pre "oprávnených používateľov" alebo používateľov, ktorí poznajú "prístupový kód" vytvorený oprávneným používateľom.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_2_installation_of_deform_v12_0_1_in_linux/2_2_image002.jpg' | relative_url }})

Ak chcete nastaviť používateľa ako autorizovaného používateľa, budete potrebovať prístup root v počítači, v ktorom je spustený Správca licencií. V priečinku License Manager (zvyčajne na adrese

_/usr/local/SFTC/LicenseManager_) vytvorte alebo upravte súbor "authorized_users.txt". V tomto súbore bude zoznam používateľov, ktorí sú autorizovanými používateľmi. Formát zoznamu je:

_názov_užívateľa1@názov_počítača1_

_názov_užívateľa2@názov_počítača2_

Autorizovaný používateľ má úplnú kontrolu nad službami DEFORM.

  * Prístup k službám DEFORM všetkých počítačov DEFORM.
  * Nastavenie alebo zmena prístupového kódu služby DEFORM.
  * Aktualizujte súbor s licenčným heslom DEFORM (DEFORM.PWD).

Prístupový kód služby DEFORM umožňuje prístup k službám DEFORM na všetkých počítačoch DEFORM od:

  * Akýkoľvek počítač DEFORM (iný ako autorizovaný počítač)
  * Akýkoľvek počítač s webovým prehliadačom (nie je potrebné inštalovať DEFORM)

Prístupový kód môže vytvoriť alebo zmeniť iba oprávnený používateľ DEFORM.

Karta Služby DEFORM umožňuje spúšťať a zastavovať služby DEFORM na serveri a počítačoch DEFORM, ako aj aktualizovať aplikácie služieb na počítačoch DEFORM. Ak je niektorá zo služieb zastavená, kliknutím na príslušné tlačidlo spustenia službu spustíte.

## Vykonávanie systému

Na spustenie systému DEFORM sa môže použiť nasledujúci postup:

  1. Prihláste sa do používateľského konta DEFORM z terminálu X

  2. Spustite nasledujúce príkazy na vyvolanie systému DEFORM.

DEF_GUI | Hlavné rozhranie pre DEFORM
---|---
mo | Integrovaný výrobný proces (MO)
mo64 | 64-bitový integrovaný výrobný proces (MO)
  
  1. Úplný zoznam príkazov nájdete po zadaní príkazu alias.

## OTÁZKY / PROBLÉMY

Ak máte akékoľvek otázky, pripomienky alebo problémy s inštaláciou DEFORM V14.0.2, kontaktujte:

**Scientific Forming Technologies Corporation**

**2545 Farmers Drive,****Suite 200**

**Columbus, OH 43235 USA**

**Telefón: (614) 451-8330**

**E-mail:[support@deform.com](mailto:support@deform.com)**

**alebo**

**Navštívte našu webovú stránku na adrese<http://www.deform.com>**

## Typy CPU

Tu nájdete niekoľko zdrojov na určenie generácie vášho procesora Intel.

  
Ak chcete určiť používateľský procesor, zadajte

cat /proc/cpuinfo | grep "názov modelu"

Na tejto webovej lokalite spoločnosti Intel nájdete prehľad o tom, ako určiť generáciu vášho procesora založeného na jadre porovnaním so zisteným procesorom, ako je uvedené vyššie.

<https://www.intel.com/content/www/us/en/processors/processor-numbers.html>

  
Ak sa vám nepodarilo určiť generáciu procesora Intel z vyššie uvedeného odkazu, skúste nasledovné.

  1. Kliknite na jeden z nasledujúcich odkazov (v závislosti od typu procesora) a vyhľadajte svoj procesor.

Pre procesory Intel Xeon:  
<https://en.wikipedia.org/wiki/List_of_Intel_Xeon_microprocessors>

Pre procesory Intel Core i7:

<https://en.wikipedia.org/wiki/List_of_Intel_Core_i7_microprocessors>

Ďalšie procesory Intel Core nájdete v časti "Pozri tiež" na konci stránky o procesoroch Intel Core i7.

  
Ak sa napríklad podľa vyššie uvedených pokynov zobrazí zistený procesor ako:

názov modelu : Intel(R) Core(TM) i7-6700 CPU @ 3,40GHz

Potom vyhľadajte položku "6700".

Zobrazí sa prepojenie, ktoré vás presmeruje na webovú lokalitu spoločnosti Intel s ďalšími informáciami.

  1. Kliknite na tento odkaz.

  2. Na stránke spoločnosti Intel možno architektúru nájsť pri pohľade na kódové označenie "Products formerly _______".

  3. Teraz, keď poznáte architektúru, môžete zistiť, či je staršia alebo novšia ako Haswell, kliknutím na nasledujúci odkaz a vyhľadaním architektúry.

<https://en.wikipedia.org/wiki/List_of_Intel_CPU_microarchitectures>

****
