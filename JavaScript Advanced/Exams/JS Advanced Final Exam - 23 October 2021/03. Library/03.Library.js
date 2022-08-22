describe("library", function() {
    describe("calcPriceOfBook", function() {
        it("Validate it", function() {
            expect(() =>library.calcPriceOfBook(22, "string")).to.throw("Invalid input");
            expect(() =>library.calcPriceOfBook(22, 23)).to.throw("Invalid input");
            expect(() =>library.calcPriceOfBook("22", "23")).to.throw("Invalid input");
        });
        it("Book is old", function() {
            expect(library.calcPriceOfBook("No name", 1980)).to.equal(`Price of No name is 10.00`);
            expect(library.calcPriceOfBook("No name", 1971)).to.equal(`Price of No name is 10.00`);
        });
        it("Book is not old", function() {
            expect(library.calcPriceOfBook("No name", 1994)).to.equal(`Price of No name is 20.00`);
        });
     });
     describe("findBook", function() {
        it("if book length is 0", function() {
            expect(() =>library.findBook([], "string")).to.throw("No books currently available");
        });
        it("if book is not there", function() {
            expect(library.findBook(["Troy", "Life Style", "Torronto"], "string")).to.deep.equal("The book you are looking for is not here!");
        });
        it("if book is there", function() {
            expect(library.findBook(["Troy", "Life Style", "Torronto"], "Troy")).to.deep.equal("We found the book you want.");
        });
});

describe("arrangeTheBooks", function() {
        it("validate it", function() {
            expect(() =>library.arrangeTheBooks("string")).to.throw("Invalid input");
            expect(() =>library.arrangeTheBooks(-5)).to.throw("Invalid input");
            expect(() =>library.arrangeTheBooks(5.2)).to.throw("Invalid input");
        });
        it("if no spacet", function() {
            expect(library.arrangeTheBooks(41)).to.equal("Insufficient space, more shelves need to be purchased.");
        });
        it("it's allright", function() {
            expect(library.arrangeTheBooks(40)).to.equal("Great job, the books are arranged.");
            expect(library.arrangeTheBooks(39)).to.equal("Great job, the books are arranged.");
        });
        });

});