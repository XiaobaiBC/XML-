import os
import xml.etree.ElementTree as ET

# 指定文件夹路径
folder_path = r"C:\xxx\"

# 定义命名空间
namespaces = {
    'nfe': 'http://www.portalfiscal.inf.br/nfe'
}

# 打开文件1.txt以写入模式，处理完毕后关闭文件
with open("1.txt", "w", encoding="utf-8") as output_file:
    # 遍历文件夹中的所有XML文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            file_path = os.path.join(folder_path, filename)

            try:
                # 解析XML文件
                tree = ET.parse(file_path)
                root = tree.getroot()

                # 查找支付金额vPag元素
                vPag_element = root.find('.//nfe:vPag', namespaces)

                # 提取支付金额的值
                if vPag_element is not None:
                    vPag_value = vPag_element.text
                    output_file.write(f"{filename} - {vPag_value}\n")
                else:
                    output_file.write(f"文件: {filename} - 未找到支付金额vPag元素\n")
            except ET.ParseError:
                output_file.write(f"文件: {filename} - 解析错误\n")
