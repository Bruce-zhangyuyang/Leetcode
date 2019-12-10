# 思路1：可以直接用IFNUll， 如果第一个能够取出第二高的工资，则返回null，否则就返回null

# select IFNUll(
#   select distinct salary from employee order by salary DESC limit 1,1 (limit 1 offset 1), null
# )as SecondHighestSalary