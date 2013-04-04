var h = new Human();

console.log(Annotations(Human));
h.FirstName = Annotations(Human)['FirstName']['myDefaultValue']; /*display John*/
h.LastName = Annotations(Human).LastName.myDefaultValue; /*display Doe*/
console.log(h.toString()); /*display John Doe*/

