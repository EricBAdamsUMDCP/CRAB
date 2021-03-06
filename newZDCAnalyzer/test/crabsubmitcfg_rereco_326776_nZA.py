import FWCore.ParameterSet.Config as cms
from CRABClient.UserUtilities import config

#process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring()) #Added 5/13

config = config()
config.General.requestName = 'PbPb2018_326776'
config.General.transferLogs = True
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.outputFiles = ['PbPb2018_AOD_MinBias2_326776_nZA.root']
config.JobType.pyCfgParams = ['noprint']
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'FOR_CRAB_zdcDigiAnalyze_IOmodificationmany.py' #MUST BE IN SAME FOLER OR GIVE FULL PATH
config.Data.inputDataset = '/HIMinimumBias2/HIRun2018A-04Apr2019-v1/AOD' #I  this is right CHANGE TO MINIMUM BIAS 2 (FROM 1)
#config.Data.inputDataset = '/PAMinimumBias2/PARun2016D-PromptReco-v1/AOD' old line
config.Data.splitting = 'FileBased' #LumiBased
config.Data.unitsPerJob = 20
config.Data.publication = False
lumi_mask='Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt' #include this in the same directory as the crab submit
config.Data.outLFNDirBase = '/store/user/eadams'
config.Data.runRange = '327126'
config.Site.storageSite = 'T3_US_FNALLPC'
