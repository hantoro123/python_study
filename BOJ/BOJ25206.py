import sys

majorScore = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0, 'P' : -1}

grades = []
scores = []

for _ in range(20):
    major, grade, score = sys.stdin.readline().split()
    if majorScore[score] != -1:
        scores.append(majorScore[score]*(float(grade)))
        grades.append(float(grade))

if sum(grades) != 0:    
    print(sum(scores)/sum(grades))
else:
    print(0.00000)

# totalscore = 3*4.5+3*4.5+3*4.0+3*4.5+3*4.5+3*3.0+3*4.0+3*3.0+3*3.0+3*2.5+3*3.0+4*4.5+3*3.5+3*2.0+3*1.5+3*2.5+3*3.0+3*3.5+3*1.0
# print(totalscore)
# print(totalscore/58)