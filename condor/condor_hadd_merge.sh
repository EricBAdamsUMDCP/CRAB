#!/bin/bash

cd /cvmfs/cms.cern.ch/slc6_amd64_gcc700/cms/cmssw/CMSSW_10_3_3/src ## your preferred CMSSW version
eval `scramv1 runtime -sh`
cd -


hadd "/home/ebadams/Merged_Root_Files_PbPb2018/MB_2/326943/rereco_PbPb2018_AOD_MinBias2_326943_ZDCandTracks_merged.root" "/home/ebadams/PbPb2018_CMS_DATA_MB2/HIMinimumBias2/crab_rereco_PbPb2018_AOD_MinBias2_326943_ZDC/0000/rereco_PbPb2018_AOD_MinBias2_326943_RPDZDC_"{1..31}.root

