import io
from enum import Enum

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel

from helper.wordsearch.difficulty_option import Difficulty
from helper.wordsearch.utils import DifficultyOption, PuzzleData, Worksheet


class Word(BaseModel):
    name: str


class WordSearchModel(BaseModel):
    difficulty: Difficulty
    is_uppercase: bool = False
    is_hint_twist: bool = False
    words: list[Word]


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/wordsearch/")
async def create_wordsearchs(wordsearch_model: WordSearchModel):
    difficulty_option = DifficultyOption(wordsearch_model.difficulty)
    words = [word.name for word in wordsearch_model.words]

    puzzle_data = PuzzleData(
        words,
        difficulty_option,
        wordsearch_model.is_uppercase,
        wordsearch_model.is_hint_twist,
    )
    puzzle_data.make()
    worksheet = Worksheet(puzzle_data)
    worksheet.write()
    worksheet.write_answer()
    bio = io.BytesIO()

    # response = JSONResponse(
    #     "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    # )
    # response["Content-Disposition"] = "attachment; filename=download.docx"
    worksheet.save(bio)
    bio.seek(0)
    response = Response(
        bio.getvalue(),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": "attachment;filename=download.hwp",
        },
    )

    return response
