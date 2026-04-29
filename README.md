# AI Code Reviewer (Gemini + Python)

CLI project that reviews a single source file using Gemini and prints a structured report in the terminal.

## Features
- Reads a code file from disk
- Sends it to Gemini with a strict JSON schema
- Validates response with Pydantic
- Renders results with Rich panels/tables

## Project Structure
```text
.
|- analyzer.py      # Gemini request + schema-based parsing
|- schemas.py       # Pydantic response model
|- main.py          # CLI and Rich output
|- examples/        # sample files to analyze
```

## Requirements
- Python 3.10+
- Gemini API key

## Installation

```bash
python -m venv venv
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

pip install google-genai pydantic python-dotenv typer rich
```

## Environment
Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run
```bash
python main.py
```

When prompted, provide a file path, for example:
```text
examples/linear_search.py
```

## Response Schema
The model returns:
- `overall_quality_summary`
- `general_score` (1 to 5)
- `estimated_complexity` (Big O)
- `strengths`
- `issues`
- `improvements`

## Examples Folder
This repository includes 4 code samples:
- `examples/linear_search.py`
- `examples/two_sum_hashmap.py`
- `examples/search_in_sorted_array.py`
- `examples/bubble_sort.py`

Try them with:
```bash
python main.py
# then type one of:
# examples/linear_search.py
# examples/two_sum_hashmap.py
# examples/bubble_sort.py
```

