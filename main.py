import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
# from ML import obtain_image
from fastapi.responses import FileResponse

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    tags: list[str] = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return{"item-id":item_id, "message":"Hello World from read_item with item param"}

@app.post("/items/")
def create_item(item: Item):
    return item

# @app.get("/generate")
# def generate_image(prompt: str):
#    image = obtain_image(prompt, num_inference_steps=5, seed = 100)
#    image.save("image.png")

#    #return {"prompt": prompt}

if __name__ == '__main__':
    uvicorn.run('main:app')