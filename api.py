import google.generativeai as palm
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

palm.configure(api_key="AIzaSyDle7O_DyAArPcSjFP-jH9a-Q4yJNnq8Qk")
models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]
model = models[0].name

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/api/categorize")
def categorize_item(item):
    category = palm.generate_text(
        model=model,
        prompt=f"Categorize {item} in one of the categories. The list of categories is as follows: Food, Grocery, Medical, Education, Entertainment, Rent, Sports/Fitness. Give result as just the name of the category.",
        temperature=0,
        max_output_tokens=800,
    )
    return {'category': category.result}
