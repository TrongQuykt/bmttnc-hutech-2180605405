def dao_nguoc_chuoi(chuoi):
  return chuoi[::-1]

input_string = input("Mời nhập chuỗi cần đảo ngược: ")

result = dao_nguoc_chuoi(input_string)

print("Chuỗi đảo ngược là:", result)