import random


class Table:

    GRID = [
        [None, "UTG", "HI", None],
        ["BB", None, None, "CO"],
        [None, "SB", "BTN", None],
    ]
    POSITION_NAMES = {
        "UTG": "UTG - __________",
        "HI": "HI  - __________",
        "CO": "CO  - __________",
        "BTN": "BTN - __________",
        "SB": "SB  - __________",
        "BB": "BB  - __________",
    }
    ACTION = {0: "_____raise", 1: "______call", 2: "______fold"}

    def __init__(self):
        self.actions = None

    def pad_action_sequence(self, action_sequence, max_length):
        return action_sequence + ["__________"] * (max_length - len(action_sequence))

    def generate_actions(self, mode, length, hero_cards):

        action_sequence = []

        if mode == "RFI":

            action_sequence += [self.ACTION[2]] * random.randint(0, length - 2) + [
                f"______{hero_cards}"
            ]

            action_sequence = self.pad_action_sequence(
                action_sequence=action_sequence, max_length=length
            )

            if length == 6:
                action_sequence = zip(["UTG", "HI", "CO", "BTN", "SB", "BB"], action_sequence)

        return {action_name: action for action_name, action in action_sequence}

    def to_string(self):
        output_string = ""
        position_idx = 0
        for row in self.GRID:
            for position in row:
                if position is None:
                    output_string += "     "
                else:
                    output_string += (
                        self.POSITION_NAMES[position].replace("__________", self.actions[position])
                        + "    "
                    )
                    position_idx += 1
            output_string += "\n"

        return output_string

    def print_table(self):
        print(self.to_string())


if __name__ == "__main__":

    table = Table()
    table.actions = table.generate_actions(mode="RFI", length=6, hero_cards="Ts4h")
    table.print_table()
