<template>
    <h1>🐍 Blue NRG Snake</h1>
    <h2>SCORE : {{score}}</h2>
    <canvas ref="canvas" width="400" height="400"></canvas>
    <div>
        <ul>
            <li>Connecté au serveur : <strong>{{connectedToWs ? `Oui (${wsUrl})` : 'Non'}}</strong></li>
            <li>Direction reçue par le serveur : <strong>{{wsDirection}}</strong></li>
        </ul>
    </div>
</template>

<script>
    import WebSocketClient from "../core/WebSocketClient";

    export default {
        name: "Snake",
        data: function () {
            return {
                playerX: 10,
                playerY: 10,
                velocityX: 0,
                velocityY: 0,
                appleX: 15,
                appleY: 15,
                trail: [],
                tail: 5,
                context: null,
                canvas: null,
                gridSize: 20,
                tileCount: 20,
                wsConnection: null,
                connectedToWs: false,
                wsUrl: 'ws://0.0.0.0:8080',
                wsDirection: 'Aucune',
                score: 0,
                colorSnake: 'lime'
            }
        },
        methods: {
            drawBackground() {
                this.context.fillStyle = 'black';
                this.context.fillRect(0, 0, this.canvas.width, this.canvas.height);
            },
            drawSnake() {
                this.playerX += this.velocityX;
                this.playerY += this.velocityY;

                this.context.fillStyle = this.colorSnake;
                for (let i = 0; i<this.trail.length; i++) {
                    this.context.fillRect(
                        this.trail[i].x * this.gridSize,
                        this.trail[i].y * this.gridSize,
                        this.gridSize - 2,
                        this.gridSize - 2
                    );
                    if (this.trail[i].x === this.playerX && this.trail[i].y === this.playerY) {
                        this.tail = 5;
                        this.score = 0;
                    }
                }
                this.trail.push({x: this.playerX, y: this.playerY});
                while (this.trail.length > this.tail) {
                    this.trail.shift();
                }
            },
            drawApple() {
                this.context.fillStyle = 'red';
                this.context.fillRect(
                    this.appleX * this.gridSize,
                    this.appleY * this.gridSize,
                    this.gridSize - 2,
                    this.gridSize - 2
                );
            },
            onEatApple() {
                if (this.appleX === this.playerX && this.appleY === this.playerY) {
                    this.appleX = Math.floor(Math.random() * this.tileCount);
                    this.appleY = Math.floor(Math.random() * this.tileCount);
                    this.tail++;
                    this.score += 10;
                }
            },
            onCollideBorders() {
                if (this.playerX < 0) {
                    this.playerX = this.tileCount - 1;
                }
                if (this.playerX > this.tileCount - 1) {
                    this.playerX = 0
                }
                if (this.playerY < 0) {
                    this.playerY = this.tileCount - 1;
                }
                if (this.playerY > this.tileCount - 1) {
                    this.playerY = 0;
                }
            },
            drawGame(){
                this.drawBackground();
                this.drawSnake();
                this.drawApple();
                this.onEatApple();
                this.onCollideBorders();
            },
            initElements() {
                this.canvas = this.$refs.canvas;
                this.context = this.canvas.getContext('2d');
                this.wsConnection = new WebSocketClient({
                    url: this.wsUrl,
                    onOpen: () => {
                        console.log('connected !');
                        this.connectedToWs = true
                    }
                });
            },
            changeSnakeColor(wsData) {
                const colors = ['red', 'yellow', 'green', 'lime', 'orange'];
                this.colorSnake = colors[Math.floor(Math.random() * colors.length)];
            },
            goSnakeForward(wsData) {
                this.wsDirection = wsData;
                this.velocityX =- 0;
                this.velocityY = -1;
            },
            goSnakeBackward(wsData) {
                this.wsDirection = wsData;
                this.velocityX = 0;
                this.velocityY = 1;
            },
            goSnakeRight(wsData) {
                this.wsDirection = wsData;
                this.velocityX = 1;
                this.velocityY = 0;
            },
            goSnakeLeft(wsData) {
                this.wsDirection = wsData;
                this.velocityX =- 1;
                this.velocityY = 0;
            },
            handleWsEvents() {
                this.wsConnection
                    .on('RIGHT', this.goSnakeRight)
                    .on('LEFT', this.goSnakeLeft)
                    .on('FORWARD', this.goSnakeForward)
                    .on('BACKWARD', this.goSnakeBackward)
                    .on('CHANGE_COLOR', this.changeSnakeColor)
                    .init();
            }
        },
        mounted() {
            this.initElements();
            this.handleWsEvents();
            setInterval(this.drawGame, 1000/5);
        }
    }
</script>

<style scoped>
    canvas {
        width: 500px;
        height: 500px;
    }
</style>