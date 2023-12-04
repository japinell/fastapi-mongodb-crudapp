# Import statement
from fastapi import FastAPI
from routes.user import user_router

# Create app
app = FastAPI()

# Register the router
app.include_router(user_router)