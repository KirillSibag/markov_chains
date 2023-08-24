import markovify
import pickle

text = ""
print("file:")
a = input()
print("numberss:")
b = int(input())

##for i in range(1):
##    # Get raw text as string.
##    with open(a + "/" + str(i) + ".txt", encoding='ANSI') as f:
##        text += f.read()

with open("rersult_all.txt", encoding='ANSI') as f:
        text += f.read()
        
# Build the model.
state_size = 1

for i in range(6):
    text_model = markovify.NewlineText(text, state_size = state_size)

    try:
        with open("result_all" + str(state_size + 30) + ".pickle", "wb") as f:
            pickle.dump(text_model, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

    
    state_size += 1
