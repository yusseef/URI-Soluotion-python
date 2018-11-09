def parrot_trouble(talking, hour):
   if not talking and hour ==21 or hour ==23:
       return False
   if talking and hour < 7 or hour > 20:
     return True
   elif talking and hour==7 or hour==20:
       return False
   elif not talking and hour < 7 or hour > 20:
       return False

   else:
    return False
