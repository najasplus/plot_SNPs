## plot_SNPs
Plot distribution of heterozygous and homozygous SNPs over the chromosomes

Input: 
vcf file with variants from a single sample (otherwise only the last sample will be used).
The script exists in the variants for vcf files produced using GRCz11 (Ensembl) or Grcz10 (UCSC) as the reference. Please mind the version of the genome when selecting the script to use!

The python script will: 
* call GATK to extract and save homozygous and heterozygous SNPs (or indels) in your working directory 
* apply vcftools to homozygous and heterozygous SNPs to calculate SNP density over the windows of 1Mb and 50kb
* create an R script from template included in the repository and call it
* The R script will plot the distribution of SNPs over the chromosomes and save it as PNG in the working directory

To run the script from command line:

```{bash}

mkdir yourworkingdirectory #please mind the disc quota! It should be sufficient for writing the vcf files of homozygous and heterozygous SNPs

cd yourworkingdirectory

python3 /path/to/vcf_data_prep_GRCz11.py path/to/variant_calls.vcf #Please provide absolute path to the vcf_data_prep_GRCz11.py
```

Please note: at the momen the script needs either the absolute or relative path to the vcf_data_prep_GRCz1*.py. If the script is in your working directory, use "./vcf_data_prep_GRCz1*.py"

Example command for eCNV group:
```
python3 /ebio/ecnv_projects/common_resourses/code/prepare_vcf_data_for_plotting/vcf_data_prep_GRCz11.py /ebio/ecnv_projects/zebrafish_natural_variation/data/Individual_strains_variants/GRCz11/Mutants/aub.S960Nr1.filtered_indels.vcf
```
