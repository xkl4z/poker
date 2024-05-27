from util.deck import Deck
from util.table import Table

deck = Deck()
deck.new_round()
deck.shuffle()

table = Table()


def main(args):

    output_filepath = args.output_filepath or "quiz.txt"

    with open(output_filepath, "w") as f:

        while len(deck.remaining) > 0:
            cards = deck.deal() + deck.deal()
            table.actions = table.generate_actions(mode="RFI", length=6, hero_cards=cards)
            s = table.to_string()
            f.write(s + "\n====\n\n")


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_filepath")
    args = parser.parse_args()

    main(args)
