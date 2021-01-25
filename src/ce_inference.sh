bash predict.sh textbook_ce  qg/finetune_qg_checkpoints/squad_gold_train/checkpoint_last.pt
mv qg/textbook_ce/textbook_ce_output.txt/ qg/textbook_ce/textbook_ce_squad_gold.txt

bash predict.sh squad_ce  qg/finetune_qg_checkpoints/squad_gold_train/checkpoint_last.pt
mv qg/squad_ce/squad_ce_output.txt/ qg/squad_ce/squad_ce_squad_gold.txt

bash predict.sh textbook_ce  qg/finetune_qg_checkpoints/synqg_train/checkpoint_last.pt
mv qg/textbook_ce/textbook_ce_output.txt/ qg/textbook_ce/textbook_ce_synqg.txt

bash predict.sh squad_ce  qg/finetune_qg_checkpoints/synqg_train/checkpoint_last.pt
mv qg/squad_ce/squad_ce_output.txt/ qg/squad_ce/squad_ce_synqg.txt

bash predict.sh textbook_ce  qg/finetune_qg_checkpoints/combined_train/checkpoint_last.pt
mv qg/textbook_ce/textbook_ce_output.txt/ qg/textbook_ce/textbook_ce_combined.txt

bash predict.sh squad_ce  qg/finetune_qg_checkpoints/combined_train/checkpoint_last.pt
mv qg/squad_ce/squad_ce_output.txt/ qg/squad_ce/squad_ce_combined.txt
