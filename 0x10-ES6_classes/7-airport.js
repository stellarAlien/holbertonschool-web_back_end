export default class Airport {
    constructor(name, code) {
        this_name = name;
        this._code = code;
    }

    tosString() {
        return `[${typeof this} ${this._code}]` ;
    }
}