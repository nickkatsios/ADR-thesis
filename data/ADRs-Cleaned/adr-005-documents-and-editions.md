record resolve consistency uniqueness content publishing api adopted openclosed principle domain model based around central contentitem model numerous entity store data related contentitem however contentitem knowledge time data structure revealed number problem developer user publishing api difficulty maintaining uniqueness constraint multiple table particularly problematic concurrent request long verbose query inconsistent query normally authored rubyonrails slow performing query due many join large amount code try resolve problem identified number nonexclusive considered resolve issue merge userfacingversion locale contentitem table would allow set single uniqueness constraint could raise error concurrent request merge userfacingversion locale basepath state contentitem table would allow multiple uniqueness constraint break openclosed principal split contentitems document edition model edition particular version content item document spanning version split contentitem model two separate model one focus uniqueness relationship latter content contentstore specified directly database rather byproduct state value store state history would change state single field updated collection stored contentitem take location centric approach storing basepath value stored contentitems would involve table storing item particular basepaths would open door storing item redirects require basepath considered selection chosen implemented rejected favour effectively superseded felt additional complexity introduced openclosed principal greater cost potential complexity increasing concern contentitem model concern model could become god model initial proposal tried avoid agreed model layer logic possible instead supplementary class would allow keep model thin uncertainty naming decided original proposal document edition concept already govuk publishing synonymous meaning concern content publishing api store considered document however felt term document already within publishing would introducing fresh problem key aspect influenced choosing offered simple mean lock request concurrency provided simpler interface someone look content draft live made distinction translation piece content clearer rejected felt letting application concern influence schema greatly also clear difference model would responsibility data felt would make challenging abstraction explain initially delayed investigation however transpired unique index basepath state postgresql would thus implemented rejected due current concern idea may revisited part work include workflow history andor support greater array workflow state rejected since point concerned different entity sharing concept basepath felt concern idea offered increase complexity without clear benefit reconsidered pursue idea redirects firstclass citizen