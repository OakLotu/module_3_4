def s(r, *w): return [x for x in w if r.lower() in x.lower() or x.lower() in r.lower()]

print(s('rich', 'richiest', 'orichalcum', 'cheers', 'richies'), s('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))