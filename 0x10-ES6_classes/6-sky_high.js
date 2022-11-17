import Building from './5-building.js'

export default class SkyHighBuilding extends Building {
    constructor(sqft, floors) {
        super(sqft);
        this.floors = floors;
    }

    get floors() {
        return this._floors;
    }

    set floors(floors) {
        if (typeof floors == 'number') this._floors = floors;
    }

    evacuationWarningMessage() {
        console.log(`Evacuate slowly the NUMBER_OF_FLOORS ${floors}.`);
    }
} 