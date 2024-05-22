from fastapi import FastAPI

from db import Base, engine


def createAPI():
	app = FastAPI()
	Base.metadata.create_all(bind=engine)
	return app
