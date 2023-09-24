from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction

def compute_template_strand(coding_strand):
    return coding_strand.reverse_complement()

def function(filename, format, output, output_format):
    sec = list(SeqIO.parse(filename, format))

    # printing the ID's of each and every record in file
    for i in sec:
        print("Seq ID: ", i.id)

    # printing total number of records in file
    print("Total record are: ", len(sec))

    # printing GC-Fraction of the DNA Samples
    for i in sec:
        print(f"GC fraction of {i.id} is: ", gc_fraction(i.seq))

    #Computing template strand
    for i in sec:
        template_strand = compute_template_strand(i.seq)
        
    # printing Transcribed sequence of the DNA Samples
    for i in sec:
        print(f"Transcribed result of {i.id} is :", i.seq.transcribe())

    
    with open(output, 'w') as protein_output:
        for i in sec:
            mRNA = i.seq.transcribe()

            Temp = len(mRNA)%3
            if Temp!=0:
                mRNA += "N" * (3-Temp)

            protein = mRNA.translate()

            Temp = SeqRecord(
                seq=protein,
                id=i.id,
                description="protein formation from mRNA."
            )
            Temp.annotations["molecule_type"] = "protein"
            SeqIO.write(Temp, protein_output, output_format)

function("./gbinv1024.seq", "genbank", "Proteins.gb", "genbank")

