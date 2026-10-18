---
lang: sk
title: "2D HT Lab 5 – Vstupné údaje"
---

# 2D HT Lab 5 – Vstupné údaje

Príprava údajov o materiáloch a fázových premenách

  
5.1. Zhrnutie problému

5.2. Základné pojmy

5.3. Vytvorenie nového problému

5.4. Nastavenie vlastností materiálu

5.5. Nastavenie vlastností medzi materiálmi

## Zhrnutie problému

Cieľom tohto cvičenia je oboznámiť používateľa so zadávaním vlastností materiálov potrebných na modelovanie fázových prechodov v programe DEFORM®. V rámci tohto cvičenia používateľ upraví materiál zo systémovej knižnice materiálov, aby vytvoril nový súbor údajov pre iný druh ocele.

Kľúčové pojmy, na ktoré by sa mal používateľ zamerať, sú:

  1. Aké vlastnosti materiálu sú potrebné na definovanie fázy?

  2. Aké údaje sú potrebné na opísanie prechodu medzi fázami?

  3. Ako je možné pripraviť vstupné údaje pre simuláciu tepelného spracovania v programe DEFORM® na základe metalurgických referenčných alebo experimentálnych údajov?

## Základné pojmy

V simuláciách DEFORM sú deformácia, prenos tepla, fázová premena a difúzia navzájom prepojené. Obr. 2DHTML5.1. znázorňuje základný popis ich vzájomných vzťahov. Napríklad v prípade uhlíkovej ocele sú vlastnosti materiálu funkciami obsahu uhlíka. Keďže sa koncentrácia uhlíka môže meniť difúziou, menia sa s ňou aj mechanické a tepelné vlastnosti ocele.

V programe DEFORM je možné materiál definovať ako „zmesový“ materiál, ktorý sa skladá zo súboru zložkových materiálov, z ktorých každý má svoje vlastné údaje o pružnosti, plasticite a tepelných vlastnostiach. Tieto zložkové materiály sa označujú ako „fázy“. Vlastnosti tohto zmesového materiálu sa určujú na základe vlastností fáz pomocou pravidla váženého priemeru zmesi, založeného na objemovom podiele každej fázy.

Obr. 2DHTML5.2. znázorňuje príklad transformačných vzťahov uhlíkovej ocele. Uvažujú sa tri rôzne fázy: austenit, martenzit a perlit. Austenit existuje pri vyšších teplotách, zatiaľ čo martenzit (metastabilný) a perlit (stabilný) sú fázy pri nižších teplotách. Metastabilné fázy možno vytvoriť rýchlym ochladením austenitu. Vlastnosti prechodu z jednej fázy do druhej sú definované kinetickým modelom, ktorý slúži na určenie rýchlosti prechodu a ďalších vlastností, ako je latentné teplo a zmena objemu. Údaje o prechode sa tiež označujú ako medzimateriálové vlastnosti.

(Všimnite si, že definícia pojmu „fáza“ v programe DEFORM sa mierne líši od vedeckej definície pojmu „fáza“ v niektorých učebniciach, kde sa napríklad perlit nepovažuje za „fázu“, ale za „mikrozložku“ pozostávajúcu z viacerých „fáz“ s konkrétnou štruktúrou. Naša definícia pojmu „fáza“ zahŕňa aj takúto „mikrosložku“.)

Vo všeobecnosti sa tepelné a mechanické vlastnosti fázy pri malých zmenách zloženia materiálu výrazne nemenia. Tieto vlastnosti je preto možné aproximovať pomocou údajov z podobných materiálov. Napríklad vlastnosti austenitu, perlitov a martenzitu z materiálu JIS-S45C v knižnici materiálov je možné použiť pre niektoré bežné nízkouhlíkové ocele.

Niektoré vlastnosti, najmä kinetika premeny, sú však veľmi citlivé na zloženie materiálov, a preto ich nie je možné aproximovať pomocou materiálov s podobným zložením. V takomto prípade sa od používateľov očakáva, že si údaje získajú z odbornej literatúry alebo experimentov. Pokiaľ ide o kinetiku premeny, medzi užitočné referenčné publikácie patria

  1. **Atlas časovo-teplotných diagramov pre liatiny a ocele od G. F. Vander Voorta, ASM International, 1991.**

  2. **Atlas časovo-teplotných diagramov pre zliatiny neželezných kovov, autor: G. F. Vander Voort, ASM International, 1991.**

  3. **Príručka ASM: Tepelné spracovanie, ASM International, 1991.**

Okrem toho je možné kinetiku transformácie stanoviť pomocou dilatometrických experimentov v metalurgických laboratóriách, ktoré dokážu zároveň merať latentné teplo a zmenu objemu počas transformácie.

![]({{ '/assets/images/about_deform/1_3_capabilities/1_3_image001.jpg' | relative_url }})

Vzájomný vzťah medzi tromi režimami pri tvárnení kovov

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab5_material_input/image0002.jpg' | relative_url }})

Schéma vzájomných vzťahov medzi rôznymi fázami ocele

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main, ako je znázornené na obrázku 2DHTML5.3.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 2DHTML5.4. Vyberte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek vyberte „**SI**“ pomocou prepínača. Názov úlohy zadajte ako „**STEEL_DATA**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt, pričom predvolený názov problému sa aktualizuje na „**STEEL_DATA**“ ako názov projektu. (Pozri obr. 2DHTML5.5.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab5_material_input/image0005.jpg' | relative_url }})

Okno na výber miesta problému

Používateľ môže tiež zmeniť systém jednotiek (systém jednotiek vybraný v ponuke Súbor sa nastaví ako predvolený); pre toto cvičenie vyberieme systém jednotiek SI a pridáme operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. 2DHTML5.6.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab5_material_input/image0006.jpg' | relative_url }})

Priradenie názvu problému

Otvorí sa sprievodca viacerými operáciami s novým projektom s názvom **STEEL_DATA**. Zoznamu operácií v prehliadači pridajte operáciu 2D Forming. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky 2D Forming alebo ju môžete pridať aj pretiahnutím do editora operácií. (Pozri obr. 2DHTML5.7.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab5_material_input/image0007.jpg' | relative_url }})

Sprievodca MO s operáciou 2D tvarovania

## Nastavenie vlastností materiálu

Otvorte dialógové okno „Materiál“ kliknutím na vetvu so zoznamom materiálov v strome operácií a kliknite na tlačidlo „Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})“. Vyberte kategóriu **Oceľ** a načítajte materiál „**JIS-S45 (tepelné spracovanie)**“. Tento materiál je zmesový materiál s tromi zložkami (fázami): austenit, perlit a martenzit. Zmeňte názov zmesového materiálu z „S45C-Japan“ na „**Nová oceľ**“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab5_material_input/image0008.jpg' | relative_url }})

Načítanie materiálu z knižnice

Preskúmajte a porovnajte plastické vlastnosti perlitov a martenzitov. Všímajte si, že martenzit má pri rovnakej teplote vyššie napätie tečenia ako perlit. Najnižšie napätie tečenia má zase austenit. Rovnaký trend možno pozorovať aj v hodnotách tvrdosti týchto fáz. Preskúmajte tiež jemné rozdiely v elastických, tepelných a difúznych vlastnostiach týchto fáz. Venujte pozornosť aj ich závislosti od obsahu uhlíka.

V tomto laboratórnom cvičení nebudeme meniť materiálové vlastnosti týchto fáz.

****

**Otázka: Čo je to tečivé napätie?** Tečivé napätie je napätie potrebné na postupnú plastickú deformáciu materiálu. Ak dochádza k plastickej deformácii materiálu, efektívne napätie v materiáli sa určuje na základe údajov o tečivom napätí, ktoré závisia od teploty, deformácie a rýchlosti deformácie, pri ktorých sa materiál deformuje. **Otázka: Ako získať vlastnosti fázy?** Vlastnosti každej jednotlivé fázy je možné určiť experimentálne pomocou špeciálnych mikrosond, ktorými sa testuje každá jednotlivá fáza. Tieto vlastnosti môžu byť k dispozícii aj z literatúry alebo ich možno odhadnúť na základe chemického zloženia pomocou vzorcov založených na skúsenostiach alebo počítačových modelov. Jemné rozdiely v plastických, tepelných a difúznych vlastnostiach medzi fázami majú často menší vplyv na výsledky simulácie ako vlastnosti fázovej transformácie. Ak teda vlastnosti jednotlivých fáz nie sú k dispozícii, na všetky fázy sa môžu použiť rovnaké vlastnosti (s výnimkou tvrdosti). V tomto prípade, za predpokladu, že údaje o transformácii sú správne, simulácia môže aj tak zachytiť niektoré podstatné javy.  
---  
  
## Nastavenie vlastností medzi materiálmi

V tejto časti predefinujeme vlastnosti transformácie pre novú oceľ. Predpokladajme, že obr. 2DHTML5.9. predstavuje diagram izotermickej transformácie (IT) pre vašu oceľ, ktorý je k dispozícii v odbornej literatúre alebo v metalurgickom laboratóriu. Informácie z tohto obrázku budeme musieť previesť do vstupných údajov programu DEFORM.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab5_material_input/image0009.jpg' | relative_url }})

Diagram izotermickej transformácie (IT)

  1. Vyberte materiál zmesi „New Steel“. Kliknutím na kartu „Transformácia“ otvoríte dialógové okno „Transformácia“.

  2. V tomto dialógovom okne vyberte transformáciu „Austenit -> Perlit“ a otvorte kartu „Kinetika“. Upozorňujeme, že „Perlit“ tu zodpovedá označeniu „F + C“ v diagramu.

  3. Na karte „Kinetika“ ponechajte ako model „Difúzia (krivky TTT)“ a ako režim údajov TTT „Počiatočné a konečné krivky“.

  4. Nastavte počiatočný objemový podiel a konečný objemový podiel na 0,01, resp. 0,99.

  5. Kliknite na tlačidlo „Data“ vedľa položky „Log(Time) = f(Temp., Stress, Atom)“, čím sa otvorí dialógové okno na definovanie počiatočnej a koncovej krivky.

  6. Zmeňte počet riadkov pre teplotu na 11 a zadajte teploty v rozmedzí 250 – 750 °C s intervalmi po 50 °C.

**Otázka: Čo sú počiatočný a konečný objemový podiel?** Ide o kritériá na určenie začiatku (ľavá krivka) a konca (pravá krivka) transformácie v metalurgických skúškach. Podľa väčšiny konvencií sú to hodnoty 0,01 a 0,99. Niektoré diagramy však používajú hodnoty 0,001 a 0,999. Upozorňujeme, že tieto nastavenia sú dôležité pre výpočet rýchlostí transformácie.  
---  
  
.

  1. Odstráňte závislosť Stress znížením počtu riadkov na jeden. Do jediného riadku zadajte nulu. (Poznámka: ak je v tabuľke Stress len jeden riadok, skutočná hodnota tohto riadku nie je dôležitá. Tu je inicializovaná na nulu len z estetických dôvodov.)

  2. V programe Atom nastavte počet riadkov na jeden a v jedinom riadku nastavte hodnotu na 0,8.

  3. Z obr. 2DHTML5.9. vyberáme nasledujúce dátové body pre krivku začiatku transformácie (krivka 1) a krivku konca transformácie (krivka 2):

**Teplota (°C)** |  **Začiatok záznamu [Čas (s)]** |  **Koniec záznamu (s)]**  
---|---|---  
250  |  1,75 |  3,30  
300 |  1,60 |  2,80  
350 |  1,35 |  2,55  
400 |  1,05 |  2,30  
450 |  0,80 |  2,35  
500 |  0,55 |  2,45  
550 |  0,45 |  2,15  
600 |  0,40 |  1,70  
650 |  0,60 |  1,45  
700 |  1,05 |  2,30  
750 |  3,00 |  4,00  
  
Zadajte tieto údaje do dialógového okna a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}). Mali by sa vám zobraziť krivky, ako je znázornené na obr. 2DHTML5.11. Po dokončení kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab5_material_input/image0010.jpg' | relative_url }})

Dialógové okno s vlastnosťami transformácie

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab5_material_input/image0011.jpg' | relative_url }})

Dialógové okno „Začiatok a koniec krivky transformácie“
