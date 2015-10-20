# sou-hack-word2vec
Topic analysis and word2vec workgroup from SOU Hack 2015-10-20

# Vad?
En applikation som låter användaren skriva in ett ord och få ut relaterade ord årtionde för årtionde

# Minimimål
Vi väljer ut några ord och kör dem "manuellt" mot alla våra modeller (en modell per årtionde)

# Extra
* script som låter användaren köra ett ord mot alla årtionden
* visualisering
* GUI
* Analysera begrepp istället för ord

# Användning
För att skapa en model från en textfil:
python create_word2vec_model.py -i [input-file] -0 [output-file]
Exempel:
'python create_word2vec_model.py -i "/Users/mos/Downloads/SOUtxtDecadeFiles/30talstortxtfil.txt" -o "/Users/mos/Dropbox/projects/sou-hack-word2vec/30tal.model"

För att få ut topp 10 relaterade ord för en viss textfil sparad som word2vec-modell:
python word_similarity_word2vec -m [model] -w [word]
Exempel:
'python word_similarity_word2vec -m "/Users/mos/Dropbox/projects/sou-hack-word2vec/models/model-20.pickle" -w "demokrati"