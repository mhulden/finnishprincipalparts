from sys import argv
from re import sub
from collections import defaultdict

def read_foma_output(fn):
    outputs = [[]]
    inputs = ["DUMMY"]
    for line in open(fn):
        line = line.strip()
        if line:
            input, output = line.split("\t")
            if inputs[-1] == "DUMMY":
                inputs[-1] = input
            ofields = output.split("|")
            outputs[-1].append((int(ofields[0]), list(set(ofields[1:]))))
        else:
            outputs.append([])
            inputs.append("DUMMY")

    return [i for i in inputs if i != "DUMMY"], [o for o in outputs if o != []]

def filter_inconsistent_sets(outputs):
    return [[o for o in output if len(o[1]) == 1] for output in outputs]

def filter_insufficient_sets(inputs, outputs):
    return zip(*[(i,o) for i,o in zip(inputs,outputs) if len(o) == 1])

def reduce_sets(inputs):
    return [sub(r"[a-zåäö'é]+","+",i) for i in inputs]

def collapse_forms(forms):
    return {sub(r"[0-9]","",form) for form in forms.split("+") if form}

if __name__=="__main__":
    inputs,outputs = read_foma_output(argv[1])
    assert(len(inputs) == len(outputs))
    
    outputs = filter_inconsistent_sets(outputs)
    inputs, outputs = filter_insufficient_sets(inputs, outputs)

    inputs = reduce_sets(inputs)
    
    all_lem = set()
    paradigm_dict = defaultdict(set)
    for i, o in zip(inputs,outputs):
        lemma = o[0][1][0]
        all_lem.add(lemma)
        paradigm_dict[i].add(lemma)

    print("AFTER FILTERING %u CLASSES REMAIN." % len(all_lem))
    min_count = 1000
    min_forms = []

    for forms, lemmas in paradigm_dict.items():
        forms = collapse_forms(forms)
        if len(all_lem.difference(lemmas)) == 0: 
            if len(forms) < min_count:
                min_count = len(forms) 
                min_forms = [forms]
            elif len(forms) == min_count:
                min_forms.append(forms)

    print("MINIMAL PPARTS SET SIZE:",min_count)
    for forms in min_forms:
        print(forms)
