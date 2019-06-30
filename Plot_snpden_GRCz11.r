#setwd() and base_name should be set by python script 


library(readr)
library(ggplot2)
library(methods)


het_file_1m <- list.files(pattern = paste0(base_name, "_het_snps_depth_1m.snpden"))
hom_file_1m <- list.files(pattern = paste0(base_name, "_hom_snps_depth_1m.snpden"))

het <- read_tsv(het_file_1m, col_types = cols("CHROM" = "c"))
hom <- read_tsv(hom_file_1m, col_types = cols("CHROM" = "c"))

#make chromosome list from chr1 to chr25 according to Ensembl GRCz11

chr_list = seq(1:25)

het_chr <- het[het$CHROM %in% chr_list,]
hom_chr <- hom[hom$CHROM %in% chr_list,]

het_chr <- cbind(het_chr, HOM = rep("het", nrow(het_chr)))
hom_chr <- cbind(hom_chr, HOM = rep("hom", nrow(hom_chr)))

#prepare data frame for plotting with ggplot2
full_snps <-rbind(hom_chr, het_chr)

#plot snpsdensity with 1Mb resolution

g <- ggplot(full_snps, aes(BIN_START, SNP_COUNT, color = HOM)) +
  geom_line()+
  facet_wrap(~CHROM, ncol = 5) + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
g

ggsave(paste0(base_name, "_1m.png"), g, width = 150, height = 150, units = "mm", limitsize = F)

#50k resolution

het_file_50k <- list.files(pattern = paste0(base_name, "_het_snps_depth_50k.snpden"))
hom_file_50k <- list.files(pattern = paste0(base_name, "_hom_snps_depth_50k.snpden"))

het50k <- read_tsv(het_file_50k, col_types = cols("CHROM" = "c"))
hom50k <- read_tsv(hom_file_50k, col_types = cols("CHROM" = "c"))

het_chr50k <- het50k[het50k$CHROM %in% chr_list,]
hom_chr50k <- hom50k[hom50k$CHROM %in% chr_list,]

het_chr50k <- cbind(het_chr50k, HOM = rep("het", nrow(het_chr50k)))
hom_chr50k <- cbind(hom_chr50k, HOM = rep("hom", nrow(hom_chr50k)))

full_snps50k <-rbind(hom_chr50k, het_chr50k)

#plot chr1-25

g <- ggplot(full_snps50k, aes(BIN_START, SNP_COUNT, color = HOM)) +
  geom_line()+
  facet_wrap(~CHROM, ncol = 5) + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
g

ggsave(paste0(base_name, "_50k.png"), g, width = 150, height = 150, units = "mm", limitsize = F)

