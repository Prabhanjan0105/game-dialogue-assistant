"""Your code. One stub per milestone; build them in order and keep each one small."""


def milestone_1():
    """Collect and preprocess a corpus of NPC game dialogue."""
    import re

    dialogues = [
        "Guard: The northern gate is closed tonight.",
        "Guard: The village is safe during the day.",
        "Guard: Beware of the monsters in the forest.",
        "Guard: The king has ordered us to protect the city.",
        "Guard: You must leave before the sun sets.",
        "Merchant: Welcome traveler, take a look at my wares.",
        "Merchant: I have the finest weapons in the kingdom.",
        "Merchant: Would you like to buy a healing potion?",
        "Merchant: The price of this sword is ten gold coins.",
        "Merchant: Come back when you have more gold.",
        "Wizard: The ancient crystal holds great power.",
        "Wizard: Magic flows through the mountains.",
        "Wizard: You must find the lost spell book.",
        "Wizard: The dark forest hides many secrets.",
        "Wizard: I can teach you the art of magic.",
        "Villager: Our village needs your help.",
        "Villager: The monsters attacked us last night.",
        "Villager: Please protect our homes from danger.",
        "Villager: The old castle is beyond the river.",
        "Villager: Thank you for saving our village.",
    ]

    processed_dialogues = []

    for dialogue in dialogues:
        # Remove the speaker label
        text = dialogue.split(":", 1)[1].strip()

        # Convert to lowercase
        text = text.lower()

        # Remove punctuation and special characters
        text = re.sub(r"[^a-z0-9\s]", "", text)

        # Split dialogue into word tokens
        tokens = text.split()

        if tokens:
            processed_dialogues.append(tokens)

    return processed_dialogues



# --- Milestone 2: Build the n-gram language model with smoothing.
# Hint: Implement n-gram counting and add-k smoothing for the language model.
def milestone_2():  # TODO(milestone 2)
    raise NotImplementedError("TODO(milestone 2)")


# --- Milestone 3: Implement dialogue generation logic using the model.
# Hint: Apply the next-word prediction logic to iteratively build dialogue.
def milestone_3():  # TODO(milestone 3)
    raise NotImplementedError("TODO(milestone 3)")


# --- Milestone 4: Design a CLI where users can input a starting phrase and generate dialogue.
# Hint: Utilize command-line argument parsing to handle user input.
def milestone_4():  # TODO(milestone 4)
    raise NotImplementedError("TODO(milestone 4)")
