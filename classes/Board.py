from tkinter import *


class Board:
    def __init__(self, specimen, num_queens, collisions, specimen_score, layout, queen_positions, barrier_positions,
                 empty_cells):
        self.specimen = specimen
        self.num_queens = num_queens
        self.collisions = collisions
        self.specimen_score = specimen_score
        self.layout = layout
        self.queen_locations = queen_positions
        self.barrier_locations = barrier_positions
        self.empty_cells = empty_cells

    def get_score(self):
        return self.specimen_score

    def get_specimen(self):
        return self.specimen

    def get_barrier_locations(self):
        return self.barrier_locations

    def get_queen_locations(self):
        return self.queen_locations

    def get_empty_cells(self):
        return self.empty_cells

    def get_layout(self):
        return self.layout

    def print_list_to_gui(self, board, cells, text="", background="SystemButtonFace"):
        for cell in cells:
            tile_button = Button(board,
                                 width=1,
                                 height=1,
                                 text=text,
                                 borderwidth=2,
                                 relief="groove",
                                 font=("Courier", 16),
                                 bg=background,
                                 command="")
            tile_button.grid(row=cell[1], column=cell[0])

    def print_layout_to_console(self, layout):
        for y in range(0, len(layout)):
            for x in range(0, len(layout[0])):
                if layout[x][y].get_queen():
                    print("Q", end="")
                elif layout[x][y].get_barrier():
                    print("B",end="")
                else:
                    print("_",end="")
            print()

    def print_board_to_gui(self, board, layout):
        if len(self.empty_cells) != 0:
            self.print_list_to_gui(board, self.empty_cells)
            self.print_list_to_gui(board, self.barrier_locations, text="B", background="Red")
            self.print_list_to_gui(board, self.queen_locations, text="♕")
        else:
            for y in range(0, len(layout)):
                for x in range(0,len(layout[0])):
                    for x in range(0, len(layout[0])):
                        if layout[x][y].get_queen():
                            text = "♕"
                            background = "white"
                        elif layout[x][y].get_barrier():
                            text = "B"
                            background = "Red"
                        else:
                            text = ""
                            background = "white"
                        tile_button = Button(board,
                                             width=1,
                                             height=1,
                                             text=text,
                                             borderwidth=2,
                                             relief="groove",
                                             font=("Courier", 16),
                                             bg=background,
                                             command="")
                        tile_button.grid(row=y, column=x)


        print("Printed Specimen")

