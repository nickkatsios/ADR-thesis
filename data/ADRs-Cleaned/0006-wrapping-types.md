update code update template wrapper proposed deciders bendk rfkelly mhammond consulted jhugman janerik travis discussion problem statement uniffi able support type external crate rust orphan rule prevents implementing viaffi trait order add support needed choose updating uniffi trait updating liftpy lowerpy scaffolding function general question come often adding new feature often choose two path updating code target language updating template wrapping code adr discus particular also general pro con path driver wanted support external crate define new type wrapping uniffi primitive type example supporting serdejsonvalue wrap string handle wrap int wanted kind wrapping code exist outside uniffi allow experimentation wrapped type support type specific particular library example applicationservices guid type considered extend template code wrap type recordenumobjecterror code would newtype pattern wrap external type struct wrappertypeexternaltype filter function generate code wrap liftlowerreadwrite example lowerrs filter could output wrappertypexlower lower wrappertype update uniffi code generalize viaffi trait define fficonverter work almost viaffi except instead always converting self ffitype define second associated type rusttype fficonverter convert rusttype ffitype userdefined type record error object enum create new unit struct set rusttype type handle external type without issue since implementing fficonverter struct orphan rule doesnt apply associated type eliminated lowerrs liftrs readrs writer filter function ffi conversion handled rust code directly outcome chosen update uniffi code generalize viaffi trait taken relatively easy implement wrapper type allowing external crate add custom scaffolding code code could wrap primitive type liftingloweringreadingwriting handled rust code gone wrapping code would hook template function liftrs lowerrs etc couldnt see simple way implement updating code target language result readable generated code newtype pattern make generated code difficult read especially type wrapped vec etc pattern could implement wrapping binding side positive consequence paved way wrapper type simplified template code negative consequence implementing wrapping template function lead direct code example lifting integer value noop still generate function call issue rust since compiler optimize call away could issue binding code decide issue could hybrid solution generate liftinglowering code target language also liftlower filter function exist solely optimize liftinglowering simple type