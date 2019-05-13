import FWCore.ParameterSet.Config as cms
#ADDED line 3
import FWCore.PythonUtilities.LumiList as LumiList
#note json file must be in same folder at config file
from Configuration.StandardSequences.Eras import eras

process = cms.Process("Demo",eras.Run2_2018_pp_on_AA)

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')

#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.TFileService = cms.Service("TFileService",fileName=cms.string("AOD_zdc_digi_tree_327126_many.root"))

process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/52817F13-0D9F-6F4B-9639-56755E393276.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/DDCB82C7-1680-814E-8326-289CD90CD997.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/3769AEB9-D6ED-AD47-8376-C452B081211A.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/E31D9945-F26C-CA44-98C4-B33614F7CD20.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/E6553281-A58C-8D4C-8132-3532B738051F.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/4C6AFA58-B3C6-344D-BB03-1B4A8E6949ED.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/FBFB66F7-CD00-B54A-AA52-54F5BBF0E31F.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/EFE26BC0-52C0-3547-B23B-2D30DF63937A.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/2331CD4F-76C2-BC4B-BE60-A42E723FE3E3.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/DF58554A-8B0D-524A-831C-DE1E23E2A4D9.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/FDEEAB62-F067-CD46-8D25-F8AF44B7B1EF.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/605C6FEA-3B9D-134E-AC2F-893744A4BE40.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/1AF5746B-0F13-404B-85B2-A06C9D220D4A.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/E6DD4E80-CB24-8C4F-9D91-1F1013D893F3.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/008ACF93-1C35-A44A-A3FC-4198113D2B65.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/2AB9CC33-1375-4D49-8829-DE98EEEAE1F0.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/E48EA669-044E-FF49-B7AB-3CD76946D877.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/998A26BB-6EC7-A044-9791-B227748CE41E.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/BAC22EB6-5B9E-F341-926F-83ED1A09B508.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/7C180F6C-5CAC-104B-85D6-A914B090B9F8.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/0C954FE0-0B5C-914D-8A3D-37E24E8819A1.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/0EB6DD36-0A57-7A47-91F8-E8C494455275.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/F823FD5C-9A8E-6648-A70C-5B886F9ECC7F.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/CF2B8288-EF39-E947-B2D4-3F226078803B.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/78A1503B-ABB9-384F-AA39-6FEF8121A0D7.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/3858E520-5937-9F45-B84C-4FE9936B400C.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/6148370B-7867-AA4C-BE2A-B35BE2025832.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/DA9FEE94-4C53-C845-9E4E-46758DD190F9.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/2F5D1E46-2BE9-6941-9ACC-02F14E91FB21.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/126/00000/ACE22E9D-6CAA-AF48-B743-558ADBA94A7B.root'))
#process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring('/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/776/00000/42FDBB3F-421D-1A40-9D5F-DA88DAF86B4A.root'))
#process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring('file:test_reco_py_RAW2DIGI_RECO.root'))
#Insert JSON file name below
JSONfile = 'Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt'
#added line below this comment
process.source.lumisToProcess = LumiList.LumiList(filename = JSONfile).getVLuminosityBlockRange()
process.analyzer = cms.EDAnalyzer('newZDCAnalyzer',
                                zdc = cms.InputTag("hcalDigis","ZDC","RECO"),
                                tower = cms.InputTag("towerMaker"),
                                track = cms.InputTag("generalTracks"),
                                pixel = cms.InputTag("siPixelRecHits"),
                                hltresults = cms.InputTag("TriggerResults","","HLT")
                                )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = '92X_upgrade2017_realistic_v10'
#process.GlobalTag.globaltag = '103X_dataRun2_Express_v2'
process.GlobalTag.globaltag = '103X_dataRun2_Prompt_v3'


#process.es_ascii = cms.ESSource(
#    'HcalTextCalibrations',
#    input = cms.VPSet(
#            cms.PSet(
#                object = cms.string('ElectronicsMap'),
#                file = cms.FileInPath("QWAna/QWNtrkOfflineProducer/run2018/HcalElectronicsMap_2018_v3.0_data_ext.txt")
#                )
#          )
#)
#process.es_prefer = cms.ESPrefer('HcalTextCalibrations', 'es_ascii')


#set digi and analyzer
#process.hcalDigis.InputLabel = "rawDataCollector"

#process.QWInfo = cms.EDProducer('QWEventInfoProducer')

# ZDC info
#process.load('QWZDC2018Producer_cfi')
#process.load('ZDC2018Pedestal_cfg')
#process.zdcdigi.SOI = cms.untracked.int32(4)

#process.digiPath = cms.Path(
#    process.hcalDigis *
#    process.zdcdigi
#)

process.analyze_step = cms.Path(process.analyzer)

process.schedule = cms.Schedule(
#                    process.digiPath,
                    process.analyze_step)
