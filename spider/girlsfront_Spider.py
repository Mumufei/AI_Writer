import requests
import re

url = "https://zh.moegirl.org"
url_init = "https://zh.moegirl.org/%E5%B0%91%E5%A5%B3%E5%89%8D%E7%BA%BF"
response = requests.get(url_init)
urlData_list = re.findall("<li><a href=.*? ", re.findall("<ul><li>常規地圖[\s\S]*?</div>", response.text)[0])
titleData_list = re.findall("title=.*?</li>", re.findall("<ul><li>常規地圖[\s\S]*?</div>", response.text)[0])
url_list = []
title_list = []
for s in urlData_list:
    s = s.replace("<li><a href=\"", "").replace("\" ", "")
    url_list.append(s)
    #print(url)
for s in titleData_list:
    s = s.replace("title=\"", "").replace("\">", "").replace("/", "_").replace(":", "_")
    s = re.sub("<.*?>", "", s)
    title_list.append(s)
    #print(title)
filehandle = open("test.txt", "w", encoding="UTF-8")
filehandle.write(response.text)
filehandle.close()

# url_data = "%s%s" % (url, url_list[1])
# print(title_list[1], url_data)
# response = requests.get(url_data)
# data = response.text
#     # data_list = re.findall("剧情文本[\s\S]*?table", data)
#     # if len(data_list) > 1:
#     #     data = data_list[-1].replace("剧情文本\">剧情文本</span></h2>", "")
#     #     data = re.sub("<.*?>", "", data)
#     #     filehandle = open("%s.txt" % title_list[2], "w", encoding="UTF-8")
#     #     filehandle.write(data)
#     #     filehandle.close()
# filehandle = open("%s.txt" % title_list[1], "w", encoding="UTF-8")
# filehandle.write(data)
# filehandle.close()
print(len(title_list), len(url_list))
for i in range(0, len(title_list)):
    url_data = "%s%s" % (url, url_list[i])
    print(title_list[i], url_data)
    response = requests.get(url_data)
    data = response.text
    data_list = re.findall("id=\"剧情文本\">剧情文本</span></h2>[\s\S]*?</div> <div class=\"printfooter\">", data)
    if len(data_list) > 0:
        data = data_list[0].replace("剧情文本\">剧情文本</span></h2>", "")
        data = re.sub("<.*?>", "", data)
        filehandle = open("%s.txt" % title_list[i], "w", encoding="UTF-8")
        filehandle.write(data)
        filehandle.close()