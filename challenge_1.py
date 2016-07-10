import string

result = []

text_given = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr \'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
key1 = "abcdefghijklmnopqrstuvwxyz"
key2 = "cdefghijklmnopqrstuvwxyzab"

translation = str.maketrans(key1, key2)

print(text_given.translate(translation))

text_given2 = "map"

print(text_given2.translate(translation))