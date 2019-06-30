# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
Created on Fri Jun 28 12:08:15 2019

@author: Anastasia

run the script from the directory where you want your output
python3 vcf_data_prep_GRCz11.py /path/to/your/vcf_file

"""

import os
import sys
from subprocess import PIPE, run

ref_directory = "/ebio/ecnv_projects/common_resourses/data/reference_genome/"
cmd_picard = "/ebio/ecnv_projects/common_resourses/data/software/picard-tools-1.130/picard.jar"
cmd_picard2 = "/ebio/ecnv_projects/common_resourses/data/software/picard-tools-1.130/picard2.jar"
cmd_GenomeAnalysisTK = "/ebio/ecnv_projects/common_resourses/data/software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK-3.8-0-ge9d806836/GenomeAnalysisTK.jar"
cmd_GATK4 = "/ebio/ecnv_projects/common_resourses/data/software/gatk-4.0.4.0/gatk-package-4.0.4.0-local.jar"
cmd_vcftools = "/ebio/ecnv_projects/common_resourses/data/software/vcftools/vcftools"

ref = ref_directory + "danRer10.fa"
ref_dict = ref_directory + "danRer10.dict"

#grab the stdout result of a shell command

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout



#input vcf file with a single sample

input_vcf = sys.argv[1]
print(input_vcf)

#input_vcf = "/ebio/ecnv_projects/zebrafish_natural_variation/data/Individual_strains_variants/GRCz10/Mutants/nr30.filtered_snps.vcf"

#identify genotype name as spelled in the vcf - find the last of the column names
grep_cmd = "grep CHROM {}".format(input_vcf)
head_list = out(grep_cmd).strip()

head_list = head_list.split("\t")
genotype = head_list[-1]

print(genotype)

#Use GATK to select heterozygous and homozygous SNPs across the genome and exclude filtered SNPs

select_cmd1 = "java -jar {} -jdk_deflater -jdk_inflater -T SelectVariants --excludeFiltered -R {} -V {} -select 'vc.getGenotype(".format(cmd_GenomeAnalysisTK, ref, input_vcf)

select_cmd2_het = ").isHet()' -o {}_snps_het.vcf".format(genotype) 
select_cmd2_hom = ").isHomVar()' -o {}_snps_hom.vcf".format(genotype)

select_het = select_cmd1 + "\"" + genotype + "\"" + select_cmd2_het
select_hom = select_cmd1 + "\"" + genotype + "\"" + select_cmd2_hom
print(select_het)
os.system(select_het)
os.system(select_hom)

#Collect statistics about SNP density of hom and het snps across the chromosomes

#1MB
snpden_hom_cmd_1m = "{} --vcf {}_snps_hom.vcf --out {}_hom_snps_depth_1m --SNPdensity 1000000".format(cmd_vcftools, genotype, genotype)
snpden_het_cmd_1m = "{} --vcf {}_snps_het.vcf --out {}_het_snps_depth_1m --SNPdensity 1000000".format(cmd_vcftools, genotype, genotype)

#50k
snpden_hom_cmd_50k = "{} --vcf {}_snps_hom.vcf --out {}_hom_snps_depth_50k --SNPdensity 50000".format(cmd_vcftools, genotype, genotype)
snpden_het_cmd_50k = "{} --vcf {}_snps_het.vcf --out {}_het_snps_depth_50k --SNPdensity 50000".format(cmd_vcftools, genotype, genotype)

for item in [snpden_hom_cmd_1m, snpden_het_cmd_1m, snpden_hom_cmd_50k, snpden_het_cmd_50k]:
    print(item)
    os.system(item)
