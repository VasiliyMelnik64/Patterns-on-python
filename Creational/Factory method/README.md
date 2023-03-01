# Use-cases

- if you need flexibility when creating entities.
- when the types and dependencies of the objects that your code must work with are not known in advance.
- the production code can be expanded without touching the main one.
- allow users to extend parts of an existing framework or library.
- saving system resources, reusing already created objects, instead of generating new ones.

#### A factory method can be defined by creating methods that return product objects via abstract types or interfaces. This allows to override the types of generated products in subclasses.
