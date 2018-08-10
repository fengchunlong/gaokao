import requests
from bs4 import BeautifulSoup
import lxml

def get_score(xm='',ksh=''):
    url = "http://www.jledu.gov.cn/chengji_2018.php"  # url地址
    """获取考试成绩"""
    formdata = {'xm': xm.encode('gbk'), 'ksh': ksh}   # 表单参数,对xm进行编码
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7,ja;q=0.6",
        'Cache-Control': "max-age=0",
        'Connection': "keep-alive",
        'Content-Length': '40',
        'Content-Type': "application/x-www-form-urlencoded",
        'Host': "www.jledu.gov.cn",
        'Origin': "http://www.jledu.gov.cn",
        'Referer': "http://www.jledu.gov.cn/",
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    try:
        # post 提交数据
        response = requests.post(url, data=formdata,headers=headers)
        if response.status_code == 200:  # 如果状态码是200，表示请求成功
            return response.text         # 返回页面内容
        return None
    except ConnectionError:              # 连接失败，返回None
        print('Error occurred')
        return None


def parse_page_detail(html_str):
    """解析成绩"""
    soup = BeautifulSoup(html_str,'lxml',) # 常见实例
    info = soup.find_all('td')             # 获取所有<td>标签内容
    data = [x.get_text() for x in info]    # 将考试成绩写入列表
    return data

if __name__ == '__main__':
    result = get_score()                 # 调用get_score获取页面内容
    print(result)
    data = parse_page_detail(result)
    print(data)
