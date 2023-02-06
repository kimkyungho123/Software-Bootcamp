# print("Python", "Java", sep=", ", end="?")
# print("무엇이 더 재밌을까요?")



# import sys
# print("Python", "Java", file=sys.stdout) #표준출력
# print("Python", "Java", file=sys.stderr) #표준에러



# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(3), str(score).rjust(4), sep=":")


# 은행 대기순번표 ex) 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))



answer = input("아무 값이나 입력하세요 : ")
# 중요: input()함수는 항상 문자열로 값을 저장한다
print(type(answer))
print("입력하신 값은 " + answer + " 입니다.")