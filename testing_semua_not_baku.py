
from cfg import *
from cnf import *
from cyk import *

rules = open('rules.txt', 'r').read().splitlines()
start_symbol = "K"
dictionary_cfg = {}
dictionary_cnf = {}
if __name__ == '__main__':
    with open('not_baku.txt', 'r') as file:
        list_sentences = file.read().splitlines()
for sentence in list_sentences:
    # print(sentence)
    string_input = sentence
    cfg(dictionary_cfg, rules)
    cnf(dictionary_cfg, dictionary_cnf, start_symbol)
    if cyk(dictionary_cnf, string_input)[0] == 'valid':
        print("The sentence is Valid")
    else: 
        if cyk(dictionary_cnf, string_input)[0] == 'invalid':
            print("The sentence is Invalid")
        else:
            print("The sentence is not Registered")
    print(string_input)

# Kalimat baku: SCORE ==> 
# 1) Nenek mengambil sedikit daun ubi di kebun. (S P O Ket) PASS
# 2) Banyak orang menghadiri acara itu. (S P O) PASS
# 3) Sekitar lima mahasiswa mengikuti kegiatan pengabdian tersebut. (S P O) FAIL
# 4) Orang dewasa saja diperbolehkan menaiki wahana itu. (S P Pel) FAIL
# 5) Pemadam kebakaran itu hanya mempunyai sedikit waktu untuk menyelamatkan penduduk desa tersebut. (S P O Pel) FAIL
# 6) Anak laki-laki itu jarang bermain di taman kota. (S P Ket) FAIL losing hope
# 7) Ibu memasak banyak makanan lezat. (S P O) PASS yum
# 8) Para siswa sering belajar di perpustakaan kampus. (S P Ket) PASS
# 9) Polisi selalu menjaga ketertiban di jalan. (S P O Ket) PASS
# 10) Burung merpati itu hanya terbang di siang hari. (S P Ket) FAIL
# 11) Ikan koi banyak berenang di kolam taman. (S P Ket) PASS
# 12) Kuda pacuan itu selalu berlari dengan cepat di lintasan pacu. (S P Pel Ket) FAIL
# 13) Monyet kecil itu sering bergelantungan di ranting pohon. (S P Ket) FAIL
# 14) Kelinci putih itu melompat-lompat di kebun. (S P Ket) 
# 15) Lumba-lumba itu bermain di laut lepas. (S P Ket)
# 16) Kupu-kupu sering hinggap di bunga (S P Ket).
# 17) Sapi selalu mengunyah rumput di padang rumput. (S P O Ket)
# 18) Lebah itu mengumpulkan banyak nektar dari bunga. (S P O Pel)
# 19) Seekor buaya sedang berjemur di tepi danau (S P Ket)
# 20) Banyak mahasiswa hadir pada acara seminar itu. (S P Pel)
# 21) Dr. Siti Rahayu memberikan kuliah di universitas. (S P O Ket)
# 22) Ani sedang berlibur di pantai. (S P Pel)
# 23) Adi Santoso merupakan pemimpin proyek tersebut. (S P Pel)
# 24) Bu Ratna adalah pemilik warung kopi itu.(S P Pel)
# 25) Prof. Dr. Hadi Prayitno adalah pakar bidang ekologi. (S P Pel)
# 26) Kiki menjadi juara pada lomba menyanyi.
# 27) Ibu Sinta akan menjadi pembicara dalam seminar itu. (S P Pel Ket)
# 28) Bapak Haryono selalu membantu tetangga. (S P O)
# 29) Laut Mediterania sangat terkenal dengan keindahan pantainya (S P Pel).
# 30) Bukit Tinggi memiliki pemandangan alam indah (S P O).
# 31) Danau Baikal adalah danau terdalam di dunia. (S P Pel Ket)
# 32) Pantai Copacabana menjadi ikon kota Rio de Janeiro (S P Pel).
# 33) Bali selalu terkenal dengan keindahan pantainya. (S P Pel)
# 34) Kota Bandung itu terkenal dengan kulinernya. (S P Pel)
# 35) Bogor dikenal dengan kota hujan. (S P Pel)
# 36) Monas terletak di tengah Jakarta. (S P Ket)
# 37) Bali memiliki banyak budaya indah. (S P Pel)
# 38) Denpasar sangat ramai pada malam hari. (S P Ket)
# 39) Surabaya merupakan kota terbesar di Jawa Timur. (S P Pel Ket)
# 40) Pentas ogoh-ogoh dilakukan menyambut Tahun Baru Saka. (S P Pel)
# 41) Arab Saudi merupakan negara penghasil minyak terbesar di dunia. (S P Pel Ket)
# 42) Indonesia adalah negara kepulauan terbesar di dunia. (S P Pel Ket)
# 43) Lima belas pasang sepatu terpajang di rak sepatu (S P Ket)
# 44) Delapan buah rumah sedang dalam tahap konstruksi. (S P)
# 45) Dua ekor kucing selalu bermain di taman belakang rumah. (S P Ket)
# 46) Sepuluh orang siswa sedang belajar di perpustakaan. (S P Ket)
# 47) Tujuh puluh lima orang pengunjung hadir dalam acara tersebut. (S P Pel)
# 48) Kamar tidur ini sangat nyaman. (S P)
# 49) Pertunjukan teater ini sangat indah. (S P)
# 50) Mobil tersebut sudah lama digunakan. (S P Pel)
# 51) Bunya itu harus disiram setia pagi. (S pel Ket)
# 52) Kotak besar itu berisi banyak mainan anak-anak. (S P Pel)
# 53) Kuda hitam itu sedang berlari. (S P)
# 54) Dia membeli tiga buah buku. (S P O)
# 55) Bapak selalu membeli tiga bungkus rokok. (S P O)
# 56) Saya sedang meneliti sejarah kebudayaan Bali. (S P O)
# 57) Teman saya sedang kursus bahasa Jepang. (S P Pel)
# 58) Asrama putri itu sangat luas. (S P)
# 59) Laki-laki itu adalah pemain sepak bola. (S P Pel)
# 60) Bapak guru saya itu orang Medan. (S P)
# 61) Kakek saya sangat menyukai kursi rotan. (S P O)
# 62) Pelatih tari itu dua orang. (S P)
# 63) Rencana perjalanan kita selalu disusun dengan sangat baik (S P Pel)).
# 64) Pengembangan teknologi berlangsung dengan pesat (S P Pel).
# 65) Gadis kecil itu sangat senang dengan boneka barunya (S P Pel).
# 66) Air terjun pegunungan itu sangat indah. (S P)
# 67) Pertunjukan seni malam ini sangat menghibur (S P).
# 68) Rumah tua itu memiliki sejarah panjang. (S P O)
# 69) Bunga yang mekar itu adalah kebanggaan taman kita (S P Pel).
# 70) Kucing hitam itu menjadi teman setia anak-anak (S P Pel).
# 71) Udara sejuk memberikan kesegaran pikiran (S P O)
# 72) Prestasi anak-anak itu adalah kebanggaan orang tua (S P Pel).
# 73) Rasa cokelat menjadi kelemahannya. (S P Pel)
# 74) Pohon rindang itu memberikan kesejukan. (S P O)
# 75) Air hujan membuat suasana romantis. (S P O)
# 76) Cita-cita tinggi adalah pendorong kesuksesan. (S P Pel)
# 77) Kucing itu hewan peliharaan manis. (S P) PASS
# 78) Pameran itu menampilkan karya seni kontemporer. (S P O)
# 79) Budaya lokal menjadi daya tarik wisata daerah itu. (S P Pel)
# 80) Hewan peliharaan ini adalah teman setia keluarga kami. (S P Pel)
    
#     Kalimat tidak baku: SCORE ==> 12/20 = 60% 
# 1) Sangat menyukai kursi rotan. PASS
# 2) Pelatih tari itu. PASS
# 3) Rencana perjalanan kita selalu. FAIL maybe because of L3
# 4) Pengembangan teknologi. PASS
# 5) Gadis kecil itu. PASS
# 6) Air terjun pegunungan itu. FAIL because terjun counted as Verb
# 7) Sangat menghibur. PASS
# 8) Memiliki sejarah panjang. PASS
# 9) Kebanggaan taman kita. PASS
# 10) Menjadi teman setia anak-anak. PASS
# 11) Memberikan kesegaran pikiran. PASS
# 12) Kebanggaan orang tua. FAIL maybe because of L3
# 13) Rasa cokelat menjadi. FAIL maybe because rasa count as S and menjadi is P
# 14) Pohon rindang itu memberikan. PASS unexpectedly
# 15) Air hujan membuat. FAIL as long as we dont seperate verb that start with me(m)-
# 16) Cita-cita tinggi adalah pendorong kesuksesan. FAIL, sounds like a legit sentence too
# 17) Hewan peliharaan manis. FAIL peliharaan manis counted as P
# 18) Karya seni kontemporer. FAIL seni kontemporer as P
# 19) Menjadi daya tarik wisata daerah itu. PASS
# 20) Teman setia keluarga kami. PASS