i=int(input())
if i>=3600:
    result1=i//3600
    result2=i%3600
    result3=result2//60
    result4=result2%60
    result5=result4
    print(str(result1)+":"+str(result3)+":"+str(result5))
if i<3600 and i>=60:
    result1=0
    result3=i//60
    result4=i%60
    result5=result4
    print(str(result1)+":"+str(result3)+":"+str(result5))
if i<60:
    result1=0
    result3=0
    result5=i
    print(str(result1)+":"+str(result3)+":"+str(result5))
