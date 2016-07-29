# -*- coding: ascii -*-

"""
morinkit.calc
~~~~~~~~~~~~~

This module contains top-level functions that calculate or summarise files.
"""

import logging
from cyvcf2 import VCF
from .vcf import count_alleles_strelka


def calc_strelka_vaf(vcf_files, output):
    """Calculate the variant allele fraction (VAF) from a Strelka VCF file.

    Args:
        vcf_files: List of opened files pointing to VCF files
        output: Opened writeable file for output
    """
    logging.info('Running calc_strelka_vaf')
    with open(output, 'w') as ofile:
        for vcf in vcf_files:
            logging.info('Processing {}'.format(vcf))
            vcf_reader = VCF(vcf)
            for variant in vcf_reader:
                counts = count_alleles_strelka(variant)
                if counts is None:
                    continue
                oline = '\t'.join(str(x) for x in [variant.CHROM, variant.POS, variant.REF, variant.ALT, counts])
                ofile.write(oline + '\n')
    logging.info('Finished running calc_strelka_vaf')
