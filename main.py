from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# Generating a token for authentication
# Creating the endpoint to the token for authentication
# Will attach data placed in the form.
@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}

# once the authenticaion occurs, then the scheme happens
# creating another endpoint depending on the OAuth2 scheme. 
# If the token is available, then it will push 200 OK.
@app.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {'the_token': token}

