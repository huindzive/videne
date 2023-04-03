zime=(input('ievadi zīmi (+,-,*,/)'))
sk1=float(input('ievadi 1. ciparu'))
sk2=float(input('ievadi 2. ciparu'))
if zime=='/' and sk2==0:
    print('darbība nav iespējama')
elif zime!= '/' and zime!='*' and zime!='-' and zime!='+':
    print('zīme netika saprasta')
elif zime== '/':
    print((sk1),(zime),(sk2),('='),(sk1/sk2))
elif zime== '*':
    print((sk1),(zime),(sk2),('='),(sk1*sk2))
elif zime== '-':
    print((sk1),(zime),(sk2),('='),(sk1-sk2))
elif zime== '+':
    print((sk1),(zime),(sk2),('='),(sk1+sk2))