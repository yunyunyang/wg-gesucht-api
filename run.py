import sys
import os
import uvicorn

# Add the root directory to sys.path to access static folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


if __name__ == '__main__':

    uvicorn.run(
        "src.main:app", 
        host    = "127.0.0.1", 
        port    = 8000, 
        reload  = True
    )