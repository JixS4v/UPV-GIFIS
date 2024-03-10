from py_asciimath.translator.translator import ASCIIMath2Tex
while(True):
    snippet = input()
    asciimath2tex = ASCIIMath2Tex(log=False, inplace=True)
    parsed = asciimath2tex.translate(snippet,displaystyle=True,from_file=False,pprint=False)
    print(parsed)
