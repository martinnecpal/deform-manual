---
lang: sk
title: "40. Úvod do deformácií pri obrábaní"
---

# 40\. Úvod do deformácií pri obrábaní

Operácia „Deformácia pri obrábaní“ umožňuje nastaviť údaje modelu a simulovať obrábací priechod na súčiastke s históriou deformácií a zvyškových napätí. Funkcia „Deformácia pri obrábaní“ modeluje a simuluje obrábací proces s upínacími prípravkami a elastickým spätným odskokom po ich odstránení.

Operácie „Deformácia pri obrábaní“ slúžia na prípravu údajov potrebných pre simuláciu. Na použitie tejto operácie potrebuje používateľ výsledok zo simulačného modelu DEFORM, ktorý zahŕňa zvyškové napätie v diele. Typické modely zahŕňajú model procesu elastoplastického deformovania alebo model procesu tepelného spracovania. Okrem týchto vstupných údajov vyžaduje model procesu deformácie pri obrábaní podrobnosti o upínacích prípravkoch, ich umiestnení a podrobnosti o obrábacom cykle.

Postup operácií, podľa ktorého budeme modelovať, je nasledovný:

  1. Vyrobte diel na stroji.

  2. Nechajte diel sa vrátiť do pôvodného tvaru a zároveň ho zafixujte pomocou nástrojov.

  3. Nechajte diel voľne vyskočiť z upínacích prostriedkov.

Všetky tieto operácie je možné vykonať v rámci operácie „Deformácia pri obrábaní“. Z týchto fáz

V šablóne sú definované iba údaje týkajúce sa obrábania, zatiaľ čo systémové postupy automaticky vypočítajú následnú fázu spätného pruženia po odstránení upínacích prípravkov. Postprocesor umožní používateľovi zobraziť výsledky (napäťový stav a spätný posun/deformácie) po obrábaní a odstránení upínacích prípravkov. Tento proces je možné zopakovať pre nasledujúce prechody, ktoré môžu zahŕňať aj otočenie objektu a prepositionovanie upínacích prípravkov pred obrábaním.

**Súvisiace témy:**

[40.1. 2D Machining Distortion](/docs/en/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/)

[40.2. 3D Machining Distortion](/docs/en/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/)
