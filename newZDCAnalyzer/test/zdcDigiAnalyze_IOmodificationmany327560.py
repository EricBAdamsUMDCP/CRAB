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

process.TFileService = cms.Service("TFileService",fileName=cms.string("AOD_zdc_digi_tree_327560_many.root"))

process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/0AB47FC5-69FD-DD45-B001-F1793F12D1ED.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/0329E85F-FEB5-8448-BF59-D9857F32DB71.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/6EEC2E74-E089-9E4E-9AE3-1444FCA15FEF.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/2644BEE5-881B-9544-939F-063BB1068927.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/2815C3E3-8A1A-FC47-8259-24F5EA1095C4.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/2440E655-4C5A-D246-9523-572A7ED192EC.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/7562F38A-BFF2-AB47-9930-D6C9E557CA2A.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/DE9AB959-5911-A141-9808-74D2BED6BA79.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/83092BE2-B0B9-D94B-AA26-F1C90A7D78F2.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/28D439FD-FB35-FA4C-8160-B8B40A0DE3FE.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/6E28F47B-67E6-0341-9DF2-4EBCE532578B.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/882AFE84-88D7-F84E-B6AD-39E0DBA9F2EC.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/17D67424-5A01-FB47-B287-5551C77E24A5.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/0F4F3D5B-4EEB-314F-B0BF-A4DF7746B09C.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/777CEA03-CB88-0D45-A59B-EC5BCF4E4B06.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/103C3E7C-99B5-4E48-907D-B74EFF6E595C.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/4EEF4843-59CF-1343-9599-DF07B92E170E.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/BDC333F8-5F5D-4D44-9435-43BB27579077.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/77DD2F76-80BE-0140-9D07-02D6B0D8F240.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/71095DD0-BF2D-4944-AB36-AB3C1C18B122.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/BA688291-663B-C646-BBFE-7FB2AE5A869D.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/AE8A3E71-122D-BA4D-9BA1-CCBA3CFA59E7.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/9AF72C15-C1FC-2E4F-A2D4-6CBDD109264B.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/0CDBA830-CA54-EC45-A271-5FE3F6567D87.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/2F746AED-B3D4-404C-80A4-4F455D581747.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/DC33C997-35D3-414A-B4F8-231900FF66C7.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/09FD08C9-8C95-AA4D-A883-5C6743551289.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/1F839D1F-B84C-E244-BF02-2C4F6994D1DA.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/A7C999B9-EF19-644F-A405-A2567B75B98E.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/1BDBBE0B-5C08-954D-B8F3-53A4D730EFDB.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/15F8F83E-F697-B343-920B-024ECAAAC30F.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/432C00D0-E073-0141-8A34-50614F2FD963.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/C8070E4B-61A3-764D-AB73-14099E190A3F.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/A9B752F5-4461-4F45-839E-D58E794FEEBB.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/04B0F0FD-4A6E-3E44-98BA-70D28C07B9DB.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/D395E675-FF8D-2C4D-9781-822B20D807CF.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/A7277B1A-D1DF-1246-9A65-A2E0F88C0923.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/4CC22105-835F-104B-86B0-D109E1A2D2BD.root',
'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v2/000/327/560/00000/DA061638-E080-104D-B9CA-6A2FCE5A85F1.root'))
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
