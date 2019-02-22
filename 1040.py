
numbers = input().split()  
n1 = float(numbers[0]) * 2
n2 = float(numbers[1]) * 3
n3 = float(numbers[2]) * 4
n4 = float(numbers[3])
media = (n1 + n2 + n3 + n4) / 10
print("Media:", format(media, ".1f"))
if media >= 7:
    print("Aluno aprovado.")
elif 5 <= media < 7:
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame:", format(ne, ".1f"))
    if (ne + media) / 2 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:", format((ne + media) / 2, ".1f"))
else:
  print("Aluno reprovado.")
