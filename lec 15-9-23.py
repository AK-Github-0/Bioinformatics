from Bio.Seq import Seq

simple_seq = Seq("GATC")

from Bio.SeqRecord import SeqRecord

#simple_seq_r = SeqRec

from Bio import SeqIO
record = SeqIO.read("NC_005816.fna","fasta")

print(record)

print(record.seq)

print(record.id)

print(record.name)

print(record.description)

print(len(record.seq))


print("**********************************")
record2 = SeqIO.read("NC_005816.gb","genbank")
print(record2)
my_snp = 4350

for feature in record.features:
    if my_snp in feature:
        print("%s%s"%(feature.type,feature.qualifiers.get("db_xref")))
#.strand 1, coding strand -1, template strand 0, you dont care none, only one strand like rna
print("*************************")
from Bio.SeqFeature import SeqFeature, SimpleLocation
seq = Seq("ACCGTACACCGATCGTACATCCGACTTGGC")

feature = SeqFeature(SimpleLocation(5,18,strand=-1),type="gene")

feature_seq = feature.extract(seq)

print(feature_seq)

Temp = seq[5:18]

print(Temp.reverse_complement())
