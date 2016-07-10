import re
import urllib.request

nothing_pre = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing_format = r"[0-9]{5}"
nothing_var = "8022"
nothing_url = nothing_pre + nothing_var

for var1 in range(0, 400):
    current_page = urllib.request.urlopen(nothing_pre + nothing_var).read()
    current_page = str(current_page.decode("utf-8"))
    if re.search("\d+", current_page):
        nothing_var = re.findall("\d+", current_page)
        nothing_var = "".join(nothing_var)
        print(nothing_var)
        print(nothing_pre + nothing_var)
        continue
    else:
        print(current_page)
        break
