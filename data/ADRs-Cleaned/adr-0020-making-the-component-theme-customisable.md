kind architecture record adr making component theme customisable florian sander explained adr finding accessible color creating design token introduced design token divided two category choice represent color component supposed private exposed customizable instance colorred bed represent semantic choice applying specific color specific content type supposed public customizable instance colortextsuccess token stored custom prop inside javascript file needed imported component goal semantic token kind api theme customisation one wanted customise common theme mainly color moment component would insert color value semantic token instance colortextsuccess value problem several limitation made properly customising theme impossible limitation actually well known first step building theme system making customisable serving theme theme contained javascript file every component import import defaultthemestyles stylesdefaultthemejs static get style return defaulttheme meant token processed constructable stylesheet difficult override value file outside component keeping javascript file provide token would meant relying build process allow people customise token since also make component available via cdn want rely build process allow people override token value planning dark theme component issue background color would block theme customisation define default background color cause issue long integrated white color background soon changed background color parent issue appeared background color hard coded wanted component dark mode changing colorbgdefault token would effect component background would remain white hand default font color inherited thus could end white text color inherited website dark mode color white background color hard coded within component solution serving theme decided move theme javascript file file several advantage file easily swapped another require hook build process file work integrate easily web project component import theme anymore also drawback people file integrate workflow people might forget file word make theme little bit easy way easier customise decided make component completely broken without file black white text still readable component state selected etc still visible goal people would notice something wrong updating build process file update build process file would part final bundle cdn npm package npm package npm package decided copy file inside style folder rely rollup plugin copy also minify file even though really small moment rollup npm config plugins copy target src srcstylesdefaultthemecss dest diststyles transform stylesheet minifystylesheetstylesheet component inside project one import file nodemodules procedure depends project stack tried give example component theme cdn needed update cdn would serve file specific endpoint wanted provide dynamic endpoint would handle semantic versioning correctly instance stylescssversion considering file going change lot want generate new file every component version want store defaultthemecss defaultthemecss file actually exact content meant cdn backend needed way map file related version one file could related several component version cdn already system exact thing component filename contain hash generated rollup based content mean filename change content change cdn relies manifest match component version specific file related component code dependency providing filename hash file given filename hash file needed processed rollup part bundle meant could rely copy rollup plugin like npm build rollup typically process javascript file new file part bundle neither copied given filename hash based content created custom plugin named stylesassetsplugin plugin read file minifies rollup emitfile function generate file part rollup bundle const stylesheet fsreadfilesyncsrcstylesdefaultthemecss utf const minifiedstylesheet transformstylesheet thisemitfile type asset name defaultthemecss source minifiedstylesheet rollup generates filename hash based file content deps manifest file needed referenced inside manifest associated given version instance manifest json file specific version component instance manifest version component named depsmanifestjson done inside depsmanifest plugin updated plugin provide new style property also decided bump manifestversion example manifest new style property manifestversion packageversion xzy file style path assetsdefaultthemecacss serving file content updated cdn backend provide new endpoint component dependency typically serve file split request several smaller one optimize performance instance version lang import addtranslations setlanguage incbejs import instringddjs import lang translation translationsenabfdjs addtranslationslang translation setlanguagelang importvendoraabjs importcclinkdajs importccbuttoncacjs contrary component split request several smaller request payload actually small dependency decided inline content file directly response way one small call make server updated cdn allow developer directly copy link tag corresponding selected version instance html link relstylesheet hrefhttpscomponentsclevercloudcomstylescssversion avoiding variable conflict since chose provide token global custom property needed make sure would conflict custom property chose prefix global custom property semantic token colortextsuccess became cccolortextsuccess note choice prefixed meant exposed anyway custom property defined component level prefixed since global planning dark theme working theme customisation always dark mode mind probably challenging theme customisations plan supporting handling default background text color thinking dark theme obvious thing allow swapping default font color well default background color might seem trivial component needed background color transparent others needed default background color design token instance ccbutton outlined mode needed transparent avoid button look weird inside notice neutral background ccinput form field needed default background make sure would always stand rest font color question whether component inherit always define default text color token component level host chose let default font color inherited everytime possible exception closer standard html element way simpler deal mean however switch default font color define font color parent component body would make sense time apply color cccolordefaulttext changing design token name avoid confusion renamed light suffix weak design token avoid confusion dark theme cccolortextlight became cccolortextweak idea color meant stand default text color light theme usually mean lighter shade default text color dark theme might actually mean opposite darker shade default text color next step lot coming remove choice design token color variable theme published via npm cdn make sure component rely avoid shipping layer variable supposed customised anyway see issue publish documentation design token customise theme see issue opportunity define clear terminology token layer discussed naming design token lukas oppermann continue grow design token see issue introduce dark theme might done several step grow design token see issue