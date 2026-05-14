import random

# Basic deck draw simulation to estimate probability of drawing key cards.

def simulate_draw(deck, target, trials=10000):
    hits = 0
    for _ in range(trials):
        hand = random.sample(deck, min(5, len(deck)))
        if target in hand:
            hits += 1
    return hits / trials

if __name__ == '__main__':
    deck = ['H', 'ORACLE', 'DIFFUSION', 'MEASURE', 'SHIELD', 'PULSE'] * 5
    print('Probability:', simulate_draw(deck, 'ORACLE'))
