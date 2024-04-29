from routing import *
from uvicorn import run

def main():
    app = fastapi.FastAPI()
    app.include_router(Router().router)

    run(app)

if __name__ == "__main__":
    main()