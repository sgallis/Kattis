#https://open.kattis.com/problems/teque

from collections import deque
import sys
class teque:
    def __init__(self) -> None:
        self.deque1 = deque()
        self.deque2 = deque()
        self.output = ""
    
    def push_back(self, x):
        self.deque2.append(x)
        if len(self.deque2) > len(self.deque1):
            self.deque1.append(self.deque2.popleft())

    def push_front(self, x):
        self.deque1.appendleft(x)
        if len(self.deque1) - len(self.deque2) > 1:
            self.deque2.appendleft(self.deque1.pop())

    def push_middle(self, x):
        if len(self.deque1) == len(self.deque2):
            self.deque1.append(x)
        elif len(self.deque1) == len(self.deque2) + 1:
            self.deque2.appendleft(x)

    def get(self, i):
        if i < len(self.deque1):
            output = f"{self.deque1[i]}\n"
        else:
            output = f"{self.deque2[i-len(self.deque1)]}\n"
        sys.stdout.write(output)

if __name__ == "__main__":
    tequee = teque()
    n = int(input())
    for _ in range(n):
        instruction, number = sys.stdin.readline().rstrip().split()
        if instruction == "push_back":
            tequee.push_back(int(number))
        elif instruction == "push_front":
            tequee.push_front(int(number))
        elif instruction == "push_middle":
            tequee.push_middle(int(number))
        else:
            tequee.get(int(number))

