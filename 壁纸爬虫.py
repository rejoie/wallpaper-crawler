# import urllib.request, urllib.error, re
# from bs4 import BeautifulSoup
#
# findpicture = re.compile(r'<img\salt=.*?src="(.*?.jpg)"/>')
#
#
# def main():
#     baseurl = 'http://pic.netbian.com/4kdongman/index'
#     datalist = getData(baseurl)
#     savepath = './壁纸/'
#     savePicture(datalist, savepath)
#
#
# # 爬取网页
# def getData(baseurl):
#     datalist = []
#     for i in range(1, 149):
#         if i == 1:
#             url = baseurl + '.html'
#         else:
#             url = baseurl + '_' + str(i) + '.html'
#         html = askURL(url)
#         soup = BeautifulSoup(html, 'html.parser')
#         # 解析数据
#         # class加下划线表示属性值
#         for item in soup.find_all('li'):
#             item = str(item)
#             link = re.findall(findpicture, item)
#             if link:
#                 datalist.append(link[0])
#
#     return datalist
#
#
# def askURL(url):
#     head = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
#     }
#     request = urllib.request.Request(url, headers=head)
#     html = ''
#     try:
#         response = urllib.request.urlopen(request)
#         html = response.read()
#         print(html)
#     except urllib.error.URLError as e:
#         # hasattr函数判断对象是否包含对应属性
#         if hasattr(e, 'code'):
#             print(e.code)
#         if hasattr(e, 'reason'):
#             print(e.reason)
#
#     return html
#
#
# def savePicture(datalist, path):
#     i = 0
#     for link in datalist:
#         i += 1
#         with open(path + '{}.jpg'.format(i), 'wb') as p:
#             p.write(urllib.request.urlopen('http://pic.netbian.com' + link).read())
#             print('正在下载第{}张图片'.format(i))
#     return
#
#
# if __name__ == '__main__':
#     main()
#     print('爬取完毕')

# p站
import urllib.request, urllib.error, re

findpicture = re.compile(r'<img\ssrc="(.*?)"')


def main():
    baseurl = 'https://www.huashi6.com/search?searchText=r18'
    datalist = getData(baseurl)
    print(datalist)
    savepath = './壁纸/'
    savePicture(datalist, savepath)


# 爬取网页
def getData(baseurl):
    url = baseurl
    html = askURL(url)
    link = re.findall(findpicture, html.decode('utf-8'))

    return link


def askURL(url):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
    except urllib.error.URLError as e:
        # hasattr函数判断对象是否包含对应属性
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

    return html


def savePicture(datalist, path):
    i = 0
    for link in datalist:
        i += 1
        with open(path + '{}.jpg'.format(i), 'wb') as p:
            p.write(urllib.request.urlopen('http://pic.netbian.com' + link).read())
            print('正在下载第{}张图片'.format(i))
    return


if __name__ == '__main__':
    main()
    print('爬取完毕')
