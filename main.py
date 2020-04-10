import os
import shutil

icon = "hefftorlinux.svg"

lists = [x for x in os.listdir("icons")]

for x in lists:
    shutil.copy(icon, "icons/" + x + "/scalable/apps/" + icon)
