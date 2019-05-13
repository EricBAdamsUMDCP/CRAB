#THIS HAS THE VSTRING EMPTY TO ALLOW CRAB TO FILL THE NECESSARY LUMI SECTIONS, IMPORTANTLY.
										################
										#FOR RUN 326776#
										################
import FWCore.ParameterSet.Config as cms
#ADDED line 3
import FWCore.PythonUtilities.LumiList as LumiList
#note json file must be in same folder at config file
from Configuration.StandardSequences.Eras import eras

from CRABClient.UserUtilities import config

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

config.Data.inputDataset = '/HIMinimumBias2/HIRun2018A-PromptReco-v1/AOD'   #'/HIMinimumBias2/AOD/PromptReco-v1/AOD' #I hope this is right //added 5/13

process.TFileService = cms.Service("TFileService",fileName=cms.string("AOD_zdc_digi_tree_326776_CRAB.root"))

process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring())
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
