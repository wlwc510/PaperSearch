import urllib.request
import ssl
from bs4 import BeautifulSoup

def url2bsObj(url):
    ssl._create_default_https_context = ssl._create_stdlib_context
    # 网址

    headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
               'Connection': 'keep-alive'
               }
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read()

    data = data.decode('utf-8')
    bsObj = BeautifulSoup(data,'html.parser')
    return bsObj


######设定总共爬多少页
totalPageNum = 100

for num in range(1,totalPageNum):
    url = "https://www.nature.com/subjects/physical-sciences/ncomms?searchType=journalSearch&sort=PubDate&page=" + str(num)
    ######起始url
    # url = "https://www.nature.com/subjects/physical-sciences/ncomms?searchType=journalSearch&sort=PubDate&page=1"
    ul = url2bsObj(url).find("ul",{"class":"ma0 mb-negative-2 clean-list"})
    host = "https://www.nature.com"

    for child in ul.children:
        try:
            # print(child)
            chis = child.find("h3",{"class":"mb10 extra-tight-line-height word-wrap"})
            href = chis.find("a")
            paperUrl = host + href.attrs['href']
            print(href.text.strip())
            print(paperUrl)

            ########根据超链接，爬文章，并解析########
            currentbsObj = url2bsObj(paperUrl)
            title = currentbsObj.find("h1", {"data-test": "article-title"}).get_text().replace("\n", "")
            print(title)
            content = currentbsObj.find("div", {"data-track-component": "article body"})

            for chd in content.children:
                try:
                    if (chd.attrs["aria-labelledby"] == "Abs1"):
                        Abs1_content = chd.find("div", {"id": "Abs1-content"})
                        print("======Abs1_content=============================================")
                        print(Abs1_content.get_text())

                    if (chd.attrs["aria-labelledby"] == "Sec1"):
                        Sec1_content = chd.find("div", {"id": "Sec1-content"})
                        print("======Sec1_content=============================================")
                        print(Sec1_content.get_text())

                    if (chd.attrs["aria-labelledby"] == "Sec2"):
                        Sec2_content = chd.find("div", {"id": "Sec2-content"})
                        print("======Sec2_content=============================================")
                        print(Sec2_content.get_text())

                    if (chd.attrs["aria-labelledby"] == "Sec6"):
                        Sec6_content = chd.find("div", {"id": "Sec6-content"})
                        print("======Sec6_content=============================================")
                        print(Sec6_content.get_text())

                    if (chd.attrs["aria-labelledby"] == "Sec7"):
                        Sec7_content = chd.find("div", {"id": "Sec7-content"})
                        print("======Sec7_content=============================================")
                        print(Sec7_content.get_text())

                    if (chd.attrs["aria-labelledby"] == "data-availability"):
                        data_availability_content = chd.find("div", {"id": "data-availability-content"})
                        print("======data_availability_content=============================================")
                        print(data_availability_content.get_text())

                    if (chd.attrs["aria-labelledby"] == "additional-information"):
                        additional_information_content = chd.find("div", {"id": "additional-information-content"})
                        print("======additional_information_content=============================================")
                        print(additional_information_content.get_text())

                    if (chd.attrs["aria-labelledby"] == "Bib1"):
                        Bib1_content = chd.find("div", {"id": "Bib1-content"})
                        print("======Bib1_content=============================================")
                        print(Bib1_content.get_text())
                except:
                    continue

        except:
            continue
