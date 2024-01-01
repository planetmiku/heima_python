my_str = "万过月薪，员序程马黑来，nohtyP学"

new_my_str = my_str[::-1][9:14]
print(new_my_str)

new_my_str1 = my_str.split("，")[1].replace("来","")[::-1]

print(new_my_str1)