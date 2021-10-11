import re

print("Write string")
string = input()
string = re.sub("((^(\w) )|(( \w ))|( \w$))|((^a\w+ )|(^b\w+ )|(^c\w+ )|(^d\w+ )|(^e\w+ )|( a\w+ )|( b\w+ )|( c\w+ )|( d\w+ )|( e\w+ ))", " ", string)
string = re.sub("(^( +))", "", string)
print(string)
# eegExr was created by gskin a ner.com, and is prou f dly hosted by Media Eemp g le.
