# ProphetNet-CausalQG

This branch of the repo contains all of the code used to produced the questions used in [CausalQG](https://github.com/kstats/CausalQG). This is simply a fork of the ProphetNet repo with a few scripts to automate the question generation process on user given data.

## QG Model Weights

- [ProphetNet-large-16GB](https://drive.google.com/file/d/1IiutfQp_Q5ggQErcdKd2byuAEnwzC09I/view) (fine-tuned on SQuAD with 5 epochs)

Store thix in `src/qg/pretrained_checkpoints`.

## How to Use

### Question Generation

You should store CSVs of your data in `src/qg/<folder-name>`. They should have the following format:

```
Text, Cause, Effect
```

Make sure your CSV has the same name as the directory it is stored. For example, if your data is in `squad_ce.csv`, it should be stored as `src/qg/squad_ce/squad_ce.csv`. Ensuring they are the same is crucial for the scripts to function.

To convert this CSV into a format usable by Fairseq, use `prophetnet_causal_process.py` while in the `src/qg/` directory. For example,

```
cd src/qg
python prophetnet_causal_process.py --dirname squad_ce --input
```

After this step, in your folder you will see 2 new files in your folder: `dirname.txt` and `dirname_q.txt`. Note: the `dirname_q.txt` just contains "nothing?" repeated because Fairseq doesn't directly support free-form generation, only comparison to some ground truth. However, this ground truth doesn't affect the generated output, so we generated dummy ground truth.

Now, we are reading to generate questions. Move back to the `src/` directory. The `predict.sh` scripts handles tokenizing all of the data and then running the generation process. Ther are 2 ordered arguments to this script:

1) dirname - the name of the directory stored in `qg` folder. DO NOT add the `qg/` portion to this path. Simply use the dirname.

2) (Optional) Path to pretrained weights. If you don't specify it will default to the folder `qg/pretrained_checkpoints/prophetnet_large_16G_qg_model.pt`, which is where the original ProphetNet suggested adding the weights.

Example usage:
```
bash predict.sh squad_ce # default qg weights
bash predict.sh squad_ce qg/finetuned_weights/qg_trained.pt # custom weights
```

This script makes calls to 2 python scripts for tokenzing the input data (`data_tokenize.py`) and for fixing casing (`process_data.py.py`). It then runs `fairseq-preprocess` and then `fairseq-generate`.

This script will create a `dirname_ouput.txt` file in the specific directory. This will have all of the generated questions. Now, go back into the `qg/` folder. You can use the same `prophet_causal_process.py` file to add the generated questions back into the original CSV. Simply run:

```
python prophet_causal_process.py --output dirname --output
```

The original CSV will now have the following format:

```
Text, Cause, Effect, cause_question, effect_question
```

### Finetuning

You should store CSVs of your data in `src/qg/<folder-name>`. They should have the following format:

```
context, question
```

Make sure your CSV has the same name as the directory it is stored. For example, if your data is in `squad_ce.csv`, it should be stored as `src/qg/squad_ce/squad_ce.csv`. Ensuring they are the same is crucial for the scripts to function.

To convert this CSV into a format usable by Fairseq, use `finetune_process.py` while in the `src/qg/` directory. For example,

```
cd src/qg
python finetune_process.py --dirname dirname
```

After this step, in your folder you will see 2 new files in your folder: `dirname.txt` and `dirname_q.txt`.

To begin the finetuning process, go up a level to the `src/` directory. Use the `finetune.sh` to finetune the QG model. This requires having the original weights from the ProphetNet repo.

You can change the hyperparameters for finetuning by modifiyng the values directly in the `finetune.sh` script.'

## Misc

There are a few miscelleanous scripts in the `src/` folder that contain the runs of experiments we did. They aren't of much importance. You can also see in the git history the data we used and how it is formatted. We recommended re-creating it yourself following the steps in [CausalQG](https://github.com/kstats/CausalQG).

## Questions

If you have any questions about anything related to this repo, let us know!
