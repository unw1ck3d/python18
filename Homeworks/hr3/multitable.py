# С помощью циклов и генераторов выведите на экран полную таблицу умножения, вместе с числами, которые
# участвуют в операции, в таком виде:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3

for i in range(1,11):
     for j in range(1,11):
         print(i, '*', j , '=', i * j)