import requests
import chardet

def fetch_and_filter():
    url = 'http://mdxgh.tpddns.cn:9999/new/mdzb.txt'
    
    # 获取文件内容
    response = requests.get(url)
    raw_content = response.content  # 获取二进制数据
    
    # 自动检测原始编码
    detected_encoding = chardet.detect(raw_content)['encoding']
    print(f"检测到的编码: {detected_encoding}")
    
    # 如果检测到的编码无效，尝试常见的中文编码
    possible_encodings = [detected_encoding, 'utf-8', 'gbk', 'gb2312', 'big5']
    
    content = None
    for encoding in possible_encodings:
        if not encoding:
            continue
        try:
            content = raw_content.decode(encoding)
            print(f"成功使用编码: {encoding}")
            break
        except (UnicodeDecodeError, LookupError):
            print(f"尝试编码失败: {encoding}")
    
    if content is None:
        raise ValueError("无法解码文件内容，请手动检查编码。")
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    
    # 保存到新文件，使用 UTF-8 编码
    with open('live_ipv4.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()
