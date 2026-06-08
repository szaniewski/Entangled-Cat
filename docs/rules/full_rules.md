This is a draft for the `docs/rules/full_rules.md` file. I’ve used a professional yet accessible "rulebook" tone, typical of modern strategy board games, while maintaining the quantum metaphors used in the project.

---

# 🐈 Entangled Cat: Full Rules of Play

Welcome to **Entangled Cat**, the tabletop game where quantum mechanics meets competitive strategy. Your mission is to build functional quantum algorithms, stabilize your qubits, and trigger a successful measurement before your opponents collapse your system.

---

## 🌌 1. The Core Concept

In *Entangled Cat*, you are a Quantum Engineer. You don't just "play cards"; you assemble **Quantum Circuits**.

* **Gate Cards** are your building blocks ($H, X, CNOT$, etc.).
* **Algorithm Cards** are your blueprints (your win conditions).
* **Special Cards** represent the chaotic nature of the universe—decoherence, noise, and strategic interference.

---

## 🛠 2. Setup

1. **Create One Main Deck:** Shuffle all Gate, Algorithm, and Special cards together into a single combined deck.
2. **Laboratory Screens:** Each player takes a cardboard **Laboratory Screen** and places it with the artwork facing outward.
3. **Draw Pile:** Place the combined deck face down in the center of the table.
4. **Starting Hand:** Each player draws exactly **5 random cards** from the combined deck.
5. **Secret Organization:** As cards are drawn, players keep them hidden behind their screen and organize them into the marked sections:
   * **GATES** — gate cards and active circuit pieces
   * **ALGORITHM** — the current algorithm and assembled gate sequence
   * **DECOHERENCE** — disruption, defense, and reaction cards

---

## 🔄 3. Turn Structure

Each turn consists of three distinct phases:

### A. Draw Phase

* **First Turn:** Draw 5 cards.
* **Subsequent Turns:** Draw 1 card from any deck of your choice (Gate, Algorithm, or Special).

### B. Action Phase

During this phase, you may perform **any number** of the following actions:

1. **Initialize a Qubit:** Play a **Gate Card** into your Register.
2. **Plan an Objective:** Place an **Algorithm Card** face up near your Register.
3. **Interfere:** Play a **Special Card** to disrupt an opponent or protect your own circuit.
4. **Quantum Fluctuation (Card Swap):** Exactly **once per turn**, you may discard exactly 2 cards from your hand or Laboratory to the global **Discard Pile** and immediately draw 2 new cards from the main draw deck. *Immediately after this draw, the main draw deck must be thoroughly reshuffled.* This action helps prevent hand deadlock and introduces unpredictability into your strategy.

### C. Measurement Phase (The "Collapse")

If you have an **Algorithm Card** and the **exact sequence of Gates** required to fulfill it:

1. **Declare "Measurement!":** This halts the game.
2. **Verification:** Arrange your gates in the specific order required by the algorithm.
* *Warning:* If the order is incorrect or a gate is missing, the measurement fails (Lose 5 points).



---

## ⚔️ 4. Player Interaction & The Stack

When a player declares **Measurement**, the system becomes unstable. This is the last chance for opponents to interfere.

1. **The Intervention Window:** Opponents may play **Special Cards** (e.g., *Decoherence* to remove a gate, or *Swap* to change the order).
2. **The Stack:** Cards are played one on top of another.
3. **Resolution:** Resolve the stack from **Top to Bottom** (the last card played is the first to take effect).
* *Example:* If Player A declares Measurement, Player B plays "Decoherence", and Player A plays "Shield", the Shield resolves first, protecting the gate from Decoherence.



---

## 📉 5. Measurement Results

When a Measurement resolves (whether successful or failed), **all cards involved must be immediately sent to the global Discard Pile**—no cards remain with any player. This ensures continuous circulation of the 100-card deck.

* **Success:** If the algorithm sequence remains intact after the Stack resolves:
  * The player **records the points** for the completed algorithm on their score tracker (pen and paper, digital tracker, or custom tokens).
  * The Algorithm Card, all Gate cards in the sequence, and any Special cards used in the battle are **immediately discarded to the global Discard Pile**.
  * **Scoring Bonus:** Disrupting an opponent's algorithm awards +5 points to the player who caused the disruption.

* **Failure:** If the circuit is broken or incomplete:
  * All cards involved (Algorithm and Gates) are **immediately discarded to the global Discard Pile**.
  * The player earns 0 points (or records a -5 penalty if the failure was due to a manual error).
  * Any Special cards used in defensive or attack reactions are also discarded.



---

## 6. Deck Depletion & Discard Pile

To maintain continuous card circulation in the 100-card deck:

* **Main Draw Deck Exhausted:** If the main draw deck runs out of cards before the end of the game:
  * Immediately shuffle the entire global **Discard Pile** to form a new main draw deck.
  * Continue play without interruption.

* **No Cards Available:** If both the draw deck and Discard Pile are empty simultaneously (extremely rare), the current player's draw phase is skipped, but gameplay continues.

---

## 🏆 7. Scoring Table & Tracking

| Algorithm Complexity | Gate Requirement | Point Value |
| --- | --- | --- |
| **Simple** | 2–3 Gates | 10 pts |
| **Medium** | 4–5 Gates | 20 pts |
| **Complex** | 6+ Gates / QFT | 30–40 pts |
| **Disruption** | Successfully breaking an opponent's circuit | +5 pts |
| **Failed Measurement** | Declaring measurement without a valid sequence | -5 pts |

**Score Tracking:** Players do not keep physical cards to represent points. Instead, each player must track their score using an external method such as:
* Pen and paper (scoresheet)
* A digital tracker or app
* Custom tokens or markers on a scoreboard

Points are recorded **instantly upon successful measurement** before cards are sent to the Discard Pile.

---

## 🔚 8. Game End

The game concludes when:

1. The **Gate Deck** is exhausted.
2. A predetermined number of turns is reached.

**The player with the highest total points is crowned the Quantum Master.**

---

## 🧠 9. Key Quantum Terms for Players

* **Decoherence:** In the game, this represents losing a card from your sequence due to environmental noise (or a mean opponent).
* **Superposition ($H$ gate):** The gate that opens up possibilities. Use it to start most complex algorithms.
* **Entanglement ($CNOT$):** Links two qubits. In-game, these are often the hardest sequences to protect but offer the highest rewards.

---

*“God does not play dice with the universe, but you will.”*