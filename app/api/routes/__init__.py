from fastapi import APIRouter
from app.api.routes.health import router as health_router
from app.api.routes.select_llm import router as llm_selection_router
from app.api.routes.qa import router as get_answer_router

# This is the main router for the API, which includes all the sub-routers.
router = APIRouter()
router.include_router(health_router)
router.include_router(llm_selection_router)
router.include_router(get_answer_router)