import yaml

# Placeholder for deck balance analysis.

def score_deck(deck):
    return sum(card.get('complexity', 0) for card in deck)

if __name__ == '__main__':
    sample_deck = [{'complexity': 2}, {'complexity': 3}, {'complexity': 1}]
    print('Deck score:', score_deck(sample_deck))
