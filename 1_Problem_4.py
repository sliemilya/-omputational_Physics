'''
В данной задаче найдем собственные значения по методу из линейной алгебры:
l - собственное значение
p - сигма
det(A) = (1-l)^2 - 10p = 0 , тогда собственное значение l = 1 +- (10p)**0.5
тогда наибольшее значение будет:
l = 1 + (10p)**0.5
тогда найдем число обусловленности значений: для этого возьмем производную l по p и получим:
dl/dp = 5/((10p)**0.5) тогда для  p = 10:  dl/dp = 0.5,
                             для  p = 0.1: dl/dp = 5
Ответ: p = 10:  dl/dp = 0.5
       p = 0.1: dl/dp = 5
'''
