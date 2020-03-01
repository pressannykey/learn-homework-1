with open('referat.txt', 'r', encoding='utf-8') as f:
    print(len(str(f)))
    words = 0
    for line in f:
        new_line = line.replace("-", "").split()
        words += len(new_line)
        with open('referat2.txt', 'a', encoding='utf-8') as new_f:
            new_f.write(line.replace(".", "!"))

    print(f'Слов в файле: {words}')
