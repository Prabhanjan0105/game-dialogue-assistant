# Game Dialogue Assistant

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/sr92cbgeqr/badge.svg)](https://ask.thili.ai/b/sr92cbgeqr)

This project, 'Game Dialogue Assistant', provides game designers with a valuable tool to generate dialogue snippets for NPCs. By leveraging a next-word predictor built from scratch, it ensures character consistency and speeds up the prototyping process based on a corpus of game scripts.

## What you are building

**Goal.** You will build a command-line tool that assists game designers in generating dialogue snippets for Non-Player Characters (NPCs).

**Done when.** The tool successfully collects and preprocesses game dialogue, builds an n-gram language model with smoothing, implements dialogue generation, and allows users to input a starting phrase via a CLI to generate dialogue.

## Milestones

Tick these off as you go, and commit after each one.

- [ ] **1. Collect and preprocess a corpus of game dialogues.**  
      Hint: Use text preprocessing techniques to clean and tokenize the corpus.
- [ ] **2. Build the n-gram language model with smoothing.**  
      Hint: Implement n-gram counting and add-k smoothing for the language model.
- [ ] **3. Implement dialogue generation logic using the model.**  
      Hint: Apply the next-word prediction logic to iteratively build dialogue.
- [ ] **4. Design a CLI where users can input a starting phrase and generate dialogue.**  
      Hint: Utilize command-line argument parsing to handle user input.

## Run it

You need Python 3.12 and git.

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then choose a model; see the comments inside
python -m app.cli hello
pytest
```

Your work goes in `app/core.py` (one stub per milestone) and `tests/test_core.py`. The first tests pass already; they
check the plumbing.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Stretch ideas

- Allow users to specify the desired length of the generated dialogue snippet.
- Implement a feature to generate multiple alternative dialogue snippets for a given starting phrase.
- Add an option to filter generated dialogue based on a specific character's name or theme if present in the corpus.
