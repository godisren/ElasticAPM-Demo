from fastapi import FastAPI  
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

apm = make_apm_client({
    'SERVICE_NAME': 'app-demo-python',
    'SECRET_TOKEN': 'set_your_secret_key_for_APM_server',
    'SERVER_URL': 'http://localhost:8200',
})
app = FastAPI()   
app.add_middleware(ElasticAPM, client=apm)

@app.get("/") 
async def main_route():     
  return "This is python application for APM integration demo"

@app.get("/user")
def get_some_info():
    return {"user_id": 1, "name": "Nancy", "gender":"female", "email":"nancy@cc.haha.com"}