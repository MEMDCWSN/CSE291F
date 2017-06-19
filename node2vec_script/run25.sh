#! /bin/bash
for i in 0.25 0.5 1 2 4;
do 
  m=$(expr $i*100 | bc)
  ms=${m%.*}
  for j in 0.25 0.5 1 2 4;
  do 
    n=$(expr $j*100 | bc)
    ns=${n%.*}
    python src/main.py --p $i --q $j --input graph/astrophy.edgelist --output emb/astrophy_${ms}_${ns}.emd
  done
done
