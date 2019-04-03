import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Waar wil ik toegang tot
scope = ['https://spreadsheets.google.com/feeds' , 'https://www.googleapis.com/auth/drive' ]
credentials = ServiceAccountCredentials.from_json_keyfile_name('Loods5-d71de8db7c29.json', scope)
gc = gspread.authorize(credentials)


worksheet = gc.open('Leerlingen_data').sheet1
laatste_leerling_ID = worksheet.col_values(1)
beschikbaar_lln_id = ( int(laatste_leerling_ID[-1]) + 3 )


lln = str(input("Geeft de volledige naam en achter van de leerling,\nwaarvan je de domein_uren wilt zien: "))




def enkele_lln():
        cell_list = worksheet.findall(lln)
        x = str(cell_list)
        # Zoekt naar de naam en geeft het de row en colom van die cell: in dit geval
        y = x[8]
        alle_waardes_rij_van_lln = worksheet.row_values(y)
        Leerling_ID = (alle_waardes_rij_van_lln[0])
        values_list = worksheet.row_values(Leerling_ID)
        print(values_list[2],"heeft zelfstudie op: ")
        ding = [i for i, x in enumerate(values_list) if x == 'Zelfstudie']
        x = []
        for z in ding:
            if (int(z)) == int(4):
                dag = ('Ma_1')
                x.extend([dag])
            elif (int(z)) == int(5):
                dag = ('Ma_2')
                x.extend([dag])
            elif (int(z)) == int(6):
                dag = ('Ma_3')
                x.extend([dag])
            elif (int(z)) == int(7):
                dag = ('Ma_4')
                x.extend([dag])
            elif (int(z)) == int(8):
                dag = ('Ma_5')
                x.extend([dag])
            elif (int(z)) == int(9):
                dag = ('Ma_6')
                x.extend([dag])
            elif (int(z)) == int(10):
                dag = ('Ma_7')
                x.extend([dag])
            elif (int(z)) == int(11):
                dag = ('Di_1')
                x.extend([dag])
            elif (int(z)) == int(12):
                dag = ('Di_2')
                x.extend([dag])
            elif (int(z)) == int(14):
                dag = ('Ma_14')
                x.extend([dag])
            elif (int(z)) == int(15):
                dag = ('Ma_15')
        print(x)
enkele_lln()





# Als je van iedereen alle domein-uren wilt opvragen
def alles_geg():
    # Voor lln 1 tot lnn n
    for i in range(3,beschikbaar_lln_id):
        values_list = worksheet.row_values(i)
        print(values_list[2],"heeft zelfstudie op: ")
        ding = [i for i, x in enumerate(values_list) if x == 'Zelfstudie']
        x = []
        for z in ding:
            if (int(z)) == int(4):
                dag = ('Ma_1')
                x.extend([dag])
            elif (int(z)) == int(5):
                dag = ('Ma_2')
                x.extend([dag])
            elif (int(z)) == int(6):
                dag = ('Ma_3')
                x.extend([dag])
            elif (int(z)) == int(7):
                dag = ('Ma_4')
                x.extend([dag])
            elif (int(z)) == int(8):
                dag = ('Ma_5')
                x.extend([dag])
            elif (int(z)) == int(9):
                dag = ('Ma_6')
                x.extend([dag])
            elif (int(z)) == int(10):
                dag = ('Ma_7')
                x.extend([dag])
            elif (int(z)) == int(11):
                dag = ('Di_1')
                x.extend([dag])
            elif (int(z)) == int(12):
                dag = ('Di_2')
                x.extend([dag])
            elif (int(z)) == int(14):
                dag = ('Ma_14')
                x.extend([dag])
            elif (int(z)) == int(15):
                dag = ('Ma_15')
        print(x)


# alles_geg()



# In het vervolg om deze rechtstreek te updaten

