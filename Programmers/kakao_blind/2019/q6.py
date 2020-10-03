import re


def solution(word: str, pages: list) -> int:
    word: list = word.lower()
    info_list: list = []

    for index, page in enumerate(pages):
        page = page.lower()
        score = re.sub('[^a-z]+', '.', page).split('.').count(word.lower())
        out_links = re.findall('a href="(.*)"', page)
        my_url = re.findall('<meta property=\"og:url\" content="(.+?)"/>', page)[0]
        info_list.append(PageInfo(score, out_links, index, my_url))

    for i, i_info in enumerate(info_list):
        for j, j_info in enumerate(info_list):
            if i_info.my_url == j_info.my_url:
                continue

            if i_info.my_url in j_info.out_links:
                i_info.link_score += j_info.link_point
        
        # j_info.score += j_info.link_score

    for info in info_list:
        # print(info.score)
        info.score += info.link_score
    info_list.sort(key=lambda x: (x.score, -x.index), reverse=True)    
    return info_list[0].index


class PageInfo(object):
    def __init__(self, basic_score: int, out_links: list, index: int, my_url: str):
        self.out_links: list = out_links 
        self.index: int = index
        self.my_url: str = my_url
        self.link_point = basic_score / len(out_links) if len(out_links) != 0 else 0
        self.score: int = basic_score
        self.link_score: int = 0


if __name__ == '__main__':
    print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
    print()
    print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2 <a href=\"https://Hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))