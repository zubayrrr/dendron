#!/usr/bin/python3

import os, sys, json
import datetime

link = str(sys.argv[1])
print("Processing " + link)

resp = json.loads(os.popen("mercury-parser " + link + " --format=markdown").read())
today = datetime.datetime.now()

out_content = resp["content"]
out_title   = resp["title"]
out_url     = resp["url"]
out_domain  = resp["domain"]
out_wc      = resp["word_count"]
if resp["author"]:
    out_author = resp["author"]
else:
    out_author = "Unknown"

# Ewww, www
if "www." in out_domain:
    out_domain = out_domain.replace("www.", "")

if resp["lead_image_url"]:
    out_lead_img = resp["lead_image_url"]
    header = "* **Source:** [" + out_domain + "](" + out_url + ")\n* **Author:** " + out_author + "\n* **Word count:** " + str(out_wc) + "\n* **Extracted at:** " + today.strftime("%Y-%m-%d %H:%M") + "\n\n"
    content = "# " + out_title + "\n\n" + header + "![lead image](" + out_lead_img + ")\n\n" + out_content
else:
    header = "* **Source:** [" + out_domain + "](" + out_url + ")\n* **Author:** " + out_author + "\n* **Word count:** " + str(out_wc) + "\n* **Extracted at:** " + today.strftime("%Y-%m-%d %H:%M") + "\n\n---\n\n"
    content = "# " + out_title + "\n\n" + header + out_content

# Formats the title of the file
title = today.strftime("%Y%m%d-" + out_title)
title = title.lower()
for ch in [" ", " "]:
    if ch in title:
        title = title.replace(ch, "-")
for ch in ["'", ",", "’"]:
    if ch in title:
        title = title.replace(ch, "")

# Writes to the actual file
f = open(os.path.join(os.pardir, "links/" + title + ".md"), "w")
f.write(content)
f.close()

print("Done!")
