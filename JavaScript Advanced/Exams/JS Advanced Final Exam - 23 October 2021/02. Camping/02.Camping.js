class SummerCamp {
    constructor(organizer, location) {
        this.organizer = organizer;
        this.location = location;
        this.priceForTheCamp = { "child": 150, "student": 300, "collegian": 500 };
        this.listOfParticipants = [];
    }

    registerParticipant(name, condition, money) {
        if (!["child", "student", "collegian"].includes(condition)) {
            throw Error("Unsuccessful registration at the camp.")
        }

        let currentParticipant = SummerCamp.findParticipandByName(name, this.listOfParticipants);
        if (currentParticipant != undefined) {
            return `The ${name} is already registered at the camp.`
        }

        let neededMoney;
        if (condition == 'child') {
            neededMoney = this.priceForTheCamp['child'];
        } else if (condition == 'student') {
            neededMoney = this.priceForTheCamp['student'];
        } else {
            neededMoney = this.priceForTheCamp['collegian']
        }

        if (money < neededMoney) {
            return `The money is not enough to pay the stay at the camp.`
        }

        this.listOfParticipants.push({
            name,
            condition,
            power: 100,
            wins: 0
        })

        return `The ${name} was successfully registered.`
    }

    unregisterParticipant(name) {
        let currentParticipant = SummerCamp.findParticipandByName(name, this.listOfParticipants);

        if (currentParticipant == undefined) {
            throw Error(`The ${name} is not registered in the camp.`)
        }

        let index = this.listOfParticipants.indexOf(currentParticipant);
        this.listOfParticipants.splice(index, 1);

        return `The ${name} removed successfully.`
    }

    timeToPlay(typeOfGame, participant1, participant2) {
        if (typeOfGame == 'WaterBalloonFights') {
            const player1 = SummerCamp.findParticipandByName(participant1, this.listOfParticipants);
            const player2 = SummerCamp.findParticipandByName(participant2, this.listOfParticipants);
            if (player1 == undefined && player2 != undefined) {
                throw Error(`Invalid entered name.`)
            } else if (player1 != undefined && player2 == undefined) {
                throw Error(`Invalid entered name.`)
            } else if (player1 == undefined && player2 == undefined) {
                throw Error(`Invalid entered names.`)
            }

            if (player1.condition != player2.condition) {
                throw Error(`Choose players with equal condition.`);
            }

            if (player1.power == player2.power) {
                return `There is no winner.`
            } else if (player1.power < player2.power) {
                player2.wins += 1;
                return `The ${player2.name} is winner in the game ${typeOfGame}.`;
            } else {
                player1.wins += 1;
                return `The ${player1.name} is winner in the game ${typeOfGame}.`;
            }

        } else if(typeOfGame == 'Battleship'){
            const player1 = SummerCamp.findParticipandByName(participant1, this.listOfParticipants);
            if (player1 == undefined) {
                return Error(`Invalid entered name.`);
            }

            player1.power += 20;
            return `The ${player1.name} successfully completed the game ${typeOfGame}.`;
        }
    }

    toString() {
        let result = [];
        result.push(`${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`)

        let sortedParticipants = this.listOfParticipants.sort((a, b) => b.wins - a.wins);

        for (let p of sortedParticipants) {
            result.push(`${p.name} - ${p.condition} - ${p.power} - ${p.wins}`)
        }

        return result.join('\n');
    }

    static findParticipandByName(name, allParticipants) {
        for (let participant of allParticipants) {
            if (participant.name == name) {
                return participant;
            }
        }
    }
}