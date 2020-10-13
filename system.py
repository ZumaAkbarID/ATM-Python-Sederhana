from data import data_user
from data import data_bank

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

def feeBank():
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

def tarikUang(jumlah, uid):
    # MASIH Perlu perbaikan !!!
    # SAYA NGANTUK NANTI LAGI YA
    user = cekUser(uid)
    userBank = cekBank(data_user[user]['norek'])
    for bank in data_bank:
        if bank['default'] == True:
            fee = bank['biaya']
            default = bank['name']
    if user >= 0:
        if userBank['nama'] == default:
            if  data_user[user]['saldo'] >= int(jumlah):
                data_user[user]['saldo'] -= int(jumlah)
                print('Berhasil menarik uang Rp.'+str(jumlah))
                print('Silahkan ambil uang Anda')
                print('Sisa saldo anda adalah Rp.'+str(data_user[user]['saldo']))
            else:
                print('Maaf saldo anda tidak mencukupi')