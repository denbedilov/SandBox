s = 'aekjhfgbskhjdb@adsfsdfsd'

if '@' in s:
    s = s[0:s.find('@')]

print(s)
