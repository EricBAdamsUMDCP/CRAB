import FWCore.ParameterSet.Config as cms
from CRABClient.UserUtilities import config

#for use storing at LPC

#process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring()) #Added 5/13

config = config()
config.General.requestName = 'rereco_PbPb2018_AOD_MinBias2_327327_ZDC'
config.General.transferLogs = True
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.outputFiles = ['rereco_PbPb2018_AOD_MinBias2_327327_RPDZDC.root']
config.JobType.pyCfgParams = ['noprint']
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'rerecoForCRABpythonfileforModernProduction_327327.py' #MUST BE IN SAME FOLER OR GIVE FULL PATH
config.Data.inputDataset = '/HIMinimumBias2/HIRun2018A-04Apr2019-v1/AOD' 
config.Data.splitting = 'Automatic' #'FileBased' #LumiBased
config.Data.unitsPerJob = 183 #20
config.Data.publication = False
lumi_mask='Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt' #include this in the same directory as the crab submit
config.Data.outLFNDirBase = '/store/user/eadams' #I believe this is correct
config.Data.runRange = '327327'
config.Site.storageSite = 'T3_US_FNALLPC'
#'T3_US_UMD'
