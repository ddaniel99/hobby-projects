
# short deck 60 cards
uno_deck = ["0 Red", "1 Red", "2 Red", "3 Red", "4 Red", "5 Red", "6 Red", "7 Red", "8 Red", "9 Red", "Skip Red", "Reverse Red", "Draw Two Red", "Wild", "Wild Draw Four", "0 Blue", "1 Blue", "2 Blue", "3 Blue", "4 Blue", "5 Blue", "6 Blue", "7 Blue", "8 Blue", "9 Blue", "Skip Blue", "Reverse Blue", "Draw Two Blue", "Wild", "Wild Draw Four", "0 Green", "1 Green", "2 Green", "3 Green", "4 Green", "5 Green", "6 Green", "7 Green", "8 Green", "9 Green", "Skip Green", "Reverse Green", "Draw Two Green", "Wild", "Wild Draw Four", "0 Yellow", "1 Yellow", "2 Yellow", "3 Yellow", "4 Yellow", "5 Yellow", "6 Yellow", "7 Yellow", "8 Yellow", "9 Yellow", "Skip Yellow", "Reverse Yellow", "Draw Two Yellow", "Wild", "Wild Draw Four"]

# full deck 108 cards
uno_deck = ["0 Red", "1 Red", "2 Red", "3 Red", "4 Red", "5 Red", "6 Red", "7 Red", "8 Red", "9 Red", "Skip Red", "Reverse Red", "Draw Two Red", "Wild", "Wild Draw Four", "0 Blue", "1 Blue", "2 Blue", "3 Blue", "4 Blue", "5 Blue", "6 Blue", "7 Blue", "8 Blue", "9 Blue", "Skip Blue", "Reverse Blue", "Draw Two Blue", "Wild", "Wild Draw Four", "0 Green", "1 Green", "2 Green", "3 Green", "4 Green", "5 Green", "6 Green", "7 Green", "8 Green", "9 Green", "Skip Green", "Reverse Green", "Draw Two Green", "Wild", "Wild Draw Four", "0 Yellow", "1 Yellow", "2 Yellow", "3 Yellow", "4 Yellow", "5 Yellow", "6 Yellow", "7 Yellow", "8 Yellow", "9 Yellow", "Skip Yellow", "Reverse Yellow", "Draw Two Yellow", "Wild", "Wild Draw Four", "1 Red", "2 Red", "3 Red", "4 Red", "5 Red", "6 Red", "7 Red", "8 Red", "9 Red", "Skip Red", "Reverse Red", "Draw Two Red", "1 Blue", "2 Blue", "3 Blue", "4 Blue", "5 Blue", "6 Blue", "7 Blue", "8 Blue", "9 Blue", "Skip Blue", "Reverse Blue", "Draw Two Blue", "1 Green", "2 Green", "3 Green", "4 Green", "5 Green", "6 Green", "7 Green", "8 Green", "9 Green", "Skip Green", "Reverse Green", "Draw Two Green", "1 Yellow", "2 Yellow", "3 Yellow", "4 Yellow", "5 Yellow", "6 Yellow", "7 Yellow", "8 Yellow", "9 Yellow", "Skip Yellow", "Reverse Yellow", "Draw Two Yellow"]

# imitates an overhand shuffle with the "shuffle_drop" average amount of cards dropped from the shuffling hand stack into the shuffled stack. "shuffle_dev"
# is the absolute value of the random deviations from shuffle_drop. "uno_deck" is the input deck to be shuffled.
# "total_shuffles" is the number of times the shuffle is repeated, 1 by default.
# splitting a full deck would be shuffle(54,0,uno_deck)
def shuffle(shuffle_drop, shuffle_dev, uno_deck, total_shuffles=1):
    import random
    shuffled_deck = []
    totshuffle = 0

    for _ in range(total_shuffles):
        deckshuffle = 0
        totshuffle += 1
        deck_remainder = len(uno_deck)
        deck = []

        while deck_remainder > 0:
            shuffle_hand = shuffle_drop + random.randint(-shuffle_dev, shuffle_dev)

            if shuffle_hand >= deck_remainder:
                shuffle_hand = deck_remainder
                deck.insert(0, uno_deck[0:shuffle_hand])
                del uno_deck[0:shuffle_hand]
                deck_remainder -= shuffle_hand

            elif shuffle_hand < deck_remainder:
                deck.insert(0, uno_deck[0:shuffle_hand])
                del uno_deck[0:shuffle_hand]
                deck_remainder -= shuffle_hand
            print("Shuffle hand: ", shuffle_hand, "Deck remainder: ", deck_remainder, "Deck: ", deck)
            deckshuffle += 1

        for lists in deck:
            for items in lists:
                shuffled_deck.append(items)

        uno_deck = shuffled_deck
    print("Shuffled Deck: ", shuffled_deck)
    print("Total shuffles ", totshuffle)
    print("Total shuffles per deck: ", deckshuffle)
    print("Deck remainder: ", deck_remainder)
    print("Len uno_deck: ", len(uno_deck))
    print("Len shuffled_deck:", len(shuffled_deck))
    return uno_deck

# a full deck (2 sets of 56 and 52 cards) will have a full colour score of 92 for 12 plus 13 consecutive colours,
# omitting the universal colour cards.
def colour_score(uno_deck):
    r_score = 0
    g_score = 0
    b_score = 0
    y_score = 0
    for i in range(1, len(uno_deck)):
        if "Red" in uno_deck[i] and "Red" in uno_deck[i - 1]:
            r_score += 1
        elif "Blue" in uno_deck[i] and "Blue" in uno_deck[i - 1]:
            b_score += 1
        elif "Green" in uno_deck[i] and "Green" in uno_deck[i - 1]:
            g_score += 1
        elif "Yellow" in uno_deck[i] and "Yellow" in uno_deck[i - 1]:
            y_score += 1
    colour_score = sum([r_score, g_score, b_score, y_score])
    print(colour_score, " / 92")
    return colour_score

# the distance between the shuffled deck and the original deck is calculated using Shannon entropy
def shannon_entropy(shuffled_deck):
    import numpy as np
    position_dict = {}
    uno_deck = ["0 Red", "1 Red", "2 Red", "3 Red", "4 Red", "5 Red", "6 Red", "7 Red", "8 Red", "9 Red", "Skip Red",
                "Reverse Red", "Draw Two Red", "Wild", "Wild Draw Four", "0 Blue", "1 Blue", "2 Blue", "3 Blue",
                "4 Blue", "5 Blue", "6 Blue", "7 Blue", "8 Blue", "9 Blue", "Skip Blue", "Reverse Blue",
                "Draw Two Blue", "Wild", "Wild Draw Four", "0 Green", "1 Green", "2 Green", "3 Green", "4 Green",
                "5 Green", "6 Green", "7 Green", "8 Green", "9 Green", "Skip Green", "Reverse Green", "Draw Two Green",
                "Wild", "Wild Draw Four", "0 Yellow", "1 Yellow", "2 Yellow", "3 Yellow", "4 Yellow", "5 Yellow",
                "6 Yellow", "7 Yellow", "8 Yellow", "9 Yellow", "Skip Yellow", "Reverse Yellow", "Draw Two Yellow",
                "Wild", "Wild Draw Four", "1 Red", "2 Red", "3 Red", "4 Red", "5 Red", "6 Red", "7 Red", "8 Red",
                "9 Red", "Skip Red", "Reverse Red", "Draw Two Red", "1 Blue", "2 Blue", "3 Blue", "4 Blue", "5 Blue",
                "6 Blue", "7 Blue", "8 Blue", "9 Blue", "Skip Blue", "Reverse Blue", "Draw Two Blue", "1 Green",
                "2 Green", "3 Green", "4 Green", "5 Green", "6 Green", "7 Green", "8 Green", "9 Green", "Skip Green",
                "Reverse Green", "Draw Two Green", "1 Yellow", "2 Yellow", "3 Yellow", "4 Yellow", "5 Yellow",
                "6 Yellow", "7 Yellow", "8 Yellow", "9 Yellow", "Skip Yellow", "Reverse Yellow", "Draw Two Yellow"]

    for count, card in enumerate(uno_deck, start=1):
        position_dict[count] = card

    base_list = [i for i in range(1, len(uno_deck) + 1)]
    hist_list = []
    for key, value in position_dict.items():
        pos = shuffled_deck.index(value) + 1
        hist_list.append(pos)

    result = []
    for b, a in zip(hist_list, base_list):
        if b - a < 0:
            c = b - a + len(uno_deck)
            result.append(c)
        else:
            result.append(b - a)

    histogram = np.histogram(result, bins=range(1, len(uno_deck) + 1))
    histogram = histogram[0] / len(uno_deck)
    histogram = histogram[histogram != 0]
    histogram = histogram[~np.isnan(histogram)]
    entropy = histogram * np.log2(histogram)
    entropy = -np.sum(entropy)
    return entropy

# setting up a curve for colour randomness testing and plotting
import matplotlib.pyplot as plt
colour_dict = {}
res = shuffle(15, 3, uno_deck)
colour_dict[0] = colour_score(res)
for i in range(1, 100):
    res = shuffle(15, 3, res)
    cscore = colour_score(res)
    colour_dict[i] = cscore

# plotting a series of dictionaries where the key is the shuffle iteration and the value is the colour score.
# a "6_3" dictionary is a shuffle with 6 cards dropped and a deviation of 3.
plt.plot(*zip(*sorted(colour_dict_3_3.items())))
plt.plot(*zip(*sorted(colour_dict_4_3.items())))
plt.plot(*zip(*sorted(colour_dict_5_3.items())))
plt.plot(*zip(*sorted(colour_dict_6_3.items())))
plt.plot(*zip(*sorted(colour_dict_7_3.items())))
plt.plot(*zip(*sorted(colour_dict_8_3.items())))
plt.plot(*zip(*sorted(colour_dict_9_3.items())))
plt.plot(*zip(*sorted(colour_dict_10_3.items())))
plt.plot(*zip(*sorted(colour_dict_11_3.items())))
plt.plot(*zip(*sorted(colour_dict_12_3.items())))
plt.plot(*zip(*sorted(colour_dict_13_3.items())))
plt.plot(*zip(*sorted(colour_dict_14_3.items())))
plt.plot(*zip(*sorted(colour_dict_15_3.items())))
plt.xlabel("Shuffle Iteration")
plt.ylabel("Colour Score")
plt.title("Colour Score Curve")
plt.legend(["h3, dev3", "h4, dev3", "h5, dev3", "h6, dev3", "h7, dev3", "h8, dev3", "h9, dev3", "h10, dev3", "h11, dev3", "h12, dev3", "h13, dev3", "h14, dev3", "h15, dev3"])
plt.savefig("Colour_Score_Curve.png")
plt.grid()
plt.show()
plt.waitforbuttonpress()



# setting up a curve for Shannon randomness testing and plotting
import matplotlib.pyplot as plt
shannon_dict = {}
res = shuffle(3, 3, uno_deck)
shannon_dict[0] = shannon_entropy(res)
for i in range(1, 100):
    res = shuffle(3, 3, res)
    sscore = shannon_entropy(res)
    shannon_dict[i] = sscore

# plotting a series of dictionaries where the key is the shuffle iteration and the value is the Shannon score.
# a "6_3" dictionary is a shuffle with 6 cards dropped and a deviation of 3.
plt.plot(*zip(*sorted(shannon_dict_3_3.items())))
plt.plot(*zip(*sorted(shannon_dict_4_3.items())))
plt.plot(*zip(*sorted(shannon_dict_5_3.items())))
plt.plot(*zip(*sorted(shannon_dict_6_3.items())))
plt.plot(*zip(*sorted(shannon_dict_7_3.items())))
plt.plot(*zip(*sorted(shannon_dict_8_3.items())))
plt.plot(*zip(*sorted(shannon_dict_9_3.items())))
plt.plot(*zip(*sorted(shannon_dict_10_3.items())))
plt.plot(*zip(*sorted(shannon_dict_11_3.items())))
plt.plot(*zip(*sorted(shannon_dict_12_3.items())))
plt.plot(*zip(*sorted(shannon_dict_13_3.items())))
plt.plot(*zip(*sorted(shannon_dict_14_3.items())))
plt.plot(*zip(*sorted(shannon_dict_15_3.items())))
plt.xlabel("Shuffle Iteration")
plt.ylabel("Shannon Score")
plt.title("Shannon Score Curve")
plt.legend(["h3, dev3", "h4, dev3", "h5, dev3", "h6, dev3", "h7, dev3", "h8, dev3", "h9, dev3", "h10, dev3", "h11, dev3", "h12, dev3", "h13, dev3", "h14, dev3", "h15, dev3"])
plt.savefig("Shannon_Score_Curve.png")
plt.grid()
plt.show()
plt.waitforbuttonpress()





