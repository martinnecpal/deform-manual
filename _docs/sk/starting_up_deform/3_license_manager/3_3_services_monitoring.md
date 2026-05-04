---
lang: sk
title: "3.3. Monitorovanie služieb"
---

# 3.3. Monitorovacie služby

V systéme DEFORM máme 3 služby na licencovanie a radenie simulácií. Sú to DeformLicenseServer, DeformSimServer a DeformBatchQueue server.

Licenčný server riadi všetky produkty a možnosti závislé od licencie DEFORM na základe licenčného hesla poskytnutého SFTC. Patrí sem 2D alebo 3D modul, rôzni sprievodcovia DEFORM, počet simulácií, radenie simulácií do frontu a viacero procesorov.
simulácie.

Dávkový frontový server sa používa na odosielanie dávok úloh vo fronte. Používateľ môže odoslať jednu alebo viac úloh na spustenie vo fronte na základe dostupných licencií a počtu simultánnych simulácií povolených zo simulačného servera. Pri zaraďovaní úloh do frontu musí byť simulačný server spustený v počítači, v ktorom sa majú úlohy spustiť.

**Spustenie, zastavenie a reštartovanie služieb:**

Používateľ môže spustiť a zastaviť služby zo Správcu úloh, ale spustenie služieb z nástrojov na správu systému Windows Služba poskytne viac možností, napríklad Spustiť ako niektorý z používateľov alebo Spustiť ako systém. Používateľ musí otvoriť služby ako správca.

  
**Kontrola stavu služieb:**

Stav služieb možno skontrolovať na karte Procesy Správcu úloh v systéme Windows-XP sledovaním stavu spustiteľných súborov servera, v prípade počítača so systémami Windows7, Windows 8 a Windows 10 možno stav skontrolovať na karte Služby.  
Túto skutočnosť možno skontrolovať aj v nástrojoch Windows pre správu Services (Služby) sledovaním ich stavu.

Reštartovaním systému sa automaticky spustia všetky 3 služby DEFORM, v počítači Sever sa spustí služba dávkového frontu a služba simulácie v klientskom počítači, v ktorom je potrebné spustiť úlohy, je potrebné odoslať úlohy do frontu. Používateľ teda musí skontrolovať stav týchto služieb pred odoslaním úloh do frontu. Toto je možné skontrolovať aj v dialógovom okne Možnosti spustenia hlavného grafického rozhrania DEFORM Kontrola servera.

V prípade akýchkoľvek problémov súvisiacich s licenciou môže používateľ sledovať súbor protokolu licencie, či neobsahuje konkrétne chybové hlásenia pre spustenie alebo zastavenie služieb.

**Súvisiace témy:**

[3.1. DEFORM License Setup](/docs/sk/starting_up_deform/3_license_manager/3_1_deform_license_setup/)

[3.2. License Monitoring](/docs/sk/starting_up_deform/3_license_manager/3_2_license_monitoring/)

[3.4. Trouble Shooting License Issues](/docs/sk/starting_up_deform/3_license_manager/3_4_trouble_shooting_license_issues/)
