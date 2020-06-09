def display_kontak(daftar_kontak):    
    for kontak in daftar_kontak:
        print("==================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Tlp : {kontak['tlp']}")


def new_kontak():
    nama = input("nama :")
    email = input("email :")
    tlp = input("tlp :")
    kontak ={
    "nama": nama,
    "email": email,
    "tlp": tlp
    }
    return kontak

def hapus_kontak(daftar_kontak):
 telepon = input("no tlpn yg akan dihapus :")

 index= -1
 for i in range(0, len(daftar_kontak)):
      kontak =daftar_kontak[i]
      if telepon == kontak["tlp"]:
         index = i
      break

 if index == -1:
   print("data kontak tidak ditemukan")
 else:      
   del daftar_kontak[index]
   print("berhasil menghapus data kontak")

def cari_kontak(daftar_kontak):
cari = input("nama yg dicari :")

for kontak in daftar_kontak:
    nama = kontak["nama"]
    if nama.lower().find(cari.lower()) != -1:        
     print("==================")
     print(f"Nama : {kontak['nama']}")
     print(f"Email : {kontak['email']}")
     print(f"Tlp : {kontak['tlp']}")






