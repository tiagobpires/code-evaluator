from pydantic import BaseModel, Field


class CodeReview(BaseModel):
    overall_quality_summary: str = Field(
        description="Short summary of the overall code quality"
    )
    general_score: int = Field(description="Overall score from 1 to 5")
    estimated_complexity: str = Field(
        description="Estimated time complexity in Big O notation, for example O(n) or O(n^2)"
    )
    strengths: list[str] = Field(description="Main strengths found in the code")
    issues: list[str] = Field(description="Main issues found in the code")
    improvements: list[str] = Field(
        description="Concrete suggestions to improve the code"
    )
