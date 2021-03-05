# finnishprincipalparts

## Running `find_prparts.py`

**STEP 1:** Generate class scripts (these are used for extracting WF+TAG combinations for each example lexeme from the grammar)

```
$ python3 generate_class_script.py
```
You should get output which looks like this:
```
define valo [1 ["|" {valo}]^14  .o. Gr .o. ~$["|"] .o. [[..] -> " " || [GENPL1|GENPL2|GENPL3|GENSG|ILLPL1|ILLPL2|ILLPL3|ILLSG|NOMPL|NOMSG|PARTPL1|PARTPL2|PARTSG1|PARTSG2] _ ] ];
define palvelu [2 ["|" {palvelu}]^14  .o. Gr .o. ~$["|"] .o. [[..] -> " " || [GENPL1|GENPL2|GENPL3|GENSG|ILLPL1|ILLPL2|ILLPL3|ILLSG|NOMPL|NOMSG|PARTPL1|PARTPL2|PARTSG1|PARTSG2] _ ] ];
...
```

**STEP 2:** Generate WF+TAG combinations

Start foma using 
```
$ foma -l fi-gr-parallel.foma
```
Copy-paste the output of `generate_class_script.py` into foma and execute all commands including `lower-words`. You should get output which looks like this:
```
valoNOMSG valonGENSG valoaPARTSG1 valoPARTSG2 valoonILLSG valotNOMPL valojenGENPL1 valoGENPL2 valoGENPL3 valojaPARTPL1 valoPARTPL2 valoILLPL1 valoihinILLPL2 valoILLPL3 
palveluNOMSG palvelunGENSG palveluaPARTSG1 palveluPARTSG2 palveluunILLSG palvelutNOMPL palvelujenGENPL1 palveluidenGENPL2 palveluittenGENPL3 palvelujaPARTPL1 palveluitaPARTPL2 palveluILLPL1 palveluihinILLPL2 palveluILLPL3 
...
```

Store the output in a file `FORMS`

**STEP 3:** Generate combinations of forms

Run: 
```
$ python3 generate_combinations.py FORMS > COMBINATIONS
```
The output file (which will be a fairly long file) should look like this:
```
valoNOMSG
valonGENSG
valoaPARTSG1valoPARTSG2
valoonILLSG
valotNOMPL
valojenGENPL1valoGENPL2valoGENPL3
valojaPARTPL1valoPARTPL2
valoILLPL1valoihinILLPL2valoILLPL3
...
```

**STEP 4:** Perform foma lookup

Run:
```
$ flookup fi-gr-parallel.fomabin < COMBINATIONS > COMBINATIONS.out
```
The output should look like this:
```
valoNOMSG       48|valo
valoNOMSG       2|valo
valoNOMSG       3|valo
valoNOMSG       4|valo
valoNOMSG       5|valo
valoNOMSG       6|valo
valoNOMSG       8|valo
valoNOMSG       9|valo
...
```

**STEP 5**: Identify principal parts
Run
```
$ python3 find_prparts.py COMBINATIONS.out 
```
The output should look like this:
```
MINIMAL PPARTS SET SIZE: 5
{'GENPL', 'PARTPL', 'ILLSG', 'PARTSG', 'GENSG'}
{'GENPL', 'ILLSG', 'PARTSG', 'GENSG', 'ILLPL'}
{'NOMPL', 'GENPL', 'PARTPL', 'ILLSG', 'PARTSG'}
{'NOMPL', 'GENPL', 'ILLSG', 'PARTSG', 'ILLPL'}
```
