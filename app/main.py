from app.api import createAPI


app = createAPI()


@app.get('/')
async def helloworld():
	return {'message': 'hello world'}
