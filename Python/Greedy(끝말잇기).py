# 끝말잇기는 1. 중복된 단어가 나오거나 2. 이전 단어의 끝 단어와 현재 단어의 맨 앞 단어가 일치하지 않을 경우에 틀린다.
# words_a를 list로 두고 words를 돌면서 중복되거나 이전 마지막 문자와 겹치지 않으면 index를 매긴다
# n으로 나눠서 몫+1과 나머지를 results로 반환한다


def solution(n, words):
    for i in range(len(words)):
        if i >= 1:
            if words[i][0] != words[i - 1][-1]:
                if (i + 1) % n == 0:
                    answer = [n, (i + 1) // n]
                    return answer
                else:
                    answer = [(i + 1) % n, ((i + 1) // n) + 1]
                    return answer
        for j in range(i):
            if words[i] == words[j]:
                if (i + 1) % n == 0:
                    answer = [n, (i + 1) // n]
                    return answer
                else:
                    answer = [(i + 1) % n, ((i + 1) // n) + 1]
                    return answer
    return [0, 0]
