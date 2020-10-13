repeat = 'no'
logged = False
isused = 'yes'
security = 'yes'

data_bank = [
    {
        "id" : "1",
        "nama" : "Bank Indonesia",
        "kode" : "001",
        "biaya" : 6000,
        "default" : True
    },
    {
        "id" : "2",
        "nama" : "BRI",
        "kode" : "002",
        "biaya" : 4000,
        "default" : False
    }
]

data_user = [
    {
        "id" : "1",
        "norek" : "123456",
        "username" : "UCUP",
        "pin" : "1234",
        "saldo" : 1000000,
        "bank" : "Bank Indonesia"
    },
    {
        "id" : "2",
        "norek" : "234567",
        "username" : "PUCU",
        "pin" : "4321",
        "saldo" : 0,
        "bank" : "BRI"
    },
    {
        "id" : "3",
        "norek" : "345678",
        "username" : "CUPU",
        "pin" : "1324",
        "saldo" : 1000000,
        "bank" : "Bank Indonesia"
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

def userRek(norek):
    for i in range(len(data_user)):
        if str(data_user[i]['norek']) == norek:
            return data_user[i]
    return False
    
def cekBank(norek):
    user = userRek(norek)
    for i in range(len(data_bank)):
        if data_bank[i]['nama'] == user['bank']:
            return data_bank[i]
    return False

def feeTransfer():
    print('1. Biaya admin antar bank Rp.'+str(data_bank[0]['biaya']))
    print('2. Transfer sesama Bank Indonesia gratis')

def transferUang(jumlah, norek, uid):
    first_user = cekUser(uid)
    firstUser = cekBank(data_user[first_user]['norek'])    
    second_user = cekRek(norek)
    secondUser = cekBank(data_user[second_user]['norek'])
    for bank in data_bank:
        if bank['default'] == True:
            fee = bank['biaya']
    if first_user == second_user:
        print('Anda tidak dapat melakukan transaksi dengan akun Anda sendiri')
    else:
        if first_user >= 0:
            if firstUser['id'] != secondUser['id']:
                if  data_user[first_user]['saldo'] >= int(jumlah) + fee:
                    data_user[first_user]['saldo'] -= int(jumlah) + fee
                    data_user[second_user]['saldo'] += int(jumlah)
                    print('Anda berhasil mentransfer uang Rp.'+str(jumlah)+' dengan biaya admin '+ str(fee) +' ke rekening '+norek)
                    print('Sisa saldo anda adalah Rp.'+str(data_user[first_user]['saldo']))
                else:
                    print('Maaf saldo anda tidak mencukupi')
            else:
                if  data_user[first_user]['saldo'] >= int(jumlah):
                    data_user[first_user]['saldo'] -= int(jumlah)
                    data_user[second_user]['saldo'] += int(jumlah)
                    print('Anda berhasil mentransfer uang Rp.'+str(jumlah)+' ke rekening '+norek)
                    print('Sisa saldo anda adalah Rp.'+str(data_user[first_user]['saldo']))
                else:
                    print('Maaf saldo anda tidak mencukupi')

def feeTarik():
    print('1. Biaya admin tarik uang menggunakan kartu ATM selain Bank Indonesia Rp.'+str(data_bank[0]['biaya']))
    print('2. Tarik uang menggunakan ATM Bank Indonesia gratis')

def tarikUang(jumlah, uid):
    user = cekUser(uid)
    userBank = cekBank(data_user[user]['norek'])
    for bank in data_bank:
        if bank['default'] == True:
            fee = bank['biaya']
            default = bank['nama']
    if user >= 0:
        if userBank['nama'] == default:
            if  data_user[user]['saldo'] >= int(jumlah):
                data_user[user]['saldo'] -= int(jumlah)
                print('Berhasil menarik uang Rp.'+str(jumlah))
                print('Silahkan ambil uang Anda')
                print('Sisa saldo anda adalah Rp.'+str(data_user[user]['saldo']))
            else:
                print('Maaf saldo anda tidak mencukupi')
        else:
            if  data_user[user]['saldo'] >= int(jumlah) + fee:
                data_user[user]['saldo'] -= int(jumlah) + fee
                print('Berhasil menarik uang Rp.'+str(jumlah)+' dengan biaya admin Rp.'+str(fee))
                print('Silahkan ambil uang Anda')
                print('Sisa saldo anda adalah Rp.'+str(data_user[user]['saldo']))
            else:
                print('Maaf saldo anda tidak mencukupi')

def feeDeposit():
    print('1. Biaya admin deposit menggunakan kartu ATM selain Bank Indonesia Rp.'+str(data_bank[0]['biaya']))
    print('2. Deposit menggunakan ATM Bank Indonesia gratis')

def deposit(jumlah, uid):
    user = cekUser(uid)
    userBank = cekBank(data_user[user]['norek'])
    for bank in data_bank:
        if bank['default'] == True:
            fee = bank['biaya']
            default = bank['nama']
    if user >= 0:
        if userBank['nama'] == default:
            data_user[user]['saldo'] += int(jumlah)
            print('Berhasil deposit sebesar Rp.'+str(jumlah))
            print('Saldo anda adalah Rp.'+str(data_user[user]['saldo']))
        else:
            data_user[user]['saldo'] += int(jumlah) - fee
            print('Berhasil deposit sebesar Rp.'+str(jumlah)+' dengan biaya admin Rp.'+str(fee))
            print('Saldo anda adalah Rp.'+str(data_user[user]['saldo']))

while isused == 'yes':
    while logged == False:
        print('')
        print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;'.center(50))
        print(';       ATM INDONESIA      ;'.center(50))
        print(';--------------------------;'.center(50))
        print(';       Author : Zuma      ;'.center(50))
        print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;'.center(50))
        print('')
        print('Silahkan masukkan kartu ATM Anda'.center(50))
        print('')
        card = input('Masukkan kartu (ketik "card" kemudian enter): ')
        print('')
        if len(card) == 0:
            print('')
            print('Kartu ATM harus dimasukkan')
            print('')
        elif  card != 'card':
            print('')
            print('Maaf yang anda masukkan bukanlah kartu ATM')
            print('')
        else:
            security = 'no'
            print('Silahkan masukkan kode PIN Anda'.center(50))
            print('')
        if security == 'no':
            pin = input('Masukkan PIN: ')
            print('')
            login = cekLogin(pin)
            if login != False:
                print('Selamat datang, '+login['username'])
                userid = login['id']
                logged = True
                repeat = 'yes'
            else:
                print('')
                print('Kode PIN ada salah ')
                print('')

    while repeat == 'yes' and logged == True:
        print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;'.center(50))
        print(';       ATM INDONESIA      ;'.center(50))
        print(';--------------------------;'.center(50))
        print(';       Author : Zuma      ;'.center(50))
        print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;'.center(50))
        print('Menu'.center(50))
        print('========================='.center(50))
        print('1. Cek Saldo          2. Tarik Uang    '.center(50))
        print('3. Transfer Uang      4. Deposit       '.center(50))
        print('5. Logout             6. Keluar Program'.center(50))
        print('========================='.center(50))
        selected = int(input('Pilih Menu (masukkan nomor): '))
        if selected == 1:
            print('')
            print('Cek Saldo'.center(50))
            print('========================='.center(50))
            print('Saldo Anda adalah Rp.'+str(cekSaldo(userid)))
            print('')
        elif selected == 2:
            print('')
            print('Tarik Uang'.center(50))
            print('========================='.center(50))
            jumlah = input('Masukkan nominal: ')
            print('')
            tarikUang(jumlah, userid)
            print('')
        elif selected == 3:
            print('')
            print('Transfer Uang'.center(50))
            print('========================='.center(50))
            feeTransfer()
            print('')
            norek = input('Masukkan nomor rekening tujuan: ')
            if len(norek) == 0:
                print('')
                norek = input('Nomor rekening tidak valid, Masukkan nomor rekening tujuan: ')
            elif userRek(norek) != False:
                user = userRek(norek)
                print('')
                print('Penerima :')
                print('No. Rek  : '+user['norek'])
                print('Nama     : '+user['username'])
                print('Bank     : '+user['bank'])
                print('')
                tf = input('Tekan enter jika setuju ')
            else:
                print('')
                print('Penerima tidak ditemukan')
                print('')
                repeat = 'yes'
                break
            print('')
            jumlah = input('Masukkan nominal: ')
            print('')
            transferUang(jumlah, norek, userid)
            print('')
        elif selected == 4:
            print('')
            print('Deposit'.center(50))
            print('========================='.center(50))
            feeDeposit()
            print('')
            jumlah = input('Masukkan nominal: ')
            print('')
            deposit(jumlah, userid)
            print('')
        elif selected == 5:
            logged = False
        elif selected == 6:
            logged = False
            repeat = 'no'
            isused = 'no'
        else:
            print('')
            print('Menu tidak ditemukan')
            print('')
        if logged == True:
            input('Kembali ke menu (enter)')
            print('')
            repeat = 'yes'