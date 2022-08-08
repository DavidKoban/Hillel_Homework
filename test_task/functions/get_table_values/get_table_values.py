import decimal
from googleapiclient.discovery import build
from google.oauth2 import service_account


def get_table_values():
    SERVICE_ACCOUNT_FILE = 'test_task/functions/get_table_values/keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    SAMPLE_SPREADSHEET_ID = '10J-A-B-RAYCQgm4ZOqUnOGVo-PBY29vZrOUI1DvULL0'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range='list1!A2:D').execute()
    values = result.get('values', ())
    value_list_of_dicts = []
    for i in values:
        value_dict = {'table_id': int(i[0]),
                      'order_number': int(i[1]),
                      'cost_usd': decimal.Decimal(i[2]),
                      'delivery_time': i[3],
                    }
        value_list_of_dicts.append(value_dict)
    return value_list_of_dicts
