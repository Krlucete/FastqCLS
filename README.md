# FastqCLS

The robust FASTQ-specific compressor for recent generation data via score-based reordering.

## Installing

FastqCLS has no external dependencies, using only linux commands and general compressor zpaq.

FastqCLS can be used on docker hub. 

```docker pull krlucete/fastqcls:1.3```

```docker container run -itd --name [Your Container Name] krlucete/fastqcls:1.3```

```docker attach [Your Container Name]```

```cd zpaq-master ```

```make clean```

```make install```

## Usage

FastqCLS is used from the command line. 
Please make sure to move the file to the same path as the command.

The general compression command is:

```python3 cls.py (options) -i [input file] ```

The general decompression command is:

```python3 cls_decomp.py (options) -i [input file] ```

If you wish, you can use the pypy compiler.

```pypy cls.py (options) -i [input file] ```

```pypy cls_decomp.py (options) -i [input file] ```


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

FastqCLS uses the approach described in a paper submitted to Bioinformatics to perform lossless compression. 
Data is reordering by the letter percentage to improve entropy. 

## License

FastqCLS is available under the terms of the MIT. See COPYING for more information.

## Bugs and Feedback

Please use GitHub issues to open bug reports or provide feedback about FastqCLS.

## Authors

FastqCLS was created by DoHyeon Lee at Pusan National University.
