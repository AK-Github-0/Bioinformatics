from Bio import SeqIO 
record_iter = SeqIO.parse("gbbct1.seq","genbank")
first_record = next(record_iter)
print(first_record.id)


#first record only
first_record2 = next(SeqIO.parse("ls_orchid.fasta","fasta"))
# for reading one record you can better use this one
# SeqIO.read()

records = list(SeqIO.parse("ls_orchid.fasta","fasta"))
print("Found %i records"%len(records))

print("the last record")

last_record =records[-1]

print(last_record.id)


#extracting data
all_Species=[]
for seq_record in SeqIO.parse("NC_005816.gb","genbank"):
    all_Species.append(seq_record.annotations["organism"])
print(all_Species)

#list comprehension
all_Species = [seq_record.annotations["organism"] for seq_record in SeqIO.parse("NC_005816.gb","genbank")]


print("****************")
from Bio import SeqIO 
record_iter = SeqIO.parse("gbbct1.seq","genbank")
first_record = next(record_iter)
print(first_record.id)
print(first_record.annotations.keys())
records = list(SeqIO.parse("gbbct1.seq","genbank"))
print("Found %i records"%len(records))
#for record in records:
#    print(record.annotations["source"])

all_Species2 = []
for seq_record in SeqIO.parse("ls_orchid.fasta","fasta"):
    all_Species2.append(seq_record.description.split()[1])

print(all_Species2)
print(len(all_Species2))

print("************Modifying data**************")
record_iter2 = SeqIO.parse("ls_orchid.fasta","fasta")
first_record3 = next(record_iter2)
first_record3.id
first_record3.id = "new id"

first_record3.description = first_record3.id + "" + "desired new description"

print(first_record3.format("fasta"))

