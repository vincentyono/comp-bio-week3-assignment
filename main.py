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


def mrna_to_aminoacid(mrna_seq: str) -> str:
    assert len(mrna_seq) % 3 == 0, "Invalid mRNA sequence length"

    def translate(codon: str) -> str:
        if codon == "UUU" or codon == "UUC":
            return "Phe (F)"
        elif (
            codon == "UUA"
            or codon == "UUG"
            or codon == "CUU"
            or codon == "CUC"
            or codon == "CUA"
            or codon == "CUG"
        ):
            return "Leu (L)"
        elif codon == "AUU" or codon == "AUC" or codon == "AUA":
            return "Ile (I)"
        elif codon == "AUG":
            return "Met (M)"
        elif codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG":
            return "Val (V)"
        elif (
            codon == "UCU"
            or codon == "UCC"
            or codon == "UCA"
            or codon == "UCG"
            or codon == "AGU"
            or codon == "AGC"
        ):
            return "Ser (S)"
        elif codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
            return "Pro (P)"
        elif codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
            return "Thr (T)"
        elif codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
            return "Ala (A)"
        elif codon == "UAU" or codon == "UAC":
            return "Tyr (Y)"
        elif codon == "UAA" or codon == "UAG" or codon == "UGA":
            return "Stop (*)"
        elif codon == "CAU" or codon == "CAC":
            return "His (H)"
        elif codon == "CAA" or codon == "CAG":
            return "Gln (Q)"
        elif codon == "AAU" or codon == "AAC":
            return "Asn (N)"
        elif codon == "AAA" or codon == "AAG":
            return "Lys (K)"
        elif codon == "GAU" or codon == "GAC":
            return "Asp (D)"
        elif codon == "GAA" or codon == "GAG":
            return "Glu (E)"
        elif codon == "UGU" or codon == "UGC":
            return "Cys (C)"
        elif (
            codon == "AGA"
            or codon == "AGG"
            or codon == "CGU"
            or codon == "CGC"
            or codon == "CGA"
            or codon == "CGG"
        ):
            return "Arg (R)"
        elif codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG":
            return "Gly (G)"

    result = []
    for i in range(0, len(mrna_seq), 3):
        result.append(translate(mrna_seq[i : i + 3]))

    return " - ".join(result)


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
aminoacid = mrna_to_aminoacid(mrna)

print(f"Input DNA = {input_dna}")
print()
print(f"Compliment DNA = {dna_compliment}")
print(f"mRNA = {mrna}")
print(f"Aminoacid = {aminoacid}")
print()

input_aminoacid = "NAN"
mrna = "".join([aminoacid_to_codon(amino_acid) for amino_acid in input_aminoacid])
print(f"Input Aminoacid = {input_aminoacid}")
print()
print(f"mRNA = {mrna}")

codonfreq = codon_frequency(mrna)

for codon in codonfreq.keys():
    print(f"{codon} = {codonfreq[codon]}")
