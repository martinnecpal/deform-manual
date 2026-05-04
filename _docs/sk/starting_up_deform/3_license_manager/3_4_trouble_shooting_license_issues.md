---
lang: sk
title: "3.4. Riešenie problémov s licenciami"
---

# 3.4. Riešenie problémov s licenciami

3.4.1. Identifikácia problému licenčného servera v12.1

3.4.2. Riešenie problému licenčného servera v12.1: špecifické problémy témy

3.4.3. Rôzne poznámky týkajúce sa služieb

## Identifikácia problému licenčného servera v12.1

**Krok 1**

Skontrolujte, či je licenčný server spustený, otvorením karty "služby" v Správcovi úloh. Ak sa DeformLicenseserver zobrazí ako spustená služba, potom je spustený.

  * Ak je spustený, prejdite na krok 2 (A) vysvetlený nižšie.

  * Ak nie je spustený, prejdite na krok 2 (B) vysvetlený nižšie.

  
**Krok 2**

(A) Pravdepodobne ide o problém s heslom alebo hardvérovým kľúčom. Existujú tri spôsoby kontroly:

  * Zobrazte najnovší súbor protokolu [zvyčajne v C:\Program Files\SFTC\License Manager\log\<year>\].

  * Spustite diagnostický nástroj v priečinku Správca licencií [zvyčajne sa nachádza na adrese C:\Program Files\SFTC\Správca licencií\Defdiag.exe] a kliknite na tlačidlo Získať informácie... Výsledný súbor .dgf pomôže tímu podpory diagnostikovať problém.

  * Ak sa v programe DEFORM Setup po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_syncronize_button.jpg' | relative_url }}) zobrazí správa "licenčný server je ukončený": problém s hardvérovým kľúčom.

Ak sa na kontrolu chýb používa súbor denníka:

  * Ak súbor protokolu uvádza, že hardvérový kľúč je neplatný: Hardvérový kľúč problém. Prosím, pošlite súbor .dgf na adresu [support@deform.com](mailto:support@deform.com)

  * Ak je v súbore denníka uvedené "žiadne heslo" alebo "žiadne dostupné heslo": problém s heslom. Kontaktujte [support@deform.com](mailto:support@deform.com). Upozorňujeme, že ak ste dostali nový súbor s heslom, ktorý nahradil súbor s heslom, ktorého platnosť vypršala, je dôležité reštartovať službu License Manager Service alebo reštartovať počítač License Manager Server.

(B) Je spustený starý licenčný server, problém s registračnou službou alebo problém s inštaláciou:

Ak je v log súbore [zvyčajne v C:\Program Files\SFTC\License Manager\log\<year>\] napísané "môže byť spustený starý licenčný server (v2.1)", problém je identifikovaný: starý licenčný server je spustený.

  * Otvorte DEFORMSetup a navštívte kartu Služby. V záložke Services (Služby) kliknite na "Open DEFORM Service for local DEFORM computer" (Otvoriť službu DEFORM pre miestny počítač DEFORM). Mala by sa nám zobraziť značka chyby, ako je znázornené na obrázku [Fig. 3.1.21.](3_1_deform_license_setup.htm#Fig._3.1.21._Updating_Simulation_services_files_in_DEFORM_Services_window)(a). Chybová značka ![]({{ '/assets/icons/pre_icons/error_status_icon.jpg' | relative_url }}) znamená, že lokálny počítač DEFORM nepoužíva rovnakú verziu License Manger ako systém licenčného servera DEFORM, preto kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_deform_setup_update_icon.jpg' | relative_url }}) a aktualizujte služby lokálneho počítača DEFORM. Po aktualizácii služieb si môžeme všimnúť ikonu ![]({{ '/assets/icons/pre_icons/mo_deform_setup_valid_sucess_icon.jpg' | relative_url }}) vedľa lokálneho počítača DEFORM. Program DEFORMsetup možno zatvoriť a grafické používateľské rozhranie DEFORM možno spustiť z ponuky Štart ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Programs.

Ak problém stále nie je identifikovaný, kontaktujte [support@deform.com](mailto:support@deform.com).

## Riešenie problému licenčného servera v12.1: špecifické problémy témy

### Problém s heslom

Skopírujte správny súbor v*_* (kde *_* je číslo verzie programu DEFORM) DEFORM.PWD do adresára licenčného servera (C:\Program Files\SFTC\Licence Manager). Na načítanie/aktiváciu nového súboru hesla je potrebný reštart alebo reštart služby.

### Kontrolný zoznam problémov s hardvérovým kľúčom

  * Je dôležité odinštalovať ovládač Sentinel verzie 7.5 alebo staršie. Odstráňte hardvérový kľúč, odinštalujte starý ovládač (ovládače) a nainštalujte nový ovládač.
  * Skontrolujte, či používateľ nainštaloval ovládač Sentinel verzie 7.6.3 (je to možnosť v procese inštalácie). Ak nie, nainštalujte nový ovládač.
  * Skontrolujte, či je port USB neaktívny. Prepnite kľúč USB na iný port USB a skúste reštartovať službu a server.
  * Ak sa pri inštalácii ovládača Sentinel v systéme Windows 7 objaví chybové hlásenie "Nepodarilo sa pridať súbor Sentinel64.cat" a používate hardvérový kľúč USB, túto chybu môžete bezpečne ignorovať.

### Stará licencia je spustená

Používateľ musí odinštalovať starý licenčný server (v2.1) alebo ho vypnúť.

### Problém so spustením služby

K tomu môže občas dôjsť, najmä ak používateľ vymieňa kľúč USB medzi počítačmi. Nasledujúce metódy možno použiť na spustenie služby DeformLicenseServer, keď sa objaví v zozname služieb systému Windows a je tiež zastavená.

  * Reštartujte počítač s licenčným serverom.

  * Otvorte konzolu na správu služieb (nie Správcu úloh) a spustite službu ručne.

  * Otvorte DEFORMSetup a navštívte záložku služby, ak je licenčný server na lokálnom systéme, vyberte "Open DEFORM Service for local DEFORM computer" (Otvoriť službu DEFORM pre lokálny počítač DEFORM), inak vyberte "Open DEFORM Service for all DEFORM computers" (Otvoriť službu DEFORM pre všetky počítače DEFORM) a zadajte prístupový kód. Kliknutím na tlačidlo![]({{ '/assets/icons/pre_icons/run_action_icon.jpg' | relative_url }}) vedľa licenčného servera v stĺpci "Actions" (Akcie) spustite službu.

## Rôzne poznámky týkajúce sa služieb

**Poznámky k službám v systéme Windows Vista a novších**
Na registráciu, spustenie alebo zrušenie registrácie služby sa vyžaduje zvýšené oprávnenie správcu prostredníctvom systému Windows User Access Control [UAC]. Je to potrebné aj v prípade, že používateľ už má v počítači administrátorské oprávnenia. Správu služby možno vykonať v konzole na správu služieb alebo pomocou funkcie "Spustiť ako správca" so zástupcami ponuky DEFORM Service Start (Štart).

**Súvisiace témy:**

[3.1. DEFORM License Setup](/docs/sk/starting_up_deform/3_license_manager/3_1_deform_license_setup/)

[3.2. License Monitoring](/docs/sk/starting_up_deform/3_license_manager/3_2_license_monitoring/)

[3.3. Services Monitoring](/docs/sk/starting_up_deform/3_license_manager/3_3_services_monitoring/)
