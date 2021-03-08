{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(people, limit): # list, int\n",
    "    people.sort()\n",
    "    answer = 0 \n",
    "    while len(people) >= 2:\n",
    "        if people[0]+people[-1] <= limit:\n",
    "            people.pop()\n",
    "            people.pop(0)\n",
    "        else:\n",
    "            people.pop()   \n",
    "        answer += 1\n",
    "    return answer+len(people)\n",
    "# 시간초과 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(people, limit): # list, int\n",
    "    people.sort()\n",
    "    answer = 0 \n",
    "    while len(people) >= 2:\n",
    "        \n",
    "        if people[0] + people[1] > limit:\n",
    "            return answer + len(people)\n",
    "        elif people[-1] + people[-2] <= limit:\n",
    "            if len(people) % 2 == 0:\n",
    "                return answer + len(people)\n",
    "            else:\n",
    "                return answer + len(people) + 1\n",
    "        else:\n",
    "            if people[0]+people[-1] <= limit:\n",
    "                people.pop()\n",
    "                people.pop(0)\n",
    "            else:\n",
    "                people.pop()   \n",
    "        answer += 1\n",
    "    return answer + len(people)\n",
    "# 정답 시간 초과."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(people, limit): # list, int\n",
    "    people.sort()\n",
    "    answer = 0 \n",
    "    while len(people) >= 2:\n",
    "        if people[0] + people[1] > limit:\n",
    "            return answer + len(people)\n",
    "        elif people[-1] + people[-2] <= limit:\n",
    "            if len(people) % 2 == 0:\n",
    "                return answer + len(people) // 2\n",
    "            else:\n",
    "                return answer + len(people) // 2 + 1\n",
    "        else:\n",
    "            if people[0]+people[-1] <= limit:\n",
    "                people.pop()\n",
    "                people.pop(0)\n",
    "            else:\n",
    "                people.pop()   \n",
    "        answer += 1\n",
    "    return answer + len(people)\n",
    "# 진짜 이것도??\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "그러면 미리 짤라볼까?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(people, limit): # list, int\n",
    "    people.sort(reverse = True)\n",
    "    answer = 0\n",
    "    index = 0\n",
    "    for i in range(len(people)):\n",
    "        if people[i] + people [-1] <=  limit :\n",
    "            index = i\n",
    "            people = people[0:index+1]\n",
    "            break\n",
    "    while len(people) >= 2:\n",
    "        if people[0]+people[-1] <= limit:\n",
    "            people.pop()\n",
    "            people.pop(0)\n",
    "        else:\n",
    "            people.pop(-1)   \n",
    "        answer += 1\n",
    "    return answer+len(people)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(people, limit): # list, int\n",
    "    people.sort()\n",
    "    for i in range(1,len(people)):\n",
    "        if people[0] + people[i] > limit:\n",
    "            lst = people[0:i]\n",
    "            break\n",
    "    answer = len(people) - len(lst)\n",
    "    while len(lst) >= 2:\n",
    "        if lst[0]+lst[-1] <= limit:\n",
    "            lst.pop()\n",
    "            lst.pop(0)\n",
    "        else:\n",
    "            lst.pop()   \n",
    "        answer += 1\n",
    "    return answer+len(lst)\n",
    "# 진짜 이것도?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(people, limit): # list, int\n",
    "    people.sort()\n",
    "    answer = 0 \n",
    "    while len(people) >= 2:\n",
    "        if people[0]+people[-1] <= limit:\n",
    "            people.pop()\n",
    "            people.pop(0)\n",
    "        else:\n",
    "            people.pop()   \n",
    "        answer += 1\n",
    "    return answer+len(people)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def solution(people, limit): # list, int\n",
    "    m = min(people)\n",
    "    num = len(people)\n",
    "    n = limit - min \n",
    "    people.append(n)\n",
    "    people.sort()\n",
    "    people = people[0:people.index(n)]\n",
    "    answer = num - len(people) \n",
    "    while len(lst) >= 2:\n",
    "        if lst[0]+lst[-1] <= limit:\n",
    "            lst.pop()\n",
    "            lst.pop(0)\n",
    "        else:\n",
    "            lst.pop()   \n",
    "        answer += 1\n",
    "    return answer+len(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
