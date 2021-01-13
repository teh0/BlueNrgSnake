import WsRoute from "./WsRoute";

export default class WebSocketClient {
    constructor(options = {}) {
        this.url = options.url || 'ws://localhost:8080';
        this.routes = [];
        this.onOpenCallback = options.onOpen || function () {};
        this.onErrorCallback = options.onError || function () {};
    }

    on(eventName, callback) {
        const newRoute = new WsRoute(eventName, callback);

        if (!this.routes.find(route => route.getEventName() === newRoute.getEventName())) {
            this.routes.push(newRoute);
        }

        return this;
    }

    onOpen(callback) {
        this.onOpenCallback = callback;

        return this;
    }

    onError(callback) {
        this.onErrorCallback = callback;

        return this;
    }

    init() {
        const connection = new WebSocket(this.url);
        connection.onmessage = (event) => {
            this.routes.forEach(route => {
                if (event.data === route.getEventName()) {
                    route.getCallback()(event.data);
                }
            });
        };

        connection.onerror = this.onErrorCallback;
        connection.onopen = this.onOpenCallback;

        return connection;
    }
}