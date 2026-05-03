class Solution:
    def subdomainVisits(self, cpdomains):
        counts = {}
        for entry in cpdomains:
            num, domain = entry.split()
            num = int(num)
            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counts[subdomain] = counts.get(subdomain, 0) + num
        return [f"{cnt} {dom}" for dom, cnt in counts.items()]
