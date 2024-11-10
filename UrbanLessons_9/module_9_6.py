def all_variants(text):
    text_len = len(text)
    for start in range(text_len):
        for end in range(start + 1, text_len + 1):
            yield text[start:end]

a = all_variants("abc")
for i in a:
    print(i)
