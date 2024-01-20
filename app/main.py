from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import json

app = FastAPI()

@app.get("/hello/")
async def say_hello():
    return {"hey": "hello"}

@app.get("/testfile/")
async def say_hello():
    f = open("/logs/demofile2.txt", "w")
    f.write("Now the file has more content!")
    f.close()
    return {"hey": "test"}


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(zone_list: str, file: UploadFile = File(...)):
    print (zone_list)
    return {"filename": file.filename}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    info = {"filenames": [file.filename for file in files]}
    for file in files:
        print (file)
        if file.filename.__contains__('.json'):
            data = await file.read()
            json_data = json.loads (data)
            print (json_data)
    return info