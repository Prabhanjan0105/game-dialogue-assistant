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




def milestone_2(n=3, k=1.0):
    """
    Build an n-gram language model with add-k smoothing.
    Default: trigram model (n=3).
    """
    from collections import Counter, defaultdict

    if not isinstance(n, int) or n < 2:
        raise ValueError("n must be an integer >= 2")

    if k <= 0:
        raise ValueError("k must be positive")

    # Load preprocessed dialogues from Milestone 1
    dialogues = milestone_1()

    ngram_counts = Counter()
    context_counts = Counter()
    vocabulary = set()

    for tokens in dialogues:
        vocabulary.update(tokens)

        # Add sentence-start and sentence-end markers
        padded = ["<s>"] * (n - 1) + tokens + ["</s>"]

        for i in range(n - 1, len(padded)):
            context = tuple(padded[i - n + 1:i])
            word = padded[i]

            ngram_counts[context + (word,)] += 1
            context_counts[context] += 1

    vocabulary.add("</s>")
    vocabulary = sorted(vocabulary)

    def predict_next(context, top_n=5):
        """Return the most likely next words."""
        if top_n < 1:
            raise ValueError("top_n must be positive")

        context = tuple(context[-(n - 1):])

        if len(context) < n - 1:
            context = ("<s>",) * (
                n - 1 - len(context)
            ) + context

        total = context_counts[context]
        vocab_size = len(vocabulary)

        predictions = []

        for word in vocabulary:
            count = ngram_counts[context + (word,)]

            probability = (
                (count + k) /
                (total + k * vocab_size)
            )

            predictions.append((word, probability))

        predictions.sort(
            key=lambda x: (-x[1], x[0])
        )

        return predictions[:top_n]

    return {
        "n": n,
        "k": k,
        "vocabulary": vocabulary,
        "ngram_counts": ngram_counts,
        "context_counts": context_counts,
        "predict_next": predict_next
    }




def milestone_3(starting_phrase="the northern",
                max_words=20, n=3, k=1.0):
    """
    Generate NPC dialogue using the n-gram language model.

    Starting phrase: Initial words supplied by the user.
    max_words: Maximum number of newly generated words.
    """
    import re

    if not isinstance(max_words, int) or max_words < 1:
        raise ValueError("max_words must be a positive integer")

    if not isinstance(starting_phrase, str):
        raise ValueError("starting_phrase must be a string")

    # Train the language model from Milestone 2
    model = milestone_2(n=n, k=k)
    predict_next = model["predict_next"]

    # Clean and tokenize the starting phrase
    tokens = re.findall(
        r"[a-z0-9]+",
        starting_phrase.lower()
    )

    if not tokens:
        raise ValueError("Starting phrase cannot be empty")

    generated = tokens.copy()

    # Repeatedly predict the next word
    for _ in range(max_words):
        context = generated[-(n - 1):]

        predictions = predict_next(
            context,
            top_n=len(model["vocabulary"])
        )

        # Select the most likely next word
        next_word = predictions[0][0]

        # Stop at the end-of-sentence marker
        if next_word == "</s>":
            break

        generated.append(next_word)

    # Format the final dialogue
    dialogue = " ".join(generated)
    dialogue = dialogue.capitalize()

    if not dialogue.endswith((".", "!", "?")):
        dialogue += "."

    return dialogue



# --- Milestone 4: Design a CLI where users can input a starting phrase and generate dialogue.
# Hint: Utilize command-line argument parsing to handle user input.
def milestone_4():  # TODO(milestone 4)
    raise NotImplementedError("TODO(milestone 4)")
