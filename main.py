from fastapi import FastAPI

app=FastAPI()

def home():
    return{
        "message":"welcome to home page"
    }
@app.get("/home")
def get_user():
    return{
        "name":"foram",
        "role":"it"
    },
    {
        "name":"noidhi",
        "role":it
    }

@app.get("/about")
def home():
    return{
       "message":"about page...."
    }

##pip freeze > requirements.txt

 ##pip install fastapi[standard] python-dotenv