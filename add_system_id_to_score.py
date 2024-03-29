new_score = {}
with open("predictions/scores.txt", "r") as file:
    # 逐行读取文件内容
    for line in file:
        # 去除行尾的换行符
        line = line.strip()
        # 使用逗号分割行数据
        columns = line.split(" ")
        new_score[columns[0]] = columns[1]


# 打开文件A以读取内容
with open(
    "/data_hdd/lx20/ty_workspace/SSL_Anti-spoofing/output/eval_CM_scores_file_SSL_LA_denoised-samo.txt",
    "r",
) as file_a:
    lines = file_a.readlines()

# 处理每一行，将最后一列替换成1
modified_lines = []
for line in lines:
    # 分割每行内容，假设以空格分隔
    columns = line.strip().split()
    if columns:
        # 将最后一列替换成1
        columns[-1] = new_score[columns[0]]
        # 重新组合每行内容
        modified_line = " ".join(columns)
        modified_lines.append(modified_line)

# 打开文件B以写入处理后的内容
with open("predictions/scores_with_system_id.txt", "w") as file_b:
    file_b.writelines("\n".join(modified_lines))
