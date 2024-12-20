def add_score(subject_score, subject, score):
       
    average = 0
    score_dict = subject_score

    add_subject = subject.replace("'", "")
    add_subject = add_subject.replace(" ", "")

    score = score.replace("'","")
    score = score.replace(" ","")
    score = int(score)
    score_dict[add_subject]= score

    score_dict = {k:v for (k,v) in score_dict.items() if v>=0 and k !=''}

    count = 0
    for x in list(score_dict.values()):
      average += x
      count += 1

    try:
        1/count
    except:
        average=0
    else :
        average = average/count

    print(f"{score_dict}, Average score: {average:.2f}")


    return 0


value = input()


value =[str(e) for e in value.split("|")]
res = eval(value[0].replace("'", "\""))


output = add_score(subject_score=res , subject=value[1], score=value[2])
