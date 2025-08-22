#실제과제는 업다운 게임?
import random

correct_number=random.randint(1, 100)
#print("correct number:", correct_number) #random 기억 불러오기
attempt_available = random.randint(6, 10)
attempt_count = 0

W_L_message = "(X) 더 위입니다!"
W_H_message = "(X) 더 아래입니다!"
# LL_message = f"맞추지 못했습니다! 목표: {correct_number}"
# WW_message = f"대단하십니다! 목표: {correct_number}\n 시도 {attempt_count}번"
print("업다운 게임에 오신 걸 환영합니다!")
print(f"이번 라운드의 횟수 제한은 {attempt_available} 입니다!")

while attempt_available > attempt_count:
    print(f"시도: {attempt_count} 번째\n남은 횟수: {attempt_available - attempt_count}\n")
    guess_number = input("당신의 예측 숫자를 알려주세요!\n")
    if correct_number > int(guess_number):
        print(W_L_message)
        attempt_count += 1
    elif correct_number < int(guess_number):
        print(W_H_message)
        attempt_count += 1
    elif correct_number == int(guess_number):
        print(f"대단하십니다! 목표: {correct_number}\n 시도 {attempt_count}번  남았던 시도: {attempt_available - attempt_count}번")
        break
else:
    print(f"맞추지 못했습니다! 목표: {correct_number}")