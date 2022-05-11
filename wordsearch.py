import copy
import json
import os
import random
from statistics import mean

import hgtk
import requests
from bs4 import BeautifulSoup
import re
import string
from enum import Enum
from pathlib import Path
from pprint import pprint
from random import randint, shuffle

from docx import Document
from docx.dml.color import ColorFormat
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor


class Direction(Enum):
    FORWARD = 1
    STEADY = 2
    BACKWARD = 3


class Puzzle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.puzzle = [[0 for _ in range(width)] for _ in range(height)]
        self.words = list()

    def enter(self, words):
        self.words = words
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

        self.answer = copy.deepcopy(self.puzzle)
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
        self.x_direction = Direction.FORWARD  # random.choice(list(Direction))
        self.y_direction = Direction.STEADY  # random.choice(list(Direction))


class Language(Enum):
    KOREAN = 1
    ENGLISH = 2


class Worksheet:
    def __init__(self, lang: Language = Language.ENGLISH):
        self.lang = lang
        self.heading = "Word Puzzle"
        if lang == Language.KOREAN:
            self.heading = "낱말 찾기"
        self.uppercase = True
        self.chosung_scramable = True

    def configure_settings(self, puzzle_data: Puzzle):
        self.width = puzzle_data.width
        self.height = puzzle_data.height
        self.puzzle = puzzle_data.puzzle
        self.answer = puzzle_data.answer

        # write to docx file
        # Write to docx to puzzle.docx
        self.document = Document()
        # changing the page margins
        sections = self.document.sections
        for section in sections:
            section.top_margin = Cm(1)
            section.bottom_margin = Cm(0.8)
            section.left_margin = Cm(2.3)
            section.right_margin = Cm(2.3)

        self.grade: int = "__"
        self.class_num: int = "__"

    def add_heading(self):
        head = self.document.add_heading(self.heading, 0)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para_belong = self.document.add_paragraph(
            f"{self.grade}학년 {self.class_num}반 이름: _______"
        )
        para_belong.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    def add_puzzle(self):
        puzzle_table = self.document.add_table(
            rows=self.height, cols=self.width, style="Table Grid"
        )
        puzzle_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        self.set_height = 7200 / self.height
        for i, row in enumerate(puzzle_table.rows):
            #######################세로 길이 정하기!
            # accessing row xml and setting tr height
            tr = row._tr
            trPr = tr.get_or_add_trPr()
            trHeight = OxmlElement("w:trHeight")
            trHeight.set(qn("w:val"), str(self.set_height))
            trHeight.set(qn("w:hRule"), "atLeast")
            trPr.append(trHeight)

            for j, cell in enumerate(row.cells):
                #####가로 길이 정하기!
                cell.width = Inches(5)
                cell.text = self.get_text_from_puzzle(self.puzzle, i, j)
                for paragraph in cell.paragraphs:
                    #####가운데 정렬!!
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    paragraph.style.font.bold = True
                #####상하 방향에서 가운데 정렬
                tc = cell._tc
                tcPr = tc.get_or_add_tcPr()
                tcVAlign = OxmlElement("w:vAlign")
                tcVAlign.set(qn("w:val"), "center")
                tcPr.append(tcVAlign)

    def get_text_from_puzzle(self, puzzle, i, j):
        if self.uppercase and self.lang == Language.ENGLISH:
            return str(puzzle[i][j]).upper()
        else:
            return str(puzzle[i][j])

    def add_hint(self):
        # 힌트 테이블 만들기
        # 사진이 안 들어가고 영어인 경우
        if self.lang == Language.ENGLISH:
            hint_table = self.document.add_table(rows=1, cols=1, style="Table Grid")
            hint_table.alignment = WD_TABLE_ALIGNMENT.CENTER
            hint_table_row = hint_table.rows[0]
            hint_tr = hint_table_row._tr
            hint_trPr = hint_tr.get_or_add_trPr()
            hint_trHeight = OxmlElement("w:trHeight")
            hint_trHeight.set(qn("w:val"), "1000")
            hint_trHeight.set(qn("w:hRule"), "atLeast")
            hint_trPr.append(hint_trHeight)
            hint_table_cell = hint_table_row.cells[0]
            hint = ""

            for word in words:
                if self.uppercase:
                    word = word.upper()
                if self.chosung_scramable:
                    spelling = [i for i in word]
                    shuffle(spelling)
                    word = "".join(spelling)
                hint += word + ", "
            hint_table_cell.width = Inches(100)
            for paragraph in hint_table_cell.paragraphs:
                paragraph.add_run(hint.strip(", "))
                paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            tc = hint_table_cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcVAlign = OxmlElement("w:vAlign")
            tcVAlign.set(qn("w:val"), "center")
            tcPr.append(tcVAlign)

        else:
            # 사진이 안 들어가고 한글인 경우
            if self.chosung_scramable:
                hint_table = self.document.add_table(rows=1, cols=1, style="Table Grid")
                hint_table.alignment = WD_TABLE_ALIGNMENT.CENTER
                hint_table_row = hint_table.rows[0]
                hint_tr = hint_table_row._tr
                hint_trPr = hint_tr.get_or_add_trPr()
                hint_trHeight = OxmlElement("w:trHeight")
                hint_trHeight.set(qn("w:val"), "1000")
                hint_trHeight.set(qn("w:hRule"), "atLeast")
                hint_trPr.append(hint_trHeight)
                hint_table_cell = hint_table_row.cells[0]
                hint = ""
                for word in words:
                    cho_word = ""
                    for chr in word:
                        chosung_scramable = hgtk.letter.decompose(chr)[0]
                        cho_word += chosung_scramable
                    hint += cho_word + ", "
                hint_table_cell.width = Inches(100)
                for paragraph in hint_table_cell.paragraphs:
                    paragraph.add_run(hint.strip(", "))
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                tc = hint_table_cell._tc
                tcPr = tc.get_or_add_tcPr()
                tcVAlign = OxmlElement("w:vAlign")
                tcVAlign.set(qn("w:val"), "center")
                tcPr.append(tcVAlign)
            else:
                hint_table = self.document.add_table(rows=1, cols=1, style="Table Grid")
                hint_table.alignment = WD_TABLE_ALIGNMENT.CENTER
                hint_table_row = hint_table.rows[0]
                hint_tr = hint_table_row._tr
                hint_trPr = hint_tr.get_or_add_trPr()
                hint_trHeight = OxmlElement("w:trHeight")
                hint_trHeight.set(qn("w:val"), "1000")
                hint_trHeight.set(qn("w:hRule"), "atLeast")
                hint_trPr.append(hint_trHeight)
                hint_table_cell = hint_table_row.cells[0]
                hint = ""
                for word in words:
                    hint += word + ", "
                hint_table_cell.width = Inches(100)
                for paragraph in hint_table_cell.paragraphs:
                    paragraph.add_run(hint.strip(", "))
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                tc = hint_table_cell._tc
                tcPr = tc.get_or_add_tcPr()
                tcVAlign = OxmlElement("w:vAlign")
                tcVAlign.set(qn("w:val"), "center")
                tcPr.append(tcVAlign)

    def write(self):
        self.add_heading()
        self.add_puzzle()
        self.add_hint()

    def write_answer(self, puzzle_data: Puzzle):
        width = puzzle_data.width
        height = puzzle_data.height
        puzzle = puzzle_data.answer
        print(puzzle)

        # 정답 파일 쓰기
        self.answ_doc = Document()
        answer_table = self.answ_doc.add_table(
            rows=height, cols=width, style="Table Grid"
        )
        answer_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, row in enumerate(answer_table.rows):
            #######################세로 길이 정하기!
            # accessing row xml and setting tr height
            tr = row._tr
            trPr = tr.get_or_add_trPr()
            trHeight = OxmlElement("w:trHeight")
            trHeight.set(qn("w:val"), str(self.set_height))
            trHeight.set(qn("w:hRule"), "atLeast")
            trPr.append(trHeight)

            for j, cell in enumerate(row.cells):
                #####가로 길이 정하기!
                cell.width = Inches(8)
                cell.text = self.get_text_from_puzzle(self.answer, i, j)
                for paragraph in cell.paragraphs:
                    #####가운데 정렬!!
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    paragraph.style.font.bold = True
                    if cell.text == "0":
                        for run in paragraph.runs:
                            run.font.color.rgb = RGBColor(255, 255, 255)
                    else:
                        for run in paragraph.runs:
                            run.font.color.rgb = RGBColor(255, 0, 0)
                #####상하 방향에서 가운데 정렬
                tc = cell._tc
                tcPr = tc.get_or_add_tcPr()
                tcVAlign = OxmlElement("w:vAlign")
                tcVAlign.set(qn("w:val"), "center")
                tcPr.append(tcVAlign)

    def save(self, filename):
        self.answ_doc.save("./{}_정답.docx".format(filename))
        self.document.save("./{}.docx".format(filename))


if __name__ == "__main__":
    puzzle = Puzzle(20, 20)
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
    worksheet.configure_settings(puzzle)
    worksheet.write()
    worksheet.write_answer(puzzle)
    worksheet.save("filename")

    # document = Document()
    # document.save("test.docx")
