MAIN_DIR=qg/${1}

echo "Tokenizing data"
python data_tokenize.py --input ${MAIN_DIR}/${1}.txt
python data_tokenize.py --input ${MAIN_DIR}/${1}_q.txt

#echo "Generating src and tgt files"
python process_data.py --input ${MAIN_DIR}/tokenized_${1}.txt --output ${MAIN_DIR}/${1}.src --src
python process_data.py --input ${MAIN_DIR}/tokenized_${1}_q.txt --output ${MAIN_DIR}/${1}.tgt --tgt

echo "Fairseq Preprocess"
DEST_DIR=qg/${1}/processed

fairseq-preprocess \
--user-dir prophetnet \
--task translation_prophetnet \
--source-lang src --target-lang tgt \
--trainpref qg/${1}/${1} \
--destdir $DEST_DIR --srcdict vocab.txt --tgtdict vocab.txt \
--workers 20

echo "Generating questions"
BEAM=5
NBEST=5
TOP=0.95
LENPEN=1.5
CHECK_POINT=qg/finetune_qg_checkpoints/prophetnet_large_16G_qg_model.pt
OUTPUT_FILE=qg/${1}/${1}_output.txt
TEMP_FILE=qg/${1}/${1}_score.txt

fairseq-generate $DEST_DIR --path $CHECK_POINT --user-dir prophetnet --task translation_prophetnet --batch-size 1 --gen-subset train --sampling --sampling-topp $TOP --nbest $NBEST --num-workers 4 --no-repeat-ngram-size 3 --lenpen $LENPEN 2>&1 > $TEMP_FILE
grep ^H $TEMP_FILE | cut -c 3- | sort -n | cut -f3- | sed "s/ ##//g" > $OUTPUT_FILE

echo "Complete"
