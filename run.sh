# processed_data 中是 preprocess.py 生成的文件列表。如果使用新的数据集，没有该列表，则需要用 preprocess.py 重新生成；如果 processed_data 已有，则不必再生成。
# processed_data 中的 json 可能标签全是 spoof，需要重新生成。
# 训练的模型位于 results\
# 在 SpoofSpeechClassifier.yaml 中指定模型名，或者在命令行中使用 --model=trained_on_19LAsilence 来 override
# eval_annotation 为要评估的文件列表
# eval.py 中的 gt_file 可能需要修改
python3 train_spoofspeech.py eval yaml/SpoofSpeechClassifier.yaml --model=trained_on_19LAsilence
python3 eval.py
