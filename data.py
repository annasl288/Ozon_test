class Data:

    SUPERHEROES_GENDER_WORK = [
        ["Male", True],
        ["Male", False],
        ["Female", True],
        ["Female", False],
        ["-", True],
        ["-", False]
    ]

    SUPERHEROES_WRONG_DATA_TYPE = [
        [None, False],
        [1, False],
        [True, True],
        ["Male", "False"],
        ["Male", 2],
        ["Female", None]
    ]

    SUPERHEROES_NAME_HEIGHT = [
        {"name": "A-Bomb", "height": "203 cm"},
        {"name": "Anti-Monitor", "height": "61.0 meters"},
        {"name": "Dagger", "height": "0 kg"}
    ]
