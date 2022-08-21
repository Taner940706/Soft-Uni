describe("flowerShop", function() {
    describe("calcPriceOfFlowers", function() {

        it("wrong input types", function() {
            expect(flowerShop.calcPriceOfFlowers("string","string","string")).to.throw("Invalid input!");
            expect(flowerShop.calcPriceOfFlowers("22","string","string")).to.throw("Invalid input!");
            expect(flowerShop.calcPriceOfFlowers(22,"string","string")).to.throw("Invalid input!");
            expect(flowerShop.calcPriceOfFlowers("string",22,"string")).to.throw("Invalid input!");
            expect(flowerShop.calcPriceOfFlowers("string","string",22)).to.throw("Invalid input!");
            expect(flowerShop.calcPriceOfFlowers(22,22,"string")).to.throw("Invalid input!");
            expect(flowerShop.calcPriceOfFlowers(22,"string",22)).to.throw("Invalid input!");
        });
        it("all right", function() {
            expect(flowerShop.calcPriceOfFlowers("string",10,10)).to.equal("You need $100.00 to buy string!");
        });
     });

     describe("checkFlowersAvailable", function() {

        it("Flower doesn't exist", function() {
            expect(flowerShop.checkFlowersAvailable("roza",["zumbul","laika"])).to.equal("The roza are sold! You need to purchase more!");
        });
        it("Flower exist", function() {
            expect(flowerShop.checkFlowersAvailable("roza",["roza","laika"])).to.equal("The roza are available!");
            expect(flowerShop.checkFlowersAvailable("roza",["roza","roza"])).to.equal("The roza are available!");
        });
     });

     describe("sellFlowers", function() {

        it("TypeError, uncorrect inputs", function() {
            expect(flowerShop.sellFlowers(23, 5)).to.throw("Invalid input!");
            expect(flowerShop.sellFlowers([1,5,6], "string")).to.throw("Invalid input!");
            expect(flowerShop.sellFlowers("string","banane")).to.throw("Invalid input!");
            expect(flowerShop.sellFlowers("string","33")).to.throw("Invalid input!");
            expect(flowerShop.sellFlowers([1,5,6],-1)).to.throw("Invalid input!");
            expect(flowerShop.sellFlowers([1,5,6],3)).to.throw("Invalid input!");
            expect(flowerShop.sellFlowers([1,5,6],5)).to.throw("Invalid input!");
        });


        it("everything is correct", function() {
            expect(flowerShop.sellFlowers(["roza","zumbul","laika"],2)).to.deep.equal("roza / zumbul");
            expect(flowerShop.sellFlowers(["roza","zumbul","laika"],1)).to.deep.equal("roza / laika");
        });
     });

});