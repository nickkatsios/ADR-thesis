splitting object graph code gen serialization discussed paul dub alex black november serialization code generation different come object graph laid generating code lot easier able directly access referenced object traverse graph however object graph serialization object appear multiple place becomes apparent defining constraint single constraint might referring input multiple time also multiple constraint refer multiple input main reason want keep serialization mind want keep code generator language viable serializing graph meant runtime code generation however would easily become problem object identity required equality comparison implementer different language would therefore work graph find identical object would know identity coincidence meant way creating object graph make explicit make work easier two distinct object graph one code generation serialization consequence advantage easier work object graph aligned usecase error prone access direct disadvantage explicitly transform one object graph another want support reading json back also define backwards transformation