class Card {
    constructor(value) {
        const validValues = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T','Q', 'K', 'A'];
        if (!validValues.includes(value)) {
            throw new Error('Invalid card value');
        }
        this.value = value;
        this.numericalValue = validValues.indexOf(value);
    }
}

class Hand {
    constructor(cards) {
        if (!Array.isArray(cards) || cards.length !== 5) {
            throw new Error('A hand must consist of exactly 5 cards');
        }
        this.cards = [];
        //Create count with 0 on every possible value
        const counts = {J: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0, 7:0, 8:0, 9:0, T:0, Q:0, K:0, A:0}
        //const counts = {};
        let jokers = 0;
        //const counts = {};
        for (let i = 0; i < cards.length; i++) {
            this.cards.push(new Card(cards[i]));
            if(cards[i] === 'J') {
                jokers += 1;
            }
            else {
                counts[cards[i]] = (counts[cards[i]] || 0) + 1;
            }
        }
        
        // Distribute the jokers to maximize the hand value
        while (jokers > 0) {
            let maxKey = Object.keys(counts).reduce((a, b) => counts[a] > counts[b] ? a : b);
            counts[maxKey] += 1;
            jokers -= 1;
        }
        const countValues = Object.values(counts);
        countValues.sort((a, b) => b - a);

        if (countValues[0] === 5) {
            this.value = 7; // Five of a kind
        } else if (countValues[0] === 4) {
            this.value = 6; // Four of a kind
        } else if (countValues[0] === 3 && countValues[1] === 2) {
            this.value = 5; // Full house
        } else if (countValues[0] === 3) {
            this.value = 4; // Three of a kind
        } else if (countValues[0] === 2 && countValues[1] === 2) {
            this.value = 3; // Two pair
        } else if (countValues[0] === 2) {
            this.value = 2; // One pair
        } else {
            this.value = 1; // High card
        }
    }

    isLowerThan(otherHand) {
        // Assuming the cards are sorted in descending order
        if (this.value < otherHand.value) {
            return true;
        } else if (this.value > otherHand.value) {
            return false;
        }
    
        for (let i = 0; i < this.cards.length; i++) {
            if (this.cards[i].numericalValue < otherHand.cards[i].numericalValue) {
                return true;
            } else if (this.cards[i].numericalValue > otherHand.cards[i].numericalValue) {
                return false;
            }
        }
        // If we get here, the hands are equal
        return false;
    }

}

class HandBet {
    constructor(hand, bet) {
        this.hand = hand;
        this.bet = bet;
    }
}

const fs = require('fs');

const data = fs.readFileSync('input.txt', 'utf8');
const lines = data.split('\n');
console.log(lines);
const handBets = [];

for (let line of lines) {
    const [handStr, betStr] = line.split(' ');
    const hand = new Hand(handStr.split(''));
    const bet = parseInt(betStr, 10);
    if(handBets.length === 0) {
        handBets.push(new HandBet(hand, bet));
        //console.log("Adding first hand");
        //console.log(handBets);
        continue;
    }

    // Find the insertion position of the new hand
    let low = 0;
    let high = handBets.length - 1;
    // Binary search to find the insertion position
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);

        if (handBets[mid].hand.isLowerThan(hand)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    // Insert the new element at the correct position
    handBets.splice(low, 0, new HandBet(hand, bet));
    //console.log("Inserted new hand");
    //console.log(handBets);
}

totalWinnings = 0;

for (let i = 0; i < handBets.length; i++) {
    const handBet = handBets[i];
    const winnings = handBet.bet * (i + 1);
    totalWinnings += winnings;
}

console.log(totalWinnings);
