import io

from fastapi import FastAPI, Response, Query
from fastapi.middleware.cors import CORSMiddleware
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


@app.get("/wordsearch/")
async def create_wordsearchs(
    difficulty: Difficulty,
    is_uppercase: bool,
    is_hint_twist: bool,
    words: list[str] | None = Query(default=None),
):
    difficulty_option = DifficultyOption(difficulty)
    # words = [word.name for word in wordsearch_model.words]
    print(words)
    puzzle_data = PuzzleData(
        words,
        difficulty_option,
        is_uppercase,
        is_hint_twist,
    )
    puzzle_data.make()
    worksheet = Worksheet(puzzle_data)
    worksheet.write()
    worksheet.write_answer()
    bio = io.BytesIO()

    worksheet.save(bio)
    bio.seek(0)
    response = Response(
        bio.getvalue(),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": "attachment;",
            "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "Access-Control-Expose-Headers": "Content-Disposition",
        },
    )

    return response
