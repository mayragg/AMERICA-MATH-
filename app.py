from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

CONVERSIONS = {
    "football_field": {
        "type": "area",
        "value_m2": 5351,
        "description": "American football field (with end zones)"
    }
}

class ConversionRequest(BaseModel):
    value: float
    unit_type: str  # e.g., "area", "population"

@app.post("/convert")
def convert(request: ConversionRequest):
    results = []
    for name, data in CONVERSIONS.items():
        if data["type"] == request.unit_type:
            count = request.value / data["value_m2"]
            results.append({
                "equivalent": name,
                "count": round(count, 2),
                "description": data["description"]
            })
    return {"results": results}