graphql apollo setting redesign deciders lauren zugai ben bangert wil clouser jody heavener orchard danny coates barry chen vijay budhram dave justice alex davis problem statement setting redesign project created new react application turn opened door ass certain piece technology stack graphql gql database query language instead query language apis describes data requirement powerful alternative rest benefit gained top existing rest architecture apollo document refers apollo client apollo server piece apollo platform described unified data layer enables application interact data data store apis word allows write handle graphql client server apollo also give many tool box like caching adr serf lay pro con graphql apollo setting redesign project alternative hitting conventional rest endpoint apollo also offer apollo graph manager apollo federation paid service read doc gql apollo server apollo client driver performance implication consideration around number network request data transferred ease setup clientside api call clarity around expected data react integration developer tooling development speed around initial setup new feature roll considered send standard crud request rest endpoint layer graphql apollo top rest architecture making direct database call basic operation full graphql apollo integration direct database call outcome chosen layer graphql top rest architecture gql offer performance optimization allowing consolidate network request sending data requirement single request asking needed client shifting burden figuring gather data client onto server server compensates overfetching sending back requested allowing developer query expect exactly needed endtoend typing declarative way thinking towards data requirement along keeping data requirement schema close theyre consumed make painfully clear whats sent received client server preclude replace supplement direct call fxa authserver line faster initial development also help mitigate risk around relatively novel piece technology fxa nice sideeffects include gql playground managing single api endpoint ability store local state network data apollo cache pro con send standard crud request rest endpoint description dont graphql send request corresponding endpoint pro novel tech additional setup time new technical debt rest api setup vetted year production con would avoid new technical debt would still want work towards optimizing setting page network call would likely spend additional time looking manually optimize call current rest pattern result sending many query overfetching data may figure ideal way organize api call fxapaymentsserver blueprint well turning benefit laid graphql section like clarity clientside around data sent received later choose graphql even approach well face lot refactoring later time could mitigated graphql apollo description section outline pro con graphql apollo general applies graphql novel tech fxa stack entirely novel fxa ecosystem say admin panel project fxaadminpanelfxaadminserver package served prototype experimenting gql apollo pro gql setting redesign wont mix gql rest gql consolidate network request even gql query fed authserver client relieved heavy network request burden instead single request client asks server perform request offer performance boost especially main setting page many sequential request must made since required data requested data returned wont overfetched like traditional rest architecture resulting smaller payload gql offer flexible declarative approach data developer focus describing data rather implementing optimizing numerous rest endpoint rest pattern tend define resource server data requirement schema gql closer client data consumed make painfully clear whats sent received client server improve visibility whats happening component graphql apollo gained lot popularity year substantial community support company backing airbnb facebook surveygizmo github many others stack promotes strong endtoend typing apollo offer great feature box like caching error handling optimistic rendering nice integration tool react even provides react hook react setting application manage interacting single endpoint apollo client make managing data react app straightforward apollo client creates internal redux store hood allows store local data apollo cache place data network request stored apollo also provides graphql playground graphical interactive inbrowser gql ide provides easy access schema selfdocumenting way allows developer write query mutation send server developer verify behaves expected copied directly application graphql make easier evolve apis time provides way deprecate schema member discourage usage certain part apis custom messaging graphql database agnostic graphql query easy write understand neutral query always return code even query errored query unsuccessful response instead error key associated error message stacktrace however error messaging quite detailed include resolvers refer exact part query fault con learning curve come introducing new tech initial setup time another service graphqlapiserver gql caching done database client level though apollo gql doesnt rely http caching method gql around long enough gain excellent community support rest around established pattern even longer layer graphql apollo top rest architecture making direct database call basic operation description allows begin working graphql apollo top rest architecture proxying existing authserver call except make sense interact database directly simple operation pro risk upfront work well still heavily reduce number initial network request performed setting frontend incremental approach apollo server orchestrate rest request sufficient fulfil query return exactly data requested apollo server proxy existing authserver call incrementally swap authserver api call direct implementation con creates tech debt wont fully integrated finish swapping authserver api call stack universal across fxa well rest nonsettings fxa page payment server refactoring done graphql database agnostic unable graphql subscription database support realtime data full graphql apollo integration direct database call description would extend complex operation routed authserver would directly implemented apollo server pro tech debt later would see performance boost allout dedication approach could open door evaluating database able work graphql subscription quickly pave path move backend mysql something else regional conscious architecture con increased risk well pushing new setting app staging production building setting redesign project already lot moving part incremental approach take ideal existing rest endpoint authserver arent query embed business logic wed duplicate logic graphql test tandem rest make sure dont break anything either side much time needed setup access control auth security already implemented authserver might expensive reinvent additional link setting redesign project jira adr setting redesign new react app graphql doc apollo doc graphql subscription graphql api technical specification doc setting redesign