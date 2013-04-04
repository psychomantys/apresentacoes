var obj = {
get foo() {
	return "getter";
},
set foo(value) {
	print("setter: "+value);
}
};
