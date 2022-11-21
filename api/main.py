from fastapi import FastAPI
from pydantic import BaseModel
from database.query import query_get, query_put


app = FastAPI()

@app.get("/")
async def root():
    return {"Welcom to our API": "This API deals with accident data."}


@app.get("/show-all")
def get_all():
    accident = query_get("""
        SELECT * FROM accidents;
        """,())
    return {"All accidents " : accident}


def get_at_row(row: int):
    accident = query_get(
    """
        SELECT * FROM accidents 
        LIMIT %s , 1
    """,(row-1))
    return {"Random accidents data " : accident}



@app.get("/get-by-date/{date}")
def get_by_date(date: str):
    accident = query_get( 
    """ 
        SELECT * FROM `accidents` WHERE accident_date = %s
        
    """, (date) )
    messages = "All accidents occurred on " + str(date)
    return { messages  : accident }
