import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/test-gspread")
def test_gspread():
  Json = "celtic-sunlight-406403-355cac21e116.json"
  Connect = SAC.from_json_keyfile_name(Json)
  GoogleSheets = gspread.authorize(Connect)
  Sheet = GoogleSheets.open_by_key(
      "1IDAJHxjL4LJ0-F_gjxEX_UpIC_f8-PL3OWK3NmYPuKo")
  Sheets = Sheet.sheet1
  return Sheets.get_all_records();
