class Constants:
    # colors
    GREY_10 = (200, 200, 200)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    CYAN = (64, 224, 208)

    # Standard board setup
    SIZE_CELL_OF_BOARD = 80
    POS_OF_BOARD_X = 100
    POS_OF_BOARD_Y = 100
    FIG_WHITE: str = 'White'
    FIG_BLACK: str = 'Black'
    BOARD_SETUP_ = [
        ['', '', '', '', '', '', '', 'W'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['k', '', '', '', '', '', '', 'K'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['w', '', '', '', '', '', '', '']
    ]

    BOARD_SETUP_ = [
        ['w', 'p', '', '', '', '', 'P', 'W'],
        ['s', 'p', '', '', '', '', 'P', 'S'],
        ['g', 'p', '', '', '', '', 'P', 'G'],
        ['k', 'p', '', '', '', '', 'P', 'K'],
        ['h', 'p', '', '', '', '', 'P', 'H'],
        ['g', 'p', '', '', '', '', 'P', 'G'],
        ['s', 'p', '', '', '', '', 'P', 'S'],
        ['w', 'p', '', '', '', '', 'P', 'W']
    ]

    BOARD_SETUP = 'wp0000PW/sp0000PS/gp0000PG/kp0000PK/hp0000PH/gp0000PG/sp0000PS/wp0000PW'

    # THANKS FOR https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/
    E_PAWN = [
        [0.0, 0.5, 0.5, 0.0, 0.5, 1.0, 5.0, 0.0],
        [0.0, 1.0, -0.5, 0.0, 0.5, 1.0, 5.0, 0.0],
        [0.0, 1.0, -1.0, 0.0, 1.0, 2.0, 5.0, 0.0],
        [0.0, -2.0, 0.0, 2.0, 2.5, 3.0, 5.0, 0.0],
        [0.0, -2.0, 0.0, 2.0, 2.5, 3.0, 5.0, 0.0],
        [0.0, 1.0, -1.0, 0.0, 1.0, 2.0, 5.0, 0.0],
        [0.0, 1.0, -0.5, 0.0, 0.5, 1.0, 5.0, 0.0],
        [0.0, 0.5, 0.5, 0.0, 0.5, 1.0, 5.0, 0.0],
    ]

    E_KNIGHT = [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0, 0.5, 0.0, 0.5, 0.0, -2.0, -4.0],
        [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
        [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
        [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
        [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
        [-4.0, -2.0, 0.5, 0.0, 0.5, 0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    ]

    E_BISHOP = [
        [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
        [-1.0, 0.5, 1.0, 0.0, 0.5, 0.0, 0.0, -1.0],
        [-1.0, 0.5, 1.0, 1.0, 0.5, 0.5, 0.0, -1.0],
        [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
        [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
        [-1.0, 0.5, 1.0, 1.0, 0.5, 0.5, 0.0, -1.0],
        [-1.0, 0.5, 1.0, 0.0, 0.5, 0.0, 0.0, -1.0],
        [-2.0, -1.0, -1.0, -1.0, -0.0, -1.0, -1.0, -2.0],
    ]

    E_ROOK = [
        [0.0, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, 0.0],
    ]

    E_QUEEN = [
        [-2.0, -1.0, -1.0, 0.0, -0.5, -1.0, -1.0, -2.0],
        [-1.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
        [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
        [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
        [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
        [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
        [-1.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
        [-2.0, -1.0, -1.0, 0.0, -0.5, -1.0, -1.0, -2.0],
    ]

    E_KING = [
        [2.0, 2.0, -1.0, -2.0, -3.0, -3.0, -3.0, -3.0],
        [3.0, 2.0, -2.0, -3.0, -4.0, -4.0, -4.0, -4.0],
        [1.0, 0.0, -2.0, -3.0, -4.0, -4.0, -4.0, -4.0],
        [0.0, 0.0, -2.0, -4.0, -5.0, -5.0, -5.0, -5.0],
        [0.0, 0.0, -2.0, -4.0, -5.0, -5.0, -5.0, -5.0],
        [1.0, 0.0, -2.0, -3.0, -4.0, -4.0, -4.0, -4.0],
        [3.0, 2.0, -2.0, -3.0, -4.0, -4.0, -4.0, -4.0],
        [2.0, 2.0, -1.0, -2.0, -3.0, -3.0, -3.0, -3.0],
    ]

    EVALUATION_FIG = {
        'p': {
            'value': 10,
            'evalu': E_PAWN
        },
        's': {
            'value': 30,
            'evalu': E_KNIGHT
        },
        'g': {
            'value': 30,
            'evalu': E_BISHOP
        },
        'w': {
            'value': 50,
            'evalu': E_ROOK
        },
        'h': {
            'value': 90,
            'evalu': E_QUEEN
        },
        'k': {
            'value': 900,
            'evalu': E_KING
        },
    }

