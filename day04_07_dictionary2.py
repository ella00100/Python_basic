alcohol_foods = {
    'beer' : 'chicken',
    'soju' : 'soup',
    'wine' : 'cheese',
    'makguli' : 'jun'
}
alcohol_list = list(alcohol_foods)
while True:
    alcohol = int(input(f"술을 선택 하세요 1){alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]} : "))
    if alcohol == 5:
        print('다음에 또 오세요~')
        break
    elif alcohol in (1,2,3,4) :
        print(f'{alcohol_list[alcohol-1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[alcohol-1]]}입니다')
        pass
    else:
        print('메뉴에서 골라주세요')