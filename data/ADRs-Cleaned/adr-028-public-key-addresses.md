adr public key address changelog initial version analysis algorithm update proposed abstract adr defines address format addressable cosmos sdk account includes new public key algorithm multisig public key module account issue identified public key address space currently overlapping confirmed significantly decrease security cosmos sdk problem attacker control input address generation function lead birthday attack significantly decrease security space overcome separate input different kind account type security break one account type shouldnt impact security account type initial proposal one initial proposal extending address length adding prefix different type address ethanfrey explained alternate approach originally httpsgithubcomiovoneweave spent quite bit time thinking issue building weave cosmos sdk basically define condition type format human readable string binary data appended condition hashed address byte prefix make impossible find preimage given address different condition secpk explained depth httpsweavereadthedocsioenlatestdesignpermissionshtml code look mainly top process condition httpsgithubcomiovoneweaveblobmasterconditionsgo explained approach sufficiently collision resistant yeah afaik byte collision resistance preimages unique malleable space would expect collision likely around element birthday paradox want find collision existing element database still element written state good example brought public key byte valid public key two algorithm supported codec meaning either broken would break account even secured safer variant issue differentiating type info present preimage hashing address would like hear argument byte space actual issue security would happy increase address size weave figured cosmos ethereum bitcoin byte good enough argument made feel secure done deeper analysis led first proposal proved good enough concatenate key type public key hash take first byte hash summarized shakeytypeprefix keybytes review discussion discussed various solution agreed byte future proof extending address length way allow address different type various signature type etc disqualifies initial proposal issue discussed various modification choice hash function move prefix hash function keytypeprefix shakeybytes posthashprefixproposal double hashing shakeytypeprefix shakeybytes increase keybytes hash slice byte byte concluded byte produced good hash function future secure requirement support currently tool dont want break ecosystem add long adaptation period ref httpsgithubcomcosmoscosmossdkissues try keep address length small address widely state part key object value scope adr defines process generation address byte enduser interaction address api cli etc still bech format address string adr doesnt change bech string encoding give support checksum error code handling user typo define following account type define address function simple account represented regular public key secpk naive multisig account composed addressable object naive multisig composed account native address key bls group module account module account basically account cannot sign transaction managed internally module legacy public key address dont change currently jan officially supported cosmos sdk user account secpk basic account legacy amino multisig existing cosmos sdk zone following address format secpk ripemdshapkbytes legacy amino multisig shaaminocdcmarshalpk dont want change existing address address two key type remain current multisig public key amino serialization generate address retain public key address formatting call legacy amino multisig public key protobuf also create multisig public key without amino address described hash function choice part cosmos sdk sha basic address start defining base algorithm generating address call hash notably account represented single key pair public key schema associated typ string explained next section hash cryptographic hash function defined previous section const alen func hashtyp string key byte byte return hashhashtyp keyalen byte concatenation doesnt separator algorithm outcome consultation session professional cryptographer motivation algorithm keep address relatively small length typ doesnt impact length final address secure posthashprefixproposal first byte pubkey hash significantly reducing address space moreover cryptographer motivated choice adding typ hash protect switch table attack addresshash low level function generate base address new key type example bls addresshashbls pubkey composed address simple composed account like new naive multisig generalize addresshash address constructed recursively creating address sub account sorting address composing single address ensures ordering key doesnt impact resulting address dont pubkey interface anything addressable type addressable interface address byte func composedtyp string subaccounts addressable byte address mapsubaccounts lengthprefixaaddress address sortaddresses return addresshashtyp address addressesn typ parameter schema descriptor containing significant attribute deterministic serialization utf string lengthprefix function prepends byte address value byte length address bit prepending address must bit long lengthprefix eliminate conflict assures list address every long concatenatemapas lengthprefixa mapbs lengthprefixb implementation tip account implementation cache address multisig address new multisig public key define typ parameter based encoding scheme amino protobuf avoids issue nondeterminism encoding scheme example protobuf package cosmoscryptomultisig message pubkey uint threshold repeated googleprotobufany pubkeys func multisig pubkey address first gather nested pub key var key addressaddressable cryptotypespubkey implement addressable key range multisigpubkeys key appendkeys keygetcachedvaluecryptotypespubkey form type message name cosmoscryptomultisigpubkey threshold joined together prefix fmtsprintfsd protomessagenamemultisig multisigthreshold composed function defined return addresscomposedprefix key derived address must able cryptographically derive one address another one derivation process must guarantee hash property hence already defined hash function func deriveaddress derivationkey byte byte return hashaddress derivationkey module account address module account module type module account sub account submodule account created based module name sequence derivation key typically first derivation key class derived account derivation process defined order module name submodule key subsubmodule key example module account created addressmodulemodulename key example submodule account created grouppolicyaddresses byte addressmodulemodulename grouppolicyaddresses policyid addressmodule function addresshash module type argument byte representation module name concatenated submodule key two last component must uniquely separated avoid potential clash example modulenameab submodulekeybc derivation key modulenamea submodulekeybbc null byte separate module name submodule key work null byte part valid module name finally subsubmodule account created applying derive function recursively could derive function also first step rather concatenating module name zero byte submodule key decided concatenation avoid one level derivation speed computation backward compatibility existing authtypesnewmoduleaddress add special case module function derivation key provided fallback legacy implementation func modulemodulename string derivationkeys byte byte lenderivationkeys return authtypesnewmoduleaddressmodulename legacy case submoduleaddress hashmodule bytemodulename key return folda derivea subsubkeys submoduleaddress example lending btc pool address would btcpool addressmodulelending btcaddress want create address module account depending one key concatenate btcatomamm addressmoduleamm btcaddress atomaddress example smartcontract address could constructed smartcontractaddr modulemysmartcontractvm smartcontractsnamespace smartcontractkey equal smartcontractaddr derived modulemysmartcontractvm smartcontractsnamespace smartcontractkey schema type typ parameter hash function unique account type since cosmos sdk account type serialized state propose protobuf message name string example public key type unique protobuf message type similar protobuf package cosmoscryptosr message pubkey byte key protobuf message unique fully qualified name example cosmoscryptosrpubkey name derived directly proto file standardized way place type url anys easily obtain name protomessagenamemsg consequence backwards compatibility adr compatible committed directly supported cosmos sdk repository positive simple algorithm generating address new public key complex account module algorithm generalizes native composed key increased security collision resistance address approach extensible future usecases one address type long dont conflict address length specified byte support new account type negative address communicate key type prefixed approach would done address longer consume storage space requires refactor kvstore store key handle variable length address neutral protobuf message name key type prefix discussion account fixed name may constructed way module discussing idea account predefined name meregen could institution without going detail kind address compatible hash based address described long dont length specifically special account address must length equal byte appendix consulting session end dec session alan szepieniec consult approach presented alan general observation dont preimage resistance byte address space collision resistance attacker control input object address problem birthday attack issue smartcontracts hashing sha mining breaking address preimage hashing algorithm attack breaking blake break blake alan pretty confident current security analysis blake hash algorithm finalist author well known security analysis algorithm alan recommends hash prefix addresspubkey hashhashkeytype pubkey main benefit free user arbitrary long prefix name still dont risk collision switch table discussion penalization adding prefix post hash aaron asked post hash prefix addresspubkey keytype hashpubkey difference alan noted approach longer address space stronger algorithm complex composed key merging tree like address algorithm fine module address module address different size differentiate set preimage prefix module address keep byte space hashhashmodule modulekey aaron observation already deal variable length break secpk key discussion arithmetic hash function zkp posseidon rescue problem much bigger risk dont know much technique history cryptoanalysis arithmetic construction still new ground area active research post quantum signature size alan suggestion falcon speed size ration good aaron think alan based early extrapolation thing get able break cryptography thats lot uncertainty magic happening recursion linking simulation speedup progress idea let say key two different address algorithm different case still safe alan want hide public key case secure fix reference note