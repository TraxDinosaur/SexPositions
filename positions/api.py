import uvicorn
from fastapi import FastAPI, HTTPException
from .funcs import getSoup, getNumber, getName, getDescription, getImageUrl, getSimilar, getSft

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the Sex Positions API. Use /positions/{position} to get details about a position."}


@app.get("/positions/{position}")
def read_position(position: int):
    try:
        soup = getSoup(position)
        positionNumber = getNumber(soup)
        positionName = getName(soup)
        positionDescription = getDescription(soup)
        positionImageUrl = getImageUrl(soup)
        positionSimilar = getSimilar(soup)
        sft = getSft(soup)

        return {
            'position': positionNumber,
            'name': positionName,
            'description': positionDescription,
            'img_url': positionImageUrl,
            'similar': positionSimilar,
            'sft': sft
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Position {position} not found or an error occurred: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
