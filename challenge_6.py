import zipfile
import re

nothing_var = "90052"
text = ".txt"
list_files = []
list_comments = []

with zipfile.ZipFile("channel.zip") as file:        # Move it from the Resources folder to the present one
    count = len(file.infolist()) - 1
    for var1 in range(count):
        list_comments.append(file.getinfo(str(nothing_var) + ".txt").comment.decode("utf-8"))
        with file.open(str(nothing_var) + ".txt") as archive:
            for line in archive:
                if re.search("\d+", str(line)):
                    nothing_var = re.findall("\d+", str(line))
                    nothing_var = "".join(nothing_var)
                    list_files.append(nothing_var)
                else:
                    print(line.decode("utf-8"))

print("".join(list_comments))
