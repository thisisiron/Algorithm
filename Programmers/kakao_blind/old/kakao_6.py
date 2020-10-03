class info():
    def __init__(self, i, me, basic_score, link=[], link_score=0):
        self.idx = i
        self.url = me
        self.basic_score = basic_score
        self.link_score = link_score
        self.link = link
        self.total = basic_score
    
import re

def solution(word, pages):
    answer = 0
    N = len(pages)
    web_pages = []
    word = word.lower()
    for i,page in enumerate(pages):
        page = page.lower()
        me = re.findall(r'content="(.*)"', page)
        basic_score = len(re.findall(r'\b(%s)[\d*|\s*|\W*]' % word, page))
        link = re.findall(r'<a href="(.*)">', page)
        if len(link)!=0:
            link_score = basic_score / len(link)
        else:
            link_score = 0
        web_pages.append(info(i, me, basic_score, link, link_score))

    for page in web_pages:
        for a_tag in page.link:
            for search_page in web_pages:
                if a_tag == search_page.url[0]:
                    search_page.total += page.link_score
    
    web_pages.sort(key=lambda x:x.total,reverse=True)


    for page in web_pages:
        print(page.idx,':',page.total, ', ', page.basic_score)

    return web_pages[0].idx


print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print('----------------------')
print(solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))