#!/bin/bash

cd /cvmfs/cms.cern.ch/slc6_amd64_gcc700/cms/cmssw/CMSSW_10_3_3/src ## your preferred CMSSW version
eval `scramv1 runtime -sh`
cd -


hadd "/home/ebadams/Merged_Root_Files_PbPb2018/MB_2/326822/rereco_PbPb2018_AOD_MinBias2_326822_ZDCandCENT_ONLY_merged.root" "/home/ebadams/PbPb2018_CMS_DATA_MB2/HIMinimumBias2/crab_rereco_PbPb2018_AOD_MinBias2_326822_ZDC_and_CENT/190722_153416/0000/rereco_ZDC_AND_CENT_PbPb2018_AOD_MinBias2_326822_"{1..56}.root

