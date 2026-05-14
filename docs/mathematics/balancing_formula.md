# Balancing Formula

## Core Formula

Card and algorithm power is evaluated using:

$$\text{Power} = \frac{\text{Complexity} \times \text{RarityModifier}}{\text{Stability}}$$

---

## Variable Definitions

| Variable | Meaning |
|----------|---------|
| **Complexity** | Number and difficulty level of gates in the algorithm |
| **RarityModifier** | Rarity multiplier of required cards (common=1, uncommon=1.2, rare=1.5, etc.) |
| **Stability** | Resistance to interference (higher = more resilient, lower = riskier) |

---

## Interpretation Rules

### Complexity Impact
- **Higher complexity** → Greater power and reward
- Reflects the difficulty of assembling the required gate sequence

### Rarity Impact
- **Higher rarity** → Greater reward
- Rare cards are harder to draw, justifying higher point values

### Stability Impact
- **Higher stability** → **Lower power value** (easier to execute)
- **Lower stability** → **Higher power value** (riskier, deserves more points)
- Reflects the decoherence risk model

---

## Practical Applications

### Example 1: Simple Algorithm
- Complexity: 2 (H, CNOT)
- RarityModifier: 1.0 (common gates)
- Stability: 3 (high resilience)
- **Power = (2 × 1.0) / 3 ≈ 0.67** → Low complexity algorithm

### Example 2: Complex Algorithm
- Complexity: 4 (H, CNOT, CR2, CR3, SWAP)
- RarityModifier: 1.5 (rare controlled gates)
- Stability: 1 (vulnerable)
- **Power = (4 × 1.5) / 1 = 6.0** → High risk, high reward

---

## Game Balance Implications

The formula directly balances:

1. **Execution Cost** — How difficult is it to draw and play the cards?
2. **Risk Factor** — How likely is the algorithm to fail before completion?
3. **Point Profitability** — Is the reward worth the investment?

**Result:** Players face meaningful strategic choices:
- Play safe, simple algorithms for steady points
- Or gamble on complex, rare algorithms for big rewards