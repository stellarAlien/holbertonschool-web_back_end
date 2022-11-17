import Currency from '3-currency.js'

export default class Pricing {
    constructor(amount, currency) {
        this.amount = amount;
        this.currency = currency;
    }

    get amount() {
        return this._amount;
    }

    get currency() {
        return this._currency;
    }

    set amount(amount) {
        if (typeof amount == 'number') this._amount = amount; 
    }

    set currency(currency) {
        if (currency instanceof Currency) this._currency = currency;
    }

    displayFullPrice() {
        console.log(`${this._amount} ${this._currency_name} (${this._currency_code})`)
    }

    static cnvertPrice(amount, conversionRate) {
        return amount * conversionRate;
        }
} 