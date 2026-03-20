import fastapi

app = fastapi.FastAPI()

@app.get("/")
def root():
    return {'status': 'ok', 'message': 'Mini Celery is running'}