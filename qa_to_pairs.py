#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
%prog qa_file --qbed query.bed --sbed subject.bed

convert qa_file back to the original gene names
"""
a = open('maizev4_sorghumv3_6_27_2017.csv','w')
a.write('Sorghum3.1\tMaize4.1\n')
import sys

from bed_utils import Bed, RawLine

def qa_to_pairs(qa_file, qbed, sbed):

    for line in open(qa_file):
        if line[0] == "#":
            #print line,
            continue
        s = RawLine(line)
        try:
            query = qbed[s.pos_a].accn
            subject = sbed[s.pos_b].accn
            yield query, subject
        except:
            print 'what the heck'

if __name__ == "__main__":

    import optparse

    parser = optparse.OptionParser(__doc__)
    parser.add_option("--qbed", dest="qbed",
            help="path to qbed")
    parser.add_option("--sbed", dest="sbed",
            help="path to sbed")

    (options, args) = parser.parse_args()

    if not (len(args) == 1 and options.qbed and options.sbed):
        sys.exit(parser.print_help())

    qbed = Bed(options.qbed)
    sbed = Bed(options.sbed)

    qa_file = args[0]

    for q, s in qa_to_pairs(qa_file, qbed, sbed):
        #print "\t".join((q, s))
        a.write(''.join(q)+'\t'+''.join(s)+'\n')
