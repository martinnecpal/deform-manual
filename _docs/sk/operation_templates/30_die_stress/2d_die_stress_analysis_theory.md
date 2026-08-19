---
lang: sk
title: "Teória analýzy napätí v 2D čipe"
---

# Teória analýzy napätí v 2D výtvore

1\. Prehľad

2\. Druhy analýz

3\. Praktické hľadiská

4\. Druhy porúch lisovacích foriem

5\. Požadované údaje

6\. Nastavenie Die Stress

7\. Definícia lisovaného spojenia

8\. Stručný prehľad okrajovej podmienky s tepelne zmrštiteľným spojom

9\. Dôležité merania napätia

10\. Výklad pojmu „stres“

## Prehľad

Táto časť príručky sa zaoberá teoretickými aspektmi vykonávania analýzy napätia v lisovacej forme. Analýza napätia v lisovacej forme je výpočtová metóda na stanovenie veľkosti a rozloženia napätia v nástroji počas simulácie kovania (alebo akéhokoľvek iného procesu spojeného s deformáciou). Účelom analýzy napätia v nástroji je pomôcť určiť hlavnú príčinu poruchy nástroja alebo identifikovať pravdepodobné miesta poruchy nástroja v danej konštrukcii výkovku. To si vyžaduje značné technické znalosti o napätí a o fungovaní zostavy. Pochopenie napätia pomôže používateľovi pri správnej interpretácii výsledkov. Inžinierske posúdenie je dôležité pri rozhodovaní o tom, ako zorganizovať zmysluplnú simuláciu reakcie nástroja a interpretáciu výsledkov. Niektoré kľúčové hľadiská pri nastavovaní analýz napätia v lisovacej forme sú:

Nástroje nefungujú izolovane. Objekty nástrojov musia pôsobiť na ostatné objekty, aby sa mohli deformovať v dôsledku tvárniacich napätí. Veľmi dôležitou otázkou pri simulácii je, ako definovať okrajové podmienky pre príslušné nástroje.

Je dôležité zohľadniť nielen správanie samotnej tvárnej matrice alebo vložky, ale aj nosnej konštrukcie tohto nástroja. V prípadoch, keď s nástrojom priamo interagujú iné nástroje, najmä ak na nástroj pôsobí pred zaťažením určité predpätie, je na získanie správneho napäťového stavu potrebná dôkladná analýza tohto predpätia.

Existuje niekoľko rôznych prístupov, ktoré možno použiť pri simulácii, ako aj mnoho rôznych kritérií slúžiacich na interpretáciu výsledkov. V tomto dokumente vysvetlíme rôzne metódy analýzy napätia v lisovacej forme a objasníme, ktoré metódy interpretácie sú najvhodnejšie pre konkrétne prípady. Na obr. 1 je zobrazený príklad výsledku analýzy napätia v lisovacej forme, pri ktorej sa zohľadnili tri objekty. Výstupom simulácie je napätie v každom telese, ktoré poskytuje informácie o potenciálnych poruchách.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0001.jpg' | relative_url }})

Analýza napätí znázorňujúca napätia vo vložke, puzdre a opornej doske

## Druhy analýz

Existujú dva všeobecné typy analýzy (prvý z nich sa odporúča pre väčšinu analýz):

  1. **Oddelená analýza (jeden krok)**: Pri tejto analýze sa najskôr vykoná simulácia deformácie s deformovateľným obrobkom a tuhými formami (pozri obr. 2). Po vykonaní tohto prvého kroku sa vytvorí nová úloha a načíta sa príslušný krok zo simulácie tvárnenia. Sily pôsobiace z deformovateľného telesa sa následne interpolujú na pružnú formu. Potom sa vykoná jeden krok analýzy na výpočet napätí v pružnej forme. Výhodou tohto typu analýzy je, že je veľmi jednoduchá na nastavenie a rýchla na spustenie, ako aj možnosť experimentovať s tvarom opory a/alebo vložky bez zmeny tvaru dutiny. Nevýhodou je, že sa analyzuje len jeden časový okamih na jednu analýzu a pri deformácii obrobku sa nezohľadňuje poddajnosť nástrojov.

**Poznámka:** Táto analýza predstavuje primeranú aproximáciu, pokiaľ je deformácia nástroja zanedbateľná. Vo väčšine, hoci nie vo všetkých procesoch tvárnenia, ide o správny predpoklad.

  1. **Spriahnutá analýza (jedna alebo viac deformujúcich sa matíc počas deformácie obrobku):** V tejto simulácii je sledovaný nástroj nastavený ako pružný a je mu priradená sieť (pozri obr. 3). Celá simulácia deformácie prebieha s týmto lisovacím nástrojom ako pružným a napätia v nástroji sú k dispozícii pre každý uložený krok. Existujú dve nevýhody pri vykonávaní tohto typu simulácie.

Doba behu je podstatne dlhšia ako v prípade jedného deformujúceho sa telesa.

Náročnosť formulácie problému sa podstatne zvyšuje.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0002.jpg' | relative_url }})

Náčrt analýzy napätia v neodspájanom čipe

Obrázok vľavo ukazuje, že sa najskôr vykoná analýza deformácie, a obrázok vpravo ukazuje, že sily sa interpolujú na pružnú maticu s cieľom vypočítať napätia v matici.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0003.jpg' | relative_url }})

Náčrt analýzy vzájomného pôsobenia deformovateľnej matrice a obrobku

##  Praktické hľadiská

Okrem toho sa pri tejto analýze môžu zvážiť nasledujúce možnosti:

  1. Tepelnú analýzu možno považovať buď za spriahnutú analýzu, alebo za jednokrokovú analýzu.

  * V prípade spriahnutej analýzy môže byť dôležité zohľadniť túto skutočnosť pri simuláciách tvárnenia za tepla a za vysokých teplôt, keďže pri týchto teplotách sa môžu výrazne meniť elastické vlastnosti materiálu nástroja. 

  * V prípade jednokrokového výpočtu je možné v prípade potreby zohľadniť teplotnú rozťažnosť. Pri riešení deformácie by mal príslušný tuhý lisovací nástroj mať teplotný profil zodpovedajúci bežnej praxi.

  1. Interakciu medzi formovacím zariadením a materiálom je možné zahrnúť buď do analýzy so vzájomným pôsobením, alebo do jednokrokové analýzy. 

  2. Viacero deformujúcich sa telies, vrátane viacerých tesných spojov, je možné presne simulovať ako diskrétne objekty. V prípade, že na príslušný nástroj pôsobí tesný spoj, je potrebné tento efekt zohľadniť, aby bolo možné vypočítať správne napätia pôsobiace na nástroje.

  3. Kováčska sila. Na získanie správnych hodnôt napätia v lisovacej forme je potrebná správna formovacia sila. Aby bolo možné presne odhadnúť kováčsku silu, je potrebné, aby bolo presne stanovených niekoľko premenných. Medzi ne patria:

  * Údaje o napätí v prúde materiálu

  * História obrobku (napr. správna teplota, správne rozloženie deformácie)

  * Napĺňanie formy (pri kovaní v uzavretej forme sa zaťaženie výrazne zvyšuje v miere, ako sa vyplňujú rohy)

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0004.jpg' | relative_url }})

Porucha matrice v polovici zdvihu na základe krivky napätia a zdvihu

## Spôsoby poruchy matrice

Medzi rôzne spôsoby poruchy matrice patria:

  1. **Katastrofické zlyhanie v dôsledku krehkého lomu** \- Tomu sa zvyčajne dá predísť pomocou jednoduchého výpočtu pomeru sily k ploche.

  2. **Plastická deformácia** – Túto je možné určiť porovnaním výsledkov analýzy napätí v lisovacej forme s medzou kĺzavosti materiálu formy.

  3. **Porucha spôsobená únavou pri nízkom počte cyklov (LCF)****v dôsledku cyklického, tepelného a mechanického zaťaženia** – K tomu dochádza, keď sú napätia nižšie ako medza tečnosti materiálu matrice, avšak po mnohých cykloch ťahového zaťaženia vedú k poruche matrice. Týmto javom je možné predísť znížením alebo odstránením ťahových napätí.

  4. **Opotrebenie** – Najčastejší spôsob poruchy lisovacích foriem. Odhad tohto javu presahuje rámec analýzy napätí v lisovacích formách. (Ďalšie informácie k tejto téme nájdete v dokumente [20.4. Inter-object Data Tool wear section](/docs/en/pre_processor/20_inter-object_data_definition/20_4_tool_wear/).)

## Požadované údaje

Údaje potrebné na vykonanie analýzy napätia v lisovacej forme sú:

  1. Geometria formy.

  2. Podmienky upevnenia a montáže formy.

  3. Sily pôsobiace na povrch formy zo strany obrobku.

**Poznámka** :

Na to je potrebné v simulácii deformácie zohľadniť presné zaťaženie, aby bolo možné presne predpovedať napätie a priehyb.

  1. Rozloženie teploty v lisovacích formách (pre neizotermickú analýzu).

  2. Vlastnosti materiálu formy (prípadne aj tepelné vlastnosti).

  3. Tepelné zúženie.

  4. Akékoľvek zvyškové napätie alebo iné predpätia.

## Nastavenie Die Stress

  1. Spustiť analýzu toku.

  2. Určte kľúčové kroky pri simulácii toku.

  * Koniec zdvihu.

  * Ďalší krok, pri ktorom môžu byť nástroje vystavené nerovnomernému zaťaženiu.

  1. Vytvorte nový problém pre analýzu napätia v liatej súčiastke.

  2. Načítajte kritické napätie z databázy deformácií.

  3. Nástroje na podporu importu.

  4. Nastavte okrajové podmienky rýchlosti na obmedzenie nástrojov.

  5. Interpolovať sily zo simulácie prúdenia z obrobku na povrchy nástroja.

  6. Určte lisované spoje medzi nástrojmi a puzdrami.

  7. Priraďte vzťahy typu „master-slave“ medzi nástrojmi.

  8. Vytvorte databázu a spustite simuláciu.

## Definícia lisovaného uloženia

Tlakové uloženie je situácia, keď sa dva nástroje spájajú s vyrovnávacími rozmermi, ktoré sa mierne prekrývajú. Pri spojení týchto dvoch nástrojov vzniká medzi nimi značné napätie ešte pred pôsobením akéhokoľvek kováčskeho zaťaženia. Účelom tohto postupu je udržať tlakové obvodové predpätie, ktoré by regulovalo ťahové napätia v obvodovom smere. To je veľmi dôležité v prípade karbidových nástrojov, pri ktorých sa v prítomnosti ťahových napätí výrazne skracuje životnosť nástroja.

Tlakové lisovanie možno modelovať pomocou dvoch pružných foriem. Pružný objekt možno zjednodušene považovať za pružinu (pozri obr. 5). Keď sa oba objekty stlačia k sebe, konečný stav napätia určí najmenšie množstvo energie potrebné na deformáciu oboch objektov. Každá matrica by mala byť navrhnutá tak, aby presne zodpovedala druhej matrici (t. j. bez prekrývania). Následne by sa lisované spojenie malo aplikovať ako okrajová podmienka „zúženého spojenia“ na jednu z matríc. Prerez kombinácie vložky a puzdra je znázornený na obr. 6a, kde je tepelné zúženie aplikované na vnútorný polomer puzdra. Po spustení simulácie bude puzdro pôsobiť silou na vložku. Oba tieto telesa sa ohnú s cieľom minimalizovať celkovú energiu deformácie uloženú v oboch objektoch (pozri obr. 6b). Podobne je možné postupovať aj v prípade, ak je lisované spojenie aplikované na vložku. Na vložku môže byť aplikované lisované spojenie na vonkajší polomer (pozri obr. 7a). Po spustení simulácie sa obe telesa deformujú s cieľom minimalizovať celkovú energiu deformácie uloženú v týchto dvoch objektoch (pozri obr. 7b). Pre presnú analýzu napätia v matrici je veľmi dôležité zohľadniť lisované uloženie, keďže lisované uloženie má často veľmi významný vplyv na celkový stav napätia v zostave. Je vhodné to skontrolovať bez interpolovaných síl, aby sa ďalej uistilo, že veľkosť použitého lisovaného uloženia neprekračuje limity pre bezpečnú prevádzku kováčskeho procesu.

## Stručný prehľad okrajovej podmienky s tepelne zmrštiteľným spojom

Ako stručný prehľad postupu pri aplikácii okrajových podmienok s tepelne zmrštiteľným spojom vykonajte nasledujúce kroky v uvedenom poradí:

Spojte povrchy nástrojov a umiestnite ich tak, aby sa dotýkajúce sa povrchy dokonale zhodovali.

Priraďte okrajovú podmienku s tlakovým uložením buď vložke, alebo puzdru. Hodnota presahu by mala predstavovať polovicu rozdielu priemerov.

Vytvorte kontakt medzi dvoma objektmi, ktoré sa dotýkajú. Ak sa kontakt pri predvolenej tolerancii kontaktu nevytvorí, mierne zvýšte toleranciu kontaktu, aby sa kontakt vytvoril.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0005.jpg' | relative_url }})

Predpokladajme, že vložka a puzdro tvoria 2 pružiny

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0006.jpg' | relative_url }})

(a) Priraďte kladný posun vnútornej časti skrine (b) Po spustení simulácie sa systém dostane do rovnováhy

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0007.jpg' | relative_url }})

(a) Zadajte kladný posun na vonkajšej strane vložky. (b) Po spustení simulácie sa systém ustáli v rovnovážnom stave.

## Dôležité merania napätia

Napätie je dôležitý pojem v strojárstve. Všeobecný prehľad nájdete v časti venovanej základným pojmom v príručke. 

  1. **Efektívne napätie (Von Mises)** – uznávaná veličina vyjadrujúca počiatočné tečenie, keď toto napätie prekročí medzu tečenia materiálu matrice (pri danej teplote).

  2. **Maximálne hlavné napätie** – v prípade karbidu budú ťahové napätia s určitosťou viesť k predčasnému zlyhaniu v dôsledku únavy pri nízkych cykloch (LCF) – v prípade kalených lisovacích ocelí to zvyšuje náchylnosť k zlyhaniam v dôsledku únavy pri nízkych cykloch (LCF). Táto veličina predstavuje maximálne možné napätie v jednom bode v danej orientácii (pozri obr. 8.).

  3. **Stresové komponenty** – pri riešení problémov s čipmi sú tieto komponenty veľmi užitočné pri určovaní základných príčin a skúmaní alternatívnych riešení.

  4. **Priemerné napätie** – tento stav napätia nemá vo všeobecnosti kritický význam pri analýze napätia v lisovacej forme.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0008.jpg' | relative_url }})

Popis hlavného napätia

## Výklad pojmu „stres“

**Oceľ** :

V prípade ocele, ak efektívne napätie pri prevádzkovej teplote prekročí medzu tečnosti, dôjde k tečnému deformovaniu nástroja. Stredná až nízka medza tečnosti môže mať veľmi nepriaznivý vplyv na proces kovania, pretože sa vyrobí iný diel, ako bol zamýšľaný, a nástroje nakoniec úplne zlyhajú. Vysoké hodnoty kladného hlavného napätia môžu viesť k únavovým poruchám, aj keď je napätie nižšie ako medza tečnosti.

Tvrdšie nástrojové ocele majú spravidla vyššiu medzu tečnosti (pozri obr. 9), ale nižšiu odolnosť voči únavovému namáhaniu v ťahu. Nástrojové ocele s nižšou tvrdosťou majú nižšiu medzu tečnosti, ale lepšiu odolnosť voči únavovému namáhaniu v ťahu.

**Karbid:**

Karbid dokáže znášať mimoriadne vysoké efektívne napätie, je však mimoriadne citlivý na ťahové (kladné) hlavné napätia a ľahko podlieha únavovému poškodeniu. Vyšší obsah kobaltu zvyšuje odolnosť proti únave, znižuje však odolnosť proti opotrebeniu. Nižší obsah kobaltu má lepšie vlastnosti z hľadiska opotrebenia, je však menej odolný voči veľkým kladným hlavným napätiam.

**Zjednodušené pravidlá:**

Pri interpretácii výsledkov analýzy napätia v tvárnici sa často môžu hodiť niektoré veľmi jednoduché pravidlá. Tu je krátky zoznam vecí, na ktoré by ste mali pamätať.

  1. Efektívne napätie v oceli by malo byť nižšie ako medza tečnosti. Je to síce celkom zrejmé, ale poskytuje to dobrý východiskový bod pre posúdenie situácie, keď dochádza k poruchám lisovacích foriem, alebo pre posúdenie plánovanej montáže.

  2. Maximálne hlavné napätie v karbide by malo byť záporné alebo malo by mať malé kladné hodnoty (10–20 ksi alebo 50–100 MPa). Keďže karbid je vyrobený z lisovaného keramického materiálu, zrná majú tendenciu sa pomerne ľahko od seba oddeľovať, avšak množstvo napätia, ktoré tieto materiály dokážu zvládnuť pri tlakovom namáhaní, je skutočne ohromujúce. Preto je vhodné navrhnúť zostavu tak, aby karbid počas celého procesu kovania nebol nikdy vystavený ťahovému napätiu.

  3. Maximálne hlavné napätie v oceliach môže byť vyššie, avšak veľmi vysoké hodnoty (100 ksi alebo 700 MPa) môžu viesť k únavovým poruchám. Jedným z prvých zákonov únavy je, že čím sa cyklická prevádzka približuje k medze tečnosti, tým nižší je počet cyklov, ktoré proces vydrží pred konečným zlyhaním. Aj keď je proces pod medzou tečnosti o nominálnu rezervu, často je možné dosiahnuť predĺženie životnosti ďalším znížením maximálneho efektívneho napätia pôsobiaceho na nástroje.

  4. Ak dochádza k vysokému namáhaniu, zložky namáhania možno využiť na identifikáciu základnej príčiny tohto namáhania. Pri snahe o prepojenie poruchy vo výrobnej hale so simuláciou namáhania formy sa zložky, v ktorých sa vyskytujú vysoké namáhania, často dajú prepojiť so spôsobom, akým došlo k poruche formy.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0009.jpg' | relative_url }})

Porovnanie idealizovaných kriviek napätia a deformácie s krivkami tvárnych a krehkých materiálov

**Súvisiace témy:**

[Object Boundary Condition](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[2D Die Stress Study with Multiple Steps](/docs/en/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/)

[2D Die Stress Study with Single steps](/docs/en/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/)
