import time
import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds' , 'https://www.googleapis.com/auth/drive' ]
credentials = ServiceAccountCredentials.from_json_keyfile_name('Loods5-d71de8db7c29.json', scope)
gc = gspread.authorize(credentials)

x  = datetime.datetime.utcnow().isocalendar()[1]
now = datetime.datetime.now()
y = str(now.date())

G = str(("Week:",x,now.strftime("%A"),y,"domein6"))
sh = gc.create(str(G))
sh.share('513442@lln.corlaercollege.nl', perm_type='user', role='writer', email_message='False')
# Voeg link bij voor accces
# sh.share('rkoppelaar@corlaercollege.nl', perm_type='user', role='writer', email_message='False')
# blijkbaar limiet van 50 / dag

def sheets_aanmaken():
    # Kan helaas echt niet makkelijker of beter
    worksheet1uur = sh.add_worksheet(title="Domein 6: 1e uur", rows="60", cols="20")
    worksheet2uur = sh.add_worksheet(title="Domein 6: 2e uur", rows="60", cols="20")
    worksheet3uur = sh.add_worksheet(title="Domein 6: 3e uur", rows="60", cols="20")
    worksheet4uur = sh.add_worksheet(title="Domein 6: 4e uur", rows="60", cols="20")
    worksheet5uur = sh.add_worksheet(title="Domein 6: 5e uur", rows="60", cols="20")
    worksheet6uur = sh.add_worksheet(title="Domein 6: 6e uur", rows="60", cols="20")
    worksheet7uur = sh.add_worksheet(title="Domein 6: 7e uur", rows="60", cols="20")
    worksheet1uur.update_acell('A1', '1e uur')
    worksheet1uur.update_acell('A2', 'Voornaam_Achternaam')
    worksheet1uur.update_acell('B2', 'Klas')
    worksheet1uur.update_acell('C2', 'Present')
    worksheet1uur.update_acell('D2', 'Ziek')

    worksheet2uur.update_acell('A1', '2e uur')
    worksheet2uur.update_acell('A2', 'Voornaam_Achternaam')
    worksheet2uur.update_acell('B2', 'Klas')
    worksheet2uur.update_acell('C2', 'Present')
    worksheet2uur.update_acell('D2', 'Ziek')

    worksheet3uur.update_acell('A1', '3e uur')
    worksheet3uur.update_acell('A2', 'Voornaam_Achternaam')
    worksheet3uur.update_acell('B2', 'Klas')
    worksheet3uur.update_acell('C2', 'Present')
    worksheet3uur.update_acell('D2', 'Ziek')

    worksheet4uur.update_acell('A1', '4e uur')
    worksheet4uur.update_acell('A2', 'Voornaam_Achternaam')
    worksheet4uur.update_acell('B2', 'Klas')
    worksheet4uur.update_acell('C2', 'Present')
    worksheet4uur.update_acell('D2', 'Ziek')

    worksheet5uur.update_acell('A1', '5e uur')
    worksheet5uur.update_acell('A2', 'Voornaam_Achternaam')
    worksheet5uur.update_acell('B2', 'Klas')
    worksheet5uur.update_acell('C2', 'Present')
    worksheet5uur.update_acell('D2', 'Ziek')

    worksheet6uur.update_acell('A1', '6e uur')
    worksheet6uur.update_acell('A2', 'Voornaam_Achternaam')
    worksheet6uur.update_acell('B2', 'Klas')
    worksheet6uur.update_acell('C2', 'Present')
    worksheet6uur.update_acell('D2', 'Ziek')

    worksheet7uur.update_acell('A1', '7e uur')
    worksheet7uur.update_acell('A2', 'Voornaam_Achternaam')
    worksheet7uur.update_acell('B2', 'Klas')
    worksheet7uur.update_acell('C2', 'Present')
    worksheet7uur.update_acell('D2', 'Ziek')
sheets_aanmaken()

