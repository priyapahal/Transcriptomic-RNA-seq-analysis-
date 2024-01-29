# -*- coding: utf-8 -*-
"""trial
"""

!mkdir -p raw fastqc multiqc

!wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR176/003/SRR1765723/SRR1765723.fastq.gz
!wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR176/006/SRR1765726/SRR1765726.fastq.gz
!wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR176/004/SRR1765724/SRR1765724.fastq.gz
!wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR176/005/SRR1765725/SRR1765725.fastq.gz

!sudo apt-get -y install fastqc

pip install multiqc

!mv *.gz raw/

!fastqc raw/*.gz -o fastqc/

!multiqc fastqc/ -o multiqc/

!wget https://ftp.ncbi.nlm.nih.gov/genomes/genbank/vertebrate_mammalian/Mus_musculus/latest_assembly_versions/GCA_000001635.9_GRCm39/GCA_000001635.9_GRCm39_genomic.fna.gz

!wget https://ftp.ncbi.nlm.nih.gov/genomes/genbank/vertebrate_mammalian/Mus_musculus/latest_assembly_versions/GCA_000001635.9_GRCm39/GCA_000001635.9_GRCm39_genomic.gtf.gz

!gunzip GCA_000001635.9_GRCm39_genomic.fna.gz
!gunzip GCA_000001635.9_GRCm39_genomic.gtf.gz

!mkdir -p mapping

!wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.6/bowtie2-2.2.6-linux-x86_64.zip

!unzip bowtie2-2.2.6-linux-x86_64.zip

!/content/bowtie2-2.2.6/bowtie2-build GCA_000001635.9_GRCm39_genomic.fna mapping/mus_muscullus (./bowtie2-2.2.6/bowtie2-build /home/amjesh/GCA_000001635.9_GRCm39_genomic.fna /home/amjesh/mapping/mus_muscullus)

!/content/bowtie2-2.2.6/bowtie2 -x mapping/mus_muscullus -1 raw/SRR1765723.fastq.gz -2 raw/SRR1765724.fastq.gz -S mapping/SRR1765723.sam

!/content/bowtie2-2.2.6/bowtie2 -x mapping/mus_muscullus -1 raw/SRR1765725.fastq.gz -2 raw/SRR1765726.fastq.gz -S mapping/SRR1765725.sam

!apt-get install autoconf automake make gcc perl zlib1g-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev libncurses5-dev

! wget https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2 -O samtools.tar.bz2

!tar -xjvf samtools.tar.bz2

! samtools-1.3.1/.configure --prefix=/bin/bash

!sudo apt-get install samtools

!samtools view -S -b mapping/SRR1765723.sam >mapping/SRR1765723.bam

!samtools view -S -b mapping/SRR1765725.sam >mapping/SRR1765725.bam

!sudo apt-get install subread

!mkdir -p read_count

!featureCounts -g gene_id -T 10 -O -M -a GCA_000003055.5_Bos_taurus_UMD_3.1.1_genomic.gtf -o read_count/bowtie_fct_gene mapping/SRR1765723.bam

!featureCounts -g gene_id -T 10 -O -M -a GCA_000003055.5_Bos_taurus_UMD_3.1.1_genomic.gtf -o read_count/bowtie_fct_gene mapping/SRR1765725.bam

!cut -f1,7,8,9,10,11,12 read_count/bowtie_fct_gene > read_count/bt2_featurecounts_gene_count.Rmatrix.txt
