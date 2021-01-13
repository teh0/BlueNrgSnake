export default class WsRoute {
    constructor(eventName, callback) {
        this.eventName = eventName;
        this.callback = callback;
    }

    getEventName() {
        return this.eventName;
    }

    getCallback() {
        return this.callback;
    }
}