deprecate response fallback restconfigurableproducer class currently restconfigurableproducer pas payload received target system serializer one fails catch exception fallback original response continue execution done allow certain apis return nondeserializable response still able continue execution either ignoring payload response code enough evaluate something else make evaluator vulnerable guarantee expect something evaluated due fallback present default one endpoint could randomly fail target system decides send back response format expected application decided deprecate response fallback version remove next major version new parameter introduced restconfigurableproducer responseformat define expected response format format passed deserialize function instantiate appropriate visitor example plaintextvisitor could implemented process nonjson response still producing evaluable object default responseformat setup encoding passed consequence order introduce change backwards compatible way new boolean introduced restconfigurableprotocol responsefallback prevent fallback setting false throw exception payload cannot deserialized metadata author andresrey people involved davidcamprubi