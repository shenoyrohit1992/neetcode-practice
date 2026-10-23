class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqMap = {i: [] for i in range(numCourses)}
        visiting, completed = set(), set()
        output = []

        # build preReqMap
        for course, preReq in prerequisites:
            preReqMap[course].append(preReq)

        def canComplete(course: int):
            # base cases
            if course in visiting:
                return False
            if course in completed:
                return True  # already added to output

            visiting.add(course)
            for preReq in preReqMap[course]:
                if not canComplete(preReq):
                    return False

            visiting.remove(course)
            completed.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not canComplete(course):
                return []
        return output
