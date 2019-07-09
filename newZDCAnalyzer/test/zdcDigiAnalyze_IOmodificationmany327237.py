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

process.TFileService = cms.Service("TFileService",fileName=cms.string("Tracks_AOD_zdc_digi_tree_327237.root"))

process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(
#327237
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/610009/BEF4B6E4-F3BA-6942-ACA3-0F3B7752BCB1.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/610009/3E20B5C1-F604-7541-813B-458F01929A57.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/DE7AF7ED-0591-7B4A-A8A1-C54ADB59861C.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/BEB279DA-9706-9242-A6F6-7B937651A3CA.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/ABC9DC7D-1FE1-A047-BA20-655C4B63409A.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/C54D2125-CE3D-A244-9972-B181B38C69F6.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/4C3673E6-A551-A249-ABD5-16571AC83A0B.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/FB9E9D20-21E2-944C-B6EB-3EA8169389A4.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/43A01394-C4C6-4245-81E9-B97B0438AE89.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/011EDB89-CCC6-CA4D-9575-D3F1C1BFAF2E.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/00001/68792601-824B-D044-BEC3-F199C74579DA.root ',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/2907A1B4-1565-F840-90EA-0C5825B7DF4C.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/9B4A0FC9-E9E2-4547-83ED-27E9C4A9EAA1.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/8A289694-C0BC-5F4E-A4BC-F44A14C9558E.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/67FFB067-63B3-1941-9C62-DA4F7207ECF2.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/3CA7E7F1-6CC7-FA4F-82E1-12641CD3E291.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/98C969FC-63B9-FE47-814C-606254A79FCA.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/B207EC65-B5C1-6B48-9FFC-A05E776B833E.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/72EF40CB-C50F-E340-958B-F8AC34203850.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/33700D00-39FE-644D-BB53-274B2CA94B54.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/1238FB0B-88BE-394F-B844-B48881EF265C.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/D5523E5F-2DA4-3E4B-B2DA-2EABF86B959D.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/A6CCA45A-A15C-1648-8D93-C895C6465474.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/04Apr2019-v1/100001/D399E71C-D74D-364D-B9C3-EB3286A83C33.root'
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
