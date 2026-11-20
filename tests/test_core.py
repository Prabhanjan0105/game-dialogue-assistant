"""Your tests. Each milestone in README.md gets one here: write the test first, then make it pass.

They start skipped. Remove the `skip` line as you work on each milestone.
"""
import pytest


# Milestone 1: Collect and preprocess game dialogue
def test_milestone_1():
    from app.core import milestone_1

    dialogues = milestone_1()

    # Verify the number of dialogues
    assert len(dialogues) == 20

    # Each dialogue must contain word tokens
    for tokens in dialogues:
        assert isinstance(tokens, list)
        assert len(tokens) > 0

        for token in tokens:
            assert isinstance(token, str)
            assert token == token.lower()
            assert token.isalnum()

    # Verify known vocabulary
    vocabulary = {
        word
        for dialogue in dialogues
        for word in dialogue
    }

    assert "guard" not in vocabulary
    assert "village" in vocabulary
    assert "magic" in vocabulary




# Milestone 2: Build n-gram model with smoothing
def test_milestone_2():
    from app.core import milestone_2

    model = milestone_2(n=3, k=1.0)

    # Verify model structure
    assert model["n"] == 3
    assert model["k"] == 1.0
    assert len(model["vocabulary"]) > 0

    assert len(model["ngram_counts"]) > 0
    assert len(model["context_counts"]) > 0

    # Verify next-word prediction
    predictions = model["predict_next"](
        ["the", "northern"],
        top_n=5
    )

    assert len(predictions) == 5

    # "gate" should be the most likely next word
    assert predictions[0][0] == "gate"

    # Probabilities must be valid
    for word, probability in predictions:
        assert isinstance(word, str)
        assert 0 < probability <= 1

    # Verify descending probability order
    probabilities = [
        probability for word, probability in predictions
    ]

    assert probabilities == sorted(
        probabilities, reverse=True
    )

    # Verify unseen context receives smoothing
    unseen = model["predict_next"](
        ["unknown", "context"],
        top_n=3
    )

    assert all(prob > 0 for _, prob in unseen)



# Milestone 3: Implement NPC dialogue generation
def test_milestone_3():
    from app.core import milestone_3

    # Generate dialogue from a known starting phrase
    dialogue = milestone_3(
        starting_phrase="the northern",
        max_words=20
    )

    assert isinstance(dialogue, str)
    assert len(dialogue) > 0

    # Verify starting phrase is preserved
    assert dialogue.lower().startswith("the northern")

    # Verify sentence formatting
    assert dialogue[0].isupper()
    assert dialogue.endswith(".")

    # Verify a known dialogue sequence
    assert "northern gate" in dialogue.lower()

    # Verify configurable maximum length
    short_dialogue = milestone_3(
        starting_phrase="the northern",
        max_words=2
    )

    # Two initial words + at most two generated words
    assert len(short_dialogue.rstrip(".").split()) <= 4

    # Verify invalid input handling
    import pytest

    with pytest.raises(ValueError):
        milestone_3(starting_phrase="")

    with pytest.raises(ValueError):
        milestone_3(max_words=0)



# Milestone 4: Design a CLI where users can input a starting phrase and generate dialogue.
@pytest.mark.skip(reason="remove this line when you start milestone 4")
def test_milestone_4():
    raise NotImplementedError("write the test for milestone 4")

