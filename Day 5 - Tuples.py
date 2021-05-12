#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

d = dict()
lst = list()

fname = input('enter the file name : ')
try:
    fopen = open(fname, 'r')
except:
    print('wrong file name !!!')

for line in fopen:

    stline = line.strip()

    if stline.startswith('From:'):
        continue
    elif stline.startswith('From'):
        spline = stline.split()

        time = spline[5]
        tsplit = time.split(':')

        t1 = tsplit[0].split()

        for t in t1:
            if t not in d:
                d[t] = 1
            else:
                d[t] = d[t] + 1

for k, v in d.items():
    lst.append((k, v))
lst = sorted(lst)

for k, v in lst:
    print(k, v)
