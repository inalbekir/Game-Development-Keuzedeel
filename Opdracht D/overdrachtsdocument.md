# Overdrachtsdocument - Dodge the Bombs

**Projectnaam:** Dodge the Bombs  
**Auteur:** Bekir Inal 
**Repository:** https://github.com/inalbekir/Game-Development-Keuzedeel

---

## Projectoverzicht

Dodge the Blocks is een arcade-achtige game waarbij de speler blokken moet ontwijken en power-ups kan verzamelen. Door het behalen van meerdere levels kan de speler de game winnen. Bij botsing met blokken verliest de speler het spel.

De game is ontwikkeld in Python met gebruik van de Raylibpy game engine.

---

## Technische Informatie

- **Programmeertaal:** Python 3
- **Game engine / bibliotheken:**
  - `raylibpy` (Python binding voor Raylib)
  - Eigen modules voor speler (`player.py`), blokken (`blocks.py`), power-ups (`powerup.py`), achtergrond (`background.py`) en geluiden (`sounds.py`).
- **Resolutie:** 800x600 pixels
- **Target FPS:** 60

### Projectstructuur:
/dodge-the-blocks
│
├── main.py
├── features/
│   ├── player.py
│   ├── blocks.py
│   ├── powerup.py
│   └── sounds.py
├── background.py
├── assets/ (images, sounds)
└── README.md

---

## Hoe verder te ontwikkelen

Een nieuwe ontwikkelaar kan op de volgende manier verder bouwen:

1. **Nieuwe levels & moeilijkheidsgraden**  
   - Extra obstakels en snelheidsaanpassingen kunnen eenvoudig toegevoegd worden in `blocks.py`.
   - Moeilijkheidsschaal aanpassen door `score` thresholds in `main.py` te wijzigen.

2. **Nieuwe power-ups toevoegen**  
   - `powerup.py` uitbreiden met nieuwe effecten zoals tijdelijk onsterfelijk zijn of slow-motion.

3. **UI en visuele verbeteringen**  
   - Intro-menu, high-score lijst of instellingenmenu implementeren.
   - Betere achtergrondmuziek of animaties toevoegen via `background.py` en `sounds.py`.

4. **Bugfixes & optimalisaties**
   - Verbeteren van collision detection en performance optimalisatie bij hogere framerates.

---

## Installatie-instructies

1. Vereiste Python-versie: 3.11 (aanbevolen)
2. Installeren van dependencies:
```bash
pip install raylib-py