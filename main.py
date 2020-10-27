# -- coding: utf-8 --

from googletrans import Translator
import csv


PL = "PL"
ENG = "EN"

translator = Translator()

with open('in.tsv') as f:
    with open('out.tsv', 'a+') as out:
        out_tsv = csv.writer(out)
        sentence = f.readline()
        while sentence is not None or sentence != "":
            print(sentence.replace('\n', ''))
            translation = translator.translate(sentence, dest=ENG, source=PL)

            print(translation.text.replace('\n', ''), '\n')
            out_tsv.writerow({translation.text})
            sentence = f.readline()
