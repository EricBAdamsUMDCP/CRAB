#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc700 #may need to use the slc 7 version
eval `scramv1 project CMSSW CMSSW_10_3_3_patch1`
cd CMSSW_10_3_3_patch1/src/
eval `scramv1 runtime -sh` # cmsenv is an alias not on the workers
echo "CMSSW: "$CMSSW_BASE #end set up of CMSSW
cd ${_CONDOR_SCRATCH_DIR}
xrdcp root://cmseos.fnal.gov//store/user/eadams/input_file.root . 
root -b -q good1.C
xrdcp output_file.root root://cmseos.fnal.gov//store/user/eadams/output_file.root
### the output file is removed before the job ends because otherwise
### condor will transfer it to your submit directory at the end of the job
rm output_file.root

#DONT FORGET TO SET PERMISSION TO EXECUTE IN BASH!!!!
#submit many jobs with condor http://chtc.cs.wisc.edu/multiple-jobs.shtml#process
#it will likely be best to merge smaller root files
#into sizes from 1-5 GB then submit them.
#https://uscms.org/uscms_at_work/computing/setup/condor_worker_node.shtml#NFSdiskMigrate
# need to create a shell script that takes a input numbering e.g. 1-35 so just input 35
#this hsell screates 35 LPC_condor_for_skimming.sh in whih the numbering of the input and ouput file is +1
#it must also create 35 example.C files and change their number t +1 up to 35