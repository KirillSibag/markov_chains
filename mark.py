import markovify
import pickle
from nltk.tokenize import word_tokenize
from googletrans import Translator
translator = Translator()
import nltk

while True:
    #print("")
    print("выберите стиль:")
    print("проза - 1")
    print("крутая проза - 4")
    print("стих  - 2")
    print("хокку - 3")
    tok = mm1 = int(input())

    if tok == 1:
        print("выбери базу слов (2-5)")
        tok = int(input())
        try:
            with open("data" + str(tok) + ".pickle", "rb") as f:
                text_model = pickle.load(f)
        except Exception as ex:
            with open("data123456.pickle", "rb") as f:
                text_model = pickle.load(f)

    elif tok == 2:
        print("выбери базу слов (2-5)")
        tok = int(input())
        try:
            with open("data_poem_1" + str(tok) + ".pickle", "rb") as f:
                text_model = pickle.load(f)
        except Exception as ex:
            with open("data_poem_12.pickle", "rb") as f:
                text_model = pickle.load(f)

    elif tok == 4:
        print("выбери базу слов (1-6)")
        tok = int(input())
        try:
            with open("result_all3" + str(tok) + ".pickle", "rb") as f:
                text_model = pickle.load(f)
        except Exception as ex:
            with open("result_all32.pickle", "rb") as f:
                text_model = pickle.load(f)
                
    else:
        print("выбери базу слов (1-6)")
        tok = int(input())
        try:
            with open("data_hokku_2" + str(tok) + ".pickle", "rb") as f:
                text_model = pickle.load(f)
        except Exception as ex:
            with open("data_hokku_22.pickle", "rb") as f:
                text_model = pickle.load(f)

    while True:
        print("введите 'меню' чтобы выйти назад")
        print("")
        print("выбери режим:")
        print("предложения  - - - - - - 0")
        print("одно на основе другого - 1")
        print("прогрессия - - - - - - - 2")
        mode = input()
        
        if mode == "меню":
            break

        elif mode == "2":
            minxx = 1
            stri = ""
            while True:
                #приказ к генерации
                i = input()

                if i == "меню":
                    break
                
                while len(stri) <= minxx:
                    stri = text_model.make_sentence(min_words = 1, max_words = 2000, tries = 200)

                print(minxx, "___", stri)
                minxx = (len(stri)) + 5
                stri = ""
            
        elif mode == "0":
            
            print("минимальная длина: (иначе 9)")
            
            minn = input()
            if minn == "":
                minn = 9
            else:
                try:
                    minn = int(minn)
                except Exception as ex:
                    minn = 9


            print("максимальная длина: (иначе 13)")
            
            maxx = input()
            if maxx == "":
                maxx = 13
            else:
                try:
                    maxx = int(maxx)
                except Exception as ex:
                    maxx = 13
                    
            stri = ""
            data = ""
            print("введите 'меню' чтобы выйти назад")
            while True:
                #приказ к генерации
                i = input()

                if i == "меню":
                    break

                while stri == "" or stri == None or (stri[0: len(stri)//3] in data) or (stri[len(stri)//3: len(stri)//3*2] in data) or (stri[len(stri)//3*2: len(stri)-1] in data):
                    stri = text_model.make_sentence(min_words = minn, max_words = maxx, tries = 200)

                if mm1 != 1:
                    listt = []
                    app = ""
                    for inn in stri:
                        if inn in "ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЁЯЧСМИТЬБЮ":
                            listt.append(app)
                            app = ""

                        app += inn
                        

                    listt.append(app)
                    for inn in listt:
                        print(inn)

                else:
                    print(stri)
                
                data += " " + stri
                stri = ""

                

        else:
            stri = ""
            count = 0
            print("введите 'меню' чтобы выйти назад")
            while True:
                #приказ к генерации
                i = input()

                if i == "меню":
                    break

                #разбиваем предыдущую строку на слова
                a = []
                add = ""
                for j in stri:
                    if j != " ":
                        add += j
                    else:
                        a.append(add)
                        add = ""
                a.append(add)


                #нахождение ключевых слов
                b = []        
                for i in a:
                    #не нужны короткие слова (явно не ключевые)
                    if len(i) > 3:
                        #переводим слово и классифицируем по части речи
                        s = nltk.pos_tag([translator.translate(i, dest='en').text])

                        #если существительное (можно добавить варианты, вписав в строку)
                        if s[0][1] in "NN":

                            #считаем ключевым
                            b.append(i)

                a = b
                #print(a)
                stri = ""
                i = 0
                            
                while i < 2 or stri == None:
                    stri = text_model.make_sentence(min_words = 3, tries = 200)

                    i = 0
                    if count != 0:
                        for abc in a:
                            if abc in stri:
                                i += 1

                    else:
                        i = 100
                        
               
                print(stri)
                count +=1
