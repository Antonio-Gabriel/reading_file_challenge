import unittest

from uvicorn import run
from fastapi import FastAPI, Form, Request, File, UploadFile

from fastapi.templating import Jinja2Templates

from mapper.MappingDataFromFile import MappingDataFromFile
from system.WriteDataFromLocalFile import WriteDataFromLocalFile
from system.SaveBulkDataFileToDatabase import SaveBulkDataFileToDatabase

app = FastAPI()

templates = Jinja2Templates(directory="views")


@app.get("/")
def index(request: Request):
    """Show the index page to upload file"""

    return templates.TemplateResponse(
        "index.html", {"request": request, "username": "Atónio Gabriel"}
    )


@app.post("/upload-file")
async def handle_form(
    request: Request, tablename: str = Form(...), file: UploadFile = File(...)
):
    """endpoint for reading file data"""

    content_file = await file.read()

    write_in_file = WriteDataFromLocalFile()
    write_in_file.write(content_file.decode())

    create_dynamic_bulk_attr = SaveBulkDataFileToDatabase(
        tablename, MappingDataFromFile()
    )

    save_result = create_dynamic_bulk_attr.save_bulk_data_attr()

    print("\n")
    return save_result


if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8080)
    # unittest.main()
