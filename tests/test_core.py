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



# Milestone 2: Build the n-gram language model with smoothing.
@pytest.mark.skip(reason="remove this line when you start milestone 2")
def test_milestone_2():
    raise NotImplementedError("write the test for milestone 2")


# Milestone 3: Implement dialogue generation logic using the model.
@pytest.mark.skip(reason="remove this line when you start milestone 3")
def test_milestone_3():
    raise NotImplementedError("write the test for milestone 3")


# Milestone 4: Design a CLI where users can input a starting phrase and generate dialogue.
@pytest.mark.skip(reason="remove this line when you start milestone 4")
def test_milestone_4():
    raise NotImplementedError("write the test for milestone 4")

