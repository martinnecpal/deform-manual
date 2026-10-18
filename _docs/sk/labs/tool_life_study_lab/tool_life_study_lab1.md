---
lang: sk
title: "Laboratórium štúdie životnosti nástroja1"
---

# Laboratórium štúdie životnosti nástroja1

1.1 Úvod

1.2. Vytvorenie nového problému

1.2.1. Pridanie štúdie životnosti nástroja

1.2.2. Definícia objektov

1.2.2.1. Horná matrica

1.2.2.2. Spodná matrica

[1.2.3. SS Temperature/Wear]({{ '/docs/sk/labs/tool_life_study_lab/tool_life_study_lab1/' | relative_url }}#1_2_3_SS_Temperature/Wear)

1.2.3.1. Extrakcia údajov

1.2.3.2. Armatúra krivky

1.2.3.3. Ovládacie prvky simulácie

1.2.4. Únava

1.2.4.1. Výber cyklu

1.2.4.2. Ovládacie prvky simulácie

1.2.5. Generovať databázu

1.2.6. Simulácia chodu

1.2.7. Post Processing

1.2.7.1 Životnosť nástroja

Úvod

Životnosť nástroja má vplyv na výrobné náklady. Je určená mnohými faktormi, ako je teplota nástroja, opotrebovanie nástroja, únava nástroja atď. V module životnosti nástroja vykonávame výpočet teploty v ustálenom stave, predikciu opotrebenia nástroja a viacstupňový výpočet napätia matrice v preprocesore, ktorý sa použije na analýzu únavy v postprocesore.

V tomto laboratóriu budeme kopírovať už simulovaný 2D projekt Spike, ktorý má formovaciu operáciu simulovanú počas 5 cyklov s výpočtom opotrebenia nástroja pre matrice.

## Vytvorenie nového problému

Na počítači so systémom Windows prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * v1x.x. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. TLSL1.1. Pomocou prepínača vyberte prepínač „* * Integrovaný výrobný proces **“ a systém ** Unit ** ako „** SI * * “. Definujte názov problému ako "**2D_Tool_Life_Study** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0001.jpg' | relative_url }})

Okno výberu typu problému

  
Sprievodca viacnásobnou operáciou sa otvorí s dialógovým oknom Nový projekt, ako je znázornené na obr. TLSL1.2., v tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**2D_Tool_Life_Study** “. Importujeme už simulovaný 2D projekt „2D_Tool_Life_Study“ z 2D/LABS/ inštalačného priečinka pomocou možnosti „Kopírovať existujúci projekt“.

Vyberte prepínač „**Kopírovať existujúci projekt** “ v dialógovom okne Nový projekt, potom kliknite na Zdrojové umiestnenie a vyhľadajte súbor „** 2D_Tool_Life_Study.moproj ** “ z inštalačného priečinka 2D\LABS\2D_Tool_Life_Study pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_browse_button.jpg' | relative_url }}). Zapnite začiarkavacie políčko „**Kopírovať databázový súbor** “, ako je znázornené na obr. TLSL1.2. aby sa databázový súbor skopíroval spolu so súborom projektu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie. Načítaný projekt MO je znázornený na obr. TLSL1.3.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0002.jpg' | relative_url }})

Sprievodca MO Nový projekt s možnosťou Kopírovať existujúci projekt

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0003.jpg' | relative_url }})

Skopírovaný 2D_Tool_Life_Study projekt Načítaný v sprievodcovi MO

### Pridanie štúdie životnosti nástroja

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) (Pridať novú štúdiu) a vyberte možnosť „**Pridať štúdiu životnosti nástroja ** “, ako je znázornené na obr. TLSL1.4. Pridaná štúdia životnosti nástroja je znázornená na obr. TLSL1.5.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0004.jpg' | relative_url }})

Pridanie štúdie životnosti nástroja

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0005.jpg' | relative_url }})

Pridaná prevádzka štúdie životnosti nástroja v MO.

Predmety matrice sa načítajú z operácie tvárnenia. V položke úlohy sú tri možnosti,

* Teplota v ustálenom stave,

* Opotrebovanie náradia a

únava

  
Prvé dve možnosti, teplota v ustálenom stave a opotrebenie nástroja, predpovedajú teplotu v ustálenom stave a opotrebenie nástroja na základe údajov histórie z operácie tvárnenia. Možnosť Únava aktivuje viacstupňovú záťažovú štúdiu a použije údaje o záťaži na vykonanie analýzy únavy v postprocesore. V tomto príklade vyberieme všetky tri možnosti. Všimnite si, že pri aktualizácii možností položky úlohy sa aktualizuje aj operačný strom, ako je znázornené na obr. TLSL1.6.

  
V položke úlohy skontrolujte, či sú začiarknuté políčka Ustálená teplota, Opotrebenie nástroja a Únava a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Objekt.

  
POZNÁMKA:
• Lisovnice, ktoré sa skúmajú z hľadiska teploty v ustálenom stave a opotrebovania nástroja, musia byť sieťované v nominálnom nastavení, pre pracovnú sieť len pre únavu sa v nominálnom nastavení nevyžaduje.

• Začiarkavacie políčko „Definovať model na výpočet opotrebenia nástroja“ musí byť zapnuté v medziobjektových vzťahoch nominálneho nastavenia pre matrice, ktorých opotrebenie nástroja sa bude skúmať.

• Štúdia životnosti nástroja sa môže vykonať len pre jednu operáciu tvárnenia a táto operácia tvárnenia musí byť v cykle v nominálnom nastavení na vykonanie štúdie životnosti nástroja.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0006.jpg' | relative_url }})

Aktualizácia položky úlohy

### Definícia objektov

Na štúdiu životnosti nástroja v tomto laboratóriu použijeme všetky objekty matrice z operácie „tvárnenie“, takže kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Top Die (Horná matrica).

#### Top Die

Obr. TLSL1.7. zobrazuje stránku objektu hornej matrice. Pre každý objekt máme tiež tri možnosti – teplota v ustálenom stave, opotrebovanie nástroja a únava. To nám umožňuje vybrať, či je pre aktuálny objekt potrebná/vylúčená konkrétna analýza. V tomto laboratóriu ponecháme predvolený výber a vykonáme všetky tri úlohy pre každý objekt matrice. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku BCC.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0007.jpg' | relative_url }})

Stránka objektu Top Die

##### Horné hraničné podmienky

Použite hraničnú podmienku rýchlosti (Vy=0) pre hornú matricu na hornom povrchu, ako je znázornené na obr. TLSL1.8. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Spodná matrica.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0008.jpg' | relative_url }})

Priradená hraničná podmienka rýchlosti (Vy=0) pre hornú matricu

#### Spodná matrica

V tomto laboratóriu ponecháme predvolený výber a vykonáme všetky tri úlohy pre každý objekt matrice. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku BCC.

##### Hraničné podmienky spodnej matrice

Použite Vx=0 hraničnú podmienku rýchlosti na povrchu symetrie a Vy=0 hraničnú podmienku rýchlosti pre spodnú matricu na spodnom povrchu, ako je znázornené na obr. TLSL1.9. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až do stránky SS Teplota/Opotrebenie.

  
![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0009.jpg' | relative_url }})

Priradená hraničná podmienka rýchlosti pre spodnú matricu

### SS Teplota/opotrebenie

Teraz nastavíme simuláciu teploty v ustálenom stave a opotrebenia nástroja. Zámerom je extrahovať tepelný tok/opotrebenie z kontaktnej oblasti s obrobkom a prispôsobiť údaje pomocou exponenciálnych funkcií. Potom uložte namontované údaje na objekty matrice a spustite simuláciu prenosu tepla na dostatočne dlhú dobu, kým nedôjde ku konvergencii tepelného stavu.

Extrakcia údajov

Kliknite na ** Extrakcia údajov ** zo stromu prevádzky, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_extract_data_button.jpg' | relative_url }}) spustite extrakciu tepelného toku/opotrebenia z kontaktnej oblasti s obrobkom. Indikátor priebehu na stránke Extrakcia údajov zobrazuje priebeh extrakcie tepelného toku a opotrebenia z kontaktnej oblasti predmetov matrice. Po dokončení extrakcie a montáže môžeme vidieť namontované koeficienty na stránke krivky montáže. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Curve Fitting.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0010.jpg' | relative_url }})

Extrakcia údajov

#### Prispôsobenie krivky

Kontaktovanú oblasť a namontovanú krivku môžeme skontrolovať kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}), ako je znázornené na obr. TLSL1.11. Medzitým sa vygenerujú a uložia súbory stredných a konečných výsledkov do adresára Operations/Task00004, ktorý obsahuje dva podpriečinky – HeatFlux a ToolWear, ktoré ukladajú výsledky pre extrakciu tepelného toku a extrakciu opotrebenia nástroja, a OutputForPredict.KEY, čo je súbor kľúčových slov objektu obsahujúci namontované koeficienty.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0011.jpg' | relative_url }})

Stránka Curve Fitting

#### Ovládacie prvky simulácie

Nastavili sme parametre riadenia simulácie pre predikciu teploty v ustálenom stave, ktorá zahŕňa simuláciu prenosu tepla na matricových objektoch s tepelným tokom BCC pomocou namontovaných koeficientov. Ako je znázornené na obr. TLSL1.12. potrebujeme len definovať tri parametre - počet cyklov na predpovedanie (celkový čas sa vypočíta automaticky na základe času procesu tvarovacej operácie, ktorá je v cykle), buď časový krok alebo celkový krok a krok prírastku. Predvolený počet cyklov na predpovedanie je nastavený na 10-násobok počtu cyklov v operácii tvárnenia, čo je v tomto prípade 50. V tomto laboratóriu použijeme * * počet cyklov * * na predpovedanie ako * * 50 ** s ** časom ** ** krokom ** ako * * 0,0100093 * * sek/krok a * * krokom * * ako * * 1 * *, ako je znázornené na obr. TLSL1.12.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0012.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie teploty

Únava

Poslednou úlohou v preprocesore je Únava, čo je v podstate nastavenie výpočtu napätia formy vo viacerých krokoch od prevádzky cyklu. Prvým krokom je výber cyklov z tvárniacej operácie na vykonanie výpočtu napätia formy (pozri obr. TLSL1.13.). Môžeme buď vybrať posledný cyklus z databázy, všetky cykly alebo zvoliť cykly postupne. Budeme tiež musieť nastaviť simulačné kontrolné parametre pre výpočet napätia v zápustke (pozri obr. TLSL1.14.).

VÝBER CYKLU

Vyberte „**Cyklus*** *****Výber** “ v časti Únava zo stromu operácií, uistite sa, že je predvolene vybraný „* * Posledný ** * * cyklus * * “, ako je znázornené na obr. TLSL1.13. Ak nie je vybraté, vyberte prepínač „* * Posledný ** * * cyklus * * “. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku ovládacích prvkov simulácie.

  
![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0013.jpg' | relative_url }})

VÝBER CYKLU

#### Ovládacie prvky simulácie

V ovládacích prvkoch simulácie použijeme predvolený **počet krokov simulácie * * ako ** 1 **, ** prírastok kroku na uloženie* * ako * * 1 * * a * *čas na krok* * ako * * 1e-06 * *, ako je znázornené na obr. TLSL1.14. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete stránku DB.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0014.jpg' | relative_url }})

Únava - stránka s ovládacími prvkami simulácie

Všeobecné

Keď klikneme na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na Generovanie DB, dostaneme vyskakovacie okno extrakcie údajov pri načítaní stránky generovania DB, ako je znázornené na obr. TLSL1.15. V kontextovom okne vyberte ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}), pretože sme už vykonali extrakciu údajov.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0015.jpg' | relative_url }})

Vyskakovacie okno Extrakcia údajov

Kliknite na štítok akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a skontrolujte, či sa nevyskytli nejaké chyby alebo varovania, ktoré by zastavili generovanie DB. Ak nie sú žiadne chyby alebo upozornenia, vytvorte databázu kliknutím na štítok akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) (pozri obr. TLSL1.16.).

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0016.jpg' | relative_url }})

Okno Generovať databázu

### Simulácia behu

Po vygenerovaní databázy prepnite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad operačným stromom. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. TLSL1.17. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať z posledného kroku** “ (z kroku -1) a potom vyberte režim simulácie ako **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0017.jpg' | relative_url }})

Vyskakovacie okno s možnosťami spustenia

Priebeh simulácie je možné monitorovať počas jej priebehu tak, že sa pozriete na kartu Simulačná správa a Simulačná grafika z oblasti grafického zobrazenia v režime simulácie. Ak je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) na karte Simulation Message (Simulačná správa), ktorá je predvoleným nastavením, súbor správy sa automaticky obnoví.

  
Súbor správy poskytuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a informácie o tom, ako dobre simulácia prebieha, ako je znázornené na obr. TLSL1.18.

  
![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0018.jpg' | relative_url }})

Simulačný režim

Postprocessing

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) a navštívte postprocesor MO. Simulované výsledky možno vidieť v Post ( obr. TLSL1.19.). Obsahuje dve časti, jedna je teplotná história z chodu prenosu tepla s uloženým tepelným tokom BCC a druhá je namáhanie formy.

  
Kroky analýzy prenosu tepla v ustálenom stave a analýzy opotrebenia nástroja sú zoskupené pod názvom simulácie SS Temp. Tu názov simulácie **Fatigue-Step52** znamená napätie matrice vyplývajúce z kroku 52 v operácii tvárnenia. Na analýzu únavy sa používa zvýraznený panel nástrojov založený na vypočítaných údajoch o napätí matrice. Obr. TLSL1.19. zhŕňa výsledky simulácie teplotných a matricových napätí z predikcie teploty SS a viacstupňovej stresovej štúdie matrice. Posledný krok urobíme zo simulácie prenosu tepla ako teploty v ustálenom stave a uložíme ju na objekty matrice pri výpočte napätia matrice. Všimnite si, že ak zvolíme únavu ako jedinú úlohu, uložíme teplotný profil z príslušných krokov z tvarovacej operácie ako počiatočnú teplotu.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0019.jpg' | relative_url }})

MO Post – Únava – krok 52

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) v prehliadači krokov, potom prehrajte animáciu z prvého kroku pomocou premennej teplotného stavu a sledujte teplotu matrice, keď sa blíži k ustálenému stavu.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0020.jpg' | relative_url }})

VÝSLEDKY SIMULÁCIE

#### Životnosť nástroja

Nástroj Life Post sa používa na analýzu výsledkov teploty v ustálenom stave a opotrebovania nástroja, ako aj na predpovedanie únavovej životnosti matríc. Z príspevku MO môžeme získať prístup k životnosti nástroja kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_tool_life_post_icon.jpg' | relative_url }}), ako je znázornené na obr. TLSL1.19. Životnosť nástroja je otvorená, ako je znázornené na obr. TLSL1.21

  
**SS Temp & Wear**: Výberom tejto možnosti môžeme vykresliť výsledky pre prevádzku SS Temp & Wear (pozri obr. TLSL1.21.). V rámci tejto možnosti môžeme pre vybraný cyklus zobraziť teplotu nástroja, hĺbku opotrebenia nástroja, rýchlosť opotrebenia nástroja a výstup opotrebovanej geometrie.

  
Rôzne číslo cyklu môžeme vybrať v časti **Cyklus ** potiahnutím posuvnej lišty alebo zadaním príslušného čísla cyklu do vstupného poľa. Po zadaní čísla cyklu môže používateľ vybrať jeden z výsledkov opotrebovania nástroja a zobraziť výsledky na displeji, obr. TLSL1.22 zobrazuje hĺbku opotrebenia nástroja v cykle 40.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0021.jpg' | relative_url }})

Výsledky životnosti nástroja pre SS Temp & Wear

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0022.jpg' | relative_url }})

Výsledok miery opotrebenia nástroja v cykle 40

  
**Únava** : Výberom tejto možnosti môžeme zakresliť výsledky pre únavovú prevádzku (pozri obr. TLSL1.23.). Spočiatku nebude v zozname žiadny model únavy. Model únavy môžeme pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Pridáva sa model s názvom „* * AISI ** **-1025: ** * * SNSD_CONST * * “, kde AISI-1025 znamená názov materiálu a SNSD_CONST znamená štandardný model založený na napätí. Môžeme pozorovať, že štandardný model založený na strese je vybraný ako typ modelu. Parametre modelu môžeme definovať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) a zobrazí sa editor funkcií. Parametre, ktoré sme pre tento model definovali, nájdete na obr. TLSL1.24. Ďalším spôsobom, ako pridať model únavy, je načítanie súborov modelu z adresára používateľa alebo knižnice únavy. Všimnite si, že musíme byť na stránke Únava, aby sme aktivovali tlačidlá zaťaženia (pozri obr. TLSL1.25.). Súbor modelu má rovnaký formát ako súbor kľúčového slova, kde za kľúčovým slovom nasleduje jeho hodnota.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0023.jpg' | relative_url }})

Životnosť nástroja – únavový výstup

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0024.jpg' | relative_url }})

Definícia modelu únavy

  
![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0025.jpg' | relative_url }})

Načítava sa súbor modelu

Akonáhle je model definovaný, môžeme vidieť graf predikcie únavovej životnosti výberom buď Absolute Max principal alebo Signed Von Mises alebo Signed Shear ako kombinovanú metódu s modelom a kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}). Výsledok je znázornený na obr. TLSL1. 26.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0026.jpg' | relative_url }})

Únava Životný graf
