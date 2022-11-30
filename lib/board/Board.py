from lib.utils.Constants import Constants
from lib.board.Field import Field
from copy import copy


class Board:
    def __init__(self, color, setup):
        self.fields = self.load_fields(setup)
        self.pos_board_x = 100
        self.pos_board_y = 100
        self.white_on_top = False if color == Constants.FIG_WHITE else True
        self.selected_figure = None
        self.check_color = None
        self.legal_moves_on_check = []
        self.evaluation = 0
        self.kings_already_move = {
            Constants.FIG_WHITE: False,
            Constants.FIG_BLACK: False,
        }

    def save_fields(self):
        save = ''
        for row in self.fields:
            for field in row:
                if field.empty:
                    save += '0'
                else:
                    save += field.symbol
            save += '/'

        return save[:-1]

    def draw_fields(self, screen):
        if self.white_on_top:
            course = 1
        else:
            course = -1

        for i, row in enumerate(self.fields[::course]):
            for j, field in enumerate(row[::course]):
                if not field.empty:
                    field.draw_figure(screen, i, j)

    def select_figure(self, color, pos_x: int, pos_y: int):
        if self.white_on_top:
            field: Field = self.fields[pos_x][pos_y]
        else:
            field: Field = self.fields[7 - pos_x][7 - pos_y]

        if field.empty or field.figure.color != color:
            self.selected_figure = None
        else:
            if not self.check_color:
                self.selected_figure = field
            else:
                select_figure = None
                for available_move in self.legal_moves_on_check:
                    if available_move[0] == field:
                        select_figure = field
                        break
                if not select_figure:
                    self.selected_figure = None
                else:
                    self.selected_figure = select_figure

    def check_move(self, pos_x, pos_y):
        if not self.white_on_top:
            pos_x = 7 - pos_x
            pos_y = 7 - pos_y
        if self.selected_figure:
            if not self.check_color and (pos_x, pos_y) in self.selected_figure.possible_moves(self.fields):
                # checking if this move give check for myself
                subboard = self.make_move_simulation(self.selected_figure, (pos_x, pos_y))
                king = self.find_king(subboard, self.selected_figure.figure.color)
                if not king.check_check(subboard):
                    return True
                else:
                    return False

            elif self.check_color:
                moves = []
                for available_move in self.legal_moves_on_check:
                    if available_move[0] == self.selected_figure:
                        moves.append(available_move[1])
                if (pos_x, pos_y) in moves:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def move(self, target_x, target_y):
        # switch x, y if board is reserved
        if not self.white_on_top:
            target_x = 7 - target_x
            target_y = 7 - target_y

        if self.checking_castle(target_x, target_y):
            self.castle(target_x, target_y)

        else:
            old_x: int = self.selected_figure.pos_x
            old_y: int = self.selected_figure.pos_y
            clear_field = Field(old_x, old_y)

            # move figure to new position
            self.selected_figure.pos_x = target_x
            self.selected_figure.pos_y = target_y
            self.fields[target_x][target_y] = self.selected_figure

            # clear old figure position
            self.fields[old_x][old_y] = clear_field

            # clear selected figure
            self.selected_figure = None

            # clear check status
            self.check_color = None

            # check and promotion pawns
            self.promotion_pawns()

            # set evaluation
            self.set_evaluation()

            # check if king move of start position
            self.set_king_already_move()

    def set_legal_moves_on_check(self):
        legal_moves_on_check = []
        for row in self.fields:
            for field in row:
                if field.is_color(self.check_color):
                    if field.symbol == 'k' or field.symbol == 'K':
                        moves = field.possible_moves(self.fields)
                        for m in moves:
                            legal_moves_on_check.append((field, m))
                    else:
                        moves = field.possible_moves(self.fields)
                        for move in moves:
                            subboard = self.make_move_simulation(field, move)

                            king = self.find_king(subboard, self.check_color)

                            if not king.check_check(subboard):
                                legal_moves_on_check.append((field, move))

        self.legal_moves_on_check = legal_moves_on_check

    # give new board with simulation
    def make_move_simulation(self, field, move):
        subboard = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                subboard[i][j] = copy(self.fields[i][j])

        subboard[move[0]][move[1]] = field
        x, y = field.pos_x, field.pos_y
        subboard[x][y] = Field(x, y)

        return subboard

    def set_evaluation(self):
        evaluation = 0
        for row in self.fields:
            for field in row:
                if not field.empty:
                    symbol = field.symbol
                    color = field.figure.color
                    x, y = field.pos_x, field.pos_y
                    if color == Constants.FIG_WHITE:
                        e_fig = Constants.EVALUATION_FIG[symbol]
                        e = e_fig['value']
                        e_pos = e_fig['evalu'][x][y]
                    else:
                        e_fig = Constants.EVALUATION_FIG[symbol.lower()]
                        e = e_fig['value'] * -1
                        e_pos = [ar[::-1] for ar in e_fig['evalu'][::-1]][x][y] * -1
                    evaluation += e + e_pos
        self.evaluation = evaluation

    def castle(self, target_x, target_y):
        if not self.white_on_top:
            target_x = 7 - target_x
            target_y = 7 - target_y

        castle_setups = {
            'white-short': [(0, 0), (1, 0), (2, 0), (3, 0)],
            'white-long': [(7, 0), (6, 0), (5, 0), (3, 0)],
            'black-short': [(0, 7), (1, 7), (2, 7), (3, 7)],
            'black-long': [(7, 7), (6, 7), (5, 7), (3, 7)],
        }
        setup = []

        if (target_x, target_y) == (0, 0):
            setup = castle_setups['white-short']

        elif (target_x, target_y) == (7, 0):
            setup = castle_setups['white-long']

        elif (target_x, target_y) == (0, 7):
            setup = castle_setups['black-short']

        elif (target_x, target_y) == (7, 7):
            setup = castle_setups['black-long']

        old_r_x, old_r_y = setup[0]
        new_k_x, new_k_y = setup[1]
        new_r_x, new_r_y = setup[2]
        old_k_x, old_k_y = setup[3]

        old_rook = self.fields[old_r_x][old_r_y]
        old_king = self.fields[old_k_x][old_k_y]
        # move king to new position
        self.fields[new_k_x][new_k_y] = old_king
        self.fields[new_k_x][new_k_y].pos_x = new_k_x
        self.fields[new_k_x][new_k_y].pos_y = new_k_y
        # move rook to new position
        self.fields[new_r_x][new_r_y] = old_rook
        self.fields[new_r_x][new_r_y].pos_x = new_r_x
        self.fields[new_r_x][new_r_y].pos_y = new_r_y
        # clear old fields
        self.fields[old_r_x][old_r_y] = Field(old_r_x, old_r_y)
        self.fields[old_k_x][old_k_y] = Field(old_k_x, old_k_y)
        # clear selected figure
        self.selected_figure = None
        # clear check status
        self.check_color = None
        # set evaluation
        self.set_evaluation()
        # king can use one castle
        self.set_king_already_move()

    def set_king_already_move(self):
        if self.fields[3][0].empty:
            self.kings_already_move[Constants.FIG_WHITE] = True
            king = self.find_king(self.fields, Constants.FIG_WHITE)
            king.set_first_move()

        if self.fields[3][7].empty:
            self.kings_already_move[Constants.FIG_BLACK] = True
            king = self.find_king(self.fields, Constants.FIG_BLACK)
            king.set_first_move()

    @ staticmethod
    def find_king(fields, color):
        for row in fields:
            for field in row:
                if field.symbol == 'k' and color == Constants.FIG_WHITE:
                    return field
                if field.symbol == 'K' and color == Constants.FIG_BLACK:
                    return field

    def promotion_pawns(self):
        for i, row in enumerate(self.fields):
            if row[0].symbol == 'P':
                row[0] = Field(i, 0, 'H')
        for i, row in enumerate(self.fields):
            if row[7].symbol == 'p':
                row[7] = Field(i, 7, 'h')

    def checking_castle(self, target_x, target_y):
        if (target_x, target_y) in [(0, 0), (7, 0), (0, 7), (7, 7)]:
            if self.selected_figure.symbol == 'k' and not self.kings_already_move[Constants.FIG_WHITE]:
                return True

            if self.selected_figure.symbol == 'K' and not self.kings_already_move[Constants.FIG_BLACK]:
                return True

        return False

    @staticmethod
    def load_fields(setup):
        fields = [[] for _ in range(8)]

        for i, (row_f, row_s) in enumerate(zip(fields, setup.split('/'))):

            for j, symbol in enumerate([*row_s]):
                if symbol != '0':
                    field = Field(i, j, symbol)
                else:
                    field = Field(i, j)

                fields[i].append(field)
        return fields
