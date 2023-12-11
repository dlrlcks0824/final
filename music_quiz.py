import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# 랜덤 가사 데이터베이스 (가사, 노래 제목)
lyrics_database = [
    {"lyrics": "너를 만나 참 행복했어 나 이토록 사랑할 수 있었던 건", "title": "폴킴 - 너를 만나"},
    {"lyrics": "어쩜 이렇게 하늘은 더 파란건지", "title": "아이유 - 좋은 날"},
    {"lyrics": "I'm so sorry but i love you 다 거짓말이야 몰랐어", "title": "빅뱅 - 거짓말"},
    {"lyrics": "You can call me artist You can call me idol", "title": "방탄소년단 - IDOL"},
    {"lyrics": "꽃잎이 번지면 그럼에도 새로운 봄이 오겠죠 한참이 걸려도 그대 반드시 행복해지세요", "title": "정승환 - 눈사람"},
    {"lyrics": "물끄러미 너를 들여다 보곤 해 그것 말고는 아무것도 할 수 없어서", "title": "성시경 - 너의 모든 순간"},
    {"lyrics": "미안해 더는 널 바라보지 않아 미안해 더는 나 후회하지 않아", "title": "양다일 - 미안해"},
    {"lyrics": "파란 하늘위로 훨훨 날아가겠죠", "title": "거북이 - 비행기"},
]

# 전역 변수로 correct_count를 선언
correct_count = 0

def get_random_lyrics(used_lyrics):
    remaining_lyrics = [lyrics for lyrics in lyrics_database if lyrics["lyrics"] not in used_lyrics]
    if not remaining_lyrics:
        return None
    return random.choice(remaining_lyrics)

def display_lyrics(lyrics):
    turtle.clear()
    turtle.write(f'"{lyrics}"', align="center", font=("Arial", 14, "normal"))

def show_game_screen():
    global correct_count, return_button, used_lyrics  # 전역 변수로 설정
    start_button.destroy()  # 게임 시작 버튼 제거
    if 'return_button' in globals():
        return_button.destroy()  # "메인 화면으로" 버튼 제거
    correct_count = 0  # 맞춘 문제의 개수 초기화
    used_lyrics = set()  # 사용된 가사 초기화

    turtle.reset()  # 터틀 초기화
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 100)  # 가사가 아래로 내려감
    turtle.pendown()

    for _ in range(8):
        # 랜덤 가사 가져오기
        current_lyrics = get_random_lyrics(used_lyrics)
        if current_lyrics is None:
            break

        display_lyrics(current_lyrics["lyrics"])
        used_lyrics.add(current_lyrics["lyrics"])

        # 사용자에게 퀴즈 제시
        user_answer = simpledialog.askstring("가사 퀴즈", "위 가사의 노래 제목은 무엇일까요?").strip().lower()

        # 정답 확인
        correct_answer = current_lyrics["title"].lower()
        is_correct = user_answer == correct_answer

        # 정답 및 오답 메시지 표시
        if is_correct:
            messagebox.showinfo("정답!", f"정답입니다: {correct_answer}")
            correct_count += 1  # 맞춘 문제의 개수 증가
        else:
            messagebox.showinfo("오답", f"틀렸습니다. 정답은 '{correct_answer}'입니다.")

    # 모든 문제를 다 푼 경우 "메인 화면으로" 버튼 추가
    return_button = tk.Button(turtle.Screen()._root, text=f"맞춘 문제: {correct_count}\n메인 화면으로", command=show_main_screen, font=("Arial", 18))
    return_button.place(relx=0.5, rely=0.4, anchor="center")

def show_main_screen():
    global start_button  # 전역 변수로 설정
    if 'return_button' in globals():
        return_button.destroy()  # "메인 화면으로" 버튼 제거
    turtle.reset()  # 터틀 초기화
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 150)
    turtle.write("SongTitle Riddles", align="center", font=("Arial", 24, "normal"))

    # 메인 화면 배경색 변경 (하늘색)
    turtle.Screen().bgcolor("skyblue")

    # 게임 시작 버튼 추가 (형광색 타원형 버튼)
    start_button = tk.Button(turtle.Screen()._root, text="게임 시작", command=show_game_screen, font=("Arial", 18),
                             bg="lime", activebackground="lime", bd=0)
    start_button.place(relx=0.5, rely=0.4, anchor="center")
    turtle.Screen().update()  # 화면 업데이트

if __name__ == "__main__":
    show_main_screen()
    turtle.Screen().mainloop()