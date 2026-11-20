"""
Build iclr2027/data.json (the ICLR 2027 score-percentile page's data) from an OpenReview download.

The download: ~/Desktop/iclr2027_percentiles_v2.py (needs an openreview.net login) writes
iclr2027_ratings_<YYYY_MM_DD_HHMM>.csv with one row per paper: id, title, ratings, avg, venueid, confidences,
conf_weighted_avg (ratings and confidences in the same review order).

Run:  python3 _tools/iclr2027_build_data.py ~/Desktop/iclr2027_ratings_2026_11_20_1720.csv "2026-11-20 17:20 GMT"
      (the second argument is the download's UK time, shown on the page)

data.json: {"downloaded", "papers": [[id, title, ratings, confidences, status], ...]}; ratings and confidences are
digit strings in review order ("332" = 3, 3, 2), status 0 = under review, 1 = withdrawn, 2 = desk-rejected.
Jekyll does not publish folders starting with "_", so this script is not on the site.
"""
import csv
import json
import os
import sys

src, when = sys.argv[1], sys.argv[2]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "iclr2027", "data.json")
STATUS = {"Submission": 0, "Withdrawn_Submission": 1, "Desk_Rejected_Submission": 2}


def digits(s):
    vals = [float(x) for x in s.split(";")]
    assert all(v.is_integer() and 0 <= v <= 9 for v in vals), s   # one digit per score (ICLR 2027: 1-4)
    return "".join(str(int(v)) for v in vals)


papers, skipped = [], 0
for r in csv.DictReader(open(src, newline="")):
    rs, cs = r["ratings"].split(";"), r["confidences"].split(";")
    if len(rs) != len(cs) or "" in cs:
        skipped += 1
        continue
    papers.append([r["id"], r["title"].strip(), digits(r["ratings"]), digits(r["confidences"]),
                   STATUS[r["venueid"].split("/")[-1]]])

with open(out, "w") as f:
    json.dump({"downloaded": when, "papers": papers}, f, ensure_ascii=False, separators=(",", ":"))
print(f"{len(papers)} papers ({skipped} skipped: a review without a confidence) -> {os.path.normpath(out)}"
      f" ({os.path.getsize(out) / 1e6:.1f} MB)")
