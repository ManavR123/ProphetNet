fairseq-preprocess \
--user-dir prophetnet \
--task translation_prophetnet \
--source-lang src --target-lang tgt \
--trainpref qg/ex/tokenized_ex \
--destdir qg/ex_processed --srcdict ./vocab.txt --tgtdict ./vocab.txt \
--workers 20
