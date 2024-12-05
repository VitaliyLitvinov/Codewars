#
# In a small town the population is p0 = 1000
# at the beginning of a year. The population regularly
# increases by 2 percent per year and moreover 50 new
# inhabitants per year come to live in the town.
# How many years does the town need to see its
# population greater than or equal to p = 1200 inhabitants?

def nb_year(p0, percent, aug, p):
    year = 0
    while p0 <= p:
        p0 += p0 * (percent * 0.01) + aug
        year += 1
    print(year)
nb_year(1500, 5, 100, 5000)
nb_year(1500000, 2.5, 10000, 2000000)
nb_year(1500000, 0.25, 1000, 2000000)