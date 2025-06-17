# 🎮 Dodge The Blocks - Game Project

Welkom bij **Dodge The Blocks**, een arcade game ontwikkeld in het kader van het keuzedeel *Basis Programmeren van Games (K0788)*. In deze game draait het om reactiesnelheid, ontwijken en power-ups verzamelen.

---

## 📖 Inhoud

- [Beschrijving](#beschrijving)
- [Gameplay Uitleg](#gameplay-uitleg)
- [Technische Structuur](#technische-structuur)
- [Installatie Instructies](#installatie-instructies)
- [Besturingsinstructies](#besturingsinstructies)
- [Achtergrond - Code Architectuur](#achtergrond---code-architectuur)
- [Testresultaten](#testresultaten)
- [Mogelijke uitbreidingen](#mogelijke-uitbreidingen)
- [Ontwikkelaar](#ontwikkelaar)

---

## 📝 Beschrijving

**Dodge The Blocks** is een 2D game waarin de speler blokken moet ontwijken die van boven naar beneden vallen. Door power-ups te verzamelen, kan de speler tijdelijk sneller bewegen. Naarmate de tijd vordert wordt het spel moeilijker: de blokken vallen sneller en de speler moet alert blijven.

**Doel van het spel:**  
- Overleef zolang mogelijk
- Behaal minimaal 5 punten om te winnen

---

## 🎮 Gameplay Uitleg

- De speler bestuurt een piraat karakter.
- Blokken (bommen) vallen willekeurig vanaf de bovenkant van het scherm.
- Elke 10 seconden krijg je een punt.
- Naarmate de tijd vordert vallen de blokken sneller.
- Er verschijnen power-ups die je tijdelijk sneller laten bewegen.
- Als je geraakt wordt door een blok: Game Over.
- Als je 5 punten haalt: You Win 🎉

---

## 🖥 Technische Structuur

De code is modulair opgebouwd in verschillende Python-bestanden:

| Bestand | Functie |
|---------|---------|
| `main.py` | Hoofdgame loop, coördineert alle modules |
| `player.py` | Speler logica en beweging |
| `blocks.py` | Beheer van vallende blokken |
| `powerup.py` | Power-up logica en timers |
| `background.py` | Achtergrond, startscherm en logo |
| `sounds.py` | Muziek en geluidseffecten |
| `assets/` | Afbeeldingen en geluiden |

---

## ⚙️ Installatie Instructies

### 1️⃣ Vereisten:

- Python 3.10+  
- raylibpy library (Python binding voor Raylib)

### 2️⃣ Installeren van raylibpy

pip install raylibpy

### 3️⃣ Raylib shared library installeren

Raylibpy gebruikt native Raylib C bibliotheken. Op MacOS (bijvoorbeeld M1/M2/M3 chip) heb je de Raylib dynamic library nodig:

#### Voor MacOS met Homebrew:

brew install raylib

### 🎮 Besturingsinstructies

| Actie         | Toets  |
| ------------- | ------ |
| Start spel    | ENTER  |
| Stoppen       | ESC    |
| Bewegen links | ←      |
| Bewegen rechts| →      |

### 🔬 Achtergrond - Code Architectuur

De game is opgebouwd uit modules die elk een eigen taak uitvoeren. Hieronder volgt een korte toelichting op de logica per bestand.

#### main.py

- Initieert het spelvenster en laadt alle assets.
- Roept de gameloop `run_game()` aan.
- Controleert of speler wint of verliest.
- Toont startscherm, win scherm en game-over scherm.

#### player.py

- Beweegt de speler links en rechts op basis van keyboard input.
- Controleert of de speler binnen de schermgrenzen blijft.
- Beheert de boost-functionaliteit na het oppakken van een power-up.
- Houdt bij hoe lang een boost actief blijft.

#### blocks.py

- Spawnt nieuwe blokken met een willekeurige x-positie.
- Laat de blokken vallen en versnelt ze naarmate de tijd vordert.
- Voert botsingscontrole uit tussen speler en blokken.
- Reset alle blokken bij herstart van het spel.

#### powerup.py

- Beheert de spawn-positie en valbeweging van de power-up.
- Controleert of de speler de power-up oppakt.
- Activeert de boost bij het oppakken.

#### background.py

- Tekent de achtergrondafbeelding.
- Tekent het startscherm en het logo.
- Laat de startkeuze aan de gebruiker (ENTER of ESC).

#### sounds.py

- Laadt alle geluidseffecten en muziek.
- Speelt geluiden af op de juiste momenten (explosie, power-up, winnen etc.).
- Beheert achtergrondmuziek.

---

### 📊 Testresultaten

#### Test #1: Eerste gebruikers test met Paul en Alex

**Datum:** 29 april 2025

**Feedback:**

- Moeilijkheidsgraad stijgt te snel.
- Score en level-up tekst slecht zichtbaar.
- Mist extra feedback bij scoreverhoging.

**Aanpassingen:**

- Score-interval verlengd van 3 naar 10 seconden.
- Score en level-up tekst visueel verplaatst naar midden boven.
- Geluidseffect toegevoegd bij scoreverhoging.

#### Test #2: Hertoets na aanpassingen

**Datum:** 29 april 2025

**Feedback:**

- Moeilijkheid nu beter gebalanceerd.
- Score feedback goed zichtbaar en hoorbaar.
- Geen verdere problemen gevonden.

---

### 🚀 Mogelijke uitbreidingen

- High score bijhouden.
- Meer soorten power-ups.
- Meerdere levels met toenemende moeilijkheid.
- Speciale visuele effecten (explosies, particle systems).
- Multiplayer mode.
- Mobiele versie bouwen.

---

### 👨‍💻 Ontwikkelaar

- **Naam:** Bekir
- **Project:** Keuzedeel Basis Programmeren van Games (K0788)
- **Opleiding:** Bit Academy