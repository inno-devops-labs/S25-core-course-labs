from src.routes.moscow_time import router as time_router
from src.routes.visits import router as visits_router

ALL_ROUTERS = [
    time_router,
    visits_router
]

__all__ = [
    ALL_ROUTERS
]
