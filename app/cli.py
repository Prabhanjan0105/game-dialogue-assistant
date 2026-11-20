
"""Command-line interface for Game Dialogue Assistant."""

import argparse
from app.core import milestone_3


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="game-dialogue-assistant",
        description="Generate NPC dialogue using an n-gram language model."
    )

    sub = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Original starter command
    sub.add_parser(
        "hello",
        help="Check that the application is working"
    )

    # Dialogue generation command
    generate_parser = sub.add_parser(
        "generate",
        help="Generate NPC dialogue from a starting phrase"
    )

    generate_parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Starting phrase for dialogue generation"
    )

    generate_parser.add_argument(
        "--max-words",
        type=int,
        default=20,
        help="Maximum number of new words (default: 20)"
    )

    generate_parser.add_argument(
        "--n",
        type=int,
        default=3,
        help="N-gram size (default: 3)"
    )

    generate_parser.add_argument(
        "--k",
        type=float,
        default=1.0,
        help="Add-k smoothing value (default: 1.0)"
    )

    args = parser.parse_args(argv)

    if args.command == "hello":
        print(
            "Game Dialogue Assistant is ready. "
            "Open README.md for your milestones."
        )

    elif args.command == "generate":
        try:
            dialogue = milestone_3(
                starting_phrase=args.prompt,
                max_words=args.max_words,
                n=args.n,
                k=args.k
            )

        except (ValueError, TypeError) as error:
            parser.error(str(error))

        print("\n" + "=" * 55)
        print("GAME DIALOGUE ASSISTANT")
        print("=" * 55)

        print(f"Starting Phrase : {args.prompt}")
        print(f"Maximum Words   : {args.max_words}")
        print(f"N-gram Model    : {args.n}-gram")
        print(f"Smoothing       : {args.k}")

        print("-" * 55)
        print("GENERATED NPC DIALOGUE:")
        print(dialogue)
        print("=" * 55)


if __name__ == "__main__":
    main()
