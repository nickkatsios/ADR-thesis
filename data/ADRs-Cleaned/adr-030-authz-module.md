adr authorization module changelog initial draft updated draft proto api update sdkmsg instead sdkservicemsg latter concept removed cosmos sdk updated sendauthorization proto doc clarify spendlimit required field generic authorization bank msg type url create limit bank authorization abstract adr defines xauthz module allows account grant authorization perform action behalf account account concrete case motivated module include desire delegate ability vote proposal account besides account one delegated stake subkeys functionality originally proposed term describe functionality provided module together feegrant module adr group module subkeys functionality roughly refers ability one account grant subset capability account possibly robust easier security measure instance master account representing organization could grant ability spend small amount organization fund individual employee account individual group multisig wallet could grant ability vote proposal one member key current implementation based work done gaians team hackatom berlin create module named authz provides functionality granting arbitrary privilege one account granter another account grantee authorization must granted particular msg service method one one implementation authorization interface type authorization determine exactly privilege granted extensible defined msg service method even outside module msg method defined authorization reference msg typeurl authorization type authorization interface protomessage msgtypeurl return fullyqualified msg typeurl described adr process accept reject request msgtypeurl string accept determines whether grant permit provided sdkmsg performed provides upgraded authorization instance acceptctx sdkcontext msg sdkmsg acceptresponse error validatebasic simple validation check doesnt require access information validatebasic error acceptresponse instrument controller authz message request updated deleted type acceptresponse struct accepttrue controller accept authorization handle update accept bool deletetrue controller must delete authorization object release storage resource delete bool controller calling authorizationaccept must check updated nil yes must updated version handle update storage level updated authorization example sendauthorization like defined msgsend take spendlimit update zero type sendauthorization struct spendlimit specifies maximum amount token spent authorization updated token spent field required generic authorization bank msg type url create limit bank authorization spendlimit sdkcoins func sendauthorization msgtypeurl string return sdkmsgtypeurlmsgsend func sendauthorization acceptctx sdkcontext msg sdkmsg authzacceptresponse error msend msgmsgsend return authzacceptresponse sdkerrorserrinvalidtypewraptype mismatch limitleft isnegative aspendlimitsafesubmsendamount isnegative return authzacceptresponse sdkerrorserrinsufficientfundswrapfrequested amount spend limit limitleftiszero return authzacceptresponseaccept true delete true nil return authzacceptresponseaccept true delete false updated sendauthorizationspendlimit limitleft nil different type capability msgsend could implemented authorization interface change underlying bank module small note acceptresponse acceptresponseaccept field set true authorization however rejected function accept raise error without setting acceptresponseaccept false acceptresponseupdated field set nonnil value real change authorization authorization remains instance always case genericauthorization field nil msg service protobuf service msg grant grant provided authorization grantee granter account provided expiration time rpc grantmsggrant return msggrantresponse exec attempt execute provided message authorization granted grantee message one signer corresponding granter authorization rpc execmsgexec return msgexecresponse revoke revoke authorization corresponding provided method name granter account granted grantee rpc revokemsgrevoke return msgrevokeresponse grant give permission execute provided method expiration time message grant googleprotobufany authorization cosmosprotoacceptsinterface cosmosauthzvbetaauthorization googleprotobuftimestamp expiration gogoprotostdtime true gogoprotonullable false message msggrant string granter string grantee grant grant gogoprotonullable false message msgexecresponse cosmosbaseabcivbetaresult result message msgexec string grantee authorization msg request execute msg must implement authorization interface repeated googleprotobufany msg cosmosprotoacceptsinterface cosmosbasevbetamsg router middleware authz keeper expose dispatchactions method allows module send msg router based authorization grant type keeper interface dispatchactions route provided msg respective handler grantee granted authorization send message first signer msg dispatchactionsctx sdkcontext grantee sdkaccaddress msg sdkmsg sdkresult cli exec method cli user want run transaction behalf another account msgexec exec method instance gaiacli gov vote yes grantee generateonly gaiacli authz exec sendas granter grantee would send transaction like msgexec grantee mykey msg sdkmsg msgvote proposalid voter cosmosthsdghegh yes grant grantee authorization granter cli command send msggrant transaction authorization encoded json cli revoke grantee methodname granter cli command send msgrevoke transaction builtin authorization sendauthorization protobuf sendauthorization allows grantee spend spendlimit coin granter account message sendauthorization repeated cosmosbasevbetacoin spendlimit genericauthorization protobuf genericauthorization give grantee unrestricted permission execute provided method behalf granter account message genericauthorization cosmosprotoimplementsinterface authorization msg identified type url grant unrestricted permission execute string msg consequence positive user able authorize arbitrary action behalf account user improving key management many case solution generic previously considered approach authorization interface approach extended cover case sdk user negative neutral reference initial hackatom implementation httpsgithubcomcosmosgaianscosmossdktreehackatomxdelegation posthackatom spec httpsgistgithubcomaaroncbdfcadbabedelegationmodule bharvest subkeys spec httpsgithubcomcosmoscosmossdkissues