import random
Kor = ["아", "에", "우", "이", "오", 
       "카", "키", "쿠", "케", "코",
       "사", "시", "스", "세", "소",
       "타", "치", "츠", "테", "토",
       "나", "니", "누", "네", "노",
       "하", "히", "후", "헤", "호",
       "마", "미", "무", "메", "모",
       "야", "유", "요",
       "라", "리", "루", "레", "로",
       "와", "조사 오",
       "응"]

Jap = ["あ","い", "う", "え", "お",
       "か", "き", "く", "け", "こ",
       "さ", "し", "す", "せ", "そ",
       "た", "ち", "つ", "て", "と",
       "な", "に", "ぬ", "ね", "の",
       "は", "ひ", "ふ", "へ", "ほ", 
       "ま", "み", "む", "め", "も", 
       "や", "ゆ", "よ",
       "ら", "り", "る", "れ", "ろ",
       "わ", "を",
       "ん"]
check = False
print("hiya")
while True:
    check = False
    mode = input("Type mode(J, K): ")
    #print(mode)
    while check == False:
        if mode.lower() == "k":
            k = random.randint(0, 45)
            print(Kor[k])
            #print(k)
            rep = input()
            if rep == "":
                print(Jap[k])
                print("----")
            #    print(k)
            elif rep == "b":
                check = True
            elif rep == "q":
                print("Ending practice!")
                exit()
    #while check == False:
        if mode.lower() == "j":
            k = random.randint(0, 45)
            print(Jap[k])
            #print(k)
            rep = input()
            if rep == Kor[k]:
                print("Correct!")
                print("----")
            elif rep == "b":
                check = True
            elif rep == "q":
                print("Ending practice!")
                exit()
            elif rep != Kor[k]:
                print("Wrong! The correct answer is")
                print(Kor[k])
                print("----")
            #    print(k)
              
