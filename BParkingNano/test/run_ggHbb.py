from FWCore.ParameterSet.VarParsing import VarParsing
import FWCore.ParameterSet.Config as cms

options = VarParsing('python')

options.register('isMC', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register('globalTag', 'NOTSET',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Set global tag"
)
options.register('wantSummary', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register('wantFullRECO', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register('reportEvery', 100,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "report every N events"
)
options.register('skip', 0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "skip first N events"
)

#options.setDefault('maxEvents', 100)       # number of events analyzed. then consider the trigger
options.setDefault('tag', '10215')
options.parseArguments()

globaltag = '102X_dataRun2_v11' if not options.isMC else '102X_upgrade2018_realistic_v15'
if options._beenSet['globalTag']:
    globaltag = options.globalTag

extension = {False : 'data', True : 'mc'}
outputFileNANO = cms.untracked.string('_'.join(['BParkNANO', extension[options.isMC], options.tag])+'.root')
outputFileFEVT = cms.untracked.string('_'.join(['BParkFullEvt', extension[options.isMC], options.tag])+'.root')
if not options.inputFiles:
    options.inputFiles = [
        '/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CFBFCA29-1649-2345-970E-731824064446.root'] if not options.isMC else [
        '/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/D2130569-D2C7-5642-9546-91AF74A3BB6C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/2E326906-498E-C344-AD43-CE29FB1CD428.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/BF719C38-8173-F94D-99CD-CE874760B2CC.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/F97BE2F8-BE47-BF4B-B6EE-FA98E33A251E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/505783F7-118A-144B-A472-8908A01EA6C3.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/E60966AA-4CA6-BA47-B146-313B835DC581.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/C085EF51-712F-0941-AA09-B03D863B9F16.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/A5EAD7C3-840F-9C4A-870D-3815D0A7CD60.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/7177D333-BB46-B847-90DC-85A9E33A01FA.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/5761B066-9396-4046-AD23-06D0B72B147A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/26E84B48-9992-CF4D-8B24-2DD5BA9303E2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/A47841D5-8181-394A-B047-3A58B4657209.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/CCF83D8F-5A54-704A-8FBF-FF00D159C618.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/39CB433B-2703-9346-A5C9-8A5926B55E1B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/44E2C5AD-AEB3-A54C-B926-38A6726E21E3.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/3251C937-1158-0942-AA4D-B7B06254FC39.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/900636AF-18D6-1148-AEAA-B40562957AC0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/0C42D2E5-C723-A549-ADC9-7E893C839B63.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/52AEFA74-623B-D144-ACD2-C5C2AF2D9A26.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/558D6977-C0CD-754D-B0CB-5ECB8342C63B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/77CB2920-001C-104F-91D7-43A075444EF7.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/277FB287-077F-D047-B7A8-F76562E21F10.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/753CA424-E754-9545-B0EA-6FC1F1C9642A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/30C79E01-39DC-6D42-A1A1-60FBCEF44C3C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/877F64B7-B269-0F44-A77E-DA2790DFB74F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/1789BFCA-AD00-394C-8758-870F07B3978B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/E08ED8F1-BF51-2E4D-911F-2304C2EE7F18.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/6AE97364-4CA4-9B4D-9A45-FDFAF0754A2B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/4B7903E9-0CA0-B243-8E80-C9B042A3E2BC.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/7DC98F59-F4A7-EA4F-98B7-FF198D21286F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/46F45C25-B8A4-DB41-8547-9DA7B6DEE658.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/4DE630F9-0513-9E4F-817E-67B7E4F6C557.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/086F1202-3FE2-CB41-82D1-E62CC3CAB01D.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/F46121CE-F64B-9C47-9F06-68DC9D00A8C0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/178F88CB-B2C2-5348-8679-405A540AB014.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1FC1F6B4-D1C8-5841-85FF-F38322A60EBE.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/D862482D-1F05-704E-99E8-5CC007C1692F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/193E9FFC-9CB3-0A43-B02C-B7D17E9B7AA9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4F53C355-7BD2-FD48-9A2C-E11B89CCE371.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/ACA01AFB-2F9B-F749-9EC3-72D934EE4EF0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/86ECB7B8-3FCE-224E-8008-FE1768818175.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/A76B74CE-689C-304F-9F7F-1BFCC01188B9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/96793AB7-6AF8-4748-9D25-367167850AB8.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/FAC3DDBD-8B25-0444-9C32-6B3FCCDCA1AD.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/240DD4F4-8B3A-F646-B31B-D05E4461F3B2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E997964B-5DF8-1D41-B9FE-F70B971852D7.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4E4F1D4B-3EE7-024A-85BC-84757CDCD052.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/D8E400E4-D929-864A-A1C6-A013E321E6D7.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/5BCC17B5-EBE5-0544-8810-60B94A21EFF3.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/7C85F87F-EB52-BB47-912C-66930056A27A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/60E0E707-444F-D74F-BD21-8313985ECCEA.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/839CE06D-ADE7-484A-A5B7-60072A31553D.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/BE816FAE-7508-6F43-9E35-0AB33F9D423F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/34C696A8-9A78-2C41-A4B8-AFCFDBA49A37.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4C9505C5-566A-C34E-A81C-4A66015E2BC4.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E52580D2-DD61-CE4F-9AB5-130595A48BF7.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/B564DA23-FF7A-5D40-BD05-6B5008D8AD19.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/C6C230ED-E12E-2A4C-B7F8-95669ABE3E40.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/68776BF7-498A-1B49-B43D-D9D954AD231A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/50BC7DB3-DD0C-8643-A10B-8A35FD65A75A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1297A42D-AAE4-8A42-8EEB-F3AB607E052C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/5D1B9C29-B9CC-0B47-817D-04995E682EAE.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4F320E7B-3917-4F4A-8F8F-8B8B8B640B91.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8F3845A7-CFDF-4D4D-9CE1-5D52631D849B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/6B67F856-7822-3444-9EBE-BA02988C19D2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/0BAB1DE5-13FE-3147-8C5E-3EC1B11610CE.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/817E7067-1CF0-224C-AED9-7493C6F64C57.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/89188072-295A-3D4D-9B14-9AE9CA7A8043.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1DA268B7-8941-1D48-B0DF-631DDE9338AF.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4B999DE8-3B9D-ED41-8121-3E15802DFEA3.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/56C44507-1012-EB46-A4DF-F36F98FE99DE.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E86FDCAC-E220-B94B-A86E-012E36A359F9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/021E5942-BF06-774F-A293-B274DA69048C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/44D9525E-9E15-0843-B9D9-9DE4DFD16BCB.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/54497406-437B-3742-B4D1-66A6ED93DD86.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/52402C42-0BF0-1347-9564-9FA7C6D1F5B1.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/A6075911-6F5E-BB4E-8EBB-018AC613C1CA.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/07EF9182-6A13-C145-845D-6E9E9724F2C2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/41C76791-A5B3-0944-B44E-AEF70CC02DBA.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1DDFE87C-B7FB-854C-9602-B5DF1AA09E14.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/406B54AD-EF54-C14E-B009-F6F2B867FEDF.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/CC45B38C-89C8-5A47-8ADF-8B215349E3B3.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/FFE86DD1-DCEF-1643-89DE-7757B6F53D49.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/35A08F24-BC20-0142-8205-E6ED0FEBE371.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/B431261F-804A-CD4E-89A0-FA95D95DAF1D.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/80FD62F6-86E5-A04E-A58A-738DD0641A5D.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/3504A2A1-6D08-C948-987B-E1167984D2C9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/9F6C4258-8CA9-A247-B5A2-402959AEDB02.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/2B3503F7-717E-F744-ADA1-77C728DE13F3.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/B0A0992D-CC5E-4D40-AF8D-72111C3D8303.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E984E86F-C4D9-B041-BB30-90F1F22AFE9B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/900DCC32-147D-DA4A-8905-41CA4C398965.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/72AED8B4-2C2E-F943-90AC-C19D59964BE5.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E552627E-6E46-D347-B155-2678B0F3E683.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/F5335412-BCDC-5B42-80D0-7CEC8D6D8C30.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/93449438-EEFC-E443-83D7-70AA00230AA7.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/D4602F10-F0DA-DF4B-9E4C-15CD8C5DA4A2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/CB57D1F6-0941-4343-8519-181FE919F6F3.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/DA2107C4-9537-0B49-BDD4-D3C71D21E1C5.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8AD65440-EE39-CE4D-9A49-F383F6535234.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/DE5A287E-FDCF-324D-96E7-1AF79559A43A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/61264BD0-83FC-2348-9922-761777C37722.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8131463F-CDBF-A049-8859-54DE941AAB15.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1CA15E9E-64F8-8645-B9F6-8879A21064E4.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/391CEA03-B069-EF42-AC89-31568C60E996.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1397F4D0-9CBA-6240-B7BC-31D64CBABD4A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/6B99272F-F8CA-054A-9E65-C640317764B9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/DC3BFA0D-B284-EB4F-B604-997F08F00797.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/3245CA23-8110-0E45-9CBD-F2F1223A0C11.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1119491A-7384-6645-AC1F-A72EE1AB866C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/BA367F5A-EC12-8348-A8B5-66EC0EA6B3A0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/0E849C6E-66B5-9246-B05E-D343A7556EE6.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/61107132-437B-E14E-8684-CDADF452C10A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/9CCB9F8B-731F-4D4C-9268-A9A3E6E35AB9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/73C61A88-C18C-A342-B6B7-6A0D69F0CE16.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/BE26F45E-3ACE-CC48-B155-74E60F5A8B10.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/BEE6C03A-8360-BD45-B81A-7F88ED8F01DD.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/A5676C46-9A75-0C4F-ADF3-A11442731EF1.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/3A5BB3E7-B3F8-7344-BE9D-552FBDAA6B52.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1A738F3C-87D1-1948-9800-1A8314A6B818.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/F7641FA0-58B7-034A-B908-B7DAF46FCABB.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8E2FDC9B-3296-1148-9D9F-EBAB304C77B8.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/DF62FC9D-AE71-DF4B-A593-D3DE52F34B02.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4FF78903-596D-B843-9879-9F983BEBE406.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/F23C3733-F3A0-6E43-A077-A01C5D717360.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/EA5D1454-9CCB-E440-8462-785F8ACBAD56.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/9B3BB1C7-8B36-F64A-B35D-83BBB41EC46C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/72456350-9490-2847-B246-1D2AAB0BC4A2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/C2BB2A2E-C3E3-F448-A810-407EDCAB5EED.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/D764E278-F775-DB4B-9646-F616E7E0C6AB.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/FDCFD14F-88D7-A94B-9178-FF0FA81E2F84.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/B902EDEC-3906-7E41-8044-75CB1219E01B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/ED52E4A5-F236-BD48-BEEE-48B52BEC997C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/26AAB8CC-1706-694C-A7FF-FA8DC1036656.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/F4473017-0805-3A45-80D0-D7D69233D26E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/FEDF11B1-4204-3143-B0D2-71D95DB0FCF2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4D097880-6BBD-2E48-BD35-EDDE451DD418.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/13F1CD86-0E92-0342-A2FC-3F07DEB6F52C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/0BAF78A8-0E10-4C4C-8FA7-BF2091D2FAFD.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/ADD6C691-B4FF-1246-BAFC-6C6108F0A396.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/6E2AD6C0-8F74-6840-9545-1513F251703B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1613F16D-91A9-E140-9D4B-2E874FE65D29.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/C3A6FADC-EFA6-DD49-8CD2-4F90F0E14261.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1372726E-DE59-AC4E-AD19-2244BA1CB921.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/601741F2-25DE-B248-8DEB-AA9FE1D42014.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/EE7B49C1-C6CA-F949-B6EC-DB3F646137C9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/7A86E271-DBF3-8947-96CB-C8E587E1361A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/DE1C2F35-CD2E-3B41-99F5-42F27199077D.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4B8EED58-9BB3-6B45-9EB9-96FAB2B85145.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/C8B3FDC8-032E-894D-B1BE-518F880B7B93.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/17059F6C-A0B1-C04B-B827-A52A664828FC.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/3AF9EE2B-11A7-134D-8E1A-9ECF5CB55804.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/A7B03035-3472-D049-BF59-3DB108887315.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/DE8986ED-BC4C-E64C-8C7C-AD5DCAD4C7AD.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/98E6D6F1-7EDF-4144-B73C-F707B1400D69.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/033A6F99-742F-D847-AC14-56547C90BD58.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/3D81D45C-1C5A-EC42-BDF8-BE81D9914F8F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/63D209AF-FCB8-1A42-BFFD-10654CB4BFCF.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/58FA2FCD-2B17-8641-8D71-824D65805055.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/02DB4B12-DBAB-4745-8506-6187711F747F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/DF9A6FEC-0153-F344-8033-00328FEAF77C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/A4F84DDD-7C02-DE46-B4E8-69573505A4FC.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/179433E8-A1B8-1249-9BDE-FE46E356CA82.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/B384809B-68AC-6D46-B778-C5023953DED1.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/BFEC695A-37F7-A74A-AC1D-08276ED5C9CA.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/BCD146B4-D9E7-2347-949B-023C8C47BDFA.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/F6232C53-F0A5-9446-B7DB-0B831F811B38.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E1D4F294-707A-844B-B015-233BB0558B0D.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/1E29BDCB-5EDA-9B48-9093-FB53DDF19430.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/45F08D98-9FF5-C64A-9545-2587A6FD8D3D.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8C078A6A-2BE2-2E4C-BF39-FF4AC115630F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8E37058C-07B2-5C4C-8ECE-DE33E07CBCA9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/D6838B28-8A17-3645-A71A-116F751D7ECC.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/B4F45D65-00DC-A64C-9D52-0AFADD7C2A5E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/FD99C1B6-C43B-4A4A-A8E7-5540068BFEC9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E9A5C04B-9988-0242-9813-9D0820D36929.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/BB0EAAD9-79EE-AA4C-9EF9-61195627278F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/EEE77C52-1C8F-6440-83D8-9D4E9DAA5C2E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/B492265A-FA25-A04F-B927-1B73A4365829.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/5B7FB518-7688-E541-85B4-301B1DC4C42A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/4827311F-5084-3A4B-90BC-63FDCBBDC325.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/5237163E-283D-0D43-AF45-CEF87FBC191F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/90EAA4DE-7725-124D-9871-4261B18BB20B.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/E0F1FA4A-2FB1-1448-B3AC-401426F82964.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/510000/EF274444-D6B0-3649-85A7-10FE4B35F807.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/1049CD6E-48EC-184D-800F-E3717967309E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/93A22A90-0EEF-FA47-8E63-889EDD710D6E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/5E7EEC19-601A-F846-92A9-FEA7D16D836C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/1A4CBF03-EAE4-184B-9D4D-0D28063CBB72.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/C52815B7-8351-2A41-B67C-0896CB86EACC.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/7A462BDD-9DD4-AB42-A315-80900810A6BA.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/AB9F3E42-FB60-C949-AF27-1775D3492C6C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/62355395-300C-284C-82A1-7371DF202B07.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/3A9DDC29-34CC-664F-BCF6-3E9896C47636.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/4AA94810-0CB1-C34B-BFC6-8D440CB9B91E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/35984233-2135-CE41-9E81-9481320C0D1E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/BC083012-650C-3B4B-A77A-C0DF2B08F846.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/8E9CAA9D-0BD5-0048-A564-86BD7E2182CB.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/B3731FAE-8DC7-2947-9F33-7DC24A4091B0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/DBE9E9D5-3315-9B43-83A8-603212ADB877.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/C9347CFF-2238-B245-B7CC-EED9CDE87CC5.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/F85D24EA-AC84-5349-B16C-3BCBD11082C8.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/F3DF71C2-3715-EC42-BB1F-74DB9862530A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/485E3DFE-5A91-574C-B5D6-ECB183464EB0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/7EC47DB8-CFBF-3E43-9D10-D244C8F80047.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/E674CA1C-69B7-E44A-BE6C-89EEE9E06385.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/ABC20F7F-AAA1-2F48-BDF1-5209D989BAF0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/784E3EBA-7033-4B4C-BE19-7381E455D18C.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/C59917B6-3D38-7449-8ECB-853B12705D21.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/AAB41D6E-6412-D649-8125-1CA6AB332F94.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/6A7DB3FD-AEC5-9742-90FA-935BA63D9B7A.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/2D51AD80-92EA-E946-A171-3B3C206AE062.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/7C784F1C-B4F8-0E4D-9694-956BC2A36E73.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/F0A09D31-B1D8-E84C-86B0-B4E0AF68279F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/FB593B88-72D5-CF44-B56F-4EB6FACC7941.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/ACA806E4-D66F-814C-949C-E020CA14D9D2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/F55735C3-C76C-9D43-B2CD-100D768A729E.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/FD1C3588-D033-AE4A-8883-940515C86CD0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/03A03D7E-E8AC-EF4D-BB9E-3FEA471409EA.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/F1330C02-276E-9141-BF4C-2686EFA19319.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/8796429F-008D-4E44-93CE-BD0D1A124227.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/6F604D2D-6800-CD4E-B7DD-BC9D401C11E7.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/695AE7E6-AD45-EE46-BD10-6CA43C3146DB.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/23B810B9-E831-434F-B38E-D94ADEC10FE2.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/6DE4EA53-01FF-CF4A-B725-AE228AED2FF9.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/D4546B83-4A3B-E140-BF8D-DDD4AB5BB876.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/F9070CD2-58D7-9A44-B370-36C495666FC3.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/41CC3D36-46C5-7B41-B3C9-1F89CF357AC6.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/F70252EC-9D72-EC42-9E80-A718D8297D15.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/9A49DB88-0517-1141-A51C-9CA2544E2919.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/915B561D-0168-E444-965C-E69B433855D0.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/D0CC19B5-62B9-C04B-B375-8DBFFA889B0F.root',
        #'/store/mc/RunIISummer20UL16MiniAODv2/HHHTo4B2G_c3_0_d4_0_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/04EDCC0D-D279-0842-A26B-E7E0CC47AA22.root'
    ]#['/store/mc/RunIIAutumn18NanoAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/NANOAODSIM/102X_upgrade2018_realistic_v15-v1/90000/D6407856-BDE7-C341-B778-0406CA4A2136.root']
annotation = '%s nevts:%d' % (outputFileNANO, options.maxEvents)
#'/store/data/Run2018B/ParkingBPH4/MINIAOD/05May2019-v2/230000/6B5A24B1-0E6E-504B-8331-BD899EB60110.root']

from Configuration.StandardSequences.Eras import eras
process = cms.Process('BParkNANO',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('PhysicsTools.BParkingNano.nanoBPark_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring(),
    skipEvents=cms.untracked.uint32(options.skip),
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(options.wantSummary),
)

process.nanoMetadata.strings.tag = annotation
# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string(annotation),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = outputFileFEVT,
    outputCommands = (cms.untracked.vstring('keep *',
                                            'drop *_*_SelectedTransient*_*',
                     )),
    splitLevel = cms.untracked.int32(0)
)

process.NANOAODoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = outputFileNANO,
    outputCommands = cms.untracked.vstring(
      'drop *',
      "keep nanoaodFlatTable_*Table_*_*",     # event data
      "keep nanoaodUniqueString_nanoMetadata_*_*",   # basic metadata
    )

)


# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, globaltag, '')
# this is for the LowPt energy regression
process.GlobalTag.toGet = cms.VPSet(
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_eb_ecalOnly_05To20_mean"),
         tag = cms.string("lowPtElectron_eb_ecalOnly_05To20_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_ee_ecalOnly_05To20_mean"),
         tag = cms.string("lowPtElectron_ee_ecalOnly_05To20_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_eb_ecalOnly_05To20_sigma"),
         tag = cms.string("lowPtElectron_eb_ecalOnly_05To20_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_ee_ecalOnly_05To20_sigma"),
         tag = cms.string("lowPtElectron_ee_ecalOnly_05To20_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_eb_ecalTrk_05To20_mean"),
         tag = cms.string("lowPtElectron_eb_ecalTrk_05To20_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_ee_ecalTrk_05To20_mean"),
         tag = cms.string("lowPtElectron_ee_ecalTrk_05To20_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_eb_ecalTrk_05To20_sigma"),
         tag = cms.string("lowPtElectron_eb_ecalTrk_05To20_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_ee_ecalTrk_05To20_sigma"),
         tag = cms.string("lowPtElectron_ee_ecalTrk_05To20_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_eb_ecalOnly_20To50_mean"),
         tag = cms.string("lowPtElectron_eb_ecalOnly_20To50_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_ee_ecalOnly_20To50_mean"),
         tag = cms.string("lowPtElectron_ee_ecalOnly_20To50_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_eb_ecalOnly_20To50_sigma"),
         tag = cms.string("lowPtElectron_eb_ecalOnly_20To50_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_ee_ecalOnly_20To50_sigma"),
         tag = cms.string("lowPtElectron_ee_ecalOnly_20To50_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_eb_ecalTrk_20To50_mean"),
         tag = cms.string("lowPtElectron_eb_ecalTrk_20To50_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_ee_ecalTrk_20To50_mean"),
         tag = cms.string("lowPtElectron_ee_ecalTrk_20To50_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_eb_ecalTrk_20To50_sigma"),
         tag = cms.string("lowPtElectron_eb_ecalTrk_20To50_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("lowPtElectron_ee_ecalTrk_20To50_sigma"),
         tag = cms.string("lowPtElectron_ee_ecalTrk_20To50_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("gsfElectron_eb_ecalOnly_05To50_mean"),
         tag = cms.string("gsfElectron_eb_ecalOnly_05To50_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("gsfElectron_ee_ecalOnly_05To50_mean"),
         tag = cms.string("gsfElectron_ee_ecalOnly_05To50_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("gsfElectron_eb_ecalOnly_05To50_sigma"),
         tag = cms.string("gsfElectron_eb_ecalOnly_05To50_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("gsfElectron_ee_ecalOnly_05To50_sigma"),
         tag = cms.string("gsfElectron_ee_ecalOnly_05To50_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("gsfElectron_eb_ecalTrk_05To50_mean"),
         tag = cms.string("gsfElectron_eb_ecalTrk_05To50_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("gsfElectron_ee_ecalTrk_05To50_mean"),
         tag = cms.string("gsfElectron_ee_ecalTrk_05To50_mean_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("gsfElectron_eb_ecalTrk_05To50_sigma"),
         tag = cms.string("gsfElectron_eb_ecalTrk_05To50_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("gsfElectron_ee_ecalTrk_05To50_sigma"),
         tag = cms.string("gsfElectron_ee_ecalTrk_05To50_sigma_2018V1"),
         connect = cms.string("sqlite_file:/t3home/gcelotto/CMSSW_10_2_15/src/PhysicsTools/BParkingNano/test/lowPtEleReg_2018_02062020_nv.db")))







from PhysicsTools.BParkingNano.nanoBPark_cff import *
process = nanoAOD_customizeMuonTriggerBPark(process)
process = nanoAOD_customizeElectronFilteredBPark(process)
process = nanoAOD_customizeTrackFilteredBPark(process)
#process = nanoAOD_customizeBToKLL(process)
#process = nanoAOD_customizeBToKstarEE(process)
#process = nanoAOD_customizeBToKstarMuMu(process)
process = nanoAOD_customizeTriggerBitsBPark(process)




# Path and EndPath definitions
#process.nanoAOD_KMuMu_step = cms.Path(process.nanoSequence)
process.nanoAOD_jets_step = cms.Path(process.nanoSequence)

#process.nanoAOD_Kee_step   = cms.Path(process.nanoSequence + process.nanoBKeeSequence   + CountBToKee   )
#process.nanoAOD_KstarMuMu_step = cms.Path(process.nanoSequence + process.KstarToKPiSequence + process.nanoBKstarMuMuSequence + CountBToKstarMuMu )
#process.nanoAOD_KstarEE_step  = cms.Path(process.nanoSequence+ process.KstarToKPiSequence + process.nanoBKstarEESequence + CountBToKstarEE  )

# customisation of the process.
if options.isMC:
    from PhysicsTools.BParkingNano.nanoBPark_cff import nanoAOD_customizeMC
    nanoAOD_customizeMC(process)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

# Schedule definition
process.schedule = cms.Schedule(
                                process.nanoAOD_jets_step,
                                process.endjob_step, 
                                process.NANOAODoutput_step
                               )
if options.wantFullRECO:
    process.schedule = cms.Schedule(
                                    process.nanoAOD_jets_step,
                                 #   process.nanoAOD_Kee_step,  #   process.nanoAOD_KstarMuMu_step, #   process.nanoAOD_KstarEE_step,
                                    process.endjob_step, 
                                    process.FEVTDEBUGHLToutput_step, 
                                    process.NANOAODoutput_step
                                    )
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

process.NANOAODoutput.SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
                                   'nanoAOD_jets_step', 
                               #    'nanoAOD_Kee_step', #    'nanoAOD_KstarMuMu_step',#   'nanoAOD_KstarEE_step',
                                   )
)


### from https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/3287/1/1/1/1/1.html
process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))
process.NANOAODoutput.fakeNameForCrab=cms.untracked.bool(True)    

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
