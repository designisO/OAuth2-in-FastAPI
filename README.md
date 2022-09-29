## Authentication with FastAPI

A Simple example of how to authenticate using FastAPI framework using OAuth2RequestForm and OAuth2Password Bearer. Instead of Uvicorn I was able to use Hypercorn web server.

##### To install:

pip install python-multipart
pip install fastapi, hypercorn

To run: hypercorn <.py file>:app --reload

Docs : https://fastapi.tiangolo.com/tutorial/security/.

OAuth2PasswordBearer & OAuth2PasswordRequestForm: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
