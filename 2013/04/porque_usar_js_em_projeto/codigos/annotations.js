function Human(){
	/* @@-FirstName-
	 * myType:TEXT,
	 * myDefaultValue:John
	 * @@ */
	this.FirstName;
	/* @@-LastName-
	 * myType:TEXT,
	 * myDefaultValue:Doe
	 * @@ */
	this.LastName;

	this.toString = function(){
		return this.FirstName+" "+this.LastName;
	}
}

