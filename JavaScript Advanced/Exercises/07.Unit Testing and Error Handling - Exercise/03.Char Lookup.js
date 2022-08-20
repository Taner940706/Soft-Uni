describe('Symetric mtfk', () =>{
    it('test 1 not working because not string', ()=>{
        expect(lookupChar([1,2,3,3,2,1],2)).to.be.undefined;
        expect(lookupChar(5465,2)).to.be.undefined;
        expect(lookupChar(true,2)).to.be.undefined;
        expect(lookupChar(false,2)).to.be.undefined;
        expect(lookupChar({chislo:2},2)).to.be.undefined;

    });
    it('test 2 not working because index not integer', ()=>{
        expect(lookupChar("taner",[1,2,3,3,2,1])).to.be.undefined;
        expect(lookupChar("taner",true)).to.be.undefined;
        expect(lookupChar("taner",false)).to.be.undefined;
        expect(lookupChar("taner",{chislo:2})).to.be.undefined;

    });
    it('test 3 not working because index lower than 0', ()=>{
        expect(lookupChar("taner",-1)).to.equal("Incorrect index");

    });
    it('test 4 not working because index bigger than index of string', ()=>{
        expect(lookupChar("taner",8)).to.equal("Incorrect index");
        expect(lookupChar("test", 1.23)).to.equal(undefined);

    });
    it('test 5 working properly', ()=>{
        expect(lookupChar("taner",0)).to.equal("t");
        expect(lookupChar("hello", 3)).to.equal('l');

    });

});