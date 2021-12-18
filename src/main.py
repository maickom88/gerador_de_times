import uvicorn

from src import init_app
from src.settings.environment import env

if __name__ == "__main__":
    app = init_app()
    uvicorn.run(app, host=env.api_host(),
                port=env.api_port(), debug=env.is_debug())
