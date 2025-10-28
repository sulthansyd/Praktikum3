jumlah_data = int(input("masukkan jumlah data (minimal 3): "))
if jumlah_data < 3:
  print("jumlah data minimal 3! ")
else:
  data =[]
  for i in range(jumlah_data):
    nilai=int(input(f"masukkan data ke-{i+1}: "))
    data.append(nilai)
  data.sort()
  print("\nurutan bilangan:")
  for d in data:
    print(d)
