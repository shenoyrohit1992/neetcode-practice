class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i: [] for i in range(numCourses)}
        visiting = set()

        # build preReqMap
        for course, preReq in prerequisites:
            preReqMap[course].append(preReq)

        def canComplete(course: int):
            # base cases
            if course in visiting:
                return False
            if preReqMap[course] == []:
                return True

            visiting.add(course)
            for preReq in preReqMap[course]:
                if not canComplete(preReq):
                    return False

            visiting.remove(course)
            preReqMap[course] = []
            return True

        for course in range(numCourses):
            if not canComplete(course):
                return False
        return True
