from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leggo_enna():
    return {"messaggio": "Ciao! Enea è online e funzionante 🔥"}
