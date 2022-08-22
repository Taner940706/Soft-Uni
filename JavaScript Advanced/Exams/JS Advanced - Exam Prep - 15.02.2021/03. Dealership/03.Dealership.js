describe("Dealership", function() {
    describe("newCarCost", function() {
        it("return newcar", function() {
            expect(dealership.newCarCost("lambo",6)).to.equal(6);
        });
        it("return price", function() {
            expect(dealership.newCarCost("Audi A4 B8", 15001)).to.equal(1);
        });
     });
     describe("carEquipment", function() {
        it("happy case", function() {
            expect(dealership.carEquipment(["heated seats", "sliding roof", "sport rims","navigation"],[0, 1, 2])).to.deep.equal(["heated seats", "sliding roof", "sport rims"]);
        });
     });
     describe("euroCategory", function() {
        it("slow", function() {
            expect(dealership.euroCategory(3)).to.equal("Your euro category is low, so there is no discount from the final price!");
        });
        it("fast", function() {
            expect(dealership.euroCategory(4)).to.equal("We have added 5% discount to the final price: 14250.");
            expect(dealership.euroCategory(5)).to.equal("We have added 5% discount to the final price: 14250.");
        });
     });
     
});