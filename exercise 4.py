# st= input("enter any message")
# coding=True
# if(coding):
#     if (len(st)>=3):
#         r1="sgh"
#         r2="jkl"
#         st=st[1:] + st[0]
#         print(st)
#     else:
#         pass

#encoding
st = input("Enter any message: ")
words = st.split(" ")
coding = True
nwords = []
if coding:
    for word in words:
        if len(word) >= 3:
            r1 = "sgh"
            r2 = "jkl"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

    print(" ".join(nwords))
