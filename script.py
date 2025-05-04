import requests

def fetch_and_filter():
    url = 'https://tv.iill.top/m3u/Gather'
    
    # 获取文件内容
    response = requests.get(url)
    raw_content = response.content  # 获取二进制数据
    
    # 使用 UTF-8 解码
    try:
        content = raw_content.decode('utf-8')
        print("成功使用固定编码: utf-8")
    except UnicodeDecodeError as e:
        raise ValueError(f"解码失败，请检查文件内容是否为 UTF-8 编码: {e}")
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    
    # 保存到新文件，使用 UTF-8 编码
    with open('live_ipv4.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()
