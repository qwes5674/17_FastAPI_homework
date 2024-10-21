from pydantic import BaseModel, validator

class CalculationRequest(BaseModel):
    num1: int
    num2: int
    operator: str

    # 유효성 검사
    @validator('operator')
    def validate_operator(cls, v):
        if v not in ['+', '-', '*', '%']:
            # 유효하지 않으면 예외처리 
            raise ValueError("Operator must be one of '+', '-', '*', '%'")
        return v

class SquareRequest(BaseModel):
    number: int

class SquareRootRequest(BaseModel):
    number: int