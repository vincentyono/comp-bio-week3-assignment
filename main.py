from random import choice


def validate_dna(dna_seq: str) -> bool:
    seq = dna_seq.upper()
    return len(dna_seq) == (
        seq.count("A") + seq.count("C") + seq.count("G") + seq.count("T")
    )


def compliment(dna_seq: str) -> str:
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    result = ""

    for c in dna_seq.upper():
        if c == "A":
            result = result + "T"
        elif c == "T":
            result = result + "A"
        elif c == "G":
            result = result + "C"
        elif c == "C":
            result = result + "G"

    return result


def dnaseq_to_mrna(dna_seq: str) -> str:
    return compliment(dna_seq).replace("T", "U")


def codon_frequency(mrna_seq: str) -> dict:
    dic = {}

    assert len(mrna_seq) % 3 == 0, "Invalid mrna sequence length"

    for i in range(0, len(mrna_seq), 3):
        if mrna_seq[i : i + 3] in dic:
            dic[mrna_seq[i : i + 3]] += 1
        else:
            dic[mrna_seq[i : i + 3]] = 1

    return dic


def aminoacid_to_codon(amino_acid: str) -> str or None:
    tac = {
        "A": [
            "GCT",
            "GCC",
            "GCA",
            "GCG",
        ],
        "C": [
            "TGT",
            "TGC",
        ],
        "D": [
            "GAT",
            "GAC",
        ],
        "E": [
            "GAA",
            "GAG",
        ],
        "F": [
            "TTT",
            "TTC",
        ],
        "G": [
            "GGT",
            "GGC",
            "GGA",
            "GGG",
        ],
        "H": [
            "CAT",
            "CAC",
        ],
        "I": [
            "ATA",
            "ATT",
            "ATC",
        ],
        "K": [
            "AAA",
            "AAG",
        ],
        "L": [
            "TTA",
            "TTG",
            "CTT",
            "CTC",
            "CTA",
            "CTG",
        ],
        "M": [
            "ATG",
        ],
        "N": [
            "AAT",
            "AAC",
        ],
        "P": [
            "CCT",
            "CCC",
            "CCA",
            "CCG",
        ],
        "Q": [
            "CAA",
            "CAG",
        ],
        "R": [
            "CGT",
            "CGC",
            "CGA",
            "CGG",
            "AGA",
            "AGG",
        ],
        "S": [
            "TCT",
            "TCC",
            "TCA",
            "TCG",
            "AGT",
            "AGC",
        ],
        "T": [
            "ACT",
            "ACC",
            "ACA",
            "ACG",
        ],
        "V": [
            "GTT",
            "GTC",
            "GTA",
            "GTG",
        ],
        "W": [
            "TGG",
        ],
        "Y": [
            "TAT",
            "TAC",
        ],
        "-": [
            "TAA",
            "TAG",
            "TGA",
        ],
    }

    if amino_acid in tac:
        return choice(tac[amino_acid])
    else:
        return None


input_dna = "TTACGA"
dna_compliment = compliment(input_dna)
mrna = dnaseq_to_mrna(input_dna)

print(f"Input DNA = {input_dna}")
print()
print(f"Compliment DNA = {dna_compliment}")
print(f"mRNA = {mrna}")
print(f"Aminoacid =")
print()

input_aminoacid = "NAN"
mrna = "".join([aminoacid_to_codon(amino_acid) for amino_acid in input_aminoacid])
print(f"Input Aminoacid = {input_aminoacid}")
print()
print(f"mRNA = {mrna}")

codonfreq = codon_frequency(mrna)

for codon in codonfreq.keys():
    print(f"{codon} = {codonfreq[codon]}")
