import math
def add_score(subject_score, student, subject, score):
    subject_score = eval(subject_score.replace("'", "\""))
    student = student.replace("'", "")
    student = student.replace(" ", "")
    subject = subject.replace("'", "")
    subject = subject.replace(" ", "")
    score = score.replace("'", "")
    score = score.replace(" ", "")

    score = int(score)
    subject_score[student][subject]=score

    avg = calc_average_score(subject_score, student)

    # print(f"{subject_score}, Average score: {avg:.2f}")
    # return subject_score, avg
    print(f"{subject_score}, Average score: {avg}")

def calc_average_score(subject_score, student):
    avg = {}
    sum =0
    count =0


    for x in subject_score:
        for y in subject_score[x]:
            sum+=subject_score[x][y]
            count +=1
    
    num = sum/count
    avg[student] = '%.2f' % num
    
    return avg


value = "{'65010001': {'python': 50}} | '65010001' | 'calculus' | 60"
# value = input()

value =[str(e) for e in value.split("|")]
output = add_score(value[0],value[1],value[2],value[3])

# print(output)