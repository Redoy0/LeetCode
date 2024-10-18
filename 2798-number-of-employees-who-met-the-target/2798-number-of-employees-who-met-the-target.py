class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        meet = 0
        for hour in range(0,len(hours)):
            if hours[hour]>=target:
                meet+=1
        return meet

        