from libraries import files
s = ''
for i in range(550, 601):
    s += '"http://www.gsmarena.com/apple_iphone_5-reviews-4910p' + str(i) + '.php",\n'

files.general_export(s, 'text.txt')