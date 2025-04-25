import requests

def fetch_and_filter():
    url = 'http://mdxgh.tpddns.cn:9999/new/mdzb.txt'
    
    # 获取文件内容
    response = requests.get(url)
    
    # 使用指定的原始编码（例如 'ISO-8859-1'），并将其转换为 UTF-8
    content = response.content.decode('ISO-8859-1')  # 假设原始编码为 'ISO-8859-1'
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    
    # 保存到新文件，使用 UTF-8 编码
    with open('live_ipv4.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()
