SUFFIX=_qg_test_beam5
BEAM=5
LENPEN=1.5
CHECK_POINT=qg/finetune_qg_checkpoints/prophetnet_large_16G_qg_model.pt
OUTPUT_FILE=qg/output$SUFFIX.txt
SCORE_FILE=qg/score$SUFFIX.txt

fairseq-generate qg/ex --path $CHECK_POINT --user-dir prophetnet --task translation_prophetnet --batch-size 80 --gen-subset tokenized_ex --beam $BEAM --num-workers 4 --no-repeat-ngram-size 3 --lenpen $LENPEN 2>&1 > $OUTPUT_FILE
grep ^H $OUTPUT_FILE | cut -c 3- | sort -n | cut -f3- | sed "s/ ##//g" > qg/sort_hypo$SUFFIX.txt

