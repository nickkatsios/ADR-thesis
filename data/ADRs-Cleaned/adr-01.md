adr api tech stack november retrospective zooniverse maintains numerous rail apis mostly built three five year ago vary wildly amount attention theyve received gem deprecated unmaintained otherwise generally good idea tyool research necessary modern standardized api functionality solution would meet following requirement crud serialization pagination filtration authentication authorization considered refers different thing ootb rail course sufficient building fullfeatured api however weve come expect certain feature lighten cognitive load app dev dev broke question possibility api format plain straight json representation resource pro straightforward build extra part required con another nonstandard api stable jsonapi spec pro follows proven standard lot dropin stuff thatd manual otherwise con bit learning curve front back end devs rail nonjsonapi mostly ootb rail gear api would simpler initially featureful said dropin gem provide required feature could mean rolling something entirely freeform building internal schema validation system example stack could either auth pundit given across pagination kaminari serialization tojson blueprinter internallydefined json schema filtration ransack custom pro straightforward build focus getting something working overall complexity jsonapi spec con still lot make gem pagination filtration etc another nonstandard api stable apps dip jsonapi spec managing link relationship manually implementing piece spec others new totally bespoke interface seems like movement wrong direction jsonapi spec jsonapi spec jsonapiorg schema standard intends normalize way apis interacted web perfect might even strictly necessary allows code written client gem every piece mentioned top make assumption rail solution exist everywhere spectrum full replacement literally controller code helper deserialize ill get internal difference here upshot pro follows proven standard lot dropin stuff thatd manual otherwise client server side abundant existing documentation knowing something acting client surface bug server code knowing expecting getting learningprofessional development opportunity catch rail world con learning curve potentially overkill project size fastest route functional api said suboptions suboption jsonapiresources httpsjsonapiresourcescom big one space full dropin replacement foralmost everything designed controller literally entirely empty inheriting including gem class boom api give crud everything whether want handle interaction request model pretty much suboption diy jsonapi build stack without magic similar stack gem pundit kaminari ransack include basic jsonapiformatted serialization fastjsonapi seems like there lot churn space lately though record here may seem fine first blush ended vetoing activemodelserializers fully maintenance mode update since mid big one long time several apps readme say look elsewhere jsonapirb confusingly similarly named next one point first alternative however hasnt seen lot activity recently either open since whole section documentation labeled todo suboption jsonapirb httpsgithubcomstasjsonapirb found gem research precisely would suboption loc gem bundle together gem planning primarily ransack fastjsonapi tie together boilerplate code boilerplate validation error handlingformatting getting data tofrom ransack filteringsorting pagination link outcome end day difficult choose jsonapi spec greenfield project balance standardization gadgetiness basic nondry controller one end graphql spec front end devs sortof familiar account existing service sortof implementation gave opportunity rabbit hole bit learn whats discovery surprising activemodelserializers fully deprecated whod guessed mind test drove suboptions jsonapiresources framework sure relatively simple case could handled found getting hung straightforward question wasnt sure magic correctly definitely seemed like overkill wanted accomplish furthermore magic extra required documentation reading would make much difficult onboard someone new work app end decided jsonapirb lean existing popular tech hard stuff fastjsonapi ransack serialization filtersort respectively pretty much everything else stuff implement manually way though see exactly done override necessary there sorcery empty controller simple classesmethods clear extendable even fixed example readme merged couple hour later certainly active said would relatively straightforward process disentangle gem entirely rest app grabbing necessary class lib throwing apps