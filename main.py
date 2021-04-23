from tkinter import *
import random
import classes.Board as Board


class Generation:
    def __init__(self, gen_num, boards, best, worst, average_score):
        self.gen_num = gen_num
        self.generation = boards
        self.best = best
        self.worst = worst
        self.breading_pairs = []
        self.average_score = average_score

    def get_gen_num(self):
        return self.gen_num

    def get_generation(self):
        return self.generation

    def get_best_specimen(self):
        return self.best

    def get_worst_specimen(self):
        return self.worst

    def get_average_score(self):
        return self.average_score

    def get_specimen(self, num):
        if num < len(self.generation):
            print("ERROR, Number given was too high")
            return
        return self.generation(num)

    def get_breading_pairs(self,num_children):
        self.breading_pairs = []
        breading_specimens = []
        num = 0
        for specimen in self.generation:
            if specimen.get_score() > self.get_average_score():
                breading_specimens.append(specimen)
        while num != num_children-(int(num_children*.05)*2):
            random_specimen1 = random.randint(0, len(breading_specimens) - 1)
            random_specimen2 = random.randint(0, len(breading_specimens) - 1)
            self.breading_pairs.append([breading_specimens[random_specimen1], breading_specimens[random_specimen2]])
            num += 2

        return self.breading_pairs

    def print_best_specimen(self):
        best_specimen.print_layout_to_console(best_specimen.get_layout())



class Tile:
    def __init__(self, game_board, x_pos, y_pos):
        self.queens_toggled = []
        self.board = game_board
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.total_queens_path = []
        self.this_queens_path = []
        self.is_queen = False
        self.is_barrier = False
        self.toggleOn = False

    def add_queen_toggle(self, queen):
        self.queens_toggled.append(queen)

    def remove_queen_toggle(self, queen):
        self.queens_toggled.remove(queen)

    def get_queen_toggle(self):
        return self.queens_toggled

    def add_queen_path(self, position):
        self.total_queens_path.append(position)

    def get_total_queen_path(self):
        return self.total_queens_path

    def make_queen(self, x_pos, y_pos, intelligent=False):
        global empty_spaces
        global board_pieces
        self.is_queen = True
        self.l_horizontal_path_queen()
        self.r_horizontal_path_queen()
        self.t_vertical_path_queen()
        self.b_vertical_path_queen()
        self.tr_diagonal_path_queen()
        self.tl_diagonal_path_queen()
        self.bl_diagonal_path_queen()
        self.br_diagonal_path_queen()
        try:
            empty_spaces.remove([x_pos, y_pos])
        except ValueError:
            pass
        if intelligent:
            for pos in self.this_queens_path:
                if not len(board_pieces[pos[0]][pos[1]].get_total_queen_path()) == 0:
                    try:
                        empty_spaces.remove([pos[0], pos[1]])
                    except ValueError:
                        pass

    def make_barrier(self):
        self.is_barrier = True

    def get_queen(self):
        return self.is_queen

    def get_barrier(self):
        return self.is_barrier

    def t_vertical_path_queen(self):
        global board_pieces
        up = self.y_pos
        while up >= 0:
            if not up == self.y_pos:
                if board_pieces[self.x_pos][up].get_barrier():
                    break
                self.this_queens_path.append([self.x_pos, up])
                board_pieces[self.x_pos][up].add_queen_path([self.x_pos, up])
            up -= 1

    def b_vertical_path_queen(self):
        global board_pieces
        global board_height
        down = self.y_pos
        while down < board_height:
            if not down == self.y_pos:
                if board_pieces[self.x_pos][down].get_barrier():
                    break
                self.this_queens_path.append([self.x_pos, down])
                board_pieces[self.x_pos][down].add_queen_path([self.x_pos, down])
            down += 1

    def l_horizontal_path_queen(self):
        global board_pieces
        global board_width
        left = self.x_pos
        while left >= 0:
            if not left == self.x_pos:
                if board_pieces[left][self.y_pos].get_barrier():
                    break
                self.this_queens_path.append([left, self.y_pos])
                board_pieces[left][self.y_pos].add_queen_path([left, self.y_pos])
            left -= 1

    def r_horizontal_path_queen(self):
        global board_pieces
        global board_width
        right = self.x_pos
        while right < board_width:
            if not right == self.x_pos:
                if board_pieces[right][self.y_pos].get_barrier():
                    break
                self.this_queens_path.append([right, self.y_pos])
                board_pieces[right][self.y_pos].add_queen_path([right, self.y_pos])
            right += 1

    def tr_diagonal_path_queen(self):
        global board_pieces
        global board_width
        global board_height
        y = self.y_pos
        x = self.x_pos
        while y >= 0 and x < board_width:
            if not (y == self.y_pos and x == self.x_pos):
                if board_pieces[x][y].get_barrier():
                    break
                self.this_queens_path.append([x, y])
                board_pieces[x][y].add_queen_path([x, y])
            y -= 1
            x += 1

    def tl_diagonal_path_queen(self):
        global board_pieces
        global board_width
        global board_height
        y = self.y_pos
        x = self.x_pos
        while y >= 0 and x >= 0:
            if not (y == self.y_pos and x == self.x_pos):
                if board_pieces[x][y].get_barrier():
                    break
                self.this_queens_path.append([x, y])
                board_pieces[x][y].add_queen_path([x, y])
            y -= 1
            x -= 1

    def bl_diagonal_path_queen(self):
        global board_pieces
        global board_width
        global board_height
        y = self.y_pos
        x = self.x_pos
        while y < board_height and x >= 0:
            if not (y == self.y_pos and x == self.x_pos):
                if board_pieces[x][y].get_barrier():
                    break
                self.this_queens_path.append([x, y])
                board_pieces[x][y].add_queen_path([x, y])
            y += 1
            x -= 1

    def br_diagonal_path_queen(self):
        global board_pieces
        global board_width
        global board_height
        y = self.y_pos
        x = self.x_pos
        while y < board_height and x < board_width:
            if not (y == self.y_pos and x == self.x_pos):
                if board_pieces[x][y].get_barrier():
                    break
                self.this_queens_path.append([x, y])
                board_pieces[x][y].add_queen_path([x, y])
            y += 1
            x += 1

    # def display_queens_path(self):
    #     global board_pieces
    #     if not self.toggleOn:
    #         self.toggleOn = True
    #     else:
    #         self.toggleOn = False
    #     for row in self.this_queens_path:
    #         if not self.toggleOn and len(board_pieces[row[0]][row[1]].get_queen_toggle()) <= 1:
    #             board_pieces[row[0]][row[1]].set_bg("SystemButtonFace")
    #             board_pieces[row[0]][row[1]].remove_queen_toggle([self.x_pos, self.y_pos])
    #         else:
    #             board_pieces[row[0]][row[1]].set_bg("yellow")
    #             try:
    #                 board_pieces[row[0][row[1]]].get_queen_toggled.index([self.x_pos, self.y_pos])
    #                 board_pieces[row[0]][row[1]].remove_queen_toggle([self.x_pos, self.y_pos])
    #             except TypeError:
    #                 board_pieces[row[0]][row[1]].add_queen_toggle([self.x_pos, self.y_pos])
    #
    # def set_bg(self, color):
    #     self.tile_button = Button(board, width=button_width, height=button_height, text=self.text, borderwidth=2,
    #                               relief="groove",
    #                               command=self.display_queens_path, bg=color,
    #                               font=("Courier", font_size))
    #     self.tile_button.grid(row=self.y_pos, column=self.x_pos)

    def clear_total_queens_path(self):
        self.total_queens_path.clear()

    def clear_this_queens_path(self):
        self.this_queens_path.clear()


def place_barriers(layout, num_barriers=None):
    global board_pieces
    global board_width
    global board_height
    global barrier_locations
    barriers_placed = 0
    if not layout:
        while True:
            if num_barriers is None:
                return
            for x in range(0, board_height):
                for y in range(0, board_width):
                    barrier_chance = random.randint(0, 4)
                    if barrier_chance == 0 and not (board_pieces[x][y].get_queen() or board_pieces[x][y].get_barrier()):
                        barrier_locations.append([x, y])
                        board_pieces[x][y].make_barrier()
                        barriers_placed += 1
                        empty_spaces.remove([x, y])
                        if num_barriers is None or num_barriers <= barriers_placed:
                            return
            if num_barriers is None or num_barriers <= barriers_placed:
                return
    else:
        for x in range(0, board_height):
            for y in range(0, board_width):
                if [x, y] in layout:
                    barrier_locations.append([x, y])
                    board_pieces[x][y].make_barrier()
                    empty_spaces.remove([x, y])


def place_queens(locations=None, intelligent=False, gen_num=None):
    global queen_locations
    global queen_count
    if locations is not None:
        mutate_x = random.randint(0, board_width-1)
        mutation_chance_generation = random.uniform(0, int(mutation_factor))
        # print(mutation_factor)
        for location in locations:
            # If my total average score > last_gen_average score = guaranteed mutation
            # as my total average score approaches the last generation average score increase mutation chance
            # 4-3 = 1/.2 = 5

            mutation_chance_specimen = random.randint(0, 5)
            y_on_mutation = random.randint(0, board_height - 1)
            if mutation_chance_generation < 1.5 and location[0] == mutate_x and mutation_chance_specimen < 2:
                # print("Mutated")
                mutation_type = ["add_specimen", "change_specimen", "both"]
                choice = random.choice(mutation_type)
                if choice == mutation_type[0]:
                    if not (board_pieces[location[0]][location[1]].get_queen() or board_pieces[location[0]][location[1]].get_barrier()):
                        board_pieces[location[0]][location[1]].make_queen(location[0], location[1], intelligent)
                        queen_locations.append([location[0], location[1]])
                        queen_count += 1
                    new_location_y = random.randint(0, board_height-1)
                    while True:
                        if board_pieces[location[0]][new_location_y].get_queen() or board_pieces[location[0]][new_location_y].get_barrier():
                            new_location_y = random.randint(0, board_height-1)
                        else:
                            board_pieces[location[0]][new_location_y].make_queen(location[0], new_location_y)
                            queen_locations.append([location[0], new_location_y])
                            queen_count += 1
                            break
                elif choice == mutation_type[1]:
                    while True:
                        if board_pieces[location[0]][y_on_mutation].get_queen() or board_pieces[location[0]][y_on_mutation].get_barrier():
                            y_on_mutation = random.randint(0, board_height-1)

                        else:
                            board_pieces[location[0]][y_on_mutation].make_queen(location[0], y_on_mutation, intelligent)
                            queen_locations.append([location[0], y_on_mutation])
                            queen_count += 1
                            break
                else:
                    new_location_y = random.randint(0, board_height-1)
                    while True:
                        if board_pieces[location[0]][new_location_y].get_queen() or board_pieces[location[0]][new_location_y].get_barrier():
                            new_location_y = random.randint(0, board_height-1)
                        else:
                            board_pieces[location[0]][new_location_y].make_queen(location[0], new_location_y)
                            queen_locations.append([location[0], new_location_y])
                            queen_count += 1
                            break
                    while True:
                        if board_pieces[location[0]][y_on_mutation].get_queen() or board_pieces[location[0]][y_on_mutation].get_barrier():
                            y_on_mutation = random.randint(0, board_height-1)
                        else:
                            board_pieces[location[0]][y_on_mutation].make_queen(location[0], y_on_mutation, intelligent)
                            queen_locations.append([location[0], y_on_mutation])
                            queen_count += 1
                            break
            else:
                if not(board_pieces[location[0]][location[1]].get_queen() or board_pieces[location[0]][location[1]].get_barrier()):
                    board_pieces[location[0]][location[1]].make_queen(location[0], location[1], intelligent)
                    queen_locations.append([location[0], location[1]])
                    queen_count += 1
    elif intelligent:
        while True:
            for space in empty_spaces:
                queen_chance = random.randint(0, 10)
                if queen_chance == 9:
                    board_pieces[space[0]][space[1]].make_queen(space[0], space[1], intelligent)
                    queen_locations.append([space[0], space[1]])
                    queen_count += 1
            if len(empty_spaces) == 0:
                break
    else:
        for x in range(0, board_width):
            barrier_in_col = False
            made_queen_in_col = False
            num_queens_in_col = 0
            while not made_queen_in_col:
                for y in range(0, board_height):
                    queen_chance = random.randint(0, 9)
                    if queen_chance == 9 and not (board_pieces[x][y].get_queen() or board_pieces[x][y].get_barrier()):
                        board_pieces[x][y].make_queen(x, y, intelligent)
                        made_queen_in_col = True
                        queen_count += 1
                        num_queens_in_col += 1
                        queen_locations.append([x, y])
                        if not barrier_in_col:
                            for z in range(0, board_height):
                                if board_pieces[x][z].get_barrier():
                                    barrier_in_col = True
                                    break
                        if not barrier_in_col:
                            break


def clear_generation():
    global best_specimen
    global worst_specimen
    global current_generation
    current_generation = []
    best_specimen = None
    worst_specimen = None


def create_generation(num_specimens, intelligent=False):
    # global generations
    global total_score
    global total_average_score
    global last_generation
    global generation_num
    global mutation_factor
    clear_generation()
    total_specimen = 0
    generation_score = 0
    try:
        if not total_average_score < 0:
            mutation_factor = (abs(last_generation.get_average_score() - total_average_score)) * 5
            print(mutation_factor)
    except ZeroDivisionError or ZeroDivisionError:
        pass
    if generation_num > 0 and not intelligent:
        for breading_pair in last_generation.get_breading_pairs(num_specimens):
            parent_one = sorted(breading_pair[0].get_queen_locations())
            parent_two = sorted(breading_pair[1].get_queen_locations())
            offspring_one = []
            offspring_two = []
            for x in range(0, board_width):
                parent_chance = random.randint(0, 1)
                for pair in parent_one:
                    if pair[0] == x and parent_chance == 0:
                        offspring_one.append(pair)
                    elif pair[0] == x:
                        offspring_two.append(pair)
                for pair in parent_two:
                    if pair[0] == x and parent_chance == 1:
                        offspring_one.append(pair)
                    elif pair[0] == x:
                        offspring_two.append(pair)
                offspring_one = sorted(offspring_one)
                offspring_two = sorted(offspring_two)
            create_specimen(offspring_one)
            generation_score += current_generation[total_specimen].get_score()
            total_specimen += 1
            if total_specimen == num_specimens - 1:
                break
            create_specimen(offspring_two)
            generation_score += current_generation[total_specimen].get_score()
            total_specimen += 1
            if total_specimen == num_specimens - 1:
                break

    for x in range(total_specimen, num_specimens):
        create_specimen(intelligent=intelligent)
        generation_score += current_generation[x].get_score()
    # generations.append(Generation(generation_num, current_generation, best_specimen, worst_specimen))
    average_score = float(generation_score)/float(num_specimens)
    last_generation = Generation(generation_num, current_generation, best_specimen, worst_specimen, average_score)
    total_score += average_score
    total_average_score = total_score / (generation_num+1)
    last_generation.print_best_specimen()
    print("Generation: %i | Worst Score: %i | Best Score: %i | Average Score: %f | Total Average Score: %f " % (generation_num, worst_specimen.get_score(), best_specimen.get_score(), average_score, total_average_score))
    generation_num += 1


def clear():
    global empty_spaces
    global queen_count
    global queen_locations
    global barrier_locations
    global board_pieces
    global num_collisions
    global score
    queen_count = 0
    num_collisions = 0
    score = 0
    queen_locations = []
    barrier_locations = []
    board_pieces = []
    empty_spaces = []


def create_specimen(offsprings=None, intelligent=False):
    global current_specimen_num
    global board_pieces
    global board_width
    global board_height
    global num_collisions
    global best_specimen
    global worst_specimen
    global score
    clear()
    for x in range(0, board_height):
        column = []
        for y in range(0, board_width):
            column.append(Tile(board, x, y))
            empty_spaces.append([x, y])
        board_pieces.append(column)
    place_barriers(barrier_placement)
    place_queens(locations=offsprings, intelligent=intelligent)
    for queen in queen_locations:
        num_collisions += len(board_pieces[queen[0]][queen[1]].get_total_queen_path())
    if queen_count == 0:
        score = -9999
    else:
        score = queen_count - num_collisions
    current_specimen = Board.Board(current_specimen_num, queen_count, num_collisions, score, board_pieces,
                                   queen_locations,
                                   barrier_locations, empty_spaces)
    current_generation.append(current_specimen)
    if best_specimen is None or best_specimen.get_score() < current_specimen.get_score():
        best_specimen = current_specimen
    if worst_specimen is None or worst_specimen.get_score() > current_specimen.get_score():
        worst_specimen = current_specimen
    current_specimen_num += 1


def clear_gui(game_board, pieces):
    pieces.clear()
    gb = game_board.grid_slaves()
    for cell in gb:
        cell.destroy()


def create_board_gui(specimen_to_print):
    specimen_to_print.print_board_to_gui(board, specimen_to_print.get_layout())


def create_gui(specimen_to_print):
    new_generation_button = Button(board,
                                   width=1,
                                   height=1,
                                   text="NG",
                                   borderwidth=2,
                                   relief="groove",
                                   font=("Courier", 16),
                                   command=add_generation)
    new_generation_button.grid(row=1, column=board_width + 1)
    generation_label = Label(board, text="Select Generation: ", font=("Courier", font_size))
    generation_label.grid(row=5, column=(board_width + 2), columnspan=2, sticky="NESW")
    selected_generation = StringVar(board)
    selected_generation.set(generation_num)
    # select_generation = OptionMenu(board, selected_generation, generations)
    # select_generation.config(bg="green", font=("Courier", font_size))
    # select_generation["menu"].config(bg="white")
    # select_generation.grid(row=5, column=(board_width + 4), columnspan=1, sticky="NESW")

    specimen_label = Label(board, text="Select specimen per the generation: ", font=("Courier", font_size))
    specimen_label.grid(row=6, column=(board_width + 2), columnspan=2, sticky="NESW")
    selected_specimen = StringVar(board)
    selected_specimen.set(generation_num)

    gen_list = []
    for x in range(0, generation_num):
        gen_list.append(x)
    select_specimen = OptionMenu(board, selected_specimen, gen_list)
    select_specimen.config(bg="green", font=("Courier", font_size))
    select_specimen["menu"].config(bg="white")
    select_specimen.grid(row=5, column=(board_width + 4), columnspan=1, sticky="NESW")

    q_count_label = Label(board, text="Score: ", borderwidth=2, relief="groove",
                          font=("Courier", font_size))
    q_count_label.grid(row=2, column=board_width + 2, columnspan=3, sticky="NESW")
    q_count_number = Label(board, text=str(specimen_to_print.get_score()), borderwidth=2, relief="groove",
                           font=("Courier", font_size))
    q_count_number.grid(row=3, column=board_width + 3, sticky="NESW")


def add_generation():
    # while True:
    create_generation(1000)
    create_gui(best_specimen)
    # if best_specimen.get_score() == 9:
    #     break
    create_board_gui(best_specimen)


# Barriers locations are stored as arrays of [x,y] starting from
# x and going to the board_width -1. If you enter a number higher
# than the width or height of the board, that barrier will not be placed
barrier_placement = []
button_width = 1
button_height = 1
font_size = 10

best_specimen = None
worst_specimen = None
board = Tk()
board_width = 8
board_height = 8
current_specimen_num = 0
queen_count = 0
num_collisions = 0
score = 0
queen_locations = []
barrier_locations = []
board_pieces = []
empty_spaces = []
current_generation = []
mutation_factor = 10
# generations = []
last_generation = None
generation_num = 0
total_score =  0
total_average_score = 0
while best_specimen is None or best_specimen.get_score() != 8:
    create_generation(100, intelligent=True)
create_gui(best_specimen)
create_board_gui(best_specimen)
board.mainloop()
