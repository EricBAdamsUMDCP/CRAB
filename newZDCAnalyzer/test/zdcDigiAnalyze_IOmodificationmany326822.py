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

process.TFileService = cms.Service("TFileService",fileName=cms.string("Tracks_AOD_zdc_digi_tree_326822.root"))

process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(
#326822
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/8294A9BC-7CB1-FA45-8568-2F62CE79360B.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/4DD92603-0B45-9143-A01B-73B5BDAF8F85.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/D64B26D5-6170-AC43-A917-034494E7794D.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00001/03DF21C3-36E9-884C-A2E1-17F9ED4853C8.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/69678A7F-2D04-5E47-821D-BCF71AAA7D1B.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/36AA7ECD-9DBC-3D44-B7B8-4F9C99F420F9.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/472D1FD8-0E9A-B949-AD5F-40C463709DAC.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/2CCC82EE-AB7A-AF4B-9E92-E0192FA5D7DB.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/3871C78A-48C5-8B46-959B-A74FC5B95312.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/6E2BB3E3-F91A-D042-99E0-56DD2F648505.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00001/EBFF4835-2252-3545-94CB-9E517D53E71D.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00001/55181AFE-0FBD-E649-B904-65516AE205C2.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/6974A463-2A78-C645-9362-4BFA9BC5CB4C.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00001/8209576F-DACD-644C-B31C-34AF8BB734E0.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/D06DD85A-E57E-AC49-B24E-E88B3753B95D.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/3F7F1D97-DA3D-FA4B-B040-2797050E2446.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/58530F71-260F-224A-88D1-74BECB770554.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/4A14D9A4-92C0-EB40-9411-7AED058B068E.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/0E915DAA-0A67-BD40-8595-16EFDCDB2374.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00000/86245C15-149D-4540-867C-F4CD57EE4948.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/822/00001/A2772529-ED35-D343-BCCF-3163C909A5A6.root'
))
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
                                hltresults = cms.InputTag("TriggerResults","","HLT"),
                                centralityTag_ = cms.InputTag("hiCentrality") #Eba refers to centrality data from input root files
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
