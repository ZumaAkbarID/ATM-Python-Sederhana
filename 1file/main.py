userid = 0
repeat = 'n'
logged = False
isused = 'y'

data_user = [
    {
        "id" : "1",
        "norek" : "123456",
        "username" : "UCUP",
        "pin" : "1234",
        "saldo" : 1000000
    },
    {
        "id" : "2",
        "norek" : "234567",
        "username" : "PUCU",
        "pin" : "4321",
        "saldo" : 2000
    }
]

def cekLogin(p):
    for user in data_user:
        if user['pin'] == p:
            return user
    return False

def cekUser(id):
    for i in range(len(data_user)):
        if data_user[i]['id'] == str(id):
            return int(i)
    return -1

def cekSaldo(id):
    for i in range(len(data_user)):
        if data_user[i]['id'] == str(id):
            return data_user[i]['saldo']
    return -1

def cekRek(norek):
    for i in range(len(data_user)):
        if str(data_user[i]['norek']) == norek:
            return int(i)
    return -1

def transferUang(jumlah, norek):
    first_user = cekUser(userid)
    second_user = cekRek(norek)
    if first_user >= 0:
        if data_user[first_user]['saldo'] >= int(jumlah):
            data_user[first_user]['saldo'] -= int(jumlah)
            data_user[second_user]['saldo'] += int(jumlah)
            print('Anda berhasil mentransfer uang Rp.'+str(jumlah)+' ke rekening '+norek)
            print('Sisa saldo anda adalah Rp.'+str(data_user[first_user]['saldo']))
        else:
            print('Maaf saldo anda tidak mencukupi')

def tarikUang(jumlah):
    user = cekUser(userid)
    if user >= 0:
        if data_user[user]['saldo'] >= int(jumlah):
            data_user[user]['saldo'] -= int(jumlah)
            print('Berhasil mengambil uang Rp.'+str(jumlah))
            print('Sisa saldo anda adalah Rp.'+str(data_user[user]['saldo']))
        else:
            print('Maaf saldo anda tidak mencukupi')

while isused == 'y':
    while logged == False:
        print('ATM Indonesia'.center(50))
        print('')
        print('Silahkan masukkan kartu ATM Anda'.center(50))
        card = input('Masukkan kartu (ketik "card" kemudian enter): ')
        if len(card) == 0:
            print('')
            print('Kartu ATM harus dimasukkan')
            print('')
        elif  card != 'card':
            print('')
            print('Maaf yang anda masukkan bukanlah kartu ATM')
            print('')
        else:
            security = 'n'
            print('Silahkan masukkan kode PIN Anda'.center(50))

        if security == 'n':
            pin = input('Masukkan PIN: ')
            login = cekLogin(pin)
            if login != False:
                print('Selamat datang, '+login['username'])
                userid = login['id']
                logged = True
                repeat = 'y'
            else:
                print('')
                print('Kode PIN ada salah ')
                print('')

    while repeat == 'y' and logged == True:
        print('ATM Indonesia'.center(50))
        print('Menu'.center(50))
        print('===================='.center(50))
        print('1. Cek Saldo      2. Tarik Uang'.center(50))
        print('3. Transfer Uang      4. Logout'.center(50))
        print('')
        selected = int(input('Pilih Menu (masukkan nomor): '))
        if selected == 1:
            print('')
            print('Cek Saldo'.center(50))
            print('')
            print('Saldo Anda adalah Rp.'+str(cekSaldo(userid)))
            print('')
            repeat = 'n'
        elif selected == 2:
            print('')
            print('Tarik Uang'.center(50))
            jumlah = input('Masukkan nominal: ')
            print('')
            tarikUang(jumlah)
            print('')
        elif selected == 3:
            print('')
            print('Transfer Uang'.center(50))
            print('')
            norek = input('Masukkan nomor rekening tujuan: ')
            jumlah = input('Masukan nominal: ')
            transferUang(jumlah, norek)
            print('')
        elif selected == 4:
            print('')
            print('Silahkan ambil kartu ATM Anda')
            print('')
            logged = False
            repeat = 'n'
            isused = 'n'
        else:
            print('')
            print('Menu tidak ditemukan')
            print('')
        if logged == True:
            input('Kembali ke menu (enter)')
            print('')
            repeat = 'y'