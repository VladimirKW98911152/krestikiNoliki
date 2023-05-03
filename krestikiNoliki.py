print("|","-"*25,"|")
print("|","*"*25,"|")
print("|","*"*8, "И Г Р А", "*"*8,"|")
print("|","*"*4, "Крестики-нолики", "*"*4,"|")
print("|","*"*2, " (Для двух игроков)", "*"*2,"|")
print("|","*"*25,"|")
print("|","-"*25,"|")

field = list(range(1, 10))

def displaying_fild(field):
    print("|","-"*11,"|")
    for i in range(3):
        print("|","|",field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("|","-"*11,"|")
 

def Entering_a_symbol(symbol):
    valid = False
    while not valid:
        cross_nolik = input("Укажите номер клетки\n, в которую поставите "+symbol+" : ")
        try:
            cross_nolik = int(cross_nolik)
        except:
            print("Некорректный ввод.\n Вы точно уверены, что ввели число?")
            continue
        if cross_nolik >= 1 and cross_nolik <=9:
            if(str(field[cross_nolik-1]) not in "X0"):
                field[cross_nolik-1] = symbol
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def control(field):
    winning_combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in winning_combinations:
        if field[each[0]]==field[each[1]]==field[each[2]]:
            return field[each[0]]
    return False

def play(field):
    begining = 0
    victory = False
    while not victory:
        displaying_fild(field)
        if begining % 2 == 0:
            Entering_a_symbol("X")
        else:
            Entering_a_symbol("0")
        begining += 1
        if begining > 4:
            tmp = control(field)
            if tmp:
                print("Победили", tmp)
                victory = True
                break
        if begining == 9:
            print("Ничья!")
            break
    displaying_fild(field)
    
play(field)

input("Нажмите Enter\nчтобы выйти из игры")
