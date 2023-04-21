# run.py
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import uvicorn

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
