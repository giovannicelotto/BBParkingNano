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

options.setDefault('maxEvents', 50000)       # number of events analyzed. then consider the trigger
options.setDefault('tag', '10215')
options.parseArguments()

globaltag = '102X_dataRun2_v11' if not options.isMC else '102X_upgrade2018_realistic_v15'
if options._beenSet['globalTag']:
    globaltag = options.globalTag

extension = {False : 'data', True : 'mc'}
outputFileNANO = cms.untracked.string('_'.join(['HH4b', extension[options.isMC], options.tag])+'.root')
outputFileFEVT = cms.untracked.string('_'.join(['BParkFullEvt', extension[options.isMC], options.tag])+'.root')
if not options.inputFiles:
    options.inputFiles = [
        '/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CFBFCA29-1649-2345-970E-731824064446.root'] if not options.isMC else [
        '/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/2EA135EF-43C9-624B-A50B-B72B2E2D5393.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/A386A139-01EC-3C4C-AB48-F2FC8814FDF2.root', 
        '/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/23EBA0E0-6729-7C41-9888-F8E07B20C677.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/5A00A84C-ED50-B94B-A25D-EE2A6EAD3D4C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/7010DF71-3814-3047-8786-3A3A894D0E02.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F338472B-D37A-8040-B482-111D21820AD7.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/DE59C01E-2184-334D-A77A-6D5B18697B02.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F7C64AA3-BA68-0F4D-B845-D59C363DF441.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/34F08FC8-A8C6-DC4B-9018-F5D15643214E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/220732E7-4467-8845-9A2B-1291F221D868.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/AFA7115C-B768-F941-A75E-0EB075D041DE.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/089A8EE8-D28D-984D-B919-B805354AA768.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/953BD5D9-E431-4242-AF61-0B6F02C2E45F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/ECEA4DAC-D2C1-B54B-B063-62D2FC191AB6.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/E6445E0E-293D-C54D-945A-231965851B8D.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/AD774CA0-0F77-B84F-84EE-2166D26C86C7.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/B87D28CF-09FB-FB43-A667-195B9AAA172B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/785B0DA3-5DC5-694A-B6C5-EEE438D17E55.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CA6C0D04-E5D6-374F-81B3-A05B14D92586.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/799C1218-6E4B-3846-A10F-090FF71F79F1.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/135B5FBB-C405-8546-9B0D-78FF244C7409.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/510A1421-15C0-9441-936F-10004740A139.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/79E44496-F1F8-9A40-A7D9-3970D95422A9.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/06FC569F-8B20-B941-BAEF-9DC14D217B5F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F79A682B-AB39-3F4C-98E2-78D70C4A206B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/57E48ADA-723F-8F47-BCD5-111299FADEB0.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/62A947EE-9E4F-A94A-8B2B-27179293953B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/95A0C2EE-1315-3F40-ADF8-322CCAA796AD.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/38801BEA-2A45-1147-BA54-4947AB82E00F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/98AB0A14-377F-2D4B-B911-5F273E2CCD3B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/2BF9D9FD-3AB9-4F41-92E0-085884F1BA21.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/04DE3B16-8AA3-9245-8FB8-BA2441952BDE.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F9F348BF-7723-CD47-8E76-182CA2F22E58.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/D6ED00BD-BED9-FE4D-98AC-47C085DE2DCC.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/A66B3322-3EBD-DC4B-8D01-1BD763E9800C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CCF6A87C-A00A-E14D-81D3-577D60413B6B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/BC5B03E8-40AA-7244-AF70-2F60FE00622E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/C9F51DDD-30BA-D545-9F2F-B911E23C23F7.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CF3F1866-4962-0B4D-8314-C1FE6F2DA1D8.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/6C14358E-D4EA-8642-988D-CF240672C76F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/D581C6F5-798B-7E41-90A3-C93A79E4FCA3.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/2EC5AF93-887F-1F4C-9EF9-A7DC712D3760.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/669F5BD2-88E2-F140-9397-7698CFB10F6E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/05C91C42-FE2A-244E-894F-DF14E9055D18.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F3AFE7EE-FCCB-FE47-A140-12CE86BC6E50.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/0E878E66-7CE0-074A-802D-12DA959CA4FA.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/A693F93A-C6DA-F641-BA0C-CE87D57E1961.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CCB2EF45-AF09-894E-BBAE-A86001119A2F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/099805B3-7F58-FB4F-AD44-99F9ECFB5C63.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/72ECE7C4-7480-7D4E-94D7-15BBE0619A68.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/01799CFD-BA2E-844B-87CB-273185CF1A4A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/2BDEFF3E-82E3-3D4A-8F7C-AFC2E0D6943E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/9F21D845-94AD-8F45-83D8-B312AE908A2A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/A0666D8C-F47A-A64A-9CA2-33AD1ABF1DDB.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/6FCB6108-C8B1-5343-AA71-3C18D925541C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/01A68841-D7EA-B145-98E6-BB1F3F2B5545.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/909C4ADA-6A7E-2948-8C74-BDBA64553F4E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/628EB1C1-3BD5-C541-A403-AF4A4991EFEA.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CD6452BF-AF03-664F-BA5C-BADCA4AC7125.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/39138082-0BD0-AD43-9079-F95090EE0F20.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/1A93CBA9-8314-2942-8C4B-CBA4CCDBBA9F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/43D6ABA3-DB7D-5C49-862A-20262E85FB7C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/C1A10EDE-5E22-F848-99A8-3E9158BD8E46.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F7B57451-6D2D-F148-B23A-75DD1D5F21B5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/1510BE78-741C-9341-BF87-90B16501E921.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/B4E469AD-509E-C246-B512-9F4EEDB41AD8.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/11A18177-53D4-DE43-BC20-3409C162334F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/818790FB-482E-364F-A438-D948E6F3846D.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/71B14FCD-5F77-664F-B3BE-D4AE53C8CDE0.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/E329D271-B2E3-B643-8616-E9F24E777221.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/BA35C994-5443-C244-AD93-C5E6BB824162.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/95FEBDA8-474F-8348-A6C1-D050C606C0FC.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F5786D4D-FDFA-074A-9AC2-1E33282B82B6.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/E5841139-80CF-AC46-A547-264F6BF9C4F2.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/54FE2061-EF35-5B44-BAA0-F5237F428A5D.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/ED713101-07FD-C24F-96C6-FE2033C6847C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/42DC086D-EBB6-FC46-804A-55D2E96E2CED.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/371F9196-0355-1844-B7E5-8BEDACED1FDC.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/038EAEEC-AA7B-9041-B22D-F9C2F30D4339.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/59E83B1B-0B26-3D4C-999C-9244A5650F9E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/9907CC85-FEC6-0446-A07A-C891CBB2CC63.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/D342BF54-E229-D14C-B224-6550D7525AAE.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/C82D3E9E-0BCB-7B43-A218-09D9A4364EE6.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/A8AE3E5A-6DD5-0E42-B66B-14D75169B5E7.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/0B7E55FE-280F-6A40-AE54-6A75DBFBB363.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/BE02F68F-EFEC-BC42-9D8F-2BB359D95060.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/538ACFB7-137E-0849-951D-A7AE7B3E8D6C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/D0F268FC-BEFF-9F40-96D1-08FD6DCAE630.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/29A2A31E-5739-724C-9250-0319DC5ED9D0.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/226216F5-CBF7-084D-8D32-1DE0B50C2EA4.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/10038D2F-95AD-1943-8EE3-A2F8ACAA28E9.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/03A282E5-DD9C-6E48-9032-19E2F4A4EFE5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/928E95F6-AEC0-9F43-8758-BC98B9265804.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/5D735447-7060-FE42-A3F5-230E255CB6F5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/91E8D7A7-B225-344A-BB95-84BB67848D25.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/19937924-280D-2642-8B11-57663168C92D.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/2BD85BE2-A425-DE46-886B-54AE27D6BF88.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F2402456-A714-944A-9A9B-E498BFC1ECE2.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/21B308C5-B132-BD4C-A155-BB1F69265062.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/A5940314-E0AC-244F-B81C-C18FABD8C5C5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/32C9B779-11E4-AA4B-AF9E-166BA5DB3CC8.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CACB041A-204F-EA48-9F72-4C3B1A82CE92.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/896EF2A7-AFB0-CF4A-AAC8-851A8610EC34.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/7AC26515-CD59-AA45-A215-701A5F11DE6B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/EB0C0D52-3A04-4648-8040-80E89FF4F409.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/DF3BF4EE-C5E0-6447-843F-F0189F2977E4.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/16A793B3-8782-4C45-BC09-E03B8B053C2E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/34D652E7-1B47-2343-B5E9-EAE8C834C3CA.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/60645C56-6CC2-AD48-9FD9-4637C1577184.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/D45B0897-436F-8643-AC61-FEAD7DFDA1B5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/12B24432-F11E-BB48-A4A2-F71A62D93FFE.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/B6504357-AFFD-384F-9451-F72530EA2DFA.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/2A312497-1696-2F4A-AFAE-07A639FA8542.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/1127ADCD-E69E-A545-A0EE-89CE3F693D4E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/6C6FAD05-0BFB-5B41-8C74-96C5ED20950A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F110C26B-F043-F04B-AC4F-689C64FB09F1.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/11B57DD7-DC73-B645-A118-DB2F2C37EC45.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/473556ED-1976-CF46-8DCF-85E49D14F1C4.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/02713625-5219-B94B-88ED-7283261E6EF8.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/5876D3E0-0EDB-4A40-AAAE-E203C6979E8F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/BEA6AB93-3787-EF4E-93F9-6DA0D969BE3B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/7188BD34-B226-A946-A8E3-32BF339F7CF9.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/DAC9060C-8E58-9C40-8711-3E0D596D856A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/10D3BC71-04C2-1341-B3FB-23FC8288E8E9.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/2046FE27-0536-9C44-AB79-5B047C2CA7D6.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/9D0AA422-7553-CA4B-BE5E-A22DD7B51074.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/A4FADF6A-18ED-7246-AD8D-07BE0E3A73C1.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B6EE78B4-0B6A-3441-9629-5673AE7B5B6A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/7F319C6F-C4C9-144E-8053-A063342F2A13.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/47537A86-E472-EE46-BBE6-EB4BA609DDBF.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6DB271C5-62A5-084F-A55C-AB3381C73A6F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/9D5913E9-71A2-6044-8FC2-5128222AED8A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/228F905C-A323-214C-A134-CD03EE0FACCD.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B4A9B772-5FAB-FC4F-B073-E955F92F6EF2.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F586D446-359F-7D49-89D5-D855B2BB3A24.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6B804DFA-FC76-EF40-B563-D0DA61319217.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/19C78C1D-E6D6-9442-8186-A104C89F4D17.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/4E6E76AE-1483-3B48-B61A-B51254453E5B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/C5F10248-F5A9-1B4D-9D2F-5B415CE18BB0.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/3BDEF1B4-5C1A-3B45-A209-EB4FE04AF8D5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/06CAFB35-229C-544A-BB48-F356C32C47C1.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/364DA264-1582-7F4C-9B39-56981BFA868C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/A2414500-1A1B-514F-970D-FE247F8F2BC9.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/EBA37DA8-6F1F-F740-899F-7EFB3133F2B0.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/02E54D00-A671-6649-A780-962534A4CC8E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6E6A5E5A-20FA-3B44-AAC8-09E6A24971DD.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CF6E61EE-A727-2B42-8816-36CA42A261B4.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/45454651-D407-654E-AC36-F15D74175336.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/4EB2B596-C303-5B42-B707-23BB64E891CE.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/7C63996F-F6B6-6647-87F3-89371E51B536.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/765DC7D7-5CE4-0C42-9D97-9C5524738A2D.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/730F45E2-1061-C34F-8144-FA7B8D041EE2.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/762F3326-3696-1248-805E-7D962E8C2C28.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B2A7E6DB-F25B-3743-B7D9-3B437764727B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B36CE5B2-3FAD-734C-8F77-B1309A4D5128.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B64F9699-5B99-7F40-BEDF-2718BEE2743A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/BF5647DB-0E43-254D-83B4-5CA405C2A890.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/1243DFCA-B86A-284D-8DD6-600424C08FAC.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/49FE0321-6952-174D-8D83-6DC86CB3493B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/E62ACEF7-D49A-4840-ABF8-6096DDFFAA80.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/D353152A-8245-3245-AFFF-B435B13CBDAF.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/9946E555-5C41-944C-B43B-45F01F2F5473.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/244E35EC-AE7E-0247-820C-FB972BC7BFB1.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F25154A9-2B15-954F-83BB-E1E519F8329B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/51ECF3C2-CC0D-FA4D-8CB9-B316AB1FF11F.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/070E922B-F31D-1347-9F47-E8E8100CAC4B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/2447DE9D-A51B-054F-9C30-D1D158A5BF8C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/EE482A46-9894-4642-881E-B1E175B6810C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/DDC0682E-0323-984A-93A1-1CF2075A1A56.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/FFF92AB0-3DA3-1E44-BC29-1308B864C321.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/414ADE62-5624-F94D-8A3B-DF4E40D5FDA5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/16B728C6-C43D-9947-B1AB-0DF3C16D2F00.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6DCC456E-114A-4F49-9D84-7CD6D8B0E6E6.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B69F386A-94F8-A54F-9943-AEDD8BBB0FAF.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/3CD123B6-0DE5-B64C-8176-9BC902E329D6.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/21646ACE-66C0-0244-9299-3125E2574113.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CE79D4E1-3AF3-9847-88A3-00CB7287A190.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/431058DD-8CC8-2848-9B38-EE3B47EC5E70.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8F0E7EE7-AA54-5240-A6FA-A38A0FAD7542.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/30095F00-CC2B-1841-BCCA-734EC1F4F61E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/C7491212-2D12-4748-BF21-D4C53CF750C2.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/4D741DAF-49E2-2C4E-AC48-ECF7819E5A03.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/E6564E4A-F0BC-6D4C-9E21-4A278034192D.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/29B0093F-A40A-C64D-8EBB-76A72E71F2A3.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/42E3ADAF-6FC3-7E4C-B568-56F3D01E6AA9.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/2BC8DEB2-B78E-EE48-BE6E-FB6BB21A4EE5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B318A043-8EAF-0B45-B6F4-98395152A013.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/212B3A0A-D3B6-3B48-94D7-6F541F97709C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6CC6BABE-B866-C64D-BF46-F83BEA8B0A23.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/0549FEFA-31B9-884B-8B4A-1EA2DB5F0646.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/C2335E8C-0F2F-BA4F-9F68-C8A7128B9487.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/29688EB3-6A96-6744-984F-A3AB96F0DBB7.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B3895230-B1D5-CD44-B032-5ECEE30253E8.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/136113B1-D8C8-344E-AE49-F7F4EF4B2663.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/ADCE46A5-D8AD-A647-9A51-4DD472529802.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F4C37487-4048-2446-AF79-CDEF08E09BFE.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/16299125-F9F1-E746-B344-825D68F55652.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/5F7A4D38-216D-D649-A3C7-0AC289AB132E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/477C217B-6260-CF45-BC92-ED73C160F31B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/5FDDA84A-6ED0-7B48-AA8E-DDC4DAE463EA.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6DD5579E-A725-3F4C-879C-F971084A3E56.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/4B93AA0C-2598-FA45-B9CA-0D6019956021.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/7BA482AB-BB3A-D84F-8B9F-1EFC69CCAA82.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/3EEF25D5-7462-2047-84B8-737D6A03FCB8.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/B7E6F4A8-FAB0-1441-B05E-0D5CA38EF4EB.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8F04FA5C-427C-E74C-970D-486898494ECE.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/18489F97-F497-0845-A75D-80ED0992BEDF.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/B4939884-7B76-3E4A-ACE6-DF11C18E0A9C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/BA5BA25B-D4AB-D14C-B22A-35D32376517D.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/0A0F51B3-C841-CD4E-ACE4-F479584F977C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F826E245-07F5-AC48-992C-9921C2A8B1B2.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/99BBEC75-992C-D048-A7B5-0FF3BCA21E64.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/D521CB55-63C1-6944-89E8-01EC5E307C8B.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/71DEE541-A476-C44E-AAC6-39ADA539B6AD.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/E52F34CB-9A52-FB4C-A9EB-3A0357A84869.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/745D9CAD-C053-CA44-9173-72CD3C8C95DF.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/9CB5B487-C678-3043-AA89-8937BC2B7482.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/241A2497-1C3B-F04E-8EC1-BFD52A2E6518.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/984B6F29-A923-2046-9B29-910B1EE4348A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/48751D01-1780-0945-8D7D-641D5C5930EA.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/34B66CB5-B225-5A4B-912F-ADCD09748ECC.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F4C6D1B1-0104-044A-846F-2043B41FF8A2.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/630F7A14-BF4A-2949-8FFF-E5EAF116216C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/BDE9BF69-3B7E-1946-8871-FBDBE95AFBC5.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/80ED75DF-49C1-F144-B19F-24D4A457F2A2.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/01601D65-1575-6A4C-B9DF-F10CD95AC24C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/8569ED65-2971-7949-BF46-7B54AA3F8385.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/FBC27CE1-2C3E-E446-BEF3-975A8D1DB4F7.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/D3922D65-1D3A-904B-A560-6D3B9E1663AE.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/6BB78DCB-D74C-5F46-800D-8A72ED5CF5C4.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/BE67FEBD-F6AE-6049-9462-CDA49CE330AD.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/67110FB6-2D11-FD4F-8B11-584EC1E2EC16.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F049C5D8-3BF6-6940-8B64-02962EB8D2AA.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/23BD0C76-3350-F644-AC45-BDCAA0DDD460.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/BC368359-A7CF-7245-B005-D628B213FE6A.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/83D47CA0-42F0-DE47-997C-353423F33CC4.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/745BE498-ABDC-164C-8CC8-655CFFA0F9E0.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/E2E3097A-F06A-0841-BD02-1D19A313AF17.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/60DD143C-F7D8-0740-9DB5-6D71C0C92A0E.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/GluGluHToBB_M125_13TeV_powheg_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/CFBFCA29-1649-2345-970E-731824064446.root',
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
