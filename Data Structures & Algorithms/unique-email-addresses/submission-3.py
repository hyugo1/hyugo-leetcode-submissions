class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = 1
        new_locals = []
        seen = set()
        for e in emails:
            split_local_domain = e.split('@')
            local = split_local_domain[0]
            domain = split_local_domain[1]
            new_local = ""
            for i in range(len(local)):
                if local[i] == ".":
                    continue
                if local[i] == "+":
                    break
                new_local += local[i]
            # new_locals.append(new_local)
            seen.add((new_local, domain))
        return len(seen)