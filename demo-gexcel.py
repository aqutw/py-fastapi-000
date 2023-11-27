import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

Json = "celtic-sunlight-406403-355cac21e116.json"
Url = ["https://spreadsheets.google.com/feeds"]
Connect = SAC.from_json_keyfile_name(Json)
GoogleSheets = gspread.authorize(Connect)
Sheet = GoogleSheets.open_by_key("1IDAJHxjL4LJ0-F_gjxEX_UpIC_f8-PL3OWK3NmYPuKo")
Sheets = Sheet.sheet1
dataTitle = ["name", "account", "password"]
datas = ["Alex", "qaz", "111"]
Sheets.append_row(dataTitle)
Sheets.append_row(datas)
print("寫入成功")
print(Sheets.get_all_values())

