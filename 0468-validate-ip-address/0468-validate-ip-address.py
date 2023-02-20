class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def validateIpv4(ip):
            ips = ip.split(".")
            if len(ips) != 4:
                return "Neither"
            for ip in ips:
                if ip == "":
                    return "Neither"
                if ip[0] == "0" and len(ip) != 1:
                    return "Neither"
                if ip.isdigit():
                    if int(ip) < 0 or int(ip) > 255:
                        return "Neither"
                else:
                    return "Neither"
            return "IPv4"
        def validateIpv6(ip):
            ips = ip.split(":")
            print(ips)
            hexdigits = '0123456789abcdefABCDEF'
            
            if len(ips) != 8:
                print("here1")
                return "Neither"
            
            for ip in ips:
                if ip == "":
                    return "Neither"
                if len(ip) < 1 or len(ip) > 4:
                    return "Neither"
                
                for ch in ip:
                    if ch not in hexdigits:
                        return "Neither"

            return "IPv6"
        
        countDot = 0
        countColon = 0
        for i in queryIP:
            if i == ".":
                countDot += 1
            elif i == ":":
                countColon += 1
        if countDot == 3:
            ans = validateIpv4(queryIP)
        elif countColon == 7:
            ans = validateIpv6(queryIP)
        else:
            return "Neither"
        return ans
    