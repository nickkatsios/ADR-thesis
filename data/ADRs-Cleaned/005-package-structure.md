package structure proposed project defines library component build top aws cdk aiming improve user experience managing infrastructure guardian library continues grow important library structured sensibly developer maintaining library position match structure different cdk library aws cdk publishing numerous individual library split resource group iam although publishing one library could mirror structure directory would mean user familiar cdk would able take good guess component lived project also mean dont make component live follow aws could define style library doesnt contain anywhere near full range component aws cdk provides following structure may best choice provide range component library provide multiple implementation underlying resource policy construct gulogshippingpolicy gussmruncommandpolicy gugetsobjectpolicy top level directory construct directory mirror aws cdk library name directory contain indexts file export class within file within directory either top level nested within directory nested directory exist grouping multiple implementation underlying construct example gulogshippingpolicy gussmruncommandpolicy gugetsobjectpolicy could seperate file within constrcutsiampolicies directory directory also export memebers indexts file pattern defined top level within pattern directory exported indexts file imported guardiancdk consequence clearly defined project structure make easier developer library find add maintain component also make intuitive experience user library know look import component