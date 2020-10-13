import system

repeat = 'no'
logged = False
isused = 'yes'
security = 'yes'

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
            login = system.cekLogin(pin)
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
        print('1. Cek Saldo          2. Tarik Uang'.center(50))
        print('3. Transfer Uang      4. Logout    '.center(50))
        print('5. Keluar ATM                      '.center(50))
        print('========================='.center(50))
        selected = int(input('Pilih Menu (masukkan nomor): '))
        if selected == 1:
            print('')
            print('Cek Saldo'.center(50))
            print('========================='.center(50))
            print('Saldo Anda adalah Rp.'+str(system.cekSaldo(userid)))
            print('')
        elif selected == 2:
            print('')
            print('Tarik Uang'.center(50))
            print('========================='.center(50))
            jumlah = input('Masukkan nominal: ')
            print('')
            system.tarikUang(jumlah, userid)
            print('')
        elif selected == 3:
            print('')
            print('Transfer Uang'.center(50))
            print('')
            system.feeBank()
            print('')
            norek = input('Masukkan nomor rekening tujuan: ')
            if len(norek) == 0:
                print('')
                norek = input('Nomor rekening tidak valid, Masukkan nomor rekening tujuan: ')
            elif system.userRek(norek) != False:
                user = system.userRek(norek)
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
            jumlah = input('Masukkan nominal: ')
            print('')
            system.transferUang(jumlah, norek, userid)
            print('')
        elif selected == 4:
            logged = False
        elif selected == 5:
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