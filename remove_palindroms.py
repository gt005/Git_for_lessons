def remove_palindroms(spells):
    i = 0
    while i != len(spells):
        if ''.join(spells[i].split()).lower() == ''.join(
                spells[i][::-1].split()).lower():
            spells.pop(i)
            continue
        i += 1
