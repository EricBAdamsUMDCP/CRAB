import FWCore.ParameterSet.Config as cms
from CRABClient.UserUtilities import config

#for use storing at LPC

#process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring()) #Added 5/13

config = config()
config.General.requestName = 'rereco_PbPb2018_AOD_MinBias2_327524_ZDC_and_CENT'
config.General.transferLogs = True
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.outputFiles = ['rereco_ZDC_AND_CENT_PbPb2018_AOD_MinBias2_327524.root']
config.JobType.pyCfgParams = ['noprint']
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '327524_rerecoForCRABpythonfileforModernProductionofZDC_and_CENT.py' #MUST BE IN SAME FOLER OR GIVE FULL PATH
config.Data.inputDataset = '/HIMinimumBias2/HIRun2018A-04Apr2019-v1/AOD' 
config.Data.splitting = 'FileBased' #LumiBased
config.Data.unitsPerJob = 20
config.Data.publication = False
lumi_mask='Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt' #include this in the same directory as the crab submit
config.Data.outLFNDirBase = '/store/user/eadams' #I believe this is correct
config.Data.runRange = '327524'
config.Site.storageSite = 'T3_US_UMD'
#'T3_US_UMD'
