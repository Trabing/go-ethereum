#!/usr/bin/env python3

import csv


with open('notes/logs/github-authors.log','r') as f:
    with open('notes/logs/github-authors.txt','w') as g:
        rows = set(tuple(a) for a in csv.reader(f))
        writer = csv.writer(g)
        for row in rows:
            writer.writerow(row)
