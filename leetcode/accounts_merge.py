from typing import Dict
from collections import defaultdict


class DSU:
    def __init__(self, n_elements):
        self.parent = list(range(n_elements))

    def find(self, x):  # find set(group) of x, i.e. find leader of x
        leader = self.parent[x]

        if leader == x:
            return x

        while leader != self.parent[leader]:
            leader = self.parent[leader]

        # we have found the leader of x
        # compress the path
        while self.parent[x] != x:
            self.parent[x], x = leader, self.parent[x]

        return leader

    def union(self, x, y):  # assign x (and implicitly its group/set) to group/set of y
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n_emails = sum(map(lambda acc: len(acc) - 1, accounts))
        dsu = DSU(n_emails)
        id_counter = 0
        email_to_id: Dict[str, int] = {}
        email_to_name: Dict[str, str] = {}

        for name, *emails in accounts:
            fst_email = emails[0]
            for email in emails:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    id_counter += 1
                # put curr email in the same group as first email in curr account
                dsu.union(email_to_id[email], email_to_id[fst_email])

        # acc_id will be the "group/leader" of some email in DSU
        emails_by_acc_id = defaultdict(list)
        for email in email_to_id:
            emails_by_acc_id[dsu.find(email_to_id[email])].append(email)

        return [[email_to_name[emails[0]], *sorted(emails)] for emails in emails_by_acc_id.values()]