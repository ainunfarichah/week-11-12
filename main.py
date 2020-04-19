import os

A = []
B = []
At=[]
J = []
K = []


menu = ['1.Penjumlahan dan Pengurangan', '2. Determinan','3. Transpose','4. Exit']


print ("=======Selamat Datang di Operasi Matriks 2x2====")
print ("MASUKKAN MATRIKS A")
print(" ")

for baris in range (0,2,1) :
  for kolom in range (0,1,1) :
    
    print ("Baris ke-" , baris+1 ," Kolom ke-",kolom+1)
    test = int (input("Masukkan :"))

    print ("Baris ke-" , baris+1 ," Kolom ke-",kolom+2)
    test1 = int (input("Masukkan :"))

    A.append([test,test1])


os.system("clear")

#printmatriks#
for baris in range (0,2,1) :
  print (A[baris][0], '\t', A[baris][1])


while True :
  print ("")
  print ('=======MENU=======')
  print ('\t'.join(menu))

  pilihmenu = int (input("pilih :"))
  os.system("clear")


  if pilihmenu == 1 :
    print ('====Penjumlahan dan Pengurangan====')
    print("")

    print ("Masukkan matriks B terlebih dahulu :")

    for baris in range (0,2,1) :
      for kolom in range (0,1,1) :
        print ("Baris ke-" , baris+1 ," Kolom ke-",kolom+1)
        test = int (input("Masukkan :"))

        print ("Baris ke-" , baris+1 ," Kolom ke-",kolom+2)
        test1 = int (input("Masukkan :"))
        B.append([test,test1])

#jumlah
    for x in range (0,2,1):
     for y in range (0,1,1) :
      for z in range (1,0,-1) :
        #print (x,y,x,z)
        hasil1 = A[x][y] + B[x][y]
        hasil2= A[x][z] + B[x][z]
        J.append([hasil1,hasil2])

#kurang
    for x in range (0,2,1):
     for y in range (0,1,1) :
      for z in range (1,0,-1) :
        #print (x,y,x,z)
        hasil1 = A[x][y] - B[x][y]
        hasil2= A[x][z] - B[x][z]
        K.append([hasil1,hasil2])

    print ("Matriks A :")
    for baris in range (0,2,1) :
      print (A[baris][0], '\t', A[baris][1])
      
    print ("Matriks B :")
    for baris in range (0,2,1) :
      print (B[baris][0], '\t', B[baris][1])

    print("")
    print("Hasil Penjumlahan :")
    for baris in range (0,2,1) :
      print (J[baris][0], '\t', J[baris][1])

    print("")
    print("Hasil Pengurangan")
    for baris in range (0,2,1) :
      print (K[baris][0], '\t', K[baris][1])
    
  elif pilihmenu == 2 :
    print ('====Determinan====')
    det = (A[0][0]*A[1][1] - A[0][1]*A[1][0])
    print (abs(det))


  elif pilihmenu == 3 :
    print('====Transpose====')
    for x in range (0,2,1):
       for y in range (0,1,1) :
         for z in range (1,0,-1) :
          # print (x,y,x,z)
           At.append([A[y][x],A[z][x]])

    for baris in range (0,2,1) :
      print (At[baris][0], '\t', At[baris][1])
  

  elif pilihmenu==4 :
    break

