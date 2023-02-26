print("*** Reading E-Book ***")

text,high=input('Text , Highlight : ').split(',')

for i in range(len(text)):
    if text[i]==high:
        print('[',text[i],']',sep='',end='')
    else:
        print(text[i],end='')
