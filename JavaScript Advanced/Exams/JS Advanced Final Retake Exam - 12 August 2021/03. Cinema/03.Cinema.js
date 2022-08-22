describe("Tests task Cinema", function() {
    describe("showMovies", function() {
        it("Length of array is zero", function() {
            expect(cinema.showMovies([])).to.equal("There are currently no movies to show.")
        });
        it("Length of array is not zero", function() {
            expect(cinema.showMovies(["King Kong", "The Tomorrow War", "Joker"])).to.equal("King Kong, The Tomorrow War, Joker");
        });
     });
     describe("ticketPrice", function() {
        it("if has properties", function() {
            expect(cinema.ticketPrice("Premiere")).to.equal(12.00)
            expect(cinema.ticketPrice("Discount")).to.equal(5.50)
        });
        it("if not properties", function() {
            expect(()=>cinema.ticketPrice("Premre")).to.throw("Invalid projection type.")
        });
     });
     describe("swapSeatsInHall", function() {
        it("Unsuccessful change", function() {
            expect(cinema.swapSeatsInHall(5)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(20, "string")).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall("23", 5)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall("20", "string")).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(23, 5)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(2, 50)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(0, 5)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(3, 0)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(2, -5)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(-2, 5)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(-3, -5)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(5, 5)).to.equal("Unsuccessful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(21, 22)).to.equal("Unsuccessful change of seats in the hall.")

        });
        it("Successful change", function() {
            expect(cinema.swapSeatsInHall(5,6)).to.equal("Successful change of seats in the hall.")
            expect(cinema.swapSeatsInHall(6,5)).to.equal("Successful change of seats in the hall.")
            
        });
        
     });
});