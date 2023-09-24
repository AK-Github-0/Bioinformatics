from Bio import SeqIO
from Bio.SeqUtils import gc_fraction\
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Provide the correct path to your GenBank file
genbank_file = "gbinv1024.seq"

try:
    records = list(SeqIO.parse(genbank_file, "genbank"))

    # Iterate through each record and print them
    for record in records:
        print(record)
except FileNotFoundError:
    print(f"File '{genbank_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("*********************************")
for record in records:
    print(record.id)

for record in records:
    print(gc_fraction(record.seq))

# Define a function to compute the template strand
def compute_template_strand(coding_strand):
    return coding_strand.reverse_complement()

# Define a function to transcribe to mRNA
def transcribe_to_mrna(coding_strand):
    return coding_strand.transcribe()

# Define a function to translate mRNA to proteins
def translate_to_proteins(mrna):
    return mrna.translate()

# Function to pad the sequence with trailing Ns to make its length a multiple of three
def pad_sequence(seq):
    remainder = len(seq) % 3
    if remainder != 0:
        padding = "N" * (3 - remainder)
        return seq + padding
    return seq

# Provide the correct path to your GenBank file
genbank_file = "gbinv1024.seq"

try:
    records = list(SeqIO.parse(genbank_file, "genbank"))

    # Create a GenBank output file for proteins
    protein_output_file = "proteins_output.gb"

    with open(protein_output_file, "w") as protein_out:
        # Iterate through each record and process it
        for record in records:
            # Compute template strand
            template_strand = compute_template_strand(record.seq)

            # Transcribe to mRNA
            mrna = transcribe_to_mrna(record.seq)

            # Pad the sequence with trailing Ns if needed
            mrna = pad_sequence(mrna)

            # Translate mRNA to proteins
            proteins = translate_to_proteins(mrna)

            # Create a new SeqRecord for proteins
            protein_record = SeqRecord(
                seq=proteins,
                id=record.id,
                description="Proteins translated from mRNA",
            )

            # Add the molecule_type annotation
            protein_record.annotations["molecule_type"] = "protein"

            # Add features and annotations as needed for your specific use case

            # Write the protein record to the output file
            SeqIO.write(protein_record, protein_out, "genbank")

except FileNotFoundError:
    print(f"File '{genbank_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


