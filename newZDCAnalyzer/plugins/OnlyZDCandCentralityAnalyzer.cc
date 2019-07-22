// -*- C++ -*-
//
// Package:    ZDC/OnlyZDCandCentralityAnalyzer
// Class:      OnlyZDCandCentralityAnalyzer
//
/**\class OnlyZDCandCentralityAnalyzer OnlyZDCandCentralityAnalyzer.cc ZDC/OnlyZDCandCentralityAnalyzer/plugins/OnlyZDCandCentralityAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Sourced from Oliver Suranyi, Thank you!
//parts butchered from Will McBrayer's analyzer
//And some ideas from Jaime Gomez's analyzer
//  Edited & written by Eric Adams wih the Assitance of Colin Champney
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h" //eba added

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetUnit.h"

#include "DataFormats/CaloRecHit/interface/CaloRecHit.h"
#include "DataFormats/HcalDetId/interface/HcalDetId.h"
#include "DataFormats/HcalRecHit/interface/HFRecHit.h"
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"
#include "DataFormats/HeavyIonEvent/interface/Centrality.h" //EBA
#include "CondFormats/HIObjects/interface/CentralityTable.h" //EBA dont know if file location will work

#include "DataFormats/CaloTowers/interface/CaloTower.h"
#include "DataFormats/CaloTowers/interface/CaloTowerCollection.h"
//#include "DataFormats/CaloTowers/interface/CaloTowerFwd.h"
#include "DataFormats/EcalDetId/interface/EcalSubdetector.h"
#include "DataFormats/HcalDetId/interface/HcalSubdetector.h"

#include "CalibFormats/HcalObjects/interface/HcalCoderDb.h"
#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "CalibCalorimetry/HcalAlgos/interface/HcalPulseShapes.h"
#include "Geometry/Records/interface/HcalRecNumberingRecord.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

#include "DataFormats/DetId/interface/DetId.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/IdealGeometryRecord.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/Handle.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "Math/Vector3D.h" //eba added

#include "TTree.h"

#include "nominal_fC.h"

//
// class declaration
//


const int MAX = 50000;
const int MAX_TS = 10;

class OnlyZDCandCentralityAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
  public:
    explicit OnlyZDCandCentralityAnalyzer(const edm::ParameterSet&);
    ~OnlyZDCandCentralityAnalyzer();

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


  private:
    virtual void beginJob() override;
    virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;

    bool TrackQuality_HIReco(const reco::TrackCollection::const_iterator& itTrack, const reco::VertexCollection&);
                                                                                    //may add back in coonst


    // ----------member data ---------------------------
    //HLTPrescaleProvider hltPrescaleProvider_;
    string trgResultsProcess_;
    
    edm::Service<TFileService> fs;

    edm::EDGetTokenT<QIE10DigiCollection> zdcToken;
    edm::EDGetTokenT<CaloTowerCollection> caloTowerToken;
    edm::EDGetTokenT<edm::TriggerResults> hltToken;
    edm::EDGetTokenT<reco::TrackCollection> trackToken;
    //edm::EDGetTokenT<SiPixelRecHitCollection> pixelToken;
    ///EBA adding centrality
    edm::InputTag centralityTag_;
    edm::EDGetTokenT<reco::Centrality> centralityToken;
    edm::Handle<reco::Centrality> centrality_; //EBA token

    edm::InputTag vertexTag_;
    edm::EDGetTokenT<std::vector<reco::Vertex>> vertexToken; //EBA added
    edm::Handle<std::vector<reco::Vertex>> vertex_;


// REMEBER TO MODIFY .XML THIS IS LIKELY WHY UPDATING THE ANALYZER AND A CONTINUATION OF CRASHES IS OCCURING!!

   // https://github.com/ssanders50/PbPb_2018/blob/5628f011b98cb4b51767668558ee7cadd9a307a5/CMSSW_10_3_2/src/HeavyIonsAnalysis/EventAnalysis/src/HiEvtAnalyzer.cc useful 

    TTree* zdcDigiTree;
    int run, lumi, event, bxid;
   
    int n;

    int zside[MAX];
    int section[MAX];
    int channel[MAX];
    int adc[MAX_TS][MAX];
    float nfC[MAX_TS][MAX];
    float rfC[MAX_TS][MAX];

    int rejected = 0;

    double centval = 0; //EBA variable to store values

    int nRejectedTracks = 0;


    bool firstEvent;
    int* trigflag;
    int* prscflag;
    //HLTPrescaleProvider hltPrescaleProvider;

};

OnlyZDCandCentralityAnalyzer::OnlyZDCandCentralityAnalyzer(const edm::ParameterSet& iConfig) /*:
  hltPrescaleProvider(iConfig, consumesCollector(), *this)*/{

  usesResource("TFileService");
  zdcToken = consumes<QIE10DigiCollection>(iConfig.getParameter<edm::InputTag>("zdc")); //creates token that uses resource "zdc" from input parameter(?)
  caloTowerToken = consumes<CaloTowerCollection>(iConfig.getParameter<edm::InputTag>("tower"));
  hltToken = consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("hltresults"));
  trgResultsProcess_ = iConfig.getParameter<edm::InputTag>("hltresults").process();
  //hltCfg = hltPrescaleProvider_.hltConfigProvider(iConfig, consumesCollector(), *this);

  centralityTag_ = iConfig.getParameter<edm::InputTag>("centralityTag_"); //EBA got config
  centralityToken = consumes<reco::Centrality>(centralityTag_); //EBA obtain token for centrality info referenced in config file
}


OnlyZDCandCentralityAnalyzer::~OnlyZDCandCentralityAnalyzer(){
}


//
// member functions
//

// ------------ method called for each event  ------------
void OnlyZDCandCentralityAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){

  event = iEvent.id().event();
  run = iEvent.id().run();
  lumi = iEvent.luminosityBlock();
  bxid = iEvent.bunchCrossing();

  // Processing ZDC QIE10 digis
  edm::Handle<QIE10DigiCollection> zdcDigiCollection;
  iEvent.getByToken(zdcToken, zdcDigiCollection); //gets resource from zdcToken and stores its data in zdcDigiCollection

  //edm::ESHandle<HcalDbService> conditions;
  //iSetup.get<HcalDbRecord>().get(conditions);

  // Add ZDC digi branches to event tree in the first cycle
  if(firstEvent){
    const QIE10DataFrame& frame = (*zdcDigiCollection)[0];
    std::cout << "Number of timeslices: " << frame.samples() << std::endl;

    for(int i=0; i < frame.samples();i++){
      TString adc_str("adc"), nfC_str("nfC"), rfC_str("rfC");
      adc_str+=i; nfC_str+=i, rfC_str+=i;

      zdcDigiTree->Branch(adc_str,adc[i],adc_str+"[n]/I");
      zdcDigiTree->Branch(nfC_str,nfC[i],nfC_str+"[n]/F");
      //zdcDigiTree->Branch(rfC_str,rfC[i],rfC_str+"[n]/F");
    }
  }

  n = 0;
  rejected = 0;

  bool valid = true;

  // Read ZDC QIE10 digis  
  for(QIE10DigiCollection::const_iterator it = zdcDigiCollection->begin(); it != zdcDigiCollection->end(); it++) {
    const QIE10DataFrame& frame(*it);
    CaloSamples caldigi;

    HcalZDCDetId cell = frame.id();

    /*const HcalQIECoder* qiecoder = conditions->getHcalCoder(cell);
    const HcalQIEShape* qieshape = conditions->getHcalShape(qiecoder);
   
    HcalCoderDb coder(*qiecoder,*qieshape);
    coder.adc2fC(frame,caldigi);*/

    zside[n] = cell.zside();
    section[n] = cell.section();
    channel[n] = cell.channel();

    int prevCapID;

    for(int isample = 0; isample < 10; isample++){
      if(isample != 0 && frame[isample].capid() != ((prevCapID+1)%4)){
        valid = false;
        rejected++;
        for(int jsample = 0; jsample < 10; jsample++){
          std::cout << frame[jsample].capid() << std::endl;
        }
        while(!getchar());
        break;
      }
      prevCapID = frame[isample].capid();

      adc[isample][n] = frame[isample].adc();
      nfC[isample][n] = QIE10_nominal_fC[frame[isample].adc()];
      //rfC[isample][n] = caldigi[isample];
    }

    n++;
  }

  // Processing HF towers
  edm::Handle<CaloTowerCollection> towerCollection;
  iEvent.getByToken(caloTowerToken,towerCollection);

  

//vertex checking
  //may need to move handle

  

  //nAcceptedTracks = nTrack - nRejectedTracks;
  // Processing centrality   // EBA added
  iEvent.getByToken(centralityToken, centrality_); //obtain centrality object from input via token and pass to centralityHandle
  centval = centrality_->EtHFtowerSum(); //obtain EtHFtowerSum from object as centrality value //EBA this is HI HF


  // Processing pixels
  /*edm::Handle<SiPixelRecHitCollection> pixelCollection;
  iEvent.getByToken(pixelToken, pixelCollection);    

  nPixel = pixelCollection->size();
  */
  // Processing HLT results
  
  //HLTConfigProvider const&  hltCfg = hltPrescaleProvider.hltConfigProvider();

  edm::Handle<edm::TriggerResults> hltresults;
  iEvent.getByToken(hltToken,hltresults);
  edm::TriggerNames const& triggerNames = iEvent.triggerNames(*hltresults);

  int ntrigs = hltresults->size();

  if(firstEvent){
    for(int itrig = 0; itrig != ntrigs; ++itrig) {
      TString trigName = triggerNames.triggerName(itrig);
      zdcDigiTree->Branch(trigName+"_acc", trigflag+itrig, trigName+"_acc/I");
      zdcDigiTree->Branch(trigName+"_psc", prscflag+itrig, trigName+"_psc/I");
    }
    firstEvent = false;
  }

  for(int itrig = 0; itrig != ntrigs; ++itrig){
    trigflag[itrig] = (hltresults->accept(itrig)) ? 1 : 0;
  //  prscflag[itrig] = (hltCfg.moduleType(hltCfg.moduleLabel(itrig,hltresults->index(itrig)))=="HLTPrescaler") ? 1 : 0;
      //if(!prscflag[n])
      //  save = true;+;
  }

  // Fill event tree
  if(valid)
    zdcDigiTree->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void OnlyZDCandCentralityAnalyzer::beginJob(){
  zdcDigiTree = fs->make<TTree>("zdcdigi","v1");
  
  zdcDigiTree->Branch("run",&run,"run/I");
  zdcDigiTree->Branch("lumi",&lumi,"lumi/I");
  zdcDigiTree->Branch("event",&event,"event/I");

  zdcDigiTree->Branch("Cent",&centval,"cent/D"); //EBA //this is acutally hf tower hits which a table is needed to convert to centrality

  zdcDigiTree->Branch("n",&n,"n/I");
  zdcDigiTree->Branch("zside",zside,"zside[n]/I");
  zdcDigiTree->Branch("section",section,"section[n]/I");
  zdcDigiTree->Branch("channel",channel,"channel[n]/I");

  zdcDigiTree->Branch("rejected",rejected,"rejected[n]/I"); 


  firstEvent = true;

  const int Max = 500;
  trigflag = new int[Max];
  prscflag = new int[Max];
}

// ------------ method called once each job just after ending the event loop  ------------
void OnlyZDCandCentralityAnalyzer::endJob(){
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
OnlyZDCandCentralityAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}


//define this as a plug-in
DEFINE_FWK_MODULE(OnlyZDCandCentralityAnalyzer);

