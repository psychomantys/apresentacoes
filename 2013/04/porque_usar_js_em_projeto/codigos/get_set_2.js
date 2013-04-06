> obj.foo
getter
> obj.foo = "bla";
setter: bla
bla
> Object.getOwnPropertyDescriptor(obj, "foo")
{ get: [Function: foo]
, set: [Function: foo]
, enumerable: true
, configurable: true
}
