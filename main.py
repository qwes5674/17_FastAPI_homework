from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models import CalculationRequest, SquareRequest, SquareRootRequest
from calculator import calculate

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # index template 랜더링
    return templates.TemplateResponse("index.html", {"request": request})

# 계산
@app.post("/calculate")
async def perform_calculation(request: CalculationRequest):
    try:
        result = calculate(request.num1, request.num2, request.operator)
        return {"result": result}
    # 계산중 오류 발생
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# 제곱 
@app.post("/square")
async def calculate_square(request: SquareRequest):
    return {"result": request.number ** 2}

# 제곱근
@app.post("/sqrt")
async def calculate_square_root(request: SquareRootRequest):
    if request.number < 0:
        raise HTTPException(status_code=400, detail="Cannot calculate square root of negative number")
    return {"result": request.number ** 0.5}