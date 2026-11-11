# 가위 바위 보 게임 미니 프로젝트
import random

print('=' * 31)
print("     가위 / 바위 / 보 게임")
print('=' * 31)

rps = ['가위', '바위', '보']
scores = {
    'player': 0,
    'computer': 0
}

def replay():
    while True:
        answer = input('\n다시 도전 (yes/no) : ')
        if answer.lower() in ['yes', 'y']:
            return True
        elif answer.lower() in ['no', 'n']:
            return False
        else:
            print("입력하지 않거나 잘못된 값을 입력하셨습니다.")

def rps_play(player_rps, computer_rps):
    if player_rps == 1:
        if computer_rps == '가위':
            print('=> 비김')
        if computer_rps == '바위':
            print('=> 패배')
            scores['computer'] += 1
        if computer_rps == '보':
            print('=> 승리')
            scores['player'] += 1
    elif player_rps == 2:
        if computer_rps == '가위':
            print('=> 승리')
            scores['player'] += 1
        if computer_rps == '바위':
            print('=> 비김')
        if computer_rps == '보':
            print('=> 패배')
            scores['computer'] += 1
    else:
        if computer_rps == '가위':
            print('=> 패배')
            scores['computer'] += 1
        if computer_rps == '바위':
            print('=> 승리')
            scores['player'] += 1
        if computer_rps == '보':
            print('=> 비김')
            
def play():
    print('1. 가위 / 2. 바위 / 3. 보')

    while True:
        player_rps = input('\n번호를 선택하세요. : ')
        if player_rps in ['1', '2', '3']:
            player_rps = int(player_rps)
            break

        print("1~3만 입력해주세요.")

    computer_rps = random.choice(rps)

    print('\n[게임 결과]')
    print(f'나: {rps[player_rps - 1]} vs 컴퓨터: {computer_rps}')

    rps_play(player_rps, computer_rps)

    print(f"\n현재 스코어  나 {scores['player']} : {scores['computer']} 컴퓨터")

while True:
    play()

    if replay() == False:
        print("게임을 종료합니다.")
        break