enable implementing binding separate crate deciders teshaq bdk mhammond technical story issue implementation testing implementation problem statement binding generator currently live uniffibindgen crate creates following difficulty binding live uniffi repository uniffi team maintain least review change make difficult support thirdparty developer writing binding language core team wish maintain change specific binding generator requires new uniffibindgen release accessible consumer even doesnt impact binding binding require complex build system test including build system uniffi would require developer install build system example type geckojs binding would require mozillacentral build system build test currently run test binding cargo test mean one binding target get outdated fails developer doesnt needed library installed one target test would fail also impossible write new binding live uniffibindgen crate adr proposes enabling thirdparty crate implement binding generator describes necessary uniffi change enable driver support firefox desktop javascript binding generation testability easy developer test binding care without navigate install unfamiliar library build system developer experience easier write maintain new binding generator currently release cutting release change one binding generator shouldnt harm another note version compatibility handled separate adr considered nothing mean keeping everything asis deciding binding generator least live uniffibindgen crate create public api external crate implement binding developer would trait exposed leverage implement binding generator live uniffibindgen uniffibindgen would still handle generic task related binding generation pro con nothing good make harder user accidentally different version uniffi scaffolding binding since implemented together crate good make easier make change multiple binding time case breaking change uniffi etc bad maintainability grow difficult especially binding added core uniffi team familiar bad testability also grow difficult binding added requirement test binding together one repository difficult maintain bad release binding generator tied release uniffibindgen create public api external crate implement binding good ownership clear member community opt maintain binding generator good would test core binding maintain others tested maintainer example geckojs binding generator tested mozillacentral good release external binding wouldnt impact internal one unless change internal uniffi behavior bad easier accidentally version mismatch see adr bad testability increase complexity required publish fixture example see overall preferred requirement implement binding geckojs cant tested endtoend without complex build system creates possibility community contributor writing maintaining binding generator repository increased risk version mismatch dealt see adr outcome chosen create public api external crate implement binding change expose trait bindinggenerator trait would following associated type implement bindinggeneratorconfig bindinggeneratorconfig would another trait binding generator implement configuration type purpose type carry binding specific configuration parsed uniffitoml function writebindings take componentinterface config writes binding directory outdir expose generic function entry point binding generator call generic function generating binding exposed uniffibindgen generic function parse udl parse configuration uniffitoml bindinggeneratorconfig trait consumer implement initialize bindinggenerator type consumer provides call writebindings generic type see implementation change expose fixture testing enable external binding generator implement test would publish fixture new uniffitesting crate helper consumer build consume fixture crate see implementation testing change