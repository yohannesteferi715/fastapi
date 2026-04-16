from fastapi import FastAPI


app=FastAPI()

@app.get("/api-endpoint")
async def first_api():
    return (
        
        {
            "msg":"hello yoni"
        }
    )

