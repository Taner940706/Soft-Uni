describe('Symetric', () =>{
    it('test 1 not working because not string', ()=>{
        expect(isOddOrEven([1,2,3,3,2,1])).to.be.undefined;
        expect(isOddOrEven(5465)).to.be.undefined;
        expect(isOddOrEven(true)).to.be.undefined;
        expect(isOddOrEven(false)).to.be.undefined;
        expect(isOddOrEven({chislo:2})).to.be.undefined;

    });
    it('test 2 working is even', ()=>{
        expect(isOddOrEven('tanser')).to.equal('even');

    });
    it('test 2 working is odd', ()=>{
        expect(isOddOrEven('taner')).to.equal('odd');

    });

});
