from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counter = Counter()
        for cpdomain in cpdomains:
            num_visits, address = cpdomain.split(' ')
            subdomains = [address]
            for i, c in enumerate(list(address)):
                if c == '.':
                    subdomains.append(address[i + 1:])
                    
            for subdomain in subdomains:
                domain_counter[subdomain] += int(num_visits)
        
        res = []
        for subdomain, num_visits in domain_counter.items():
            res.append(str(num_visits) + ' ' + subdomain)
        
        return res
                
