from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}

class WeatherRequest(BaseModel):
    city: str


@app.post("/weather")
async def weather(req: WeatherRequest):

    async with httpx.AsyncClient() as client:

        r = await client.get(
            f"https://wttr.in/{req.city}?format=j1"
        )

        data = r.json()

    return {
        "city": req.city,
        "temp": data["current_condition"][0]["temp_C"]
    }
