# -*- coding: ascii -*-

"""
morinkit.vcf
~~~~~~~~~~~~

This module contains utility functions relevant to VCF files.
"""

from itertools import chain
import logging


def count_alleles_strelka(variant, max_alt_alleles=1, tier1_only=True):
    """Count reads supporting reference and alternate alleles.

    Note that it is possible for a VCF variant to contain multiple
    alternate alleles. By default, this function only returns the
    first alternate allele, which covers most use cases. If this is
    changed to another value, you cannot expect the same number of
    alternate alleles for each variant.

    Args:
        variant: A VCF row variant.
        max_alt_alleles: An integer for the number of alternate alleles
            included in the returned list.
        tier1_only: A boolean for whether you only want to consider reads
            marked as tier-1 by Strelka. See Strelka paper for more info.

    Returns:
        A list of tuples containing the reference and alternate counts
        (integers) for each sample, or None if the variant is not a SNV
        or indel.
    """

    def get_allele_counts(variant, fmt_keys, tier1_only):
        """Extract allele counts."""
        total_counts = []
        # TODO (brunogrande): Find better way to get number of samples other
        # than `len(variant.gt_depths)`. The num_called variant attribute seems
        # relevant, but causes a Python segmentation fault. Fix once this issue
        # is closed: https://github.com/brentp/cyvcf2/issues/17
        for i in range(len(variant.gt_depths)):
            sample_counts = []
            for key in keys:
                allele_count = variant.format(key, int)[i]
                if tier1_only:
                    tier1_count = int(allele_count[0])
                    sample_counts.append(tier1_count)
                else:
                    all_tiers_count = int(allele_count[1])
                    sample_counts.append(all_tiers_count)
            total_counts.append(tuple(sample_counts))
        return total_counts

    # Call appropriate function based on variant type.
    if variant.is_snp:
        # variant.REF is a string while variant.ALT is a list
        # Thurs, variant.REF needs to be stored into a list before chaining
        alleles = chain([variant.REF], variant.ALT[:max_alt_alleles])
        keys = ['{}U'.format(allele) for allele in alleles]
        counts = get_allele_counts(variant, keys, tier1_only=tier1_only)
    elif variant.is_indel:
        # Strelka uses confusing terminology
        # TAR: Alternate (reference)
        # TIR: Indel (actual alternate)
        keys = ['TAR', 'TIR']
        counts = get_allele_counts(variant, keys, tier1_only=tier1_only)
    else:
        logging.warn("Encountered a variant that is not a SNV, nor an indel: {}".format(variant))
        counts = None
    return counts
