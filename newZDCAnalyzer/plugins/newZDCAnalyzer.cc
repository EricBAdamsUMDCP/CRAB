// -*- C++ -*-
//
// Package:    ZDC/newZDCAnalyzer
// Class:      newZDCAnalyzer
//
/**\class newZDCAnalyzer newZDCAnalyzer.cc ZDC/newZDCAnalyzer/plugins/newZDCAnalyzer.cc

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

class newZDCAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
  public:
    explicit newZDCAnalyzer(const edm::ParameterSet&);
    ~newZDCAnalyzer();

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
    int nPixel = 0;
    int nTrack = 0;
    const int primaryvtx = 0;
    int nRejectedTracks = 0;
    int nAcceptedTracks = 0;
    int nHF_pos = 0, nHF_neg = 0;
    float eHF_pos = 0, eHF_neg = 0;
    double vtx = 0;
    double xvtx = 0;
    double yvtx = 0;
    //double xvtxError = 0;
   // double yvtxError = 0;

    bool firstEvent;
    int* trigflag;
    int* prscflag;
    //HLTPrescaleProvider hltPrescaleProvider;

    std::vector<double>* phi;
    std::vector<double>* phiError;
    std::vector<double>* eta;
    std::vector<double>* etaError;
    std::vector<double>* Pt;
    std::vector<double>* ptError;
    std::vector<double>* chi2;

    std::vector<double>* HFPos_Phi;
    std::vector<double>* HFPos_Eta;
    std::vector<double>* HFPos_Energy;
    std::vector<double>* HFPos_Et;
    std::vector<double>* HFNeg_Phi;
    std::vector<double>* HFNeg_Eta;
    std::vector<double>* HFNeg_Energy;
    std::vector<double>* HFNeg_Et;



};

newZDCAnalyzer::newZDCAnalyzer(const edm::ParameterSet& iConfig) /*:
  hltPrescaleProvider(iConfig, consumesCollector(), *this)*/{

  usesResource("TFileService");
  zdcToken = consumes<QIE10DigiCollection>(iConfig.getParameter<edm::InputTag>("zdc")); //creates token that uses resource "zdc" from input parameter(?)
  caloTowerToken = consumes<CaloTowerCollection>(iConfig.getParameter<edm::InputTag>("tower"));
  hltToken = consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("hltresults"));
  trgResultsProcess_ = iConfig.getParameter<edm::InputTag>("hltresults").process();
  //hltCfg = hltPrescaleProvider_.hltConfigProvider(iConfig, consumesCollector(), *this);

  trackToken = consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("track"));
  //pixelToken = consumes<SiPixelRecHitCollection>(iConfig.getParameter<edm::InputTag>("pixel"));
  centralityTag_ = iConfig.getParameter<edm::InputTag>("centralityTag_"); //EBA got config
  centralityToken = consumes<reco::Centrality>(centralityTag_); //EBA obtain token for centrality info referenced in config file

  vertexTag_  = iConfig.getParameter<edm::InputTag>("vertexTag_"); //eba added for track based cuts
  vertexToken = consumes<std::vector<reco::Vertex>>(vertexTag_);


  phi = nullptr;
  phiError = nullptr;
  eta = nullptr;
  etaError = nullptr;
  Pt = nullptr;
  ptError = nullptr;
  chi2 = nullptr;

  HFPos_Phi = nullptr;
  HFPos_Eta = nullptr;
  HFPos_Energy = nullptr;
  HFPos_Et = nullptr;
  HFNeg_Phi = nullptr;
  HFNeg_Eta = nullptr;
  HFNeg_Energy = nullptr;
  HFNeg_Et = nullptr;
}



newZDCAnalyzer::~newZDCAnalyzer(){
}


//
// member functions
//

// ------------ method called for each event  ------------
void newZDCAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){

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

  nHF_pos = 0;
  nHF_neg = 0;
  
  eHF_pos = 0.0;
  eHF_neg = 0.0;

  // delete HFPos_Phi   ; HFPos_Phi    = new std::vector<double>();
  // delete HFPos_Eta   ; HFPos_Eta    = new std::vector<double>();
  // delete HFPos_Energy; HFPos_Energy = new std::vector<double>();
  // delete HFNeg_Phi   ; HFNeg_Phi    = new std::vector<double>();
  // delete HFNeg_Eta   ; HFNeg_Eta    = new std::vector<double>();
  // delete HFNeg_Energy; HFNeg_Energy = new std::vector<double>();
  HFPos_Phi->clear();
  HFPos_Eta->clear();
  HFPos_Energy->clear();
   HFPos_Et->clear();
  HFNeg_Phi->clear();
  HFNeg_Eta->clear();
  HFNeg_Energy->clear();
  HFNeg_Et->clear();

  for(auto it = towerCollection->begin(); it != towerCollection->end(); it++){
    bool isHF = false;
    for(unsigned int i = 0; i < it->constituentsSize(); i++){
      DetId cell = it->constituent(i);
      if(cell.det() == DetId::Hcal && (HcalSubdetector)cell.subdetId() == HcalForward)
        isHF = true;
    }

    if(isHF && it->energy() > 4.0){
      if(it->eta() > 0){
        nHF_pos++;
        eHF_pos += it->energy();
        HFPos_Phi->push_back(it->phi());
        HFPos_Eta->push_back(it->eta());
        HFPos_Energy->push_back(it->energy());
        HFPos_Et->push_back(it->et());
      }
      else {
        nHF_neg++;
        eHF_neg += it->energy();
        HFNeg_Phi->push_back(it->phi());
        HFNeg_Eta->push_back(it->eta());
        HFNeg_Energy->push_back(it->energy());
        HFNeg_Et->push_back(it->et());
      }
    }
  }

//vertex checking
  //may need to move handle

  iEvent.getByToken(vertexToken,vertex_);
  reco::VertexCollection recoVertices = *vertex_;
  sort(recoVertices.begin(), recoVertices.end(), [](const reco::Vertex &a, const reco::Vertex &b){
  return a.tracksSize() > b.tracksSize();
  });
  vtx = recoVertices[primaryvtx].z(); //may need to add reco::
  xvtx = recoVertices[primaryvtx].x();
  yvtx = recoVertices[primaryvtx].y();
  //hvtxRaw->Fill(vtx);

  bool vertex_good = true;
  if (fabs(vtx) < -15. || fabs(vtx) > 15.) {
    vertex_good = false;
  } 

   nRejectedTracks = 0;
   nAcceptedTracks = 0;
  // Processing tracks
  if (vertex_good){
    edm::Handle<reco::TrackCollection> trackCollection;
    iEvent.getByToken(trackToken, trackCollection);

    nTrack = trackCollection->size();

    //// extract phi, eta, and Pt values from tracks ////
    //clear track vectors
    delete phi; phi = new std::vector<double>();
    delete phiError; phiError = new std::vector<double>();
    delete eta; eta = new std::vector<double>();
    delete etaError; etaError = new std::vector<double>();
    delete Pt; Pt = new std::vector<double>();
    delete ptError; ptError = new std::vector<double>();
    delete chi2; chi2 = new std::vector<double>();


    for (reco::TrackCollection::const_iterator track_iter = trackCollection->begin(); //dereferencing edm::Handles (using * or ->) gets object that handle refers to
                            track_iter != trackCollection->end(); ++track_iter) {
  //subtract bad track values from ntrack to get acceptedntrack


//  QUESTIONS ABOUT THE NOT STAEMENT DOUBLE CHECK THAT
      if ( ! TrackQuality_HIReco(track_iter, recoVertices) ){
      //nRejectedTracks++;
      continue;
      }
      // checks to make sure tracks a koality
        // needs work still to make sure function work
        nAcceptedTracks += 1;

        phi->push_back(track_iter->phi());
        phiError->push_back(track_iter->phiError());
        eta->push_back(track_iter->eta());
        etaError->push_back(track_iter->etaError());
        Pt->push_back(track_iter->pt());
        ptError->push_back(track_iter->ptError());

        //AD ERROR IN PH IETA AND PT?
        chi2->push_back(track_iter->chi2());
    }
  } //extraneous brakcet?

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
void newZDCAnalyzer::beginJob(){
  HFPos_Phi     = new std::vector<double>;
  HFPos_Eta     = new std::vector<double>;
  HFPos_Energy  = new std::vector<double>;
  HFPos_Et  = new std::vector<double>;
  HFNeg_Phi     = new std::vector<double>;
  HFNeg_Eta     = new std::vector<double>;
  HFNeg_Energy  = new std::vector<double>;
  HFNeg_Et  = new std::vector<double>;


  zdcDigiTree = fs->make<TTree>("zdcdigi","v1");
  
  zdcDigiTree->Branch("run",&run,"run/I");
  zdcDigiTree->Branch("lumi",&lumi,"lumi/I");
  zdcDigiTree->Branch("event",&event,"event/I");
  zdcDigiTree->Branch("bxid",&bxid,"bxid/I");

  zdcDigiTree->Branch("Cent",&centval,"cent/D"); //EBA //this is acutally hf tower hits which a table is needed to convert to centrality

  zdcDigiTree->Branch("n",&n,"n/I");
  zdcDigiTree->Branch("zside",zside,"zside[n]/I");
  zdcDigiTree->Branch("section",section,"section[n]/I");
  zdcDigiTree->Branch("channel",channel,"channel[n]/I");

  zdcDigiTree->Branch("rejected",rejected,"rejected[n]/I"); 

  zdcDigiTree->Branch("nHF_pos",&nHF_pos,"nHF_pos/I");
  zdcDigiTree->Branch("nHF_neg",&nHF_neg,"nHF_neg/I");

  zdcDigiTree->Branch("eHF_pos",&eHF_pos,"eHF_pos/F");
  zdcDigiTree->Branch("eHF_neg",&eHF_neg,"eHF_neg/F");

  zdcDigiTree->Branch("vtx",&vtx,"vtx/D");
  zdcDigiTree->Branch("xvtx", &xvtx, "xvtx/D");
  zdcDigiTree->Branch("yvtx", &yvtx, "yvtx/D");

  zdcDigiTree->Branch("nTrack",&nTrack,"nTrack/I");
  zdcDigiTree->Branch("nAcceptedTracks",&nAcceptedTracks,"nAcceptedTracks/I"); //allows for iteration over tracks due to some track rejection

  zdcDigiTree->Branch("nPixel",&nPixel,"nPixel/I");

  //branches with phi eta and Pt values
  zdcDigiTree->Branch("phi", "std::vector<double>", &phi);
  zdcDigiTree->Branch("phiError", "std::vector<double>", &phiError);
  zdcDigiTree->Branch("eta", "std::vector<double>", &eta);
  zdcDigiTree->Branch("etaError", "std::vector<double>", &etaError);
  zdcDigiTree->Branch("Pt",  "std::vector<double>", &Pt);
  zdcDigiTree->Branch("ptError",  "std::vector<double>", &ptError);
  zdcDigiTree->Branch("chi2", "std::vector<double>", &chi2);

  zdcDigiTree->Branch("HFPos_Phi", "std::vector<double>", &HFPos_Phi);
  zdcDigiTree->Branch("HFPos_Eta", "std::vector<double>", &HFPos_Eta);
  zdcDigiTree->Branch("HFPos_Energy", "std::vector<double>", &HFPos_Energy);
  zdcDigiTree->Branch("HFPos_Et", "std::vector<double>", &HFPos_Et);
  zdcDigiTree->Branch("HFNeg_Phi", "std::vector<double>", &HFNeg_Phi);
  zdcDigiTree->Branch("HFNeg_Eta", "std::vector<double>", &HFNeg_Eta);
  zdcDigiTree->Branch("HFNeg_Energy", "std::vector<double>", &HFNeg_Energy);
  zdcDigiTree->Branch("HFNeg_Et", "std::vector<double>", &HFNeg_Et);


  firstEvent = true;

  const int Max = 500;
  trigflag = new int[Max];
  prscflag = new int[Max];
}

// ------------ method called once each job just after ending the event loop  ------------
void newZDCAnalyzer::endJob() {
  delete HFPos_Phi;
  delete HFPos_Eta;
  delete HFPos_Energy;
  delete HFPos_Et;
  delete HFNeg_Phi;
  delete HFNeg_Eta;
  delete HFNeg_Energy;
  delete HFNeg_Et;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
newZDCAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
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

///
bool //note this is likely missing a header or 2 but they are in vn analyzer
newZDCAnalyzer::TrackQuality_HIReco(const reco::TrackCollection::const_iterator& itTrack, const reco::VertexCollection& recoVertices)
{                                                                                           // may add back in const 
  if ( itTrack->charge() == 0 ) return false;
  if ( !itTrack->quality(reco::TrackBase::highPurity) ) return false;
  if ( itTrack->numberOfValidHits() < 11 ) return false;
  if ( itTrack->normalizedChi2() / itTrack->hitPattern().trackerLayersWithMeasurement() > 0.18 ) {
    return false;
  }
  if ( itTrack->ptError()/itTrack->pt() > 0.1 ) { //max pt error set to 10 %. may want to change to be more aggressive, jaimes number is 0.01
    return false;
  }
  if (
      itTrack->originalAlgo() != 4 and
      itTrack->originalAlgo() != 5 and
      itTrack->originalAlgo() != 6 and
      itTrack->originalAlgo() != 7
      ) {
    return false;
  }
  
  math::XYZPoint v1( recoVertices[primaryvtx].position().x(), recoVertices[primaryvtx].position().y(), recoVertices[primaryvtx].position().z() );
  double vxError = recoVertices[primaryvtx].xError();
  double vyError = recoVertices[primaryvtx].yError();
  double vzError = recoVertices[primaryvtx].zError();
  double d0 = -1.* itTrack->dxy(v1);
  double derror=sqrt(itTrack->dxyError()*itTrack->dxyError()+vxError*vyError);
  if ( fabs( d0/derror ) > 3.0 ) { // max d0d0 error set to 3.0
    return false;
  }
  
  double dz=itTrack->dz(v1);
  double dzerror=sqrt(itTrack->dzError()*itTrack->dzError()+vzError*vzError);
  if ( fabs( dz/dzerror ) > 3.0 ) { // max dzdz error is set to 3.0
    return false;
  }
  return true;
}

//define this as a plug-in
DEFINE_FWK_MODULE(newZDCAnalyzer);

