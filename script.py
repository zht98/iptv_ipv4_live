import requests

def fetch_and_filter():
    url = 'https://media-jxnc-fy-person01.jx6oss.ctyunxs.cn/PERSONCLOUD/9f92d85e-13e6-4fb1-97b4-8e402293d285.nzk?response-content-disposition=attachment%3Bfilename%3D%22gggg.nzk%22%3Bfilename*%3DUTF-8%27%27gggg.nzk&x-amz-CLIENTNETWORK=UNKNOWN&x-amz-CLOUDTYPEIN=PERSON&x-amz-CLIENTTYPEIN=PC&Signature=0p%2B0dLb4CmTP6agP95uCP2odbWI%3D&AWSAccessKeyId=0Lg7dAq3ZfHvePP8DKEU&x-amz-userLevel=100&Expires=1745585805&x-amz-limitrate=51200&x-amz-FSIZE=607298&x-amz-UID=672532495&x-amz-UFID=624201191216557947'
    
    # 获取文件内容
    response = requests.get(url)
    content = response.text
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    
    # 保存到新文件
    with open('live_ipv4.txt', 'w') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()
