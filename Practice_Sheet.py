# def profile(name, age, main_lang):
#     print(name, age, main_lang)
#
#
# profile(name="유재석", main_lang="파이썬", age=20,)
# profile(main_lang="자바", name="김태호", age=20)





# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
#
#
# profile("유재석", 20, "python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")




#가변인자
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")