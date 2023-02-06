# File Input&Output

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()


# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) #줄바꿈이 싫으면 end="" 사용
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()


#가져온 파일이 몇 줄인지 모를 때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line: #읽어올 내용이 없으면
#         break
#     print(line)
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #모든 line을 list 형태로 저장함
for line in lines:
    print(line, end="")
score_file.close()