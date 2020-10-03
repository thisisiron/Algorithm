import re


def solution(files: list) -> list:
    answer = []
    for f_name in files:
        result: list = re.split('(\d+)', f_name)
        tail: str = "".join(result[2:]) if len(result) > 2 else ""
        answer.append([result[0], result[1], tail])

    custom_sort(answer) 

    answer = [''.join(x) for x in answer]
    
    return answer


def custom_sort(arr: list):
    arr.sort(key=lambda x: (x[0].upper(), int(x[1])))



if __name__ == '__main__':
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
    print(solution(["foo010bar020.zip"]))