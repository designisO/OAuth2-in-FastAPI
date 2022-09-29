## Authentication with FastAPI

A Simple example of how to authenticate using FastAPI framework using OAuth2RequestForm and OAuth2Password Bearer. Instead of Uvicorn I was able to use Hypercorn web server.

#### Http request methods: 
Define a set of request methods to indicate the desired action to be performed for a given resource. Request methods are sometimes referred to as HTTP verbs.
	GET: Retrieve Data
	HEAD: Asks for a response identical to a GET response, but without the response body
	POST: Submits an entity to the specified resource often change in state or side effects on the server.
	PUT: Replaces all current representations of the target resource with the request payload.
	DELETE: Deletes the specified resource.

#### Status Codes:
	ie: 200 means OK, 404 means Not Found (cannot find the requested resource)

#### Await / Async
	- ASGI Documentation: Intended to provide a standard interface between aync-capable Python web servers. (Concurrency and async / await) - docs on FastAPI.

#### Creating User Models:
	- using pydantic for models to gain data validation and settings management using python type annotations.
	-uuid provides a random id.
	- you can make the uuid a fixed id as well.

#### Creating a Database
	- creating a list in the main file

#### Creating an endpoint to register users
	- cannot submit post request in a browser. So you will need a REST client like (Thunder Client in VSCode extensions) or another way to interact with the client with interactive API documetation

#### Interactive API Documentation: 
	- Provided by Swagger gives an Interactive way to interact with the RestAPI.
	- Redoc : Just the API documentation, but it's not interactive.

#### To install:

pip install python-multipart
pip install fastapi, hypercorn

To run: hypercorn <.py file>:app --reload

Docs : https://fastapi.tiangolo.com/tutorial/security/.

OAuth2PasswordBearer & OAuth2PasswordRequestForm: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
