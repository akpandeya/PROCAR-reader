import sys
if ((len(sys.argv) != 2)):
	print "Usage: python parse_procar.py ion_number \n Example: python parse_procar.py 3 \nIt will print the lm decomposed DOS for ion number 3 in POSCAR. \nRequires PROCAR file to be present"
	exit(1)
try:
	int(sys.argv[1])
except:
	print "The second argument should be integer. If you are writing element name, it won't work. Check POSCAR to find put the ion number."
	print "Usage: python lmdos.py ion_number \n Example: python lmdos.py 3 \nIt will print the lm decomposed DOS for ion number 3 in POSCAR. \nRequires PROCAR file to be present"
	exit(2)
readion = int(sys.argv[1])
try:
	f = open("PROCAR", 'r')
except IOError: 
	print "The file PROCAR could not be read. There could be many reasons for this. \n1)You did not run vasp with correct LORBIT option. \n2)Reading or writing files is not permmitted. You can try sudo in this case."
	print "Exiting program"
	exit(3)
line1 = f.readline()
line2 = f.readline()
number_list = line2.split()
nkpoint = int(number_list[3])
nbands = int(number_list[7])
nions = int(number_list[11])
blankline = f.readline()
line4 = f.readline().split()
kpoint = [float(line4[3]), float(line4[4]), float(line4[5])]
try:
	f1 = open(str(readion)+"lm.dat", "w")
except IOError:
	print "Could not open file in write mode. Perhaps writing file to your hard disk is not permitted. Try sudo"
	print "Exiting program"
	exit(4)
for i in range(0, nbands):
	blankline = f.readline()
	energy_line = f.readline().split()
	energy = energy_line[4]
	f.readline()
	if (i == 0):
		f1.write("Energy")
		f1.write("             ")
		head = f.readline().split()
		for item in head[1:]:
			f1.write(item)
			f1.write("       ")
		f1.write('\n')
	else:
		f.readline()
	f1.write(energy)
	f1.write("       ")
	for j in range(0, nions+1):
		if(j == readion-1):
			prodos = f.readline().split()
			for item in prodos[1:]:
				f1.write(item)
				f1.write("    ")
			f1.write('\n')
		else:
			f.readline()
f.close()
f1.close()
