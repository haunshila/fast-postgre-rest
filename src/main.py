import uvicorn

host = "0.0.0.0"
port = 8002
app_name = "src.app.main:app"

if __name__ == '__main__':
    uvicorn.run(app_name, host=host, port=port)
