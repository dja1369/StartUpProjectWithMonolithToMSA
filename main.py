import uvicorn
from service.container import get_container, inject_route
from service.route import route

if __name__ == '__main__':
    app = get_container()
    app = inject_route(app, route)
    uvicorn.run(
        app, host="0.0.0.0", port=8000
    )
