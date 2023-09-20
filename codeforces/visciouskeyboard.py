s = input()
print(s.count("VK")+int(s.count("KKK")>0 or (len(s) >= 2 and s[:2]=="KK") or s.count("VVV")>0 or (len(s) >= 2 and s[-2:]=="VV")))
