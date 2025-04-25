import requests
import chardet

def fetch_and_filter():
    url = 'http://mdxgh.tpddns.cn:9999/new/mdzb.txt'
    
    # 获取文件内容
    response = requests.get(url)
    raw_content = response.content  # 获取二进制数据
    
    # 自动检测原始编码
    detected_encoding = chardet.detect(raw_content)['encoding']
    if not detected_encoding:
        raise ValueError("无法检测到编码，请手动指定文件编码。")
    print(f"检测到的编码: {detected_encoding}")
    
    # 使用检测到的编码进行解码，并设置错误处理策略为 'replace'
    try:
        content = raw_content.decode(detected_encoding, errors='replace')  # 替换无法解码的字符
    except UnicodeDecodeError as e:
        raise ValueError(f"解码失败: {e}")
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    
    # 保存到新文件，使用 UTF-8 编码
    with open('live_ipv4.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()
