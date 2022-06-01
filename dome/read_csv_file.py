import csv
with open("../data/ji.csv", encoding="utf_8") as f:
    con = csv.reader(f)
    header = next(con)
    with open("../data/zheng.csv", "w", encoding="utf_8", newline="") as w:
        wf = csv.writer(w)
        wf.writerow(header)
        for i in con:
            if float(i[6]) > 0:
                wf.writerow(i)
