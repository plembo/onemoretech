#!/usr/bin/python
# Calculate bandwidth consumed from monthly average
# incoming and outgoing

print("Calculate monthly bandwidth consumed")

inb = int(input("Monthly average incoming kb/s: "))
outb = int(input("Monthly average outgoing kb/s: "))

tmb = (inb+outb)/8*60*60*24*30.5
tmb = tmb/1000000
print("Total bandwidth consumed: %s GB" % tmb)

