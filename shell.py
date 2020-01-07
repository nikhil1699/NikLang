import NikLang
while True:
    text = input('NikLang $$ ')
    result, error = NikLang.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
