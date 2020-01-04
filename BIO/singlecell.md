Single Cell
=========

## Terms
- Transcription refers DNA to mRNA.
- Translation refers mRNA to protein.
- Gene expression = transcription + translation.


## Why singlecell?
Same-typed cells are not acually same. For instance, cancer cells perform totally differently, which makes cancer treatment difficult. Thus more fine-grained cell analysis, single-cell analysis, is necessary.

Related work: (Wang+ Nature. 2014.)

## How to gather single cells?

### Microarray
Microarray is a way to measure gene expression. First, prepare for probes, shrot complementary-DNAs and/or nucleotides. They are complementary to the targeting sequence. The spot probes on the slides. After that, hybridize them to mRNAs extracted from a cell. Gene expression is the amount of the luminous intensity. Errors during the measurement of intensity is not ignoreable; it's one of major problems in microarray method.

**template switching** takes an important role in microarray method. Template switching extracts mRNAs from mixtures of various RNAs including rRNA and/or tRNA.

### RNA-Seq
RNA-Seq is a successor of microarray. It doesn't require probes. This gets possible as the sequence reading technology (NGS: Next Generation Sequencer) has been developed. Firstly, reverse-transcrip mRNAs into their cRNAs. After that, propagate them using PCR method. By reading divided sequeces in the PCR product (called reads), RNA-seq restores the original gene expressions. While RNA-seq solves many issues that microarray has, there're still problems; more reads are corresponding to longer mRNAs (We have some normalization, including RPKM).
