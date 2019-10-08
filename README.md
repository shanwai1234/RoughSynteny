# RoughSynteny

(lastz version 1.04.00 released 20170312)
lastz Sitalica_312_v2.2.cds_primaryTranscriptOnly.fa[multiple] Sviridis_311_v1.1.cds_primaryTranscriptOnly.fa --ambiguous=iupac --notransition --seed=match12 --identity=90 --coverage=50 ‑‑format=general:score,name1,strand1,size1,zstart1,end1,name2,strand2,size2,zstart2,end2,idfrac,id%,covfrac,cov% --output=Sitalica312v2-Sviridis311v1.lastz

python lastz_to_raw.py Sitalica312v2-Sviridis311v1-fix.lastz --qbed=Sitalica_312_v2.2.gene.bed --sbed=Sviridis_311_v1.1.gene.bed

(running on the server, and need to have correct version of "SCIP")
python quota_align.py --format=raw --merge --Dm=20 --min_size=5 --quota=1:1 Sitalica312v2-Sviridis311v1-fix.qa

python qa_to_pairs.py ../Sitalica312v2-Sviridis311v1-fix.qa.filtered --qbed=Sitalica_312_v2.2.gene.bed --sbed=Sviridis_311_v1.1.gene.bed > Si312v2-Sv311v1-synteny.txt
