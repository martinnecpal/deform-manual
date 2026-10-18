---
lang: sk
title: "Laboratórium lisovania 1"
---

# Laboratórium lisovania 1

V tomto laboratórnom cvičení zameranom na symetriu 3D modelu v štvrtine je na príklade ICFG predvedené nastavenie operácie **vstrekovej lisovacej operácie**.

1.1. Vytvorenie nového problému

1.2. Ako pridať operáciu 3D lisovania

1.3. Definovanie nastavení procesu lisovania

1.4. Definovanie údajov v tabuľke priechodov

1.5. Naloženie materiálu

1.6. Definovanie objektu obrobku

1.7. Definovanie objektu hornej matrice

1.8. Definovanie vzťahov medzi objektmi

1.9 Náhľad kroku lisovania

1.10. Definovanie ovládacích prvkov simulácie

1.11. Kontrola a vytvorenie databázy

1.12. Odoslať na simuláciu

1.13. Následné spracovanie výsledkov

1.14. Nastavenie explicitného nastavenia lisovania

## Vytvorenie nového problému

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DSWL1.1. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek pomocou prepínača „**SI**“. Názov problému zadajte ako „******Swaging_ICFG_Ex**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Vytvorenie novej úlohy

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“, ako je znázornené na obr. 3DSWL1.2. V tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V rozbaľovacom zozname „Názov problému“ zadajte názov problému ako „**Swaging_ICFG_Ex**“, ktorý bude zároveň názvom projektu, ako je znázornené na obr. 3DSWL1.2.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0002.jpg' | relative_url }})

Pridať nový názov projektu a systém jednotiek

## Ako pridať operáciu 3D lisovania

Operáciu lisovania môžete pridať z prehliadača MO kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie **Cogging**, prípadne ju môžete pridať aj pretiahnutím do Editoru operácií, ako je znázornené na obr. 3DSWL1.3.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0003.jpg' | relative_url }})

Pridať operáciu lisovania z prehliadača operácií

## Nastavenie procesu lisovania

Zvoľte prepínač typu procesu „Swaging“ a zadajte hodnotu zdvihu **1,9** mm, ako je znázornené na obr. 3DSWL1.4. Používateľ musí zadať hodnotu zdvihu lisovania tak, aby sa simulácia po každom zovretí zastavila, ak prekročí zdvih primárnej matrice v smere pohybu.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0004.jpg' | relative_url }})

Okno „Proces lisovania“

Keďže ide o operáciu studenej kováčskej výroby, vyberte pre výpočet teploty možnosť **Studená – izotermická**. Zvoľte **4 matrice** a **zrušte zaškrtnutie** políčka **Použiť manipulátory** – tie sa zvyčajne používajú pri operáciách zubovania na pridržanie obrobku.

Pre symetrické nastavenie zaškrtnite políčko **Použiť rotačnú symetriu** – tým sa automaticky nastavia príslušné geometrické primitívy a vygenerujú potrebné okrajové podmienky. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte údaje o kroku lisovania.

## Definovať údaje tabuľky priechodov

Do tabuľky priechodov je možné zadať všetky informácie o priechode, ako napríklad počet záberov, axiálny posun matrice na jeden záber, radiálny posun matrice na jeden záber, smer pohybu matrice, otáčanie obrobku na jeden záber, otáčanie obrobku na jeden priechod a polohovanie matrice. Nový priechod je možné pridať pomocou ikony, podobne je možné pridaný priechod odstrániť pomocou ikony. Pri pridávaní nového priechodu sa informácie o priechode skopírujú z predchádzajúceho priechodu a potrebné informácie je možné upraviť podľa požiadaviek procesu.

Zadajte **počet záberov** ako **2500**, **axiálny posuv na záber** **0,027** mm, **otáčky obrobku na záber** **22,56**, smer pohybu matrice ponechajte ako –X a vyberte****metódu** **polohovania matice na začiatku****** „**3-ofst**“, ako je znázornené na obr. 3DSWL1.5.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste načítali materiál pre obrobok.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0005.jpg' | relative_url }})

Informácie o tabuľke priechodov

## Načítanie materiálu

Načítajte materiál „**Steel****16MnCr5**“ z inštalačnej zložky programu DEFORM v priečinku \3d\LABS\ súbor „**Steel 16MnCr5.key** “ pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (načítať materiál zo súboru). Systém zobrazí dialógové okno so zoznamom materiálov, pričom tento zoznam obsahuje materiály dostupné v súbore kľúčových slov. Keďže v súbore kľúčov je len jeden materiál, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), ako je znázornené na obr. 3DSWL1.6.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0006.jpg' | relative_url }})

Načítať materiál zo súboru

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa otvorí okno „Objekt“, pričom ponechajte predvolené nastavenia, keďže axiálne rozdelenie je určené pre cogging, kde dochádza k veľkej deformácii, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli do okna „Objekt obrobku“.

## Definovanie objektu „obrobok“

Názov objektu **Billet** a predvolený typ objektu **Plastic** ponechajte bez zmien. Nastavte teplotu na **20** °C, ako je znázornené na obr. 3DSWL1.7. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte geometriu polotovaru.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0007.jpg' | relative_url }})

Okno s objektom z polotovaru

### Definovanie geometrie polotovaru

Kliknite na geometrickú voľbu ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), aby ste definovali geometriu pomocou základných tvarov, ako je znázornené na obr. 3DSWL1.8.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0008.jpg' | relative_url }})

Okno Geometria

Zadajte **dĺžku****130** mm, **vnútorný****priemer****24** mm a **vonkajší****priemer****30** mm, aby ste vytvorili symetrickú geometriu, ako je znázornené na obr. 3DSWL1.9. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno Geometrická primitívna.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0009.jpg' | relative_url }})

3D geometria polotovaru

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím otvoríte okno „2D Cross-section“, a prezrite si 2D geometriu extrahovanú z 3D geometrie použitej na vytvorenie mriežky tehál, ako je znázornené na obr. 3DSWL1.10.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0010.jpg' | relative_url }})

2D geometria získaná z polotovaru

### Definícia siete z polotovarov

Zaškrtnite voľbové tlačidlo „Brick Mesh“ a zadajte počet **prvkov** na hodnotu **390**, **Pomer veľkostí** **1** a počet **vrstiev** na **47** a vygenerujte sieť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) v rozbaľovacom okne „Predvolené okrajové podmienky“.

Pre geometriu 2D priečneho rezu, ako je znázornené na obr. 3DSWL1.10, systém vygeneruje **390** sieťových prvkov a otočí ich o 90 stupňov v 47 vrstvách, ako je znázornené na obr. 3DSWL1.11. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku Materiál.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0011.jpg' | relative_url }})

Okienko zo sieťoviny z hliníkového bloku

### Priradiť materiál k sochárskej surovine

Zoznamu materiálov vyberte nahratý materiál „**Oceľ****16MnCr5**“, aby ste ho priradili k obrobku, ako je znázornené na obr. 3DSWL1.12.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0012.jpg' | relative_url }})

Priradiť materiál na výkovky

### Definovanie okrajových podmienok

Všimnite si, že systému bola priradená predvolená rotačná symetria BCC a pevná rýchlosť na voľnom konci polotovaru BCC, ako je znázornené na obr. 3DSWL1.13 a obr. 3DSWL1.14. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die“ (Horná matrica), kde môžete definovať hornú matricu.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0013.jpg' | relative_url }})

Rotačná symetria BCC

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0014.jpg' | relative_url }})

Velocity BCC

## Definovanie objektu „Top die“

Názov objektu ponechajte ako **Top die** a predvolený typ objektu **Rigid** bez zmien a nastavte teplotu na **20** °C, ako je znázornené na obr. 3DSWL1.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0015.jpg' | relative_url }})

Na začiatok stránky objektu

### Definícia geometrie matrice

Načítajte geometriu formy **Swaging_ICFG_Die_SI.stl** z inštalačnej zložky \3d\LABS\, ako je znázornené na obr. 3DSWL1.16.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0016.jpg' | relative_url }})

Import geometrie lisovacej formy

V kontextovom menu „Knižnica používateľa“ sa zobrazí výzva na použitie aktuálnej polohy súboru geometrie ako predvoleného umiestnenia knižnice. Predvolene bude cesta k knižnici geometrie zodpovedať ceste 3D LABS, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). (Pozri obr. 3DSWL1.17.)

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0017.jpg' | relative_url }})

Aktualizácia cesty k užívateľskej knižnici

Pozrite si vnútorný profil importovanej geometrie, na ktorom sú znázornené uhol prívodu na vstupe, kalibračná dĺžka a uhol výstupu, ako je znázornené na obr. 3DSWL1.18.

**Poznámka:** Ak je potrebné umiestniť formu, mal by používateľ na stránke „Tabuľka priechodov“ zvoliť metódu umiestnenia formy „3-offset“. To mu umožní formu umiestniť.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0018.jpg' | relative_url }})

Geometria importovanej formy

### Definícia pohybu matrice

Vyberte typ rádio tlačidla „Pokročilé“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_movement_button.jpg' | relative_url }}), nastavte pohyb matrice na konštantnú **rýchlosť** **200** mm/s a nastavte ****Aktuálny zdvih** na hodnotu **-1,9**, keďže geometria formy je importovaná v uzavretej polohe, ako je znázornené na obr. 3DSWL1.19. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili stránku „Pokročilý pohyb“. 

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0019.jpg' | relative_url }})

Okienko na posun matice

## Definovanie vzťahov medzi objektmi

Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Kontakt“, keďže pri operácii lisovania sa lisovacie formy automaticky umiestňujú okolo obrobku v rovnakých uhloch, takže ručné polohovanie nie je potrebné. Vyberte typ definície kontaktu **Systém**, zaškrtnite políčka Inicializovať a Generovať plánovaný kontakt a zadajte malú hodnotu **tolerancie** kontaktu **0,0001**, ako je znázornené na obr. 3DSWL1.20. Systém automaticky vygeneruje kontakt počas generovania databázy. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka Náhľad simulácie. 

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0020.jpg' | relative_url }})

Typ systému: Nastavenia medzi objektmi

## Náhľad kroku lisovania

Pozorujte pohyb a polohovanie formy a obrobku v náhľade a vyskúšajte si rôzne možnosti ovládania krokov. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na ovládacie prvky simulácie.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0021.jpg' | relative_url }})

Okno náhľadu lisovania

## Definovanie ovládacích prvkov simulácie

Zadajte **počet krokov** na hodnotu **10 000**, **krok pre ukladanie** na hodnotu **1 000** a **0,0015** mm zdvihu na krok, ako je znázornené na obr. 3DSWL1.22. Okrem toho je definovaná hodnota koeficientu trenia **0,4**, ktorá sa použije pri výpočte kontaktného trenia. Na riešenie tohto nastavenia sa používa implicitný riešiteľ. Nechajte predvolené nastavenia implicitného riešiteľa. Ak chcete získať viac informácií o RSE a implicitnom kontakte, pozrite si príslušné časti. 

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0022.jpg' | relative_url }})

Okno riadenia simulácie

## Kontrola a vytvorenie databázy

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a sledujte kartu správ, kde sa zobrazujú správy o kontrole databázy; ak sa vyskytnú nejaké chyby vo vstupe, budú označené červenou farbou a zároveň sa zobrazia varovné správy. Chybová správa zabráni používateľovi vygenerovať databázu. Potvrďte, že kontrola databázy prebehla v poriadku, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}). (Pozri obr. 3DSWL1.23.) Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0023.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Odoslať na simuláciu

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DSWL1.24. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0024.jpg' | relative_url }})

Odoslať na simuláciu

Pomocou ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) môže používateľ využiť viac procesorov a spustiť simuláciu v 64-bitovom režime. Po spustení simulácie sa v grafickom okne simulácie aktualizujú simulované uložené kroky a stav aktuálnej simulácie sa zobrazuje aj v súboroch správ a protokolov, ako je znázornené na obr. 3DSWL1.25.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0025.jpg' | relative_url }})

Monitorovanie pomocou simulačnej grafiky

Dokončenie alebo prerušenie simulácie bude zaznamenané v súbore správ. Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste vykonali následné spracovanie databázy.

## Následná spracovanie výsledkov

Prejdite jednotlivými krokmi a pozrite si rozloženie deformácie pomocou grafického znázornenia premennej efektívneho stavu deformácie. (Pozri obr. 3DSWL1.26.)

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0026.jpg' | relative_url }})

Rozloženie napätia

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0027.jpg' | relative_url }})

Hrúbka prierezu obrobku

## Nastavenie explicitného nastavenia lisovania

V riešiteľovi Explicit nastavte obrobok ako **elastoplastický** objekt tak, že sa vrátite do okna objektu „Billet“, ako je znázornené na obr. 3DSWL1.28.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0028.jpg' | relative_url }})

Objekt z polotovaru vybraný ako elastoplastický objekt

Po vytvorení polotovaru ako elastoplastu prejdite na stránku materiálu obrobku, kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) a na karte **Thermal** nastavte **hmotnosť****hustotu** na hodnotu **7,85e-09**, ako je znázornené na obr. 3DSWL1.29. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku na úpravu materiálu.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0029.jpg' | relative_url }})

Definovanie údajov o hmotnostnej hustote

Prejdite do okna **Ovládacie prvky simulácie** a vyberte prepínač metódy **Explicitný riešiteľ**, ako je znázornené na obr. 3DSWL1.30. Zadajte **koeficient tlmenia** ako **0,5**, **škálovanie hmotnosti** ako **30** a **kontaktnú frekvenciu** ako **1**.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0030.jpg' | relative_url }})

Ovládacie prvky simulácie pre metódu explicitného riešiteľa

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do okna na vytvorenie databázy, kde skontrolujte a vygenerujte databázu, ktorú v nasledujúcich krokoch odošlete na simuláciu. Podobne ako v častiach 1.12 a 1.13 odošlite vygenerovanú databázu na simuláciu a následné spracovanie pomocou príkazu MO post.

Zobrazenie efektívneho napätia v poslednom kroku pre simulovanú databázu (pozri obr. 3DSWL1.30 a obr. 3DSWL1.31)

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0031.jpg' | relative_url }})

Graf efektívneho napätia

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0032.jpg' | relative_url }})

Prerez obrobku

**Súvisiace témy:**

[Swaging Setup]({{ '/docs/sk/operation_templates/29_cogging/29_2_swaging_setup/' | relative_url }})
