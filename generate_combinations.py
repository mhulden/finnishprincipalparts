from sys import argv

from itertools import combinations
from generate_class_script import LEX

from collections import defaultdict

def get_tag(form):
    return ''.join([c for c in form if c.isupper()])

def group(forms):
    groups = defaultdict(list)
    for form in forms:
        if form[-1] in "123":
            groups[get_tag(form[:-1])].append(form)
        else:
            groups[get_tag(form)].append(form)
    return groups

if __name__=="__main__":
    all_forms = open(argv[1]).read().split("\n")
    
    for forms in all_forms:
        forms = forms.strip().split(" ")
        forms = group(forms)
        for i in range(1, 12):
            for comb in combinations(list(forms.keys()),i):     
                print("".join([''.join(forms[c]) for c in comb]))
