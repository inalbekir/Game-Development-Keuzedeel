# Logboek - Dodge the Blocks  

**Projectnaam:** Dodge the Bombs  
**Ontwikkelaar:** Bekir  
**Startdatum:** 20 april 2025  
**Technologieën:** Python, RaylibPy  

---

## Milestone #1: Speler beweging geïmplementeerd  
**Datum:** 21 april 2025  
**Beschrijving:**  
Ik ben begonnen met het implementeren van de beweging van de speler. Hiervoor heb ik de pijltjestoetsen (LINKS en RECHTS) gebruikt om de speler horizontaal over het scherm te laten bewegen. Ik heb ervoor gezorgd dat de speler niet buiten de randen van het scherm kan gaan, zodat de game grenzen duidelijk zijn.

**Problemen en oplossingen:**  
- In het begin werd de blok niet goed weergegeven op het scherm. Dit kwam doordat de blok te klein werd geladen. Ik heb dit opgelost door een `player_scale` toe te voegen om de blok te vergroten.  
- Daarnaast bleek de hitbox van de speler niet goed overeen te komen met de zichtbare afbeelding. Dit heb ik opgelost door de hitbox handmatig bij te stellen, zodat deze precies overeenkomt met het zichtbare gebied van de sprite.  

---

## Milestone #2: Basis bommen en Power-Up mechanica  
**Datum:** 22 april 2025  
**Beschrijving:**  
Op deze dag heb ik de basis van de vallende bommen geïmplementeerd. De bommen spawnen willekeurig bovenaan het scherm en vallen in een rechte lijn naar beneden. Daarnaast heb ik ook een Power-Up toegevoegd die de speler tijdelijk een snelheidsboost geeft.

**Problemen en oplossingen:**  
- De bommen vielen in het begin buiten het scherm of overlapten elkaar. Dit kwam doordat de spawnpositie willekeurig werd gekozen zonder rekening te houden met de grootte van de sprite. Dit heb ik opgelost door de spawn-positie te beperken binnen de schermgrenzen.  
- De Power-Up werkte soms niet zoals verwacht, omdat de snelheid van de speler niet werd teruggezet na de boost. Dit heb ik opgelost door een timer toe te voegen die de snelheid na enkele seconden terugzet naar de originele waarde.  

---

## Milestone #3: Collision detection en Game Over scherm  
**Datum:** 23 april 2025  
**Beschrijving:**  
Ik heb collision detection toegevoegd zodat het spel eindigt wanneer de speler geraakt wordt door een bom. Na een collision verschijnt er een "Game Over" scherm om duidelijk te maken dat de speler verloren heeft.

**Problemen en oplossingen:**  
- In het begin werkte de collision niet goed. Soms werd de bom te vroeg of juist te laat gedetecteerd. Dit kwam door een verkeerde berekening van de hitboxes. Dit heb ik opgelost door de hitboxes handmatig bij te stellen en te testen.  
- Het Game Over scherm werd in sommige gevallen niet getoond. Dit bleek te liggen aan de volgorde van tekenen in de render-loop. Na wat aanpassingen in de code verschijnt het scherm nu altijd correct.  

---

## Milestone #4: Score systeem en moeilijkheidsschaal  
**Datum:** 24 april 2025  
**Beschrijving:**  
Ik heb een score systeem toegevoegd dat elke 10 seconden één punt toevoegt aan de score van de speler, zolang deze niet geraakt wordt door een bom. Daarnaast heb ik een moeilijkheidsschaal toegevoegd: hoe langer je speelt, hoe sneller de bommen naar beneden vallen.

**Problemen en oplossingen:**  
- De score liep soms niet synchroon met de tijd. Dit kwam door een fout in de timer-loop, wat ik opgelost heb door de timer direct te koppelen aan de game-loop.  

---

## Milestone #5: Geluidseffecten en explosie animaties  
**Datum:** 25 april 2025  
**Beschrijving:**  
Ik heb geluidseffecten toegevoegd voor verschillende gebeurtenissen: wanneer de speler een Power-Up oppakt, wanneer hij geraakt wordt door een bom, en bij het winnen of verliezen van het spel. Ook heb ik een explosie-animatie toegevoegd die afspeelt wanneer de speler geraakt wordt.

**Problemen en oplossingen:**  
- Bij deze heb ik geen problemen gehad

---

## Backlog  
- High score opslaan zodat het kan worden vergeleken bij de volgende spellen.  
- Berichten weergeven als je de hoogste score haalt.  
- Particle effect verbeteren bij explosies.  
- Meerdere levels toevoegen voor meer uitdaging.  

---

## Testverslag #1: Eerste gebruikers test
**Datum:** 29 april 2025  
**Tester:** Paul en Alex

**Bevindingen:**  
- De moeilijkheidsgraad stijgt erg snel, waardoor het lastig wordt om de game langer te spelen.  
- De score en level-up teksten staan te ver aan de zijkant van het scherm, waardoor ze minder goed zichtbaar zijn.  
- Er mist een extra feedbackmoment (bijvoorbeeld een geluid) wanneer de score omhoog gaat, zodat spelers beter weten dat ze progressie boeken.

**Doorgevoerde aanpassingen:**  
- De tijdsinterval waarin de score verhoogd wordt is aangepast van 3 seconden naar 10 seconden. Hierdoor wordt de game minder snel moeilijk.  
- De score en level-up teksten zijn visueel verplaatst naar het midden bovenaan het scherm zodat ze beter zichtbaar zijn.  
- Er is een geluidseffect toegevoegd dat wordt afgespeeld bij iedere scoreverhoging, zodat de speler extra feedback krijgt.

---

## Testverslag #2: Hertoets na aanpassingen
**Datum:** 29 april 2025  

**Bevindingen:**  
- De moeilijkheidsschaal voelt nu beter gebalanceerd aan.
- De score en level-up notificaties zijn goed zichtbaar en het extra geluid geeft een fijnere game-ervaring.
- Geen verdere problemen gevonden tijdens deze testsessie.

**Doorgevoerde aanpassingen:**  
- Geen verdere aanpassingen meer nodig.

---