# TOSCA YAML deserialization using SnakeYAML

The TOSCA YAML files have to be read into a Java model (deserialized) and written from the Java model into files (serialized).

## Considered Alternatives

* [SnakeYAML](https://bitbucket.org/asomov/snakeyaml) writing into intermediate model consisting of default Java types
* SnakeYAML writing into final Java model
* Manual reading

## Decision Outcome

* Chosen Alternative: *SnakeYAML writing into intermediate model consisting of default Java types*

# Pros and Cons of the Alternatives
  
### SnakeYAML writing into intermediate model consisting of default Java types
  
* `+` Basic YAML parsing can be done using SnakeYAML
* `+` TOSCA Java classes can be filled directly
* `-` Programming effort for conversion

### SnakeYAML writing into final Java model

* `+` Established library
* `+` Less error prone 
* `-` SnakeYAML has to be adapted to be able to convert YAML into TOSCA models
* `-` SnakeYAML is not well-prepared for adaptions
* `-` SnakeYAML has issues to write into complex Java classes (which are not Java base types). E.g., List of Maps. - see <https://bitbucket.org/asomov/snakeyaml/issues/361/list-does-not-create-property-objects>
* `-` huge effort, first attempt did not result in a working converter

### Manual reading

* `+` Can write directly into Java model
* `-` Special cases of YAML have to be handled manually
* `-` Error prone

## License

Copyright (c) 2017 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Eclipse Public License 2.0 which is available at
http://www.eclipse.org/legal/epl-2.0, or the Apache Software License 2.0
which is available at https://www.apache.org/licenses/LICENSE-2.0.

SPDX-License-Identifier: EPL-2.0 OR Apache-2.0

