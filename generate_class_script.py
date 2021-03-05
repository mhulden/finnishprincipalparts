LEX = ["valo","palvelu","valtio","laatikko","risti","paperi","ovi","nalle",
       "kala","koira","omena","kulkija","katiska","solakka","korkea",
       "vanhempi","vapaa","maa","suo","filee","rosé","parfait","tiili",
       "uni","toimi","pieni","käsi","kynsi","lapsi","veitsi","kaksi",
       "sisar","kytkin","onneton","lämmin","sisin","vasen","nainen",
       "vastaus","kalleus","vieras","mies","ohut","kevät","kahdeksas",
       "tuhat","kuollut","hame"];

EXPR = 'define LEMMA [ID ["|" {LEMMA}]^14  .o. Gr .o. ~$["|"] .o. [[..] -> " " || [GENPL1|GENPL2|GENPL3|GENSG|ILLPL1|ILLPL2|ILLPL3|ILLSG|NOMPL|NOMSG|PARTPL1|PARTPL2|PARTSG1|PARTSG2] _ ] ];'

if __name__=="__main__":
    for i, lex in enumerate(LEX):
        print(EXPR.replace("ID",str(i+1)).replace("LEMMA",lex))

    fst = "regex " + "|".join(LEX) + ";"
    
    print(fst)
    
    print("lower-words")
