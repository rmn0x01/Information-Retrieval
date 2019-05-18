from whoosh.analysis import StemmingAnalyzer

text = input()
ana = StemmingAnalyzer()
print([token.text for token in ana(text)])