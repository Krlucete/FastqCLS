# FASTQ_Cle

The robust FASTQ-specific compressor for recent generation data via score-based reordering.

## Installing

FASTQ_Cle has no external dependencies, using only linux commands and general compressor zpaq.

FASTQ_Cle can be used on docker hub. 
```docker pull krlucete/rocre:1.0```

## Usage

FASTQ_Cle is used from the command line. 

The general compression command is:

```cle (options) [input file] [output file]```

The general decompression command is:

```decle (options) [input file] [output file]```

Input and output must be files, currently it does not process standard input or output.

Available options are:

```
Operating Mode:
-p [#]        Use # as the number of threads on general compressor. (default : 8)
              Use 0 if you wish to use the number of prcessor cores.

Checking Parameters:
-sT [#]       Use # as a threshold of letter percentage on raw sequence (default : 5)
-qT [#]       Use # as a threshold of letter percentage on quality (default : 1)

Extra Options:
-h            Print help summary
```

## Algorithm

FASTQ_Cle uses the approach described in a paper submitted to Bioinformatics to perform lossless compression. 
Data is reordering by the letter percentage to improve entropy. 
clustered to reduce global variability, then each cluster is compressed by calculating a set of quantization
matrices that performs optimally under the chosen distortion metric and the empirical statistics of
the data, using a first order Markov prediction model.

## License

FASTQ_Cle is available under the terms of the GPLv3. See COPYING for more information.

## Bugs and Feedback

Please use GitHub issues to open bug reports or provide feedback about FASTQ_Cle.

## Authors

FASTQ_Cle was created by DoHyeon Lee at Pusan National University.
