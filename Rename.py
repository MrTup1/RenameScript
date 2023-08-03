import os
file = int(input("Starting File:"))
id = input("Starting ID:") #"NVINV2021002027"
company = input("Company Name:")
deposit_num = 0
deposit = "Deposit" + " " + str(deposit_num)
def rename(file):
    src_path = "/Users/mrtup/Documents/Novelte/" + str(file)
    des = id + "_" + company + "_" + deposit + ".pdf"
    des_path = "/Users/mrtup/Documents/Novelte/" + str(des)
    os.rename(src_path, des_path)

for i in range(100):
    str_file = str(file) + ".pdf"
    rename(str_file)
    file += 1
    deposit_num += 1
    deposit = "Deposit" + " " + str(deposit_num)
    id = "NVINV202100" + str(int(id[-4:]) + 1)
    des = id + "_" + company + "_" + deposit + ".pdf"


   