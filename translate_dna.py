# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:52:43 2020

@author: marsh
"""

def translate_dna(sequence):
    codon2aa = {"AAA":"K", "AAC":"N", "AAG":"K", "AAT":"N", 
                "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T", 
                "AGA":"R", "AGC":"S", "AGG":"R", "AGT":"S", 
                "ATA":"I", "ATC":"I", "ATG":"M", "ATT":"I", 

                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAT":"H", 
                "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P", 
                "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R", 
                "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L", 

                "GAA":"E", "GAC":"D", "GAG":"E", "GAT":"D", 
                "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A", 
                "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G", 
                "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V", 

                "TAA":"_", "TAC":"Y", "TAG":"_", "TAT":"Y", 
                "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S", 
                "TGA":"_", "TGC":"C", "TGG":"W", "TGT":"C", 
                "TTA":"L", "TTC":"F", "TTG":"L", "TTT":"F"}
    
    l = [codon2aa.get(sequence[n:n+3], 'X') for n in range(0, len(sequence), 3)]
    return "".join(l)