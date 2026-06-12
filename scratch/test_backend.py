
import sys
try:
    print("Testing imports...", flush=True)
    import fastapi
    print("FastAPI ok", flush=True)
    import uvicorn
    print("Uvicorn ok", flush=True)
    import google.generativeai
    print("Google GenAI ok", flush=True)
    
    print("Attempting to import SQLEngine...", flush=True)
    from backend.sql_engine import SQLEngine
    print("SQLEngine import ok", flush=True)
    
    print("Attempting to instantiate SQLEngine...", flush=True)
    engine = SQLEngine()
    print("SQLEngine instantiation ok", flush=True)

    print("Attempting to import app...", flush=True)
    from backend.main import app
    print("Backend Main ok", flush=True)
except Exception as e:
    print(f"Error: {e}", flush=True)
    import traceback
    traceback.print_exc()
