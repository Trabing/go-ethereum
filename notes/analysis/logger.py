#!/usr/bin/env python3

import csv


with open('../logs/github-authors.log','r') as f:
    with open('../logs/github-authors.txt','w') as g:
        rows = csv.reader(f)
        rows = set(tuple(a) for a in rows)
        writer = csv.writer(g)
        for row in rows:
            writer.writerow(row)
