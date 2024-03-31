from kanren import *
from kanren.core import lall
import time

"""
[Unguided 2 Sistem Pakar - PKB]
Nama	: Kevin Philips Tanamas
NPM		: 220711789
Kelas	: A
"""

def lefto(q, p, list):
	return membero((q,p), zip(list, list[1:]))
	
def nexto(q, p, list):
	return conde([lefto(q, p, list)], [lefto(p, q, list)])

houses = var()
# Urutan Ruangan, Sesi, Pemilik, Matkul, Kelas
rules = lall(
	# eq adalah menjelaskan jika mereka adalah setara, mereka yang dimaksud adalah var (hause).
	(eq, (var(), var(), var(), var(), var()), houses),
	
	# Ruangan 317 dosennya Intan
	(membero, ('317', var(), 'Intan', var(), var()), houses),
	
	# Mata Kuliah Olahraga memiliki kelas D
	(membero, (var() , var(), var(), 'Olahraga', 'D'), houses),
	
	# Sesi 2 Memiliki matkul PPKN
	(membero, (var() , '2', var(), 'PPKN', var()), houses),
	
	# Ruangan Klasik sebelah kanan ruangan yang ber kelas A
	(lefto, (var(), var(), var(), var(), 'A'), (var(), var(), 'Klasik', var(), var()), houses),
	
	# Natasya adalah dosen Mata Kuliah Biologi
	(membero, (var() , var() , 'Natasya', 'Biologi', var()), houses),
	
	# Ruangan 319 memiliki kelas E
	(membero, ('319', var(), var(), var(), 'E'), houses),
	
	# Biologi merupakan Kelas yang letaknya pertama (paling pojok kiri).
	(eq, ((var(), var(), var(), 'Biologi', var()), var(), var(), var(), var()), houses),
	
	# Ruang 315 memiliki Sesi 3
	(membero, ('315', '3', var(), var(), var()), houses),
	
	# Ruang 316 ditempati dosen riko
	(membero, ('316', var(), 'Riko', var(), var()), houses),
	
	# Sesi 1 adalah mata kuliah sejarah
	(membero, (var(), '1', var(), 'Sejarah', var()), houses),
	
	# Riko merupakan dosen yang ruangannya berada di kanan dosen Natasya
	(lefto, (var(), var(), 'Natasya', var(), var()), (var(), var(), 'Riko', var(), var()), houses),
	
	# Dosen Ven memiliki kelas A
	(membero, (var(), var(), 'Ven', var(), 'A'), houses),
	
	# Sesi 4 Mata Kuliah B indo
	(membero, (var(), '4', var(), 'Indo', var()), houses),
	
	# Kelas B berada di Sesi 3
	(membero, (var(), '3', var(), var(), 'B'), houses),
	
	# sesi 5 digunakan untuk olahraga
	(membero, (var(), '5', var(), 'Olahraga', var()), houses),
	
	# kelas C memiliki dosen Intan
	(membero, (var(), var(), 'Intan', var(), 'C'), houses),
	
	# Kelas A bertempat di ruangan 318
	(membero, ('318', var(), var(), var(), 'A'), houses),
	
	# Ruangan PPkn berada di kanan ruangan yang sesi 1
	(lefto, (var(), '1', var(), var(), var()), (var(), var(), var(), 'PPKN', var()), houses),
)

t0 = time.time()
solutions = run(0, houses, rules)
t1 = time.time()
dur = t1 - t0

count = len(solutions)
dosen = [house for house in solutions[0] if 'Riko' in house][0][0]

print("%i solutions in %.2f seconds" % (count, dur))
print("Dosen Riko mengajar di no ruangan berapa?")
print("Dosen Riko mengajar diruangan %s" % dosen)
print("Here are all the houses : ")
for line in solutions[0]:
	print(str(line))
	



