describe("bookSelection", function() {
    describe("isGenreSuitable", function() {

        it("Not suitable becouse age is less than 12", function() {
            expect(bookSelection.isGenreSuitable("Thriller",11)).to.equal("Books with Thriller genre are not suitable for kids at 11 age");
            expect(bookSelection.isGenreSuitable("Horror",10)).to.equal("Books with Horror genre are not suitable for kids at 10 age");
        });
        it("suitable if age is greather than 12", function() {
            expect(bookSelection.isGenreSuitable("Thriller",13)).to.equal("Those books are suitable");
            expect(bookSelection.isGenreSuitable("Horror",16)).to.equal("Those books are suitable");
        });

        it("suitable if genre is not Thriller or Horror", function() {
            expect(bookSelection.isGenreSuitable("Family",10)).to.equal("Those books are suitable");
            expect(bookSelection.isGenreSuitable("Action",16)).to.equal("Those books are suitable");
        });
     });

     describe("isItAffordable", function() {

        it("TypeError, uncorrect inputs", function() {
            expect(bookSelection.isItAffordable("string",[1,2,3])).to.throw("Invalid input");
            expect(bookSelection.isItAffordable(function x(){}, {a:1,b:3})).to.throw("Invalid input");
            expect(bookSelection.isItAffordable("string",26)).to.throw("Invalid input");
            expect(bookSelection.isItAffordable(66, "string")).to.throw("Invalid input");
        });
        it("if budget < price", function() {
            expect(bookSelection.isItAffordable(30,13)).to.equal("You don't have enough money");
            expect(bookSelection.isItAffordable(30,3)).to.equal("You don't have enough money");
        });

        it("if budget > price", function() {
            expect(bookSelection.isItAffordable(5,13)).to.equal("Book bought. You have 8$ left");
            expect(bookSelection.isItAffordable(30,33)).to.equal("Book bought. You have 3$ left");
        });
     });

     describe("suitableTitles", function() {

        it("TypeError, uncorrect inputs", function() {
            expect(bookSelection.suitableTitles("string","Thriller")).to.throw("Invalid input");
            expect(bookSelection.suitableTitles([1,2,3], 6)).to.throw("Invalid input");
            expect(bookSelection.suitableTitles([1,2,3], [1,2,3])).to.throw("Invalid input");
            expect(bookSelection.suitableTitles(66, 56)).to.throw("Invalid input");
            expect(bookSelection.suitableTitles("66", "56")).to.throw("Invalid input");
        });
        it("if inputs are correct but genre not in obj", function() {
            expect(bookSelection.suitableTitles([{"genre": "Thriller","title": "Adam i Eva"}],"Horror")).to.deep.equal([]);
            expect(bookSelection.suitableTitles([{"genre": "Sci-fi","title": "Adam i Eva"}],"Family")).to.deep.equal([]);
        });

        it("if genre is correct also inputs are correct", function() {
            expect(bookSelection.suitableTitles([{"genre": "Thriller","title": "Adam i Eva"}],"Thriller")).to.deep.equal(["Adam i Eva"]);
            expect(bookSelection.suitableTitles([{"genre": "Family","title": "Toys"}],"Family")).to.deep.equal(["Toys"]);
        });
     });

     // TODO: …
});