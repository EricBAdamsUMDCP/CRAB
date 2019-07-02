#!/bin/sh
#id
# hadd 

#hadd merges root files together the format is output file 1 file 2 file 3...
#mv is move from a to b
#ask alice why first part merge seperately????
hadd /data/users/acmignerey/PAMinimumBias2/merging_pPb2016.root /mnt/hadoop/cms/store/user/mignerey/PAMinimumBias2/crab_pPb2016_PromptReco_MinBias2_286516_withCent_regfC_PUrejected/180906_205555/0000/pPb2016_PromptReco_MinBias2_286516_1.root /mnt/hadoop/cms/store/user/mignerey/PAMinimumBias2/crab_pPb2016_PromptReco_MinBias2_286516_withCent_regfC_PUrejected/180906_205555/0000/pPb2016_PromptReco_MinBias2_286516_2.root
mv /data/users/acmignerey/PAMinimumBias2/merging_pPb2016.root /data/users/acmignerey/holder5TeV_pPb2016.root
n=3
while [ $n -le 23 ]; do
#same as before but this is a loop to go to file number 23 and stop
hadd /data/users/acmignerey/PAMinimumBias2/merging_pPb2016.root /data/users/acmignerey/PAMinimumBias2/holder5TeV_pPb2016.root /mnt/hadoop/cms/store/user/mignerey/PAMinimumBias2/crab_pPb2016_PromptReco_MinBias2_286516_withCent_regfC_PUrejected/180906_205555/0000/pPb2016_PromptReco_MinBias2_286516_${n}.root
mv /data/users/acmignerey/PAMinimumBias2/merging_pPb2016.root /data/users/acmignerey/PAMinimumBias2/holder5TeV_pPb2016.root
(( n++ )) # is a n++
done
#reorganizing so as to keep the merging holder and merged seperate this moves it to the final location
mv /data/users/acmignerey/PAMinimumBias2/holder5TeV_pPb2016.root /data/users/acmignerey/PAMinimumBias2/pPb2016_PromptReco_MinBias2_286516_merged.root