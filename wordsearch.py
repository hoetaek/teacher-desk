from random import randint
import random
import string
import copy
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx import Document
from docx.shared import Cm, Inches, RGBColor, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.dml.color import ColorFormat

# import hgtk
# import requests
# from bs4 import BeautifulSoup
import re
import os
from pathlib import Path
from random import shuffle
import json
from enum import Enum


class Direction(Enum):
    FORWARD = 1
    STEADY = 2
    BACKWARD = 3


class Puzzle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.puzzle = [[0 for _ in range(width)] for _ in range(height)]

    def enter(self, words):
        for word in words:
            word_enter_succeed = False
            print(word)

            try_num = 0
            max_try = 30
            while not word_enter_succeed:
                print(try_num)
                puzzle_option = PuzzleOption()
                puzzle_option.get_option()
                word_positions = WordPosition(word).get_word_positions(
                    self.width,
                    self.height,
                    len(word),
                    puzzle_option.x_direction,
                    puzzle_option.y_direction,
                )
                word_enter_succeed = self.fill_word(word, word_positions)
                try_num += 1
                if try_num > max_try:
                    self.__empty_puzzle()
                    self.enter(words)

        self.fill_random_letters()
        [print(i) for i in self.puzzle]

    def fill_word(self, word, word_positions):
        if self.word_position_exists(word, word_positions):
            x_y_seperated_positions = list(zip(*word_positions))
            for letter, x, y in zip(word, *x_y_seperated_positions):
                self.puzzle[y][x] = letter
            return True
        else:
            return False

    def fill_random_letters(self):
        for i in range(self.height):
            for j in range(self.width):
                fill_alph = random.choice(string.ascii_lowercase)
                fill_alph = "0"
                if self.puzzle[i][j] == 0:
                    self.puzzle[i][j] = fill_alph

    def word_position_exists(self, word, word_positions):
        word_zero = "0" * len(word)
        word_in_puzzle = ""
        for x, y in word_positions:
            word_in_puzzle += str(self.puzzle[y][x])
        if word_zero == word_in_puzzle:
            return True
        else:
            for i in range(len(word)):
                if word_in_puzzle[i] != word[i] and word_in_puzzle[i] != "0":
                    return False
            return True

    def __empty_puzzle(self):
        self.puzzle = [[0 for _ in range(self.width)] for _ in range(self.height)]


class WordPosition:
    def __init__(self, word):
        self.word = word

    def __get_positions(
        self, total_length: int, word_length: int, direction: Direction
    ):
        match direction:
            case Direction.FORWARD:
                start_position = randint(0, total_length - word_length)
                positions = [
                    i for i in range(start_position, start_position + word_length)
                ]
            case Direction.STEADY:
                start_position = randint(1, total_length) - 1
                positions = [start_position for _ in range(word_length)]
            case Direction.BACKWARD:
                start_position = randint(word_length, total_length - 1)
                positions = [
                    i for i in range(start_position, start_position - word_length, -1)
                ]
        print(positions)
        return positions

    def get_word_positions(
        self, width, height, word_length, x_direction: Direction, y_direction: Direction
    ):
        word_positions = list(
            zip(
                self.__get_positions(width, word_length, x_direction),
                self.__get_positions(height, word_length, y_direction),
            )
        )
        return word_positions


class PuzzleOption:
    def __init__(self) -> None:
        pass

    def get_option(self):
        self.x_direction = random.choice(list(Direction))
        self.y_direction = random.choice(list(Direction))


if __name__ == "__main__":
    from pprint import pprint

    puzzle = Puzzle(14, 14)
    words = [
        "hello",
        "python",
        "anything",
        "else",
        "witch",
        "campaign",
        "creed",
        "law",
        "small",
        "kidney",
        "basin",
        "theory",
        "refer",
        "cow",
        "twin",
        "quality",
        "wording",
        "punch",
        "perfume",
        "hemisphere",
        "training",
        "triangle",
        "opera",
        "gravity",
    ]

    puzzle.enter(words)
    worksheet = Worksheet()
    # worksheet.write(puzzle)
    # worksheet.save("filename.docx")

    # document = Document()
    # document.save("test.docx")
