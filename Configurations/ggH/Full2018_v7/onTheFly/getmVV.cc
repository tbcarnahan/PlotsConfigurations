#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TMath.h"
#include <vector>
#include "TLorentzVector.h"

class getmVV : public multidraw::TTreeFunction {
public:
  getmVV();

  char const* getName() const override { return "getmVV"; }
  TTreeFunction* clone() const override { return new getmVV(); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  UIntValueReader* nGenPart;
  FloatArrayReader* GenPart_pt;
  FloatArrayReader* GenPart_eta;
  FloatArrayReader* GenPart_phi;
  FloatArrayReader* GenPart_mass;
  IntArrayReader* GenPart_pdgId;

};

getmVV::getmVV() :
  TTreeFunction()
{
}

//look for 2 Ws; add 2 LorentzVectors and get the mass .m()


double
getmVV::evaluate(unsigned)
{
  unsigned nGen{*nGenPart->Get()};
  int pdgId;
  int Wplus_idx=-9999;
  int Wminus_idx=-9999;

  for (unsigned iGen{0}; iGen != nGen; ++iGen){ //1st particle iterates from 0 to nGen end
    pdgId = GenPart_pdgId->At(iGen);
    if (pdgId == 24){
      Wplus_idx = iGen;}
    else if (pdgId == -24){
      Wminus_idx = iGen;}
    
    if(Wplus_idx>0 && Wminus_idx>0){
      break;
    }
  }
  
  if(Wplus_idx < 0 || Wminus_idx < 0){
    std::cout << "HOLAAAAA" << std::endl;
  }
  TLorentzVector *tw1 = new TLorentzVector();
  TLorentzVector *tw2 = new TLorentzVector();
  
  tw1->SetPtEtaPhiM(GenPart_pt->At(Wplus_idx), GenPart_eta->At(Wplus_idx), GenPart_phi->At(Wplus_idx), GenPart_mass->At(Wplus_idx));
  tw2->SetPtEtaPhiM(GenPart_pt->At(Wminus_idx), GenPart_eta->At(Wminus_idx), GenPart_phi->At(Wminus_idx), GenPart_mass->At(Wminus_idx));
  
  return (*tw1+*tw2).M();
}

void
getmVV::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nGenPart, "nGenPart");
  _library.bindBranch(GenPart_pt, "GenPart_pt");
  _library.bindBranch(GenPart_eta, "GenPart_eta");
  _library.bindBranch(GenPart_phi, "GenPart_phi");
  _library.bindBranch(GenPart_mass, "GenPart_mass");
  _library.bindBranch(GenPart_pdgId, "GenPart_pdgId");
}
