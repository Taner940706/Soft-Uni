(function solve() {

    Array.prototype.skip = function (n) {

        let newArr = [];

        for (let index = n; index < this.length; index++) {

            newArr.push(this[index]);

        }
        return newArr;
    }

    Array.prototype.last = function () {

        return this[this.length - 1];

    }

    Array.prototype.take = function (n) {

        let newArr = [];

        for (let index = 0; index < n; index++) {

            newArr.push(this[index]);

        }
        return newArr;

    }

    Array.prototype.sum = function () {

        let sum = 0;

        for (let index = 0; index < this.length; index++) {

            sum += this[index];

        }
        return sum;

    }

    Array.prototype.average = function () {

        return this.sum() / this.length;
      

    }


}());