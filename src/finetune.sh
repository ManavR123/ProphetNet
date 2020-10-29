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

echo "Begin Training"
USER_DIR=./prophetnet
ARCH=ngram_transformer_prophet_large
CRITERION=ngram_language_loss
SAVE_DIR=qg/finetune_qg_checkpoints
TENSORBOARD_LOGDIR=qg/finetune_qg_tensorboard
PRETRAINED_MODEL=qg/pretrained_checkpoints/prophetnet_large_pretrained_16G_14epoch_model.pt

fairseq-train \
--user-dir $USER_DIR --task translation_prophetnet --arch $ARCH \
--optimizer adam --adam-betas '(0.9, 0.999)' --clip-norm 0.1 \
--lr 0.00001 --min-lr 1e-09 \
--lr-scheduler inverse_sqrt --warmup-init-lr 1e-07 --warmup-updates 1000 \
--dropout 0.1 --attention-dropout 0.1 --weight-decay 0.01 \
--criterion $CRITERION --label-smoothing 0.1 \
--update-freq 1  --max-tokens 1400 --max-sentences 7 \
--load-from-pretrained-model $PRETRAINED_MODEL \
--ddp-backend=no_c10d --max-epoch 10 \
--max-source-positions 512 --max-target-positions 512 \
--skip-invalid-size-inputs-valid-test \
--save-dir $SAVE_DIR \
--keep-last-epochs 10 \
--tensorboard-logdir $TENSORBOARD_LOGDIR \
$DEST_DIR

echo "Complete"
