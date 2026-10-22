class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        answer=[]

        for i in range (len(boxes)):
            count=0
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    count+=abs(i-j)
            answer.append(count)
        return answer        