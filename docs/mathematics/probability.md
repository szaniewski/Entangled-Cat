
# Probabilistic Model

## 1. Card Draw — Hypergeometric Distribution

Drawing cards without replacement is modeled by the hypergeometric distribution:

$$P(X=k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$$

### Parameters

| Symbol | Meaning |
|--------|---------|
| **N** | Total number of cards in the deck |
| **K** | Number of desired cards |
| **n** | Number of cards drawn |
| **k** | Number of desired cards drawn |

### Probability of Drawing at Least One Desired Card

$$P(X \geq 1) = 1 - \frac{\binom{N-K}{n}}{\binom{N}{n}}$$

This represents the chance of drawing at least one target gate card in a given draw phase.

---

## 2. Decoherence Model — Failure Probability

Decoherence is modeled as the risk of failure in each turn:

$$P_{\text{failure}}(t) = 1 - (1 - p)^t$$

### Parameters

| Symbol | Meaning |
|--------|---------|
| **p** | Probability of decoherence per turn |
| **t** | Number of turns required to complete the algorithm |

### Probability of Algorithm Success

$$P_{\text{success}}(t) = (1 - p)^t$$

**Key Insight:** Longer algorithms are riskier, so they should yield more points to compensate for the higher failure chance.

---

## Application to Game Balance

- **Short algorithms** (low $t$): High success probability, fewer points
- **Long algorithms** (high $t$): Lower success probability, more points
- This creates strategic tension: aim for quick wins or take on risky high-reward algorithms?