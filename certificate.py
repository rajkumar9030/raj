project_score=float(input("enter the project score :"))
internal_score=float(input("enter the internal score :"))
external_score=float(input("enter the external score :"))
if(project_score<50 ):
    print("invalid project score :"+str(project_score))
elif(internal_score<50):
    print("invalid internal score :"+str(internal_score))
elif(external_score<50):
    print("invalid external score :"+str(external_score))
else:
    total_score=0.7*project_score+0.1*internal_score+0.2*external_score
    if(total_score>90):
        print(" A grade")
    elif(total_score>80):
        print("B grade")
    else:
        print("c grade")




