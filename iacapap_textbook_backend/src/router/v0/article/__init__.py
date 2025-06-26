from .router import router

# from .caption import router as caption_router
# router.include_router(caption_router, prefix="/{article_id}/caption", tags=["CAPTION"])

from .image import router as image_router

router.include_router(image_router, prefix="/image", tags=["IMAGE"])
