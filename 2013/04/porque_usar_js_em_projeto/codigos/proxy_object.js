var obj = {
	__noSuchMethod__: function(name, args) {
		print("Method " + name);
	}
};

obj.foo();
