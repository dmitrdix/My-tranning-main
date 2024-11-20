def all_variants(text):
    for j in range(len(text)):
        for l in range(len(text)-j):
            yield text[l:l+j+1]

a = all_variants("abc")
for i in a:
    print(i)