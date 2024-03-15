#tao cac lists:
svID = []
name = [''] * 100000
sex = [''] * 100000
age = [0] * 100000
diemToan = [0] * 100000
diemLy = [0] * 100000
diemHoa = [0] * 100000
diemTB = [0] * 100000
hocluc = [''] * 100000
maxID = 1
rank = ['Gioi', 'Kha', 'Trung binh', 'Yeu']




def menu():
    print("\nCHUONG TRINH QUAN LI SINH VIEN")
    print("********************************MENU********************************")
    print('**  1. Them sinh vien                                             **')
    print('**  2. Cap nhat thong tinh sinh vien boi ID                       **')
    print('**  3. Xoa sinh vien boi ID                                       **')
    print('**  4. Tim kiem sinh vien theo ten                                **')
    print('**  5. Sap xep sinh vien sinh vien theo diem trung binh (GPA)     **')
    print('**  6. Sap xep sinh vien theo ten                                 **')
    print('**  7. Sap xep sinh vien theo ID                                  **')
    print('**  8. Hien thi danh sach sinh vien                               **')
    print('**  0. Thoat                                                      **')
    print('********************************************************************')
    
    while True:
        try:
            option_in = int(input('Nhap lua chon cua giao vien: '))
            if option_in > 8:
                print('Xin hay nhap gia tri dung!')
                continue
            break
        except ValueError:
            print('Xin hay nhap gia tri dung!')
    
    return option_in


    
def autoID():
    global maxID
    if len(name) > 0:
        svID.append(maxID)
        maxID += 1
    return svID, maxID

def addSV():
    nameSV = str(input('Nhap ten sinh vien: '))
    name[maxID] = nameSV
    
    sexSV = str(input('Nhap gioi tinh sinh vien: '))
    sex[maxID] = sexSV
    
    tuoiSV = input('Nhap tuoi sinh vien: ')
    age[maxID] = tuoiSV
    
    toan = float(input('Nhap diem toan cua sinh vien: '))
    diemToan[maxID] = toan
    
    ly = float(input("Nhap diem ly cua sinh vien: "))
    diemLy[maxID] = ly
    
    hoa = float(input('Nhap diem hoa cua sinh vien: '))
    diemHoa[maxID] = hoa
    
    diem_tb = (toan + ly + hoa) / 3
    round_tb = round(diem_tb, 2)
    diemTB[maxID] = round_tb

    if round_tb >= 8:
        hocluc[maxID] = rank[0]
    elif 8 > round_tb >= 6.5:
        hocluc[maxID] = rank[1]
    elif 6.5 > round_tb >= 5:
        hocluc[maxID] = rank[2]
    elif round_tb < 5:
        hocluc[maxID] = rank[3]
    
    autoID()
    
    while True:
        try:
            more = str(input('\nNhap them sinh vien (y/n)?:'))
            if more == 'y':
                addSV()
            elif more == 'n':
                break
            else:
                print('Xin hay nhap gia tri dung!')
                continue
            break
        
        except ValueError:
            print('Xin hay nhap gia tri dung!')
            
    
    return


def displaySV():
    if len(svID) > 0:
        print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
        for ids in svID:
            print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(ids, name[ids], sex[ids], age[ids], diemToan[ids], diemLy[ids], diemHoa[ids], diemTB[ids], hocluc[ids]))
    else:
        print('\nChua co du lieu nao duoc nhap vao.')
        

def updateSV():
    if len(svID) > 0:
        print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
        for ids in svID:
            print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(ids, name[ids], sex[ids], age[ids], diemToan[ids], diemLy[ids], diemHoa[ids], diemTB[ids], hocluc[ids]))
        find_ID = int(input('\nNhap ID sinh vien: '))
        if find_ID in svID:
            print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
            print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(find_ID, name[find_ID], sex[find_ID], age[find_ID], diemToan[find_ID], diemLy[find_ID], diemHoa[find_ID], diemTB[find_ID], hocluc[find_ID]))
            
            modi_choice = input("Chinh sua (nhan 'xong' de ket thuc chinh sua): ")
            while True:
                try:
                    if modi_choice.lower() == 'ten':
                        name[find_ID] = input('Ten: ')
                        modi_choice = input('Chinh sua: ')
                    
                    elif modi_choice.lower() == 'gioi tinh':
                        sex[find_ID] = input('Gioi tinh: ')
                        modi_choice = input('Chinh sua: ')
                    
                    elif modi_choice.lower() == 'tuoi':
                        age[find_ID] = int(input('Tuoi: '))
                        modi_choice = input('Chinh sua: ')
                    
                    elif modi_choice.lower() == 'toan':
                        diemToan[find_ID] = float(input('Diem toan: '))
                        modi_choice = input('Chinh sua: ')
                    
                    elif modi_choice.lower() == 'ly':
                       diemHoa[find_ID] = float(input('Diem ly: '))
                       modi_choice = input('Chinh sua: ')
                    
                    elif modi_choice.lower() == 'hoa':
                       diemHoa[find_ID] = float(input('Diem hoa: '))
                       modi_choice = input('Chinh sua: ')
                    
                    elif modi_choice.lower() == 'xong':
                        break
                    
                    else:
                        print('Xin hay nhap gia tri dung!')
                        modi_choice = input('Chinh sua: ')
                        
                except ValueError:
                    print('Xin hay nhap gia tri dung!')
        else:
            print('\nKhong co thong tin sinh vien nay.')
    
    else:
        print('\nChua co du lieu nao duoc nhap vao.')
    
    return

def deleteSV():
    if len(svID) > 0:
        print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
        for ids in svID:
            print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(ids, name[ids], sex[ids], age[ids], diemToan[ids], diemLy[ids], diemHoa[ids], diemTB[ids], hocluc[ids]))
            
        del_choice = int(input('\nXoa sinh vien bang ID: '))
        while True:
            try:
                if del_choice in svID:
                    svID.remove(del_choice)
                    print('Da xoa sinh vien ra khoi danh sach')
                    break
                    
                elif del_choice not in svID:
                    print('Khong co sinh vien nay.')
                    del_choice = int(input('\nXoa sinh vien bang ID: '))
                
            except ValueError:
                print('Xin hay nhap gia tri dung!')
    
    else:
        print('\nChua co du lieu nao duoc nhap vao.')                       
        
        
def findbynameSV():
    if len(svID) > 0:
        name_find = input('Nhap ten sinh vien: ')
        find_ID = name.index(name_find)
        if find_ID in svID:
            print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
            print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(find_ID, name[find_ID], sex[find_ID], age[find_ID], diemToan[find_ID], diemLy[find_ID], diemHoa[find_ID], diemTB[find_ID], hocluc[find_ID]))
        
    else:
        print('\nChua co du lieu nao duoc nhap vao.')

def sortbygpaSV():
    ID_dtb = {}
    for key in svID:
        ID_dtb[key] = diemTB[key]
    
    sorted_ID_dtb = sorted(ID_dtb.items(), key=lambda x:x[1])
    
    if len(svID) > 0:
        print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
        for key, value in sorted_ID_dtb:
            print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(key, name[key], sex[key], age[key], diemToan[key], diemLy[key], diemHoa[key], value, hocluc[key]))
            
    else:
        print('\nChua co du lieu nao duoc nhap vao.')
    
def sortbynameSV():
    first_name = [''] * 1000000
    for index, fname in enumerate(name):
        if fname == '':
            continue
        rfname = fname.rsplit(' ', 1)[1]
        first_name[index] = rfname
    
    ID_name = {}
    
    for key in svID:
        ID_name[key] = first_name[key]
    
    sorted_ID_name = sorted(ID_name.items(), key=lambda x:x[1])
    
    if len(svID) > 0:
        print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
        for key, value in sorted_ID_name:
            print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(key, name[key], sex[key], age[key], diemToan[key], diemLy[key], diemHoa[key], diemTB[key], hocluc[key]))
            
    
    else:
        print('\nChua co du lieu nao duoc nhap vao.')

def sortbyidSV():
    if len(svID) > 0:
        print('Sap xep theo ID tang dan (i)')
        print('Sap xep theo ID giam dan (d)')
        sort_choice = input('Nhap lua chon: ')
        if sort_choice == 'i':
            print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
            for ids in svID:
                print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(ids, name[ids], sex[ids], age[ids], diemToan[ids], diemLy[ids], diemHoa[ids], diemTB[ids], hocluc[ids]))
        
        elif sort_choice == 'd':
            print('\nID  |  Ten                   |  Gioi tinh  |  Tuoi  |  Toan  |  Ly  |  Hoa  |  TBM  |  Hoc Luc  ')
            dec_svID = sorted(svID, reverse=True)
            for dec_ids in dec_svID:
                print('{:<3} | {:<22} | {:<11} | {:<6} | {:<6} | {:<4} | {:<5} | {:<5} | {:<10} '.format(dec_ids, name[dec_ids], sex[dec_ids], age[dec_ids], diemToan[dec_ids], diemLy[dec_ids], diemHoa[dec_ids], diemTB[dec_ids], hocluc[dec_ids]))
    
    else:
        print('\nChua co du lieu nao duoc nhap vao.')
        
    
     
while True:
    option = menu()
    
    if option == 0:
        break
    if option == 1:
        addSV()
        
    if option == 2:
        updateSV()
        
    if option == 3:
        deleteSV()
        
    if option == 4:
        findbynameSV()
        
    if option == 5:
        sortbygpaSV()
        
    if option == 6:
        sortbynameSV()
        
    if option == 7:
        sortbyidSV()
    if option == 8:
        displaySV()