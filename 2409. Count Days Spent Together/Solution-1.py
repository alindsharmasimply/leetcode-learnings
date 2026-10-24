class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days_till_now(s: str):
            month = int(s[:2])
            day = int(s[3:])
            prev_days = 0
            for i in range(month):
                prev_days += month_days[i]
            return prev_days + day

        alice_arrival_days = days_till_now(arriveAlice)
        alice_leaving_days = days_till_now(leaveAlice)
        bob_arrival_days = days_till_now(arriveBob)
        bob_leaving_days = days_till_now(leaveBob)

        days_spent_together = 0
        for day in range(1, 366):
            if (
                alice_arrival_days <= day
                and alice_leaving_days >= day
                and bob_arrival_days <= day
                and bob_leaving_days >= day
            ):
                days_spent_together += 1

        return days_spent_together
