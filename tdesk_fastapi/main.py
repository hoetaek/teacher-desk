import io

from fastapi import Depends, FastAPI, Response, Query
from fastapi.middleware.cors import CORSMiddleware

from helper.wordsearch.difficulty_option import Difficulty
from helper.wordsearch.utils import DifficultyOption, PuzzleData, Worksheet


class WordSearchParams:
    def __init__(self, difficulty: Difficulty,
    is_uppercase: bool,
    is_hint_twist: bool,
    words: list[str] | None = Query(default=None)):
        self.difficulty = difficulty
        self.is_uppercase = is_uppercase
        self.is_hint_twist = is_hint_twist
        self.words = words

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
    wordsearch : WordSearchParams = Depends(WordSearchParams),
):
    difficulty_option = DifficultyOption(wordsearch.difficulty)
    print(wordsearch.words)
    puzzle_data = PuzzleData(
        wordsearch.words,
        difficulty_option,
        wordsearch.is_uppercase,
        wordsearch.is_hint_twist,
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
