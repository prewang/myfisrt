import pandas as pd

def process_excel(input_file_path, output_file_path):
    # 读取 Excel 文件
    df = pd.read_excel(input_file_path)

    # 示例处理：计算某列的总和
    if '数值列' in df.columns:
        total = df['数值列'].sum()
        print(f"数值列的总和为: {total}")

    # 示例处理：添加新列
    df['新列'] = '示例值'

    # 将处理后的数据保存到新的 Excel 文件
    df.to_excel(output_file_path, index=False)

if __name__ == "__main__":
    input_file = 'input.xlsx'
    output_file = 'output.xlsx'
    process_excel(input_file, output_file)