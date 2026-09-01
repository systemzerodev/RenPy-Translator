define e = Character("Eileen")
define m = Character("Mia")

label start:

    e "Hello there."

    "This is narration."

    e happy "Nice to meet you."

    e "Hello [player_name]."

    m "{i}Welcome to the game.{/i}"

    # e "This line must be ignored."

    show text "This is not dialogue."

    menu:
        "Start Game":
            jump chapter_one