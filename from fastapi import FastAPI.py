from fastapi import FastAPI

app = FastAPI()

@app.get("/my-first-api")
def hello(name = None):
    
    if name is None:
        text = 'hello!'
    
    else:
        text = 'hello ' + name + '!'
    
    return text        